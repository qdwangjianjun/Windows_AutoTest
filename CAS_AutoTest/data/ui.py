class LoginPageUI(object):
    def __init__(self):
        self.page= {"ControlTypeName": "WindowControl", "searchDepth":1, "AutomationId": "myMainWindow", "RegexName": "Login"}
        self.username = {"AutomationId":"txt_username", "searchDepth":2}
        self.userpwd = {"AutomationId":"txt_userpwd", "searchDepth":2}
        self.loginbtn = {"ClassName":"Text", "Name":"登录"}

class PatientPageUI(object):
    def __init__(self):
        self.page = {"ControlTypeName": "WindowControl", "searchDepth": 1, "AutomationId": "myMainWindow",
                     "RegexName": "PatientManager"}
        self.textbox_search_name = {"AutomationId": "textbox_search_name"}
        self.firstrow_parent = {"AutomationId":"examHistoryData"}
        self.firstrow = {"ClassName": "DataGridRow", "foundIndex": 1}
        self.patientname = {"ClassName": "DataGridCell", "foundIndex": 2}

class SurgicalSimulationPageUI(object):
    def __init__(self):
        self.page = {"ControlTypeName": "WindowControl", "searchDepth": 1, "AutomationId": "myMainWindow",
                     "RegexName": "PatientManager"}
        self.bar_window = {"AutomationId":"myMainWindow", "Name":"MetroProBarWindow", "searchDepth":1}
        self.surgical_WBWL  = {"AutomationId":"surgical_WBWL"}
        self.WL = {"ControlTypeName": "EditControl","AutomationId": "WL"}
        self.WB = {"ControlTypeName": "EditControl","AutomationId": "WB"}
        self.CTPreset = {"ControlTypeName":"ComboBoxControl","AutomationId": "wwwl_preset"}
        self.wOn = {"ControlTypeName": "ButtonControl","searchDepth":5,"Name":"w_ON"}
        self.wOff = {"ControlTypeName": "ButtonControl", "searchDepth": 5, "Name":"w_Off"}
        self.wdefault = {"AutomationId":"w_Default"}
        self.wOK = {"AutomationId":"w_OK"}
        self.ImageControl2D = {"Name":"ImageControl2D","searchDepth": 5}
        self.ImageControl3D = {"Name":"ImageControl3DMPR1_3","searchDepth": 5}
        self.CTPresetListControl = {"ControlTypeName":"ListItemControl","searchDepth": 6 }
