import torch
import torch.nn.functional as F
from PIL import Image

from src.model_loader import load_model
from src.preprocess import preprocess_image

# ---------------------------------------------------
# Device Configuration
# ---------------------------------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ---------------------------------------------------
# Class Names (English)
# IMPORTANT:
# Keep the same order as the classes used during training.
# ---------------------------------------------------
class_names = [
    "Plastic Bottle",
    "Carton",
    "Metal Packaging",
    "Household Waste",
    "Paper & Cardboard",
    "Glass"
]

# ---------------------------------------------------
# Load Model (Loads only once)
# ---------------------------------------------------
model = load_model("models/best_model.pth", device)


def predict_image(image_path):
    """
    Predict the waste category of an image.

    Args:
        image_path (str): Path to the input image.

    Returns:
        dict:
            prediction          -> Predicted class
            confidence          -> Confidence (%)
            probabilities       -> Probability for all classes
    """

    # Open Image
    image = Image.open(image_path)

    # Preprocess Image
    image_tensor = preprocess_image(image)
    image_tensor = image_tensor.to(device)

    # Prediction
    with torch.no_grad():

        outputs = model(image_tensor)

        probabilities = F.softmax(outputs, dim=1)

        confidence, predicted = torch.max(probabilities, dim=1)

    # Predicted Class
    predicted_class = class_names[predicted.item()]

    # Confidence
    confidence_score = confidence.item() * 100

    # Store probabilities for all classes
    probability_dict = {}

    for i, class_name in enumerate(class_names):
        probability_dict[class_name] = round(
            probabilities[0][i].item() * 100,
            2
        )

    # Return everything as a dictionary
    return {
        "prediction": predicted_class,
        "confidence": round(confidence_score, 2),
        "probabilities": probability_dict
    }