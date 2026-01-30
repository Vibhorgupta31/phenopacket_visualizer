# 🧬 Phenopacket Visualizer

A visualization tool for phenopackets data. This application parses complex, nested JSON phenopackets and renders them as readable topology graphs.


## 🛠️ Installation

This project uses **Conda** for reproducible environment management to ensure the correct Graphviz system binaries are installed.

### 1. Clone the Repository
```bash
git clone [https://github.com/Vibhorgupta31/phenopacket_visualizer.git](https://github.com/Vibhorgupta31/phenopacket_visualizer.git)
cd phenopacket_visualizer
```

### 2. Create the Environment

We use a strict `environment.yml` to guarantee stability.

```bash
conda env create -f environment.yml
conda activate phenopacket-env
```

### 3. Run the App

```bash
streamlit run phenopacket_topology.py
```

## 📂 Project Structure

```text
phenopacket-explorer/
├── phenopacket_topology.py                   # Main Entry Point (Topology View)
├── environment.yml           # Conda Dependencies (Pinned Versions)
├── README.md                 # Documentation
├── pages/
│   └── 1_Phenotype_Dashboard.py  # In Progress
├── src/
│   ├── loader.py             # JSON loading logic (local files)
│   ├── uploader.py           # Session State & File Upload Handler
│   └── visualizer.py         # Recursive Graphviz Logic & Pruning Engine
└── data/
    └── raw/                  # Default demo data

```
## 📦 Dependencies

* `python=3.10`
* `streamlit`: UI Framework
* `graphviz`: Graph Rendering Engine (requires system binary)
* `svg-pan-zoom`: JavaScript library (injected via component) for canvas interaction.

```