import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load
model = tf.keras.models.load_model('alt_model.keras')  

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
    img_array = np.array(image.resize((128, 128)))  
    img_array = img_array / 255.0  # Normalise
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Make a prediction
    predictions = model.predict(img_array)
    predicted_label = labels[np.argmax(predictions)]
    
    # Display the prediction
    st.write(f"Predicted Condition: **{predicted_label}**")

    # Display prediction confidence
    st.write("Prediction confidence:", predictions)
