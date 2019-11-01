from pywinauto import Application

app=Application().start("notepad.exe")
app.Notepad.menu_select(u'帮助->关于记事本')
about_dlg = app.window(title_re = "关于", class_name = "#32770")
# print(type(about_dlg))
# about_dlg.print_control_identifiers()
ok_button=about_dlg.window(title_re="hisense")
ok_button.print_control_identifiers()
print(type(ok_button))
ok_button.click()
