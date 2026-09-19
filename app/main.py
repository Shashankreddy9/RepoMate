import streamlit as st

from github_service import get_repository
from repository_service import get_repository_files


st.set_page_config(
    page_title="RepoMate",
    page_icon="R",
    layout="wide",
)


st.title("RepoMate")
st.subheader("AI GitHub Repository Assistant")

st.write(
    "Ask questions about a GitHub repository using natural language."
)

st.divider()


repo_url = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/username/repository",
)


if st.button("Analyze Repository"):

    if not repo_url:
        st.warning("Please enter a GitHub repository URL.")

    else:

        with st.spinner("Analyzing repository..."):

            try:
                repository = get_repository(repo_url)
                files = get_repository_files(repo_url)

            except Exception as error:
                st.error(f"Error: {error}")
                st.stop()

        if "error" in repository:

            st.error(repository["error"])

        else:

            st.success("Repository loaded successfully!")

            st.subheader(repository["name"])

            st.write(
                repository["description"]
                or "No description available."
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Stars",
                    repository["stars"],
                )

            with col2:
                st.metric(
                    "Forks",
                    repository["forks"],
                )

            with col3:
                st.metric(
                    "Language",
                    repository["language"]
                    or "Unknown",
                )

            st.write(
                f"Repository: {repository['full_name']}"
            )

            st.link_button(
                "Open on GitHub",
                repository["url"],
            )

            st.divider()

            st.subheader("Repository Files")

            if files:

                st.write(
                    f"Found {len(files)} file(s) in the repository."
                )

                for file in files:

                    st.code(
                        file["path"],
                        language="text",
                    )

            else:

                st.info("No files found in the repository.")