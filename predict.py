import tensorflow as tf
import numpy as np
from PIL import Image

MODEL_PATH = "model/best_convnext_fixed.keras"

# Load model once
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