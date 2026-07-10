from torchvision import transforms
from PIL import Image

# Image preprocessing pipeline
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


def preprocess_image(image):
    """
    Preprocesses a PIL image for ResNet50 prediction.
    """

    # Convert image to RGB
    image = image.convert("RGB")

    # Apply transformations
    image = transform(image)

    # Add batch dimension
    image = image.unsqueeze(0)

    return image