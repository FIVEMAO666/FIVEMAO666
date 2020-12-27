import cv2,os
from tkinter.filedialog import askopenfilename
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import img_function as predict
import img_math as img_math
import img_recognition as img_rec

path = "   "



def photo(self):

    self.predictor = predict.CardPredictor()
    self.predictor.train_svm()
    img_bar = cv2.imread(path)
    first_img,oldimg = self.predictor.img_first_pre(img_bar)


