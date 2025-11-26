import streamlit as st

st.set_page_config(page_title="AGILE-GEN", layout="wide")

# ---------- RULE-BASED CORE LOGIC ---------- #

def generate_epics(domain):
    return [
        f"Improve {domain} system usability",
        f"Enhance automation in {domain} workflows",
        f"Ensure robust security for all {domain} operations"
    ]

def generate_features(epic):
    return [
        f"{epic} – Feature: User Interface Enhancement",
        f"{epic} – Feature: Process Automation Engine",
        f"{epic} – Feature: Security & Access Control Module"
    ]

def generate_user_story(feature):
    return f"As a user, I want {feature.lower()} so that I can achieve better efficiency."

def generate_tasks(story):
    return [
        f"Analyze requirements for: {story}",
        f"Design module for: {story}",
        f"Implement logic for: {story}",
        f"Perform testing for: {story}"
    ]

def generate_acceptance_criteria(story):
    return [
        f"The system must allow the user to complete the action described in: {story}",
        f"The output must be consistent and predictable.",
        f"Errors must be clearly communicated to the user.",
        f"The feature must pass functional and integration tests."
    ]

def evaluate_smm(story):
    score = 0
    if "as a" in story.lower(): score += 1
    if "so that" in story.lower(): score += 1
    if len(story.split()) > 12: score += 1
    if story.endswith("."): score += 1

    if score == 1:
        level = "SMM LEVEL-1: Basic Story"
    elif score == 2:
        level = "SMM LEVEL-2: Intermediate"
    elif score == 3:
        level = "SMM LEVEL-3: Advanced"
    else:
        level = "SMM LEVEL-4: Mature Story"

    return level

def agile_rgm_mapping():
    return {
        "Education Phase": "Understanding domain, constraints, stakeholders.",
        "Feature Phase": "High-level solution extraction.",
        "Story Phase": "Breakdown into user stories.",
        "Task Phase": "Convert stories into executable tasks.",
        "Parallel Concurrency": "All phases can run iteratively and concurrently."
    }


# ---------- STREAMLIT UI ---------- #

st.title("🚀 AGILE-GEN: Intelligent Agile Requirements & Storycard Generator")
st.write("### A Real-Time Rule-Based Agile Engineering Tool")

st.divider()

domain = st.text_input("Enter Project Domain (e.g., Healthcare, Banking, E-Commerce):")

if domain:
    st.subheader("📌 Generated Epics")
    epics = generate_epics(domain)
    for epic in epics:
        st.write(f"- {epic}")

    st.subheader("🧩 Features from Epics")
    for epic in epics:
        st.markdown(f"**Epic:** {epic}")
        features = generate_features(epic)
        for f in features:
            st.write(f"  - {f}")

    st.subheader("📝 Auto-Generated User Stories")
    stories = []
    for epic in epics:
        for f in generate_features(epic):
            story = generate_user_story(f)
            stories.append(story)
            st.write(f"- {story}")

    st.subheader("📐 Acceptance Criteria")
    for story in stories:
        st.markdown(f"**Story:** {story}")
        for ac in generate_acceptance_criteria(story):
            st.write(f"- {ac}")

    st.subheader("🧪 Storycard Maturity Model (SMM) Evaluation")
    for s in stories:
        st.write(f"**Story:** {s}")
        st.success(evaluate_smm(s))

    st.subheader("🔄 Agile RGM Mapping")
    mapping = agile_rgm_mapping()
    for phase, explanation in mapping.items():
        st.write(f"**{phase}:** {explanation}")

    st.toast("Agile Requirements Generated Successfully!", icon="🚀")
