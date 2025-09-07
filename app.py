import streamlit as st

# -----------------------------
# Exemple de tables LDTA (GP-7924 ERJ-145)
# -----------------------------
tables = {
    ("CAT I","TR","FLAP 22","NO ICE"): {
        6: {"REF":1068,"WEIGHT":{"below":-45,"above":47},"ALT":32,
            "TEMP":{"belowISA":-9,"aboveISA":25},
            "WIND":{"head":-21,"tail":112},
            "SLOPE":{"up":-6,"down":178},
            "VAP":119,"REV":142},
        5: {"REF":1230,"WEIGHT":{"below":-57,"above":59},"ALT":44,
            "TEMP":{"belowISA":-12,"aboveISA":39},
            "WIND":{"head":-26,"tail":165},
            "SLOPE":{"up":-8,"down":217},
            "VAP":140,"REV":535},
        # ⚠️ compléter avec toutes les lignes du manuel GP-7924
    },
    # ⚠️ compléter aussi les autres configurations CAT/FLAP/TR/ICE
}

def get_table(cat, tr, flap, ice_state):
    if tr == "TR":
        key = (cat, tr, flap, "ICE" if ice_state else "NO ICE")
    else:
        key = (cat, "NO TR", flap, "ICE" if ice_state else "NO ICE")
    return tables.get(key)

def compute_ldta(cat, flap, tr_enabled, revs_inop, ice, rwycc,
                 weight, alt_ft, isa_dev, wind_kt, slope_pct, vap_over):
    tr = "TR" if tr_enabled else "NO TR"
    table = get_table(cat, tr, flap, ice)
    if not table or rwycc not in table:
        return None, ["Configuration non couverte"]

    row = table[rwycc]
    ref = row["REF"]
    details = [f"REF table: {ref} m"]
    total = ref

    # Correction poids
    delta_1000 = (weight - 18000) / 1000.0
    if delta_1000 < 0:
        corr_w = row["WEIGHT"]["below"] * abs(delta_1000)
    else:
        corr_w = row["WEIGHT"]["above"] * abs(delta_1000)
    total += corr_w
    details.append(f"Poids: {corr_w:+.0f} m")

    # Correction altitude
    alt_1000 = alt_ft / 1000.0
    corr_alt = row["ALT"] * alt_1000
    total += corr_alt
    details.append(f"Altitude: {corr_alt:+.0f} m")

    # Correction température (ISA deviation)
    if isa_dev < 0:
        corr_temp = (abs(isa_dev) / 5.0) * row["TEMP"]["belowISA"]
    else:
        corr_temp = (abs(isa_dev) / 5.0) * row["TEMP"]["aboveISA"]
    total += corr_temp
    details.append(f"T° ISA dev: {corr_temp:+.0f} m")

    # Correction vent
    if wind_kt >= 0:
        corr_wind = (wind_kt / 5.0) * row["WIND"]["head"]
    else:
        corr_wind = (abs(wind_kt) / 5.0) * row["WIND"]["tail"]
    total += corr_wind
    details.append(f"Vent: {corr_wind:+.0f} m")

    # Correction pente
    if slope_pct >= 0:
        corr_slope = slope_pct * row["SLOPE"]["up"]
    else:
        corr_slope = abs(slope_pct) * row["SLOPE"]["down"]
    total += corr_slope
    details.append(f"Pente: {corr_slope:+.0f} m")

    # Correction survitesse
    corr_vap = (vap_over / 5.0) * row["VAP"]
    total += corr_vap
    details.append(f"Survitesse: {corr_vap:+.0f} m")

    # Correction inverseurs inop
    if tr == "TR" and row["REV"] is not None and revs_inop > 0:
        corr_rev = revs_inop * row["REV"]
        total += corr_rev
        details.append(f"Inverseurs INOP: {corr_rev:+.0f} m")

    # Application du facteur réglementaire 1.15
    final = total * 1.15
    details.append("Facteur réglementaire 1.15 appliqué")

    return final, details

# -----------------------------
# Interface Streamlit
# -----------------------------
st.title("LDTA – Embraer 145 (GRF)")
st.write("Calculateur de LDTA basé sur les tables GP-7924 (Runway Condition Assessment Matrix)")

# Sélections config
cat = st.selectbox("Catégorie d’approche", ["CAT I","CAT II"])
flap = st.selectbox("Volets", ["FLAP 22","FLAP 45"])
tr_enabled = st.checkbox("Avec inverseurs TR", value=True)
revs_inop = st.selectbox("Inverseurs INOP", [0,1,2])
ice = st.checkbox("Ice accretion (accumulation de glace)", value=False)
rwycc = st.selectbox("RWYCC (code piste)", [6,5,4,3,2,1])

# Entrées numériques
weight = st.number_input("Poids atterrissage (kg)", 15000, 22000, 18000)
alt_ft = st.number_input("Altitude pression (ft)", 0, 10000, 0)
isa_dev = st.number_input("ISA dev (°C, OAT−ISA)", -30, 30, 0)
wind_kt = st.number_input("Vent (kt, +face / -arrière)", -50, 50, 0)
slope_pct = st.number_input("Pente % (+montée / -descente)", -3.0, 3.0, 0.0)
vap_over = st.number_input("Survitesse VREF+ (kt)", 0, 20, 0)

# Calcul
if st.button("Calculer LDTA"):
    total, details = compute_ldta(cat, flap, tr_enabled, revs_inop, ice,
                                  rwycc, weight, alt_ft, isa_dev, wind_kt, slope_pct, vap_over)
    if total is None:
        st.error("⚠️ Configuration non couverte par les tables")
    else:
        st.success(f"LDTA (avec marge 1.15): {total:.0f} m")
        with st.expander("Détail des corrections"):
            for d in details:
                st.write("•", d)