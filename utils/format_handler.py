import os
import numpy
import cv2 as cv


def path_to_image(input_path: str) -> numpy.ndarray | None:
    """take an path to a file and create numpy array"""
    return cv.imread(input_path)
