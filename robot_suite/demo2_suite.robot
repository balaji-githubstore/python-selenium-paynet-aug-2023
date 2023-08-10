*** Settings ***
Library     OperatingSystem

*** Test Cases ***
TC1
    Create Directory    path=C:\\Mine\\Demo\\new_session
    Directory Should Exist    path=C:\\Mine\\Demo\\new_session
    Remove Directory    path=C:\\Mine\\Demo\\new_session
    Directory Should Not Exist    path=C:\\Mine\\Demo\\new_session
    