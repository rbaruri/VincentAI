import streamlit as st



def main():
    st.set_page_config(page_title="Getting Started", page_icon="🚀", layout="wide")
    st.sidebar.image("https://i.imgur.com/9TX68Ou.gif")
    st.sidebar.markdown("Created with ❤️ by Rajasree Baruri")
    st.title("Getting Started 🚀")

    st.write("""
    Vincent AI is your companion for seamlessly transforming text into captivating images. Whether you're an artist, designer, or simply looking to express your creativity, our user-friendly platform makes text-to-image generation effortless. Let's explore how to get started with Vincent AI:
    """)

    with st.expander("How to Generate Images"):
        st.write("Creating images with Vincent AI can be done in 2 steps:")
        st.write("1. **Input Your Text:** Begin by typing or pasting the text you want to transform into an image.")
        st.video("https://i.imgur.com/vDSRByo.mp4")
        st.write("""2. **Generate Your Image:** Click the "Generate" button, and Vincent AI will work its magic to produce a stunning image.""")


    with st.expander("How to Write Great Text-to-Image Prompts"):
        st.write("""
        Crafting compelling prompts is essential for maximizing the potential of Vincent AI. Here are some tips to help you write exceptional text-to-image prompts:
        - **Be Descriptive:** Provide clear and vivid descriptions within your text to guide the image generation process effectively.
        - **Set the Mood:** Establish the mood and atmosphere you want your image to convey through descriptive language and tone.
        - **Use Specific Language:** Avoid ambiguity by using specific nouns, adjectives, and verbs in your prompts.
        - **Consider Context:** Tailor your prompts to suit the context in which the images will be used or displayed.
        - **Experiment and Refine:** Don't hesitate to experiment with different prompts and styles to discover what works best for you.
        """)
    
    with st.expander("Where to Find Generated Images"):
        st.write("""Once you've generated images with Vincent AI, you can find them in the "History" section of the app. Simply navigate to that section, and you'll see all the images you've created listed there. From there, you can download your generated images as needed.""")
        st.video("https://i.imgur.com/vy40SAA.mp4")
        
        
    st.write("""
    By following these guidelines, you can craft engaging and inspiring prompts that unleash the full capabilities of Vincent AI's text-to-image generation.
    """)

    st.subheader("Did you find this useful?")
# Customizing the slider appearance using HTML
    st.write("Rate this guide:")
    rating_labels = {
        1: "Poor",
        2: "Fair",
        3: "Average",
        4: "Good",
        5: "Excellent"
    }

    value = st.slider("", 1, 5, 3, key="rating_slider", help="Select a rating from 1 to 5")
    st.write(f"You rated: {rating_labels[value]}")

if __name__ == "__main__":
    main()

