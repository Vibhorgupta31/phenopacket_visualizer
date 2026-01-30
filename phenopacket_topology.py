import streamlit as st
import streamlit.components.v1 as components
from src import loader, uploader, visualizer

# Page Configuration
st.set_page_config(
    page_title="Phenopacket Visualizer",
    layout="wide",
)

data = uploader.load_upload_file()

if data:
    st.title("Phenopacket Topology Explorer")
    st.markdown("---")
    with st.expander("View Raw File (YAML)", expanded=False):
        yaml_text = loader.convert_to_yaml(data)
        st.code(yaml_text, language="yaml")

    st.subheader("Structured Topology")
    graph = visualizer.create_topology_graph(data)
    svg_data = graph.pipe(format='svg').decode('utf-8')

    # This HTML / CSS wrapper creates a box that scrolls to see the whole graph
    # Gemini Code

    html_block = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://bumbu.me/svg-pan-zoom/dist/svg-pan-zoom.min.js"></script>
        </head>
        <body style="margin: 0; padding: 0; overflow: hidden;">
            <div id="container" style="width: 100%; height: 900px; border: 1px solid #ccc;">
                {svg_data}
            </div>
            <script>
                // Wait for the SVG to load, then activate pan/zoom
                window.onload = function() {{
                    // Find the SVG element inside the string
                    var svgElement = document.querySelector("svg");

                    // Set width/height to 100% of container so it fits the window
                    svgElement.setAttribute("width", "100%");
                    svgElement.setAttribute("height", "100%");

                    // Initialize the library
                    svgPanZoom(svgElement, {{
                        zoomEnabled: true,
                        controlIconsEnabled: true,  // Adds + and - buttons
                        fit: true,
                        center: true
                    }});
                }};
            </script>
        </body>
        </html>
    """

    components.html(html_block, height=800)

else:
    st.error(f"No data available to run the app.")
