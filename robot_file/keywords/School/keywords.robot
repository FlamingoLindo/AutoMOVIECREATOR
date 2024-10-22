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
    [Arguments]    ${course_name}    ${description}    ${tag}    ${time}    ${image_path}

    Wait Until Element Is Visible    xpath=//*[@id="mainForm"]/div/h2

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[1]/div/label/div/input    ${course_name}

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[1]/label/div/label/textarea    ${description}

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[2]/div/label/div/input    ${tag}
    Click Button    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[2]/div/label/div/div/button
    
    Clear Element Text    xpath=//*[@id="mainForm"]/div/div/div/label/div/input
    Input Text    xpath=//*[@id="mainForm"]/div/div/div/label/div/input    ${time}

    Click Element    xpath=//*[@id="mainForm"]/div/label[2]/div/div
    Click Element    xpath=//*[@id="react-select-2-option-0"]

    Choose File    xpath=//*[@id="mainForm"]/div/label[1]/input    ${image_path}
    
    Click Button    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[3]/button

Add Module
    [Arguments]    ${module}

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/h2

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[1]/div/label/div/input    ${module}
    Click Button    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[1]/button

    Click Element    xpath=//*[@id="react-select-3-placeholder"]
    Element Should Be Enabled    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[2]/label[1]/div/div
    Wait Until Element Is Visible    xpath=//*[@id="react-select-3-option-0"]
    Click Element    xpath=//*[@id="react-select-3-option-0"]

    Click Button    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[2]/form/button

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/header/button

Add Video Class
    [Arguments]    ${video_name}    ${video_description}    ${video_link}    ${class_points}    

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/header/button

    Click Element    xpath=//*[@id="__next"]/main/div[2]/a

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/header/div[2]/strong

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input    ${video_name}

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea    ${video_description}

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[1]

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/input    ${video_link}
    Click Element    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/div/button[2]

    Clear Element Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input
    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input    ${class_points}

    # You will have to zoom out at the beging of the test, for some reason the scroll to function is not working...
    Scroll Element Into View    xpath=/html/body/div[1]/main/div[2]/header/button
    Wait Until Element Is Visible    xpath=/html/body/div[1]/main/div[2]/header/button
    Click Element    xpath=/html/body/div[1]/main/div[2]/header/button
    
    Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Element Should Be Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/button

Add Text Class
    [Arguments]    ${text_name}    ${text_desc}    ${text_text}    ${class_points}

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/header/button

    Click Element    xpath=//*[@id="__next"]/main/div[2]/a

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/header/div[2]/strong

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input    ${text_name}

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea    ${text_desc}

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[2]

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/label/textarea    ${text_text}
    
    Clear Element Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input
    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input    ${class_points}

    # You will have to zoom out at the beging of the test, for some reason the scroll to function is not working...
    Scroll Element Into View    xpath=/html/body/div[1]/main/div[2]/header/button
    Wait Until Element Is Visible    xpath=/html/body/div[1]/main/div[2]/header/button
    Click Element    xpath=/html/body/div[1]/main/div[2]/header/button
    
    Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Element Should Be Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/button

Add Image Class
    [Arguments]    ${img_name}    ${img_desc}    ${image_path}    ${class_points}

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/header/button

    Click Element    xpath=//*[@id="__next"]/main/div[2]/a

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/header/div[2]/strong

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input    ${img_name}

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea    ${img_desc}

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[3]

    Choose File    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/label/input    ${image_path}
    
    Clear Element Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input
    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input    ${class_points}

    # You will have to zoom out at the beging of the test, for some reason the scroll to function is not working...
    Scroll Element Into View    xpath=/html/body/div[1]/main/div[2]/header/button
    Wait Until Element Is Visible    xpath=/html/body/div[1]/main/div[2]/header/button
    Click Element    xpath=/html/body/div[1]/main/div[2]/header/button
    
    Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Element Should Be Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/button

Add Audio Class
    [Arguments]    ${aud_name}    ${aud_desc}    ${audio_path}    ${class_points}

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/header/button

    Click Element    xpath=//*[@id="__next"]/main/div[2]/a

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/header/div[2]/strong

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input    ${aud_name}

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea    ${aud_desc}

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[4]

    Choose File    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/label/input    ${audio_path}
    
    Clear Element Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input
    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input    ${class_points}

    # You will have to zoom out at the beging of the test, for some reason the scroll to function is not working...
    Scroll Element Into View    xpath=/html/body/div[1]/main/div[2]/header/button
    Wait Until Element Is Visible    xpath=/html/body/div[1]/main/div[2]/header/button
    Click Element    xpath=/html/body/div[1]/main/div[2]/header/button
    
    Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Element Should Be Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/button

Add File Class
    [Arguments]    ${file_name}    ${file_desc}    ${audio_path}    ${class_points}

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/header/button

    Click Element    xpath=//*[@id="__next"]/main/div[2]/a

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/header/div[2]/strong

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input    ${file_name}

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea    ${file_desc}

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[5]

    Choose File    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/label/input    ${audio_path}
    
    Clear Element Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input
    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input    ${class_points}

    # You will have to zoom out at the beging of the test, for some reason the scroll to function is not working...
    Scroll Element Into View    xpath=/html/body/div[1]/main/div[2]/header/button
    Wait Until Element Is Visible    xpath=/html/body/div[1]/main/div[2]/header/button
    Click Element    xpath=/html/body/div[1]/main/div[2]/header/button
    
    Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Element Should Be Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/button

Add Code Class
    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/header/button

    Click Element    xpath=//*[@id="__next"]/main/div[2]/a

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/header/div[2]/strong

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input    Robot Code Class

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea    Robot Code Description

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[6]

    Input Text    xpath=//*[@id="ace-editor"]/div[2]/div    CODE TEST
    
    Clear Element Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input
    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input    10

    # You will have to zoom out at the beging of the test, for some reason the scroll to function is not working...
    Scroll Element Into View    xpath=/html/body/div[1]/main/div[2]/header/button
    Wait Until Element Is Visible    xpath=/html/body/div[1]/main/div[2]/header/button
    Click Element    xpath=/html/body/div[1]/main/div[2]/header/button
    
    Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Element Should Be Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/button

Add Chooice Class
    [Arguments]    ${ch_name}    ${ch_desc}    ${ch_ch}    ${ch_right}    ${ch_wrong}    ${class_points}

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/header/button

    Click Element    xpath=//*[@id="__next"]/main/div[2]/a

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/header/div[2]/strong

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input    ${ch_name}

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea    ${ch_desc}

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[7]

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[1]/label/div/input    ${ch_ch}

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/button
    Click Element    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/button

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/ul/li[1]/input

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/ul/li[1]/input    ${ch_right}
    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/ul/li[2]/input    ${ch_wrong}

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/ul/li[1]/div[2]/label[1]


    Clear Element Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input
    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input    ${class_points}

    # You will have to zoom out at the beging of the test, for some reason the scroll to function is not working...
    Scroll Element Into View    xpath=/html/body/div[1]/main/div[2]/header/button
    Wait Until Element Is Visible    xpath=/html/body/div[1]/main/div[2]/header/button
    Click Element    xpath=/html/body/div[1]/main/div[2]/header/button
    
    Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Element Should Be Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/button

Add Dissertative Class
    [Arguments]    ${ar_name}    ${ar_desc}    ${ar_ar}    ${class_points}

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/header/button

    Click Element    xpath=//*[@id="__next"]/main/div[2]/a

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/header/div[2]/strong

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input    ${ar_name}

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea    ${ar_desc}

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[8]

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/label/textarea    ${ar_ar}
    
    Clear Element Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input
    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input    ${class_points}

    # You will have to zoom out at the beging of the test, for some reason the scroll to function is not working...
    Scroll Element Into View    xpath=/html/body/div[1]/main/div[2]/header/button
    Wait Until Element Is Visible    xpath=/html/body/div[1]/main/div[2]/header/button
    Click Element    xpath=/html/body/div[1]/main/div[2]/header/button
    
    Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Element Should Be Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/button

Add Essay Class
    [Arguments]    ${es_name}    ${es_desc}    ${es_es}    ${class_points}

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/header/button

    Click Element    xpath=//*[@id="__next"]/main/div[2]/a

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/header/div[2]/strong

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input    ${es_name}

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea    ${es_desc}

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[9]

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[1]/label/div/input    ${es_es}
    
    Clear Element Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input
    Input Text    xpath=//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input    ${class_points}

    # You will have to zoom out at the beging of the test, for some reason the scroll to function is not working...
    Scroll Element Into View    xpath=/html/body/div[1]/main/div[2]/header/button
    Wait Until Element Is Visible    xpath=/html/body/div[1]/main/div[2]/header/button
    Click Element    xpath=/html/body/div[1]/main/div[2]/header/button
    
    Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Element Should Be Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/button

Finish Class Creation

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/header/button
    Click Element    xpath=//*[@id="__next"]/main/header/button

    Sleep    7s
    Element Should Be Visible    xpath=//*[@id="__next"]/main/div[2]/div[3]/button
    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/div[3]/button


Open First Course

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div[3]/section/div[1]/table/tbody/tr[1]/td[8]/div/a

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/div[3]/a

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div[3]/a

Test Creation
    [Arguments]    ${test_name}    ${test_points}    ${test_test}    ${test_right}    ${test_wrong}

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div[2]/div[1]/nav/a[3]

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/section/div[2]/div/table/thead/tr/th[1]

    Click Element    xpath=//*[@id="__next"]/main/div[2]/section/div[2]/div/a/div/div

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/div[1]/div[1]/button

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div[1]/div[2]/label/div/input    ${test_name}

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div[1]/label/div/div[1]

    Wait Until Element Is Visible    xpath=//*[@id="react-select-13-option-0"]
    Click Element    xpath=//*[@id="react-select-13-option-0"]

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div[1]/div[3]/div/label[1]

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div[4]/button[7]/div

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div[2]/div/input    ${test_points}

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[1]/label/div/input    ${test_test}

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/button
    Click Element    xpath=//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/button

    Input Text    xpath=//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[2]/ul/li[1]/input    ${test_right}
    Input Text    xpath=//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[2]/ul/li[2]/input    ${test_wrong}

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[2]/ul/li[1]/div[2]/label[1]

    Scroll Element Into View    xpath=//*[@id="__next"]/main/header/button
    Click Element    xpath=//*[@id="__next"]/main/header/button

    Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div

    Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/div/button[2]

    Sleep    5s

    Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div/button
    Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/button

    Sleep    6s
    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/section/div[2]/div/table/thead/tr/th[1]

Approve course

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/section/div[2]/div/table/thead/tr/th[1]

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div[2]/div/nav/a[1]

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/div[1]/div[2]

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div[3]/a

    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/ul/div/ul/li[1]/div
    
    FOR    ${index}    IN RANGE    8
        Sleep    2s
        Click Element    xpath=//*[@id="__next"]/main/div[2]/ul/div/ul/li[1]/div/div/div/button[1]
        Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
        Sleep    1s
        Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/div/button[2]
        Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
        Sleep    1s
        Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/button
    END

    Sleep    1s    
    Click Element    xpath=//*[@id="__next"]/main/div[2]/nav/a[2]

    Click Element    xpath=//*[@id="__next"]/main/div[2]/ul/div/ul/li/div/div/div/button[1]
    Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/div/button[2]
    Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Sleep    2s
    Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/button

    Sleep    1s
    Click Element    xpath=//*[@id="__next"]/main/div[1]/div[2]/ul/li[2]
    Sleep    5s

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div[2]/a[2]
    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/div[3]/div[2]/div[1]
    Click Element    xpath=//*[@id="__next"]/main/div[2]/div[3]/div[2]/div[11]/div/button[1]

    Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div    
    Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/div[2]/button[2]
    Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Sleep    1s
    Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/button

    Sleep    1s
    Click Element    xpath=//*[@id="__next"]/main/div[1]/div[2]/ul/li[2]
    
    Wait Until Element Is Visible    xpath=//*[@id="__next"]/main/div[2]/div[3]/section/div[1]/table/thead/tr/th[1]

    Click Element    xpath=//*[@id="__next"]/main/div[2]/div[3]/section/div[1]/table/tbody/tr[1]/td[8]/div/button[1]
    Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/form/div
    Click Element    xpath=//*[@id="modal-root"]/div[2]/div/form/div/button

    Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/div/button[2]

    Wait Until Element Is Visible    xpath=//*[@id="modal-root"]/div[2]/div/div
    Sleep    1s
    Click Element    xpath=//*[@id="modal-root"]/div[2]/div/div/button
