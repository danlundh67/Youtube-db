import streamlit as st 
from frontend.kpi import ContentKPI, DeviceKPI, ViewersAge
from frontend.graphs import ViewsTrend, ViewSubsciber, SelectView
from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd


device_kpi = DeviceKPI()
content_kpi = ContentKPI()
views_graph = ViewsTrend()
viewers_kpi = ViewersAge()
view_subsciber = ViewSubsciber()
sel_view = SelectView()

def layout():
    # inset start
    st.set_page_config(page_title = "This is a Multipage WebApp") 
    #st.title("This is the Home Page Geeks.")
    st.sidebar.success("Välj vilken KPI du vill se ovan") 
    # inset stop
    st.markdown("# The data driven youtuber")
   
    st.markdown("")
    

    img=Image.open('Designer.jpeg')
    st.image(img, caption='YouTube analyse by MS Designer...')
    st.markdown("Den här dashboarden syftar till att utforska datan i Kokchun's YouTube kanal")
    
    #df = pd.DataFrame([["<img src='Designer.jpeg' width='300'/>"]], columns=["Image"])
    # Display the table with HTML content
    #st.write(df.to_html(escape=False), unsafe_allow_html=True)

    #st.image(img, caption='YouTube analyse by MS Designer...')
    # device_kpi.display_device_views()
    # device_kpi.display_device_summary()
    # content_kpi.display_content()
    # views_graph.display_plot()
    # device_kpi.display_content()
    # viewers_kpi.display_content()
    # view_subsciber.display_plot()
    # sel_view.display_plot()

    read_css()


def read_css():
    css_path = Path(__file__).parents[0] / "style.css"

    with open(css_path) as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True,
        )

if __name__ == "__main__":
    layout()