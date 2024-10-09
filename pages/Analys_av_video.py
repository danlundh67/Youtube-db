import streamlit as st 
from frontend.graphs import SelectView
from frontend.styleutil import cssstyle

select_graph = SelectView()



st.sidebar.success("Analys av valbar video")
select_graph.display_plot()
cssstyle()