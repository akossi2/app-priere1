import streamlit as st
import datetime
import random

# Configuration
st.set_page_config(page_title="🙏 Connexion Divine", layout="centered")

# Titre
st.title("🙏 Connexion Divine")
st.subheader("Reste connecté à Dieu toute la journée")

# Heure actuelle
now = datetime.datetime.now()
heure = now.hour

# Prières selon moment
def get_priere(heure):
    if heure < 12:
        return "🌅 Seigneur, merci pour ce nouveau jour. Guide mes pas et mes décisions aujourd’hui."
    elif heure < 18:
        return "☀️ Seigneur, merci pour cette journée. Donne-moi la force et la sagesse pour continuer."
    else:
        return "🌙 Seigneur, merci pour tout ce que tu as fait aujourd’hui. Pardonne-moi et accorde-moi une nuit paisible."

# Versets
versets = [
    "Je puis tout par celui qui me fortifie. (Philippiens 4:13)",
    "L'Éternel est mon berger, je ne manquerai de rien. (Psaume 23:1)",
    "Demandez, et l’on vous donnera. (Matthieu 7:7)",
    "Confie-toi en l'Éternel de tout ton cœur. (Proverbes 3:5)"
]

# Affichage prière
st.markdown("## 🙏 Prière du moment")
st.info(get_priere(heure))

# Verset du jour
st.markdown("## 📖 Verset du jour")
st.success(random.choice(versets))

# Bouton prière
if st.button("✅ J’ai prié"):
    st.success("Que Dieu te bénisse 🙏")

# Suivi simple
if "compteur" not in st.session_state:
    st.session_state.compteur = 0

if st.button("📊 Ajouter une prière"):
    st.session_state.compteur += 1

st.markdown("## 🔥 Ton engagement")
st.write(f"Nombre de prières aujourd’hui : {st.session_state.compteur}")

# Planning
st.markdown("## ⏰ Heures de prière recommandées")
st.write("""
- 🌅 Matin : 6h
- ☀️ Midi : 12h
- 🌇 Soir : 18h
- 🌙 Nuit : 22h
""")