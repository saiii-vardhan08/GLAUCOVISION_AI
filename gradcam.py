import tensorflow as tf
import numpy as np
import cv2

def generate_gradcam(model, image):

    img = image.resize((384, 384))

    img = np.array(img).astype(np.float32)

    if len(img.shape) == 2:
        img = np.stack([img] * 3, axis=-1)

    img_array = np.expand_dims(img, axis=0)

    # Use ConvNeXt output directly
    feature_extractor = tf.keras.Model(
        inputs=model.input,
        outputs=model.get_layer("convnext_tiny").output
    )

    with tf.GradientTape() as tape:

        features = feature_extractor(img_array)

        tape.watch(features)

        x = model.layers[2](features)
        x = model.layers[3](x)
        x = model.layers[4](x)
        x = model.layers[5](x)
        predictions = model.layers[6](x)

        loss = predictions[:, 0]

    grads = tape.gradient(
        loss,
        features
    )

    pooled_grads = tf.reduce_mean(
        grads,
        axis=(0, 1, 2)
    )

    features = features[0]

    heatmap = tf.reduce_sum(
        pooled_grads * features,
        axis=-1
    )

    heatmap = np.maximum(
        heatmap,
        0
    )

    heatmap = heatmap / (
        np.max(heatmap) + 1e-8
    )

    heatmap = cv2.resize(
        heatmap.numpy(),
        (
            image.size[0],
            image.size[1]
        )
    )

    return heatmap