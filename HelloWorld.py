import streamlit as st




st.title("Hello World");
st.markdown("""Hello World !""")

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)


option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)