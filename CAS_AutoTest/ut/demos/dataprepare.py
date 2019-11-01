import os
import glob
import zipfile
import shutil
import subprocess
import uiautomation as uia
patients_path = "E:\lung"

def mimics_unzip_rename(patients_path):
    for patient in os.listdir(patients_path):
        patient_path = os.path.join(patients_path,patient)
        if os.path.isdir(patient_path):
            file_zip_path = glob.glob(os.path.join(patient_path,"*.zip"))
            stl = glob.glob(os.path.join(patient_path,"*.stl"))
            print(file_zip_path,stl)
            if file_zip_path and stl:
                file_zip = zipfile.ZipFile(file_zip_path[0])
                for file in file_zip.namelist():
                    mimics_path = os.path.join(patient_path,"mimics")
                    file_zip.extract(file,os.path.join(mimics_path,"Artery"))
                file_zip.close()
                print("zipfile解压完成")
                shutil.copyfile(stl[0],os.path.join(mimics_path,"Artery.stl"))
                print("stl重命名成功")

def result_bak(patients_path):
    for patient in os.listdir(patients_path):
        patient_path = os.path.join(patients_path,patient)
        if os.path.isdir(patient_path):
            result_path = os.path.join(patient_path,"Results")
            if os.path.exists(result_path):
                artery_path = os.path.join(result_path,"Artery")
                artery_path_bak = os.path.join(result_path,"Artery_bak")
                stl_path = os.path.join(result_path,"stl/Artery.stl")
                stl_path_bak = os.path.join(result_path,"stl/Artery_bak.stl")
                if os.path.exists(artery_path):
                    os.rename(artery_path,artery_path_bak)
                else:
                    print("Artery不存在")
                if os.path.exists(stl_path):
                    os.rename(stl_path,stl_path_bak)
                else:
                    print("Artery.stl不存在")
                os.mkdir(artery_path)

# result_bak(patients_path)

def gettestdata(patients_path):
    for patient in os.listdir(patients_path):
        patient_path = os.path.join(patients_path,patient)

