import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Set the page title
st.title("Lao License Plate Recognition")

# Create a layout with two columns
columns = st.columns([2, 1])

# Image input
uploaded_file = st.file_uploader("ເລືອກຮູບພາບ", type=["jpg", "jpeg", "png"])

# Check if an image is uploaded
if uploaded_file is not None:
    # Display the uploaded image in the left column
    image = Image.open(uploaded_file)
    columns[0].image(image, caption='ຮູບທີ່ Upload', use_column_width=True)
    

    # Run button
    if columns[1].button("Run"):
        # Convert image to byte array
        img_bytes = BytesIO()
        image.save(img_bytes, format='JPEG')
        img_bytes = img_bytes.getvalue()

        # Prepare request data
        files = {'file': img_bytes}

        # Send POST request to the API
        api_url = "http://192.168.100.4:5000/api/predict"
        response = requests.post(api_url, files=files)

        # Check if the request is successful
        if response.status_code == 200:
            plate_info = response.json()
            # Extract char and province values
            char_number_value = plate_info["char_number"]
            province_value = plate_info["province"]

            # Display the license plate info below the image
            columns[1].empty()
            columns[1].markdown("**ຊື່ແຂວງ:** {}".format(province_value))
            columns[1].markdown("**ເລກທະບຽນ:** {}".format(char_number_value))
        else:
            st.write("Failed to get license plate information from the API")
