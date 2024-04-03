
import streamlit as st
import os
import replicate
import random as rand

# Set up Replicate client
os.environ["REPLICATE_API_TOKEN"] = "r8_YdwVbF2Vcg8c08exKIk1Y7vEwfgFs1X1Yrhk9"
api = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])

def random_seed():  
    return rand.randint(0, 2**63 - 1)

def generate_image(prompt):
    input_data = {
        "prompt": prompt,
        "image_seed": random_seed(),  # Your image seed
        "guidance_scale": 11,
        "performance_selection": "Speed",
        "aspect_ratios_selection": "1024*1024",
    }
    output = None
    try:
        output = api.run(
            "konieshadow/fooocus-api-realistic:612fd74b69e6c030e88f6548848593a1aaabe16a09cb79e6d714718c15f37f47",
            input=input_data
        )
    except Exception as e:
        st.error(f"Error generating image: {e}")
    return output

# Set Streamlit configurations
st.set_page_config(page_title="Vincent App", page_icon="🖼️", layout="wide")
st.title("Vincent AI")

st.sidebar.image("https://i.imgur.com/9TX68Ou.gif")
st.sidebar.markdown("Created with ❤️ by Rajasree Baruri")

# Input fields for the prompt and number of images
prompt = st.text_input("Enter the prompt for image generation:")
num_of_images = st.number_input("Number of images to generate:", min_value=1, max_value=4, value=1)

# Generate images based on the provided prompt
if st.button("Generate Images"):
    with st.spinner('Generating images...'):
        images = []
        for i in range(num_of_images):
            # Generate image
            generated_image = generate_image(prompt)
            if generated_image:
                # Append the generated image to the list
                images.append(generated_image)
            else:
                st.error("Error generating image. Please try again.")
                break
            
        # Display the generated images
        if images:
            rows = st.columns(2)
            for i, image in enumerate(images):
                rows[i % 2].image(image, caption=f"Generated Image {i+1}", use_column_width=True, width=800)
        else:
            st.warning("No images generated.")