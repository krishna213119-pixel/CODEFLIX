import streamlit as st
import requests
import textwrap


# =====================================
# CONFIGURATION
# =====================================

API_URL = "https://codeflix-backend-rvj.onrender.com"

st.set_page_config(
    page_title="CODEFLIX AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =====================================
# HELPER FUNCTIONS
# =====================================

def render_html(html):
    """
    Render HTML without Markdown converting
    indented HTML into a code block.
    """
    st.markdown(
        textwrap.dedent(html),
        unsafe_allow_html=True
    )


def get_json_response(response):
    """
    Safely read JSON from a backend response.
    Returns None if the response is not JSON.
    """
    content_type = response.headers.get(
        "content-type",
        ""
    ).lower()

    if "application/json" not in content_type:
        return None

    try:
        return response.json()

    except ValueError:
        return None


def show_backend_error(
    response,
    default_message
):
    """
    Display backend errors safely.
    """

    data = get_json_response(response)

    if data is not None:

        detail = data.get(
            "detail",
            data.get(
                "message",
                default_message
            )
        )

        st.error(
            f"Backend error: {detail}"
        )

    else:

        st.error(
            f"{default_message} "
            f"Status code: {response.status_code}"
        )

        if response.text:

            with st.expander(
                "View backend response"
            ):

                st.code(
                    response.text[:1500]
                )


# =====================================
# PAGE CSS
# =====================================

render_html(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at top right,
                rgba(229, 9, 20, 0.18),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #050505,
                #0d0d0d
            );

        color: white;
    }


    .block-container {
        max-width: 1250px;
        padding-top: 1.5rem;
        padding-bottom: 4rem;
    }


    #MainMenu {
        visibility: hidden;
    }


    footer {
        visibility: hidden;
    }


    header {
        background: transparent !important;
    }


    .logo {
        color: #e50914;
        font-size: 3rem;
        font-weight: 900;
        letter-spacing: -2px;

        text-shadow:
            0 0 15px
            rgba(229, 9, 20, 0.35);
    }


    .subtitle {
        color: #a8a8a8;
        font-size: 1rem;
        margin-bottom: 2rem;
    }


    .hero {
        padding: 4rem;
        margin-bottom: 2.5rem;

        border-radius: 20px;

        background:
            linear-gradient(
                90deg,
                rgba(0, 0, 0, 0.98),
                rgba(20, 5, 5, 0.85)
            );

        border:
            1px solid
            rgba(229, 9, 20, 0.35);

        box-shadow:
            0 15px 60px
            rgba(0, 0, 0, 0.8);
    }


    .hero-title {
        color: white;

        font-size: 3.8rem;
        font-weight: 900;

        line-height: 1.05;

        margin-bottom: 1.2rem;
    }


    .red-text {
        color: #e50914;
    }


    .hero-description {
        max-width: 720px;

        color: #c5c5c5;

        font-size: 1.15rem;

        line-height: 1.8;
    }


    .section-title {
        color: white;

        font-size: 1.5rem;

        font-weight: 800;

        margin-top: 2rem;

        margin-bottom: 1rem;
    }


    .feature-card {
        min-height: 165px;

        padding: 1.5rem;

        border-radius: 16px;

        background:
            linear-gradient(
                145deg,
                #181818,
                #0c0c0c
            );

        border:
            1px solid
            #303030;

        transition:
            transform 0.25s,
            border-color 0.25s;
    }


    .feature-card:hover {
        transform:
            translateY(-5px);

        border-color:
            #e50914;

        box-shadow:
            0 10px 30px
            rgba(229, 9, 20, 0.18);
    }


    .card-icon {
        font-size: 2rem;
    }


    .card-title {
        color: white;

        font-size: 1.1rem;

        font-weight: 800;

        margin-top: 0.7rem;
    }


    .card-text {
        color: #9c9c9c;

        font-size: 0.9rem;

        margin-top: 0.4rem;

        line-height: 1.5;
    }


    .stTextInput input {
        color: white !important;

        background:
            #151515 !important;

        border:
            1px solid
            #383838 !important;

        border-radius:
            9px !important;

        padding:
            0.9rem !important;
    }


    .stTextInput input:focus {
        border-color:
            #e50914 !important;

        box-shadow:
            0 0 0 1px
            #e50914 !important;
    }


    .stButton button {
        width: 100%;

        color: white !important;

        font-weight: 800 !important;

        border: none !important;

        border-radius:
            9px !important;

        padding:
            0.75rem !important;

        background:
            linear-gradient(
                135deg,
                #e50914,
                #a9070f
            ) !important;
    }


    .stButton button:hover {
        background:
            linear-gradient(
                135deg,
                #ff202b,
                #e50914
            ) !important;

        box-shadow:
            0 6px 25px
            rgba(229, 9, 20, 0.4);
    }


    [data-testid="stChatMessage"] {
        background:
            rgba(20, 20, 20, 0.9);

        border:
            1px solid
            #303030;

        border-radius:
            14px;

        padding:
            1rem;
    }


    [data-testid="stChatInput"] {
        background:
            #111111;

        border:
            1px solid
            #393939;

        border-radius:
            12px;
    }


    [data-testid="stMetric"] {
        background:
            #141414;

        border:
            1px solid
            #303030;

        border-radius:
            12px;

        padding:
            1rem;
    }


    .footer {
        color: #666666;

        text-align: center;

        padding-top: 4rem;

        font-size: 0.85rem;
    }

    </style>
    """
)


# =====================================
# SESSION STATE
# =====================================

if "repository_indexed" not in st.session_state:

    st.session_state.repository_indexed = False


if "messages" not in st.session_state:

    st.session_state.messages = []


if "repo_name" not in st.session_state:

    st.session_state.repo_name = ""


# =====================================
# HEADER
# =====================================

render_html(
    """
    <div class="logo">
        CODEFLIX
    </div>

    <div class="subtitle">
        AI-powered GitHub repository intelligence
    </div>
    """
)


# =====================================
# HERO
# =====================================

render_html(
    """
    <div class="hero">

        <div class="hero-title">
            Your code.<br>

            <span class="red-text">
                Explained by AI.
            </span>
        </div>

        <div class="hero-description">

            Add a GitHub repository, let AI understand
            the codebase, and ask questions about
            files, architecture, logic, and implementation.

        </div>

    </div>
    """
)


# =====================================
# FEATURE CARDS
# =====================================

col1, col2, col3 = st.columns(3)


with col1:

    render_html(
        """
        <div class="feature-card">

            <div class="card-icon">
                📂
            </div>

            <div class="card-title">
                Repository Analysis
            </div>

            <div class="card-text">
                Index GitHub repositories
                automatically.
            </div>

        </div>
        """
    )


with col2:

    render_html(
        """
        <div class="feature-card">

            <div class="card-icon">
                🧠
            </div>

            <div class="card-title">
                AI Code Understanding
            </div>

            <div class="card-text">
                Ask questions about your
                complete codebase.
            </div>

        </div>
        """
    )


with col3:

    render_html(
        """
        <div class="feature-card">

            <div class="card-icon">
                🔍
            </div>

            <div class="card-title">
                Source-Aware Answers
            </div>

            <div class="card-text">
                See the repository files
                supporting each answer.
            </div>

        </div>
        """
    )


# =====================================
# INDEX REPOSITORY
# =====================================

render_html(
    """
    <div class="section-title">
        📂 Add a Repository
    </div>
    """
)


repo_url = st.text_input(
    "GitHub Repository URL",
    placeholder=(
        "https://github.com/"
        "username/repository"
    ),
    label_visibility="collapsed"
)


if st.button(
    "▶ INDEX REPOSITORY",
    use_container_width=True
):

    if not repo_url.strip():

        st.warning(
            "Enter a GitHub repository URL."
        )

    else:

        with st.spinner(
            "AI is analyzing the repository..."
        ):

            try:

                response = requests.post(
                    f"{API_URL}/index/",
                    json={
                        "repo_url": repo_url.strip()
                    },
                    timeout=300
                )


                if response.ok:

                    data = get_json_response(
                        response
                    )


                    if data is None:

                        st.error(
                            "The backend returned "
                            "an invalid response."
                        )

                    else:

                        st.session_state.repository_indexed = True

                        st.session_state.messages = []

                        st.session_state.repo_name = (
                            repo_url.rstrip("/")
                            .split("/")[-1]
                        )

                        st.success(
                            "Repository indexed successfully!"
                        )


                        metric1, metric2, metric3 = (
                            st.columns(3)
                        )


                        metric1.metric(
                            "Repository",
                            st.session_state.repo_name
                        )


                        metric2.metric(
                            "Documents",
                            data.get(
                                "documents",
                                0
                            )
                        )


                        metric3.metric(
                            "AI Chunks",
                            data.get(
                                "chunks",
                                0
                            )
                        )


                else:

                    show_backend_error(
                        response,
                        "Repository indexing failed."
                    )


            except requests.exceptions.Timeout:

                st.error(
                    "The backend took too long. "
                    "Render may be waking up. "
                    "Please try again."
                )


            except requests.exceptions.ConnectionError:

                st.error(
                    "Cannot connect to the "
                    "Render backend."
                )


            except requests.exceptions.RequestException as error:

                st.error(
                    f"Request failed: {error}"
                )


# =====================================
# CHAT
# =====================================

st.divider()


if st.session_state.repository_indexed:

    render_html(
        f"""
        <div class="section-title">

            💬 Ask CODEFLIX

            <span class="red-text">
                · {st.session_state.repo_name}
            </span>

        </div>
        """
    )

else:

    render_html(
        """
        <div class="section-title">
            💬 Ask CODEFLIX
        </div>
        """
    )


# =====================================
# DISPLAY CHAT HISTORY
# =====================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# =====================================
# CHAT INPUT
# =====================================

question = st.chat_input(
    "Ask anything about this repository..."
)


if question:

    if not st.session_state.repository_indexed:

        st.warning(
            "Index a repository before "
            "asking questions."
        )

    else:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )


        with st.chat_message("user"):

            st.write(question)


        with st.chat_message("assistant"):

            with st.spinner(
                "CODEFLIX is analyzing the code..."
            ):

                try:

                    response = requests.post(
                        f"{API_URL}/chat/",
                        json={
                            "question": question
                        },
                        timeout=300
                    )


                    if response.ok:

                        data = get_json_response(
                            response
                        )


                        if data is None:

                            st.error(
                                "The backend returned "
                                "invalid JSON."
                            )

                        else:

                            answer = data.get(
                                "answer",
                                "No answer was returned."
                            )


                            st.markdown(
                                answer
                            )


                            if data.get(
                                "sources"
                            ):

                                with st.expander(
                                    "📄 View Sources"
                                ):

                                    for source in data[
                                        "sources"
                                    ]:

                                        st.code(
                                            source
                                        )


                            st.session_state.messages.append(
                                {
                                    "role": "assistant",
                                    "content": answer
                                }
                            )


                    else:

                        show_backend_error(
                            response,
                            "Unable to generate an answer."
                        )


                except requests.exceptions.Timeout:

                    st.error(
                        "The AI response took too long. "
                        "Please try again."
                    )


                except requests.exceptions.ConnectionError:

                    st.error(
                        "Cannot connect to the "
                        "Render backend."
                    )


                except requests.exceptions.RequestException as error:

                    st.error(
                        f"Request failed: {error}"
                    )


# =====================================
# FOOTER
# =====================================

render_html(
    """
    <div class="footer">

        CODEFLIX AI ·
        GitHub Repository Intelligence

    </div>
    """
)