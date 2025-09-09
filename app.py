import streamlit as st

st.set_page_config(page_title="LDTA ERJ-145 (reprise)", layout="centered")
st.title("LDTA – Embraer 145 (reprise)")
st.write("Version reprise : tables FLAP 22 (CAT I) incluses. LDTA finale = valeur calculée × 1.15.")

# -----------------------------
# Tables LDTA (reprise)
# - Les blocs complets fournis ici : toutes les combinaisons FLAP 22 pour CAT I (TR/NO TR + ICE/NO ICE).
# - Les autres combinaisons (FLAP 45, CAT II) sont laissées vides (placeholders) et seront remplies ensuite.
# -----------------------------
tables = {
    # ======================
    # CAT I - FLAP 22
    # ======================

    # --- NO ICE ---
    ("CAT I","TR","FLAP 22","NO ICE"): {
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

    ("CAT I","NO TR","FLAP 22","NO ICE"): {
        6: {"REF":1159,"WEIGHT":{"below":-49,"above":53},"ALT":34,
            "TEMP":{"belowISA":-11,"aboveISA":26},
            "WIND":{"head":-24,"tail":127},
            "SLOPE":{"up":-9,"down":192},
            "VAP":148,"REV":None,"OVERWEIGHT":{"per1000kg":149}},
        5: {"REF":1711,"WEIGHT":{"below":-68,"above":69},"ALT":47,
            "TEMP":{"belowISA":-20,"aboveISA":36},
            "WIND":{"head":-40,"tail":205},
            "SLOPE":{"up":-34,"down":307},
            "VAP":234,"REV":None,"OVERWEIGHT":{"per1000kg":149}},
        4: {"REF":1873,"WEIGHT":{"below":-74,"above":75},"ALT":49,
            "TEMP":{"belowISA":-22,"aboveISA":37},
            "WIND":{"head":-45,"tail":229},
            "SLOPE":{"up":-41,"down":328},
            "VAP":240,"REV":None,"OVERWEIGHT":{"per1000kg":149}},
        3: {"REF":2247,"WEIGHT":{"below":-90,"above":91},"ALT":54,
            "TEMP":{"belowISA":-26,"aboveISA":41},
            "WIND":{"head":-54,"tail":276},
            "SLOPE":{"up":-56,"down":387},
            "VAP":257,"REV":None,"OVERWEIGHT":{"per1000kg":149}},
        2: {"REF":3130,"WEIGHT":{"below":-125,"above":126},"ALT":70,
            "TEMP":{"belowISA":-36,"aboveISA":54},
            "WIND":{"head":-83,"tail":426},
            "SLOPE":{"up":-87,"down":574},
            "VAP":326,"REV":None,"OVERWEIGHT":{"per1000kg":149}},
        1: {"REF":4839,"WEIGHT":{"below":-199,"above":200},"ALT":111,
            "TEMP":{"belowISA":-58,"aboveISA":86},
            "WIND":{"head":-153,"tail":757},
            "SLOPE":{"up":-180,"down":1077},
            "VAP":547,"REV":None,"OVERWEIGHT":{"per1000kg":149}},
    },

    # --- ICE ---
    ("CAT I","TR","FLAP 22","ICE"): {
        6: {"REF":1142,"WEIGHT":{"below":-47,"above":49},"ALT":33,
            "TEMP":{"belowISA":-10,"aboveISA":26},
            "WIND":{"head":-22,"tail":117},
            "SLOPE":{"up":-7,"down":184},
            "VAP":127,"REV":197,"OVERWEIGHT":{"per1000kg":114}},
        5: {"REF":1315,"WEIGHT":{"below":-55,"above":56},"ALT":41,
            "TEMP":{"belowISA":-13,"aboveISA":38},
            "WIND":{"head":-27,"tail":163},
            "SLOPE":{"up":-11,"down":227},
            "VAP":152,"REV":485,"OVERWEIGHT":{"per1000kg":114}},
        4: {"REF":1446,"WEIGHT":{"below":-60,"above":61},"ALT":45,
            "TEMP":{"belowISA":-16,"aboveISA":42},
            "WIND":{"head":-32,"tail":189},
            "SLOPE":{"up":-18,"down":264},
            "VAP":160,"REV":621,"OVERWEIGHT":{"per1000kg":114}},
        3: {"REF":1738,"WEIGHT":{"below":-72,"above":73},"ALT":50,
            "TEMP":{"belowISA":-19,"aboveISA":47},
            "WIND":{"head":-42,"tail":236},
            "SLOPE":{"up":-28,"down":348},
            "VAP":184,"REV":789,"OVERWEIGHT":{"per1000kg":114}},
        2: {"REF":2431,"WEIGHT":{"below":-101,"above":102},"ALT":63,
            "TEMP":{"belowISA":-27,"aboveISA":60},
            "WIND":{"head":-64,"tail":351},
            "SLOPE":{"up":-47,"down":524},
            "VAP":264,"REV":1196,"OVERWEIGHT":{"per1000kg":114}},
        1: {"REF":3795,"WEIGHT":{"below":-161,"above":162},"ALT":97,
            "TEMP":{"belowISA":-43,"aboveISA":93},
            "WIND":{"head":-113,"tail":610},
            "SLOPE":{"up":-104,"down":934},
            "VAP":455,"REV":2053,"OVERWEIGHT":{"per1000kg":114}},
    },

    ("CAT I","NO TR","FLAP 22","ICE"): {
        6: {"REF":1239,"WEIGHT":{"below":-52,"above":54},"ALT":36,
            "TEMP":{"belowISA":-12,"aboveISA":28},
            "WIND":{"head":-27,"tail":136},
            "SLOPE":{"up":-11,"down":201},
            "VAP":161,"REV":None,"OVERWEIGHT":{"per1000kg":157}},
        5: {"REF":1832,"WEIGHT":{"below":-72,"above":73},"ALT":49,
            "TEMP":{"belowISA":-21,"aboveISA":41},
            "WIND":{"head":-46,"tail":219},
            "SLOPE":{"up":-37,"down":320},
            "VAP":249,"REV":None,"OVERWEIGHT":{"per1000kg":157}},
        4: {"REF":2012,"WEIGHT":{"below":-79,"above":80},"ALT":52,
            "TEMP":{"belowISA":-24,"aboveISA":45},
            "WIND":{"head":-52,"tail":247},
            "SLOPE":{"up":-44,"down":354},
            "VAP":261,"REV":None,"OVERWEIGHT":{"per1000kg":157}},
        3: {"REF":2416,"WEIGHT":{"below":-96,"above":97},"ALT":57,
            "TEMP":{"belowISA":-28,"aboveISA":50},
            "WIND":{"head":-63,"tail":298},
            "SLOPE":{"up":-59,"down":420},
            "VAP":282,"REV":None,"OVERWEIGHT":{"per1000kg":157}},
        2: {"REF":3387,"WEIGHT":{"below":-137,"above":138},"ALT":75,
            "TEMP":{"belowISA":-40,"aboveISA":66},
            "WIND":{"head":-99,"tail":465},
            "SLOPE":{"up":-93,"down":635},
            "VAP":367,"REV":None,"OVERWEIGHT":{"per1000kg":157}},
        1: {"REF":5228,"WEIGHT":{"below":-214,"above":215},"ALT":117,
            "TEMP":{"belowISA":-65,"aboveISA":101},
            "WIND":{"head":-178,"tail":828},
            "SLOPE":{"up":-192,"down":1197},
            "VAP":619,"REV":None,"OVERWEIGHT":{"per1000kg":157}},
    },

    # ======================
    # CAT I - FLAP 45 (placeholders for now)
    # ======================
    ("CAT I","TR","FLAP 45","NO ICE"): {},
    ("CAT I","NO TR","FLAP 45","NO ICE"): {},
    ("CAT I","TR","FLAP 45","ICE"): {},
    ("CAT I","NO TR","FLAP 45","ICE"): {},

    # ======================
    # CAT II - FLAP 22 & 45 (placeholders for now)
    # ======================
    ("CAT II","TR","FLAP 22","NO ICE"): {},
    ("CAT II","NO TR","FLAP 22","NO ICE"): {},
    ("CAT II","TR","FLAP 22","ICE"): {},
    ("CAT II","NO TR","FLAP 22","ICE"): {},
    ("CAT II","TR","FLAP 45","NO ICE"): {},
    ("CAT II","NO TR","FLAP 45","NO ICE"): {},
    ("CAT II","TR","FLAP 45","ICE"): {},
    ("CAT II","NO TR","FLAP 45","ICE"): {},
}

# -----------------------------
# Fonctions de calcul
# -----------------------------
def get_table(cat, tr, flap, ice):
    key = (cat, "TR" if tr else "NO TR", flap, "ICE" if ice else "NO ICE")
    return tables.get(key)

def compute_ldta(cat, flap, tr_enabled, revs_inop, ice, rwycc,
                 weight, alt_ft, isa_dev, wind_kt, slope_pct, vap_over, overweight_mode):
    table = get_table(cat, tr_enabled, flap, ice)
    if not table or rwycc not in table:
        return None, [f"Configuration non couverte: {cat}, {'TR' if tr_enabled else 'NO TR'}, {flap}, {'ICE' if ice else 'NO ICE'}, RWYCC={rwycc}"]

    row = table[rwycc]
    ref = row["REF"]
    details = [f"REF table: {ref} m"]
    total = float(ref)

    # Poids (standard ou overweight footer)
    delta_1000 = (weight - 18000) / 1000.0
    if overweight_mode and weight > 18000:
        details.append(f"Overweight actif — correction appliquée en pied de page: {row.get('OVERWEIGHT',{}).get('per1000kg','?')} m /1000kg")
    else:
        corr_w = row["WEIGHT"]["below"] * abs(delta_1000) if delta_1000 < 0 else row["WEIGHT"]["above"] * abs(delta_1000)
        total += corr_w
        details.append(f"Poids: {corr_w:+.0f} m (Δ={delta_1000:+.2f}×1000kg)")

    # Altitude
    corr_alt = row["ALT"] * (alt_ft/1000.0)
    total += corr_alt
    details.append(f"Altitude: {corr_alt:+.0f} m")

    # Température (ISA deviation)
    if isa_dev < 0:
        corr_temp = (abs(isa_dev)/5.0) * row["TEMP"]["belowISA"]
    else:
        corr_temp = (abs(isa_dev)/5.0) * row["TEMP"]["aboveISA"]
    total += corr_temp
    details.append(f"T° ISA dev: {corr_temp:+.0f} m (ISA {isa_dev:+.0f}°C)")

    # Vent
    if wind_kt >= 0:
        corr_wind = (wind_kt/5.0) * row["WIND"]["head"]
    else:
        corr_wind = (abs(wind_kt)/5.0) * row["WIND"]["tail"]
    total += corr_wind
    details.append(f"Vent: {corr_wind:+.0f} m ({wind_kt:+.0f} kt)")

    # Pente
    if slope_pct >= 0:
        corr_slope = slope_pct * row["SLOPE"]["up"]
    else:
        corr_slope = abs(slope_pct) * row["SLOPE"]["down"]
    total += corr_slope
    details.append(f"Pente: {corr_slope:+.0f} m ({slope_pct:+.2f}%)")

    # Survitesse (VREF +)
    corr_vap = (vap_over/5.0) * row["VAP"]
    total += corr_vap
    details.append(f"Survitesse: {corr_vap:+.0f} m (VREF+ {vap_over} kt)")

    # Inverseurs INOP
    if tr_enabled and row.get("REV") and revs_inop > 0:
        corr_rev = revs_inop * row["REV"]
        total += corr_rev
        details.append(f"Inverseurs INOP: {corr_rev:+.0f} m ({revs_inop})")

    # Overweight footer (appliquée si choisi)
    if overweight_mode and weight > 18000:
        per1000 = row.get("OVERWEIGHT",{}).get("per1000kg",0)
        corr_ov = per1000 * ((weight-18000)/1000.0)
        total += corr_ov
        details.append(f"Overweight footer: {corr_ov:+.0f} m")

    # Application du facteur réglementaire 1.15
    final = total * 1.15
    details.append("Facteur réglementaire 1.15 appliqué")

    return final, details

# -----------------------------
# Interface Streamlit
# -----------------------------
st.header("Configuration")
col1, col2 = st.columns(2)
with col1:
    cat = st.selectbox("Catégorie", ["CAT I","CAT II"])
    flap = st.selectbox("Volets", ["FLAP 22","FLAP 45"])
    tr_enabled = st.checkbox("Avec inverseurs TR (au moins 1 op.)", value=True)
    revs_inop = st.selectbox("Inverseurs INOP", [0,1,2], index=0)
with col2:
    ice = st.checkbox("Ice accretion (accumulation de glace)", value=False)
    rwycc = st.selectbox("RWYCC (code piste)", [6,5,4,3,2,1], index=2)
    overweight_mode = st.checkbox("Atterrissage > MLW (méthode overweight)", value=False)

st.header("Paramètres avion/piste")
col3, col4 = st.columns(2)
with col3:
    weight = st.number_input("Poids atterrissage (kg)", min_value=10000, max_value=22000, value=18000, step=100)
    alt_ft = st.number_input("Altitude pression (ft)", min_value=-1000, max_value=12000, value=0, step=100)
    isa_dev = st.number_input("ISA deviation (°C, OAT − ISA)", min_value=-40, max_value=60, value=0, step=1)
with col4:
    wind_kt = st.number_input("Vent (kt) (+ face / - arrière)", min_value=-100, max_value=100, value=0, step=1)
    slope_pct = st.number_input("Pente (%) (+ montée / - descente)", min_value=-5.0, max_value=5.0, value=0.0, step=0.1)
    vap_over = st.number_input("Survitesse (VREF +, kt)", min_value=0, max_value=50, value=0, step=1)

if st.button("Calculer LDTA"):
    total, details = compute_ldta(cat, flap, tr_enabled, revs_inop, ice, rwycc,
                                  weight, alt_ft, isa_dev, wind_kt, slope_pct, vap_over, overweight_mode)
    if total is None:
        st.error(details[0])
    else:
        st.success(f"LDTA finale (avec ×1.15): {total:.0f} m")
        with st.expander("Détail des corrections"):
            for d in details:
                st.write("•", d)

st.caption("Remarque : seules les tables FLAP 22 (CAT I) sont actuellement remplies. Les autres combinaisons sont des placeholders et seront complétées sur demande.")