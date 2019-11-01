import subprocess
import time
from data.setting import Setting
import psutil
from page.loginpage import LoginPage
import uiautomation as auto

class App(Setting):
    @classmethod
    def cas_process(cls):
        appname = Setting.appname
        pids = psutil.pids()
        for pid in pids:
            processname = str(psutil.Process(pid).name()).upper()
            appname = str(appname).upper()
            if appname in processname:
                return pid
        else:
            return None

    @classmethod
    def start(cls):
        exepath = Setting.exepath
        work_dir = Setting.work_dir
        caspid = App.cas_process()
        if not caspid:
            subprocess.Popen(args = exepath ,cwd = work_dir)
            time.sleep(30)
            return LoginPage

    @classmethod
    def close(cls):
        btn_close =  auto.Control(AutomationId ="btn_close")
        btn_close.Click()





