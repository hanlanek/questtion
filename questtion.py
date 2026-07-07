import streamlit as st
import random

# Ustawienia strony z ładną czcionką, większym rozmiarem tekstu i fuksjowymi kartami
st.markdown(
    """
    <style>
    /* Import czcionki szeryfowej Playfair Display */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;1,500&display=swap');

    /* Tło strony - śliczny pastelowy róż */
    .stApp {
        background-color: #FFD1DC;
    }

    /* Ustawienia czcionki dla wszystkich tekstów */
    .stApp, div[data-testid="stMarkdownContainer"] p, label, button, .stHeader {
        font-family: 'Playfair Display', 'Georgia', 'Times New Roman', serif !important;
        color: #4A2E35 !important;
        font-size: 24px !important;
    }

    /* Duży i wyśrodkowany tytuł */
    h1 {
        font-size: 60px !important;
        text-align: center;
        margin-bottom: 30px;
    }

    /* Stylizacja nagłówków wewnątrz kart */
    .stHeader {
        margin-top: 10px;
    }

    /* Pytania mają fuksjowy kolor i są boldowane */
    .pytanie {
        color: #FF00FF !important;
        font-weight: bold;
        font-size: 30px !important;
    }

    /* Kod na animację spadających gwiazdek */
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
    }

    /* Główne karty z pytaniami */
    .stApp div[data-testid="stMarkdownContainer"] > div {
        background: white;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    /* Kontener dla kart odpowiedzi */
    .odpowiedzi-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 20px;
    }

    /* Styl kart odpowiedzi (przycisków) */
    div.stButton > button {
        background-color: white;
        color: #4A2E35;
        border: 2px solid #DDDDDD;
        border-radius: 10px;
        font-size: 24px !important;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.3s ease;
        text-transform: none; /* Wyłącz duże litery */
        padding: 10px 20px;
        margin: 10px;
    }

    /* Efekt hover dla kart odpowiedzi */
    div.stButton > button:hover {
        background-color: #DDDDDD;
        color: #4A2E35;
        border-color: #DDDDDD;
    }

    /* Stylizacja sekcji z logiką - po kliknięciu odpowiedzi (np. "if Q1 = ...") */
    .stApp div.stMarkdown > div:not(:first-child) {
        border: none;
        box-shadow: none;
        background: transparent;
        padding: 0px;
    }

    /* Teksty pod kartami nie mają tła */
    .stApp .stMarkdown p {
        background: transparent;
        border: none;
        box-shadow: none;
        padding: 0px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("✨ ⭐ ✨ ⭐ ✨")

# --- KROK 1 ---
st.markdown('<p class="stHeader vraag pytanie">Cześć, lubisz formalności społeczne w relacjach? ✨</p>', unsafe_allow_html=True)
st.write("---")

# Używamy sesji, żeby zapamiętać wybraną odpowiedź
if 'odpowiedz_1' not in st.session_state:
    st.session_state['odpowiedz_1'] = None

# Tworzymy dwie kolumny dla kart odpowiedzi
col1_1, col2_1 = st.columns(2)

with col1_1:
    if st.button("raczej tak", key="odp_1_tak"):
        st.session_state['odpowiedz_1'] = "tak"
with col2_1:
    if st.button("no nie wiem", key="odp_1_nie"):
        st.session_state['odpowiedz_1'] = "nie"

# Logika po wybraniu odpowiedzi w kroku 1
if st.session_state['odpowiedz_1'] == "nie":
    st.markdown('<p class="stHeader vraag">to jak mogę Ciebie nazywać?</p>', unsafe_allow_html=True)
elif st.session_state['odpowiedz_1'] == "tak":
    st.write("---")

    # --- KROK 2 (pojawia się tylko po wybraniu "raczej tak") ---
    st.markdown('<p class="stHeader vraag pytanie"> Nazywać cię swoim chłopakiem? </p>', unsafe_allow_html=True)
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
        if st.button("za wcześnie", key="odp_3_nie"):
            st.session_state['odpowiedz_3'] = "za wcześnie"
    if st.session_state['odpowiedz_2'] == "nie":
        st.write("zanotowano")
    if st.session_state['odpowiedz_3'] == "za wcześnie":
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