*** Settings ***
Library    SeleniumLibrary
Library    XML
Resource   ../../keywords/School/keywords.robot
Resource   ../../resources/School/variables.robot

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${login_url}    ${browser}

Type In Email
    [Arguments]    ${email}
    Input Text    xpath=//*[@id="__next"]/main/div/main/form/div[2]/div[1]/label/input    ${email}

Type In Password
    [Arguments]    ${password}
    Input Text    xpath=//*[@id="__next"]/main/div/main/form/div[2]/div[2]/label/input    ${password}

Click Login Button
    Click Element    xpath=//*[@id="__next"]/main/div/main/form/div[2]/button

Dashboard Should Be Visible
    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/div[3]/div[1]
    Element Should Be Visible    xpath=//*[@id="__next"]/main/div[2]/div[3]/div[1]

# Course creation
Open Courses Page
    Click Element    xpath=/html/body/div[1]/main/div[1]/div[2]/ul/li[2]/a
    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/div[2]
    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/div[3]/section/div[2]/div/a  
Add New Course
    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/div[3]/section/div[2]/div/a  
    Click Element    xpath=//*[@id="__next"]/main/div[2]/div[3]/section/div[2]/div/a
    
Fill General Info
    Wait Until Element Is Visible    xpath=//*[@id="mainForm"]/div/h2

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[1]/div/label/div/input    Course made using robotframework

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[1]/label/div/label/textarea    Description

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[2]/div/label/div/input    robot
    Click Button    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[2]/div/label/div/div/button
    
    Clear Element Text    xpath=//*[@id="mainForm"]/div/div/div/label/div/input
    Input Text    xpath=//*[@id="mainForm"]/div/div/div/label/div/input    10

    Click Element    xpath=//*[@id="mainForm"]/div/label[2]/div/div
    Click Element    xpath=//*[@id="react-select-2-option-0"]

    Choose File    xpath=//*[@id="mainForm"]/div/label[1]/input    C:\\Users\\josef\\Desktop\\AutoMOVIECREATOR\\selenium_file\\movie.png
    
    Click Button    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[3]/button

Add Module
    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/h2

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[1]/div/label/div/input    Module 1
    Click Button    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[1]/button

    Click Element    xpath=//*[@id="react-select-3-placeholder"]
    Element Should Be Enabled    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[2]/label[1]/div/div
    Click Element    xpath=//*[@id="react-select-3-option-0"]

    Click Button    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/form/button

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/header/button

Add Video Class
    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/header/button

    Click Element    xpath=//*[@id="__next"]/main/div[2]/a

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/header/div[2]/strong

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input    Robot Video Class

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea    Robot Video Description

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[1]

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/input    https://www.youtube.com/watch?v=DjhpZhWmPZ8&ab_channel=MemeCollege
    Click Element    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/div/button[2]

    Scroll Element Into View    xpath=//*[@id="__next"]/main/div[2]/header/button
    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/header/button
    Click Element    xpath=//*[@id="__next"]/main/div[2]/header/button

    Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div/button
    Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/button
    

    
    
