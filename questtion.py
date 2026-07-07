import streamlit as st
import random

# Ustawienia strony, piękna czcionka, karty pytań i kosmiczne tło
st.markdown(
    """
    <style>
    /* Import czcionki szeryfowej Playfair Display */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;1,500&display=swap');

    /* Tło strony - śliczny pastelowy róż */
    .stApp {
        background-color: #FFD1DC;
    }

    /* Ustawienia czcionki dla zwykłych tekstów */
    .stApp, div[data-testid="stMarkdownContainer"] p, label, button {
        font-family: 'Playfair Display', 'Georgia', 'Times New Roman', serif !important;
        color: #4A2E35 !important;
        font-size: 24px !important;
    }

    /* Duży i wyśrodkowany tytuł bezpośrednio na różowym tle */
    h1 {
        font-size: 60px !important;
        text-align: center;
        margin-bottom: 30px;
        color: #4A2E35 !important;
    }

    /* --- NOWE, PRECYZYJNE KARTY DLA PYTAŃ --- */
    .karta-pytania {
        background: white !important;
        border-radius: 15px !important;
        padding: 30px !important;
        margin-top: 10px !important;
        margin-bottom: 25px !important;
        box-shadow: 0 8px 24px rgba(0,0,0,0.06) !important;
        text-align: center !important;
        position: relative !important;
        z-index: 10 !important; /* Karty są wyżej niż kosmici */
    }

    /* Styl tekstu pytania wewnątrz karty */
    .pytanie {
        color: #FF00FF !important;
        font-weight: bold !important;
        font-size: 30px !important;
        margin: 0 !important;
    }

    /* --- ANIMACJA SPADAJĄCYCH GWIAZDEK (FINAŁ) --- */
    @keyframes fall {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(110vh) rotate(720deg); opacity: 0; }
    }
    .star {
        position: fixed;
        top: -50px;
        pointer-events: none;
        animation: fall 4.5s linear forwards;
        z-index: 9999;
        background: transparent !important;
        box-shadow: none !important;
    }

    /* --- ANIMACJA LATAJĄCYCH KOSMITÓW W TLE --- */
    @keyframes flyAcross {
        0% { left: -100px; transform: translateY(0px) rotate(0deg); }
        100% { left: 100vw; transform: translateY(60px) rotate(360deg); }
    }

    .alien {
        position: fixed;
        pointer-events: none;
        animation: flyAcross linear infinite;
        opacity: 0.35; /* Lekka przezroczystość, żeby subtelnie wtapiały się w tło */
        z-index: 1; /* Kosmici latają NAD różowym tłem, ale POD kartami i przyciskami */
        font-size: 55px !important;
        background: transparent !important;
        box-shadow: none !important;
        border: none !important;
    }

    /* Różne wysokości i czasy przelotu dla każdego ufo */
    .ufo1 { top: 12%; animation-duration: 22s; animation-delay: 0s; }
    .ufo2 { top: 45%; animation-duration: 30s; animation-delay: 6s; }
    .ufo3 { top: 78%; animation-duration: 18s; animation-delay: 12s; }
    .ufo4 { top: 90%; animation-duration: 22s; animation-delay: 0s; }

    /* Zabezpieczenie przycisków, aby też były nad kosmitami */
    div.stButton {
        position: relative;
        z-index: 10;
    }

    /* Styl przycisków odpowiedzi */
    div.stButton > button {
        background-color: white;
        color: #4A2E35;
        border: 2px solid #DDDDDD;
        border-radius: 10px;
        font-size: 24px !important;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.3s ease;
        text-transform: none;
        padding: 10px 20px;
        margin: 10px auto;
        display: block;
    }

    div.stButton > button:hover {
        background-color: #DDDDDD;
        color: #4A2E35;
        border-color: #DDDDDD;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Wstrzyknięcie czystych kosmitów w tło (całkowicie bez kafelków)
st.markdown(
    """
    <div class="alien ufo1">🛸</div>
    <div class="alien ufo2">👽</div>
    <div class="alien ufo3">🛸</div>
    <div class="alien ufo4">👽</div>
    """,
    unsafe_allow_html=True
)

st.title("✨ ⭐ ✨ ⭐ ✨")

# --- KROK 1 ---
st.markdown('<p class="stHeader vraag pytanie">Cześć mogę być Twoja? ✨</p>', unsafe_allow_html=True)
st.write("---")

if 'odpowiedz_1' not in st.session_state:
    st.session_state['odpowiedz_1'] = None
col1_1, col2_1 = st.columns(2)

with col1_1:
    if st.button("raczej tak", key="odp_1_tak"):
        st.session_state['odpowiedz_1'] = "tak"
with col2_1:
    if st.button("no nie wiem", key="odp_1_nie"):
        st.session_state['odpowiedz_1'] = "nie"

# Logika po wybraniu odpowiedzi w kroku 1
if st.session_state['odpowiedz_1'] == "nie":
    st.markdown('<p class="stHeader vraag"> sorry missclick </p>', unsafe_allow_html=True)
elif st.session_state['odpowiedz_1'] == "tak":
    st.write("---")

    # --- KROK 2 (pojawia się tylko po wybraniu "raczej tak") ---
    st.markdown('<p class="stHeader vraag pytanie"> Czy nazywać Cię swoim chłopakiem? </p>', unsafe_allow_html=True)
    st.write("---")

    if 'odpowiedz_2' not in st.session_state:
        st.session_state['odpowiedz_2'] = None

    col1_2, col2_2 , col3_2 = st.columns(3)

    with col1_2:
        if st.button("tak", key="odp_2_tak"):
            st.session_state['odpowiedz_2'] = "tak"
    with col2_2:
        if st.button("nie", key="odp_2_nie"):
            st.session_state['odpowiedz_2'] = "nie"
    with col3_2:
        if st.button("za wcześnie", key="odp_2_zawczesnie"):
            st.session_state['odpowiedz_2'] = "za wcześnie"
    if st.session_state['odpowiedz_2'] == "nie":
        st.write("zanotowano")
    if st.session_state['odpowiedz_2'] == "za wcześnie":
        st.write("zanotowano")
    elif st.session_state['odpowiedz_2'] == "tak":
        st.write("---")

        # --- KROK 3 (pojawia się tylko po drugim "tak") ---
        st.markdown('<p class="stHeader vraag pytanie">Czy może oblubieńcem?</p>', unsafe_allow_html=True)
        st.write("---")

        if 'odpowiedz_3' not in st.session_state:
            st.session_state['odpowiedz_3'] = None

        col1_3, col2_3 = st.columns(2)

        with col1_3:
            if st.button("tak", key="odp_3_tak"):
                st.session_state['odpowiedz_3'] = "tak"
        with col2_3:
            if st.button("no nie wiem", key="odp_3_nie"):
                st.session_state['odpowiedz_3'] = "nie"

        # Logika po wybraniu odpowiedzi w kroku 3
        if st.session_state['odpowiedz_3'] == "nie":
            st.write("ok")
        elif st.session_state['odpowiedz_3'] == "tak":
            # Gwiezdny finał!
            star_html = "".join([
                f'<div class="star" style="left: {random.randint(0, 100)}%; animation-delay: {random.uniform(0, 3.5)}s; font-size: {random.randint(20, 45)}px;">⭐</div>'
                for _ in range(60)
            ])
            st.markdown(star_html, unsafe_allow_html=True)
            st.success("oke zip zip zab zab👽! 🥰🎉✨")