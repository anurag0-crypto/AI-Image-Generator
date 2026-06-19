import os

from io import BytesIO
from datetime import datetime

import streamlit as st

from PIL import Image

from api.image_api import generate_image
from prompts.styles import STYLE_PROMPTS
from utils.random_prompts import get_random_prompt
from ui.components import apply_css, header


# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨",
    layout="wide"
)

# ----------------------------------
# SESSION STATE
# ----------------------------------

if "history" not in st.session_state:
    st.session_state.history = []

if "gallery" not in st.session_state:
    st.session_state.gallery = []

if "prompt" not in st.session_state:
    st.session_state.prompt = ""

if "last_prompt" not in st.session_state:
    st.session_state.last_prompt = ""

if "favorites" not in st.session_state:
    st.session_state.favorites = []



# ----------------------------------
# CSS
# ----------------------------------

apply_css()


header()

# ----------------------------------
# SIDEBAR
# ----------------------------------

with st.sidebar:

    st.header("⚙ Settings")



    style = st.radio(
        "Choose Style",
        list(STYLE_PROMPTS.keys())
    )

    image_count = st.slider(
        "Number of Images",
        1,
        4,
        1
    )

    negative_prompt = st.text_input(
        "Negative Prompt"
    )

    enhance_prompt = st.toggle(
        "✨ Auto Enhance Prompt"
    )

    st.divider()

    st.metric(
        "Images Generated",
        len(st.session_state.gallery)
    )

    st.metric(
        "Prompts Used",
        len(st.session_state.history)
    )

    st.divider()

    if st.button("🎲 Random Prompt"):

        st.session_state.prompt = (
            get_random_prompt()
        )

        st.rerun()

    if st.button("🗑 Clear History"):

        st.session_state.history = []

    if st.button("🖼 Clear Gallery"):

        st.session_state.gallery = []

    if st.button("🔄 Regenerate Last"):

        if st.session_state.last_prompt:

            try:

                image_bytes = generate_image(
                    st.session_state.last_prompt
                )

                image = Image.open(
                    BytesIO(image_bytes)
                )

                st.session_state.gallery.append({
                    "image": image,
                    "prompt": st.session_state.last_prompt,
                    "style": "Regenerated",
                    "time": datetime.now().strftime(
                        "%d-%m-%Y %H:%M:%S"
                    )
                })

                st.success(
                    "Image regenerated."
                )

            except Exception as e:

                st.error(str(e))


# ----------------------------------
# MAIN INPUT
# ----------------------------------

prompt = st.text_area(
    "Describe your image",
    key="prompt",
    height=150,
    placeholder=
    "Example: A futuristic Indian city at night..."
)

col1, col2 = st.columns([1, 5])

with col1:

    if st.button("⭐ Save"):

        if prompt.strip():

            if prompt not in st.session_state.favorites:

                st.session_state.favorites.append(
                    prompt
                )

                st.success(
                    "Added to favorites!"
                )

            else:

                st.info(
                    "Already in favorites."
                )

with col2:

    st.caption(
        f"Characters: {len(prompt)}"
    )

# ----------------------------------
# PROMPT IDEAS
# ----------------------------------

with st.expander("💡 Prompt Ideas"):

    st.write(
        """
        • A cyberpunk Kolkata street

        • A futuristic Indian city

        • Dragon flying over Himalayas

        • Ancient temple on Mars

        • Floating city in the clouds
        """
    )

# ----------------------------------
# GENERATE
# ----------------------------------

generate = st.button(
    "🚀 Generate Image",
    use_container_width=True
)

if generate:

    if not prompt.strip():

        st.warning(
            "Please enter a prompt."
        )

    else:

        final_prompt = (
            f"{prompt}, "
            f"{STYLE_PROMPTS[style]}"
        )

        if enhance_prompt:

            final_prompt += (
                ", highly detailed,"
                " award winning,"
                " professional artwork,"
                " sharp focus"
            )

        if negative_prompt:

            final_prompt += (
                f". Avoid: {negative_prompt}"
            )

        st.session_state.last_prompt = (
            final_prompt
        )

        st.info(
            "Prompt sent to model"
        )

        st.code(final_prompt)

        progress = st.progress(0)

        os.makedirs(
            "generated_images",
            exist_ok=True
        )

        for i in range(image_count):

            try:

                progress.progress(
                    int(
                        ((i + 1)
                        / image_count)
                        * 100
                    )
                )

                image_bytes = (
                    generate_image(
                        final_prompt
                    )
                )

                image = Image.open(
                    BytesIO(image_bytes)
                )

                st.image(
                    image,
                    caption=
                    f"Generated Image {i+1}",
                    use_container_width=True
                )

                timestamp = (
                    datetime.now()
                    .strftime(
                        "%Y%m%d_%H%M%S"
                    )
                )

                file_path = (
                    f"generated_images/"
                    f"img_{timestamp}_{i}.png"
                )

                image.save(file_path)

                buffer = BytesIO()

                image.save(
                    buffer,
                    format="PNG"
                )

                st.download_button(
                    f"Download Image {i+1}",
                    buffer.getvalue(),
                    f"image_{i+1}.png",
                    "image/png"
                )

                if st.button(
                    f"⭐ Favorite Prompt {i}"
                ):
                    st.session_state.favorites.append(
                        prompt
                    )

                st.session_state.gallery.append({

                    "image": image,

                    "prompt": prompt,

                    "style": style,

                    "time":
                    datetime.now().strftime(
                        "%d-%m-%Y %H:%M:%S"
                    )
                })

            except Exception as e:

                st.error(str(e))

        st.session_state.history.append({

            "prompt": prompt,

            "style": style,

            "time":
            datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )
        })

        st.success(
            "Generation Complete!"
        )

# ----------------------------------
# FAVORITES
# ----------------------------------

st.divider()

st.subheader("⭐ Favorite Prompts")

if st.session_state.favorites:

    for idx, fav in enumerate(
        st.session_state.favorites
    ):

        col1, col2 = st.columns([8, 1])

        with col1:

            if st.button(
                fav,
                key=f"use_fav_{idx}"
            ):

                st.session_state.prompt = fav

                st.rerun()

        with col2:

            if st.button(
                "❌",
                key=f"remove_fav_{idx}"
            ):

                st.session_state.favorites.pop(
                    idx
                )

                st.rerun()

else:

    st.info(
        "No favorite prompts yet."
    )
# ----------------------------------
# HISTORY
# ----------------------------------

st.divider()

st.subheader(
    "📝 Prompt History"
)

if st.session_state.history:

    for item in reversed(
        st.session_state.history
    ):

        with st.expander(
            item["prompt"]
        ):

            st.write(
                f"Style: {item['style']}"
            )

            st.write(
                f"Time: {item['time']}"
            )

else:

    st.info(
        "No history yet."
    )

# ----------------------------------
# GALLERY
# ----------------------------------

st.divider()

st.subheader(
    "🖼 Gallery"
)

if st.session_state.gallery:

    cols = st.columns(3)

    for idx, item in enumerate(
        st.session_state.gallery
    ):

        with cols[idx % 3]:

            st.image(
                item["image"],
                use_container_width=True
            )

            st.caption(
                item["prompt"]
            )

            st.write(
                item["style"]
            )

            st.write(
                item["time"]
            )

else:

    st.info(
        "No images generated yet."
    )

# ----------------------------------
# FOOTER
# ----------------------------------

st.divider()

st.caption(
    "Built with Streamlit + Hugging Face FLUX.1-schnell"
)