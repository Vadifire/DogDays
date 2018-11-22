''' Dog Breed Classifier '''
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import csv
from skimage.io import imread

''' Create and train model using training data'''
def train_model(train_dir, train_labels):
    lst = os.listdir(train_dir)
    lst.sort(); # ensure alpha-numeric for quick lookup
    i=0
    for filename in lst:
        breed = train_labels.iloc[i][1]
        im = imread(train_dir+"/"+filename) #  Width x Height x 3 (colors) array
        # Train model using image 'im' and label 'breed'
        i=i+1

''' Label images from testing dataset using trained model '''
def label_images(test_dir, breeds):
    lst = os.listdir(test_dir)
    print(breeds)
    test_labels = pd.DataFrame(columns = breeds)
    print(test_labels.head())
    print(test_labels.shape)

with open('breeds.csv', 'r') as f:
    breeds = list(csv.reader(f, delimiter='\n'))
train_labels = pd.read_csv("labels.csv")
#train_model("train/", train_labels)
label_images("test/", breeds)

