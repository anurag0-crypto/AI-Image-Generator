# AI Image Generator

A Streamlit-based AI Image Generator that converts text prompts into AI-generated images. Users can enter a prompt, choose an artistic style, apply prompt enhancements, use negative prompts, generate multiple images, save favorite prompts, browse image history, and download generated images.

---

## Features


* Streamlit frontend
* Text prompt input
* Style selection using radio buttons
* AI image generation using Hugging Face FLUX.1-schnell
* Generated image display
* Prompt history
* Environment variable based API key management
* Clean modular project structure
* Favorite prompts
* Prompt history
* Gallery view
* Download generated images
* Random prompt generator
* Regenerate last image
* Negative prompt support
* Auto prompt enhancement
* Multiple image generation
* Generation statistics
* Automatic local image saving

---

## Technologies Used

* Python
* Streamlit
* Pillow (PIL)
* Requests
* Hugging Face Inference API
* FLUX.1-schnell Image Generation Model

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/anurag0-crypto/AI-Image-Generator.git
cd <project_folder>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Add Your API Key

Create a `.env` file in the project root:

```env
HF_TOKEN=API_TOKEN
```

```gitignore
.env
```

---

## Running the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## How It Works

1. Enter an image prompt.
2. Select an image style.
3. Optionally add:

   * Negative prompts
   * Prompt enhancement
   * Multiple image generation
4. Click **Generate Image**.
5. View, download, and save generated images.

---

## Supported Styles

* Realistic
* Anime
* Cyberpunk
* Fantasy
* Watercolor
* Digital Art
* Pixel Art
* Cinematic

Each style automatically appends style-specific instructions to improve image quality and consistency.

---

## Example

### User Prompt

```text
A futuristic Indian city at night
```

### Selected Style

```text
Cyberpunk
```

### Final Prompt Sent to Model

```text
A futuristic Indian city at night, cyberpunk aesthetic, neon lights, futuristic cityscape
```

---

## Known Limitation

The FLUX.1-schnell inference endpoint does not provide full native negative prompt control through the simple API route used in this project. Negative prompts are appended as textual instructions and their effectiveness may vary depending on the generated image.

---

## Future Improvements

* User authentication
* Image upscaling
* Image editing and inpainting
* Prompt templates
* Cloud image storage
* Image sharing links
* Advanced generation controls

---

## Deployment

### Streamlit Community Cloud

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub repository.
4. Add the Hugging Face token under Secrets.
5. Deploy the application.

---

## Author

Anurag Kar

Built using Streamlit and Generative AI.
