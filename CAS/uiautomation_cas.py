import os, sys, time
import subprocess
import uiautomation as automation
from pywinauto import application
automation.ShowDesktop()
# 打开cas
subprocess.Popen(args='D:\Release-4396\Higemi.exe',cwd=r"D:\Release-4396")
# # 查找cas
cas = automation.WindowControl(searchDepth=1, AutomationId='myMainWindow', Name='Login')
# 可以判断window是否存在，如果不判断，找不到window的话会抛出异常
if automation.WaitForExist(cas, 3):
    automation.Logger.WriteLine("CAS exists now",logFile="cas.txt")
else:
    automation.Logger.WriteLine("CAS does not exist after 3 seconds",logFile="cas.txt")
cas.SetActive()
# # 登录
login = automation.ButtonControl(searchFromControl=cas,AutomationId ="btn_login")
# login=cas.ButtonControl(AutomationId ="btn_login")
login.Click()
# 查找病例
patientManager = automation.WindowControl(Name = 'PatientManager',AutomationId='myMainWindow')
patientManager.SetActive()
patient = automation.TextControl(searchFromControl=patientManager,Name = 'LI QIANG',ClassName="TextBlock",foundIndex=1)
patient.Click()
# # 进入三维重建
_3dRebuidBtn = patientManager.ButtonControl(AutomationId="_3dRebuidBtn")
_3dRebuidBtn.Click()
time.sleep(10)
lung = patientManager.ImageControl(AutomationId="lung")
lung.Click()
# 设置窗宽窗位
WL = patientManager.EditControl(AutomationId="WL")
WL.SetValue("600")
WB = patientManager.EditControl(AutomationId="WB")
WB.SetValue("1400")
w_OK = patientManager.ButtonControl(AutomationId = "w_OK")
w_OK.Click()
wwwl_preset = patientManager.ComboBoxControl(AutomationId="wwwl_preset")
wwwl_preset.Select("CT Lung")
# 选择种子点并执行
segmentation_TakePixel = patientManager.ButtonControl(AutomationId="segmentation_TakePixel")
segmentation_TakePixel.Click()
automation.Win32API.MouseClick(600,250)
automation.Win32API.MouseWheelDown(2)
automation.Win32API.MouseClick(600,350)
segmentation_Show = patientManager.ButtonControl(AutomationId = "segmentation_Show")
segmentation_Show.Click()
BarWindow = automation.WindowControl(Name= "MetroProBarWindow",AutomationId ="myMainWindow",ClassName="Window")
while automation.WaitForExist(BarWindow,3):
    pass
print("快速分割完成")
# 保存
save = patientManager.ButtonControl(AutomationId = "save")
save.Click()
umessageBox = automation.WindowControl(Name="UMessageBox",AutomationId ="myMainWindow",ClassName="Window")
if automation.WaitForExist(umessageBox,3):
    yes = umessageBox.TextControl(AutomationId ="tb_YES")
    yes.Click()
    print("保存成功")