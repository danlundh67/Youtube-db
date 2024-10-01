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
        self.df.rename(columns={"Prenumerationsstatus":"Status","Visningstid (timmar)": "Total visningstid (h)", 'Visningar':'Visat (antal ggr)','Genomsnittlig visningslängd':'Medel visningstid (s)'}, inplace=True)
        fig = px.bar(self.df,
                     x='Status', 
                     y=['Total visningstid (h)','Visat (antal ggr)','Medel visningstid (s)'], 
                     barmode="group", 
                     labels={"value":""},)
        
        fig.update_legends(title='',)
        st.markdown("## Visningstid (h), antal visningar och genomsnittlig tittartid (s) under senaste månaden")
        st.plotly_chart(fig)


class SelectView:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.content_view_time;").df

    def display_plot(self):

        

        df = self._content
        #html=df.to_html(classes='

        kpis = {
            "videor": len(dmystyle')f),
            "visade timmar": df["Visningstid_timmar"].sum(),
            "prenumeranter": df["Prenumeranter"].sum(),
            "exponeringar": df["Exponeringar"].sum(),
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col: 
                st.metric(kpi, round(kpis[kpi]))

        st.dataframe(df)

