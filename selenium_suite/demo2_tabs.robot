*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
TC1
    Open Browser        browser=chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    20s
    Go To    url=https://www.online.citibank.co.in/
    #close all popup
    Click Element    xpath=//a[@class='newclose']
    Click Element    xpath=//a[@class='newclose2']
    #click on login
    Click Element    xpath=//span[text()='Login']
    Switch Window   Citibank India
    #click on forgot userid
    Click Element    xpath=//div[contains(text(),'Forgot User')]
    Click Element    link=select your product type
    Click Element    partial link=Credit Card
    Execute Javascript   document.querySelector('#bill-date-long').value='20/12/2000'
    Sleep    5s
    Close Browser


