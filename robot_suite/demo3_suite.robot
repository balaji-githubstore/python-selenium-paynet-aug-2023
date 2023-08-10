*** Settings ***
Library    Collections
*** Variables ***
${BROWSER_NAME}     chrome
@{COLORS}   red     green   yellow    blue
&{MOBILE_CAP}      platformName=android     deviceName=redmi    browserName=chrome

*** Test Cases ***
TC1
    Log To Console    ${BROWSER_NAME}

TC2
    Log To Console    ${BROWSER_NAME}
    Log To Console    ${COLORS}
    Log To Console    ${COLORS}[0]
    
    Log To Console    ${MOBILE_CAP}
    Log To Console    ${MOBILE_CAP}[deviceName]

TC3
    @{fruits}      Create List     mango   pineapple   orange
    #append apple to the list
    Append To List  ${fruits}   apple   

    #remove orange from the list
    Remove Values From List    ${fruits}    orange
    #insert grapes at index 1
    Insert Into List    ${fruits}    1    grapes

     Log To Console    ${fruits}
     Log    ${fruits}
     Remove From List    ${fruits}    0
     Log    ${fruits}

