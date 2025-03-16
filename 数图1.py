# import cv2
# # 读取图像文件
# car_image = cv2.imread(r'C:\Users\21607\Desktop\car.png')
#
# # 检查图像是否成功加载
# if car_image is None:
#     print("图像加载失败，请检查文件路径和文件名是否正确。")
# else:
#     # 显示原始图像
#     cv2.imshow('Original Image', car_image)
#     cv2.waitKey(0)  # 等待按键操作
#
#     # 将彩色图像转换为灰度图像
#     gray_image = cv2.cvtColor(car_image, cv2.COLOR_BGR2GRAY)
#
#     # 显示灰度图像
#     cv2.imshow('Gray Image', gray_image)
#     cv2.waitKey(0)
#
#     # 保存灰度图像
#     cv2.imwrite(r'C:\Users\21607\Desktop\gray_car.png', gray_image)
#
#     # 获取图像的感兴趣区域
#     # 假设车牌区域的坐标为 (x1, y1, x2, y2)
#     x1, y1, x2, y2 = 453, 470, 538, 495  # 这些坐标需要根据实际情况调整
#     # 假设有人区域的坐标为 (x3, y3, x4, y4)
#     x3, y3, x4, y4 = 380, 165, 639, 284  # 这些坐标需要根据实际情况调整
#
#     # 截取车牌区域
#     license_plate_region = gray_image[y1:y2, x1:x2]
#     cv2.imshow('License Plate Region', license_plate_region)
#     cv2.waitKey(0)
#
#     # 截取有人区域
#     people_region = gray_image[y3:y4, x3:x4]
#     cv2.imshow('People Region', people_region)
#     cv2.waitKey(0)
#
#     cap = cv2.VideoCapture()
#
#     # 检查摄像头是否成功打开
#     if not cap.isOpened():
#         print("无法打开摄像头，请检查设备连接。")
#     else:
#         count = 0
#         while True:
#             ret, frame = cap.read()  # 读取一帧
#             if not ret:
#                 print("无法从摄像头读取帧，退出...")
#                 break
#
#             cv2.imshow('Camera', frame)
#
#             # 按下 's' 键截图
#             if cv2.waitKey(1) & 0xFF == ord('s'):
#                 cv2.imwrite(r'C:\Users\21607\Desktop\camera_shot_{}.png'.format(count), frame)
#                 count += 1
#                 if count > 2:  # 截图3张后退出
#                     break
#
#         cap.release()  # 释放摄像头资源
#
#     # 关闭所有窗口
#     cv2.destroyAllWindows()
# import cv2
#
# cap = cv2.VideoCapture()
#
# # 检查摄像头是否成功打开
# if not cap.isOpened():
# print("无法打开摄像头，请检查设备连接。")
# else:
# count = 0
# while True:
# ret, frame = cap.read() # 读取一帧
# if not ret:
# print("无法从摄像头读取帧，退出...")
# break
#
# cv2.imshow('Camera', frame)
#
# # 按下 's' 键截图
# if cv2.waitKey(1) & 0xFF == ord('s'):
# cv2.imwrite(r'C:\Users\21607\Desktop\camera_shot_{}.png'.format(count), frame)
# count += 1
# if count > 2: # 截图3张后退出
# break
#
# cap.release() # 释放摄像头资源
#
# # 关闭所有窗口
# cv2.destroyAllWindows()
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,GridsearchCV
import numpy as np
import matplotlib.pyplot as plt
ir = load_iris()
print(ir)
X_train,X_