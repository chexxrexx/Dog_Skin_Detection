import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load your trained model
model = tf.keras.models.load_model('piecederesistance.h5')  # Change to the actual path

# Define labels for conditions
labels = {0: "Bacterial Dermatitis", 1: "Fungal Infection", 2: "Healthy", 3: "Hypersensitivity"}

st.title("Dog Skin Condition Classifier")
st.write("Upload an image of a dog's skin to detect the condition.")

# File uploader for the image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# If an image is uploaded
if uploaded_file is not None:
    # Open the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Preprocess the image to fit model input requirements
    img_array = np.array(image.resize((128, 128)))  # Resize to your model’s input size
    img_array = img_array / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Make a prediction
    predictions = model.predict(img_array)
    predicted_label = labels[np.argmax(predictions)]
    
    # Display the prediction
    st.write(f"Predicted Condition: **{predicted_label}**")

    # Optional: Display prediction confidence
    st.write("Prediction confidence:", predictions)
