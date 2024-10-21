*** Settings ***
Library    SeleniumLibrary
Resource   ../../keywords/School/keywords.robot
Resource   ../../resources/School/variables.robot

*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Type In Email    ${email}
    Type In Password    ${password}
    Click Login Button
    Dashboard Should Be Visible
    [Teardown]    Close Browser
