import uiautomation as  automation
import time

cas = automation.WindowControl(AutomationId="myMainWindow", Name="PatientManager", ClassName="Window", searchDepth=1)
cas.SetActive()
for loop in range(100):

    lung = cas.ImageControl(AutomationId = "lung",ClassName ="Image")
    lung.Click()

    takepixel = cas.ButtonControl(ClassName="Button",AutomationId="segmentation_TakePixel")
    takepixel.Click()

    automation.Win32API.MouseClick(631,265)
    automation.Win32API.MouseClick(599,272)
    automation.Win32API.MouseClick(861,285)
    automation.Win32API.MouseClick(846,352)

    show = cas.ButtonControl(AutomationId ="segmentation_Show",ClassName="Button")
    show.Click()

    barwindow = automation.WindowControl(AutomationId="myMainWindow", Name="MetroProBarWindow", searchDepth=1)
    while not automation.WaitForDisappear(barwindow, 5):
        time.sleep(3)

    save = cas.ButtonControl(AutomationId="save", ClassName="Button")
    save.Click()

    messagebox1 = automation.WindowControl(AutomationId="myMainWindow", Name="UMessageBox", searchDepth=1)
    yes1 = messagebox1.TextControl(ClassName="TextBlock", AutomationId="tb_YES")
    yes1.Click()
    time.sleep(5)

    lungvessel = cas.ImageControl(AutomationId="lungvessel", ClassName="Image")
    lungvessel.Click()
    messagebox2 = automation.WindowControl(AutomationId="myMainWindow", Name="UMessageBox", searchDepth=1)
    yes2 = messagebox2.TextControl(ClassName="TextBlock", AutomationId="tb_YES")
    yes2.Click()

    BloodSegmentation = cas.ButtonControl(AutomationId="seg_BloodSegmentation", ClassName="Button")
    BloodSegmentation.Click()

    while not automation.WaitForDisappear(barwindow, 5):
        time.sleep(3)
    save.Click()
    messagebox1 = automation.WindowControl(AutomationId="myMainWindow", Name="UMessageBox", searchDepth=1)
    yes1 = messagebox1.TextControl(ClassName="TextBlock", AutomationId="tb_YES")
    yes1.Click()
    time.sleep(5)

    automation.Logger.WriteLine("the loop no:%d"%loop)
