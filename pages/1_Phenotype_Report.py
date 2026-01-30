import streamlit as st
from src import uploader

st.set_page_config(page_title="Phenotype Report", layout="wide")

data = uploader.load_upload_file()

if data:
    st.title("🧬 Proband Phenopacket Profile")
    st.info("Construction in progress, check soon 🚧")
