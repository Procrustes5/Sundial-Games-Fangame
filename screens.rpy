﻿################################################################################
## 초기화
################################################################################

init offset = -1


################################################################################
## 스타일
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 게임내 스크린
################################################################################


## Say 스크린 #####################################################################
##
## Say 스크린은 플레이어에게 대사를 출력할 때 씁니다. 화자 who와 대사 what, 두
## 개의 매개변수를 받습니다. (화자 이름이 없으면 who는 None일 수 있음)
##
## 이 스크린은 id "what"을 가진 텍스트 디스플레이어블을 생성해야 합니다. (이 디
## 스플레이어블은 렌파이의 대사 출력에 필요합니다.) id "who" 와 id "window" 디스
## 플레이블이 존재할 경우 관련 스타일 속성이 적용됩니다.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        add SideImage() xpos 950 yalign 1.0
        if who is not None:

            window:
                id "namebox"
                style "namebox"
                if who != "ch_nar":
                    add "menu/name.png" xpos 420 ypos 0
                text who id "who" outlines [ (absolute(2), "#E484AA", absolute(0), absolute(0)) ] xpos 615 ypos 22

        text what id "what"


    ## 사이드 이미지가 있는 경우 글자 위에 표시합니다. 휴대폰 환경에서는 보이지
    ## 않습니다.


## Character 객체를 통해 스타일을 지정할 수 있도록 namebox를 사용할 수 있게 만듭
## 니다.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input 스크린 ###################################################################
##
## 플레이어 입력을 받는 renpy.input을 출력할 때 쓰이는 스크린입니다. prompt 매개
## 변수를 통해 입력 지문을 표시할 수 있습니다.
##
## 이 스크린은 id "input"을 가진 input 디스플레이어블을 생성해야 합니다.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice 스크린 ##################################################################
##
## menu 명령어로 생성된 게임내 선택지를 출력하는 스크린입니다. 한 개의 매개변수
## items를 받고, 이는 선택지 내용(caption)과 선택지 결과(action)이 있는 오브젝트
## 가 들어있는 리스트입니다.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

init:
    image center:
        im.FactorScale('choice/choice_0.png', 0.2)
    $ feel = "-"
    $ length_items = "-"
    screen icon:
        if length_items == "1":
            add (im.FactorScale('/choice/choice_%s.png' %feel, 0.2)) xalign 0.2 yalign 0.93
        elif length_items == "2":
            add (im.FactorScale('/choice/choice_%s1.png' %feel, 0.2)) xalign 0.2 yalign 0.93
        elif length_items == "3":
            add (im.FactorScale('/choice/choice_%s.png' %feel, 0.2)) xalign 0.2 yalign 0.93
        elif length_items == "4":
            add (im.FactorScale('/choice/choice_%s1.png' %feel, 0.2)) xalign 0.5 yalign 0.93
        else:
            add (im.FactorScale('/choice/choice_%s.png' %feel, 0.2)) xalign 0.5 yalign 0.93
    screen choice(items):
        
        if len(items) == 1:
            imagebutton idle 'center' hover 'center' action NullAction() xalign 0.2 yalign 0.93
            vbox:
                xalign 0.5 yalign 0.9
                for caption, action, chosen in items[3:]:
                    if action:
                        button:
                            action (action, Hide('icon'))
                            style "menu_choice_button"
                            text caption[:-8] size 30 color "#ffffff" outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ] hover_bold True hover_color '#FFD700' line_spacing 15 style "menu_choice"
                            hovered Show('icon', length_items = "1", feel="2")
                            unhovered Hide('icon')
                    
            
            vbox:
                xpos 420 yalign 0.86
                for caption, action, chosen in items[:3]:
                    if action:
    
                        button:
                            action (action, Hide('icon'))
                            style "menu_choice_button"
                            text caption[:-8] size 30 color "#ffffff" outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ] hover_color '#FFD700' line_spacing 15 style "menu_choice"
                            hovered Show('icon', length_items = "1", feel="2")
                            unhovered Hide('icon')
                            xminimum 100
        elif len(items) == 2:
            imagebutton idle 'center' hover 'center' action NullAction() xalign 0.2 yalign 0.93
            vbox:
                xpos 60 yalign 0.9
                for caption, action, chosen in items[2:]:
                    if action:
                        button:
                            action (action, Hide('icon'))
                            style "menu_choice_button"
                            text caption[:-8] size 23 text_align 0.0 color "#ffffff" outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ] hover_color '#FFD700' line_spacing 25 style "menu_choice"
                            hovered Show('icon', length_items = "2", feel=caption[-1])
                            unhovered Hide('icon')
                    
            
            vbox:
                xpos 400 yalign 0.9
                for caption, action, chosen in items[:2]:
                    if action:
    
                        button:
                            action (action, Hide('icon'))
                            style "menu_choice_button"
                            text caption[:-8] size 25 text_align 0.0 color "#ffffff" outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ] hover_color '#FFD700' line_spacing 25 style "menu_choice"
                            hovered Show('icon', length_items = "2", feel=caption[-1])
                            unhovered Hide('icon')
                            xminimum 100    
        elif len(items) == 3:
            imagebutton idle 'center' hover 'center' action NullAction() xalign 0.2 yalign 0.93
            vbox:
                xpos 60 yalign 0.94
                for caption, action, chosen in items[3:]:
                    if action:
                        button:
                            action (action, Hide('icon'))
                            style "menu_choice_button"
                            text caption[:-8] size 23 text_align 0.0 color "#ffffff" outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ] hover_color '#FFD700' line_spacing 25 style "menu_choice"
                            hovered Show('icon', length_items = "3", feel=caption[-1])
                            unhovered Hide('icon')
                    
            
            vbox:
                xpos 400 yalign 0.94
                for caption, action, chosen in items[:3]:
                    if action:
    
                        button:
                            action (action, Hide('icon'))
                            style "menu_choice_button"
                            text caption[:-8] size 23 text_align 0.0 color "#ffffff" outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ] hover_color '#FFD700' line_spacing 25 style "menu_choice"
                            hovered Show('icon', length_items = "3", feel=caption[-1])
                            unhovered Hide('icon')
                            xminimum 100

        elif len(items) == 4:
            imagebutton idle 'center' hover 'center' action NullAction() xalign 0.5 yalign 0.93
            vbox:
                xpos 60 yalign 0.9
                for caption, action, chosen in items[2:]:
                    if action:
                        button:
                            action (action, Hide('icon'))
                            style "menu_choice_button"
                            text caption[:-8] size 23 text_align 0.0 color "#ffffff" outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ] hover_color '#FFD700' line_spacing 25 style "menu_choice"
                            hovered Show('icon', length_items = "4", feel=caption[-1])
                            unhovered Hide('icon')
                    
            
            vbox:
                xpos 720 yalign 0.9
                for caption, action, chosen in items[:2]:
                    if action:
    
                        button:
                            action (action, Hide('icon'))
                            style "menu_choice_button"
                            text caption[:-8] size 23 text_align 0.0 color "#ffffff" outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ] hover_color '#FFD700' line_spacing 25 style "menu_choice"
                            hovered Show('icon', length_items = "4", feel=caption[-1])
                            unhovered Hide('icon')
                            xminimum 100
        else:
            imagebutton idle 'center' hover 'center' action NullAction() xalign 0.5 yalign 0.93
            vbox:
                xpos 300 yalign 0.94
                for caption, action, chosen in items[3:]:
                    if action:
                        button:
                            action (action, Hide('icon'))
                            style "menu_choice_button"
                            text caption[:-8] size 23 text_align 0.0 color "#ffffff" outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ] hover_color '#FFD700' line_spacing 25 style "menu_choice"
                            hovered Show('icon', length_items = "6", feel=caption[-1])
                            unhovered Hide('icon')
                    
            
            vbox:
                xpos 720 yalign 0.94
                for caption, action, chosen in items[:3]:
                    if action:
    
                        button:
                            action (action, Hide('icon'))
                            style "menu_choice_button"
                            text caption[:-8] size 23 text_align 0.0 color "#ffffff" outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ] hover_color '#FFD700' line_spacing 25 style "menu_choice"
                            hovered Show('icon', length_items = "6", feel=caption[-1])
                            unhovered Hide('icon')
                            xminimum 100
define config.narrator_menu = True

## 돌아가는 설정 버튼 #######################
##
##
init:
    image rotating_icon:
        im.FactorScale("menu/setting_icon.png", 0.12)
        xpos -12 ypos -12
        rotate 0
        linear 2.5 rotate -360
        repeat

## Quick Menu 스크린 ##############################################################
##
## 퀵메뉴는 게임 외 메뉴 접근성을 높여주기 위해 게임 내에 표시됩니다.
init:
    image setting_icon:
        im.FactorScale('menu/setting_icon.png', 0.12)
screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100
    if quick_menu:

        hbox:
            style_prefix "quick"
            
            imagebutton:
                idle 'setting_icon' hover 'rotating_icon' action ShowMenu("preferences") xpos 1210 ypos 5
                



## 플레이어가 UI(스크린)을 일부러 숨기지 않는 한 퀵메뉴가 게임 내에 오버레이로
## 출력되게 합니다.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main과 Game Menu 스크린
################################################################################

## Navigation 스크린 ##############################################################
##
## 이 스크린은 메인메뉴와 게임외 메뉴에 포함되어 다른 메뉴로 이동하거나 게임을
## 시작/종료할 수 있게 합니다.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos 90
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("시작하기") action Start()

        else:

            textbutton _("대사록") action ShowMenu("history")

            textbutton _("저장하기") action ShowMenu("save")

        textbutton _("불러오기") action ShowMenu("load")

        textbutton _("환경설정") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("리플레이 끝내기") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("메인 메뉴") action MainMenu()

        textbutton _("갤러리") action ShowMenu("gallery")

        if persistent.clue == True:
            textbutton _("단서") action ShowMenu("clue")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## 도움말 메뉴는 모바일 디바이스와 맞지 않아 불필요합니다.
            textbutton _("조작방법") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("종료하기") action Quit(confirm=not main_menu)

init python:
    

 
    # 먼저 스크립트에서 '이제부터 CG 갤러리 설정 만들거임' 이란 증거로
    # 아래와 같이 써줍니다.
    g = Gallery()
 
    # 이 CG갤러리에서 "잠긴 CG 버튼"에 쓸 그림을 설정합니다.
    g.locked_button = 'images/gallery/transbutton.png'
 
    # 마우스를 버튼 위에 올렸을 때 이 버튼을 골랐다는 것을 알려줄
    # 그림을 지정합니다. 없으면 비워도 됩니다.
    ## g.hover_border = 'images/library/slot_hover_background.png'     
 
    # 이제 CG갤러리에서 쓸 CG버튼의 설정을 차례로 만들어줍시다.
    # 맨 처음에는 무조건 g.button('버튼이름') 을 적어줍시다.
    g.button('ninon1')
    g.unlock_image("cg_ninon_happy_04")
 
    g.button('ninon2')
    g.unlock_image("ninon_pingping")

    g.button('monica1')
    g.unlock_image("cg_monica_first_01")
    
    g.button("monica2")
    g.unlock_image("cg_monica_onsen_01")

    g.button("kuka1")
    g.unlock_image("cg_kuka_ykt_3")

    g.button("kuka2")
    g.unlock_image("cg_yukiend1")

    g.button("yuki1")
    g.unlock_image("cg_yuki_03_plus")
    
    g.button("yuki2")
    g.unlock_image("cg_monica_basic")

    g.button("1")
    g.unlock_image("cg_kuka_end19")

    g.button("2")
    g.unlock_image("cg_kyaru")

    g.button("3")
    g.unlock_image("cg_kokoro_01")

    g.button("4")
    g.unlock_image("cg_common")

    g.button("5")
    g.unlock_image("cg_yuki_onsen_01")

    g.button("6")
    g.unlock_image("cg_ninon_onsen_02")

    g.button("7")
    g.unlock_image("cg_kimura")

    g.button("8")
    g.unlock_image("cg_kuka_onsen_hand_01")

    g.transition = dissolve
    
 
    # 이제 위에서 설정한 것들이 눈에 보이도록 스크린 블럭에 추가해야 합니다.
init:
    image gal1:
        im.FactorScale("gallery/1.png", 1.05)
    image gal2:
        im.FactorScale("gallery/2.png", 1.05)
    image gal3:
        im.FactorScale("gallery/3.png", 1.05)
    image gal4:
        im.FactorScale("gallery/4.png", 1.05)
    image gal5:
        im.FactorScale("gallery/5.png", 1.05)
    image gal6:
        im.FactorScale("gallery/6.png", 1.05)
    image gal7:
        im.FactorScale("gallery/7.png", 1.05)
    image gal8:
        im.FactorScale("gallery/8.png", 1.05)
    image gal9:
        im.FactorScale("gallery/9.png", 1.05)
    image gal10:
        im.FactorScale("gallery/10.png", 1.05)
    image gal11:
        im.FactorScale("gallery/11.png", 1.05)
    image gal12:
        im.FactorScale("gallery/12.png", 1.05)
    image gal13:
        im.FactorScale("gallery/13.png", 1.05)
    image gal14:
        im.FactorScale("gallery/14.png", 1.05)
    image gal15:
        im.FactorScale("gallery/15.png", 1.05)
    image gal16:
        im.FactorScale("gallery/16.png", 1.05)
    screen gallery:
 
        # 갤러리 스크린이 세이브 메뉴나 환경설정 메뉴 화면에서 자연스레 교체되도록 tag menu를 추가합니다.
        tag menu
 
        # 배경화면은 add로 넣습니다.
        add "images/gallery/background.png"
 
        # 버튼 격자판. CG 버튼 정렬용입니다.
        
        add g.make_button("ninon1", "images/gallery/transbutton.png", xpos = 57, ypos = 45, idle_border = "images/gallery/1.png", hover_border = "gal1")
        add g.make_button("ninon2", "images/gallery/transbutton.png", xpos = 57, ypos = 200, idle_border = "images/gallery/2.png", hover_border = "gal2")
        add g.make_button("monica1", "images/gallery/transbutton.png", xpos = 57, ypos = 355, idle_border = "images/gallery/3.png", hover_border = "gal3")
        add g.make_button("monica2", "images/gallery/transbutton.png", xpos = 57, ypos = 515, idle_border = "images/gallery/4.png", hover_border = "gal4")
        add g.make_button("kuka1", "images/gallery/transbutton.png", xpos = 350, ypos = 45, idle_border = "images/gallery/5.png", hover_border = "gal5")
        add g.make_button("kuka2", "images/gallery/transbutton.png", xpos = 350, ypos = 200, idle_border = "images/gallery/6.png", hover_border = "gal6") 
        add g.make_button("yuki1", "images/gallery/transbutton.png", xpos = 350, ypos = 355, idle_border = "images/gallery/7.png", hover_border = "gal7")
        add g.make_button("yuki2", "images/gallery/transbutton.png", xpos = 350, ypos = 515, idle_border = "images/gallery/8.png", hover_border = "gal8")
        add g.make_button("1", "images/gallery/transbutton.png", xpos = 640, ypos = 45, idle_border = "images/gallery/9.png", hover_border = "gal9")
        add g.make_button("2", "images/gallery/transbutton.png", xpos = 640, ypos = 200, idle_border = "images/gallery/10.png", hover_border = "gal10")            
        add g.make_button("3", "images/gallery/transbutton.png", xpos = 640, ypos = 355, idle_border = "images/gallery/11.png", hover_border = "gal11")
        add g.make_button("4", "images/gallery/transbutton.png", xpos = 640, ypos = 515, idle_border = "images/gallery/12.png", hover_border = "gal12")
        add g.make_button("5", "images/gallery/transbutton.png", xpos = 940, ypos = 45, idle_border = "images/gallery/13.png", hover_border = "gal13")
        add g.make_button("6", "images/gallery/transbutton.png", xpos = 940, ypos = 200, idle_border = "images/gallery/14.png", hover_border = "gal14") 
        add g.make_button("7", "images/gallery/transbutton.png", xpos = 940, ypos = 355, idle_border = "images/gallery/15.png", hover_border = "gal15")
        add g.make_button("8", "images/gallery/transbutton.png", xpos = 940, ypos = 515, idle_border = "images/gallery/16.png", hover_border = "gal16")    
    
                # 이제 위에서 만들었던 g.button 들을 추가할 차례입니다.
                # 위에서처럼 g.button으로 설정한 버튼이 없다면 CG버튼은 만들 수 없습니다.
    
                # 스크린문에서는 add와 함께 g.make_button 을 이용해 CG버튼을 만듭니다.
                # add g.make_button("위에 g.button()에서 적었던 버튼 이름", "버튼 그릴 때 사용할 그림 파일 이름")
                # 을 적으면 됩니다.
                
            
                # 위에서 g.hover_border를 지정했는데
                # hover_border 는 g.make_button 에서도 정할 수 있습니다.
                # 전체에 적용할 때는 g.hover_border 에서, 개별로 적용할 때는 g.make_button에서 지정하면 됩니다.
                # add g.make_button("dawn mary", "gal-dawn_mary.png", hover_border = 'gal-border.png',  xalign=0.5, yalign=0.5)
    
                # CG수가 적으면 일일히 add g.make_button ... 적어도 되겠지만
                # g.make_button에 입력할 내용을 리스트에 넣어놓고 for문으로 만드는 것이 훨씬 편하겠지요.
    
            # 클릭하면 메인 메뉴로 돌아가는 버튼입니다.
            # CG 버튼 양이 많아서 여러 스크린을 만들었다면 다음 CG버튼을 보여주는 버튼을 만들어야겠죠.
        button:
            text '돌아가기' color "#ffffff" outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ] hover_color "#f578f3"
            action Return()
            xalign 0.5 yalign 1.0 

init:
    screen gallery_2:
        tag menu
 
        # 배경화면은 add로 넣습니다.
        add "images/bg/bg_white.png"
 
        # 버튼 격자판. CG 버튼 정렬용입니다.
        frame:
            
            grid 4 2:
                style_prefix 'page_2'
                
                xfill True
                yfill True
    
                # 이제 위에서 만들었던 g.button 들을 추가할 차례입니다.
                # 위에서처럼 g.button으로 설정한 버튼이 없다면 CG버튼은 만들 수 없습니다.
    
                # 스크린문에서는 add와 함께 g.make_button 을 이용해 CG버튼을 만듭니다.
                # add g.make_button("위에 g.button()에서 적었던 버튼 이름", "버튼 그릴 때 사용할 그림 파일 이름")
                # 을 적으면 됩니다.
                
                add g.make_button("1", "images/library/red.png", hover_border = 'images/library/slot_hover_red.png', xalign = 0.75, yalign = 0.9, background = None)
                add g.make_button("2", "images/library/orange.png", hover_border = 'images/library/slot_hover_orange.png', xalign = 0.75, yalign = 0.9, background = None)
                add g.make_button("3", "images/library/yellow.png", hover_border = 'images/library/slot_hover_yellow.png', xalign = 0.25, yalign = 0.9, background = None)
                add g.make_button("4", "images/library/yellowgreen.png", hover_border = 'images/library/slot_hover_yellowgreen.png', xalign = 0.25, yalign = 0.9, background = None)
                add g.make_button("5", "images/library/green.png", hover_border = 'images/library/slot_hover_green.png', xalign = 0.75, yalign = 0.1, background = None)
                add g.make_button("6", "images/library/blue.png", hover_border = 'images/library/slot_hover_blue.png', xalign = 0.75, yalign = 0.1, background = None) 
                add g.make_button("7", "images/library/deepblue.png", hover_border = 'images/library/slot_hover_deepblue.png', xalign = 0.25, yalign = 0.1, background = None)
                add g.make_button("8", "images/library/purple.png", hover_border = 'images/library/slot_hover_purple.png', xalign = 0.25, yalign = 0.1, background = None)
            hbox:
                    style_prefix "page"
                    
                    xalign 0.5
                    yalign 1.0

                    spacing gui.page_spacing

                    textbutton _("<") action Show("gallery")


                    ## 범위(1, 10)는 1부터 9까지 숫자를 제공합니다.
                    textbutton _("1") action Show("gallery")
                    textbutton _("2") action NullAction()

                    textbutton _(">") action NullAction()
                # 위에서 g.hover_border를 지정했는데
                # hover_border 는 g.make_button 에서도 정할 수 있습니다.
                # 전체에 적용할 때는 g.hover_border 에서, 개별로 적용할 때는 g.make_button에서 지정하면 됩니다.
                # add g.make_button("dawn mary", "gal-dawn_mary.png", hover_border = 'gal-border.png',  xalign=0.5, yalign=0.5)
    
                # CG수가 적으면 일일히 add g.make_button ... 적어도 되겠지만
                # g.make_button에 입력할 내용을 리스트에 넣어놓고 for문으로 만드는 것이 훨씬 편하겠지요.
    
            # 클릭하면 메인 메뉴로 돌아가는 버튼입니다.
            # CG 버튼 양이 많아서 여러 스크린을 만들었다면 다음 CG버튼을 보여주는 버튼을 만들어야겠죠.
            textbutton '돌아가기' action Return() xalign .5 yalign .9
##########################
style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu 스크린 ###############################################################
##
## 렌파이가 시작할 때 메인메뉴를 출력합니다.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu
# Main Menu
#
# 렌파이를 실행할 때 처음으로 나타나는 메인 메뉴를 표시하는 데 사용되는 스크린
 
init:
    image title_screen:
        "title/title_screen.png"

    transform fadein: # 메인 메뉴 버튼에 적용할 트랜스폼
        on show: #처음 등장할 때만
            alpha 0
            linear 1 alpha 1 # 서서히 나타나도록 하는 효과를 적용
         
        on replaced: # game menu 스크린과 교체될 때는
            alpha 1 # 그냥 투명도값 100%

    # 메인 메뉴에서 쓸 배경.
    # x위치 -33 에서 0으로 반복해서 움직일 뿐이지만
    # 그냥 보기에는 무한히 오른쪽으로 움직이는 것처럼 보임
    image bg mainmenu:
        im.FactorScale("title/logo.png", 0.25)
        ease 2.0 xpos 0 ypos -10
        easeout 1.0 xpos 0 ypos 0
        repeat

screen main_menu:
 
    # This ensures that any other menu screen is replaced.
    tag menu
 
    # The background of the main menu.
    #window:
        #style "mm_root"
 
    #위 init 블록에서 지정했던 메인 메뉴 배경화면
    add 'title_screen' 
     
    # 메인 메뉴 버튼
    frame:
        # 메인메뉴 버튼에 적용되는 스타일에 mm이라는 접두어를 붙임
        style_group 'mm'
 
        # style_group 적용하려고 만든거라 배경 화면은 투명하게
        background '#fff0'
        # 이 프레임 안에 들어있는 모든 버튼에
        # 아까 지정했던 페이드인 효과 지정
        at fadein

        imagebutton idle 'bg mainmenu' hover 'bg mainmenu' action NullAction() xpos 150 ypos 50
             
        imagebutton idle 'title/start1.png' hover 'title/start2.png' action Start() xpos 80 ypos 320
        imagebutton idle 'title/load1.png' hover 'title/load2.png' action ShowMenu("load") xpos 80 ypos 400
        imagebutton idle 'title/gallery1.png' hover 'title/gallery2.png' action ShowMenu("gallery") xpos 80 ypos 480
        imagebutton idle 'title/credit1.png' hover 'title/credit2.png' action ShowMenu("about") xpos 80 ypos 560

        
        # 설정 버튼.
        imagebutton idle 'title/setting1.png' hover 'title/setting2.png' action ShowMenu("preferences") xpos 1027 ypos 624
        # 종료 버튼
        imagebutton idle 'title/exit1.png' hover 'title/exit2.png' action Quit(confirm=False) xpos 1135 ypos 624


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu 스크린 ###############################################################
##
## 게임 메뉴의 기본 틀입니다. 매개변수 title로 스크린 제목을 정하고, 배경, 제목,
## 그리고 navigation 스크린을 출력합니다.
##
## scroll 매개변수는, None, "viewport" 혹은 "vpgrid" 중 하나여야 합니다.
## transclude 명령어를 통해 다른 스크린을 이 스크린 내부에 불러옵니다.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("돌아가기"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## About 스크린 ###################################################################
##
## 이 스크린은 게임과 렌파이 엔진 크레딧과 저작권 정보를 표시합니다.
##
## 특별할 것이 없으므로 스크린을 새로 커스터마이징하여 만드는 예제이기도 합니다.

screen about():

    tag menu

    ## 이 use 명령어로 game_menu 스크린을 이 스크린 내에 불러옵니다. use 명령어
    ## 하위블럭(vbox 내용)은 game_menu 스크린 내 transclude 명령어가 있는 곳에
    ## 다시 불려집니다.
    use game_menu(_("제작진"), scroll="viewport"):

        style_prefix "about"

        vbox:
            label "[config.name!t] by Sundial Games" text_size 40 text_color "#000000" xalign 0.5
            text _("{color=#000000}프린세스 커넥트 Re:Dive 팬 게임{/color}\n") xalign 0.5

            ## gui.about 의 내용은 보통 options.rpy에 있습니다.
            if gui.about:
                text "[gui.about!t]\n"



            text "{color=#000000}{b}Art{/b}{/color}\n" xalign 0.5
            
            text "{color=#000000}  Leviathan {a=https://www.pixiv.net/en/users/27350443}{color=#000000}Pixiv{/color}{/a}, {a=https://twitter.com/hikinito0902}{color=#000000}트위터{/color}{/a}{/color}" xalign 0.5
            text "{color=#000000}  Jynack {a=https://twitter.com/Nackjy09}{color=#000000}트위터{/color}{/a}{/color}" xalign 0.5
            text "{color=#000000}  대노 {a=https://www.pixiv.net/users/8407788}{color=#000000}Pixiv{/color}{/a}{/color}" xalign 0.5
            text "{color=#000000}  ??? {a=https://www.pixiv.net/users/29074698}{color=#000000}Pixiv{/color}{/a}{/color}" xalign 0.5

            text "\n{color=#000000}{b}Scenario{/b}{/color}\n" xalign 0.5

            text "{color=#000000}  모랑모랑{/color}" xalign 0.5

            text "\n{color=#000000}{b}Programming{/b}{/color}\n" xalign 0.5

            text "{color=#000000}  Procrustes{/color}\n" xalign 0.5

            text "{color=#000000}{size=10}\n본 게임은 수익을 목적으로 하지 않는 비영리 저작물입니다. 배경 음악 등 일부 요소는 본 팀의 저작물이 아님을 밝힙니다.{/size}{/color}"


            text _("{size=10}{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] 으로 만들어진 게임입니다.\n\n[renpy.license!t]{/size}")

## options.rpy에서 규정된 내용이 about 스크린에 추가됩니다.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

## 단서 ########################################################################
##
## 단서 해금용 스크린
init:
    image hankachi:
        im.FactorScale("clue/hankachi.png", 0.8)
    image letter:
        im.FactorScale("clue/letter.png", 0.8)
    image key:
        im.FactorScale("clue/key.png", 0.8)
    image unagi:
        im.FactorScale("clue/unagi.png", 0.8)
    image kiroku:
        im.FactorScale("clue/kiroku.png", 0.8)
    image akudaikan:
        im.FactorScale("clue/akudaikan.png", 0.8)
    image syokuin:
        im.FactorScale("clue/syokuin.png", 0.8)
    image rima:
        im.FactorScale("clue/rima.png", 0.8)
    image yanki:
        im.FactorScale("clue/yanki.png", 0.8)

    image hankachi1:
        im.FactorScale("clue/hankachi.png", 0.85)
    image letter1:
        im.FactorScale("clue/letter.png", 0.85)
    image key1:
        im.FactorScale("clue/key.png", 0.85)
    image unagi1:
        im.FactorScale("clue/unagi.png", 0.85)
    image kiroku1:
        im.FactorScale("clue/kiroku.png", 0.85)
    image akudaikan1:
        im.FactorScale("clue/akudaikan.png", 0.85)
    image syokuin1:
        im.FactorScale("clue/syokuin.png", 0.85)
    image rima1:
        im.FactorScale("clue/rima.png", 0.85)
    image yanki1:
        im.FactorScale("clue/yanki.png", 0.85)

    image locked:
        im.FactorScale("clue/locked.png", 0.8)
     
screen clue:

    tag menu

    use game_menu(_("단서")):
        grid 1 3:
            xfill True
            yfill True
            if persistent.clues_hankachi == True:
                imagebutton idle 'hankachi' hover 'hankachi1' action NullAction()
            else:
                imagebutton idle 'locked' hover 'locked' action NullAction()

            if persistent.clues_letter == True:
                imagebutton idle 'letter' hover 'letter1' action NullAction()
            else:
                imagebutton idle 'locked' hover 'locked' action NullAction()

            if persistent.clues_key == True:
                imagebutton idle 'key' hover 'key1' action NullAction()
            else:
                imagebutton idle 'locked' hover 'locked' action NullAction()
                
        hbox:
            style_prefix "page"
                        
            xalign 0.5
            ypos 550

            spacing gui.page_spacing

            textbutton _("<") action NullAction()


            ## 범위(1, 10)는 1부터 9까지 숫자를 제공합니다.
            textbutton _("1") action NullAction() text_color "#f578f3"
            textbutton _("2") action Show("clue2")
            textbutton _("3") action Show("clue3")

            textbutton _(">") action Show("clue2")
screen clue2:

    tag menu

    #grid 1 3:
    use game_menu(_("단서")):
        grid 1 3:
            xfill True
            yfill True
            
            if persistent.clues_unagi == True:
                imagebutton idle 'unagi' hover 'unagi1' action NullAction()
            else:
                imagebutton idle 'locked' hover 'locked' action NullAction()

            if persistent.clues_kiroku == True:
                imagebutton idle 'kiroku' hover 'kiroku1' action NullAction()
            else:
                imagebutton idle 'locked' hover 'locked' action NullAction()

            if persistent.clues_akudaikan == True:
                imagebutton idle 'akudaikan' hover 'akudaikan1' action NullAction()
            else:
                imagebutton idle 'locked' hover 'locked' action NullAction()
            
            
            
   
        hbox:
            style_prefix "page"
                        
            xalign 0.5
            ypos 550

            spacing gui.page_spacing

            textbutton _("<") action Show("clue")


            ## 범위(1, 10)는 1부터 9까지 숫자를 제공합니다.
            textbutton _("1") action Show("clue")
            textbutton _("2") action NullAction() text_color "#f578f3"
            textbutton _("3") action Show("clue3")

            textbutton _(">") action Show("clue3")
screen clue3:

    tag menu
    use game_menu(_("단서")):
        grid 1 3:
            xfill True
            yfill True
            
            if persistent.clues_syokuin == True:
                imagebutton idle 'syokuin' hover 'syokuin1' action NullAction()
            else:
                imagebutton idle 'locked' hover 'locked' action NullAction()

            if persistent.clues_rima == True:
                imagebutton idle 'rima' hover 'rima1' action NullAction()
            else:
                imagebutton idle 'locked' hover 'locked' action NullAction()

            if persistent.clues_yanki == True:
                imagebutton idle 'yanki' hover 'yanki1' action NullAction()
            else:
                imagebutton idle 'locked' hover 'locked' action NullAction()
            
            
                

        hbox:
            style_prefix "page"
                        
            xalign 0.5
            ypos 550

            spacing gui.page_spacing

            textbutton _("<") action Show("clue2")


            ## 범위(1, 10)는 1부터 9까지 숫자를 제공합니다.
            textbutton _("1") action Show("clue")
            textbutton _("2") action Show("clue2")
            textbutton _("3") action NullAction() text_color "#f578f3"

            textbutton _(">") action NullAction()



## Load 그리고 Save 스크린 ###########################################################
##
## 이 스크린은 세이브/로드에 쓰입니다. 거의 동일하기 때문에, file_slots 스크린을
## 불러와서 씁니다.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("저장하기"))


screen load():

    tag menu

    use file_slots(_("불러오기"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("{} 페이지"), auto=_("자동 세이브"), quick=_("퀵세이브"))

    use game_menu(title):

        fixed:

            ## input이 세이브/로드 버튼보다 먼저 엔터에 반응하도록 합니다.
            order_reverse True

            ## 페이지 제목을 플레이어가 수정할 수 있음.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## 파일 슬롯 그리드.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("빈 슬롯")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## 페이지 이동 버튼.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}자동") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}퀵") action FilePage("quick")

                ## 범위(1, 10)는 1부터 9까지 숫자를 제공합니다.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences 스크린 #############################################################
##
## Preferences 스크린에서는 각종 환경설정을 플레이어가 지정할 수 있습니다.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("환경설정"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("화면 모드")
                        textbutton _("창 화면") action Preference("display", "window")
                        textbutton _("전체 화면") action Preference("display", "fullscreen")

                ## "radio_pref" 나 "check_pref" 를 추가하여 그 외에도 환경설정
                ## 항목을 추가할 수 있습니다.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("텍스트 속도")

                    bar value Preference("text speed")

                    label _("자동 진행 시간")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("배경음 음량")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("효과음 음량")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("테스트") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("음성 음량")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("테스트") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("모두 음소거"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## History 스크린 #################################################################
##
## 지난 대사록을 출력합니다. _history_list 에 저장된 대사 기록을 확인합니다.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## 이 스크린은 내용이 아주 많을 수 있으므로 prediction을 끕니다.
    predict False

    use game_menu(_("대사록"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## history_height 이 None일 경우 레이아웃이 틀어지지 않게 합니
                ## 다.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## 화자 Character에 화자 색깔이 지정되어 있으면 불러옵니
                        ## 다.
                        if "#ffffff" in h.who_args:
                            text_color h.who_args["#ffffff"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("대사가 없습니다.")


## 이것은 대사록 화면에 표시할 수 있는 태그를 결정합니다.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help 스크린 ####################################################################
##
## 입력장치의 기능을 설명합니다. 각 입력장치별 설정은 keyboard_help, mouse_help,
## gamepad_help 스크린을 각각 불러와서 출력합니다.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("조작방법"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("키보드") action SetScreenVariable("device", "keyboard")
                textbutton _("마우스") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("게임패드") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("엔터(Enter)")
        text _("대사 진행 및 UI (선택지 포함) 선택.")

    hbox:
        label _("스페이스(Space)")
        text _("대사를 진행하되 선택지는 선택하지 않음.")

    hbox:
        label _("화살표 키")
        text _("UI 이동.")

    hbox:
        label _("이스케이프(Esc)")
        text _("게임 메뉴 불러옴.")

    hbox:
        label _("컨트롤(Ctrl)")
        text _("누르고 있는 동안 대사를 스킵.")

    hbox:
        label _("탭(Tab)")
        text _("대사 스킵 토글.")

    hbox:
        label _("페이지 업(Page Up)")
        text _("이전 대사로 롤백.")

    hbox:
        label _("페이지 다운(Page Down)")
        text _("이후 대사로 롤포워드.")

    hbox:
        label "H"
        text _("UI를 숨김.")

    hbox:
        label "S"
        text _("스크린샷 저장.")

    hbox:
        label "V"
        text _("{a=https://www.renpy.org/l/voicing}대사 읽어주기 기능{/a} 토글.")


screen mouse_help():

    hbox:
        label _("클릭")
        text _("대사 진행 및 UI (선택지 포함) 선택.")

    hbox:
        label _("가운데 버튼이나 휠버튼 클릭")
        text _("UI를 숨김.")

    hbox:
        label _("우클릭")
        text _("게임 메뉴 불러옴.")

    hbox:
        label _("휠 위로\n롤백 클릭")
        text _("이전 대사로 롤백.")

    hbox:
        label _("휠 아래로")
        text _("이후 대사로 롤포워드.")


screen gamepad_help():

    hbox:
        label _("오른쪽 트리거(RT)\nA버튼/아래 버튼")
        text _("대사 진행 및 UI (선택지 포함) 선택.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("이전 대사로 롤백.")

    hbox:
        label _("오른쪽 범퍼(RB)")
        text _("이후 대사로 롤포워드.")


    hbox:
        label _("D-Pad, 아날로그 스틱")
        text _("UI 이동.")

    hbox:
        label _("스타트 버튼/가이드 버튼")
        text _("게임 메뉴 불러옴.")

    hbox:
        label _("Y버튼/위 버튼")
        text _("UI를 숨김.")

    textbutton _("조정") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## 그 외 스크린
################################################################################


## Confirm 스크린 #################################################################
##
## 게임 입력 관련 예/아니오 질문을 플레이어에게 할 때 이 스크린을 표시합니다.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 이 스크린이 출력 중일 때 다른 스크린과 상호작용할 수 없게 합니다.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("네") action yes_action
                textbutton _("아니오") action no_action

    ## 우클릭과 esc는 '아니오'를 입력하는 것과 같습니다.
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator 스크린 ##########################################################
##
## Skip_indicator 스크린은 스킵 중일 때 "스킵 중"을 표시하기 위해 출력됩니다.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("넘기는 중")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 이 transform으로 화살표를 순서대로 페이드인/페이드아웃합니다.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## BLACK RIGHT-POINTING SMALL TRIANGLE 글리프가 있는 글꼴을 사용해야 합니다.
    font "DejaVuSans.ttf"

## Clue Finded 스크린 #############################################################
##
## 단서를 발견했을 때 좌측 상단에 이미지를 출력합니다.
##

screen clueFinded:

    zorder 100

    add "gui/clue.png" at clue_appear
    vbox:
        xalign 0.08 yalign 0.03
        text "  새로운 단서 발견!"
        text "단서 항목에서 확인 가능"
    timer 3.25 action Hide('clueFinded')

transform clue_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

## Notify 스크린 ##################################################################
##
## Notify 스크린으로 플레이어에게 메시지를 출력합니다. (예를 들어 '퀵세이브 완
## 료'나 '스크린샷 저장 완료')
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL 스크린 #####################################################################
##
## NVL모드 대사와 선택지를 출력합니다.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## vpgrid나 vbox 내에 대사를 출력합니다.
        if gui.nvl_height:

            vpgrid:
                cols 2
                xpos -100 ypos 260

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## 선택지가 있을 경우, 선택지 출력. config.narrator_menu가 True일 경우
        ## 선택지가 비정상적으로 출력될 수 있습니다. (디폴트는 True입니다.)
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 동시에 출력될 수 있는 NVL 대사의 최대치를 조정합니다.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## 모바일 버전
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## 마우스가 없고 화면이 작을 가능성이 높으므로, 퀵메뉴 버튼의 크기를 키우고 가짓
## 수를 줄입니다.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("되감기") action Rollback()
            textbutton _("넘기기") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("자동진행") action Preference("auto-forward", "toggle")
            textbutton _("메뉴") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600
