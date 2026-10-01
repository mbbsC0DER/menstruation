# Defaults match the PDF: 10 epochs, 1000 images.
import torch
import torch.nn as nn
import torchvision.datasets as datasets
from torch.utils.data import DataLoader, Subset
import matplotlib.pyplot as plt
from torchvision import transforms
import os
import shutil


class VAE(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(784, 400), nn.ReLU(), nn.Linear(400, 40)
        )
        self.decoder = nn.Sequential(
            nn.Linear(20, 400), nn.ReLU(), nn.Linear(400, 784), nn.Sigmoid()
        )

    def forward(self, x):
        h = self.encoder(x.view(-1, 784))
        mu, logvar = h[:, :20], h[:, 20:]
        std = torch.exp(0.5 * logvar)
        z = mu + torch.randn_like(std) * std
        return self.decoder(z), mu, logvar


def train_and_generate(epochs=10, image_count=1000):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = VAE().to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    # Download and select digit 9 once, rather than loading MNIST each epoch.
    dataset = datasets.MNIST(
        "./data", train=True, download=True, transform=transforms.ToTensor()
    )
    indices = (dataset.targets == 9).nonzero(as_tuple=True)[0].tolist()
    loader = DataLoader(Subset(dataset, indices), batch_size=128, shuffle=True)
    for epoch in range(epochs):
        model.train()
        total_loss = 0.0
        for data, _ in loader:
            data = data.to(device)
            recon, mu, logvar = model(data)
            loss = nn.functional.binary_cross_entropy(
                recon, data.view(-1, 784), reduction="sum"
            ) - 0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
            if not torch.isfinite(loss):
                raise RuntimeError("Training produced a non-finite loss.")
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f"Epoch {epoch + 1}/{epochs}: loss={total_loss / len(indices):.2f}")

    os.makedirs("synthetic_images", exist_ok=True)
    model.eval()
    with torch.inference_mode():
        images = model.decoder(torch.randn(image_count, 20, device=device))
        images = images.cpu().numpy().reshape(-1, 28, 28)
    for i, img in enumerate(images):
        plt.imsave(f"synthetic_images/digit9_{i}.png", img, cmap="gray")
    shutil.make_archive("synthetic_images", "zip", "synthetic_images")
    return images


if __name__ == "__main__":
    train_and_generate()
    try:
        from google.colab import files
    except ImportError:
        print("Not in Colab. Images and synthetic_images.zip saved locally.")
    else:
        files.download("synthetic_images.zip")
