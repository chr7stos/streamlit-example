import streamlit as st
import altair as alt
import pandas as pd
from vega_datasets import data

st.title("Monthly water inflows since 1988 in Cyprus")
st.markdown("""
This is a dashboard with data data.gov.cy **data.gov.cy** and you can get them [here](https://www.data.gov.cy/dataset/μηνιαία-εισροή-νερού-στους-ταμιευτήρες-νερού-φράγματα).   
The goal is to have easy simple visualisations for more of the open data in Cyprus.
""")

df = st.cache(pd.read_csv)("data/monthly_water_inflows_from_1988.csv")

month = st.selectbox('Show available months', df.columns[1:], 0)

st.markdown("Flow of water in Cyprus dams")

chart = alt.Chart(df).mark_line().encode(
    x='YEAR',
    y=month
).interactive()

st.altair_chart(chart)
