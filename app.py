import streamlit as st
from st_pages import Page, show_pages



# Header with background image
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

show_pages([
    Page("app.py", "Home", "🏠"),
    Page("pages/page1.py", "Getting Started", "🚀"),
    Page("pages/page2.py", "App", "📱"),
    Page("pages/page3.py", "History", "📜")
])
st.sidebar.image("https://i.imgur.com/9TX68Ou.gif")
st.sidebar.markdown("Created with ❤️ by Rajasree Baruri")

st.title("Transform Your Imagination into Reality 🪄")
st.subheader("What is Vincent AI?")

st.markdown("Vincent AI is your gateway to a realm where words paint pictures and creativity knows no bounds. "
                "Our cutting-edge text-to-image generation app empowers you to bring your wildest visions to life "
                "with unparalleled realism and detail.")

col1, col2 = st.columns(2)
col1.image("https://i.imgur.com/LaFUnRz.png", use_column_width=True, width=400)
col2.image("https://i.imgur.com/jSGfzyh.png", use_column_width=True, width=400)

# Text description
st.write("""
This app allows you to transform your textual descriptions into stunning visuals. Ever dreamed of seeing a "cat riding a bicycle on Mars"? Or perhaps a "portrait of a cyberpunk samurai in a neon-lit cityscape"? With our innovative AI model, you can bring these ideas to life with just a few words.
""")

st.write("---")

st.subheader("Why Choose Vincent AI? 💡")
st.write("- **Hyperrealistic Images:** Our AI model produces images that defy expectations with lifelike detail "
             "and realism.")
st.write("- **User-Friendly Interface:** With a seamless user experience, creating stunning visuals has never "
             "been easier.")
st.write("- **Endless Possibilities:** From whimsical fantasies to gritty cyberpunk landscapes, Vincent AI "
             "brings any vision to life.")
st.write("- **Versatile Applications:** Use your generated images for storytelling, artwork, gaming, and "
             "beyond—the only limit is your imagination.")

st.write("---")
st.header("How it Works 🛠️")


st.write("Turn your vision into reality in three simple steps")

steps = ["1. Describe your vision:",
         "2. Let the AI work its magic:",
         "3. Download and enjoy:"
]

descriptions = [
    "Enter a detailed text description of the image you want to generate. Be as specific as possible about the objects, characters, setting, and style.",
    "Click a button and our powerful AI model will take your text prompt and translate it into a unique image.",
    "Save your generated image and use it for your creative projects, social media, or simply admire your own imagination!"
]

for step, description in zip(steps, descriptions):
    st.write(f"**{step}** {description}")


st.write("---")

# Explore the Possibilities section with accordion
st.subheader("Explore the Possibilities 🌌")
st.write("A universe of creative potential awaits")

with st.expander("Who can benefit from this tool?"):
    st.write("""
    This text-to-image generation tool has a vast range of applications. Whether you're a:
    * Writer in search of inspiring concept art for your next story ✍️
    * Artist looking for new ideas and visual references 👩‍🎨🎨
    * Gamer yearning to design your dream character or environment 🎮
    * Anyone with a spark of creativity,
    This project is here to fuel your imagination and turn your textual visions into visual masterpieces 🤩
    """)




st.header("Start Creating Today")
st.write("Don't just imagine—create. Dive into the world of Vincent AI and turn your textual visions into "
             "visual masterpieces. Whether you're a seasoned creator or a curious beginner, there's something "
             "extraordinary waiting for you. ✨")
