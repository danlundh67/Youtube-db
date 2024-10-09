import streamlit as st 
from frontend.kpi import ContentKPI, DeviceKPI
from frontend.styleutil import cssstyle

device_kpi = DeviceKPI()
content_kpi =ContentKPI()



st.sidebar.success("Videos, detta visar en sammanfattning för alla videos och grunddata för videos")
content_kpi.display_content()
cssstyle()