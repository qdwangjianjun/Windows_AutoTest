from data.ui import LoginPageUI
from page.basepage import BasePage
from page.patientpage import PatientPage


class LoginPage(BasePage,LoginPageUI):

    def active_page(self):
        page = self.find(**self.page)
        page.SetActive()
        return self

    def login(self,uname="CAS",pswd="HISENSE"):
        username = self.find(**self.username)
        username.SendKeys("{Ctrl}a{Del}")
        username.SendKeys(uname)
        userpwd = self.find(**self.userpwd)
        userpwd.SendKeys("{Ctrl}a{Del}")
        userpwd.SendKeys(pswd)
        login = self.find(**self.loginbtn)
        login.Click()
        return PatientPage
