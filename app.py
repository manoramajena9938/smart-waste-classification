import streamlit as st
from PIL import Image
import tempfile
import os

from src.predict import predict_image

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="Smart Waste Classification",
    page_icon="♻️",
    layout="wide"
)

# ----------------------------------------------------
# Load CSS
# ----------------------------------------------------
with open("style.css") as css:
    st.markdown(
        f"<style>{css.read()}</style>",
        unsafe_allow_html=True
    )

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------
with st.sidebar:

    # Logo
    st.image("assets/logo.png", width=150)

    st.markdown("## ♻️ Smart Waste")

    st.caption("AI-Powered Waste Recognition")

    st.markdown("---")

    st.subheader("📌 Project")

    st.write("""
This application classifies waste images using
a Deep Learning model based on **ResNet50**.

Simply upload an image and the model predicts
its waste category.
""")

    st.markdown("---")

    st.subheader("🤖 Model")

    st.write("• ResNet50")
    st.write("• Transfer Learning")
    st.write("• Fine-Tuning")

    st.markdown("---")

    st.subheader("📈 Performance")

    st.metric(
        "Test Accuracy",
        "74.52%"
    )

    st.markdown("---")

    st.subheader("✨ Features")

    st.write("✅ Image Upload")
    st.write("✅ AI Prediction")
    st.write("✅ Confidence Score")
    st.write("✅ Modern UI")
    st.write("✅ Streamlit Deployment")

    st.markdown("---")

    st.subheader("♻️ Categories")

    st.write("🟢 Plastic Bottle")
    st.write("📦 Carton")
    st.write("🥫 Metal Packaging")
    st.write("🗑 Household Waste")
    st.write("📄 Paper & Cardboard")
    st.write("🍾 Glass")

    st.markdown("---")

    st.subheader("👩‍💻 Developer")

    st.write("**Manorama Jena**")

# ----------------------------------------------------
# Header
# ----------------------------------------------------

col_logo, col_title = st.columns([1, 6])

with col_logo:
    st.image("assets/logo.png", width=90)

with col_title:

    st.markdown("""
<div class="main-title">

♻️ Smart Waste Classification

</div>

<div class="sub-title">

AI-Powered Waste Recognition using Deep Learning

</div>
""", unsafe_allow_html=True)

st.write("")

# ----------------------------------------------------
# Upload Section
# ----------------------------------------------------

st.subheader("📷 Upload Waste Image")

uploaded_file = st.file_uploader(
    "",
    type=["jpg", "jpeg", "png"]
)

# ----------------------------------------------------
# Prediction
# ----------------------------------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    left, right = st.columns([1.2, 1])

    with left:

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

    # Temporary File

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    ) as temp:

        image.save(temp.name)

        image_path = temp.name

    # Predict

    result = predict_image(image_path)

    os.remove(image_path)

    prediction = result["prediction"]
    confidence = result["confidence"]

    icons = {

        "Plastic Bottle": "🟢",

        "Carton": "📦",

        "Metal Packaging": "🥫",

        "Household Waste": "🗑",

        "Paper & Cardboard": "📄",

        "Glass": "🍾"

    }

    with right:

        st.markdown(
            f"""
<div class="prediction-card">

<h2>♻️ Prediction</h2>

<h1>{icons.get(prediction, "♻️")} {prediction}</h1>

</div>
""",
            unsafe_allow_html=True
        )

        st.write("")

        st.write("### Confidence")

        st.progress(confidence / 100)

        st.success(f"{confidence:.2f}%")

        if confidence < 65:

            st.warning(
                """
Low confidence prediction.

Please upload a clearer image
containing one supported waste object.
"""
            )


# ====================================================
# About Model
# ====================================================

st.markdown("<br>", unsafe_allow_html=True)

with st.expander("ℹ️ About the Model", expanded=False):

    st.markdown("""
<div class="about-card">

### 🤖 Model Information

**Architecture**
- ResNet50 (Pre-trained on ImageNet)

**Deep Learning Technique**
- Transfer Learning
- Fine-Tuning

**Framework**
- PyTorch

**Input Image Size**
- 224 × 224 pixels

**Supported Classes**
- 🟢 Plastic Bottle
- 📦 Carton
- 🥫 Metal Packaging
- 🗑 Household Waste
- 📄 Paper & Cardboard
- 🍾 Glass

**Test Accuracy**
- **74.52%**

**Purpose**
- Automatically classify waste images to promote smart recycling and waste segregation.

</div>
""", unsafe_allow_html=True)

# ====================================================
# Tips Section
# ====================================================

st.markdown("---")

st.subheader("💡 Tips for Best Predictions")

tip1, tip2, tip3 = st.columns(3)

with tip1:
    st.info("""
📸 **Use a Clear Image**

Avoid blurry or low-quality photos.
""")

with tip2:
    st.info("""
🎯 **One Object**

Keep only one waste object in the image.
""")

with tip3:
    st.info("""
💡 **Good Lighting**

Capture images in good lighting for better predictions.
""")

# ====================================================
# Sample Categories
# ====================================================

st.markdown("---")

st.subheader("♻️ Supported Waste Categories")

c1, c2, c3 = st.columns(3)

with c1:

    st.success("🟢 Plastic Bottle")

    st.success("📦 Carton")

with c2:

    st.success("🥫 Metal Packaging")

    st.success("📄 Paper & Cardboard")

with c3:

    st.success("🍾 Glass")

    st.success("🗑 Household Waste")

# ====================================================
# Future Improvements
# ====================================================

st.markdown("---")

with st.expander("🚀 Future Enhancements"):

    st.markdown("""
- 🌍 Real-time webcam prediction

- 📱 Mobile deployment

- ♻️ More waste categories

- 📊 Analytics dashboard

- ☁️ Cloud deployment

- 🤖 Object Detection using YOLO
""")

# ====================================================
# Footer
# ====================================================

st.markdown("---")

st.markdown(
"""
<div class="footer">

<h4>♻️ Smart Waste Classification</h4>

Developed by <b>Manorama Jena</b>

<br><br>

Built with ❤️ using <b>PyTorch</b>, <b>Streamlit</b> and <b>ResNet50</b>

<br><br>

© 2026 All Rights Reserved.

</div>
""",
unsafe_allow_html=True
)