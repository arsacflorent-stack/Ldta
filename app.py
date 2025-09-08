import streamlit as st

st.set_page_config(page_title="LDTA ERJ-145", layout="centered")
st.title("LDTA – Embraer 145")
st.write("Calculateur basé sur le GP-7924. Version en cours de construction.")

# --- Tables LDTA (à compléter progressivement) ---
tables = {
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
    }
}