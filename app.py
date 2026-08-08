import streamlit as st
from PIL import Image
import time
import os

from utils.predict import predict_glaucoma
from utils.pdf_report import create_pdf_report

st.set_page_config(
    page_title="Glaucoma Detection AI",
    page_icon="👁️",
    layout="wide"
)

hero_left, hero_right = st.columns([3, 7])

with hero_left:

    st.subheader("👁️ GLAUCOVISION AI")

    st.caption(
    "AI-Powered Glaucoma Screening System"
)
    st.write(
        """
        Early detection can help prevent vision loss.

        Upload a retinal fundus image and receive
        an AI-powered glaucoma screening report.
        """
    )

    uploaded_file = st.file_uploader(
        "Upload Fundus Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:

        st.success(
            """
            ✅ Analysis completed successfully.

            👇 Detailed screening results are available below.
            Please scroll down to view the report.
            """
        )

        st.markdown(
            "### ⬇ Scroll Down For Results"
        )

    else:

        st.info(
            """
            📌 Please upload a retinal fundus image for accurate glaucoma screening.

            ⚠️ Images such as selfies, signatures, documents,
            handwritten text, objects, or non-retinal photographs
            may produce invalid predictions.
            """
        )

with hero_right:

    st.image(
        "assets/doctor_bg.jpg",
        width="stretch"
    )

st.markdown("---")

st.markdown("""
<style>

/* =========================================================
   GLAUCOVISION AI — THEME AWARE UI
   ========================================================= */


/* ================================
   MAIN BACKGROUND
================================ */

.stApp {
    background: var(--background-color) !important;
    color: var(--text-color) !important;
}


/* ================================
   TEXT
================================ */

h1, h2, h3, h4, h5, h6 {
    color: var(--text-color) !important;
}

p, label {
    color: var(--text-color) !important;
}


/* ================================
   CARDS
================================ */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--secondary-background-color) !important;
    border: 1px solid rgba(128, 128, 128, 0.25) !important;
    border-radius: 18px !important;
    padding: 20px !important;
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.08) !important;
}


/* ================================
   SUCCESS / WARNING / ERROR
================================ */

div[data-baseweb="notification"] {
    border-radius: 14px !important;
}


/* ================================
   BUTTONS
================================ */

.stButton > button,
.stDownloadButton > button {

    background: #73C167 !important;
    color: white !important;

    border: none !important;
    border-radius: 12px !important;

    font-weight: 600 !important;

    padding: 12px 24px !important;

    transition: 0.3s ease !important;
}

.stButton > button:hover,
.stDownloadButton > button:hover {

    background: #5FAE52 !important;
    color: white !important;
}

/* =========================================================
   FILE UPLOADER — DARK OUTLINE
========================================================= */

section[data-testid="stFileUploader"] {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
}


/* Actual drag-and-drop area */

section[data-testid="stFileUploader"]
div[data-testid="stFileUploaderDropzone"] {

    background: var(--secondary-background-color) !important;

    border: none !important;

    border-radius: 16px !important;

    padding: 15px !important;

    /* THIS creates the visible dark box */
    box-shadow: inset 0 0 0 2px #1E293B !important;

    box-sizing: border-box !important;
}


/* Text */

section[data-testid="stFileUploader"]
div[data-testid="stFileUploaderDropzone"] label,
section[data-testid="stFileUploader"]
div[data-testid="stFileUploaderDropzone"] span,
section[data-testid="stFileUploader"]
div[data-testid="stFileUploaderDropzone"] small {

    color: var(--text-color) !important;
}


/* Browse button */

section[data-testid="stFileUploader"]
div[data-testid="stFileUploaderDropzone"] button {

    background: var(--secondary-background-color) !important;

    color: var(--text-color) !important;

    border: 1px solid #1E293B !important;

    border-radius: 8px !important;
}


/* Browse hover */

section[data-testid="stFileUploader"]
div[data-testid="stFileUploaderDropzone"] button:hover {

    border-color: #73C167 !important;

    color: #73C167 !important;
}


/* =========================================================
   METRICS
========================================================= */

div[data-testid="metric-container"] {

    background: var(--secondary-background-color) !important;

    border: 1px solid rgba(128, 128, 128, 0.25) !important;

    border-radius: 14px !important;

    padding: 15px !important;

    box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.05) !important;
}


/* Metric label */

[data-testid="stMetricLabel"] {
    color: var(--text-color) !important;
}


/* Metric value */

[data-testid="stMetricValue"] {
    color: var(--text-color) !important;
    font-weight: 700 !important;
}


/* =========================================================
   IMAGE
========================================================= */

img {
    border-radius: 16px !important;
}


/* =========================================================
   EXPANDER
========================================================= */

details {

    background: var(--secondary-background-color) !important;

    color: var(--text-color) !important;

    border-radius: 12px !important;

    padding: 10px !important;
}

details summary {
    color: var(--text-color) !important;
}


/* =========================================================
   HORIZONTAL LINE
========================================================= */

hr {

    border: 0 !important;

    border-top: 1px solid rgba(128, 128, 128, 0.25) !important;
}


/* =========================================================
   FOOTER
========================================================= */

.footer-text {

    text-align: center;

    color: var(--text-color);

    font-size: 14px;
}


/* =========================================================
   DARK MODE EXTRA CONTRAST
========================================================= */

@media (prefers-color-scheme: dark) {

    section[data-testid="stFileUploader"]
    div[data-testid="stFileUploaderDropzone"] {

        border-color: #CBD5E1 !important;
    }

    section[data-testid="stFileUploader"]
    div[data-testid="stFileUploaderDropzone"] button {

        border-color: #CBD5E1 !important;
    }
}

</style>
""", unsafe_allow_html=True)


if uploaded_file is None:

    card1, card2 = st.columns(2)

    with card1:

        with st.container(border=True):

            left, right = st.columns([4,1])

            with left:

                st.subheader(
                    "What is Glaucoma?"
                )

                st.write(
                    """
                    Glaucoma is a progressive eye disease
                    that damages the optic nerve, which is
                    responsible for carrying visual information
                    from the eye to the brain.

                    Early screening and treatment can help
                    preserve vision and reduce complications.
                    """
                )

            with right:

                st.image(
                    "assets/glaucoma_eye.jpg",
                    width=120
                )

    with card2:

        with st.container(border=True):

            left, right = st.columns([4,1])

            with left:

                st.subheader(
                    "Healthy Eye"
                )

                st.write(
                    """
                    A healthy eye has a balanced optic disc structure and no signs of optic nerve damage. The retinal tissues and blood vessels appear normal and support proper visual function.

Regular eye examinations help detect potential abnormalities at an early stage. 
                    """
                )

            with right:

                st.image(
                    "assets/healthy_eye.jpg",
                    width=120
                )


else:

    try:

        image = Image.open(
            uploaded_file
        )

        image.verify()

        image = Image.open(
            uploaded_file
        )

        with st.spinner(
            "🔍 Analyzing retinal fundus image..."
        ):

            time.sleep(2)

            label, confidence, probability, risk = predict_glaucoma(
                image
            )

        os.makedirs(
            "reports",
            exist_ok=True
        )

        image_path = "reports/uploaded_image.png"

        image.save(
            image_path
        )

        pdf_path = create_pdf_report(
            image_path,
            label,
            confidence,
            probability,
            risk
        )

    except Exception:

        st.error(
            "❌ Unable to process the uploaded image."
        )

        st.stop()
        
    image_col, result_col = st.columns([3,7])

    with image_col:

        st.subheader(
            "Uploaded Fundus Image"
        )

        st.image(
            image,
            width="stretch"
        )

    with result_col:

        st.success(
    "🔍 AI Screening Report"
)

        metric1, metric2 = st.columns(2)

        with metric1:

            if label == "Normal":

                st.success(
        f"Diagnosis: {label}"
    )

            else:

                st.error(
        f"Diagnosis: {label}"
    )

        with metric2:

            st.metric(
                "Confidence",
                f"{confidence:.2f}%"
            )

        metric3, metric4 = st.columns(2)

        with metric3:

            st.write("### Risk Level")

            if "Low Risk" in risk:

                st.success(risk)

            elif "Moderate Risk" in risk:

                st.warning(risk)

            else:

                st.error(risk)

        with metric4:

            st.metric(
                "Probability",
                f"{probability:.4f}"
            )

    st.markdown("---")


    st.subheader(
        "Prediction Explanation"
    )

    if label == "Normal":

        st.success(
            """
            The uploaded retinal image shows characteristics
            consistent with a healthy optic nerve appearance.

            No significant glaucomatous patterns were detected.

            Routine eye examinations are recommended to
            maintain long-term visual health.
            """
        )

    else:

        st.warning(
            """
            The model detected retinal patterns that may
            indicate glaucomatous changes.

            This result should be considered a screening
            indicator and not a final medical diagnosis.

            Please consult an ophthalmologist for further
            clinical evaluation and confirmation.
            """
        )


    st.markdown("### MODEL INFO")

    with st.expander(
        "🤖 Model Information & Performance"
    ):

        st.write(
            """
            **Architecture:** ConvNeXt-Tiny

            **Test Accuracy:** 89.35%

            **ROC-AUC Score:** 0.953

            **Input Resolution:** 384 × 384

            **Framework:** TensorFlow / Keras

            **Purpose:** Glaucoma Screening from
            Retinal Fundus Images
            """
        )


    st.markdown("---")

    with open(
        pdf_path,
        "rb"
    ) as pdf_file:

        st.download_button(
            label="📄 Download Detailed Report",
            data=pdf_file,
            file_name="glaucoma_report.pdf",
            mime="application/pdf",
            use_container_width=True
        )
        

st.markdown("---")

st.markdown("---")

with st.container(border=True):

    st.markdown(
        """
        **GLAUCOVISION AI**

        Powered by ConvNeXt-Tiny • TensorFlow

        Accuracy: 89.35% | ROC-AUC: 0.953

        Educational screening tool only.
        """
    )


    
    