*** Settings ***
Resource    ../resource/common_functionality.resource

Test Setup      Launch Browser And Navigate To Url
Test Teardown   Close Browser

*** Test Cases ***
Valid Login Test
    Input Text    id=authUser    admin
    Input Password    id=clearPass    pass
    Click Element    id=login-button
    Title Should Be    OpenEMR

Invalid Login Test
    Input Text    id=authUser    admin22
    Input Password    id=clearPass    pass33
    Click Element    id=login-button
    Element Text Should Be    xpath=//p[contains(text(),'Invalid')]    Invalid username or password




