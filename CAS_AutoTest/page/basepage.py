from data.setting import Setting
import uiautomation as auto
import pyautogui as autogui
import time
from log.log import Log
from PIL import Image
from PIL import ImageChops

class BasePage(Setting):

    def find(self, ControlTypeName = "Control", **kwargs):

        if ControlTypeName == "Control":
            control = auto.Control(**kwargs)

        if ControlTypeName == "ButtonControl":
            control = auto.ButtonControl(**kwargs)

        if ControlTypeName == "CalendarControl":
            control = auto.CalendarControl(**kwargs)

        if ControlTypeName == "CheckBoxControl":
            control = auto.CheckBoxControl(**kwargs)

        if ControlTypeName == "ComboBoxControl":
            control = auto.ComboBoxControl(**kwargs)

        if ControlTypeName == "CustomControl":
            control = auto.CustomControl(**kwargs)

        if ControlTypeName == "DataGridControl":
            control = auto.DataGridControl(**kwargs)

        if ControlTypeName == "DataItemControl":
            control = auto.DataItemControl(**kwargs)

        if ControlTypeName == "DocumentControl":
            control = auto.DocumentControl(**kwargs)

        if ControlTypeName == "EditControl":
            control = auto.EditControl(**kwargs)

        if ControlTypeName == "GroupControl":
            control = auto.GroupControl(**kwargs)

        if ControlTypeName == "HeaderControl":
            control = auto.HeaderControl(**kwargs)

        if ControlTypeName == "HeaderItemControl":
            control = auto.HeaderItemControl(**kwargs)

        if ControlTypeName == "HyperlinkControl":
            control = auto.HyperlinkControl(**kwargs)

        if ControlTypeName == "ImageControl":
            control = auto.ImageControl(**kwargs)

        if ControlTypeName == "ListControl":
            control = auto.ListControl(**kwargs)

        if ControlTypeName == "ListItemControl":
            control = auto.ListItemControl(**kwargs)

        if ControlTypeName == "MenuControl":
            control = auto.MenuControl(**kwargs)

        if ControlTypeName == "MenuBarControl":
            control = auto.MenuBarControl(**kwargs)

        if ControlTypeName == "MenuItemControl":
            control = auto.MenuItemControl(**kwargs)

        if ControlTypeName == "PaneControl":
            control = auto.PaneControl(**kwargs)

        if ControlTypeName == "ProgressBarControl":
            control = auto.ProgressBarControl(**kwargs)

        if ControlTypeName == "RadioButtonControl":
            control = auto.RadioButtonControl(**kwargs)

        if ControlTypeName == "ScrollBarControl":
            control = auto.ScrollBarControl(**kwargs)

        if ControlTypeName == "SemanticZoomControl":
            control = auto.SemanticZoomControl(**kwargs)

        if ControlTypeName == "SeparatorControl":
            control = auto.SeparatorControl(**kwargs)

        if ControlTypeName == "SliderControl":
            control = auto.SliderControl(**kwargs)

        if ControlTypeName == "SpinnerControl":
            control = auto.SpinnerControl(**kwargs)

        if ControlTypeName == "SplitButtonControl":
            control = auto.SplitButtonControl(**kwargs)

        if ControlTypeName == "StatusBarControl":
            control = auto.StatusBarControl(**kwargs)

        if ControlTypeName == "TabControl":
            control = auto.TabControl(**kwargs)

        if ControlTypeName == "TabItemControl":
            control = auto.TabItemControl(**kwargs)

        if ControlTypeName == "TextControl":
            control = auto.TextControl(**kwargs)

        if ControlTypeName == "ThumbControl":
            control = auto.ThumbControl(**kwargs)

        if ControlTypeName == "TitleBarControl":
            control = auto.TitleBarControl(**kwargs)

        if ControlTypeName == "ToolBarControl":
            control = auto.ToolBarControl(**kwargs)

        if ControlTypeName == "ToolTipControl":
            control = auto.ToolTipControl(**kwargs)

        if ControlTypeName == "TreeControl":
            control = auto.TreeControl(**kwargs)

        if ControlTypeName == "TreeItemControl":
            control = auto.TreeItemControl(**kwargs)

        if ControlTypeName == "WindowControl":
            control = auto.WindowControl(**kwargs)

        if control.Exists():
           return control
        else:
            name = kwargs.__str__().replace(":","：")
            Log.logger().error("元素查找失败%s"%name)
            autogui.screenshot("../log/%s.png" %name)
    #等待控件消失
    def WaitUntillDisappear(self,control):
        while not auto.WaitForDisappear(control, 5):
            time.sleep(3)

            # 比较两个图片
    def compare_images(self, path_one, path_two):
            """
            比较图片，如果有不同则生成展示不同的图片
            @参数一: path_one: 第一张图片的路径
            @参数二: path_two: 第二张图片的路径
            @返回：两个图片一样返回True，否则返回False
            """
            image_one = Image.open(path_one)
            image_two = Image.open(path_two)
            diff = ImageChops.difference(image_one, image_two)
            if diff.getbbox() is None:
               return True
            else:
               return False

   #对控件截图
    def CaptureImage(self, control, name):
        control.CaptureToImage("../screenshots/%s.png" % name)

 #   def ScreenControl(self,control):

    # def load_yaml(self,pageurl,element,**kwargs):
    #     with open(file=pageurl,mode="r",encoding="utf-8") as f:
    #         data = yaml.safe_load(f)
    #     element_locator = data[element]
    #     for k,v in kwargs.items():
    #         for keys in element_locator.keys():
    #             element_locator[keys] = str(element_locator[keys]).replace("$%s"%k,v)
    #     if "searchFromControl" in element_locator.keys():
    #         if "searchFromControl" not in element_locator["searchFromControl"].keys():
    #             parent_element = self.find(element_locator["searchFromControl"])
    #             element_locator.pop("searchFromControl")
    #             element = self.find(searchFromControl = parent_element,**element_locator)
    #         else:
    #             parent_element_locator = element_locator["searchFromControl"]["searchFromControl"]
    #             element_locator["searchFromControl"].pop("searchFromControl")
    #             sub_element_locator  = element_locator["searchFromControl"]
    #             parent_element = self.find(**parent_element_locator)
    #             sub_element = self.find(searchFromControl = parent_element,**sub_element_locator)
    #             element_locator.pop("searchFromControl")
    #             element = self.find(searchFromControl = sub_element,**element_locator)
    #     else:
    #         element = self.find(**element_locator)
    #     return element







