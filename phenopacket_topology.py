import streamlit as st
from streamlit_echarts import st_echarts
from src import loader, uploader
from src.echarts_visualizer import parse_to_echarts

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

    # Convert the JSON to the ECharts format

    tree_data = parse_to_echarts(data, label="Phenopacket")


    def count_leaves(node):
        """Recursively counts the number of leaf nodes in the tree."""
        if not node.get("children"):
            return 1
        return sum(count_leaves(child) for child in node["children"])


    leaf_count = count_leaves(tree_data)
    dynamic_height = max(600, leaf_count * 20)

    # Define the chart options
    options = {
        "tooltip": {"trigger": "item", "triggerOn": "mousemove"},
        "series": [
            {
                "type": "tree",
                "data": [tree_data],

                "symbolSize": 10,
                "label": {"position": "left", "verticalAlign": "middle", "align": "right", "fontSize": 12},
                "leaves": {
                    "label": {"position": "right", "verticalAlign": "middle", "align": "left", "fontSize": 12},
                },
                "expandAndCollapse": True,
                "animationDuration": 550,
                "animationDurationUpdate": 750,
                "symbolSize": 10,

                # Tweak this to push text further from the dot
                "label": {
                    "position": "left",
                    "verticalAlign": "middle",
                    "align": "right",
                    "distance": 10  # Add 10px buffer between dot and text
                },

            }
        ]
    }
    st_echarts(options=options, height= '800px')
else:
    st.error(f"No data available to run the app.")
