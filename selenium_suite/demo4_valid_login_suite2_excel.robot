*** Settings ***
Documentation   Explanation for test template concept in robot framework
...  which is data driven activity
Resource    ../resource/common_functionality.resource

Test Setup      Launch Browser And Navigate To Url
Test Teardown   Close Browser

Test Template   Valid Login Template

Library     DataDriver        file=../test_data/open_emr_data.xlsx      sheet_name=test_valid_login

*** Test Cases ***
Valid Login Test_${testcase_name}

*** Keywords ***
Valid Login Template
    [Arguments]     ${username}     ${password}     ${expected_title}
    Input Text    id=authUser    ${username}
    Input Password    id=clearPass    ${password}
    Click Element    id=login-button
    Title Should Be    ${expected_title}
