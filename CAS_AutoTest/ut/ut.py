# from pywinauto.application import Application
# from pywinauto.controls import hwndwrapper
# from pywinauto.controls.hwndwrapper import HwndWrapper
#
# from data.setting import Setting

# app = Application(backend="uia").connect(path= Setting.exepath)
#
# window = app.window(auto_id = "myMainWindow",title="Login")
# username = window.child_window(auto_id="txt_username")
# username.draw_outline()
# username.type_keys("^a"
#                    "{VK_DELETE}")
# username.type_keys("CAS")
# userpwd = window.child_window(auto_id="txt_userpwd")
# userpwd.draw_outline()
# userpwd.type_keys("^a"
#                    "{VK_DELETE}")
# userpwd.type_keys("HISENSE")
# login:HwndWrapper = window.child_window(auto_id="txt_userpwd")[0]
# login.draw_outline()
# login.click()

# app = Application(backend="uia").connect(path= Setting.exepath)
# window = app.window(auto_id = "myMainWindow",title="PatientManager")
# control = window.child_window(class_name="Text",title="二维阅片")
# print(control.rectangle())
# (L448, T12, R575, B42)


# import  uiautomation as  auto
#
# window = auto.WindowControl(AutomationId="myMainWindow",Name="PatientManager")
#
# control = window.Control(ClassName="Text",Name="二维阅片")
#
# print(control.BoundingRectangle)
# # (448,12,575,42)[127x30]

# import uiautomation as auto
# auto.WindowControl(searchDepth=1, AutomationId="myMainWindow", RegexName="Login").SetActive()
#
# auto.Control(AutomationId="txt_username").SendKeys("abc")


# dict ={"a":1,"b":3}
#
# def add(a=1,b=2):
#     print(a+b)
#
# add(**dict)

# coding=utf-8
#
#
# import os,subprocess
#
# with  os.popen("automation.py -t3","r") as cmd:
#     cmd.read()

# from data.setting import Setting
# import yaml


# datapath = Setting.datapath
# with open(file=r"../data/data.yaml", mode="r", encoding="utf-8") as f:
#     data = yaml.safe_load(f)
# print(data)
# pageui = data["LoginPage"]
#
# print(pageui)
# import pyguiauto
import  uiautomation as  auto
# import yaml
import pyautogui
# window = auto.WindowControl(AutomationId="myMainWindow",Name="PatientManager")
#
# firstrow = auto.Control(searchFromControl=window,AutomationId ="MainRight_Page").DataGridControl(AutomationId="examHistoryData").\
#     DataItemControl(ClassName="DataGridRow",foundIndex=1)
# firstrow.Click()
from page.basepage import BasePage
from page.patientpage import PatientPage
from page.surgicalsimulationpage import SurgicalSimulationPage


# def load_yaml(element,**kwargs):
#     pageurl = r"../data/patientpage.yaml"
#     base = BasePage()
#     with open(file=pageurl, mode="r", encoding="utf-8") as f:
#         data = yaml.safe_load(f)
#     element_locator = data[element]
#     for k, v in kwargs.items():
#         for keys in element_locator.keys():
#             element_locator[keys] = str(element_locator[keys]).replace("$%s" % k, str(v))
#     print(element_locator)
#     if "searchFromControl" in element_locator.keys():
#         parent_element = auto.ControlFromHandle(int(element_locator["searchFromControl"]))
#         print(parent_element)
#         element_locator.pop("searchFromControl")
#         print(element_locator)
#         element = base.find(searchFromControl=parent_element, **element_locator)
#         print(element)
#
#     else:element = base.find(element_locator)
#
#     return element

    # if "searchFromControl" in element_locator.keys():
    #     if "searchFromControl" not in element_locator["searchFromControl"].keys():
    #         parent_element = self.find(element_locator["searchFromControl"])
    #         element_locator.pop("searchFromControl")
    #         element = self.find(searchFromControl=parent_element, **element_locator)
    #     else:
    #         parent_element_locator = element_locator["searchFromControl"]["searchFromControl"]
    #         element_locator["searchFromControl"].pop("searchFromControl")
    #         sub_element_locator = element_locator["searchFromControl"]
    #         parent_element = self.find(**parent_element_locator)
    #         sub_element = self.find(searchFromControl=parent_element, **sub_element_locator)
    #         element_locator.pop("searchFromControl")
    #         element = self.find(searchFromControl=sub_element, **element_locator)
    # else:
    #     element = self.find(**element_locator)

# window = auto.WindowControl(AutomationId="myMainWindow",Name="PatientManager",searchDepth =1)
# window.SetActive()
# a = auto.FindControl(window,lambda c:(isinstance(c, auto.DataGridControl) or isinstance(c, auto.DataItemControl) and c.Name == 'ZHANG_QING_MEI'))
# a.Click()
#
# page = PatientPage()
# page.active_page()
# # pyautogui.click(pyautogui.locateCenterOnScreen(r"../screenshots/scroll_up.PNG"))
#
# base = BasePage()
# locator = {"ClassName":"DataGridRow","foundIndex":1}
# base.find(**locator)
# a =auto.Control(AutomationId="my123")
# print(a.Exists())
# print(window)
# print(window.__str__())
# print(window.NativeWindowHandle)
# windowhandle = window.NativeWindowHandle
# parent =  auto.Control(AutomationId="examHistoryData")
# print(parent)
# print(parent.NativeWindowHandle)
# firstrow = load_yaml("firstrow2",var1=parent.NativeWindowHandle)
# firstrow.Click()


#
# win = auto.WindowControl(searchDepth=1, ClassName='Notepad')
# win.SetActive()
# file = win.MenuItemControl(Name="文件(F)",Depth=2)
#
# file.Click()
from PIL import ImageGrab
import uiautomation as auto
from PIL import Image
from PIL import ImageChops
import math
import operator
from functools import reduce
# page = SurgicalSimulationPage()
# page.active_page()
#
# region = auto.PaneControl(Name = 'ImageControl2D',searchDepth=5)
# #box= (339,56,1919,1076)
# #im = ImageGrab.grab(box)
#

#
# CaptureImage(region,'1')
# page.ManualSetWLWB("200","100")
# CaptureImage(region,'2')
# img1 = "../screenshots/1.png"
# img2 = "../screenshots/2.png"
# def image_contrast(img1, img2):
#
#     image1 = Image.open(img1)
#     image2 = Image.open(img2)
#
#     h1 = image1.histogram()
#     h2 = image2.histogram()
#
#     result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
#     return result
# compare_result =  image_contrast(img1,img2)
# print(compare_result)


# def compare_images(path_one, path_two):
#   """
#   比较图片，如果有不同则生成展示不同的图片
#   @参数一: path_one: 第一张图片的路径
#   @参数二: path_two: 第二张图片的路径
#   @参数三: diff_save_location: 不同图的保存路径
#   """
#   image_one = Image.open(path_one)
#   image_two = Image.open(path_two)
#   diff = ImageChops.difference(image_one, image_two)
#   if diff.getbbox() is None:
#     return True
#   else:
#     return False
from page.surgicalsimulationpage import SurgicalSimulationPage
surgicalsimulationpage = SurgicalSimulationPage()
surgicalsimulationpage.active_page()
a = surgicalsimulationpage.SetCTPreset()
print(a)
