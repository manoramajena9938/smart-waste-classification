# ♻️ Smart Waste Classification using Deep Learning

> AI-powered waste classification system built using **ResNet50**, **PyTorch**, and **Streamlit** to automatically classify waste into six categories and promote efficient waste segregation.

---

## 📌 Project Overview

Waste segregation is an essential step in effective recycling and environmental sustainability. Incorrect disposal of recyclable materials increases pollution and reduces recycling efficiency.

This project uses **Deep Learning** to classify waste images into predefined categories. A user can upload an image through a modern **Streamlit web application**, and the model predicts the waste category along with its confidence score.

---
## 🌐 Live Demo

🚀 **Try the deployed application:** [Smart Waste Classification App]((https://smart-waste-classification-jgp9xepnb6speei6ydvspg.streamlit.app/))

📂 **GitHub Repository:** [View Source Code]((https://github.com/manoramajena9938/smart-waste-classification/edit/main/README.md))


## 🚀 Features

- ✅ Image Upload Interface
- ✅ Real-time Waste Classification
- ✅ Confidence Score
- ✅ Modern Streamlit Dashboard
- ✅ Transfer Learning using ResNet50
- ✅ Fine-Tuning for Improved Performance
- ✅ Responsive and User-Friendly UI
- ✅ Professional Project Structure

---

## ♻️ Supported Waste Categories

| Category | Icon |
|----------|------|
| Plastic Bottle | 🟢 |
| Carton | 📦 |
| Metal Packaging | 🥫 |
| Household Waste | 🗑 |
| Paper & Cardboard | 📄 |
| Glass | 🍾 |

---

# 🧠 Deep Learning Model

### Model Architecture

- **ResNet50**
- Pre-trained on **ImageNet**
- Framework: **PyTorch**

### Training Strategy

The model was trained in three stages:

### 1️⃣ Transfer Learning

- Loaded pretrained ResNet50
- Frozen feature extraction layers
- Trained only the final classification layer

### 2️⃣ Fine-Tuning

- Unfroze the last ResNet block
- Trained higher-level features
- Improved domain adaptation

### 3️⃣ Learning Rate Scheduling

Used a learning rate scheduler to reduce the learning rate during training for stable convergence.

---

# 📊 Model Performance

| Metric | Value |
|--------|-------|
| Test Accuracy | **74.52%** |
| Framework | PyTorch |
| Model | ResNet50 |
| Input Size | 224 × 224 |

---

# 🛠️ Tech Stack

### Programming Language

- Python

### Deep Learning

- PyTorch
- Torchvision

### Image Processing

- Pillow (PIL)

### Web Framework

- Streamlit

### Other Libraries

- NumPy
- Matplotlib
- tqdm

---

# 📂 Project Structure

```text
smart-waste-classification/
│
├── app.py                 # Streamlit application
├── style.css              # Custom UI styling
├── requirements.txt
├── README.md
│
├── assets/
│   └── logo.png
│
├── data/
│   ├── sample_images/
│   └── test_images/
│
├── models/
│   └── best_model.pth
│
├── notebooks/
│   └── waste-classification.ipynb
│
├── outputs/
│
└── src/
    ├── model_loader.py
    ├── preprocess.py
    └── predict.py
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/smart-waste-classification.git

cd smart-waste-classification
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate the environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

# 📷 Application Workflow

```
Upload Image
        │
        ▼
Image Preprocessing
        │
        ▼
ResNet50 Model
        │
        ▼
Prediction
        │
        ▼
Confidence Score
```

---



## Home Page

![Smart Waste Classification dashboard displaying a sidebar with app title and project summary, a central upload area with drag and drop file section and preview of a cardboard box, and a right panel showing prediction details](image.png)

```
images/home.png
```

---

## Prediction Result

> ![Prediction result screen showing uploaded cardboard box image, classification label Paper & Cardboard, and confidence score 94.78 percent in a bright interface](image.png)

```
images/prediction.png
```

---

# 🔮 Future Improvements

- Real-time Webcam Detection
- Mobile Deployment
- Cloud Deployment
- Larger Waste Dataset
- Object Detection using YOLO
- Multi-object Waste Detection

---

# 👩‍💻 Author

**Manorama Jena**

B.Tech Computer Science Engineering

AI | Machine Learning | Deep Learning Enthusiast

---

# ⭐ Acknowledgements

- PyTorch
- Streamlit
- ImageNet
- ResNet50
- Kaggle Waste Classification Dataset

---

## 🌱 If you found this project useful, consider giving it a ⭐ on GitHub.
