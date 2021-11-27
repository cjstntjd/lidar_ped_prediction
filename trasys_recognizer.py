import sys,pre_ui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication,QDate,Qt
import re
from PyQt5 import uic
import cv2
import sys
import pyrealsense2 as rs
import numpy as np
from PyQt5.QtWidgets import  QWidget, QLabel, QApplication, QPushButton, QFileDialog, QDesktopWidget
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot, QCoreApplication
from PyQt5.QtGui import QImage, QPixmap,  QScreen
from PyQt5 import QtCore
import os
from datetime import datetime
from darkflow.qualify import *
import random
import time
import threading
import pipline_v1

sys.setrecursionlimit(5000)

global tfnet
global color

colors = [tuple(255*np.random.rand(3)) for i in range(100)]
global mode
mode = 0
global save_path
global fps_frame
global rec
rec =0
fps_frame=1
global per_li
per_li = []
net = ret_model()

class Thread(QThread):
    changePixmap = pyqtSignal(QImage)

    def run(self):

        
        pipeline = rs.pipeline() #센서연결
        config = rs.config() # 설정
        config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30) # 설정변경
        config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30) #설정변경
        pipeline.start(config)
        global mode
        global rec
        global fps_frame
        global per_li
        
        try:
            while True:            
                frames = pipeline.wait_for_frames() #큰프레임
                depth_frame = frames.get_depth_frame() #내부프레임
                color_frame = frames.get_color_frame() #내부프레임

                if not depth_frame or not color_frame:
                    continue

                depth_image = np.asanyarray(depth_frame.get_data()) 
                color_image = np.asanyarray(color_frame.get_data())
                depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
                
                if mode == 0:
                    input_rec_image = color_image
                elif mode == 1:
                    if rec == 0:
                        input_rec_image = depth_colormap
                    elif rec == 1:
                        results = pred(net,color_image)
                        input_rec_image = pipline_v1.make_img(colors,results,depth_colormap,depth_image,0)
                elif mode == 2:
                    if rec == 0:
                        input_rec_image = np.hstack((color_image,depth_colormap))
                    elif rec == 1:
                        results = pred(net,color_image)
                        output_dep = pipline_v1.make_img(colors,results,depth_colormap,depth_image,0)
                        input_rec_image = np.hstack((color_image,output_dep))
                elif mode == 3:
                    if rec == 0:
                        input_rec_image = np.hstack((color_image,depth_colormap))
                    elif rec == 1:
                        results = pred(net,color_image)
                        output_dep = pipline_v1.make_img(colors,results,depth_colormap,depth_image,1)
                        input_rec_image = np.hstack((color_image,output_dep))

                    
                cap = input_rec_image
                rgbImage = cv2.cvtColor(cap, cv2.COLOR_BGR2RGB) 
                h, w, ch = rgbImage.shape 
                bytesPerLine = ch * w 
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)    
               
        finally:
            pipeline.stop()
    
    


class MyApp(pre_ui.Ui_Dialog,QDialog):


    def __init__(self):
        super().__init__()
        QDialog.__init__(self, None, Qt.WindowStaysOnTopHint)
        self.setupUi(self)
        self.initUI()
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))
        self.label.setScaledContents( True )
 
    
    def initUI(self):

        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()

        #버튼과 ui 상호작용
        self.start.clicked.connect(self.start_record)
        self.start.setToolTip('검지를 시작 합니다.')

        self.cctv.clicked.connect(self.change_cctv)
        self.lidar.clicked.connect(self.change_lidar)
        self.dual.clicked.connect(self.change_dual)
        self.distance.clicked.connect(self.change_distance)

        self.setWindowTitle('TRASYS Recognizer')
        self.move(300, 300)
        self.resize(1100,750)
        self.show()

    def change_dual(self):
        global mode
        mode = 2

    def change_cctv(self):
        global mode
        mode = 0

    def change_lidar(self):
        global mode
        mode = 1
    
    def change_distance(self):
        global mode
        mode = 3


    def start_record(self):
        global rec
        if rec == 0:
            rec = 1
            self.status.setText("검지 중 입니다.")
            
        elif rec == 1:
            rec = 0
            self.status.setText("정지 중") 
    
    
    

if __name__ == '__main__':
    
    app = QApplication(sys.argv) 
    ex = MyApp()
    sys.exit(app.exec_())
        