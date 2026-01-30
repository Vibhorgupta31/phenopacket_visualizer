import json
import os
from src import loader
import streamlit as st

# default file for the web app
DEFAULT_PATH = os.path.join("data", "raw", "FGFR2", "PMID_23546041_Patient_1.json")


def load_upload_file():
    '''
    - Create a file uploader in the sidebar
    - If file is uploaded parse it, otherwise uses the default file
    - Store the result in the session state [ streamlit function ] so that it persists across pages
    :return: dictionary data
    '''
    st.sidebar.title("🧬 Phenopacket Visualizer")

    st.sidebar.header("Data Source 📄")

    # File uploader widget
    uploaded_file = st.sidebar.file_uploader("Upload Phenopacket File (JSON)", type=["json"])

    data = None

    if uploaded_file is not None:
        try:
            data = json.load(uploaded_file)
            st.sidebar.success(f'Loaded: {uploaded_file.name}')
        except Exception as e:
            st.sidebar.error(f'Error reading file: {e}')

    else:
        st.sidebar.info('Using Default File')
        try:
            data = loader.load_data(DEFAULT_PATH)
        except Exception as e:
            st.sidebar.error(f'Default file could not be loaded: {e}')

    if data:
        # session state to use the data across pages
        st.session_state["phenopacket"] = data

    return data
