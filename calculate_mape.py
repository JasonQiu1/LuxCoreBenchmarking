#!/bin/env python3

# BASED ON CODE FOUND AT:
# https://stackoverflow.com/questions/189943/how-can-i-quantify-difference-between-two-images

# ARG1 IS THE RENDERED IMAGE, AND ARG2 IS THE REFERENCE IMAGE

import sys
from numpy import sum, mean
from cv2 import imread

def main():
    print("Calculating MAPE...")
    rendered_filename, reference_filename = sys.argv[1:1+2]
    # read images as 2D arrays (convert to grayscale for simplicity)
    rendered = to_grayscale(imread(rendered_filename).astype(float))
    reference = to_grayscale(imread(reference_filename).astype(float))
    # compare
    mape = compare_images(rendered, reference)
    print("MAPE: ", mape)

def compare_images(rendered, reference):
    # calculate the mean absolute percent error
    absolute_diff = abs(rendered - reference)  # elementwise for scipy arrays
    denominator = reference + (mean(reference) * 0.01)
    mape = mean(absolute_diff / denominator)
    return mape

def to_grayscale(arr):
    "If arr is a color image (3D array), convert it to grayscale (2D array)."
    if len(arr.shape) == 3:
        return mean(arr, -1)  # average over the last axis (color channels)
    else:
        return arr

main()

