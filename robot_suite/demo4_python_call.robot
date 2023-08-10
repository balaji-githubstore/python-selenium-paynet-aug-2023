*** Settings ***
Library     ../math_article/Area.py
Library     SeleniumLibrary

*** Test Cases ***
TC1
#    SeleniumLibrary.Open Browser
    ${res}      Area Of Circle    10
    Should Be Equal As Numbers    ${res}    314