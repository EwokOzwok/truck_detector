import os
import cv2
import numpy as np
from sklearn.cluster import KMeans
from skimage.feature import hog
import matplotlib.pyplot as plt
os.getcwd()
# Function to extract HOG features from an image
def extract_hog_features(image):
    resized_image = cv2.resize(image, (360, 180))  # Resize image to 360x360 pixels
    hog_features, _ = hog(resized_image, orientations=8, pixels_per_cell=(16, 16),
                          cells_per_block=(1, 1), visualize=True, multichannel=True)
    return hog_features

# Define the directory containing the images
directory = r'croppeddata/'

# List all image files in the directory
image_files = [file for file in os.listdir(directory) if file.endswith('.jpg')]


# Load and preprocess images, extract features
images = []
features = []
for file_name in image_files:
    image_path = os.path.join(directory, file_name)
    image = cv2.imread(image_path)
    if image is not None:
        images.append(image)
        features.append(extract_hog_features(image))

# Convert features to NumPy array
features_array = np.array(features)
features_array
# Apply K-means clustering
num_clusters = 2  # Adjust the number of clusters as needed
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(features_array)

# Get cluster labels
cluster_labels = kmeans.labels_




from sklearn.cluster import DBSCAN

# min_samples is n_clu
db = DBSCAN(eps=1.5, min_samples=2)


db = db.fit(features_array)

# cannot call predict with DBSCAN, you have to output labels
cluster_labels = db.labels_




# Analyze clusters
for cluster_id in range(num_clusters):
    cluster_indices = np.where(cluster_labels == cluster_id)[0]
    print(f"Cluster {cluster_id}: {len(cluster_indices)} images")

# Visualize first few images in the cluster
num_images_to_visualize = min(15, len(cluster_indices))
fig, axes = plt.subplots(1, num_images_to_visualize, figsize=(15, 3))
for i, index in enumerate(cluster_indices[:num_images_to_visualize]):
    axes[i].imshow(cv2.cvtColor(images[index], cv2.COLOR_BGR2RGB))
    axes[i].axis('off')
    axes[i].set_title(f"Image {index}")
plt.show()

import pandas as pd


paths = []
for i in range(0,len(image_files)):
  paths.append(os.path.join(directory,image_files[i]))

cluster_images = pd.DataFrame(zip(paths,cluster_labels))
cluster_images = np.array(cluster_images)


import shutil
os.getcwd()
output_path = "./clusters"

cluster_images

# Create folders for each cluster
for cluster_num in range(num_clusters):
    cluster_folder = os.path.join(output_path, f"cluster_{cluster_num}")
    os.makedirs(cluster_folder, exist_ok=True)

# Move images to respective folders based on cluster number
for image_path, cluster_num in cluster_images:
    cluster_folder = os.path.join(output_path, f"cluster_{cluster_num}")
    shutil.copy(image_path, cluster_folder)

