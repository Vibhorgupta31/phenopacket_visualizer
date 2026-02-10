# 🧬 Phenopacket Explorer
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.53.1-FF4B4B)
![ECharts](https://img.shields.io/badge/visualization-ECharts-green)

A visualization tool for phenopackets data. This application parses complex, nested JSON phenopackets and renders them as interactive topology trees.


# 🛠️ Installation

## 🛠️ Local Installation (Conda)

Recommendation to use **Conda** locally to ensure environment consistency.
### 1. Clone the Repository
```bash
git clone https://github.com/Vibhorgupta31/phenopacket_visualizer.git
cd phenopacket_visualizer
```

### 2. Create the Environment

```bash
# Create env with Python 3.10
conda create -n phenopacket_visualizer python=3.10
conda activate phenopacket_visualizer
```

### 3. Install Python Dependencies

Use `pip` inside Conda to ensure library versions match the Streamlit Cloud environment.

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run phenopacket_topology.py
```
## ☁️ Deployment Notes (Streamlit Cloud)

This repository includes configuration files specifically for Streamlit Community Cloud:

* `requirements.txt`: Handles Python libraries.
* `packages.txt`: Handles system binaries if needed.

## 📂 Project Structure

```text
phenopacket_visualizer/
├── phenopacket_topology.py   # Main Entry Point (Interactive Tree)
├── requirements.txt          # Python Dependencies
├── README.md                 # Documentation
├── src/
│   ├── loader.py             # JSON loading logic (local files)
│   ├── uploader.py           # Session State & File Upload Handler
│   └── echarts_visualizer.py # Core ECharts Logic (Parser & Smart Labeler)
└── data/
    └── raw/                  # Default demo data
```

## 🧠 How It Works: The Parser
Unlike standard JSON visualizers that "explode" or clutter when they hit large lists, this tool uses a  Recursive Parser (src/echarts_visualizer.py) to create a clean, navigable tree:
1. **Smart Labeling:** Instead of showing generic list indices (e.g., [0], [1]), the parser "peeks" inside dictionaries to find human-readable labels (e.g., "Marfan Syndrome", "FBN1").
2. **Path Flattening:** Redundant JSON wrappers (like type -> term) are automatically flattened. You see the data immediately without clicking through empty container nodes.
3. Context-Aware Coloring: Nodes are colored based on their context:

- 🔴 Red: Excluded / Absent Features (e.g., "Patient does NOT have X").
- 🟢 Green: Observed Features and Context Matches.
- 🔵 Blue: Structural Nodes (Root, Patient info)
## 🔗 Live Demo

Check out the running application here:
[**Launch Phenopacket Visualizer**](https://phenopacketvisualizer.streamlit.app/)
