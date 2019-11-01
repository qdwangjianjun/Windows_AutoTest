import uiautomation as  automation
import time
from pynput.mouse import Button,Controller
cas = automation.WindowControl(AutomationId="myMainWindow", Name="PatientManager", ClassName="Window", searchDepth=1)
cas.SetActive()
for loop in range(1):
    # 调整滑块位置
    my3DSegmentation_Bone = cas.CustomControl(ClassName="Segmentation_Bone",AutomationId="my3DSegmentation_Bone")
    silderDouble = my3DSegmentation_Bone.CustomControl(ClassName="SilderArrange",AutomationId="silderDouble")
    silderDouble.GetChildren()[2].RangeValuePatternSetValue(2493)
    time.sleep(1)
    silderDouble.GetChildren()[1].RangeValuePatternSetValue(822)

    # 生成

    generate= my3DSegmentation_Bone.ButtonControl(AutomaitonId ="Generate",ClassName="Button")
    generate.Click()

    time.sleep(5)
    # 区域A划线
    regionA = my3DSegmentation_Bone.ButtonControl(AutomationId="segmentation_ForeGround_Command",Name="Region A")
    regionA.Click()

    automation.Win32API.MouseMoveTo(677,415)
    mouse = Controller()
    mouse.press(Button.left)
    mouse.move(55,-35)
    time.sleep(0.5)
    mouse.position(70,35)
    mouse.release(Button.left)

    # 区域B划线
    regionB = my3DSegmentation_Bone.ButtonControl(AutomationId="segmentation_ForeGround_Command",Name="Region B")
    regionB.Click()
    mouse.position(855,404)
    mouse.press(Button.left)
    mouse.position(876,384)
    mouse.release(Button.left)

    # 点击显示
    show = my3DSegmentation_Bone.ButtonControl(AutomationId="segmentation_Graphcut_Show_Command",Name=u"显示")
    show.Click()
    # 执行提示框
    barwindow = automation.WindowControl(AutomationId="myMainWindow", Name="MetroProBarWindow", searchDepth=1)
    while not automation.WaitForDisappear(barwindow, 5):
        time.sleep(3)

    select_save_organ_A = my3DSegmentation_Bone.ComboBoxControl(AutomationId="select_save_organ_A")
    select_save_organ_A.Select(u"肋骨")
    time.sleep(10)
    # 重置
    reset= cas.ButtonControl(AutomationId="reset",Name=u"重置")
    reset.Click()





    # lung = cas.ImageControl(AutomationId = "lung",ClassName ="Image")
    # lung.Click()
    #
    #
    # takepixel = cas.ButtonControl(ClassName="Button",AutomationId="segmentation_TakePixel")
    # takepixel.Click()
    #
    # automation.Win32API.MouseClick(631,265)
    # automation.Win32API.MouseClick(599,272)
    # automation.Win32API.MouseClick(861,285)
    # automation.Win32API.MouseClick(846,352)
    #
    # show = cas.ButtonControl(AutomationId ="segmentation_Show",ClassName="Button")
    # show.Click()
    #
    # barwindow = automation.WindowControl(AutomationId="myMainWindow", Name="MetroProBarWindow", searchDepth=1)
    # while not automation.WaitForDisappear(barwindow, 5):
    #     time.sleep(3)
    #
    # save = cas.ButtonControl(AutomationId="save", ClassName="Button")
    # save.Click()
    #
    # messagebox1 = automation.WindowControl(AutomationId="myMainWindow", Name="UMessageBox", searchDepth=1)
    # yes1 = messagebox1.TextControl(ClassName="TextBlock", AutomationId="tb_YES")
    # yes1.Click()
    # time.sleep(5)
    #
    # lungvessel = cas.ImageControl(AutomationId="lungvessel", ClassName="Image")
    # lungvessel.Click()
    # messagebox2 = automation.WindowControl(AutomationId="myMainWindow", Name="UMessageBox", searchDepth=1)
    # yes2 = messagebox2.TextControl(ClassName="TextBlock", AutomationId="tb_YES")
    # yes2.Click()
    #
    # BloodSegmentation = cas.ButtonControl(AutomationId="seg_BloodSegmentation", ClassName="Button")
    # BloodSegmentation.Click()
    #
    # while not automation.WaitForDisappear(barwindow, 5):
    #     time.sleep(3)
    # save.Click()
    # messagebox1 = automation.WindowControl(AutomationId="myMainWindow", Name="UMessageBox", searchDepth=1)
    # yes1 = messagebox1.TextControl(ClassName="TextBlock", AutomationId="tb_YES")
    # yes1.Click()
    # time.sleep(5)
    #
    # automation.Logger.WriteLine("the loop no:%d"%loop)
