import streamlit as st
import torch
import torchvision.transforms as T
from PIL import Image
import numpy as np
import os
import gdown

# Define labels for conditions
labels = {0: "Bacterial Dermatitis", 1: "Fungal Infection", 2: "Healthy", 3: "Hypersensitivity"}

@st.cache_resource
def load_model(model_drive_url):
    # Temporary file path to store the .pth file
    pth_file_path = "model_state_dict.pth"
    
    # Download the .pth file from Google Drive
    st.info("Downloading the model from Google Drive...")
    gdown.download(model_drive_url, pth_file_path, quiet=False)
    
    # Define the model architecture (as before)
    import timm
    NUM_CLASSES = 4
    NUM_FEATURES = 768

    model = timm.create_model('vit_base_patch14_reg4_dinov2.lvd142m', pretrained=False)
    model.head = torch.nn.Sequential(
        torch.nn.Linear(NUM_FEATURES, 256),
        torch.nn.ReLU(),
        torch.nn.Dropout(0.3),
        torch.nn.Linear(256, NUM_CLASSES),
    )

    # Load the model weights from the downloaded .pth file
    model.load_state_dict(torch.load(pth_file_path, map_location=torch.device('cpu')))
    model.eval()

    # Remove the downloaded .pth file after loading
    os.remove(pth_file_path)

    return model

# Link to your model on Google Drive
model_drive_url = 'https://drive.google.com/uc?export=download&id=10XZm5EYvSuGCh2-ryBTKV-XseEghGH_a'  # Replace with your Google Drive file ID

model = load_model(model_drive_url)

# Define the image transformation pipeline
transform_image = T.Compose([
    T.Resize((518, 518)),  # Resize image to match model input
    T.ToTensor(),
    T.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])  # Normalize using mean and std dev
])

st.title("Dog Skin Condition Classifier")
st.write("Upload an image of a dog's skin to detect the condition, or use your webcam.")

# Choose between uploading a file or using the webcam
upload_option = st.radio("Select an option to provide an image:", ("Upload a file", "Use webcam"))

image = None  # Initialize image variable

if upload_option == "Upload a file":
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)

elif upload_option == "Use webcam":
    webcam_image = st.camera_input("Capture a photo")
    
    if webcam_image is not None:
        image = Image.open(webcam_image)

# If an image is provided, process it
if image is not None:
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Preprocess the image to fit model input requirements
    img_tensor = transform_image(image).unsqueeze(0)  # Add batch dimension

    # Make a prediction
    with torch.no_grad():
        output = model(img_tensor)
        predicted_class = torch.argmax(output, dim=1).item()
        predicted_label = labels[predicted_class]
        prediction_confidence = torch.nn.functional.softmax(output, dim=1).squeeze()

    # Display the prediction
    st.write(f"Predicted Condition: **{predicted_label}**")
    st.write("Prediction Confidence:")
    for i, label in labels.items():
        st.write(f"{label}: {prediction_confidence[i]:.2f}")

else:
    st.warning("Please upload or capture an image to proceed.")
