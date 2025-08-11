import streamlit as st
import matplotlib.pyplot as plt

# Données fixes
MASSE_VIDE = 584.4  # kg
BRAS_VIDE = 0.35  # m
BRAS_EQUIPE = 0.41
BRAS_PASSAGER = 1.19
BRAS_BAGAGES = 1.90
BRAS_CARBURANT = 1.12
DENSITE_CARBURANT = 0.72  # kg/L

# Limites Cat. N (exemple simplifié)
limite_bras = [0.205, 0.205, 0.43, 0.56, 0.56]
limite_masse = [600, 750, 900, 900, 650]

st.title("Calculateur de centrage DR400")

# Entrées utilisateur
pilote = st.number_input("Masse du pilote (kg)", min_value=0.0)
copilote = st.number_input("Masse du copilote (kg)", min_value=0.0)
passager1 = st.number_input("Masse passager arrière gauche (kg)", min_value=0.0)
passager2 = st.number_input("Masse passager arrière droit (kg)", min_value=0.0)
bagages = st.number_input("Masse des bagages (kg)", min_value=0.0)
carburant_l = st.number_input("Volume carburant (L)", min_value=0.0)

if st.button("Calculer le centrage"):
    # Masse carburant
    masse_carburant = carburant_l * DENSITE_CARBURANT

    # Moment total
    moment_total = (
        MASSE_VIDE * BRAS_VIDE +
        (pilote + copilote) * BRAS_EQUIPE +
        (passager1 + passager2) * BRAS_PASSAGER +
        bagages * BRAS_BAGAGES +
        masse_carburant * BRAS_CARBURANT
    )

    # Masse totale
    masse_totale = MASSE_VIDE + pilote + copilote + passager1 + passager2 + bagages + masse_carburant

    # Bras total
    bras_total = moment_total / masse_totale

    st.write(f"**Masse totale :** {masse_totale:.1f} kg")
    st.write(f"**Bras de levier :** {bras_total:.3f} m")

    # Graphique
    fig, ax = plt.subplots(figsize=(6,6))
    ax.plot(limite_bras, limite_masse, label="Limites Cat. N", color="blue")
    ax.scatter(bras_total, masse_totale, color="red", label="Point calculé")
    ax.set_xlabel("Bras de levier (m)")
    ax.set_ylabel("Masse (kg)")
    ax.set_title("Centrage DR400")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)


