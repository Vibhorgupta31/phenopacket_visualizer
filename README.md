# 🧬 Phenopacket Visualizer
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.53.1-FF4B4B)

A visualization tool for phenopackets data. This application parses complex, nested JSON phenopackets and renders them as readable topology graphs.


# 🛠️ Installation

## 🛠️ Local Installation (Conda)

Recommendation to use  **Conda** locally because it installs both Python and the required Graphviz system binary in one go.
### 1. Clone the Repository
```bash
git clone https://github.com/Vibhorgupta31/phenopacket_visualizer.git
cd phenopacket_visualizer
```

### 2. Create the Environment

This command creates the environment and installs the system binary for Graphviz.

```bash
# Create env with Python 3.10 and Graphviz binary
conda create -n phenopacket_visualizer python=3.10 graphviz
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
* `packages.txt`: Handles the Graphviz system binary automatically on the server.

## 📂 Project Structure

```text
phenopacket_visualizer/
├── phenopacket_topology.py   # Main Entry Point (Topology View)
├── requirements.txt          # Python Dependencies
├── packages.txt              # System Binaries (for Cloud Deployment)
├── README.md                 # Documentation
├── pages/
│   └── 1_Phenotype_Dashboard.py  # In progress
├── src/
│   ├── loader.py             # JSON loading logic (local files)
│   ├── uploader.py           # Session State & File Upload Handler
│   └── visualizer.py         # Recursive Graphviz Logic & Pruning Engine
└── data/
    └── raw/                  # Default demo data
```

## 🧠 How It Works: The Parser
Standard JSON visualizers "explode" when they hit large lists (e.g., 50  phenotypic_features). This tool uses a  Filter in src/visualizer.py:

1. **Lists < 2 items**: Fully expanded. The parser draws these connections using invisible "connector nodes" (`shape='point'`) to keep lines smooth and readable.

2. **Lists > 2 items**: Collapsed into summary nodes (e.g., `[Phenotypic Features: 45 items]`). This prevents the graph from becoming a "spiderweb" of unreadable data.

## 🔗 Live Demo

Check out the running application here:
[**Launch Phenopacket Visualizer**](https://phenopacketvisualizer.streamlit.app/)
