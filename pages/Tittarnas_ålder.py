import streamlit as st 
from frontend.kpi import ViewersAge
from frontend.styleutil import cssstyle

viewer_kpi = ViewersAge()



st.sidebar.success("Tittarnas åldersfördelning")
viewer_kpi.display_content()
cssstyle()