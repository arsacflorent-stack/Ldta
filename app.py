import streamlit as st

st.set_page_config(page_title="LDTA ERJ-145", layout="centered")
st.title("LDTA – Embraer 145")
st.write("Calculateur basé sur le GP-7924. Version de test (tables partielles).")

# --- Tables LDTA (exemple à compléter plus tard avec toutes les configurations) ---
tables = ("CAT I","TR","FLAP 22","NO ICE"): {
    6: {"REF":1068,"WEIGHT":{"below":-45,"above":47},"ALT":32,
        "TEMP":{"belowISA":-9,"aboveISA":25},
        "WIND":{"head":-21,"tail":112},
        "SLOPE":{"up":-6,"down":178},
        "VAP":119,"REV":142,"OVERWEIGHT":{"per1000kg":92}},
    5: {"REF":1230,"WEIGHT":{"below":-57,"above":59},"ALT":44,
        "TEMP":{"belowISA":-12,"aboveISA":39},
        "WIND":{"head":-26,"tail":165},
        "SLOPE":{"up":-8,"down":217},
        "VAP":140,"REV":535,"OVERWEIGHT":{"per1000kg":92}},
    4: {"REF":1347,"WEIGHT":{"below":-58,"above":58},"ALT":43,
        "TEMP":{"belowISA":-14,"aboveISA":36},
        "WIND":{"head":-29,"tail":145},
        "SLOPE":{"up":-13,"down":221},
        "VAP":126,"REV":544,"OVERWEIGHT":{"per1000kg":92}},
    3: {"REF":1616,"WEIGHT":{"below":-70,"above":71},"ALT":47,
        "TEMP":{"belowISA":-16,"aboveISA":41},
        "WIND":{"head":-37,"tail":186},
        "SLOPE":{"up":-19,"down":273},
        "VAP":142,"REV":663,"OVERWEIGHT":{"per1000kg":92}},
    2: {"REF":2269,"WEIGHT":{"below":-97,"above":98},"ALT":59,
        "TEMP":{"belowISA":-22,"aboveISA":52},
        "WIND":{"head":-55,"tail":276},
        "SLOPE":{"up":-29,"down":420},
        "VAP":198,"REV":970,"OVERWEIGHT":{"per1000kg":92}},
    1: {"REF":3519,"WEIGHT":{"below":-150,"above":151},"ALT":91,
        "TEMP":{"belowISA":-36,"aboveISA":80},
        "WIND":{"head":-96,"tail":492},
        "SLOPE":{"up":-58,"down":769},
        "VAP":344,"REV":1706,"OVERWEIGHT":{"per1000kg":92}},
},

# --- Fonctions utilitaires ---
def get_table(cat, tr, flap, ice):
    key = (cat, "TR" if tr else "NO TR", flap, "ICE" if ice else "NO ICE")
    return tables.get(key)

def compute_ldta(cat, flap, tr_enabled, revs_inop, ice, rwycc,
                 weight, alt_ft, isa_dev, wind_kt, slope_pct, vap_over, overweight_mode):
    table = get_table(cat, tr_enabled, flap, ice)
    if not table or rwycc not in table:
        return None, ["Configuration non couverte par les tables"]

    row = table[rwycc]
    ref = row["REF"]
    details = [f"REF table: {ref} m"]
    total = float(ref)

    # Poids
    delta_1000 = (weight - 18000) / 1000.0
    if overweight_mode and weight > 18000:
        details.append("Overweight: correction appliquée plus bas")
    else:
        corr_w = row["WEIGHT"]["below"] * abs(delta_1000) if delta_1000 < 0 else row["WEIGHT"]["above"] * abs(delta_1000)
        total += corr_w
        details.append(f"Poids: {corr_w:+.0f} m")

    # Altitude
    corr_alt = row["ALT"] * (alt_ft/1000.0)
    total += corr_alt
    details.append(f"Altitude: {corr_alt:+.0f} m")

    # Température
    if isa_dev < 0:
        corr_temp = (abs(isa_dev)/5.0) * row["TEMP"]["belowISA"]
    else:
        corr_temp = (abs(isa_dev)/5.0) * row["TEMP"]["aboveISA"]
    total += corr_temp
    details.append(f"T° ISA dev: {corr_temp:+.0f} m")

    # Vent
    if wind_kt >= 0:
        corr_wind = (wind_kt/5.0) * row["WIND"]["head"]
    else:
        corr_wind = (abs(wind_kt)/5.0) * row["WIND"]["tail"]
    total += corr_wind
    details.append(f"Vent: {corr_wind:+.0f} m")

    # Pente
    if slope_pct >= 0:
        corr_slope = slope_pct * row["SLOPE"]["up"]
    else:
        corr_slope = abs(slope_pct) * row["SLOPE"]["down"]
    total += corr_slope
    details.append(f"Pente: {corr_slope:+.0f} m")

    # Survitesse
    corr_vap = (vap_over/5.0) * row["VAP"]
    total += corr_vap
    details.append(f"Survitesse: {corr_vap:+.0f} m")

    # Inverseurs inop
    if tr_enabled and row.get("REV") and revs_inop > 0:
        corr_rev = revs_inop * row["REV"]
        total += corr_rev
        details.append(f"Inverseurs INOP: {corr_rev:+.0f} m")

    # Overweight
    if overweight_mode and weight > 18000:
        per1000 = row.get("OVERWEIGHT",{}).get("per1000kg",0)
        corr_ov = per1000 * ((weight-18000)/1000.0)
        total += corr_ov
        details.append(f"Overweight: {corr_ov:+.0f} m")

    # Facteur 1.15
    final = total * 1.15
    details.append("Facteur réglementaire 1.15 appliqué")

    return final, details

# --- Interface Streamlit ---
st.header("Configuration")
cat = st.selectbox("Catégorie", ["CAT I","CAT II"])
flap = st.selectbox("Volets", ["FLAP 22","FLAP 45"])
tr_enabled = st.checkbox("Avec inverseurs TR", value=True)
revs_inop = st.selectbox("Inverseurs INOP", [0,1,2])
ice = st.checkbox("Ice accretion", value=False)
rwycc = st.selectbox("RWYCC", [6,5,4,3,2,1])
overweight_mode = st.checkbox("Méthode Overweight", value=False)

st.header("Données avion/piste")
weight = st.number_input("Poids atterrissage (kg)", 15000, 22000, 18000, step=100)
alt_ft = st.number_input("Altitude pression (ft)", -1000, 12000, 0, step=100)
isa_dev = st.number_input("ISA deviation (°C)", -40, 40, 0)
wind_kt = st.number_input("Vent (kt, +face / -arrière)", -50, 50, 0)
slope_pct = st.number_input("Pente (%)", -5.0, 5.0, 0.0, step=0.1)
vap_over = st.number_input("Survitesse VREF+ (kt)", 0, 20, 0)

if st.button("Calculer LDTA"):
    total, details = compute_ldta(cat, flap, tr_enabled, revs_inop, ice, rwycc,
                                  weight, alt_ft, isa_dev, wind_kt, slope_pct, vap_over, overweight_mode)
    if total is None:
        st.error("⚠️ Config non couverte")
    else:
        st.success(f"LDTA (avec 1.15): {total:.0f} m")
        with st.expander("Détail des corrections"):
            for d in details:
                st.write("•", d)