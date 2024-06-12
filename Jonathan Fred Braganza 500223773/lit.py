import streamlit as st
import cv2
import numpy as np
#from tensorflow.keras.models import load_model

# Load the best model
#best_model = load_model('test.h5')

# Define a function to preprocess image for model prediction
def preprocess_image(image):
    # Resize image by 10%
    resized_image = cv2.resize(image, (int(image.shape[1]*0.9), int(image.shape[0]*0.9)))
    
    # Perform any other necessary preprocessing (e.g., normalization)
    # Here's a simple example assuming the model expects a 256x256 grayscale image
    resized_image = cv2.resize(resized_image, (256, 256))
    normalized_image = resized_image / 255.0  # Normalize pixel values
    return normalized_image.reshape(1, 256, 256, 1)  # Reshape for model input
# Create a Streamlit app
def main():
    st.title("COVID-19 Detection App")
    st.write("Upload an X-ray image for prediction.")

    # File upload
    uploaded_file = st.file_uploader("Choose an X-ray image...", type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        # Display the uploaded image
        image = np.array(Image.open(uploaded_file))
        st.image(image, caption='Uploaded X-ray Image', use_column_width=True)

        # Make predictions
        if st.button('Predict'):
            preprocessed_image = preprocess_image(image)
            #prediction = best_model.predict(preprocessed_image)
            #predicted_class = np.argmax(prediction)
            
            # Display prediction
            #classes = ['COVID-19', 'Non-COVID', 'Normal']
            #st.write(f"Prediction: {classes[predicted_class]}")
            st.write("works")
# Run the Streamlit app
if __name__ == '__main__':
    main()
