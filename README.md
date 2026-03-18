#  AI Digit Classifier (CNN + Web App)

## Overview

This project is an AI-based handwritten digit classifier using a Convolutional Neural Network (CNN).
Users can draw digits (0–9) on a canvas, and the model predicts the digit in real time.

---

## Features

* Draw digits using mouse
* Real-time prediction
* CNN-based model (high accuracy)
* Clean and modern UI
* Backend API using Flask

---

## Tech Stack

* Python
* TensorFlow (CNN)
* OpenCV
* Flask
* HTML, CSS, JavaScript

---

## Project Structure

image-classifier-mnist/
│
├── main.py          # Train CNN model
├── app.py           # Backend API
├── index.html       # Frontend UI
├── requirements.txt
└── model/
└── mnist_model.h5

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run the Project

### 1. Train Model (first time only)

```bash
python main.py
```

### 2. Start Backend

```bash
python app.py
```

### 3. Open Frontend

Open `index.html` in browser

---

## Output

* Predicts digit drawn on canvas
* Shows model accuracy (~98–99%)

---

## Approach

* Used MNIST dataset
* Built CNN model for better image understanding
* Preprocessed input images from canvas
* Integrated frontend + backend

---

## Future Improvements

* Add confidence score
* Deploy online
* Improve preprocessing further

---

## Author

Bhakti Chavanke
