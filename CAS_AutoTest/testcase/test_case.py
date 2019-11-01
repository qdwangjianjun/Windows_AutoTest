import pytest
from page.app import App
from page.loginpage import LoginPage
from page.patientpage import PatientPage
from page.surgicalsimulationpage import SurgicalSimulationPage

class Test_CAS(object):
    @classmethod
    def setup_class(cls):
        App.start()

    def test_login(self):
        loginpage = LoginPage()
        loginpage.active_page().login()

    def test_patient(self):
        patientpage = PatientPage()
        dict= patientpage.active_page().search_patient_name("LIU KAI MING").find_patient("LIU KAI MING",2).search_all().get_allpatients()
        print(dict)
        assert "LIU KAI MING" in  dict.values()

    def test_SurSim_SetWLWB(self):
        surgicalsimulationpage = SurgicalSimulationPage()
        surgicalsimulationpage.active_page().AutoSetWLWB()
        expected_result = [('-400', '1500'), ('300', '1500'), ('60', '400'), ('300', '600'), ('40', '80'), ('40', '400')]


    @classmethod
    def teardown_class(cls):
        pass