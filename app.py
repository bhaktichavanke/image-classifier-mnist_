from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import tensorflow as tf
import cv2

app = Flask(__name__)
CORS(app)

# Load model
model = tf.keras.models.load_model("model/mnist_model.h5")

# Load accuracy once
(_, _), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_test = x_test / 255.0
x_test = x_test.reshape(-1, 28, 28, 1)

loss, acc = model.evaluate(x_test, y_test, verbose=0)
model_accuracy = round(acc * 100, 2)


@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["file"]

    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)

    # Resize to larger first (important)
    img = cv2.resize(img, (280, 280))

    # Convert to binary (clean strokes)
    _, img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

    # Find bounding box
    coords = cv2.findNonZero(img)
    if coords is not None:
        x, y, w, h = cv2.boundingRect(coords)
        img = img[y:y + h, x:x + w]

    # Resize digit properly
    img = cv2.resize(img, (20, 20))

    # Pad to center (MNIST style)
    img = np.pad(img, ((4, 4), (4, 4)), "constant", constant_values=0)

    # Normalize
    img = img / 255.0

    # Reshape for CNN
    img = img.reshape(1, 28, 28, 1)

    # Predict
    prediction = model.predict(img, verbose=0)
    result = int(np.argmax(prediction))

    return jsonify({
        "prediction": result,
        "accuracy": model_accuracy
    })


if __name__ == "__main__":
    app.run(debug=True)