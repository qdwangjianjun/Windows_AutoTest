import uiautomation as  automation
import time

for loop in range(50):
    cas = automation.WindowControl(AutomationId="myMainWindow",Name="PatientManager",ClassName="Window",searchDepth=1)
    cas.SetActive()

    NewPatient = cas.ButtonControl(AutomationId = "NewPatient",ClassName="Button")
    NewPatient.Click()

    main_AddPatient = cas.CustomControl(AutomationId =  "main_AddPatient",ClassName="AddPatient")
    organ = main_AddPatient.TextControl(Name=u"肺")
    organ.Click()

    fenqi = main_AddPatient.ButtonControl(AutomationId="OK",Name=u"分期加载")
    fenqi.Click()


    patient = automation.WindowControl(AutomationId="myMainWindow",Name="PatientManager",ClassName="Window",searchDepth=2)

    # files= patient.MenuItemControl(ClassName="MenuItem",Name=u"文件")
    # files.Click()
    # openfiles = files.MenuItemControl(ClassName="MenuItem",Name=u"打开文件")
    # openfiles.Click()

    # wins= automation.WindowControl(ClassName="#32770",Name=u"浏览文件夹")
    # test= wins.TreeItemControl(Name="test")
    # test.Click()
    #
    # ok = wins.ButtonControl(Name=u"确定",ClassName="Button",AutomationId="1")
    # ok.Click()
    #
    # time.sleep(45)
    close = patient.ButtonControl(AutomationId="newPatient_Close",ClassName="Button")
    close.Click()

    messagebox = automation.WindowControl(AutomationId="myMainWindow",Name="UMessageBox",searchDepth=1)
    yes = messagebox.TextControl(ClassName="TextBlock",AutomationId="tb_YES")
    yes.Click()

    automation.Logger.WriteLine("TEST NO ##%d"%loop)