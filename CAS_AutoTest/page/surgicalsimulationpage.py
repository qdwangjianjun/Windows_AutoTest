from data.ui import SurgicalSimulationPageUI
from page.basepage import BasePage
import uiautomation as auto

class SurgicalSimulationPage(BasePage,SurgicalSimulationPageUI):
    #激活窗口
    def active_page(self):
        page = self.find(**self.page)
        page.SetActive()
        return self

    #手动调整窗宽窗位
    def ManualSetWLWB(self, WL, WB):
        surgical_WBWL = self.find(**self.surgical_WBWL)
        ImageControl2D = self.find(searchFromControl = surgical_WBWL,**self.ImageControl2D)
        imageBefor = self.CaptureImage(ImageControl2D,"../screenshots/imageBefor.png")
        WL_edit = self.find(searchFromControl = surgical_WBWL,**self.WL)
        WL_edit.SendKeys("{Ctrl}a{Del}")
        WL_edit.SendKeys(WL)
        WB_edit = self.find(searchFromControl = surgical_WBWL,**self.WB)
        WB_edit.SendKeys("{Ctrl}a{Del}")
        WB_edit.SendKeys(WB)
        W_OK = self.find(searchFromControl = surgical_WBWL,**self.wOK)
        W_OK.Click()
        imageAfter = self.CaptureImage(ImageControl2D,"../screenshots/imageAfter.png")
        image = [imageBefor,imageAfter]
        return image

    #自动调整窗宽窗位,返回设置前后的对比图片
    def AutoSetWLWB(self):
        surgical_WBWL = self.find(**self.surgical_WBWL)
        ImageControl2D = self.find(searchFromControl = surgical_WBWL,**self.ImageControl2D)
        imageBefor = self.CaptureImage(ImageControl2D,"../screenshots/imageBefor.png")
        auto.DragDrop(1500,356,1600,346)
        imageAfter = self.CaptureImage(ImageControl2D, "../screenshots/imageAfter.png")
        image = [imageBefor,imageAfter]
        return image

    #调整CT Preset
    def SetCTPreset(self):
        # index = 0
        resultValue = []
        surgical_WBWL = self.find(**self.surgical_WBWL)
        wwwl_preset = self.find(searchFromControl = surgical_WBWL,**self.CTPreset)
        WL_edit = self.find(searchFromControl=surgical_WBWL, **self.WL)
        WB_edit = self.find(searchFromControl=surgical_WBWL, **self.WB)
        for child in wwwl_preset.GetChildren():
            name = child.Name
            if name != ""  and  name != "CT Preset":
                wwwl_preset.Select(name)
                WLValue = WL_edit.GetValuePattern().Value
                WBValue = WB_edit.GetValuePattern().Value
                resultValue.append((WLValue,WBValue))
            # if index != 0:
            #     temp = index-1
            #     resultValue.insert(temp,(WLValue,WBValue))
            # index = index + 1
        return resultValue






