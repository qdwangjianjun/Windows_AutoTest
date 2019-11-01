# coding=utf-8
import glob
import os
import imageio
import pydicom
from medpy import metric
import numpy as  np
import time
from surface import Surface


# 完整显示numpy输出
# from numpy import *
# set_printoptions(threshold=NaN)


def get_dice(preds_path, labels_path, result_path):
    test_time = time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime())
    result = os.path.join(result_path, "results.txt")
    # 获取病人姓名
    patients = os.listdir(preds_path)
    dice = {}
    # 获取所有病人标签集合或者预测集合的图片张数
    global_slice_num = 0
    for patient in patients:
        pred_path = os.path.join(preds_path, patient)
        preds = sorted(glob.glob(os.path.join(pred_path, "*.bmp")))
        global_slice_num += len(preds)
    print(global_slice_num)
    # 创建array变量，存储全部的图片数据
    pred_all_data = np.zeros((512, 512, global_slice_num))
    label_all_data = np.zeros((512, 512, global_slice_num))
    local_slice_num = 0
    # 对每个病例进行DICE计算
    for patient in patients:
        # 获取标签集合和预测集合
        pred_path = os.path.join(preds_path, patient)
        label_path = os.path.join(labels_path, patient)
        preds = sorted(glob.glob(os.path.join(pred_path, "*.bmp")))
        labels = sorted(glob.glob(os.path.join(label_path, "*.bmp")))
        if len(preds) == len(labels):
            # 创建array变量，存储每个病人图片数据
            [width, height] = imageio.imread(preds[0]).shape
            pred_rawData = np.zeros((width, height, len(preds)))
            label_rawData = np.zeros((width, height, len(labels)))
            i = 0
            for pred, label in zip(preds, labels):
                # 读取图片，获取numpy array
                pred_array = imageio.imread(pred)
                label_array = imageio.imread(label)
                # 进行二值化处理
                pred_rawData[:, :, i] = pred_array / 255
                label_rawData[:, :, i] = label_array / 255
                # 循环将每张图片数据进行转换并保存
                i += 1
            # 对array进行数据格式转换
            pred_rawData = pred_rawData.astype(int)
            label_rawData = label_rawData.astype(int)
            # 计算该病人dice值
            dice[patient] = metric.dc(pred_rawData, label_rawData)
            per_result = "'%s'_Dice coefficient：%.2f" % (patient, dice[patient])
            print(per_result)
            with open(result, mode='a') as file:
                file.write(test_time)
                file.write("    ")
                file.write(per_result)
                file.write("\n")
            # 计算全局dice
            pred_all_data[:, :, local_slice_num:local_slice_num + len(preds)] = pred_rawData
            label_all_data[:, :, local_slice_num:local_slice_num + len(labels)] = label_rawData
            local_slice_num += len(preds)
        else:
            print("标签集合和预测集合张数不一致")

    dice["all"] = metric.dc(pred_all_data, label_all_data)
    all_result = "AllPatients_Dice coefficient：%.2f" % dice["all"]
    print(all_result)
    with open(result, mode='a') as file:
        file.write(test_time)
        file.write("    ")
        file.write(all_result)
        file.write("\n")
    return dice


def get_assd(preds_path, labels_path, dicoms_path, result_path, ):
    test_time = time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime())
    result = os.path.join(result_path, "results.txt")
    assd = {}
    all_assd = 0
    # 获取病人姓名
    patients = os.listdir(preds_path)
    for patient in patients:
        # 获取标签集合和预测集合
        pred_path = os.path.join(preds_path, patient)
        label_path = os.path.join(labels_path, patient)
        dicom_path = os.path.join(dicoms_path, patient)
        preds = sorted(glob.glob(os.path.join(pred_path, "*.bmp")))
        labels = sorted(glob.glob(os.path.join(label_path, "*.bmp")))
        # 创建array变量，存储每个病人图片数据
        [width, height] = imageio.imread(preds[0]).shape
        pred_rawData = np.zeros((width, height, len(preds)))
        label_rawData = np.zeros((width, height, len(labels)))
        i = 0
        for pred, label in zip(preds, labels):
            # 读取图片，获取numpy array
            pred_array = imageio.imread(pred)
            label_array = imageio.imread(label)
            # 进行二值化处理
            pred_rawData[:, :, i] = pred_array / 255
            label_rawData[:, :, i] = label_array / 255
            # 循环将每张图片数据进行转换并保存
            i += 1
        # 对array进行数据格式转换
        pred_rawData = pred_rawData.astype(int)
        label_rawData = label_rawData.astype(int)
        # print("*"*30)
        print(dicom_path)
        pixel_info = get_pixel_info(dicom_path)
        print(patient, "_像素间距:", pixel_info)
        # print("*"*30)
        evalsurf = Surface(pred_rawData, label_rawData, physical_voxel_spacing=pixel_info, mask_offset=[0., 0., 0.],
                           reference_offset=[0., 0., 0.])
        assd[patient] = evalsurf.get_average_symmetric_surface_distance()
        per_result = "'%s'_the average symmetric surface distance：%.2f" % (patient, assd[patient])
        print(per_result)
        with open(result, mode='a') as file:
            file.write(test_time)
            file.write("    ")
            file.write(per_result)
            file.write("\n")

    for key in assd.keys():
        all_assd += assd.get(key)

    average_assd = all_assd / len(assd)
    average_result = "AllPatients_the average symmetric surface distance：%.2f" % (average_assd)
    print(average_result)
    with open(result, mode='a') as file:
        file.write(test_time)
        file.write("    ")
        file.write(average_result)
        file.write("\n")
    return  assd


def get_pixel_info(dcm_data_dir):
    dcm_files = os.listdir(dcm_data_dir)
    dcm_file_1 = os.path.join(dcm_data_dir, dcm_files[0])
    dcm_tag_1 = pydicom.dcmread(dcm_file_1)
    # 获取像素间距.
    spacex, spacey = dcm_tag_1.PixelSpacing
    # 获取层间距
    # 有些 dcm图像并不是按照InstanceNumber进行排序的，不能直接用最后一张的slicelocation减去第一张，再除以张数
    SliceLocations = []
    ImagePositon_z = []
    for dcm in dcm_files:
        dcm_file = os.path.join(dcm_data_dir, dcm)
        dcm_tag = pydicom.dcmread(dcm_file)
        SliceLocations.append(dcm_tag.SliceLocation)
        ImagePositon_z.append(dcm_tag.ImagePositionPatient[2])
    SliceLocations_max = max(SliceLocations)
    SliceLocations_min = min(SliceLocations)
    ImagePositon_z_max = max(ImagePositon_z)
    ImagePositon_z_min = min(ImagePositon_z)
    # print(SliceLocations_max)
    # print(SliceLocations_min)
    # print(ImagePositon_z_max)
    # print(ImagePositon_z_min)
    if SliceLocations_max - SliceLocations_min < 1e-10:
        spacez = abs(ImagePositon_z_max - ImagePositon_z_min) / (len(dcm_files) - 1)
    else:
        spacez = abs(SliceLocations_max - SliceLocations_min) / (len(dcm_files) - 1)
    pixel_infos = [spacex, spacey, spacez]

    return pixel_infos


preds_path = r"E:\Auto_Bronchus_mimics\predict"
labels_path = r"E:\Auto_Bronchus_mimics\label"
result_path = r"E:\Auto_Bronchus_mimics"
dicoms_path = r"E:\Auto_Bronchus_mimics\dicom"

print(get_dice(preds_path,labels_path,result_path))
# print(get_assd(preds_path, labels_path, dicoms_path, result_path))
