import os, sys, time
import subprocess
import uiautomation as automation

def testNotepadCN():

    automation.Logger.WriteLine('\nI will open Notepad and automate it. Please wait for a while.')
    time.sleep(2)
    automation.ShowDesktop()
    #打开notepad
    subprocess.Popen('notepad')
    #查找notepad， 如果name有中文，python2中要使用Unicode
    window = automation.WindowControl(searchDepth = 1, ClassName = 'Notepad', RegexName = u'.* - 记事本')
    #可以判断window是否存在，如果不判断，找不到window的话会抛出异常
    #if window.Exists(maxSearchSeconds = 3):
    if automation.WaitForExist(window, 3):
        automation.Logger.WriteLine("Notepad exists now")
    else:
        automation.Logger.WriteLine("Notepad does not exist after 3 seconds", automation.ConsoleColor.Yellow)
    screenWidth, screenHeight = automation.Win32API.GetScreenSize()
    window.MoveWindow(screenWidth // 4, screenHeight // 4, screenWidth // 2, screenHeight // 2)
    window.SetActive()
    #从window查找edit
    edit = window.EditControl()
    edit.Click(waitTime = 0)
    #python2中要使用Unicode, 模拟按键
    edit.SetValue(u'hi你好')
    edit.SendKeys(u'{Ctrl}{End}{Enter}下面开始演示{! 4}{ENTER}', 0.2, 0)
    edit.SendKeys('{Enter 3}0123456789{Enter}', waitTime = 0)
    edit.SendKeys('ABCDEFGHIJKLMNOPQRSTUVWXYZ{ENTER}', waitTime = 0)
    edit.SendKeys('abcdefghijklmnopqrstuvwxyz{ENTER}', waitTime = 0)
    edit.SendKeys('`~!@#$%^&*()-_=+{ENTER}', waitTime = 0)
    edit.SendKeys('[]{{}{}}\\|;:\'\",<.>/?{ENTER}', waitTime = 0)
    edit.SendKeys(u'™®①②③④⑤⑥⑦⑧⑨⑩§№☆★○●◎◇◆□℃‰€■△▲※→←↑↓〓¤°＃＆＠＼＾＿―♂♀{ENTER}{CTRL}a')
    window.CaptureToImage('Notepad.png')
    edit.SendKeys('Image Notepad.png was captured, you will see it later.', 0.05)
    #查找菜单
    window.MenuItemControl(Name = u'格式(O)').Click()
    window.MenuItemControl(Name = u'字体(F)...').Click()
    windowFont = window.WindowControl(Name = u'字体')
    windowFont.ComboBoxControl(AutomationId = '1140').Select(u'中文 GB2312')
    windowFont.ButtonControl(Name = u'确定').Click()
    window.Close()
    if automation.WaitForDisappear(window, 3):
        automation.Logger.WriteLine("Notepad closed")
    else:
        automation.Logger.WriteLine("Notepad still exists after 3 seconds", automation.ConsoleColor.Yellow)

    # buttonNotSave = ButtonControl(searchFromControl = window, SubName = u'不保存')
    # buttonNotSave.Click()
    # or send alt+n to not save and quit
    # automation.SendKeys('{Alt}n')
    # 使用另一种查找方法
    buttonNotSave = automation.FindControl(window,
        lambda control, depth: control.ControlType == automation.ControlType.ButtonControl and u'不保存' in control.Name)
    buttonNotSave.Click()
    subprocess.Popen('Notepad.png', shell = True)
    time.sleep(2)
    # consoleWindow.SetActive()
    automation.Logger.WriteLine('script exits', automation.ConsoleColor.Cyan)
    time.sleep(2)
testNotepadCN()