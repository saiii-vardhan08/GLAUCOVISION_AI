import os

import gdown
import numpy as np
import tensorflow as tf


# ============================================================
# MODEL CONFIGURATION
# ============================================================

MODEL_PATH = "model/best_convnext_fixed.keras"
FILE_ID = "1V5v5ScU0r0ysaxisggFoWSdjqD2Q8OP4"


# ============================================================
# CREATE MODEL DIRECTORY
# ============================================================

os.makedirs("model", exist_ok=True)


# ============================================================
# DOWNLOAD MODEL FROM GOOGLE DRIVE
# ============================================================

if not os.path.exists(MODEL_PATH):

    print("Model not found. Downloading from Google Drive...")

    url = f"https://drive.google.com/uc?id={FILE_ID}"

    gdown.download(
        url,
        MODEL_PATH,
        quiet=False
    )

    print("Model downloaded successfully.")


# ============================================================
# LAZY MODEL LOADING
# ============================================================

_model = None


def get_model():

    global _model

    if _model is None:

        print("Loading ConvNeXt-Tiny model...")

        _model = tf.keras.models.load_model(
            MODEL_PATH,
            compile=False
        )

        print("Model loaded successfully.")

    return _model


# ============================================================
# GLAUCOMA PREDICTION
# ============================================================

def predict_glaucoma(image):

    # Load model only when first prediction is requested
    model = get_model()

    # Resize image to model input size
    image = image.resize((384, 384))

    # Ensure RGB format
    image = image.convert("RGB")

    # Convert image to NumPy array
    image = np.array(image, dtype=np.float32)

    # Add batch dimension
    image = np.expand_dims(image, axis=0)

    # Run prediction
    prediction = model.predict(
        image,
        verbose=0
    )[0][0]

    # Convert NumPy value to standard Python float
    prediction = float(prediction)


    # ========================================================
    # CLASS MAPPING
    # ========================================================

    if prediction >= 0.5:

        label = "Normal"

    else:

        label = "Glaucoma"


    # ========================================================
    # CONFIDENCE SCORE
    # ========================================================

    confidence = max(
        prediction,
        1 - prediction
    ) * 100


    # ========================================================
    # RISK ASSESSMENT
    # ========================================================

    if prediction >= 0.80:

        risk = "🟢 Low Risk"

    elif prediction >= 0.50:

        risk = "🟡 Moderate Risk"

    else:

        risk = "🔴 High Risk"


    # ========================================================
    # RETURN RESULTS
    # ========================================================

    return (
        label,
        confidence,
        prediction,
        risk
    )