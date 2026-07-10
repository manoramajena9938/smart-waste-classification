import torch
import torch.nn as nn
from torchvision import models


def load_model(model_path, device):
    """
    Loads the trained ResNet50 model.
    """

    # Create ResNet50 architecture
    model = models.resnet50(weights=None)

    # Replace the final fully connected layer
    model.fc = nn.Linear(model.fc.in_features, 6)

    # Load trained weights
    model.load_state_dict(
        torch.load(model_path, map_location=device)
    )

    # Move model to CPU/GPU
    model = model.to(device)

    # Set model to evaluation mode
    model.eval()

    return model