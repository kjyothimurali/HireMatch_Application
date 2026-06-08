import streamlit as st

from utils.predictor import predict_sector
from utils.role_predictor import predict_role
from utils.pdf_reader import extract_pdf
from utils.history import save_history

st.title("📄 Job Analysis")

input_method = st.radio(
    "Choose Input Method",
    [
        "Paste JD",
        "Upload PDF"
    ]
)

text = ""

if input_method == "Paste JD":

    text = st.text_area(
        "Paste Job Description",
        height=300
    )

else:

    uploaded_file = st.file_uploader(
        "Upload JD PDF",
        type=["pdf"]
    )

    if uploaded_file:

        text = extract_pdf(
            uploaded_file
        )

if st.button(
    "Analyze Job"
):

    if not text.strip():

        st.warning(
            "Provide Job Description"
        )

    else:

        with st.spinner(
            "Analyzing..."
        ):

            sector, confidence = (
                predict_sector(text)
            )

            if sector == "Other / Unknown":

                st.error(
                    "Unknown Sector"
                )

            else:

                role, similarity = (
                    predict_role(
                        text,
                        sector
                    )
                )

                save_history(
                    "Job Analysis",
                    sector,
                    role,
                    round(
                        similarity * 100,
                        2
                    )
                )

                col1, col2 = (
                    st.columns(2)
                )

                with col1:

                    st.success(
                        f"Sector: {sector}"
                    )

                    st.metric(
                        "Confidence",
                        f"{confidence*100:.2f}%"
                    )

                with col2:

                    st.success(
                        f"Role: {role}"
                    )

                    st.metric(
                        "Similarity",
                        f"{similarity*100:.2f}%"
                    )

                with st.expander(
                    "View Extracted Text"
                ):

                    st.write(
                        text[:5000]
                    )