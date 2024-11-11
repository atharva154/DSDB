# -*- coding: utf-8 -*-
"""PCA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fa3msz1UN5RioDFcvXHiCrBdYSRp4m7L
"""

# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/content/Assignment 8.csv')

# Select numerical features for PCA
X = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA to reduce to 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Explained variance to understand information captured
print("Explained variance ratio:", pca.explained_variance_ratio_)

# Create a DataFrame with principal components
df_pca = pd.DataFrame(data=X_pca, columns=['Principal Component 1', 'Principal Component 2'])
df_pca['Species'] = df['species']

# Visualize the PCA result
plt.figure(figsize=(8, 6))
scatter = plt.scatter(df_pca['Principal Component 1'], df_pca['Principal Component 2'],
                      c=pd.factorize(df_pca['Species'])[0], cmap='viridis', s=50)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Dataset')
plt.colorbar(scatter, ticks=range(len(df_pca['Species'].unique())), label='Species')
plt.show()