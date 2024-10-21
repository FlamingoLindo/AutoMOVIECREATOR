*** Settings ***
Library    SeleniumLibrary
Resource   ../../keywords/School/keywords.robot

*** Test Cases ***
Create Course
    Open Browser To Login Page
    Type In Email    ${email}
    Type In Password    ${password}
    Click Login Button
    Dashboard Should Be Visible
    
    Open Courses Page
    Add new course
    Fill General Info
    Add Module
    Add Video Class
    

    [Teardown]    Close Browser
