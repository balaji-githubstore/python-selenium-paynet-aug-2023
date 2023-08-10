*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
TC1 Login
    [Tags]     smoke
    Open Browser    url=https://www.facebook.com/   browser=chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    20s
    Input Text    id=email    john12345@gmail.com
    Input Password    id=pass    wleocme123
    Click Element    name=login

TC2 FB Sign Up
    Open Browser        browser=chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    20s
    Go To    url=https://www.facebook.com/
    Click Element    link=Create new account
    Input Text    name=firstname    john
    Select From List By Label    id=day     20
    Select From List By Label    id=month   Dec
    Select From List By Label    id=year    2000
    Click Element    xpath=//input[@value='-1']
