import streamlit as st

from github_service import get_repository
from repository_service import get_repository_files
from qa_service import answer_repository_question


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


# Session state
if "repository" not in st.session_state:
    st.session_state.repository = None

if "files" not in st.session_state:
    st.session_state.files = []

if "repo_url" not in st.session_state:
    st.session_state.repo_url = ""

if "answer" not in st.session_state:
    st.session_state.answer = None


# Repository input
with st.form("repository_form"):

    repo_url = st.text_input(
        "GitHub Repository URL",
        value=st.session_state.repo_url,
        placeholder="https://github.com/username/repository",
    )

    analyze_clicked = st.form_submit_button(
        "Analyze Repository"
    )


if analyze_clicked:

    if not repo_url:

        st.warning(
            "Please enter a GitHub repository URL."
        )

    else:

        with st.spinner("Analyzing repository..."):

            try:

                repository = get_repository(
                    repo_url
                )

                files = get_repository_files(
                    repo_url
                )

                st.session_state.repository = repository
                st.session_state.files = files
                st.session_state.repo_url = repo_url
                st.session_state.answer = None

            except Exception as error:

                st.error(
                    f"Error: {error}"
                )


# Display repository
if st.session_state.repository:

    repository = st.session_state.repository
    files = st.session_state.files

    if "error" in repository:

        st.error(repository["error"])

    else:

        st.success(
            "Repository loaded successfully!"
        )

        st.subheader(
            repository["name"]
        )

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

        st.subheader(
            "Repository Files"
        )

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

            st.info(
                "No files found in the repository."
            )

        st.divider()

        # Q&A section
        st.subheader(
            "Ask RepoMate"
        )

        with st.form("question_form"):

            question = st.text_input(
                "Ask a question about this repository",
                placeholder="What does github_service.py do?",
            )

            ask_clicked = st.form_submit_button(
                "Ask RepoMate"
            )

        if ask_clicked:

            if not question:

                st.warning(
                    "Please enter a question."
                )

            else:

                with st.spinner(
                    "Searching the repository and generating an answer..."
                ):

                    try:

                        st.session_state.answer = (
                            answer_repository_question(
                                st.session_state.repo_url,
                                question,
                            )
                        )

                    except Exception as error:

                        st.error(
                            f"Error generating answer: {error}"
                        )


        # Display answer
        if st.session_state.answer:

            st.markdown(
                "### Answer"
            )

            st.write(
                st.session_state.answer
            )


