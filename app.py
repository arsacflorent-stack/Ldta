# LDTA ERJ-145 (GRF) – Pythonista (module ui)
# Calcul LDTA basé sur les tables Embraer GP-7924 (Runways Surface Conditions – GRF)
# Entrées: CAT, Flaps, TR, Ice, RWYCC, Poids, Altitude pression, ISA dev, Vent, Pente, VREF+kts, Overweight
# Résultat: LDTA (m) + détail des corrections
# Conçu pour tourner localement dans Pythonista (iOS), sans Streamlit.

import ui

# -----------------------------
# Données tables (ERJ-145)
# -----------------------------
tables = {
    ("CAT I","TR","FLAP 22","NO ICE"): {
        6: {"REF":1068,"WEIGHT":{"below":-45,"above":47},"ALT":32,"TEMP":{"belowISA":-9,"aboveISA":25},
            "WIND":{"head":-21,"tail":112},"SLOPE":{"up":-6,"down":178},"VAP":119,"REV":142,"OVERWEIGHT":{"per1000kg":92,"max_valid":20000}},
        5: {"REF":1230,"WEIGHT":{"below":-57,"above":59},"ALT":44,"TEMP":{"belowISA":-12,"aboveISA":39},
            "WIND":{"head":-26,"tail":165},"SLOPE":{"up":-8,"down":217},"VAP":140,"REV":535,"OVERWEIGHT":{"per1000kg":92,"max_valid":20000}},
        4: {"REF":1347,"WEIGHT":{"below":-58,"above":58},"ALT":43,"TEMP":{"belowISA":-14,"aboveISA":36},
            "WIND":{"head":-29,"tail":145},"SLOPE":{"up":-13,"down":221},"VAP":126,"REV":544,"OVERWEIGHT":{"per1000kg":92,"max_valid":20000}},
        3: {"REF":1437,"WEIGHT":{"below":-63,"above":63},"ALT":47,"TEMP":{"belowISA":-14,"aboveISA":42},
            "WIND":{"head":-31,"tail":164},"SLOPE":{"up":-15,"down":246},"VAP":128,"REV":594,"OVERWEIGHT":{"per1000kg":92,"max_valid":20000}},
        2: {"REF":1567,"WEIGHT":{"below":-75,"above":77},"ALT":63,"TEMP":{"belowISA":-17,"aboveISA":63},
            "WIND":{"head":-38,"tail":246},"SLOPE":{"up":-16,"down":335},"VAP":147,"REV":1011,"OVERWEIGHT":{"per1000kg":92,"max_valid":20000}},
        1: {"REF":1713,"WEIGHT":{"below":-81,"above":81},"ALT":64,"TEMP":{"belowISA":-17,"aboveISA":62},
            "WIND":{"head":-39,"tail":234},"SLOPE":{"up":-25,"down":377},"VAP":141,"REV":1366,"OVERWEIGHT":{"per1000kg":92,"max_valid":20000}},
    },
    ("CAT I","TR","FLAP 22","ICE"): {
        6: {"REF":1145,"WEIGHT":{"below":-49,"above":52},"ALT":34,"TEMP":{"belowISA":-10,"aboveISA":28},
            "WIND":{"head":-22,"tail":117},"SLOPE":{"up":-6,"down":188},"VAP":108,"REV":148,"OVERWEIGHT":{"per1000kg":96,"max_valid":20000}},
        5: {"REF":1321,"WEIGHT":{"below":-61,"above":63},"ALT":48,"TEMP":{"belowISA":-13,"aboveISA":43},
            "WIND":{"head":-27,"tail":170},"SLOPE":{"up":-9,"down":228},"VAP":118,"REV":538,"OVERWEIGHT":{"per1000kg":96,"max_valid":20000}},
        4: {"REF":1432,"WEIGHT":{"below":-62,"above":62},"ALT":46,"TEMP":{"belowISA":-15,"aboveISA":39},
            "WIND":{"head":-29,"tail":150},"SLOPE":{"up":-13,"down":229},"VAP":107,"REV":543,"OVERWEIGHT":{"per1000kg":96,"max_valid":20000}},
        3: {"REF":1524,"WEIGHT":{"below":-67,"above":67},"ALT":51,"TEMP":{"belowISA":-16,"aboveISA":45},
            "WIND":{"head":-31,"tail":168},"SLOPE":{"up":-16,"down":256},"VAP":108,"REV":601,"OVERWEIGHT":{"per1000kg":96,"max_valid":20000}},
        2: {"REF":1661,"WEIGHT":{"below":-80,"above":81},"ALT":67,"TEMP":{"belowISA":-17,"aboveISA":68},
            "WIND":{"head":-37,"tail":250},"SLOPE":{"up":-22,"down":346},"VAP":120,"REV":1024,"OVERWEIGHT":{"per1000kg":96,"max_valid":20000}},
        1: {"REF":1805,"WEIGHT":{"below":-85,"above":86},"ALT":68,"TEMP":{"belowISA":-18,"aboveISA":67},
            "WIND":{"head":-39,"tail":238},"SLOPE":{"up":-25,"down":388},"VAP":117,"REV":1337,"OVERWEIGHT":{"per1000kg":96,"max_valid":20000}},
    },
    ("CAT I","TR","FLAP 45","NO ICE"): {
        6: {"REF":1009,"WEIGHT":{"below":-40,"above":42},"ALT":28,"TEMP":{"belowISA":-10,"aboveISA":22},
            "WIND":{"head":-20,"tail":98},"SLOPE":{"up":-5,"down":106},"VAP":103,"REV":90,"OVERWEIGHT":{"per1000kg":85,"max_valid":20000}},
        5: {"REF":1205,"WEIGHT":{"below":-54,"above":55},"ALT":42,"TEMP":{"belowISA":-13,"aboveISA":36},
            "WIND":{"head":-26,"tail":155},"SLOPE":{"up":-8,"down":146},"VAP":119,"REV":393,"OVERWEIGHT":{"per1000kg":85,"max_valid":20000}},
        4: {"REF":1319,"WEIGHT":{"below":-56,"above":55},"ALT":41,"TEMP":{"belowISA":-14,"aboveISA":35},
            "WIND":{"head":-28,"tail":142},"SLOPE":{"up":-12,"down":153},"VAP":109,"REV":372,"OVERWEIGHT":{"per1000kg":85,"max_valid":20000}},
        3: {"REF":1396,"WEIGHT":{"below":-61,"above":60},"ALT":45,"TEMP":{"belowISA":-15,"aboveISA":39},
            "WIND":{"head":-30,"tail":159},"SLOPE":{"up":-14,"down":174},"VAP":113,"REV":489,"OVERWEIGHT":{"per1000kg":85,"max_valid":20000}},
        2: {"REF":1489,"WEIGHT":{"below":-70,"above":70},"ALT":57,"TEMP":{"belowISA":-16,"aboveISA":54},
            "WIND":{"head":-34,"tail":225},"SLOPE":{"up":-15,"down":236},"VAP":122,"REV":936,"OVERWEIGHT":{"per1000kg":85,"max_valid":20000}},
        1: {"REF":1630,"WEIGHT":{"below":-76,"above":76},"ALT":59,"TEMP":{"belowISA":-17,"aboveISA":56},
            "WIND":{"head":-37,"tail":223},"SLOPE":{"up":-21,"down":285},"VAP":120,"REV":1365,"OVERWEIGHT":{"per1000kg":85,"max_valid":20000}},
    },
    ("CAT I","TR","FLAP 45","ICE"): {
        6: {"REF":1074,"WEIGHT":{"below":-43,"above":45},"ALT":31,"TEMP":{"belowISA":-10,"aboveISA":24},
            "WIND":{"head":-20,"tail":102},"SLOPE":{"up":-5,"down":112},"VAP":105,"REV":99,"OVERWEIGHT":{"per1000kg":88,"max_valid":20000}},
        5: {"REF":1280,"WEIGHT":{"below":-58,"above":58},"ALT":44,"TEMP":{"belowISA":-13,"aboveISA":39},
            "WIND":{"head":-26,"tail":159},"SLOPE":{"up":-8,"down":151},"VAP":117,"REV":417,"OVERWEIGHT":{"per1000kg":88,"max_valid":20000}},
        4: {"REF":1390,"WEIGHT":{"below":-59,"above":58},"ALT":44,"TEMP":{"belowISA":-15,"aboveISA":38},
            "WIND":{"head":-28,"tail":144},"SLOPE":{"up":-12,"down":158},"VAP":109,"REV":393,"OVERWEIGHT":{"per1000kg":88,"max_valid":20000}},
        3: {"REF":1468,"WEIGHT":{"below":-64,"above":63},"ALT":48,"TEMP":{"belowISA":-16,"aboveISA":42},
            "WIND":{"head":-31,"tail":162},"SLOPE":{"up":-14,"down":180},"VAP":112,"REV":500,"OVERWEIGHT":{"per1000kg":88,"max_valid":20000}},
        2: {"REF":1564,"WEIGHT":{"below":-74,"above":74},"ALT":60,"TEMP":{"belowISA":-17,"aboveISA":57},
            "WIND":{"head":-35,"tail":229},"SLOPE":{"up":-15,"down":241},"VAP":120,"REV":900,"OVERWEIGHT":{"per1000kg":88,"max_valid":20000}},
        1: {"REF":1704,"WEIGHT":{"below":-79,"above":79},"ALT":62,"TEMP":{"belowISA":-18,"aboveISA":59},
            "WIND":{"head":-38,"tail":226},"SLOPE":{"up":-22,"down":294},"VAP":114,"REV":1345,"OVERWEIGHT":{"per1000kg":88,"max_valid":20000}},
    },
    ("CAT II","TR","FLAP 22","ANY ICE"): {
        6: {"REF":1145,"WEIGHT":{"below":-49,"above":51},"ALT":34,"TEMP":{"belowISA":-10,"aboveISA":28},
            "WIND":{"head":-22,"tail":117},"SLOPE":{"up":-6,"down":188},"VAP":107,"REV":147,"OVERWEIGHT":{"per1000kg":96,"max_valid":20000}},
        5: {"REF":1321,"WEIGHT":{"below":-62,"above":63},"ALT":48,"TEMP":{"belowISA":-13,"aboveISA":43},
            "WIND":{"head":-27,"tail":170},"SLOPE":{"up":-9,"down":228},"VAP":118,"REV":537,"OVERWEIGHT":{"per1000kg":96,"max_valid":20000}},
        4: {"REF":1432,"WEIGHT":{"below":-61,"above":61},"ALT":46,"TEMP":{"belowISA":-15,"aboveISA":40},
            "WIND":{"head":-29,"tail":149},"SLOPE":{"up":-13,"down":229},"VAP":106,"REV":543,"OVERWEIGHT":{"per1000kg":96,"max_valid":20000}},
        3: {"REF":1523,"WEIGHT":{"below":-68,"above":67},"ALT":51,"TEMP":{"belowISA":-15,"aboveISA":45},
            "WIND":{"head":-31,"tail":168},"SLOPE":{"up":-17,"down":256},"VAP":108,"REV":601,"OVERWEIGHT":{"per1000kg":96,"max_valid":20000}},
        2: {"REF":1661,"WEIGHT":{"below":-80,"above":81},"ALT":67,"TEMP":{"belowISA":-17,"aboveISA":68},
            "WIND":{"head":-37,"tail":250},"SLOPE":{"up":-22,"down":346},"VAP":120,"REV":1023,"OVERWEIGHT":{"per1000kg":96,"max_valid":20000}},
        1: {"REF":1804,"WEIGHT":{"below":-86,"above":85},"ALT":68,"TEMP":{"belowISA":-17,"aboveISA":67},
            "WIND":{"head":-39,"tail":238},"SLOPE":{"up":-25,"down":387},"VAP":117,"REV":1338,"OVERWEIGHT":{"per1000kg":96,"max_valid":20000}},
    },

    # SANS inverseurs
    ("CAT I","NO TR","FLAP 22","NO ICE"): {
        6: {"REF":1159,"WEIGHT":{"below":-49,"above":53},"ALT":34,"TEMP":{"belowISA":-11,"aboveISA":26},
            "WIND":{"head":-24,"tail":127},"SLOPE":{"up":-9,"down":192},"VAP":148,"REV":None,"OVERWEIGHT":{"per1000kg":149,"max_valid":20000}},
        5: {"REF":1472,"WEIGHT":{"below":-73,"above":78},"ALT":56,"TEMP":{"belowISA":-17,"aboveISA":45},
            "WIND":{"head":-34,"tail":232},"SLOPE":{"up":-15,"down":307},"VAP":234,"REV":None,"OVERWEIGHT":{"per1000kg":149,"max_valid":20000}},
        4: {"REF":1711,"WEIGHT":{"below":-68,"above":69},"ALT":47,"TEMP":{"belowISA":-20,"aboveISA":36},
            "WIND":{"head":-40,"tail":205},"SLOPE":{"up":-34,"down":307},"VAP":234,"REV":None,"OVERWEIGHT":{"per1000kg":149,"max_valid":20000}},
        3: {"REF":1949,"WEIGHT":{"below":-76,"above":77},"ALT":54,"TEMP":{"belowISA":-23,"aboveISA":42},
            "WIND":{"head":-48,"tail":214},"SLOPE":{"up":-49,"down":360},"VAP":195,"REV":None,"OVERWEIGHT":{"per1000kg":149,"max_valid":20000}},
        2: {"REF":2498,"WEIGHT":{"below":-134,"above":141},"ALT":100,"TEMP":{"belowISA":-37,"aboveISA":81},
            "WIND":{"head":-71,"tail":447},"SLOPE":{"up":-53,"down":576},"VAP":229,"REV":None,"OVERWEIGHT":{"per1000kg":149,"max_valid":20000}},
        1: {"REF":3038,"WEIGHT":{"below":-96,"above":106},"ALT":79,"TEMP":{"belowISA":-40,"aboveISA":67},
            "WIND":{"head":-93,"tail":372},"SLOPE":{"up":-159,"down":984},"VAP":200,"REV":None,"OVERWEIGHT":{"per1000kg":149,"max_valid":20000}},
    },
    ("CAT I","NO TR","FLAP 22","ICE"): {
        6: {"REF":1254,"WEIGHT":{"below":-54,"above":59},"ALT":37,"TEMP":{"belowISA":-12,"aboveISA":29},
            "WIND":{"head":-25,"tail":135},"SLOPE":{"up":-10,"down":205},"VAP":137,"REV":None,"OVERWEIGHT":{"per1000kg":161,"max_valid":20000}},
        5: {"REF":1614,"WEIGHT":{"below":-82,"above":87},"ALT":62,"TEMP":{"belowISA":-19,"aboveISA":49},
            "WIND":{"head":-36,"tail":243},"SLOPE":{"up":-17,"down":331},"VAP":194,"REV":None,"OVERWEIGHT":{"per1000kg":161,"max_valid":20000}},
        4: {"REF":1841,"WEIGHT":{"below":-74,"above":75},"ALT":51,"TEMP":{"belowISA":-22,"aboveISA":39},
            "WIND":{"head":-41,"tail":233},"SLOPE":{"up":-37,"down":331},"VAP":189,"REV":None,"OVERWEIGHT":{"per1000kg":161,"max_valid":20000}},
        3: {"REF":2091,"WEIGHT":{"below":-83,"above":84},"ALT":58,"TEMP":{"belowISA":-25,"aboveISA":45},
            "WIND":{"head":-49,"tail":220},"SLOPE":{"up":-52,"down":379},"VAP":169,"REV":None,"OVERWEIGHT":{"per1000kg":161,"max_valid":20000}},
        2: {"REF":2708,"WEIGHT":{"below":-145,"above":151},"ALT":106,"TEMP":{"belowISA":-39,"aboveISA":86},
            "WIND":{"head":-78,"tail":422},"SLOPE":{"up":-59,"down":586},"VAP":225,"REV":None,"OVERWEIGHT":{"per1000kg":161,"max_valid":20000}},
        1: {"REF":3223,"WEIGHT":{"below":-105,"above":115},"ALT":85,"TEMP":{"belowISA":-42,"aboveISA":71},
            "WIND":{"head":-95,"tail":378},"SLOPE":{"up":-165,"down":953},"VAP":199,"REV":None,"OVERWEIGHT":{"per1000kg":161,"max_valid":20000}},
    },
    ("CAT I","NO TR","FLAP 45","NO ICE"): {
        6: {"REF":1071,"WEIGHT":{"below":-42,"above":46},"ALT":30,"TEMP":{"belowISA":-11,"aboveISA":22},
            "WIND":{"head":-22,"tail":107},"SLOPE":{"up":-7,"down":115},"VAP":121,"REV":None,"OVERWEIGHT":{"per1000kg":120,"max_valid":20000}},
        5: {"REF":1417,"WEIGHT":{"below":-68,"above":69},"ALT":51,"TEMP":{"belowISA":-16,"aboveISA":40},
            "WIND":{"head":-33,"tail":206},"SLOPE":{"up":-14,"down":209},"VAP":180,"REV":None,"OVERWEIGHT":{"per1000kg":120,"max_valid":20000}},
        4: {"REF":1642,"WEIGHT":{"below":-65,"above":64},"ALT":45,"TEMP":{"belowISA":-20,"aboveISA":35},
            "WIND":{"head":-38,"tail":174},"SLOPE":{"up":-30,"down":211},"VAP":161,"REV":None,"OVERWEIGHT":{"per1000kg":120,"max_valid":20000}},
        3: {"REF":1834,"WEIGHT":{"below":-71,"above":71},"ALT":51,"TEMP":{"belowISA":-22,"aboveISA":39},
            "WIND":{"head":-45,"tail":204},"SLOPE":{"up":-41,"down":268},"VAP":161,"REV":None,"OVERWEIGHT":{"per1000kg":120,"max_valid":20000}},
        2: {"REF":2138,"WEIGHT":{"below":-107,"above":110},"ALT":80,"TEMP":{"belowISA":-27,"aboveISA":64},
            "WIND":{"head":-56,"tail":380},"SLOPE":{"up":-43,"down":460},"VAP":182,"REV":None,"OVERWEIGHT":{"per1000kg":120,"max_valid":20000}},
        1: {"REF":2658,"WEIGHT":{"below":-88,"above":93},"ALT":71,"TEMP":{"belowISA":-33,"aboveISA":58},
            "WIND":{"head":-83,"tail":352},"SLOPE":{"up":-118,"down":975},"VAP":155,"REV":None,"OVERWEIGHT":{"per1000kg":120,"max_valid":20000}},
    },
    ("CAT I","NO TR","FLAP 45","ICE"): {
        6: {"REF":1147,"WEIGHT":{"below":-46,"above":49},"ALT":32,"TEMP":{"belowISA":-11,"aboveISA":24},
            "WIND":{"head":-22,"tail":112},"SLOPE":{"up":-8,"down":121},"VAP":127,"REV":None,"OVERWEIGHT":{"per1000kg":125,"max_valid":20000}},
        5: {"REF":1526,"WEIGHT":{"below":-74,"above":75},"ALT":55,"TEMP":{"belowISA":-18,"aboveISA":43},
            "WIND":{"head":-34,"tail":213},"SLOPE":{"up":-16,"down":222},"VAP":179,"REV":None,"OVERWEIGHT":{"per1000kg":125,"max_valid":20000}},
        4: {"REF":1745,"WEIGHT":{"below":-69,"above":69},"ALT":49,"TEMP":{"belowISA":-21,"aboveISA":37},
            "WIND":{"head":-39,"tail":178},"SLOPE":{"up":-32,"down":221},"VAP":179,"REV":None,"OVERWEIGHT":{"per1000kg":125,"max_valid":20000}},
        3: {"REF":1944,"WEIGHT":{"below":-76,"above":76},"ALT":54,"TEMP":{"belowISA":-24,"aboveISA":42},
            "WIND":{"head":-46,"tail":209},"SLOPE":{"up":-43,"down":278},"VAP":161,"REV":None,"OVERWEIGHT":{"per1000kg":125,"max_valid":20000}},
        2: {"REF":2274,"WEIGHT":{"below":-114,"above":116},"ALT":85,"TEMP":{"belowISA":-29,"aboveISA":68},
            "WIND":{"head":-60,"tail":386},"SLOPE":{"up":-46,"down":428},"VAP":163,"REV":None,"OVERWEIGHT":{"per1000kg":125,"max_valid":20000}},
        1: {"REF":2785,"WEIGHT":{"below":-94,"above":99},"ALT":74,"TEMP":{"belowISA":-34,"aboveISA":61},
            "WIND":{"head":-84,"tail":358},"SLOPE":{"up":-121,"down":958},"VAP":153,"REV":None,"OVERWEIGHT":{"per1000kg":125,"max_valid":20000}},
    },
    ("CAT II","NO TR","FLAP 22","ANY ICE"): {
        6: {"REF":1253,"WEIGHT":{"below":-54,"above":58},"ALT":37,"TEMP":{"belowISA":-12,"aboveISA":29},
            "WIND":{"head":-25,"tail":134},"SLOPE":{"up":-10,"down":204},"VAP":136,"REV":None,"OVERWEIGHT":{"per1000kg":159,"max_valid":20000}},
        5: {"REF":1613,"WEIGHT":{"below":-82,"above":86},"ALT":62,"TEMP":{"belowISA":-19,"aboveISA":49},
            "WIND":{"head":-36,"tail":243},"SLOPE":{"up":-17,"down":331},"VAP":194,"REV":None,"OVERWEIGHT":{"per1000kg":159,"max_valid":20000}},
        4: {"REF":1840,"WEIGHT":{"below":-75,"above":74},"ALT":51,"TEMP":{"belowISA":-20,"aboveISA":39},
            "WIND":{"head":-41,"tail":232},"SLOPE":{"up":-37,"down":331},"VAP":189,"REV":None,"OVERWEIGHT":{"per1000kg":159,"max_valid":20000}},
        3: {"REF":2091,"WEIGHT":{"below":-84,"above":83},"ALT":58,"TEMP":{"belowISA":-24,"aboveISA":45},
            "WIND":{"head":-49,"tail":220},"SLOPE":{"up":-52,"down":378},"VAP":169,"REV":None,"OVERWEIGHT":{"per1000kg":159,"max_valid":20000}},
        2: {"REF":2707,"WEIGHT":{"below":-145,"above":150},"ALT":106,"TEMP":{"belowISA":-39,"aboveISA":86},
            "WIND":{"head":-78,"tail":422},"SLOPE":{"up":-59,"down":586},"VAP":224,"REV":None,"OVERWEIGHT":{"per1000kg":159,"max_valid":20000}},
        1: {"REF":3222,"WEIGHT":{"below":-105,"above":113},"ALT":85,"TEMP":{"belowISA":-42,"aboveISA":71},
            "WIND":{"head":-95,"tail":378},"SLOPE":{"up":-165,"down":953},"VAP":198,"REV":None,"OVERWEIGHT":{"per1000kg":159,"max_valid":20000}},
    },
}

def get_table(cat, tr, flap, ice_state):
    # CAT II + FLAP 22 utilisent "ANY ICE" (tables spécifiques)
    if tr == "TR":
        if cat == "CAT II" and flap == "FLAP 22":
            key = (cat, tr, flap, "ANY ICE")
        else:
            key = (cat, tr, flap, "ICE" if ice_state else "NO ICE")
    else:
        if cat == "CAT II" and flap == "FLAP 22":
            key = (cat, tr, flap, "ANY ICE")
        else:
            key = (cat, tr, flap, "ICE" if ice_state else "NO ICE")
    return tables.get(key), key

# -----------------------------
# Logique de calcul LDTA
# -----------------------------
def compute_ldta(cat, flap, tr_enabled, revs_inop, ice, rwycc, weight, alt_ft, isa_dev, wind_kt, slope_pct, vap_over, overweight_mode):
    tr = "TR" if tr_enabled else "NO TR"
    table, key = get_table(cat, tr, flap, ice)
    if not table or rwycc not in table:
        raise ValueError("Configuration non couverte par les tables.")

    row = table[rwycc]
    ref = row["REF"]
    details = [f"REF table ({key}, RWYCC={rwycc}): {ref} m"]
    total = ref

    # Poids
    delta_1000 = (weight - 18000) / 1000.0
    if overweight_mode and weight > 18000:
        # Pas de correction standard de poids; correction 'overweight' appliquée en fin
        per1000 = row["OVERWEIGHT"]["per1000kg"]
        details.append(f"Overweight (pied de page prévu): +{per1000} m / 1000 kg > 18 000 kg (appliqué en fin).")
    else:
        if delta_1000 < 0:
            corr_w = row["WEIGHT"]["below"] * abs(delta_1000)
        else:
            corr_w = row["WEIGHT"]["above"] * abs(delta_1000)
        total += corr_w
        details.append(f"Poids: {corr_w:+.0f} m (Δ={delta_1000:+.1f}×1000 kg)")

    # Altitude (par 1000 ft)
    alt_1000 = alt_ft / 1000.0
    corr_alt = row["ALT"] * alt_1000
    total += corr_alt
    details.append(f"Altitude: {corr_alt:+.0f} m ({alt_1000:+.1f}×1000 ft)")

    # Température (ISA deviation)
    if isa_dev < 0:
        corr_temp = (abs(isa_dev) / 5.0) * row["TEMP"]["belowISA"]
    else:
        corr_temp = (abs(isa_dev) / 5.0) * row["TEMP"]["aboveISA"]
    total += corr_temp
    details.append(f"Température (ISA dev): {corr_temp:+.0f} m (ISA {isa_dev:+.0f}°C)")

    # Vent (positif = face → head; négatif = arrière → tail)
    if wind_kt >= 0:
        corr_wind = (wind_kt / 5.0) * row["WIND"]["head"]
    else:
        corr_wind = (abs(wind_kt) / 5.0) * row["WIND"]["tail"]
    total += corr_wind
    details.append(f"Vent: {corr_wind:+.0f} m ({wind_kt:+.0f} kt)")

    # Pente (positif = montée → coeff 'up'; négatif = descente → coeff 'down')
    if slope_pct >= 0:
        corr_slope = slope_pct * row["SLOPE"]["up"]
    else:
        corr_slope = abs(slope_pct) * row["SLOPE"]["down"]
    total += corr_slope
    details.append(f"Pente: {corr_slope:+.0f} m ({slope_pct:+.1f} %)")

    # Survitesse au seuil (VREF + …, par tranches de 5 kt)
    corr_vap = (vap_over / 5.0) * row["VAP"]
    total += corr_vap
    details.append(f"Survitesse (VREF +): {corr_vap:+.0f} m ({vap_over} kt)")

    # Inverseurs INOP (si TR)
    if tr == "TR":
        if revs_inop and row["REV"] is not None:
            corr_rev = revs_inop * row["REV"]
            total += corr_rev
            details.append(f"Inverseur(s) INOP: {corr_rev:+.0f} m ({revs_inop} inop)")
        else:
            details.append("Inverseurs: 0 m (tous OP)")

    # Correction overweight en fin (si sélectionnée)
    if overweight_mode and weight > 18000:
        per1000 = row["OVERWEIGHT"]["per1000kg"]
        corr_ov = per1000 * ((weight - 18000) / 1000.0)
        total += corr_ov
        details.append(f"Overweight (fin de calcul): {corr_ov:+.0f} m")

    return total, details

# -----------------------------
# Interface Pythonista (ui)
# -----------------------------
class LDTAView(ui.View):
    def __init__(self):
        super().__init__(name="LDTA – Embraer 145 (GRF)", bg_color="white")
        pad = 10
        x = pad
        y = pad

        # CAT
        self.cat = ui.SegmentedControl(segments=["CAT I","CAT II"])
        self.cat.selected_index = 0
        self.add_label("Catégorie d’approche", x, y); y += 18
        self.place(self.cat, x, y, 240); y += 36

        # Flaps (CAT II = seulement 22)
        self.flap = ui.SegmentedControl(segments=["FLAP 22","FLAP 45"])
        self.flap.selected_index = 0
        self.add_label("Volets à l’atterrissage", x, y); y += 18
        self.place(self.flap, x, y, 240); y += 36

        # TR
        self.tr = ui.SegmentedControl(segments=["Avec TR","Sans TR"])
        self.tr.selected_index = 0
        self.add_label("Inverseurs de poussée", x, y); y += 18
        self.place(self.tr, x, y, 240); y += 36

        # Rev inop
        self.rev_inop = ui.SegmentedControl(segments=["0","1","2"])
        self.rev_inop.selected_index = 0
        self.add_label("Inverseurs INOP (si TR)", x, y); y += 18
        self.place(self.rev_inop, x, y, 240); y += 36

        # Ice
        self.ice = ui.Switch(value=False)
        self.add_label("Ice accretion (accumulation de glace)", x, y); y += 18
        self.place(self.ice, x, y, 60); y += 36

        # RWYCC
        self.rwycc = ui.SegmentedControl(segments=["6","5","4","3","2","1"])
        self.rwycc.selected_index = 2  # par défaut 4
        self.add_label("RWYCC (code piste)", x, y); y += 18
        self.place(self.rwycc, x, y, 300); y += 36

        # Champs numériques
        def tf(ph, default=""):
            t = ui.TextField(placeholder=ph, keyboard_type=ui.KEYBOARD_DECIMAL_PAD, autocorrection=False)
            t.text = default
            return t

        self.weight = tf("Poids atterrissage (kg)", "18000")
        self.alt = tf("Altitude pression (ft)", "0")
        self.isa = tf("ISA dev (°C, OAT − ISA)", "0")
        self.wind = tf("Vent kt (+face / -arrière)", "0")
        self.slope = tf("Pente % (+montée / -descente)", "0")
        self.vap = tf("Survitesse VREF + (kt)", "0")

        for w in [self.weight, self.alt, self.isa, self.wind, self.slope, self.vap]:
            self.place(w, x, y, 300); y += 36

        # Overweight
        self.overweight = ui.Switch(value=False)
        self.add_label("Atterrissage > MLW (méthode 'overweight')", x, y); y += 18
        self.place(self.overweight, x, y, 60); y += 36

        # Bouton calcul
        self.btn = ui.Button(title="Calculer la LDTA")
        self.btn.action = self.calculate
        self.place(self.btn, x, y, 200); y += 44

        # Résultat
        self.result = ui.Label(text="LDTA: — m", font=("<System>", 20))
        self.place(self.result, x, y, 320); y += 32

        # Détail
        self.detail = ui.TextView(editable=False, font=("<System>", 14))
        self.detail.text = "Détail des corrections…"
        self.place(self.detail, x, y, self.width - 2*pad, 220)

        # Callbacks pour adapter l’UI
        self.cat.action = self.update_flap_options
        self.tr.action = self.update_rev_state

        # Init
        self.update_flap_options(None)
        self.update_rev_state(None)

    def add_label(self, text, x, y):
        lbl = ui.Label(text=text, font=("<System>", 14))
        lbl.frame = (x, y, 320, 20)
        self.add_subview(lbl)

    def place(self, v, x, y, w, h=30):
        v.frame = (x, y, w, h)
        self.add_subview(v)

    def update_flap_options(self, sender):
        # CAT II: flaps 22 uniquement
        cat = "CAT I" if self.cat.selected_index == 0 else "CAT II"
        if cat == "CAT II":
            self.flap.segments = ["FLAP 22"]
            self.flap.selected_index = 0
        else:
            self.flap.segments = ["FLAP 22","FLAP 45"]

    def update_rev_state(self, sender):
        # Si "Sans TR", mettre 0 inop et désactiver le contrôle
        tr_enabled = (self.tr.selected_index == 0)
        self.rev_inop.enabled = tr_enabled
        if not tr_enabled:
            self.rev_inop.selected_index = 0

    def _num(self, tf, default=0.0):
        s = (tf.text or "").replace(",", ".").strip()
        if s == "":
            return float(default)
        return float(s)

    def calculate(self, sender):
        try:
            cat = "CAT I" if self.cat.selected_index == 0 else "CAT II"
            flap = self.flap.segments[self.flap.selected_index]
            tr_enabled = (self.tr.selected_index == 0)
            revs_inop = self.rev_inop.selected_index  # 0,1,2
            ice = self.ice.value
            rwycc = int(self.rwycc.segments[self.rwycc.selected_index])

            weight = self._num(self.weight, 18000.0)
            alt_ft = self._num(self.alt, 0.0)
            isa_dev = self._num(self.isa, 0.0)
            wind_kt = self._num(self.wind, 0.0)
            slope_pct = self._num(self.slope, 0.0)
            vap_over = self._num(self.vap, 0.0)
            overweight_mode = self.overweight.value

            total, details = compute_ldta(
                cat, flap, tr_enabled, revs_inop, ice, rwycc,
                weight, alt_ft, isa_dev, wind_kt, slope_pct, vap_over, overweight_mode
            )

            self.result.text = f"LDTA: {total:.0f} m"
            self.detail.text = "• " + "\n• ".join(details) + "\n\nNB: Résultat brut 'LDTA' du GP; appliquer vos marges/SOP si requis."
        except Exception as e:
            self.result.text = "Erreur"
            self.detail.text = f"Erreur: {e}"

# Lancer l’app
v = LDTAView()
# Taille par défaut; Pythonista recadre selon l’écran
v.present("sheet")
