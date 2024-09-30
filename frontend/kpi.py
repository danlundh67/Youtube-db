import streamlit as st
from utils.query_database import QueryDatabase

class ContentKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.content_view_time;").df

    def display_content(self):
        df = self._content
        st.markdown("## KPIer för videor")
        st.markdown("Nedan visas KPIer för totalt antal")

        kpis = {
            "videor": len(df),
            "visade timmar": df["Visningstid_timmar"].sum(),
            "prenumeranter": df["Prenumeranter"].sum(),
            "exponeringar": df["Exponeringar"].sum(),
        }

        for col, kpi in zip(st.columns(len(kpis)), kpis):
            with col: 
                st.metric(kpi, round(kpis[kpi]))
        st.dataframe(df)

# create more KPIs here
class DeviceKPI:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.device_summary ORDER BY Visningstid_timmar DESC OFFSET 1;").df
    
    def display_content(self):
        df = self._content
        st.markdown("The different devices used")

        st.dataframe(df)
    

class ViewersAge:
    def __init__(self) -> None:
        self._content = QueryDatabase("SELECT * FROM marts.viewer_age;").df

    def display_content(self):
        df = self._content
        st.markdown("The viewers age span")

        st.dataframe(df)
