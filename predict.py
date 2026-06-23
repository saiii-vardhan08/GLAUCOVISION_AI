import tensorflow as tf
import numpy as np
from PIL import Image

import os
import gdown

MODEL_PATH = "model/best_convnext_fixed.keras"

FILE_ID = "1V5v5ScU0r0ysaxisggFoWSdjqD2Q8OP4"

os.makedirs(
    "model",
    exist_ok=True
)

if not os.path.exists(MODEL_PATH):

    url = f"https://drive.google.com/uc?id={FILE_ID}"

    gdown.download(
        url,
        MODEL_PATH,
        quiet=False
    )

model = tf.keras.models.load_model(
    MODEL_PATH,
    compile=False
)

def predict_glaucoma(image):

    # Resize image
    image = image.resize((384, 384))

    # Convert to RGB
    image = image.convert("RGB")

    # Convert to numpy
    image = np.array(image)

    # Convert to float32
    image = image.astype(np.float32)

    # Add batch dimension
    image = np.expand_dims(image, axis=0)

    # Predict
    prediction = model.predict(
        image,
        verbose=0
    )[0][0]

    # Class Mapping
    if prediction >= 0.5:

        label = "Normal"

    else:

        label = "Glaucoma"

    confidence = max(
        prediction,
        1 - prediction
    ) * 100

    # Risk Logic
    if prediction >= 0.80:

        risk = "🟢 Low Risk"

    elif prediction >= 0.50:

        risk = "🟡 Moderate Risk"

    else:

        risk = "🔴 High Risk"

    return (
        label,
        confidence,
        prediction,
        risk
    )

def get_model():

    return model
