
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
    
    ("CAT I","TR","FLAP 45","NO ICE"): {
        6: {"REF":1009,"WEIGHT":{"below":-40,"above":42},"ALT":28,
            "TEMP":{"belowISA":-10,"aboveISA":22},
            "WIND":{"head":-20,"tail":98},
            "SLOPE":{"up":-5,"down":106},
            "VAP":103,"REV":90,"OVERWEIGHT":{"per1000kg":85}},
        5: {"REF":1205,"WEIGHT":{"below":-54,"above":55},"ALT":42,
            "TEMP":{"belowISA":-13,"aboveISA":36},
            "WIND":{"head":-26,"tail":155},
            "SLOPE":{"up":-8,"down":146},
            "VAP":119,"REV":393,"OVERWEIGHT":{"per1000kg":85}},
        4: {"REF":1319,"WEIGHT":{"below":-56,"above":55},"ALT":41,
            "TEMP":{"belowISA":-14,"aboveISA":35},
            "WIND":{"head":-28,"tail":142},
            "SLOPE":{"up":-12,"down":153},
            "VAP":109,"REV":372,"OVERWEIGHT":{"per1000kg":85}},
        3: {"REF":1396,"WEIGHT":{"below":-61,"above":60},"ALT":45,
            "TEMP":{"belowISA":-15,"aboveISA":39},
            "WIND":{"head":-30,"tail":159},
            "SLOPE":{"up":-14,"down":174},
            "VAP":113,"REV":489,"OVERWEIGHT":{"per1000kg":85}},
        2: {"REF":1489,"WEIGHT":{"below":-70,"above":70},"ALT":57,
            "TEMP":{"belowISA":-16,"aboveISA":54},
            "WIND":{"head":-34,"tail":225},
            "SLOPE":{"up":-15,"down":236},
            "VAP":122,"REV":936,"OVERWEIGHT":{"per1000kg":85}},
        1: {"REF":1630,"WEIGHT":{"below":-76,"above":76},"ALT":59,
            "TEMP":{"belowISA":-17,"aboveISA":56},
            "WIND":{"head":-37,"tail":223},
            "SLOPE":{"up":-21,"down":285},
            "VAP":120,"REV":1365,"OVERWEIGHT":{"per1000kg":85}},
    },

    ("CAT I","NO TR","FLAP 45","NO ICE"): {
        6: {"REF":1180,"WEIGHT":{"below":-46,"above":49},"ALT":33,
            "TEMP":{"belowISA":-12,"aboveISA":25},
            "WIND":{"head":-23,"tail":115},
            "SLOPE":{"up":-8,"down":170},
            "VAP":125,"REV":None,"OVERWEIGHT":{"per1000kg":130}},
        5: {"REF":1620,"WEIGHT":{"below":-64,"above":66},"ALT":48,
            "TEMP":{"belowISA":-20,"aboveISA":38},
            "WIND":{"head":-39,"tail":200},
            "SLOPE":{"up":-30,"down":260},
            "VAP":198,"REV":None,"OVERWEIGHT":{"per1000kg":130}},
        4: {"REF":1785,"WEIGHT":{"below":-70,"above":71},"ALT":51,
            "TEMP":{"belowISA":-22,"aboveISA":40},
            "WIND":{"head":-44,"tail":230},
            "SLOPE":{"up":-37,"down":300},
            "VAP":210,"REV":None,"OVERWEIGHT":{"per1000kg":130}},
        3: {"REF":2050,"WEIGHT":{"below":-85,"above":86},"ALT":56,
            "TEMP":{"belowISA":-25,"aboveISA":45},
            "WIND":{"head":-52,"tail":280},
            "SLOPE":{"up":-48,"down":360},
            "VAP":225,"REV":None,"OVERWEIGHT":{"per1000kg":130}},
        2: {"REF":2850,"WEIGHT":{"below":-120,"above":121},"ALT":72,
            "TEMP":{"belowISA":-35,"aboveISA":58},
            "WIND":{"head":-80,"tail":420},
            "SLOPE":{"up":-80,"down":540},
            "VAP":300,"REV":None,"OVERWEIGHT":{"per1000kg":130}},
        1: {"REF":4380,"WEIGHT":{"below":-190,"above":192},"ALT":110,
            "TEMP":{"belowISA":-60,"aboveISA":95},
            "WIND":{"head":-150,"tail":750},
            "SLOPE":{"up":-170,"down":1000},
            "VAP":510,"REV":None,"OVERWEIGHT":{"per1000kg":130}},
    },

    ("CAT I","TR","FLAP 45","ICE"): {
        6: {"REF":1105,"WEIGHT":{"below":-44,"above":46},"ALT":31,
            "TEMP":{"belowISA":-11,"aboveISA":24},
            "WIND":{"head":-22,"tail":108},
            "SLOPE":{"up":-7,"down":150},
            "VAP":118,"REV":160,"OVERWEIGHT":{"per1000kg":100}},
        5: {"REF":1310,"WEIGHT":{"below":-58,"above":60},"ALT":44,
            "TEMP":{"belowISA":-16,"aboveISA":36},
            "WIND":{"head":-30,"tail":168},
            "SLOPE":{"up":-12,"down":195},
            "VAP":145,"REV":430,"OVERWEIGHT":{"per1000kg":100}},
        4: {"REF":1430,"WEIGHT":{"below":-61,"above":62},"ALT":47,
            "TEMP":{"belowISA":-18,"aboveISA":40},
            "WIND":{"head":-33,"tail":185},
            "SLOPE":{"up":-16,"down":225},
            "VAP":150,"REV":560,"OVERWEIGHT":{"per1000kg":100}},
        3: {"REF":1515,"WEIGHT":{"below":-66,"above":67},"ALT":50,
            "TEMP":{"belowISA":-20,"aboveISA":46},
            "WIND":{"head":-36,"tail":205},
            "SLOPE":{"up":-19,"down":270},
            "VAP":160,"REV":720,"OVERWEIGHT":{"per1000kg":100}},
        2: {"REF":1670,"WEIGHT":{"below":-85,"above":86},"ALT":64,
            "TEMP":{"belowISA":-30,"aboveISA":60},
            "WIND":{"head":-55,"tail":340},
            "SLOPE":{"up":-35,"down":410},
            "VAP":210,"REV":1100,"OVERWEIGHT":{"per1000kg":100}},
        1: {"REF":2350,"WEIGHT":{"below":-130,"above":132},"ALT":95,
            "TEMP":{"belowISA":-50,"aboveISA":95},
            "WIND":{"head":-120,"tail":680},
            "SLOPE":{"up":-90,"down":820},
            "VAP":370,"REV":1900,"OVERWEIGHT":{"per1000kg":100}},
    },

    ("CAT I","NO TR","FLAP 45","ICE"): {
        6: {"REF":1290,"WEIGHT":{"below":-50,"above":52},"ALT":36,
            "TEMP":{"belowISA":-13,"aboveISA":29},
            "WIND":{"head":-28,"tail":140},
            "SLOPE":{"up":-11,"down":190},
            "VAP":170,"REV":None,"OVERWEIGHT":{"per1000kg":155}},
        5: {"REF":1890,"WEIGHT":{"below":-72,"above":74},"ALT":50,
            "TEMP":{"belowISA":-22,"aboveISA":42},
            "WIND":{"head":-49,"tail":230},
            "SLOPE":{"up":-38,"down":330},
            "VAP":260,"REV":None,"OVERWEIGHT":{"per1000kg":155}},
        4: {"REF":2070,"WEIGHT":{"below":-80,"above":81},"ALT":53,
            "TEMP":{"belowISA":-25,"aboveISA":46},
            "WIND":{"head":-55,"tail":260},
            "SLOPE":{"up":-45,"down":364},
            "VAP":270,"REV":None,"OVERWEIGHT":{"per1000kg":155}},
        3: {"REF":2480,"WEIGHT":{"below":-98,"above":99},"ALT":58,
            "TEMP":{"belowISA":-30,"aboveISA":52},
            "WIND":{"head":-70,"tail":320},
            "SLOPE":{"up":-62,"down":430},
            "VAP":295,"REV":None,"OVERWEIGHT":{"per1000kg":155}},
        2: {"REF":3470,"WEIGHT":{"below":-140,"above":142},"ALT":76,
            "TEMP":{"belowISA":-45,"aboveISA":70},
            "WIND":{"head":-110,"tail":500},
            "SLOPE":{"up":-100,"down":660},
            "VAP":390,"REV":None,"OVERWEIGHT":{"per1000kg":155}},
        1: {"REF":5360,"WEIGHT":{"below":-215,"above":218},"ALT":120,
            "TEMP":{"belowISA":-75,"aboveISA":110},
            "WIND":{"head":-200,"tail":960},
            "SLOPE":{"up":-210,"down":1250},
            "VAP":650,"REV":None,"OVERWEIGHT":{"per1000kg":155}},
    },
    # ======================
    # CAT II - FLAP 22 & 45 (placeholders for now)
    # ======================
        ("CAT II","TR","FLAP 22","NO ICE"): {
        6: {"REF":1120,"WEIGHT":{"below":-46,"above":48},"ALT":33,
            "TEMP":{"belowISA":-10,"aboveISA":26},
            "WIND":{"head":-22,"tail":120},
            "SLOPE":{"up":-7,"down":180},
            "VAP":125,"REV":150,"OVERWEIGHT":{"per1000kg":95}},
        5: {"REF":1300,"WEIGHT":{"below":-55,"above":57},"ALT":45,
            "TEMP":{"belowISA":-14,"aboveISA":38},
            "WIND":{"head":-28,"tail":175},
            "SLOPE":{"up":-12,"down":225},
            "VAP":145,"REV":520,"OVERWEIGHT":{"per1000kg":95}},
        4: {"REF":1420,"WEIGHT":{"below":-60,"above":61},"ALT":47,
            "TEMP":{"belowISA":-16,"aboveISA":42},
            "WIND":{"head":-32,"tail":200},
            "SLOPE":{"up":-17,"down":260},
            "VAP":155,"REV":600,"OVERWEIGHT":{"per1000kg":95}},
        3: {"REF":1720,"WEIGHT":{"below":-72,"above":74},"ALT":52,
            "TEMP":{"belowISA":-20,"aboveISA":48},
            "WIND":{"head":-42,"tail":250},
            "SLOPE":{"up":-25,"down":330},
            "VAP":175,"REV":780,"OVERWEIGHT":{"per1000kg":95}},
        2: {"REF":2400,"WEIGHT":{"below":-102,"above":104},"ALT":65,
            "TEMP":{"belowISA":-30,"aboveISA":62},
            "WIND":{"head":-65,"tail":370},
            "SLOPE":{"up":-45,"down":520},
            "VAP":255,"REV":1200,"OVERWEIGHT":{"per1000kg":95}},
        1: {"REF":3650,"WEIGHT":{"below":-160,"above":163},"ALT":100,
            "TEMP":{"belowISA":-50,"aboveISA":95},
            "WIND":{"head":-115,"tail":700},
            "SLOPE":{"up":-110,"down":900},
            "VAP":430,"REV":2100,"OVERWEIGHT":{"per1000kg":95}},
    },

    ("CAT II","NO TR","FLAP 22","NO ICE"): {
        6: {"REF":1220,"WEIGHT":{"below":-50,"above":52},"ALT":35,
            "TEMP":{"belowISA":-12,"aboveISA":28},
            "WIND":{"head":-25,"tail":135},
            "SLOPE":{"up":-10,"down":200},
            "VAP":160,"REV":None,"OVERWEIGHT":{"per1000kg":150}},
        5: {"REF":1800,"WEIGHT":{"below":-70,"above":72},"ALT":50,
            "TEMP":{"belowISA":-22,"aboveISA":42},
            "WIND":{"head":-48,"tail":220},
            "SLOPE":{"up":-36,"down":325},
            "VAP":245,"REV":None,"OVERWEIGHT":{"per1000kg":150}},
        4: {"REF":1980,"WEIGHT":{"below":-78,"above":80},"ALT":53,
            "TEMP":{"belowISA":-25,"aboveISA":46},
            "WIND":{"head":-55,"tail":250},
            "SLOPE":{"up":-43,"down":360},
            "VAP":260,"REV":None,"OVERWEIGHT":{"per1000kg":150}},
        3: {"REF":2400,"WEIGHT":{"below":-95,"above":97},"ALT":58,
            "TEMP":{"belowISA":-30,"aboveISA":52},
            "WIND":{"head":-65,"tail":310},
            "SLOPE":{"up":-58,"down":420},
            "VAP":285,"REV":None,"OVERWEIGHT":{"per1000kg":150}},
        2: {"REF":3400,"WEIGHT":{"below":-138,"above":140},"ALT":77,
            "TEMP":{"belowISA":-42,"aboveISA":70},
            "WIND":{"head":-105,"tail":500},
            "SLOPE":{"up":-95,"down":640},
            "VAP":380,"REV":None,"OVERWEIGHT":{"per1000kg":150}},
        1: {"REF":5300,"WEIGHT":{"below":-215,"above":218},"ALT":120,
            "TEMP":{"belowISA":-70,"aboveISA":110},
            "WIND":{"head":-200,"tail":950},
            "SLOPE":{"up":-200,"down":1250},
            "VAP":640,"REV":None,"OVERWEIGHT":{"per1000kg":150}},
    },

    ("CAT II","TR","FLAP 22","ICE"): {
        6: {"REF":1200,"WEIGHT":{"below":-48,"above":50},"ALT":34,
            "TEMP":{"belowISA":-11,"aboveISA":27},
            "WIND":{"head":-24,"tail":125},
            "SLOPE":{"up":-8,"down":185},
            "VAP":135,"REV":210,"OVERWEIGHT":{"per1000kg":115}},
        5: {"REF":1380,"WEIGHT":{"below":-58,"above":60},"ALT":43,
            "TEMP":{"belowISA":-16,"aboveISA":39},
            "WIND":{"head":-30,"tail":170},
            "SLOPE":{"up":-14,"down":240},
            "VAP":160,"REV":500,"OVERWEIGHT":{"per1000kg":115}},
        4: {"REF":1520,"WEIGHT":{"below":-62,"above":64},"ALT":47,
            "TEMP":{"belowISA":-18,"aboveISA":44},
            "WIND":{"head":-34,"tail":195},
            "SLOPE":{"up":-20,"down":275},
            "VAP":175,"REV":640,"OVERWEIGHT":{"per1000kg":115}},
        3: {"REF":1820,"WEIGHT":{"below":-74,"above":76},"ALT":52,
            "TEMP":{"belowISA":-22,"aboveISA":50},
            "WIND":{"head":-45,"tail":245},
            "SLOPE":{"up":-30,"down":360},
            "VAP":195,"REV":820,"OVERWEIGHT":{"per1000kg":115}},
        2: {"REF":2520,"WEIGHT":{"below":-105,"above":108},"ALT":66,
            "TEMP":{"belowISA":-32,"aboveISA":65},
            "WIND":{"head":-70,"tail":380},
            "SLOPE":{"up":-50,"down":550},
            "VAP":280,"REV":1250,"OVERWEIGHT":{"per1000kg":115}},
        1: {"REF":3900,"WEIGHT":{"below":-165,"above":168},"ALT":100,
            "TEMP":{"belowISA":-55,"aboveISA":100},
            "WIND":{"head":-125,"tail":700},
            "SLOPE":{"up":-120,"down":980},
            "VAP":470,"REV":2100,"OVERWEIGHT":{"per1000kg":115}},
    },

    ("CAT II","NO TR","FLAP 22","ICE"): {
        6: {"REF":1300,"WEIGHT":{"below":-53,"above":55},"ALT":36,
            "TEMP":{"belowISA":-13,"aboveISA":29},
            "WIND":{"head":-28,"tail":140},
            "SLOPE":{"up":-12,"down":210},
            "VAP":165,"REV":None,"OVERWEIGHT":{"per1000kg":160}},
        5: {"REF":1900,"WEIGHT":{"below":-74,"above":76},"ALT":50,
            "TEMP":{"belowISA":-22,"aboveISA":42},
            "WIND":{"head":-50,"tail":230},
            "SLOPE":{"up":-40,"down":340},
            "VAP":255,"REV":None,"OVERWEIGHT":{"per1000kg":160}},
        4: {"REF":2080,"WEIGHT":{"below":-82,"above":84},"ALT":54,
            "TEMP":{"belowISA":-26,"aboveISA":48},
            "WIND":{"head":-58,"tail":260},
            "SLOPE":{"up":-48,"down":375},
            "VAP":270,"REV":None,"OVERWEIGHT":{"per1000kg":160}},
        3: {"REF":2500,"WEIGHT":{"below":-100,"above":102},"ALT":60,
            "TEMP":{"belowISA":-32,"aboveISA":55},
            "WIND":{"head":-70,"tail":320},
            "SLOPE":{"up":-65,"down":450},
            "VAP":300,"REV":None,"OVERWEIGHT":{"per1000kg":160}},
        2: {"REF":3520,"WEIGHT":{"below":-145,"above":147},"ALT":78,
            "TEMP":{"belowISA":-45,"aboveISA":72},
            "WIND":{"head":-110,"tail":510},
            "SLOPE":{"up":-100,"down":670},
            "VAP":400,"REV":None,"OVERWEIGHT":{"per1000kg":160}},
        1: {"REF":5460,"WEIGHT":{"below":-220,"above":223},"ALT":122,
            "TEMP":{"belowISA":-75,"aboveISA":115},
            "WIND":{"head":-210,"tail":980},
            "SLOPE":{"up":-220,"down":1280},
            "VAP":670,"REV":None,"OVERWEIGHT":{"per1000kg":160}},
    },
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