from pywinauto.application import Application,findwindows
from pywinauto import mouse
from pywinauto import *
import time
import datetime
from pywinauto import uia_element_info
import subprocess
import os

# 启动程序
# 方法1
# subprocess.Popen(args='D:\CAS_Py_V1.0_R4165_P\Release\CAS_Py_V1.0_R4165_P.exe',cwd=r"D:\CAS_Py_V1.0_R4165_P\Release")
# specify an already running application
# 方法2
app = Application(backend="uia").start(cmd_line="D:\CAS_Py_V1.0_R4165_P\Release\CAS_Py_V1.0_R4165_P.exe",wait_for_idle=False,
                                       work_dir="D:\CAS_Py_V1.0_R4165_P\Release")
# 链接到程序
# app=Application(backend="uia").connect(path=r"D:\CAS_Py_V1.0_R4165_P\Release\CAS_Py_V1.0_R4165_P.exe")

# 登录
#  specify a dialog of the application
login_dialog=app["Login"]
login_dialog.draw_outline(colour="red")
# login_dialog.print_control_identifiers()
login_control=login_dialog["Button"]
login_control.draw_outline(colour="red")
login_control.click()
# print(type(app))

#  选择病例
PM_dialog = app["PatientManager"]
# print(type(PM_dialog))
# 标记dialog或者control
PM_dialog.draw_outline(colour="red")
# PM_dialog.print_control_identifiers()
# found_index :The index of the filtered out child element to return
Patient_control = PM_dialog.window(title="LI QIANG",class_name="DataGridCell",found_index=0)
Patient_control.draw_outline(colour="red")
# Patient_control.click()
# 控件的类型也是windowspecification
# print(type(Patient_control))
# print("*"*100)
# Patient_control.print_control_identifiers()
# print("*"*100)
# owner control 通过按键进行操作
Patient_control.type_keys("{HOME}")

# # 获取控件坐标位置，进行鼠标点击
# # Menu_3D = PM_dialog.window(title="三维重建",found_index=0)
# # Menu_3D.draw_outline(colour="red")
# # Menu_3D_location=Menu_3D.element_info.rectangle.mid_point()
# # print(Menu_3D_location)
# # mouse.click(button="left",coords=Menu_3D_location)

# # 控件没有title，使用automationID进行定位
# # 切换到三维重建模块
Menu_3D = PM_dialog.window(auto_id="_3dRebuidBtn",class_name="Button")
Menu_3D.draw_outline(colour="red")
Menu_3D.click()

# 切换到肺模块
time.sleep(10)
Organ = PM_dialog.window(auto_id="lung", control_type="Image")
Organ.click_input()

# 窗宽窗位调整,需要先删除窗宽窗位默认值，再输入肺窗值
WL =PM_dialog.window(auto_id="WL",class_name="TextBox")
WL.draw_outline(colour="red")
WL.set_focus()
WL.type_keys("^a"
             "{DELETE}"
             "{VK_SUBTRACT}600" )
WB =PM_dialog.window(auto_id="WB",class_name="TextBox")
WB.draw_outline(colour="red")
WB.set_focus()
WB.type_keys("^a"
             "{DELETE}"
             "1400")
WLWB_OK =PM_dialog.window(auto_id=r"w_OK",class_name="Button")
WLWB_OK.draw_outline(colour="red")
WLWB_OK.click_input()

#快速分割
Seg_Seeds=PM_dialog.window(auto_id="segmentation_TakePixel")
Seg_Seeds.draw_outline(colour="red")
Seg_Seeds.click_input()
Seed1_xy=(600,250)
mouse.click(button="left",coords=Seed1_xy)
time.sleep(1)
mouse.scroll(coords=Seed1_xy, wheel_dist=1)
time.sleep(1)
Seed2_xy=(600,350)
mouse.click(button="left",coords=Seed2_xy)
Show=PM_dialog.window(auto_id="segmentation_Show",class_name="Button")
Show.draw_outline(colour="red")
Show.click_input()

# 保存
# 需要处理2个弹出窗口:
# 1.正在执行的窗口 MetroProBarWindow
# 2.保存提示窗口
Popup= app["MetroProBarWindow"]
Popup.wait("exists",timeout=3, retry_interval=1)
print("正在执行中.......")
Popup.wait_not("exists",timeout=60, retry_interval=1)
print("执行完毕!")
Save = PM_dialog.window(auto_id="save",class_name="Button")
Save.draw_outline(colour="red")
Save.click_input()
MessageBox = app["uMessageBox"]
MessageBox.wait("exists",timeout=10, retry_interval=1)
MessageBox.window(title="是", auto_id="tb_YES").click_input()
time.sleep(20)

# 结果校验
Stl_Dir_Path = r"D:\CASImage\20190111\20190111142120_LI QIANG\Results\Stl"
Organ_Name = r"Lung.stl"
Organ_Stl_Path = os.path.join(Stl_Dir_Path,Organ_Name)
Organ_Stl_Size = os.path.getsize(Organ_Stl_Path)/float(1024*1024)
print("三维模型体积为%.2f M"%Organ_Stl_Size)
Organ_mtime = os.path.getmtime(Organ_Stl_Path)    #时间戳类型:自1970年1月1日(00:00:00 GMT)以来的秒数
Organ_mtime_str = datetime.datetime.fromtimestamp(Organ_mtime).strftime("%Y-%m-%d %H:%M:%S")  #转换为字符串日期时间
Now_time = time.time()
print("三维模型创建时间为:"+Organ_mtime_str)
assert Organ_Stl_Size > 1.0  and Now_time-Organ_mtime <60.0,"三维模型创建失败"