from data.ui import PatientPageUI
from page.basepage import BasePage
import uiautomation as auto

class PatientPage(BasePage,PatientPageUI):

    def active_page(self):
        page = self.find(**self.page)
        page.SetActive()
        return self

    def search_patient_name(self,name):
        textbox_search_name = self.find(**self.textbox_search_name)
        textbox_search_name.SendKeys("{Ctrl}a{Del}")
        textbox_search_name.SendKeys(name)
        textbox_search_name.SendKeys("{ENTER}")
        return self

    def search_all(self):
        textbox_search_name = self.find(**self.textbox_search_name)
        textbox_search_name.SendKeys("{Ctrl}a{Del}")
        textbox_search_name.SendKeys("{ENTER}")
        return self

    def find_patient(self,name,index):
        textbox_search_name = self.find(**self.textbox_search_name)
        textbox_search_name.SendKeys("{Ctrl}a{Del}")
        textbox_search_name.SendKeys(name)
        textbox_search_name.SendKeys("{ENTER}")
        patient = self.find(ClassName="DataGridCell",Name=name,foundIndex=index)
        patient.Click()
        textbox_search_name.SendKeys("{Ctrl}a{Del}")
        return self

    def get_allpatients(self):
        self.scroll_top()
        patientsdict = {}
        firstrow_parent = self.find(**self.firstrow_parent)
        firstrow = self.find(searchFromControl=firstrow_parent,**self.firstrow)
        firstrow.Click()
        index = 1
        patientsdict["index" + str(index)] = self.find(searchFromControl = firstrow,**self.patientname).Name
        nextrow = firstrow.GetNextSiblingControl()
        while nextrow:
            auto.SendKeys("{DOWN}")
            index += 1
            patientname = self.find(searchFromControl = nextrow,**self.patientname).Name
            patientsdict["index" + str(index)] = patientname
            nextrow = nextrow.GetNextSiblingControl()
        auto.WheelUp(100)
        return patientsdict

    def scroll_top(self):
        auto.WheelUp(100)
        return self

    def scroll_Bottom(self):
        auto.WheelDown(100)
        return self



