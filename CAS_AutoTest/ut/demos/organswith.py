import uiautomation as  automation
import time
from pynput.mouse import Button,Controller

def vmmap(patientname,module,loop):
    vmmap = automation.WindowControl(ClassName="VmMapClass",RegexName="VMMap - Sysinternals:")
    vmmap.SetActive()
    time.sleep(1)
    vmmap.SendKeys("{F5}")
    time.sleep(1)
    # scrollbar=vmmap.ScrollBarControl(AutomaitonId="1107",ClassName="ScrollBar")
    # scrollbar.RangeValuePatternSetValue(0)
    vmmap.CaptureToImage("%d_%s_%s_VMMAP.jpg"%(loop,patientname,module))
    time.sleep(1)


def patient_vmmap(patientname,index,loop):
    cas = automation.WindowControl(AutomationId="myMainWindow", Name="PatientManager", ClassName="Window",
                                   searchDepth=1)
    cas.SetActive()
    patientA = cas.CustomControl(ClassName="DataGridCell",Name=patientname,foundIndex=index)
    patientA.Click()

    rebuild = cas.TextControl(ClassName="Text",Name=u"三维重建")
    rebuild.Click()
    time.sleep(30)

    vmmap(patientname,"3D", loop)
    cas.SetActive()


    lungvessel = cas.ImageControl(AutomationId="lungvessel",ClassName="Image")
    lungvessel.Click()
    time.sleep(3)

    vmmap(patientname,"Vessel", loop)
    cas.SetActive()


    whole = cas.ImageControl(AutomationId="whole",ClassName="Image")
    whole.Click()
    time.sleep(3)

    vmmap(patientname,"Whole", loop)
    cas.SetActive()

    list = cas.TextControl(Name=u"病例管理",ClassName="Text",foundIndex=2)
    list.Click()
    time.sleep(3)

    vmmap(patientname,"List", loop)
    cas.SetActive()



for loop in range(100):
    patient_vmmap("LIU KAI MING",2,loop)
    patient_vmmap("ZHANG_MIN_RONG",1,loop)

