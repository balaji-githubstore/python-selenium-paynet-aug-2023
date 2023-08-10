*** Settings ***
Documentation   Explanation for test template concept in robot framework
...  which is data driven activity
Resource    ../resource/common_functionality.resource

Test Setup      Launch Browser And Navigate To Url
Test Teardown   Close Browser

Test Template   Valid Login Template

*** Test Cases ***
TC1
    [Tags]      smoke
    accountant      accountant      OpenEMR
TC2
    physician       physician       OpenEMR

#TC3
#    [Template]      None
#    [Setup]     None
#    Log To Console    balaji
#    [Teardown]  None

*** Keywords ***
Valid Login Template
    [Arguments]     ${username}     ${password}     ${expected_title}
    Input Text    id=authUser    ${username}
    Input Password    id=clearPass    ${password}
    Click Element    id=login-button
    Title Should Be    ${expected_title}
