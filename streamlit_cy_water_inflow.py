import streamlit as st
import altair as alt
import pandas as pd
from vega_datasets import data

st.title("Monthly water inflows since 1988 in Cyprus")
st.markdown("""
This is a dashboard with data **from data.gov.cy** and you can get them [here](https://www.data.gov.cy/dataset/μηνιαία-εισροή-νερού-στους-ταμιευτήρες-νερού-φράγματα)
""")

df = st.cache(pd.read_csv)("data/monthly_water_inflows_from_1988.csv")

months = st.sidebar.multiselect('Show availavle months', df.columns[1:-1])

#st.markdown("This is cool!")
#st.line_chart(df["TOTAL"].dropna())

#st.altair_chart(df[" OCTOBER"].dropna())

chart = alt.Chart(df).mark_line().encode(
    x='YEAR',
    y=' OCTOBER',
).interactive()

st.altair_chart(chart)
