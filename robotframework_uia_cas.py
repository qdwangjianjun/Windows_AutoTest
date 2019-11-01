import uiautomation as automation

cas = automation.WindowControl(searchDepth=1, AutomationId='myMainWindow', Name='Login')
print(type(cas))
id = cas.AutomationId
print(id)
cas = str(cas)

print(cas)
print(type(cas))
cas = automation.Control()
print(type(cas))
print(cas)
login=cas.ButtonControl(AutomationId ="btn_login")
login.click()

print("test")
print ("test2")
print("456")
