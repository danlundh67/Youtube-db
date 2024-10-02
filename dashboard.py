import streamlit as st 
from frontend.kpi import ContentKPI, DeviceKPI, ViewersAge
from frontend.graphs import ViewsTrend, ViewSubsciber, SelectView


device_kpi = DeviceKPI()
content_kpi = ContentKPI()
views_graph = ViewsTrend()
viewers_kpi = ViewersAge()
view_subsciber = ViewSubsciber()
sel_view = SelectView()

def layout():
    st.markdown("# The data driven youtuber")
    st.markdown("Den här dashboarden syftar till att utforska datan i Kokchun's youtubekanal")
    # device_kpi.display_device_views()
    # device_kpi.display_device_summary()
    content_kpi.display_content()
    views_graph.display_plot()
    device_kpi.display_content()
    viewers_kpi.display_content()
    view_subsciber.display_plot()
    sel_view.display_plot()

if __name__ == "__main__":
    layout()