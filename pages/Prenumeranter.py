import streamlit as st 
from frontend.graphs import ViewSubsciber
from frontend.styleutil import cssstyle

viewer_graph = ViewSubsciber()



st.sidebar.success("Jämförelse prenumeranter och icke prenumeranter")
viewer_graph.display_plot()
cssstyle()