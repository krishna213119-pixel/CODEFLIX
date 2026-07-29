import streamlit as st
import requests


# =====================================
# CONFIG
# =====================================

API_URL = "https://codeflix-backend-rvij.onrender.com"


st.set_page_config(
    page_title="CodeFlix AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =====================================
# NETFLIX-INSPIRED CSS
# =====================================

st.markdown(
    """
    <style>

    /* Main background */

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

        color: #ffffff;
    }


    /* Remove default top spacing */

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }


    /* Hide Streamlit branding */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }


    /* Main logo */

    .logo {
        color: #e50914;
        font-size: 3rem;
        font-weight: 900;
        letter-spacing: -2px;
        margin-bottom: 0;
        text-shadow:
            0 0 15px
            rgba(229, 9, 20, 0.35);
    }


    /* Subtitle */

    .subtitle {
        color: #b3b3b3;
        font-size: 1.05rem;
        margin-top: -10px;
        margin-bottom: 2rem;
    }


    /* Hero section */

    .hero {
        padding: 3.5rem;
        border-radius: 20px;

        background:
            linear-gradient(
                90deg,
                rgba(0, 0, 0, 0.98),
                rgba(0, 0, 0, 0.72)
            );

        border:
            1px solid
            rgba(229, 9, 20, 0.25);

        box-shadow:
            0 15px 60px
            rgba(0, 0, 0, 0.8);

        margin-bottom: 2rem;
    }


    .hero-title {
        font-size: 3.4rem;
        font-weight: 900;
        line-height: 1.05;
        margin-bottom: 1rem;
    }


    .red-text {
        color: #e50914;
    }


    .hero-description {
        color: #c7c7c7;
        font-size: 1.1rem;
        max-width: 700px;
        line-height: 1.7;
    }


    /* Section titles */

    .section-title {
        font-size: 1.45rem;
        font-weight: 750;
        margin-top: 1.5rem;
        margin-bottom: 0.7rem;
    }


    /* Cards */

    .feature-card {
        background:
            linear-gradient(
                145deg,
                #151515,
                #0c0c0c
            );

        border:
            1px solid
            #252525;

        border-radius: 15px;

        padding: 1.3rem;

        min-height: 130px;

        transition: 0.3s;
    }


    .feature-card:hover {
        border-color: #e50914;

        transform:
            translateY(-4px);

        box-shadow:
            0 10px 30px
            rgba(229, 9, 20, 0.16);
    }


    .card-icon {
        font-size: 1.8rem;
    }


    .card-title {
        font-size: 1.05rem;
        font-weight: 700;
        margin-top: 0.5rem;
    }


    .card-text {
        color: #999999;
        font-size: 0.88rem;
    }


    /* Input */

    .stTextInput input {
        background-color: #141414 !important;

        color: white !important;

        border:
            1px solid
            #333333 !important;

        border-radius: 8px !important;

        padding: 0.8rem !important;
    }


    .stTextInput input:focus {
        border:
            1px solid
            #e50914 !important;

        box-shadow:
            0 0 0 1px
            #e50914 !important;
    }


    /* Red buttons */

    .stButton button {
        width: 100%;

        background:
            linear-gradient(
                135deg,
                #e50914,
                #b20710
            ) !important;

        color: white !important;

        border: none !important;

        border-radius: 7px !important;

        font-weight: 700 !important;

        padding: 0.7rem !important;

        transition: 0.25s;
    }


    .stButton button:hover {
        background:
            linear-gradient(
                135deg,
                #ff1f2a,
                #e50914
            ) !important;

        transform:
            scale(1.01);

        box-shadow:
            0 5px 22px
            rgba(229, 9, 20, 0.4);
    }


    /* Chat */

    [data-testid="stChatMessage"] {
        background-color:
            rgba(20, 20, 20, 0.85);

        border:
            1px solid
            #292929;

        border-radius: 14px;

        padding: 1rem;

        margin-bottom: 0.8rem;
    }


    /* Chat input */

    [data-testid="stChatInput"] {
        border:
            1px solid
            #333333;

        border-radius: 12px;

        background:
            #111111;
    }


    /* Metrics */

    [data-testid="stMetric"] {
        background:
            #121212;

        border:
            1px solid
            #292929;

        padding: 1rem;

        border-radius: 12px;
    }


    /* Divider */

    hr {
        border-color: #252525;
    }


    /* Success message */

    .stSuccess {
        background:
            rgba(20, 120, 50, 0.15);

        border:
            1px solid
            rgba(40, 180, 80, 0.4);
    }


    /* Footer */

    .footer {
        color: #666666;
        text-align: center;
        padding-top: 3rem;
        font-size: 0.85rem;
    }

    </style>
    """,
    unsafe_allow_html=True
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

st.markdown(
    """
    <div class="logo">
        CODEFLIX
    </div>

    <div class="subtitle">
        AI-powered GitHub repository intelligence
    </div>
    """,
    unsafe_allow_html=True
)


# =====================================
# HERO
# =====================================

# =====================================
# HERO
# =====================================

st.markdown(
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
""",
    unsafe_allow_html=True
)

# =====================================
# FEATURES
# =====================================

# =====================================
# FEATURES
# =====================================

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        """
<div class="feature-card">

<div class="card-icon">
📂
</div>

<div class="card-title">
Repository Analysis
</div>

<div class="card-text">
Index GitHub repositories automatically.
</div>

</div>
""",
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
<div class="feature-card">

<div class="card-icon">
🧠
</div>

<div class="card-title">
AI Code Understanding
</div>

<div class="card-text">
Ask questions about your complete codebase.
</div>

</div>
""",
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        """
<div class="feature-card">

<div class="card-icon">
🔍
</div>

<div class="card-title">
Source-Aware Answers
</div>

<div class="card-text">
See which repository files support the answer.
</div>

</div>
""",
        unsafe_allow_html=True
    )


# =====================================
# INDEX REPOSITORY
# =====================================

st.markdown(
    '<div class="section-title">'
    '📂 Add a Repository'
    '</div>',
    unsafe_allow_html=True
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

    if not repo_url:

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
                        "repo_url": repo_url
                    },
                    timeout=300
                )


                if response.status_code == 200:

                    data = response.json()

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
                        data["documents"]
                    )

                    metric3.metric(
                        "AI Chunks",
                        data["chunks"]
                    )


                else:

                    detail = (
                        response.json()
                        .get(
                            "detail",
                            "Repository indexing failed."
                        )
                    )

                    st.error(detail)


            except requests.exceptions.ConnectionError:

                st.error(
                    "FastAPI is not running. "
                    "Start the backend first."
                )


            except requests.exceptions.Timeout:

                st.error(
                    "Indexing took too long."
                )


# =====================================
# CHAT
# =====================================

st.divider()


if st.session_state.repository_indexed:

    st.markdown(
        f"""
        <div class="section-title">
            💬 Ask CODEFLIX
            <span class="red-text">
                · {st.session_state.repo_name}
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        """
        <div class="section-title">
            💬 Ask CODEFLIX
        </div>
        """,
        unsafe_allow_html=True
    )


# Display old messages

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )


# User input

question = st.chat_input(
    "Ask anything about this repository..."
)


if question:

    if not st.session_state.repository_indexed:

        st.warning(
            "Index a repository before asking questions."
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
                        timeout=180
                    )


                    if response.status_code == 200:

                        data = response.json()

                        answer = data["answer"]

                        st.write(answer)


                        if data.get("sources"):

                            with st.expander(
                                "📄 View Sources"
                            ):

                                for source in data[
                                    "sources"
                                ]:

                                    st.code(
                                        source,
                                        language=None
                                    )


                        st.session_state.messages.append(
                            {
                                "role": "assistant",
                                "content": answer
                            }
                        )


                    else:

                        detail = (
                            response.json()
                            .get(
                                "detail",
                                "Unable to generate an answer."
                            )
                        )

                        st.error(detail)


                except requests.exceptions.ConnectionError:

                    st.error(
                        "Cannot connect to FastAPI."
                    )


                except requests.exceptions.Timeout:

                    st.error(
                        "The AI response timed out."
                    )


# =====================================
# FOOTER
# =====================================

st.markdown(
    """
    <div class="footer">

        CODEFLIX AI ·
        GitHub Repository Intelligence

    </div>
    """,
    unsafe_allow_html=True
)