import streamlit as st


st.set_page_config(
    page_title="RepoMate",
    page_icon="🤖",
    layout="wide",
)


st.title("🤖 RepoMate")
st.subheader("AI GitHub Repository Assistant")

st.write(
    "Ask questions about a GitHub repository using natural language."
)

st.divider()

repo_url = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/Shashankreddy9/repository",
)

if repo_url:
    st.write("Repository URL:")
    st.code(repo_url)