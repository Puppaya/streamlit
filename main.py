import streamlit as st
import pandas as pd
st.title("Start with Streamlit")
st.write("test")

st.markdown("### My Markdown")
code = '''
def hello():
    print("Hello, Streamlit!")
'''

show_btn = st.button("Showa code!")
if show_btn:
    st.code(code, language='python')

cols = st.columns(2)

with cols[0]:
    age_inp = st.number_input("Input ypur age")
    st.markdown(f"Your age is {age_inp}")

with cols[1]:
    text_inp = st.text_input("Input your text")
    word_tokezine = "|".join(text_inp.split())
    st.markdown(f"{word_tokezine}")

df = pd.DataFrame({
    'first columns':[1, 2, 3, 4],
    'second columns':[10, 60, 30, 40]
})
st.dataframe(df)

show_graph = st.button("Show Graph")
if show_graph:
    st.line_chart(df, x = 'first columns', y = 'second columns')