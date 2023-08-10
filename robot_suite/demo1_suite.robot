*** Settings ***
Library     DateTime


*** Test Cases ***
TC1
    [Tags]  smoke
    Log To Console      Balaji Dinakaran

TC2
    Log To Console    Balaji

TC3
    ${session_name}     Set Variable    robot session
    Log To Console    ${session_name}

TC4
    ${radius}   Set Variable    10.2
    ${result}   Evaluate    3.14*${radius}*${radius}  
    Log To Console    ${result}

TC5
    ${current_date}     Get Current Date
    Log To Console    ${current_date}