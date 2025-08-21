# import os
# from huggingface_hub import snapshot_download
#
# # model_id = "Salesforce/blip-image-captioning-large"
# # model_id = "sshleifer/distilbart-cnn-12-6"
#
#
# # Define the model ID
# model_id = "kakao-enterprise/vits-ljs"
# current_dir = os.path.dirname(
#     os.path.abspath(__file__)
# )  # Directory of the current script
# local_models_dir = os.path.join(current_dir, "models")
# destination_path = os.path.join(
#     local_models_dir, "vits-ljs"
# )  # folder for this particular model
#
# print(f"Attempting to download '{model_id}' to: {destination_path}")
#
# try:
#     # specify ignore_patterns to exclude git history files if present
#     downloaded_path = snapshot_download(
#         repo_id=model_id,
#         local_dir=destination_path,
#         local_dir_use_symlinks=False,  # Important for Windows to copy files directly
#         # ignore_patterns=["*.git*", "README.md", "LICENSE.md"] # Optional: Exclude specific files if you only want model weights/config
#     )
#     print(f"Model downloaded successfully to: {downloaded_path}")
#
# except Exception as e:
#     print(f"An error occurred during download: {e}")
