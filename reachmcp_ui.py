import streamlit as st
import requests
import json
import os

st.set_page_config(page_title="ReachMCP UI", layout="centered")

st.title("ReachMCP Reachability Checker")

with st.form("reachability_form"):
    cve_id = st.text_input("CVE ID", "CVE-2021-34527")
    package_name = st.text_input("Package Name", "httpd")
    package_version = st.text_input("Package Version", "2.4.46")
    source_path = st.text_input("Source Path", "./test_package")
    language = st.selectbox("Language", ["python", "java", "javascript"])

    submit_button = st.form_submit_button("Check Reachability")
    
if submit_button:
    with st.spinner("Checking reachability..."):
        req = {
            "cve_id": cve_id,
            "package_name": package_name,
            "package_version": package_version,
            "source_path": source_path,
            "language": language,
        }

        try:
            res = requests.post(
                "http://localhost:8000/reachability",
                json=req
            )
            res.raise_for_status()
            response_data = res.json()

            st.success("Reachability Check Completed")
            st.json(response_data)
        except requests.exceptions.RequestException as e:
            st.error(f"Error: {e}")
            st.error("Please ensure the ReachMCP server is running at http://localhost:8000/reachability")