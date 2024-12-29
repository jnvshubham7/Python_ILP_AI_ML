import os
import kagglehub

# Specify your custom directory name (folder path)
custom_path = r"C:\Users\Shubham\Documents\Python_ILP\My_Dataset_Folder"

# Ensure the folder exists (create it if it doesn't)
os.makedirs(custom_path, exist_ok=True)

# Download the dataset to your custom folder
dataset_name = "balaka18/email-spam-classification-dataset-csv"  # Replace with the correct dataset name
path = kagglehub.dataset_download(dataset_name, path=custom_path)

print("Path to dataset files:", path)
