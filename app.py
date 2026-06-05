import random

import streamlit as st


INDUSTRIES = [
    "healthcare",
    "education",
    "urban farming",
    "live music",
    "disaster response",
    "local restaurants",
    "personal finance",
    "public transit",
    "fitness",
    "climate action",
]

TECHNOLOGIES = [
    "computer vision",
    "voice assistants",
    "augmented reality",
    "predictive analytics",
    "wearable sensors",
    "blockchain",
    "robotics",
    "natural language processing",
    "IoT devices",
    "generative AI",
]

TWISTS = [
    "for people who only have five minutes a day",
    "that works entirely offline",
    "with a chaotic game-show scoring system",
    "built for teams of strangers",
    "that turns progress into collectible badges",
    "designed for midnight emergencies",
    "using only recycled hardware",
    "where every decision has a tiny plot twist",
    "that explains itself like a friendly coach",
    "optimized for neighborhoods, not individuals",
]


def generate_idea():
    industry = random.choice(INDUSTRIES)
    technology = random.choice(TECHNOLOGIES)
    twist = random.choice(TWISTS)
    return industry, technology, twist


st.set_page_config(
    page_title="Hackathon Idea Generator",
    page_icon=":bulb:",
    layout="centered",
)

st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(255, 204, 128, 0.22), transparent 32rem),
                linear-gradient(135deg, #f8fafc 0%, #eef2ff 48%, #f7fee7 100%);
        }

        .block-container {
            max-width: 760px;
            padding-top: 4rem;
        }

        h1 {
            color: #172033;
            font-size: 3rem !important;
            letter-spacing: 0;
            line-height: 1.05;
            margin-bottom: 0.5rem;
        }

        .intro {
            color: #475569;
            font-size: 1.1rem;
            margin-bottom: 2rem;
        }

        div.stButton > button {
            width: 100%;
            border: 0;
            border-radius: 8px;
            background: #2563eb;
            color: white;
            font-size: 1.25rem;
            font-weight: 700;
            padding: 0.9rem 1.25rem;
            box-shadow: 0 14px 28px rgba(37, 99, 235, 0.25);
        }

        div.stButton > button:hover {
            background: #1d4ed8;
            color: white;
            border: 0;
        }

        .idea-card {
            margin-top: 2rem;
            padding: 1.5rem;
            border: 1px solid rgba(15, 23, 42, 0.1);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.86);
            box-shadow: 0 18px 45px rgba(15, 23, 42, 0.12);
        }

        .idea-label {
            color: #64748b;
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 0.75rem;
        }

        .idea-text {
            color: #111827;
            font-size: 1.55rem;
            font-weight: 800;
            line-height: 1.25;
            margin-bottom: 1rem;
        }

        .idea-parts {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }

        .pill {
            border-radius: 999px;
            background: #e0f2fe;
            color: #075985;
            font-size: 0.9rem;
            font-weight: 700;
            padding: 0.35rem 0.7rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Hackathon Idea Generator")
st.markdown(
    '<p class="intro">Press the button and get a delightfully weird build prompt.</p>',
    unsafe_allow_html=True,
)

if st.button("Generate Idea", type="primary"):
    industry, technology, twist = generate_idea()
    idea = f"A {technology} project for {industry} {twist}."

    st.markdown(
        f"""
        <div class="idea-card">
            <div class="idea-label">Your hackathon idea</div>
            <div class="idea-text">{idea}</div>
            <div class="idea-parts">
                <span class="pill">{industry.title()}</span>
                <span class="pill">{technology.title()}</span>
                <span class="pill">{twist.title()}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
