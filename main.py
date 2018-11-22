''' Dog Breed Classifier '''
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from skimage.io import imread

def train_model(train_dir, train_labels):
    lst = os.listdir(train_dir)
    lst.sort(); # ensure alpha-numeric for quick lookup
    i=0
    for filename in lst:
        breed = train_labels.iloc[i][1]
        im = imread(train_dir+"/"+filename) #  Width x Height x 3 (colors) array
        # Train model using image 'im' and label 'breed'
        i=i+1

train_labels = pd.read_csv("labels.csv")
train_model("train/", train_labels)
