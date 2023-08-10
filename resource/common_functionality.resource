*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${BROWSER_NAME}     chrome
${URL}      https://demo.openemr.io/b/openemr

*** Keywords ***
Launch Browser And Navigate To Url
    Open Browser    browser=${BROWSER_NAME}
    Maximize Browser Window
    Set Selenium Implicit Wait    20s
    Go To    url=${URL}

#Launch Given Browser And Navigate To Url
#    [Arguments]     ${browser_name}
#    Open Browser    browser=${browser_name}
#    Maximize Browser Window
#    Set Selenium Implicit Wait    20s
#    Go To    url=${URL}