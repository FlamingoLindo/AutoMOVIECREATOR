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
    Fill General Info    Course made using robotframework    Description    robot    10    ${image_path}
    Add Module    Module 1
    Add Video Class    Robot Video Class    Robot Video Description    ${video_link}    10
    Add Text Class    Robot Text Class    Robot Text Description    ROBOT TEXT    10 
    Add Image Class    Robot Image Class    Robot Image Description    ${image_path}    10
    Add Audio Class    Robot Audio Class    Robot Audio Description    ${audio_path}    10
    Add File Class    Robot File Class    Robot File Description    ${audio_path}    10
    # Add Code Class
    Add Chooice Class    Robot Chooice Class    Robot Chooice Description    Robot Chooices    Right    Wrong    10
    Add Dissertative Class    Robot Dissertative Class    Robot Dissertative Description    ROBOT DISSERTATIVE TEXT    10
    Add Essay Class    Robot Essay Class    Robot Essay Description    ROBOT ESSAY TEXT    10
    Finish Class Creation
    Open First Course
    Test Creation    Robot Test    15    Robot Test Chooices    Right    Wrong
    Approve course
    

    [Teardown]    Close Browser
