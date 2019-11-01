*** Settings ***
Documentation    Example using the space separated plain text format.
Library          WinAuto


*** Test Cases ***
My Test
        runapp        args=D:\\release4003\\cas-lv.exe        cwd=D:\\release4003
        ${cas}     windowcontrol    searchDepth=1           AutomationId=myMainWindow       Name=Login

        windowcontrolsetactive         ${cas}

        ${casid}     controlexists          ${cas}       searchIntervalSeconds=2

        log       ${casid}