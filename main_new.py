# -*- coding:utf-8 -*-
# @Datetime: 2020/12/22 20:31
# @Author: 铭仔
# @File: main.py
# @Software: PyCharm


import cv2
from tkinter import ttk
from PIL import Image, ImageTk
import img_function as predict
import img_math as img_math
import  numpy as np



class UI_main():
    car = []
    pic_path = ""  # 图片路径
    colorimg = 'white'  # 车牌颜色
    cameraflag = 0

    def __init__(self):
        # 车牌颜色
        self.color_ct2 = ttk.Label(background=self.colorimg,
                                   text="", width="4", font=('Times', '14'))

        self.predictor = predict.CardPredictor()
        self.predictor.train_svm()

    def get_imgtk(self, img_bgr):
        img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(img)
        pil_image_resized = im.resize((500, 400), Image.ANTIALIAS)
        imgtk = ImageTk.PhotoImage(image=pil_image_resized)
        return imgtk

    def pic(self, pic_path):
        car = []
        img_bgr = img_math.img_read(pic_path)
        first_img, oldimg = self.predictor.img_first_pre(img_bgr)
        if not self.cameraflag:
            self.imgtk = self.get_imgtk(img_bgr)
        r_color, roi_color, color_color = self.predictor.img_only_color(oldimg,
                                                                        oldimg, first_img)
        print("|", color_color,
              r_color, "|")
        car.append(color_color+' '+r_color)
        print(car)
        return color_color,r_color,car


    # 来自图片--->打开系统接口获取图片绝对路径
    def from_pic(self):
        self.cameraflag = 0
        self.pic_path = '1.png'

        self.pic(self.pic_path)
if __name__ == '__main__':
    c=UI_main()
    c.from_pic()
    print(c.car)
