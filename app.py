import streamlit as st

st.text ('Vuoi giocare?')

play = st.radio('Pick one', ['si', 'no'])

if play == 'si':
    scelta = st.slider('Ok, scegli un livello', 0,100)





else:
    st.text ('ok, alla prossima')

