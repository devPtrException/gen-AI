import os
from huggingface_hub import snapshot_download

# Define the model ID you want to download
model_id = "kakao-enterprise/vits-ljs"
current_dir = os.path.dirname(
    os.path.abspath(__file__)
)  # Directory of the current script
local_models_dir = os.path.join(
    current_dir, "multi", "models"
)  # Directory for all models
destination_path = os.path.join(
    local_models_dir, "vits-ljs"
)  # Folder to store this particular model

# Print the target download path
print(f"Attempting to download '{model_id}' to: {destination_path}")

# Ensure the directory exists
os.makedirs(destination_path, exist_ok=True)

try:
    # Download the model using snapshot_download
    downloaded_path = snapshot_download(
        repo_id=model_id,
        local_dir=destination_path,
        local_dir_use_symlinks=False,  # Avoid symlinks for WSL file systems
    )
    print(f"Model downloaded successfully to: {downloaded_path}")

except Exception as e:
    print(f"An error occurred during download: {e}")







# history:
# model_id = "Salesforce/blip-image-captioning-large"
# model_id = "sshleifer/distilbart-cnn-12-6"
