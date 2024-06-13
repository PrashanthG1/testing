import streamlit as st

st.title('Hi, website created')
st.header('This is headers')
st.text('this is text box')
st.subheader('I am your subheader')
st.markdown('**this is bold** *ionion* bigger ')
st.markdown('---')
st.markdown('[LinkedIn](https://www.linkedin.com/in/prashanth-kumar-gunda-591717200/)')

code="""
print('Hello World')
"""
st.code(code, language='python')
st.write('## H2 tag')
st.metric(label='wind speed', value='1200ms⁻¹', delta= '-1.5 ms⁻¹')
import pandas as pd
tabel =pd.DataFrame({
    'hi':[235,566],
    'bniknb':[45453,65]

})
st.table(tabel)

st.dataframe(tabel)

st.image('img1.jpeg')
st.video('vid1.mp4')