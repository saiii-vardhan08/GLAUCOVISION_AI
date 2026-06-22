from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime


def create_pdf_report(
    image_path,
    diagnosis,
    confidence,
    probability,
    risk
):

    pdf_path = "reports/glaucoma_report.pdf"

    doc = SimpleDocTemplate(
        pdf_path
    )

    styles = getSampleStyleSheet()

    content = []

    # =====================================
    # HEADER
    # =====================================

    title = Paragraph(
        "GLAUCOVISION AI",
        styles["Title"]
    )

    content.append(title)

    subtitle = Paragraph(
        "AI-Powered Glaucoma Screening Report",
        styles["Heading2"]
    )

    content.append(subtitle)

    content.append(
        Spacer(1, 20)
    )

    # =====================================
    # DATE
    # =====================================

    content.append(
        Paragraph(
            f"<b>Report Generated:</b> {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    # =====================================
    # IMAGE
    # =====================================

    content.append(
        Paragraph(
            "<b>Patient Retinal Scan</b>",
            styles["Heading3"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    fundus_img = Image(
        image_path,
        width=250,
        height=250
    )

    content.append(
        fundus_img
    )

    content.append(
        Spacer(1, 20)
    )

    # =====================================
    # RESULTS
    # =====================================

    content.append(
        Paragraph(
            "<b>AI Screening Results</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    content.append(
        Paragraph(
            f"<b>Diagnosis:</b> {diagnosis}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Confidence:</b> {confidence:.2f}%",
            styles["Normal"]
        )
    )
    
    content.append(
    Paragraph(
        f"<b>Probability:</b> {probability:.4f}",
        styles["Normal"]
    )
)

    content.append(
        Paragraph(
            f"<b>Risk Level:</b> {risk}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    # =====================================
    # MODEL INFO
    # =====================================

    content.append(
        Paragraph(
            "<b>Model Information</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            "Model: ConvNeXt-Tiny",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            "Test Accuracy: 89.35%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            "ROC-AUC Score: 0.953",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    # =====================================
    # RECOMMENDATION
    # =====================================

    if diagnosis.lower() == "normal":

        recommendation = """
        No significant glaucomatous patterns were detected.
        Routine eye examinations are recommended.
        """

    else:

        recommendation = """
        Potential glaucomatous patterns were detected.
        Please consult an ophthalmologist for further
        clinical evaluation.
        """

    content.append(
        Paragraph(
            "<b>Recommendation</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            recommendation,
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    # =====================================
    # DISCLAIMER
    # =====================================

    content.append(
        Paragraph(
            "<b>Disclaimer</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            """
            This report is generated using an AI-based
            glaucoma screening system and is intended
            for educational and screening purposes only.

            It should not be considered a substitute
            for professional medical diagnosis or treatment.
            """,
            styles["Italic"]
        )
    )

    doc.build(
        content
    )

    return pdf_path

