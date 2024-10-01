from utils.query_database import QueryDatabase
import plotly.express as px
import streamlit as st 

class ViewsTrend:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.views_per_date").df
        #print(self.df)

    def display_plot(self):
        fig = px.line(self.df, x="Datum", y="Visningar")
        st.markdown("## Antal visningar under senaste månaden")
        st.plotly_chart(fig)


def time_to_seconds(time_str):
    time_str2=str(time_str)
    h, m, s = map(int, time_str2.split(':'))
    return h * 3600 + m * 60 + s

class ViewSubsciber:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.prenumeration ORDER BY Visningar DESC OFFSET 1").df
        # print(self.df['Genomsnittlig visningslängd'].apply(time_to_seconds))
        self.df['Genomsnittlig visningslängd']=self.df['Genomsnittlig visningslängd'].apply(time_to_seconds)

    def display_plot(self):
        fig = px.bar(self.df,
                     x='Prenumerationsstatus', 
                     y=['Visningstid (timmar)','Visningar','Genomsnittlig visningslängd'], 
                     barmode="group", 
                     labels={'Visningstid (timmar)': 'Showed (hours)', 'Visningar':'Showed (# of times)','Genomsnittlig visningslängd':'Average showtime (s)'},)
        
        fig.update_legends(title='',)
        st.markdown("## Visningstid (h), antal visningar och genomsnittlig tittartid (s) under senaste månaden")
        st.plotly_chart(fig)


class SelectView:
    pass