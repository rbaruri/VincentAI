import streamlit as st
import replicate
import os



os.environ["REPLICATE_API_TOKEN"] = "r8_YdwVbF2Vcg8c08exKIk1Y7vEwfgFs1X1Yrhk9"
api = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])

# Fetch predictions from Page 1
predictions = replicate.predictions.list()

# Filter out successful predictions with non-empty output and extract output links
successful_predictions = [(idx, prediction.output[0]) for idx, prediction in enumerate(predictions) if prediction.status == 'succeeded' and prediction.output is not None]

# Display successful prediction output images in Streamlit
st.set_page_config(page_title="Generated Images", page_icon="📜", layout="wide")
st.sidebar.image("https://i.imgur.com/9TX68Ou.gif")
st.sidebar.markdown("Created with ❤️ by Rajasree Baruri")
st.header("Generated Images")
num_images = len(successful_predictions)
num_columns = 3
num_rows = (num_images + num_columns - 1) // num_columns  # Calculate the number of rows needed

for i in range(num_rows):
    row = st.columns(num_columns)
    for j in range(num_columns):
        idx = i * num_columns + j
        if idx < num_images:
            with row[j]:
                st.image(successful_predictions[idx][1], caption=f"Generated Image {successful_predictions[idx][0]+1}", use_column_width=False, width=200)
                
                