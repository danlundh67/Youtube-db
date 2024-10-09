import streamlit as st 
from frontend.kpi import DeviceKPI
from frontend.styleutil import cssstyle

device_kpi = DeviceKPI()



st.sidebar.success("Enhetstyper som används för att titta på videos")
device_kpi.display_content()
cssstyle()