import streamlit as st

from utils.pdf_reader import extract_pdf

from utils.skill_matcher import (
    match_skills,
    suggest_improvements
)

from utils.history import (
    save_history
)

st.title(
    "📑 Resume Analysis"
)

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

sector = st.selectbox(
    "Select Sector",
    [
        "IT",
        "Finance",
        "Healthcare",
        "Sales & Marketing"
    ]
)

role_map = {

    "IT": [
        "Software Developer",
        "Web Developer",
        "Data Scientist",
        "ML Engineer"
    ],

    "Finance": [
        "Accountant",
        "Financial Analyst",
        "Auditor"
    ],

    "Healthcare": [
        "Doctor",
        "Nurse",
        "Medical Assistant"
    ],

    "Sales & Marketing": [
        "Sales Executive",
        "Marketing Manager",
        "Business Analyst"
    ]
}

role = st.selectbox(
    "Select Role",
    role_map[sector]
)

if st.button(
    "Analyze Resume"
):

    if not resume:

        st.warning(
            "Upload Resume"
        )

    else:

        text = extract_pdf(
            resume
        )

        matched, missing = (
            match_skills(
                text,
                sector
            )
        )

        suggestions = (
            suggest_improvements(
                missing
            )
        )

        total = (
            len(matched)
            +
            len(missing)
        )

        score = 0

        if total > 0:

            score = int(
                (
                    len(matched)
                    / total
                )
                * 100
            )

        save_history(
            "Resume Analysis",
            sector,
            role,
            score
        )

        st.subheader(
            "Resume Match Score"
        )

        st.progress(
            score
        )

        st.success(
            f"{score}% Match"
        )

        st.subheader(
            "Matched Skills"
        )

        if matched:

            for skill in matched:

                st.success(
                    f"✓ {skill}"
                )

        else:

            st.warning(
                "No skills found"
            )

        st.subheader(
            "Missing Skills"
        )

        for skill in missing:

            st.error(
                f"✗ {skill}"
            )

        st.subheader(
            "Recommendations"
        )

        for item in suggestions:

            st.info(
                item
            )