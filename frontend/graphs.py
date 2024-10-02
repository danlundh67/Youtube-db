from utils.query_database import QueryDatabase
import plotly.express as px
import streamlit as st 
import pandas as pd

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
        st.markdown("## Prenumerationsstatus: Visningstid (h), antal visningar och genomsnittlig tittartid (s) under senaste månaden")
        st.plotly_chart(fig)


class SelectView:
    def __init__(self) -> None:
        self.df = QueryDatabase("SELECT * FROM marts.content_view_time;").df
        

    def display_plot(self):
        st.markdown("## Analys av video")
        selected = st.selectbox("Välj en titel", options=self.df['Videotitel'])
        
        #['Visningar','visade timmar','Exponeringar', 'Klickfrekvens_exponeringar']
        
        pdf=self.df

        st.markdown(f"Vald title: {selected}")
        
        required_columns = ['Videotitel','Visningar', 'Visningstid_timmar', 'Exponeringar', 'Klickfrekvens_exponering_%']
        
        df2 = self.df.loc[self.df['Videotitel'] == selected, required_columns]
            
        #st.dataframe(df2)

        avgs = pd.DataFrame({
            'Videotitel': ['Genomsnitt'],  # Label row for averages
            'Visningar': [self.df['Visningar'].median()],
            'Visningstid_timmar': [self.df['Visningstid_timmar'].median()],
            'Exponeringar': [self.df['Exponeringar'].median()],
            'Klickfrekvens_exponering_%': [self.df['Klickfrekvens_exponering_%'].median()]
        })
        

        combined_df=pd.concat([df2,avgs], axis=0)

        st.dataframe(combined_df)

        melted_df = pd.melt(combined_df, id_vars=['Videotitel'], 
                            value_vars=['Visningar', 'Visningstid_timmar', 'Exponeringar', 'Klickfrekvens_exponering_%'], 
                            var_name='Metric', value_name='Value')

        fig = px.bar(melted_df, x='Metric', y='Value', color='Videotitel', 
                     barmode='group', labels={'Value': 'Value', 'Metric': 'Metrics'}, 
                     title=f"Data för videon '{selected}' jämfört genomsnitt (median)")

        st.plotly_chart(fig)


