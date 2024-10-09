import streamlit as st 
from frontend.graphs import ViewsTrend
from frontend.styleutil import cssstyle

views_graph = ViewsTrend()
st.sidebar.success("Visningar totalt under senast månaden")
views_graph.display_plot()
cssstyle()