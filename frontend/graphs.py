from utils.query_database import QueryDatabase
import plotly.express as px
import streamlit as st 

class ViewsTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.views_per_date").df
        print(self.df)

    def display_plot(self):
        fig = px.line(self.df, x="Datum", y="Visningar")
        st.markdown("## Antal visningar under senaste månaden")
        st.plotly_chart(fig)


class ViewSubsciber:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.prenumeration").df
        print(self.df)

    def display_plot(self):
        fig = px.bar(self.df, x="Prenumerationsstatus", y=["Visningstid (timmar)"])
        st.markdown("## Antal visningar under senaste månaden")
        st.plotly_chart(fig)
# create more graphs here

