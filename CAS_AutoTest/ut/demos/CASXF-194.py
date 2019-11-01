import uiautomation as  automation
import time
from pynput.mouse import Button,Controller

def sugicalseg(i,x,y):
    AutomationId = "sugicalseg"+str(i)
    sugicalseg = automation.RadioButtonControl(AutomationId=AutomationId)
    sugicalseg.Click()
    automation.Win32API.MouseRightClick(x,y,0.1)
    automation.Win32API.MouseRightClick(x,y)

cas = automation.WindowControl(AutomationId="myMainWindow", Name="PatientManager", ClassName="Window", searchDepth=1)
cas.SetActive()

for loop in range(100):
    surgical_renalArtery_Scratch  = cas.ButtonControl(AutomationId="surgical_renalArtery_Scratch")
    surgical_renalArtery_Scratch.Click()

    # 执行提示框
    barwindow = automation.WindowControl(AutomationId="myMainWindow", Name="MetroProBarWindow", searchDepth=1)
    while not automation.WaitForDisappear(barwindow, 3):
        time.sleep(3)

    sugicalseg(1,858,451)
    sugicalseg(2,753,452)
    sugicalseg(3,979,487)
    sugicalseg(4,988,531)
    sugicalseg(5,991,594)
    sugicalseg(6,989,634)
    sugicalseg(7,743,552)
    sugicalseg(8,758,559)
    sugicalseg(9,741,619)
    sugicalseg(10,734,641)
    sugicalseg(11,764,647)



    surgical_show_Scratch =cas.ButtonControl(AutomationId="surgical_show_Scratch")
    surgical_show_Scratch.Click()
    # 执行提示框
    barwindow = automation.WindowControl(AutomationId="myMainWindow", Name="MetroProBarWindow", searchDepth=1)
    while not automation.WaitForDisappear(barwindow, 3):
        time.sleep(3)

    cas.CaptureToImage("分段显示结果%d"%loop)

    surgeryLiverSavecom = cas.ComboBoxControl(AutomationId="surgeryLiverSavecom",foundIndex=1)
    surgeryLiverSavecom.Select(u"支气管-方案1")

    SurgerySimulationASave =cas.ButtonControl(AutomationId="SurgerySimulationASave")
    SurgerySimulationASave.Click()
    time.sleep(5)
    surgeryLiverShowcom= cas.ComboBoxControl(AutomationId="surgeryLiverShowcom")
    surgeryLiverShowcom.Select(u"支气管-方案1")

    SurgerySimulationAShow =cas.ButtonControl(AutomationId="SurgerySimulationAShow")
    SurgerySimulationAShow.Click()
    time.sleep(5)

    automation.Win32API.MouseMoveTo(754,665)
    automation.Win32API.MouseMiddleClick(754,665,0.1)
    automation.Win32API.MouseMiddleClick(754,665)
    
    time.sleep(3)

    cas.CaptureToImage("分段中间双击%d"%loop)

    automation.Logger.WriteLine("test loop ##%d"%loop )