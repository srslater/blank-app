import streamlit as st

# List of items to confirm
items = [
    "MAIN FLOOR TILE",
    "SHOWER PAN TILE",
    "SHOWER WALL TILE",
    "BULLNOSE TILE",
    "ACCENT / LINER TILE",
    "NICHE",
    "CABINET",
    "FILLER",
    "SCRIBE",
    "TOE KICK",
    "CABINET HARDWARE KNOBS – PULLS –",
    "MEDICINE CABINET",
    "COUNTERTOP (SF)",
    "FABRICATION (SF)",
    "EDGE DETAIL (LINEAR INCHES)",
    "BOWL CUT OUT",
    "SIDE SPLASH",
    "SINK",
    "SINK FAUCET",
    "SINK VALVE *9000 VALVE IF MOEN",
    "SHOWER PAN",
    "SHOWER DRAIN",
    "SHOWER ENCLOSURE SLIDER OR FRAMELESS DOOR OR PANEL",
    "SHOWER GLASS CLEAR OR OBSCURE",
    "SHOWER HARDWARE (DPULL OR TOWEL BAR)",
    "CORNER SHOWER BENCH",
    "SHOWER SET",
    "SHOWER VALVE",
    "SHOWERHEAD *IF NOT PART OF THE SET*",
    "HAND SHOWER",
    "SUPPLY ELBOW",
    "HOSE",
    "BRACKET",
    "SHOWER ARM AND FLANGE",
    "DIVERTER TRIM *IF THERE IS A SEPARATE HANDSHOWER*",
    "DIVERTER VALVE",
    "TUB TRIM & VALVE *IF THERE IS A SEPARATE TUB*",
    "TUB",
    "TUB FAUCET/SPOUT *IF NOT PART OF THE SET*",
    "TUB WASTE OVERFLOW",
    "SHOWER CURTAIN ROD",
    "TOILET",
    "TOILET SEAT",
    "LIGHT FIXTURE / SCONCES",
    "RECESSED CANS/ CONDO CANS",
    "EXHAUST FAN & SWITCH",
    "WINDOW (SIZE, GLASS TYPE, FRAME COLOR)",
    "MIRROR",
    "DOOR / DOOR FRAME / DOOR HARDWARE",
    "TOWEL BAR",
    "TOWEL RING",
    "ROBE HOOK",
    "TP HOLDER",
    "GRAB BAR",
]

st.title("Project Item Confirmation Checklist")
st.write("Please confirm each item and add any necessary notes. All items must be confirmed before final confirmation is allowed.")

# We will store the confirmation states and notes in session state so they persist during interaction
if "confirmations" not in st.session_state:
    st.session_state.confirmations = {item: {"checked": False, "notes": ""} for item in items}

# Display each item with a checkbox and a text input for notes
for item in items:
    col1, col2 = st.columns([1,2])
    with col1:
        st.session_state.confirmations[item]["checked"] = st.checkbox(item, value=st.session_state.confirmations[item]["checked"])
    with col2:
        st.session_state.confirmations[item]["notes"] = st.text_input(f"Notes for '{item}':", value=st.session_state.confirmations[item]["notes"])

# Check if all items are confirmed
all_confirmed = all(val["checked"] for val in st.session_state.confirmations.values())

# If all confirmed, allow final confirmation
if all_confirmed:
    if st.button("Final Confirmation"):
        st.success("All items have been confirmed and final confirmation is complete.")
else:
    st.info("Please confirm all items before final confirmation.")
