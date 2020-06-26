 ## 초기설정 #############################
init python:
    config.rollback_enabled = True

## 스탠딩 ###############################
init:
    ## 모니카
    image stand_Monica:
        im.FactorScale("Character/monica/monica.png", 0.22)
    image stand_Monica_crying:
        im.FactorScale("Character/monica/monica_crying.png", 0.22)
    image stand_Monica_ddung:
        im.FactorScale("Character/monica/monica_ddung.png", 0.22)
    image stand_Monica_dere:
        im.FactorScale("Character/monica/monica_dere.png", 0.22)
    image stand_Monica_down:
        im.FactorScale("Character/monica/monica_down.png", 0.22)
    image stand_Monica_munen:
        im.FactorScale("Character/monica/monica_munen.png", 0.22)
    image stand_Monica_surprised:
        im.FactorScale("Character/monica/monica_surprised.png", 0.22)
    image stand_Monica_yukata:
        im.FactorScale("Character/monica/monica_yukata.png", 0.22)
    image stand_Monica_yukata_crying:
        im.FactorScale("Character/monica/monica_yukata_crying.png", 0.22)
    image stand_Monica_yukata_ddung:
        im.FactorScale("Character/monica/monica_yukata_ddung.png", 0.22)
    image stand_Monica_yukata_dere:
        im.FactorScale("Character/monica/monica_yukata_dere.png", 0.22)
    image stand_Monica_yukata_down:
        im.FactorScale("Character/monica/monica_yukata_down.png", 0.22)
    image stand_Monica_yukata_munen:
        im.FactorScale("Character/monica/monica_yukata_munen.png", 0.22)
    image stand_Monica_yukata_surprised:
        im.FactorScale("Character/monica/monica_yukata_surprised.png", 0.22)
    ## 쿠우카
    image stand_Kuka:
        im.FactorScale("Character/kuka/kuka.png", 0.18)
    image stand_Kuka_down:
        im.FactorScale("Character/kuka/kuka_down.png", 0.18)
    image stand_Kuka_hiku:
        im.FactorScale("Character/kuka/kuka_hiku.png", 0.18)
    image stand_Kuka_mousou:
        im.FactorScale("Character/kuka/kuka_mousou.png", 0.18)
    image stand_Kuka_shamed:
        im.FactorScale("Character/kuka/kuka_shamed.png", 0.18)
    image stand_Kuka_surprised:
        im.FactorScale("Character/kuka/kuka_surprised.png", 0.18)
    image stand_Kuka_yukata:
        im.FactorScale("Character/kuka/kuka_yukata.png", 0.18)
    image stand_Kuka_yukata_down:
        im.FactorScale("Character/kuka/kuka_yukata_down.png", 0.18)
    image stand_Kuka_yukata_hiku:
        im.FactorScale("Character/kuka/kuka_yukata_hiku.png", 0.18)
    image stand_Kuka_yukata_mousou:
        im.FactorScale("Character/kuka/kuka_yukata_mousou.png", 0.18)
    image stand_Kuka_yukata_shamed:
        im.FactorScale("Character/kuka/kuka_yukata_shamed.png", 0.18)
    image stand_Kuka_yukata_surprised:
        im.FactorScale("Character/kuka/kuka_yukata_surprised.png", 0.18)
    ## 유키
    image stand_Yuki:
        im.FactorScale("Character/yuki/yuki.png", 0.18)
    image stand_Yuki_angry:
        im.FactorScale("Character/yuki/yuki_angry.png", 0.18)
    image stand_Yuki_ddung:
        im.FactorScale("Character/yuki/yuki_ddung.png", 0.18)
    image stand_Yuki_proud:
        im.FactorScale("Character/yuki/yuki_proud.png", 0.18)
    image stand_Yuki_shamed:
        im.FactorScale("Character/yuki/yuki_shamed.png", 0.18)
    image stand_Yuki_yukata:
        im.FactorScale("Character/yuki/yuki_yukata.png", 0.18)
    image stand_Yuki_yukata_angry:
        im.FactorScale("Character/yuki/yuki_yukata_angry.png", 0.18)
    image stand_Yuki_yukata_ddung:
        im.FactorScale("Character/yuki/yuki_yukata_ddung.png", 0.18)
    image stand_Yuki_yukata_proud:
        im.FactorScale("Character/yuki/yuki_yukata_proud.png", 0.18)
    image stand_Yuki_yukata_shamed:
        im.FactorScale("Character/yuki/yuki_yukata_shamed.png", 0.18)
    
    ## 니논
    image stand_Ninon:
        im.FactorScale("Character/ninon/ninon.png", 0.18)
    image stand_Ninon_down:
        im.FactorScale("Character/ninon/ninon_down.png", 0.18)
    image stand_Ninon_embarassed:
        im.FactorScale("Character/ninon/ninon_embarrassed.png", 0.18)
    image stand_Ninon_innocence:
        im.FactorScale("Character/ninon/ninon_innocence.png", 0.18)
    image stand_Ninon_surprise:
        im.FactorScale("Character/ninon/ninon_surprise.png", 0.18)
    image stand_Ninon_wink:
        im.FactorScale("Character/ninon/ninon_wink.png", 0.18)
    image stand_Ninon_angry:
        im.FactorScale("Character/ninon/ninon_angry.png", 0.18)
    image stand_Ninon_daiji:
        im.FactorScale("Character/ninon/ninon_daiji.png", 0.18)
    image stand_Ninon_panic:
        im.FactorScale("Character/ninon/ninon_panic.png", 0.18)
    image stand_Ninon_yukata:
        im.FactorScale("Character/ninon/ninon_yukata.png", 0.18)
    image stand_Ninon_yukata_angry:
        im.FactorScale("Character/ninon/ninon_yukata_angry.png", 0.18)
    image stand_Ninon_yukata_daiji:
        im.FactorScale("Character/ninon/ninon_yukata_daiji.png", 0.18)
    image stand_Ninon_yukata_down:
        im.FactorScale("Character/ninon/ninon_yukata_down.png", 0.18)
    image stand_Ninon_yukata_emb:
        im.FactorScale("Character/ninon/ninon_yukata_emb.png", 0.18)
    image stand_Ninon_yukata_innocent:
        im.FactorScale("Character/ninon/ninon_yukata_innocent.png", 0.18)
    image stand_Ninon_yukata_panic:
        im.FactorScale("Character/ninon/ninon_yukata_panic.png", 0.18)
    image stand_Ninon_yukata_surp:
        im.FactorScale("Character/ninon/ninon_yukata_surp.png", 0.18)
    image stand_Ninon_yukata_wink:
        im.FactorScale("Character/ninon/ninon_yukata_wink.png", 0.18)
    ## 구라노스케
    image stand_gura:
        im.FactorScale("Character/gura/gura.png", 1.0)
    image cg_gura_baby:
        im.FactorScale("library/cg_gura_baby.png", 1.0)
    image cg_gura_child:
        im.FactorScale("library/cg_gura_child.png", 1.0)
    ## 마물
    image stand_monster:
        im.FactorScale("Character/monster/monster.png", 0.2)
## 트랜스폼
    transform movetoright:
        ease 0.5 xalign 1.0

    transform movetoveryright:
        ease 0.5 xalign 1.1

    transform movetocenter:
        linear 0.5 xalign 0.5
        
    transform movetoleft:
        ease 0.5 xalign 0.0

        
    transform rotated:
        linear .5 rotate 360 yalign 0.3

    transform fast_rotating:
        linear 0.3 rotate 360 yalign 0.5

    transform fast_rotating_2:
        linear 0.3 rotate 720 yalign 0.5
    transform xycenter:
        xalign 0.5 yalign 0.5
## 배경 cg
    image bg_forest:
        im.FactorScale("bg/forest.jpg", 0.4)

    image bg_town:
        im.FactorScale("bg/bg_town.png", 0.68)
    
    image bg_room:
        im.FactorScale("bg/room.jpg", 2.55)

    image bg_end:
        im.FactorScale("bg/bg_end.png", 1.0)    
    image highlight:
        im.FactorScale("library/highlight_line.png", 1.1)
    
    image bg_guildhouse:
        im.FactorScale("bg/bg_guildhouse.png", 0.256)
    
    image bg_black:
        im.FactorScale("bg/black.png", 2.0)
    image bg_surf:
        im.FactorScale("bg/surf.jpg", 1.75)

    image bg_onsen:
        im.FactorScale("bg/bg_onsen.jpg", 1.8)

    image bg_routen:
        im.FactorScale("bg/bg_routen.jpg", 1.3)

    image bg_onsen_heya_01:
        im.FactorScale("bg/bg_onsen_heya_01.png", 0.67)

    image bg_onsen_heya_02:
        im.FactorScale("bg/bg_onsen_heya_02.png", 1.0)

    image bg_tyugaku:
        im.FactorScale("bg/bg_tyugaku.png", 0.67)

    image bg_tyugaku_running:
        im.FactorScale("bg/bg_tyugaku_running.png", 1.3)

    image bg_tyugaku_stop:
        im.FactorScale("bg/bg_tyugaku_stop.png", 1.3)

    image logo_head = "logo/logo.png"

## 캐릭터 ###############################
init:
    define ch_ninon = Character('니논', color="#f5f562")

    define ch_monica = Character('모니카', color = "#c8ed0c")

    define ch_kuka = Character('쿠우카', color = "#a812c9")

    define ch_yuki = Character('유키', color = "#f285dc")

    define ch_ayumi = Character('아유미', color = "#0cf246")

    define player_name = "가상의 이름 simulated name"

    define player = Character("name", dynamic = True)

    define monster = Character("마물", color = "#ffffff")

    define ch_peco = Character("페코린느", color = "#f2a20c")

    define ch_kyaru = Character("배신자", color = "#071469")

    define ch_gura = Character("구라노스케")

## 나래이터류 ############################
init:
    define narrator = Character(None, kind = nvl)
    define ch_nar = Character(None)
    define centered = Character(what_bold = True, color = "#000000")
    define hatena = Character('???', color = "#ffffff")
## 포지셔닝 ##############################
init:
    define center = Position(xalign = 0.5)
    define left = Position(xalign = 0.2)
    define right = Position(xalign = 0.8)
    define underleft = Position(xalign = 0.0, yalign = 1.0)
    define veryleft = Position(xalign = 0.0)
    define veryright = Position(xalign = 1.0)
    define center_center = Position(xalign = 0.5, yalign = 0.5)
## 호감도 ################################
init:
    define love_point = 0
    define point_monica = 0
    define point_ninon = 0
    define point_kuka = 0
    define point_yuki = 0
    define ninon = 0
    define kuka = 0
    define yuki = 0
    define monica = 0
## 받침 유무 판별기 #######################
init python:
          
    finalConso =  None
    name = ''
     
    #받침유무판별기
    def finalChecker(name):
        import re
        name = name
        expr = re.compile(r'([a-zA-Z0-9\s~!@#$%^&*()_+|}{:"<>?`\-=\\\[\];\',./])')
        temp = expr.sub('', name)
          
        if temp == '':
            return False
          
        last_alphabet = repr(temp[-1])
        dec = int(str(last_alphabet[4:-1]), 16)
          
        while dec < 0x3164:
            temp = temp[:-1]
            if not temp:
                return False
                  
            last_alphabet=repr(temp[-1])
            dec = int(str(last_alphabet[4:-1]), 16)
                  
        dec= (dec-44032) % 588 % 28
   
        if dec == 0:
            return False
              
        else:
            return True
              
    #조사 바꾸기
    def pppChanger(input):
        import re
        pppList = [('가', '이'), ('는', '은'),
                        ('를', '을'), ('와', '과'),
                        ]
                          
        if finalConso:
                  
            for p, pc in pppList:
                input = re.sub('\[name\]'+ p, "[name]" + pc, input)
                input = re.sub('%\(name\)s' + p, "[name]" + pc, input)
                  
        return input
              
    config.say_menu_text_filter = pppChanger

## 갤러리 #################################
init:
    image end1 = "library/end1.jpg"
    image ninon_pingping:
        im.FactorScale("library/ninon_pingping.png", 0.5)
    image cg_yuki_01:
        im.FactorScale("library/cg_yuki_01.png", 1.0)

    image cg_ninon_happy_01 = "library/cg_ninon_happy_01.png"
    image cg_ninon_happy_02 = "library/cg_ninon_happy_02.png"
    image cg_ninon_happy_03 = "library/cg_ninon_happy_03.png"
    image cg_ninon_happy_04 = "library/cg_ninon_happy_04.png"
    image cg_ninon_happy_05 = "library/cg_ninon_happy_05.png"

define persistent.unlock_1 = False  
## 시작 전 로고 화면 ######################
label splashscreen:
    scene logo_head onlayer middle with fade
    $ renpy.pause(2, hard = True)
    show black onlayer background
    hide logo_head onlayer middle with fade
    return
## 미니 게임 변수 #########################
init:
    define win_point = 0
## 3D 카메라 ##############################
init -1600 python:

    ##########################################################################
    # Camera functions

    # value of _3d_layers isn't included in rollback.
    # so I copy it many times.
    _3d_layers = {}
    _camera_x = 0
    _camera_y = 0
    _camera_z = 0
    _camera_rotate = 0
    _FOCAL_LENGTH = 147.40
    _LAYER_Z = 1848.9
    _last_camera_arguments = None

    def register_3d_layer(*layers):
        """
         :doc: camera

         Register layers as 3D layers. Only 3D layers will be affected by camera
         movement and 3D layer transforms. This should be called in an init
         block. If no layers are registered as 3D layers, the 'master' layer
         will become a 3D layer by default.

         `layers`
              This should be a string or a group of strings naming registered layers.
         """
        global _3d_layers
        _3d_layers = {layer:_LAYER_Z for layer in layers}

    def camera_reset():
        """
         :doc: camera

         Resets the camera and 3D layers positions. This needs to be called at least once,
         or 3D layer depth may behave erratically and the 3D camera will not be able to properly save
         3D layer depth.
         """
        global _3d_layers
        _3d_layers = _3d_layers.copy()
        for layer in _3d_layers:
            layer_move(layer, _LAYER_Z)
        camera_move(0, 0, 0)

    def camera_restore():
        """
         :doc: camera

         Safety method used internally to deal with unexpected behavior.

         """
        camera_move(_camera_x, _camera_y, _camera_z)

    def camera_move(x, y, z, rotate=0, duration=0, warper='linear', subpixel=True, loop=False, x_express=None, y_express=None, z_express=None, rotate_express=None):
        """
         :doc: camera

         Moves the camera to a given coordinate and rotation.

         `x`
              The x coordinate to move the camera to.
         `y`
              The y coordinate to move the camera to.
         `z`
              The z coordinate to move the camera to.
         `rotate`
              Rotation of the camera, perpindicular to the scene, in degrees.
         `duration`
              The time, in seconds, to complete the camera move. If no time is given,
              the move will happen instantaneously.
         `warper`
              A string that points to a registered ATL warper, like \'ease\'.
              If no warper is given, this will default to \'linear\'.
         `subpixel`
              If True, transforms caused by the 3D camera will be rendered with
              subpixel precision. This defaults to True.
         `loop`
              If true, the camera move will continually loop until another camera
              action interrupts. This defaults to False.
         `x_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the x coordinate of the camera.
         `y_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the y coordinate of the camera.
         `z_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the z coordinate of the camera.
         `rotate_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the rotation value of the camera.
         """

        camera_moves([(x, y, z, rotate, duration, warper, ),], subpixel=subpixel, loop=loop, x_express=x_express, y_express=y_express, z_express=z_express, rotate_express=rotate_express)

    def camera_relative_move(x, y, z, rotate=0, duration=0, warper='linear', subpixel=True, loop=False, x_express=None, y_express=None, z_express=None, rotate_express=None):
        """
         :doc: camera

         Move the coordinate and rotate of a camera relatively and apply transforms to all 3D layers.

         `x`
              the x coordinate of a camera relative to the current one.
         `y`
              the y coordinate of a camera relative to the current one.
         `z`
              the z coordinate of a camera relative to the current one.
         `rotate`
              Defaul 0, the rotate of a camera relative to the current one.
         `duration`
              Default 0, this is the second times taken to move a camera.
         `warper`
              Default 'linear', this should be string and the name of a warper
              registered with ATL.
         `subpixel`
              Default True, if True, causes things to be drawn on the screen
              using subpixel positioning
         `loop`
              Default False, if True, this motion repeats.
         'x_express'
             This should be callable, which is called with the shown timebase
             and the animation timebase, in seconds and return a number. The
             result of this is added to the x coordinate of the camera.
         'y_express'
             This should be callable, which is called with the shown timebase
             and the animation timebase, in seconds and return a number. The
             result of this is added to the y coordinate of the camera.
         'z_express'
             This should be callable, which is called with the shown timebase
             and the animation timebase, in seconds and return a number. The
             result of this is added to the z coordinate of the camera.
         'rotate_express'
             This should be callable, which is called with the shown timebase
             and the animation timebase, in seconds and return a number. The
             result of this is added to the rotate coordinate of the camera.
         """
        camera_move(x+_camera_x, y+_camera_y, z+_camera_z, rotate+_camera_rotate, duration, warper, subpixel, loop, x_express, y_express, z_express, rotate_express)


    def layer_move(layer, z, duration=0, warper='linear', subpixel=True, loop=False, x_express=None, y_express=None, z_express=None, rotate_express=None):
        """
         :doc: camera

         Moves the z coordinate of a layer and applies a transform to the layer.

         `layer`
              A string that names a registered 3D layer to be moved.
         `z`
              The z coordinate to move the 3D layer to.
         `duration`
              The time, in seconds, to complete the layer move. If no time is given,
              the move will happen instantaneously.
         `warper`
              A string that points to a registered ATL warper, like \'ease\'.
              If no warper is given, this will default to \'linear\'.
         `subpixel`
              If True, the resulting layer move will be rendered with
              subpixel precision. This defaults to True.
         `loop`
              If true, the layer move will continually loop until another camera
              action interrupts. This defaults to False.
         `x_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the x coordinate of the camera.
         `y_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the y coordinate of the camera.
         `z_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the z coordinate of the camera.
         `rotate_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the rotation value of the camera.
         """

        layer_moves(layer, [(z, duration, warper, ),], subpixel=subpixel, loop=loop, x_express=x_express, y_express=y_express, z_express=z_express, rotate_express=rotate_express)

    def camera_moves(check_points, loop=False, subpixel=True, x_express=None, y_express=None, z_express=None, rotate_express=None):
        """
         :doc: camera

         Allows multiple camera moves to happen in succession.

         `check_points`
              A list of camera moves, in the format of (x, y, z, rotate, duration, warper)
         `loop`
              If true, the camera moves will continually loop until another camera
              action interrupts. This defaults to False.
         `subpixel`
              If True, transforms caused by the 3D camera will be rendered with
              subpixel precision. This defaults to True.
         `x_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the x coordinate of the camera.
         `y_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the y coordinate of the camera.
         `z_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the z coordinate of the camera.
         `rotate_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the rotation value of the camera.
         """
        camera_check_points = {}
        camera_check_points["x"] = []
        camera_check_points["y"] = []
        camera_check_points["z"] = []
        camera_check_points["rotate"] = []
        for x, y, z, rotate, duration, warper in check_points:
            camera_check_points["x"].append((x, duration, warper))
            camera_check_points["y"].append((y, duration, warper))
            camera_check_points["z"].append((z, duration, warper))
            camera_check_points["rotate"].append((rotate, duration, warper))
        kwargs = {coordinate+"_loop":loop for coordinate in ["x", "y", "z", "rotate"]}
        all_moves(camera_check_points=camera_check_points, loop=loop, subpixel=subpixel, x_express=x_express, y_express=y_express, z_express=z_express, rotate_express=rotate_express, **kwargs)

    def layer_moves(layer, check_points, loop=False, subpixel=True, x_express=None, y_express=None, z_express=None, rotate_express=None):
        """
         :doc: camera

         Move a layer through check points and apply transform to the layer.

         `layer`
              A string that names a registered 3D layer to be moved.
         `check_points`
              A list of layer moves, in the format of (z, duration, warper)
         `loop`
              If true, the layer moves will continually loop until another camera
              action interrupts. This defaults to False.
         `subpixel`
              If True, the resulting layer moves will be rendered with
              subpixel precision. This defaults to True.
         `x_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the x coordinate of the camera.
         `y_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the y coordinate of the camera.
         `z_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the z coordinate of the camera.
         `rotate_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the rotation value of the camera.
         """
        all_moves(layer_check_points={layer:check_points}, subpixel=subpixel, x_express=x_express, y_express=y_express, z_express=z_express, rotate_express=rotate_express, **{layer+"_loop":loop})

    def all_moves(camera_check_points=None, layer_check_points=None, subpixel=True, play=True, x_loop=False, y_loop=False, z_loop=False, rotate_loop=False, x_express=None, y_express=None, z_express=None, rotate_express=None, **kwargs):
        """
         :doc: camera

         Allows for both camera moves and layer moves to happen within the same interaction, in any given combination. The Action Editor will usually generate these.

         `camera_check_points`
             A list of check points for the camera to go through, split by coordinate in the following format:
              {
                  'x':[(x, duration, warper)...]
                  'y':[(y, duration, warper)...]
                  'z':[(z, duration, warper)...]
                  'rotate':[(rotate, duration, warper)...]
              }
         `layer_check_points`
             A list of check points for layers to go through, in the following format:
              {
                  'layer name':[(z, duration, warper)...]
              }
         `loop_x`
              If True, all x coordinate check points will loop continuously. This defaults to False.
         `loop_y`
              If True, all y coordinate check points will loop continuously. This defaults to False.
         `loop_z`
              If True, all z coordinate check points will loop continuously. This defaults to False.
         `loop_rotate`
              If True, all rotation check points will loop continuously. This defaults to False.
         `subpixel`
              If True, all transforms caused by this function will be drawn with subpixel precision. This defaults to True.
         `<layer name>_loop`
              If True, all layer move check points for the given layer will loop continuously. This defaults to False.
         `x_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the x coordinate of the camera.
         `y_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the y coordinate of the camera.
         `z_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the z coordinate of the camera.
         `rotate_express`
             This should be a callable function that is called with the shown 
             timebase and is given an animation timebase in seconds. The
             result of this function is added to the rotation value of the camera.
         """
        global _camera_x, _camera_y, _camera_z, _camera_rotate, _3d_layers, _last_camera_arguments
        from math import sin, pi
        from random import random

        if camera_check_points is None:
            camera_check_points = {}
        if layer_check_points is None:
            layer_check_points = {}
        if config.developer:
            _last_camera_arguments = (camera_check_points, layer_check_points, x_loop, y_loop, z_loop, rotate_loop, x_express, y_express, z_express, rotate_express, kwargs, _camera_x, _camera_y, _camera_z, _camera_rotate, _3d_layers.copy())
        start_xanchor = _FOCAL_LENGTH*_camera_x/(renpy.config.screen_width *_LAYER_Z) + .5
        start_yanchor = _FOCAL_LENGTH*_camera_y/(renpy.config.screen_height*_LAYER_Z) + .5
        camera_check_points2 = { 'xanchor':[(start_xanchor, 0, None, )], 'yanchor':[(start_yanchor, 0, None, )], 'z': [(_camera_z, 0, None, )], 'rotate':[(_camera_rotate, 0, None, )] }

        for coordinate in ["x", "y", "z", "rotate"]:
            if coordinate not in camera_check_points:
                camera_check_points[coordinate] = [(getattr(renpy.store, "_camera_"+coordinate), 0, None, )]
        for c in camera_check_points['x']:
            camera_check_points2['xanchor'].append((_FOCAL_LENGTH*c[0]/(renpy.config.screen_width *_LAYER_Z) + .5, c[1], c[2], ))
        for c in camera_check_points['y']:
            camera_check_points2['yanchor'].append((_FOCAL_LENGTH*c[0]/(renpy.config.screen_height *_LAYER_Z) + .5, c[1], c[2], ))
        camera_check_points2['z'].extend(camera_check_points['z'])
        camera_check_points2['rotate'].extend(camera_check_points['rotate'])
        for layer in _3d_layers:

            if layer not in layer_check_points:
                layer_check_points[layer] = [(_3d_layers[layer], 0, None), ]
            layer_check_points2 = [(_3d_layers[layer], 0, None), ]
            for c in layer_check_points[layer]:
                layer_check_points2.append((c[0], float(c[1]), c[2]))
            layer_loop = kwargs.get(layer+"_loop", False)

            if play:
                renpy.game.context().scene_lists.set_layer_at_list(layer, [Transform(function=renpy.curry(_camera_trans)(camera_check_points=camera_check_points2, layer_check_points=layer_check_points2, subpixel=subpixel, layer=layer, layer_loop=layer_loop, x_loop=x_loop, y_loop=y_loop, z_loop=z_loop, rotate_loop=rotate_loop, x_express=x_express, y_express=y_express, z_express=z_express, rotate_express=rotate_express))])
                layer_z = layer_check_points2[-1][0]
            else:
                # This is used when the time bar is changed by Action Editor
                st = _viewers.time
                xanchor = get_at_time(camera_check_points2['xanchor'], st, x_loop)
                yanchor = get_at_time(camera_check_points2['yanchor'], st, y_loop)
                z = get_at_time(camera_check_points2['z'], st, z_loop)
                rotate = get_at_time(camera_check_points2['rotate'], st, rotate_loop)
                layer_z = get_at_time(layer_check_points2, st, layer_loop)
                if x_express:
                    xanchor += _FOCAL_LENGTH*x_express(st, st)/(renpy.config.screen_width *_LAYER_Z)
                if y_express:
                    yanchor += _FOCAL_LENGTH*y_express(st, st)/(renpy.config.screen_height *_LAYER_Z)
                if z_express:
                    z += z_express(st, st)
                if rotate_express:
                    rotate += rotate_express(st, st)
                distance = float(layer_z - z)
                if distance == 0:
                    distance = .1
                if distance >= 0:
                    alpha = 1
                    zoom = _LAYER_Z / distance
                    renpy.game.context().scene_lists.set_layer_at_list(layer, [Transform(xpos=.5, ypos=.5, alpha=alpha, transform_anchor=True, xanchor=xanchor, yanchor=yanchor, zoom=zoom, rotate=rotate)])
                else:
                    alpha = 0
                    renpy.game.context().scene_lists.set_layer_at_list(layer, [Transform(xpos=.5, ypos=.5, alpha=alpha, transform_anchor=True, xanchor=xanchor, yanchor=yanchor, rotate=rotate)])

            _3d_layers[layer] = int(layer_z)
        if play:
            _camera_x = camera_check_points['x'][-1][0]
            _camera_y = camera_check_points['y'][-1][0]
            _camera_z = camera_check_points['z'][-1][0]
            _camera_rotate = camera_check_points['rotate'][-1][0]
        else:
            _camera_x         = int(((xanchor-.5)*renpy.config.screen_width*_LAYER_Z)/_FOCAL_LENGTH)
            _camera_y         = int(((yanchor-.5)*renpy.config.screen_height*_LAYER_Z)/_FOCAL_LENGTH)
            _camera_z         = int(z)
            _camera_rotate    = int(rotate)

    def _camera_trans(tran, st, at, camera_check_points, layer_check_points, layer_loop, x_loop, y_loop, z_loop, rotate_loop, subpixel, layer, x_express, y_express, z_express, rotate_express):
        # camera_check_points = (z, r, xanchor, yanchor, duration, warper)
        # layer_check_points = (layer_z, duration, warper)
        from math import sin, pi
        from random import random
        tran.xpos    = .5 
        tran.ypos    = .5
        tran.subpixel = subpixel
        tran.transform_anchor = True
        tran.xanchor = get_at_time(camera_check_points['xanchor'], st, x_loop)
        tran.yanchor = get_at_time(camera_check_points['yanchor'], st, y_loop)
        z = get_at_time(camera_check_points['z'], st, z_loop)
        tran.rotate = get_at_time(camera_check_points['rotate'], st, rotate_loop)
        layer_z = get_at_time(layer_check_points, st, layer_loop)
        if x_express:
            tran.xanchor += _FOCAL_LENGTH*x_express(st, at)/(renpy.config.screen_width *_LAYER_Z)
        if y_express:
            tran.yanchor += _FOCAL_LENGTH*y_express(st, at)/(renpy.config.screen_height *_LAYER_Z)
        if z_express:
            z += z_express(st, at)
        if rotate_express:
            tran.rotate += rotate_express(st, at)
        distance = float(layer_z - z)
        if distance == 0:
            distance = .1
        if distance >= 0:
            tran.alpha = 1
            tran.zoom = _LAYER_Z / distance
        else:
            tran.alpha = 0
        return .005

    def get_at_time(check_points, time, loop):
        # check_points = ((value, time, warper)...)
        if loop and check_points[-1][1]:
            time %= check_points[-1][1]

        for i in xrange(1, len(check_points)):
            checkpoint = check_points[i][1]
            pre_checkpoint = check_points[i-1][1]
            if time < checkpoint:
                start = check_points[i-1]
                goal = check_points[i]
                if checkpoint != pre_checkpoint:
                    g = renpy.atl.warpers[goal[2]]((time - pre_checkpoint) / float(checkpoint - pre_checkpoint))
                else:
                    g = 1.

                return g*(goal[0]-start[0])+start[0]
        else:
            return check_points[-1][0]

    # def get_camera_coordinate(tran, z, layer, layer_z): #_3d_layers can't rollback?
    #     global _camera_x, _camera_y, _camera_z, _camera_rotate
    #     _camera_x         = int(((tran.xanchor-.5)*renpy.config.screen_width*_LAYER_Z)/_FOCAL_LENGTH)
    #     _camera_y         = int(((tran.yanchor-.5)*renpy.config.screen_height*_LAYER_Z)/_FOCAL_LENGTH)
    #     _camera_z         = int(z)
    #     _camera_rotate    = int(tran.rotate)
    #     _3d_layers[layer] = int(layer_z)

init 1600 python:
    if not _3d_layers:
        register_3d_layer('master')

screen _action_editor(tab="images", layer="master", name="", time=0):
    key "game_menu" action Return()
    key "rollback"    action _viewers.rollback
    key "rollforward" action _viewers.rollforward
    if _viewers.sorted_keyframes:
        key "K_SPACE" action [SensitiveIf(_viewers.sorted_keyframes), Function(_viewers.camera_viewer.play, play=True), Function(_viewers.transform_viewer.play, play=True), Hide("_action_editor"), Show("_action_editor", tab=tab, layer=layer, name=name, time=_viewers.sorted_keyframes[-1]), renpy.restart_interaction]
    else:
        key "K_SPACE" action [SensitiveIf(_viewers.sorted_keyframes), Function(_viewers.camera_viewer.play, play=True), Function(_viewers.transform_viewer.play, play=True), Hide("_action_editor"), Show("_action_editor", tab=tab, layer=layer, name=name), renpy.restart_interaction]
    if _viewers.fps_keymap:
        key "s" action Function(_viewers.camera_viewer.y_changed, _camera_y+100+_viewers.camera_viewer.range_camera_pos)
        key "w" action Function(_viewers.camera_viewer.y_changed, _camera_y-100+_viewers.camera_viewer.range_camera_pos)
        key "a" action Function(_viewers.camera_viewer.x_changed, _camera_x-100+_viewers.camera_viewer.range_camera_pos)
        key "d" action Function(_viewers.camera_viewer.x_changed, _camera_x+100+_viewers.camera_viewer.range_camera_pos)
        key "S" action Function(_viewers.camera_viewer.y_changed, _camera_y+1000+_viewers.camera_viewer.range_camera_pos)
        key "W" action Function(_viewers.camera_viewer.y_changed, _camera_y-1000+_viewers.camera_viewer.range_camera_pos)
        key "A" action Function(_viewers.camera_viewer.x_changed, _camera_x-1000+_viewers.camera_viewer.range_camera_pos)
        key "D" action Function(_viewers.camera_viewer.x_changed, _camera_x+1000+_viewers.camera_viewer.range_camera_pos)
    else:
        key "j" action Function(_viewers.camera_viewer.y_changed, _camera_y+100+_viewers.camera_viewer.range_camera_pos)
        key "k" action Function(_viewers.camera_viewer.y_changed, _camera_y-100+_viewers.camera_viewer.range_camera_pos)
        key "h" action Function(_viewers.camera_viewer.x_changed, _camera_x-100+_viewers.camera_viewer.range_camera_pos)
        key "l" action Function(_viewers.camera_viewer.x_changed, _camera_x+100+_viewers.camera_viewer.range_camera_pos)
        key "J" action Function(_viewers.camera_viewer.y_changed, _camera_y+1000+_viewers.camera_viewer.range_camera_pos)
        key "K" action Function(_viewers.camera_viewer.y_changed, _camera_y-1000+_viewers.camera_viewer.range_camera_pos)
        key "H" action Function(_viewers.camera_viewer.x_changed, _camera_x-1000+_viewers.camera_viewer.range_camera_pos)
        key "L" action Function(_viewers.camera_viewer.x_changed, _camera_x+1000+_viewers.camera_viewer.range_camera_pos)

    if time:
        timer time+1 action Function(_viewers.change_time, _viewers.time)
    $state={k: v for dic in [_viewers.transform_viewer.state_org[layer], _viewers.transform_viewer.state[layer]] for k, v in dic.items()}

    if _viewers.default_rot and store._first_load:
        $store._first_load = False
        on "show" action Show("_rot")

    frame:
        background "#0006"
        if time:
            at _delay_show(time + 1)
        vbox:

            hbox:
                style_group "action_editor_a"
                textbutton _("time: [_viewers.time:>.2f] s") action Function(_viewers.edit_time)
                textbutton _("<") action Function(_viewers.prev_time)
                textbutton _(">") action Function(_viewers.next_time)
                bar adjustment ui.adjustment(range=7.0, value=_viewers.time, changed=_viewers.change_time) xalign 1. yalign .5
            hbox:
                style_group "action_editor_a"
                hbox:
                    textbutton _("default warper") action _viewers.select_default_warper
                    textbutton _("rot") action [SelectedIf(renpy.get_screen("_rot")), If(renpy.get_screen("_rot"), true=Hide("_rot"), false=Show("_rot"))]
                    textbutton _("hide") action HideInterface()
                    # textbutton _("window") action _viewers.AddWindow() #renpy.config.empty_window
                    if _viewers.sorted_keyframes:
                        textbutton _("play") action [SensitiveIf(_viewers.sorted_keyframes), Function(_viewers.camera_viewer.play, play=True), Function(_viewers.transform_viewer.play, play=True), Hide("_action_editor"), Show("_action_editor", tab=tab, layer=layer, name=name, time=_viewers.sorted_keyframes[-1]), renpy.restart_interaction]
                    else:
                        textbutton _("play") action [SensitiveIf(_viewers.sorted_keyframes), Function(_viewers.camera_viewer.play, play=True), Function(_viewers.transform_viewer.play, play=True), Hide("_action_editor"), Show("_action_editor", tab=tab, layer=layer, name=name), renpy.restart_interaction]
                    textbutton _("clipboard") action Function(_viewers.put_clipboard)
                hbox:
                    xalign 1.
                    textbutton _("close") action Return()
            hbox:
                style_group "action_editor_a"
                textbutton _("clear keyframes") action [SensitiveIf(_viewers.sorted_keyframes), Function(_viewers.clear_keyframes), renpy.restart_interaction]
                textbutton _("remove keyframes") action [SensitiveIf(_viewers.time in _viewers.sorted_keyframes), Function(_viewers.remove_keyframes, _viewers.time), renpy.restart_interaction]
                textbutton _("move keyframes") action [SensitiveIf(_viewers.time in _viewers.sorted_keyframes), SetField(_viewers, "moved_time", _viewers.time), Show("_move_keyframes")]
                textbutton _("last moves") action [SensitiveIf(_last_camera_arguments), Function(_viewers.last_moves), renpy.restart_interaction]
            null height 10
            hbox:
                style_group "action_editor_a"
                xfill False
                textbutton _("Images") action [SelectedIf(tab == "images"), Show("_action_editor", tab="images")]
                textbutton _("2D Camera") action [SensitiveIf(_3d_layers.keys() == ["master"]), SelectedIf(tab == "2D Camera"), Show("_action_editor", tab="2D Camera")]
                textbutton _("3D Layers") action [SelectedIf(tab == "3D Layers"), Show("_action_editor", tab="3D Layers")]
                textbutton _("3D Camera") action [SelectedIf(tab == "3D Camera"), Show("_action_editor", tab="3D Camera")]
            if tab == "images":
                hbox:
                    style_group "action_editor_a"
                    for l in config.layers:
                        if l not in ["screens", "transient", "overlay"]:
                            textbutton "[l]" action [SelectedIf(l == layer), Show("_action_editor", tab=tab, layer=l)]
                hbox:
                    style_group "action_editor_a"
                    textbutton _("+") action Function(_viewers.transform_viewer.add_image, layer)
                    for n in state:
                        textbutton "{}".format(n.split()[0]) action [SelectedIf(n == name), Show("_action_editor", tab=tab, layer=layer, name=n)]

                if name in state:
                    for p, d in _viewers.transform_viewer.props:
                        $prop = _viewers.transform_viewer.get_property(layer, name.split()[0], p)
                        $ f = _viewers.transform_viewer.generate_changed(layer, name, p)
                        if p not in _viewers.transform_viewer.force_float and ((state[name][p] is None and isinstance(d, int)) or isinstance(state[name][p], int)):
                            hbox:
                                style_group "action_editor"
                                textbutton "[p]" action [SensitiveIf((name, layer, p) in _viewers.all_keyframes), SelectedIf(_viewers.keyframes_exist((name, layer, p))), Show("_edit_keyframe", k=(name, layer, p), int=True, loop=name+"_"+layer+"_"+p+"_loop")]
                                textbutton "[prop]" action Function(_viewers.transform_viewer.edit_value, f, True, default=prop) alternate Function(_viewers.transform_viewer.reset, name, layer, p)
                                bar adjustment ui.adjustment(range=_viewers.transform_viewer.int_range*2, value=prop+_viewers.transform_viewer.int_range, page=1, changed=f) xalign 1. yalign .5
                        else:
                            hbox:
                                style_group "action_editor"
                                textbutton "[p]" action [SensitiveIf((name, layer, p) in _viewers.all_keyframes), SelectedIf(_viewers.keyframes_exist((name, layer, p))), Show("_edit_keyframe", k=(name, layer, p), loop=name+"_"+layer+"_"+p+"_loop")]
                                textbutton "[prop:>.2f]" action Function(_viewers.transform_viewer.edit_value, f, False, default=prop) alternate Function(_viewers.transform_viewer.reset, name, layer, p)
                                bar adjustment ui.adjustment(range=_viewers.transform_viewer.float_range*2, value=prop+_viewers.transform_viewer.float_range, page=.05, changed=f) xalign 1. yalign .5
            elif tab == "3D Camera" or tab == "2D Camera":
                if _3d_layers.keys() == ["master"] and tab == "3D Camera":
                    label _("Please register 3D layers")
                else:
                    hbox:
                        style_group "action_editor"
                        textbutton "x" action [SensitiveIf("_camera_x" in _viewers.all_keyframes), SelectedIf(_viewers.keyframes_exist("_camera_x")), Show("_edit_keyframe", k="_camera_x", loop="_camera_x_loop")]
                        textbutton "[_camera_x: >5]" action Function(_viewers.camera_viewer.edit_value, _viewers.camera_viewer.x_changed, _viewers.camera_viewer.range_camera_pos, default=_camera_x) alternate [Function(camera_move, _viewers.camera_viewer._camera_x, _camera_y, _camera_z, _camera_rotate), renpy.restart_interaction]
                        bar adjustment ui.adjustment(range=_viewers.camera_viewer.range_camera_pos*2, value=_camera_x+_viewers.camera_viewer.range_camera_pos, page=1, changed=_viewers.camera_viewer.x_changed) xalign 1. yalign .5
                    hbox:
                        style_group "action_editor"
                        textbutton "y" action [SensitiveIf("_camera_y" in _viewers.all_keyframes), SelectedIf(_viewers.keyframes_exist("_camera_y")), Show("_edit_keyframe", k="_camera_y", loop="_camera_y_loop")]
                        textbutton "[_camera_y: >5]" action Function(_viewers.camera_viewer.edit_value, _viewers.camera_viewer.y_changed, _viewers.camera_viewer.range_camera_pos, default=_camera_y) alternate [Function(camera_move, _camera_x, _viewers.camera_viewer._camera_y, _camera_z, _camera_rotate), renpy.restart_interaction]
                        bar adjustment ui.adjustment(range=_viewers.camera_viewer.range_camera_pos*2, value=_camera_y+_viewers.camera_viewer.range_camera_pos, page=1, changed=_viewers.camera_viewer.y_changed) xalign 1. yalign .5
                    hbox:
                        style_group "action_editor"
                        textbutton "z" action [SensitiveIf("_camera_z" in _viewers.all_keyframes), SelectedIf(_viewers.keyframes_exist("_camera_z")), Show("_edit_keyframe", k="_camera_z", loop="_camera_z_loop")]
                        textbutton "[_camera_z: >5]" action Function(_viewers.camera_viewer.edit_value, _viewers.camera_viewer.z_changed, _viewers.camera_viewer.range_camera_pos, default=_camera_z) alternate [Function(camera_move, _camera_x, _camera_y, _viewers.camera_viewer._camera_z, _camera_rotate), renpy.restart_interaction]
                        bar adjustment ui.adjustment(range=_viewers.camera_viewer.range_camera_pos*2, value=_camera_z+_viewers.camera_viewer.range_camera_pos, page=1, changed=_viewers.camera_viewer.z_changed) xalign 1. yalign .5
                    hbox:
                        style_group "action_editor"
                        textbutton "rotate" action [SensitiveIf("_camera_rotate" in _viewers.all_keyframes), SelectedIf(_viewers.keyframes_exist("_camera_rotate")), Show("_edit_keyframe", k="_camera_rotate", loop="_camera_rotate_loop")]
                        textbutton "[_camera_rotate: >5]" action Function(_viewers.camera_viewer.edit_value, _viewers.camera_viewer.r_changed, _viewers.camera_viewer.range_rotate, default=_camera_rotate) alternate [Function(camera_move, _camera_x, _camera_y, _camera_z, _viewers.camera_viewer._camera_rotate), renpy.restart_interaction]
                        bar adjustment ui.adjustment(range=_viewers.camera_viewer.range_rotate*2, value=_camera_rotate+_viewers.camera_viewer.range_rotate, page=1, changed=_viewers.camera_viewer.r_changed) xalign 1. yalign .5
            elif tab == "3D Layers":
                if _3d_layers.keys() == ["master"]:
                    label _("Please register 3D layers")
                else:
                    for layer in sorted(_3d_layers.keys()):
                        hbox:
                            style_group "action_editor"
                            textbutton "[layer]" action [SensitiveIf("layer "+layer in _viewers.all_keyframes), SelectedIf(_viewers.keyframes_exist("layer "+layer)), SetField(_viewers, "moved_time", _viewers.time), Show("_edit_keyframe", k="layer "+layer, loop=layer+"_loop")]
                            textbutton "{}".format(_3d_layers[layer]) action Function(_viewers.camera_viewer.edit_value, _viewers.camera_viewer.generate_layer_z_changed(layer), 0, default=_3d_layers[layer]) alternate [Function(layer_move, layer, _viewers.camera_viewer._3d_layers[layer]), renpy.restart_interaction]
                            bar adjustment ui.adjustment(range=_viewers.camera_viewer.range_layer_z, value=_3d_layers[layer], page=1, changed=_viewers.camera_viewer.generate_layer_z_changed(layer)) xalign 1. yalign .5
            hbox:
                style_group "action_editor"
                xfill False
                xalign 1.
                if tab == "images":
                    if name:
                        textbutton _("remove") action [SensitiveIf(name in _viewers.transform_viewer.state[layer]), Show("_action_editor", tab=tab, layer=layer), Function(renpy.hide, name, layer), Function(_viewers.transform_viewer.state[layer].pop, name, layer), Function(_viewers.transform_viewer.remove_keyframes, name=name, layer=layer), _viewers.sort_keyframes]
                        textbutton _("clipboard") action Function(_viewers.transform_viewer.put_show_clipboard, name, layer)
                    textbutton _("reset") action [_viewers.transform_viewer.image_reset, renpy.restart_interaction]
                elif tab == "2D Camera":
                    textbutton _("clipboard") action Function(_viewers.camera_viewer.put_clipboard, True)
                    textbutton _("reset") action [_viewers.camera_viewer.camera_reset, renpy.restart_interaction]
                elif tab == "3D Layers":
                    textbutton _("clipboard") action Function(_viewers.camera_viewer.put_clipboard, False)
                    textbutton _("reset") action [_viewers.camera_viewer.layer_reset, renpy.restart_interaction]
                elif tab == "3D Camera":
                    textbutton _("clipboard") action Function(_viewers.camera_viewer.put_clipboard, True)
                    textbutton _("reset") action [_viewers.camera_viewer.camera_reset, renpy.restart_interaction]

    if time:
        add _viewers.dragged at _delay_show(time + 1)
    else:
        add _viewers.dragged

init -1600:
    style action_editor_button size_group "action_editor"
    style action_editor_button idle_background None
    style action_editor_button insensitive_background None
    style action_editor_button_text color "#aaa"
    style action_editor_button_text selected_color "#fff"
    style action_editor_button_text insensitive_color "#777"
    style action_editor_a_button take action_editor_button
    style action_editor_a_button size_group None
    style action_editor_a_button_text take action_editor_button_text

    style action_editor_label xminimum 110
    style action_editor_vbox xfill True

screen _input_screen(message="type value", default=""):
    modal True
    key "game_menu" action Return("")

    frame:
        background "#0006"
        style_group "input_screen"

        has vbox

        label message

        hbox:
            input default default

init -1600:
    style input_screen_frame xfill True ypos .1 xmargin .05 ymargin .05
    style input_screen_vbox xfill True spacing 30
    style input_screen_label xalign .5
    style input_screen_hbox  xalign .5

transform _delay_show(time):
    alpha 0
    pause time
    alpha 1

screen _rot(): #show rule of thirds
    for i in range(1, 3):
        add Solid("#F00", xsize=config.screen_width, ysize=1, ypos=config.screen_height*i/3)
        add Solid("#F00", xsize=1, ysize=config.screen_height, xpos=config.screen_width*i/3)

screen _warper_selecter(current_warper=""):
    modal True
    key "game_menu" action Return("")

    frame:
        background "#0006"
        style_group "warper_selecter"

        has vbox

        label _("Select a warper function")
        viewport:
            mousewheel True
            edgescroll (100, 100)
            xsize config.screen_width-500
            ysize config.screen_height-200
            scrollbars "vertical"
            vbox:
                for warper in sorted(renpy.atl.warpers.keys()):
                    textbutton warper action [SelectedIf((_viewers.warper == warper and not current_warper) or warper == current_warper), Return(warper)] hovered Show("_warper_graph", warper=warper) unhovered Hide("_warper")
        hbox:
            textbutton _("add") action OpenURL("http://renpy.org/wiki/renpy/doc/cookbook/Additional_basic_move_profiles")
            textbutton _("close") action Return("")

screen _warper_graph(warper):
    $ t=120
    $ length=300
    $ xpos=config.screen_width-400
    $ ypos=100
    # add Solid("#000", xsize=3, ysize=1.236*length, xpos=xpos+length/2, ypos=length/2+xpos, rotate=45, anchor=(.5, .5)) 
    add Solid("#CCC", xsize=length, ysize=length, xpos=xpos, ypos=ypos ) 
    add Solid("#000", xsize=length, ysize=3, xpos=xpos, ypos=length+ypos ) 
    add Solid("#000", xsize=length, ysize=3, xpos=xpos, ypos=ypos ) 
    add Solid("#000", xsize=3, ysize=length, xpos=xpos+length, ypos=ypos)
    add Solid("#000", xsize=3, ysize=length, xpos=xpos, ypos=ypos)
    for i in range(1, t):
        $ysize=int(length*renpy.atl.warpers[warper](i/float(t)))
        if ysize >= 0:
            add Solid("#000", xsize=length/t, ysize=ysize, xpos=xpos+i*length/t, ypos=length+ypos, yanchor=1.) 
        else:
            add Solid("#000", xsize=length/t, ysize=-ysize, xpos=xpos+i*length/t, ypos=length+ypos-ysize, yanchor=1.) 

screen _move_keyframes:
    modal True
    key "game_menu" action Hide("_move_keyframes")
    frame:
        background "#0006"
        has vbox
        textbutton _("time: [_viewers.moved_time:>.2f] s") action Function(_viewers.edit_moved_time)
        bar adjustment ui.adjustment(range=7.0, value=_viewers.moved_time, changed=renpy.curry(_viewers.move_keyframes)(old=_viewers.moved_time)) xalign 1. yalign .5
        textbutton _("close") action Hide("_move_keyframes") xalign .98

# _edit_keyframe((name, layer), "xpos")
# _edit_keyframe(_camera_x)
screen _edit_keyframe(k, int=False, loop=None):
    $check_points = _viewers.all_keyframes[k]
    modal True
    key "game_menu" action Hide("_edit_keyframe")
    frame:
        background "#0009"
        xfill True
        has vbox
        label _("KeyFrames") xalign .5
        for v, t, w in check_points:
            if t != 0:
                hbox:
                    textbutton _("x") action [Function(_viewers.remove_keyframe, remove_time=t, k=k), renpy.restart_interaction] background None
                    textbutton _("{}".format(v)) action Function(_viewers.edit_the_value, check_points=check_points, old=t, value_org=v, int=int)
                    textbutton _("{}".format(w)) action Function(_viewers.edit_the_warper, check_points=check_points, old=t, value_org=w)
                    textbutton _("[t:>.2f] s") action Function(_viewers.edit_moved_time, check_points=check_points, old=t)
                    bar adjustment ui.adjustment(range=7.0, value=t, changed=renpy.curry(_viewers.move_keyframe)(old=t, check_points=check_points)) xalign 1. yalign .5
        hbox:
            textbutton _("loop") action ToggleDict(_viewers.loops, loop)
            if k[:8] == "_camera_":
                textbutton _("expression") action Function(_viewers.edit_expression, k)
            textbutton _("close") action Hide("_edit_keyframe") xalign .98

init -1098 python:
    # Added keymap
    config.underlay.append(renpy.Keymap(
        self_voicing = Preference("self voicing", "toggle"),
        action_editor = _viewers.action_editor,
        image_viewer = _open_image_viewer,
        ))


init 1100 python:
    config.locked = False
    config.keymap["action_editor"] = ['P']
    config.keymap["image_viewer"] = ['U']
    config.locked = True


init -1600 python in _viewers:
    default_rot = False
    # FPS(wasd) or vim(hjkl)
    fps_keymap = False
    default_warper = "linear"
    ##########################################################################
    # TransformViewer
    class TransformViewer(object):
        def __init__(self):

            self.int_range = 1500
            self.float_range = 7.0
            # layer->tag->property->value
            self.state_org = {}
            self.state = {}
            # ((property, default)...), default is used when property can't be got.
            self.props = (
            ("xpos", 0.), 
            ("ypos", 0.), 
            ("xanchor", 0.), 
            ("yanchor", 0.), 
            # ("xoffset", 0.), 
            # ("yoffset", 0.), 
            ("xzoom", 1.), 
            ("yzoom", 1.), 
            ("zoom", 1.), 
            ("rotate", 0,),
            ("alpha", 1.), 
            ("additive", 0.), 
            )
            self.force_float = ["zoom", "xzoom", "yzoom", "alpha", "additive"]

        def init(self):
            if not renpy.config.developer:
                return
            sle = renpy.game.context().scene_lists
            # back up for reset()
            for layer in renpy.config.layers:
                self.state_org[layer] = {}
                self.state[layer] = {}
                for tag in sle.layers[layer]:
                    if not tag[0]:
                        break
                    d = sle.get_displayable_by_tag(layer, tag[0])
                    if isinstance(d, renpy.display.screen.ScreenDisplayable):
                        break
                    pos = renpy.get_placement(d)
                    state = getattr(d, "state", None)


                    string = ""
                    for e in tag.name:
                        string += str(e) + " "
                    name = string[:-1]
                    self.state_org[layer][name] = {}
                    for p in ["xpos", "ypos", "xanchor", "yanchor"]:
                        self.state_org[layer][name][p] = getattr(pos, p, None)
                    for p, d in self.props:
                        if p not in self.state_org[layer][name]:
                            self.state_org[layer][name][p] = getattr(state, p, None)

        def reset(self, name, layer, prop):
            state={k: v for dic in [self.state_org[layer], self.state[layer]] for k, v in dic.items()}[name][prop]
            kwargs = {}
            for p, d in self.props:
                value = self.get_property(layer, name.split()[0], p, False)
                if value is not None:
                    kwargs[p] = value
                elif p != "rotate":
                    kwargs[p] = d
            kwargs[prop] = state
            renpy.show(name, [renpy.store.Transform(**kwargs)], layer=layer)
            renpy.restart_interaction()

        def image_reset(self):
            for layer in renpy.config.layers:
                for name, props in {k: v for dic in [self.state_org[layer], self.state[layer]] for k, v in dic.items()}.iteritems():
                    for prop in props:
                        self.reset(name, layer, prop)

        def set_keyframe(self, layer, name, prop, value):

            keyframes = all_keyframes.get((name, layer, prop), [])
            if keyframes:
                for i, (v, t, w) in enumerate(keyframes):
                    if time < t:
                        keyframes.insert(i, (value, time, warper))
                        break
                    elif time == t:
                        keyframes[i] = ( value, time, warper)
                        break
                else:
                    keyframes.append((value, time, warper))
            else:
                if time == 0:
                    all_keyframes[(name, layer, prop)] = [(value, time, warper)]
                else:
                    org = {k: v for dic in [self.state_org[layer], self.state[layer]] for k, v in dic.items()}[name][prop]
                    all_keyframes[(name, layer, prop)] = [(org, 0, None), (value, time, warper)]
            sort_keyframes()

        def play(self, play):
            for layer in renpy.config.layers:
                for name in {k: v for dic in [self.state_org[layer], self.state[layer]] for k, v in dic.items()}:
                    check_points = {}
                    for prop, d in self.props:
                        if (name, layer, prop) in all_keyframes:
                            check_points[prop] = all_keyframes[(name, layer, prop)]
                    if not check_points: # ビューワー上でのアニメーション(フラッシュ等)の誤動作を抑制
                        continue
                    loop = {prop+"_loop": loops[name+"_"+layer+"_"+prop+"_loop"] for prop, d in self.props}
                    if play:
                        renpy.show(name, [renpy.store.Transform(function=renpy.curry(self.transform)(check_points=check_points, loop=loop))], layer=layer)
                    else:
                        # check_points = { prop: ( (value, time, warper).. ) }
                        kwargs = {}
                        kwargs.subpixel = True
                        # kwargs.transform_anchor = True
                        st = renpy.store._viewers.time

                        for p, cs in check_points.items():
                            time = st
                            if loop[p+"_loop"] and cs[-1][1]:
                                time = time % cs[-1][1]

                            for i in xrange(1, len(cs)):
                                checkpoint = cs[i][1]
                                pre_checkpoint = cs[i-1][1]
                                if time < checkpoint:
                                    start = cs[i-1]
                                    goal = cs[i]
                                    if checkpoint != pre_checkpoint:
                                        g = renpy.atl.warpers[goal[2]]((time - pre_checkpoint) / float(checkpoint - pre_checkpoint))
                                    else:
                                        g = 1.
                                    for p2, d in self.props:
                                        if p2 == p:
                                            default = d
                                    if goal[0] is not None:
                                        if isinstance(goal[0], int) and p not in self.force_float:
                                            if start[0] is None:
                                                v = g*(goal[0]-default)+default
                                            else:
                                                v = g*(goal[0]-start[0])+start[0]
                                            v = int(v)
                                        else:
                                            if start[0] is None:
                                                v = g*(goal[0]-default)+default
                                            else:
                                                v = g*(goal[0]-start[0])+start[0]
                                        kwargs[p] = v
                                    break
                            else:
                                kwargs[p] = cs[-1][0]

                        renpy.show(name, [renpy.store.Transform(**kwargs)], layer=layer)

        def transform(self, tran, st, at, check_points, loop, subpixel=True):
            # check_points = { prop: [ (value, time, warper).. ] }
            tran.subpixel = subpixel
            # tran.transform_anchor = True

            for p, cs in check_points.items():
                time = st
                if loop[p+"_loop"] and cs[-1][1]:
                    time = st % cs[-1][1]

                for i in xrange(1, len(cs)):
                    checkpoint = cs[i][1]
                    pre_checkpoint = cs[i-1][1]
                    if time < checkpoint:
                        start = cs[i-1]
                        goal = cs[i]
                        if checkpoint != pre_checkpoint:
                            g = renpy.atl.warpers[goal[2]]((time - pre_checkpoint) / float(checkpoint - pre_checkpoint))
                        else:
                            g = 1.
                        for p2, d in self.props:
                            if p2 == p:
                                default = d
                        if goal[0] is not None:
                            if isinstance(goal[0], int) and p not in self.force_float:
                                if start[0] is None:
                                    v = g*(goal[0]-default)+default
                                else:
                                    v = g*(goal[0]-start[0])+start[0]
                                v = int(v)
                            else:
                                if start[0] is None:
                                    v = g*(goal[0]-default)+default
                                else:
                                    v = g*(goal[0]-start[0])+start[0]
                            setattr(tran, p, v)
                        break
                else:
                    setattr(tran, p, cs[-1][0])
            return .005


        def generate_changed(self, layer, name, prop):
            state={k: v for dic in [self.state_org[layer], self.state[layer]] for k, v in dic.items()}[name][prop]
            def changed(v):
                kwargs = {}
                for p, d in self.props:
                    value = self.get_property(layer, name.split()[0], p, False)
                    if value is not None:
                        kwargs[p] = value
                    elif p != "rotate":
                        kwargs[p] = d
                    if p == prop:
                        default = d
                if prop not in self.force_float and ( (state is None and isinstance(default, int)) or isinstance(state, int) ):
                    kwargs[prop] = v - self.int_range
                else:
                    kwargs[prop] = round(v -self.float_range, 2)

                self.set_keyframe(layer, name, prop, kwargs[prop])
                renpy.show(name, [renpy.store.Transform(**kwargs)], layer=layer)
                renpy.restart_interaction()
            return changed

        def get_property(self, layer, tag, prop, default=True):
            sle = renpy.game.context().scene_lists
            # if tag in self.state[layer]:
            #     #TODO
            #     default = True
            if tag:
                d = sle.get_displayable_by_tag(layer, tag)
                pos = renpy.get_placement(d)
                state = getattr(pos, prop, None)
                if state is None:
                    state = getattr(getattr(d, "state", None), prop, None)
                if state is None and default:
                    for p, d in self.props:
                        if p == prop:
                            state = d
                return state
            return None

        def put_show_clipboard(self, name, layer):
            string = """
    show %s onlayer %s""" % (name, layer)
            for p, d in self.props:
                value = self.get_property(layer, name.split()[0], p)
                if value != d:
                    if string.find(":") < 0:
                        string += ":\n        "
                    string += "%s %s " % (p, value)
            try:
                from pygame import scrap, locals
                scrap.put(locals.SCRAP_TEXT, string)
            except:
                renpy.notify(_("Can't open clipboard"))
            else:
                renpy.notify(__('Placed \n"%s"\n on clipboard') % string)

        def edit_value(self, function, int=False, default=""):
            v = renpy.invoke_in_new_context(renpy.call_screen, "_input_screen", default=default)
            if v:
                try:
                    if int:
                        v = renpy.python.py_eval(v) + self.int_range
                    else:
                        v = renpy.python.py_eval(v) + self.float_range
                    function(v)
                except:
                    renpy.notify(_("Please type value"))

        def add_image(self, layer):
            default = ()
            while True:
                name = renpy.invoke_in_new_context(renpy.call_screen, "_image_selecter", default=default)
                if isinstance(name, tuple): #press button
                    for n in renpy.display.image.images:
                        if set(n) == set(name):
                            string=""
                            for e in n:
                                string += e + " "
                            self.state[layer][string] = {}
                            renpy.show(string, layer=layer)
                            for p, d in self.props:
                                self.state[layer][string][p] = self.get_property(layer, string.split()[0], p, False)
                            all_keyframes[(string, layer, "xpos")] = [(self.state[layer][string]["xpos"], 0, None)]
                            remove_list = [n_org for n_org in self.state_org[layer] if n_org.split()[0] == n[0]]
                            for n_org in remove_list:
                                del self.state_org[layer][n_org]
                                for k in [k for k in all_keyframes if isinstance(k, tuple) and k[0] == n_org and k[1] == layer]:
                                    del all_keyframes[k]
                            sort_keyframes()
                            renpy.show_screen("_action_editor", tab="images", layer=layer, name=string)
                            return
                    else:
                        default = name
                elif name: #from input text
                    # for n in renpy.display.image.images: #テキスト入力からはいきなり表示しないようにする。
                    #     if set(n) == set(name.split()):
                    #         self.state[layer][name] = {}
                    #         renpy.show(name, layer=layer)
                    #         for p, d in self.props:
                    #             self.state[layer][name][p] = self.get_property(layer, name.split()[0], p, False)
                    #         all_keyframes[(name, layer, "xpos")] = [(self.state[layer][name]["xpos"], 0, None)]
                    #         remove_list = [n_org for n_org in self.state_org[layer] if n_org.split()[0] == n[0]]
                    #         for n_org in remove_list:
                    #             del self.state_org[layer][n_org]
                    #             transform_viewer.remove_keyframes(n_org, layer)
                    #         sort_keyframes()
                    #         renpy.show_screen("_action_editor", tab="images", layer=layer, name=name)
                    #         return
                    default = tuple(name.split())
                else:
                    renpy.notify(_("Please type image name"))
                    return

        def remove_keyframes(self, name, layer):
            for k in [k for k in all_keyframes if isinstance(k, tuple) and k[0] == name and k[1] == layer]:
                del all_keyframes[k]
    transform_viewer = TransformViewer()

    ##########################################################################
    # CameraViewer
    class CameraViewer(object):

        def __init__(self):
            self.range_camera_pos   = 6000
            self.range_rotate       = 360
            self.range_layer_z   = 10000

        def init(self):
            if not renpy.config.developer:
                return
            self._camera_x = renpy.store._camera_x
            self._camera_y = renpy.store._camera_y
            self._camera_z = renpy.store._camera_z
            self._camera_rotate = renpy.store._camera_rotate
            self._3d_layers = renpy.store._3d_layers.copy()

        def camera_reset(self):
            renpy.store.camera_move(self._camera_x, self._camera_y, self._camera_z, self._camera_rotate)
            renpy.restart_interaction()

        def layer_reset(self):
            for layer in renpy.store._3d_layers:
                renpy.store.layer_move(layer, self._3d_layers[layer])
            renpy.restart_interaction()

        def x_changed(self, v):
            v=int(v)
            renpy.store.camera_move(v - self.range_camera_pos, renpy.store._camera_y, renpy.store._camera_z, renpy.store._camera_rotate)
            self.set_camera_keyframe("_camera_x", v-self.range_camera_pos)
            renpy.restart_interaction()

        def y_changed(self, v):
            v=int(v)
            renpy.store.camera_move(renpy.store._camera_x, v - self.range_camera_pos, renpy.store._camera_z, renpy.store._camera_rotate)
            self.set_camera_keyframe("_camera_y", v-self.range_camera_pos)
            renpy.restart_interaction()

        def z_changed(self, v):
            v=int(v)
            renpy.store.camera_move(renpy.store._camera_x, renpy.store._camera_y, v - self.range_camera_pos, renpy.store._camera_rotate)
            self.set_camera_keyframe("_camera_z", v-self.range_camera_pos)
            renpy.restart_interaction()

        def r_changed(self, v):
            v=int(v)
            renpy.store.camera_move(renpy.store._camera_x, renpy.store._camera_y, renpy.store._camera_z, v - self.range_rotate)
            self.set_camera_keyframe("_camera_rotate", v-self.range_camera_pos)
            renpy.restart_interaction()

        def generate_layer_z_changed(self, l):
            def layer_z_changed(v):
                renpy.store.layer_move(l, int(v))
                self.set_layer_keyframe(l)
                renpy.restart_interaction()
            return layer_z_changed

        def put_clipboard(self, camera_tab):
            string = ""
            if camera_tab:
                string = """
    $camera_move(%s, %s, %s, %s, duration=0)""" % (renpy.store._camera_x, renpy.store._camera_y, renpy.store._camera_z, renpy.store._camera_rotate)
            else:
                for layer in renpy.store._3d_layers:
                    string += """
    $layer_move("%s", %s, duration=0)""" % (layer, renpy.store._3d_layers[layer])
            try:
                from pygame import scrap, locals
                scrap.put(locals.SCRAP_TEXT, string)
            except:
                renpy.notify(_("Can't open clipboard"))
            else:
                renpy.notify(__("Placed \n'%s'\n on clipboard") % string)

        def edit_value(self, function, range, default=""):
            v = renpy.invoke_in_new_context(renpy.call_screen, "_input_screen", default=default)
            if v:
                try:
                    function(renpy.python.py_eval(v) + range)
                except:
                    renpy.notify(_("Please type value"))

        def set_camera_keyframe(self, coordinate, value):
            keyframes = all_keyframes.get(coordinate, [])
            if keyframes:
                for i, (v, t, w) in enumerate(keyframes):
                    if time < t:
                        keyframes.insert(i, (value, time, warper))
                        break
                    elif time == t:
                        keyframes[i] = (value, time, warper)
                        break
                else:
                    keyframes.append((value, time, warper))
            else:
                if time == 0:
                    all_keyframes[coordinate] = [(value, time, warper)]
                else:
                    all_keyframes[coordinate] = [(getattr(self, coordinate), 0, None), (value, time, warper)]
            sort_keyframes()

        def set_layer_keyframe(self, layer):
            keyframes = all_keyframes.get("layer "+layer, [])
            if keyframes:
                for i, (v, t, w)  in enumerate(keyframes):
                    if time < t:
                        keyframes.insert(i, (renpy.store._3d_layers[layer], time, warper))
                        break
                    elif time == t:
                        keyframes[i] = (renpy.store._3d_layers[layer], time, warper)
                        break
                else:
                    keyframes.append((renpy.store._3d_layers[layer], time, warper))
            else:
                if time == 0:
                    all_keyframes["layer "+layer] = [(renpy.store._3d_layers[layer], time, warper)]
                else:
                    all_keyframes["layer "+layer] = [(self._3d_layers[layer], 0, None), (renpy.store._3d_layers[layer], time, warper)]
            sort_keyframes()

        def play(self, play):
            camera_check_points = {}
            for coordinate in ["_camera_x", "_camera_y", "_camera_z", "_camera_rotate"]:
                if coordinate in all_keyframes:
                    camera_check_points[coordinate[8:]] = all_keyframes[coordinate]

            layer_check_points = {}
            kwargs = {}
            for layer in renpy.store._3d_layers:
                if "layer "+layer in all_keyframes:
                    layer_check_points[layer] = all_keyframes["layer "+layer]
                kwargs[layer+"_loop"] = loops[layer+"_loop"]
            for coordinate in ["_camera_x", "_camera_y", "_camera_z", "_camera_rotate"]:
                kwargs[coordinate[8:]+"_loop"] = loops[coordinate+"_loop"]
            for coordinate in ["_camera_x", "_camera_y", "_camera_z", "_camera_rotate"]:
                if expressions[coordinate]:
                    kwargs[coordinate[8:]+"_express"] = renpy.python.py_eval(expressions[coordinate])
            if camera_check_points or layer_check_points:
                renpy.store.all_moves(camera_check_points=camera_check_points, layer_check_points=layer_check_points, play=play, **kwargs)

    camera_viewer = CameraViewer()

    class Dragged(renpy.Displayable):

        def __init__(self, child, **properties):
            super(Dragged, self).__init__(**properties)
            # The child.
            self.child = renpy.displayable(child)
            self.cx = self.x = (0.5 + renpy.store._camera_x/(2.*camera_viewer.range_camera_pos))*renpy.config.screen_width
            self.cy = self.y = (0.5 + renpy.store._camera_y/(2.*camera_viewer.range_camera_pos))*renpy.config.screen_height
            self.dragging = False

        def render(self, width, height, st, at):

            # Create a render from the child.
            child_render = renpy.render(self.child, width, height, st, at)

            # Get the size of the child.
            self.width, self.height = child_render.get_size()

            # Create the render we will return.
            render = renpy.Render(renpy.config.screen_width, renpy.config.screen_height)

            # Blit (draw) the child's render to our render.
            render.blit(child_render, (self.x-self.width/2., self.y-self.height/2.))

            # Return the render.
            return render

        def event(self, ev, x, y, st):

            if renpy.map_event(ev, "mousedown_1"):
                if self.x-self.width/2. <= x and x <= self.x+self.width/2. and self.y-self.height/2. <= y and y <= self.y+self.height/2.:
                    self.dragging = True
            elif renpy.map_event(ev, "mouseup_1"):
                self.dragging = False

            # if x <= 0:
            #     x = 0
            # if renpy.config.screen_width <= x:
            #     x = renpy.config.screen_width
            # if y <= 0:
            #     y = 0
            # if renpy.config.screen_height <= y:
            #     y = renpy.config.screen_height

            if renpy.store._camera_x != int(self.cx) or renpy.store._camera_y != int(self.cy):
                self.x = (0.5 + renpy.store._camera_x/(2.*camera_viewer.range_camera_pos))*renpy.config.screen_width
                self.y = (0.5 + renpy.store._camera_y/(2.*camera_viewer.range_camera_pos))*renpy.config.screen_height
                renpy.redraw(self, 0)

            if self.dragging:
                if self.x != x or self.y != y:
                    self.cx = int(2*camera_viewer.range_camera_pos*( float(x)/renpy.config.screen_width - 0.5))
                    self.cy = int(2*camera_viewer.range_camera_pos*( float(y)/renpy.config.screen_height - 0.5))
                    if self.cx != renpy.store._camera_x:
                        camera_viewer.set_camera_keyframe("_camera_x", self.cx)
                    if self.cy != renpy.store._camera_y:
                        camera_viewer.set_camera_keyframe("_camera_y", self.cy)
                    renpy.store.camera_move(self.cx, self.cy, renpy.store._camera_z, renpy.store._camera_rotate)
                    self.x, self.y = x, y
                    renpy.restart_interaction()
                    renpy.redraw(self, 0)

            # Pass the event to our child.
            # return self.child.event(ev, x, y, st)

        def per_interact(self):
            renpy.redraw(self, 0)

        def visit(self):
            return [ self.child ]
    dragged = Dragged("camera.png")

    ##########################################################################
    from collections import defaultdict
    loops = defaultdict(lambda:False)
    expressions = defaultdict(lambda:None)
    all_keyframes = {}
    time = 0
    moved_time = 0
    sorted_keyframes = []
    warper = default_warper

    def edit_expression(k):
        value = renpy.invoke_in_new_context(renpy.call_screen, "_input_screen", default=expressions[k])
        try:
            result = renpy.python.py_eval(value)(0, 0)
            if isinstance(result, float) or isinstance(result, int):
                expressions[k] = value
            else:
                raise
        except:
            renpy.notify(_("This isn't a valid expression"))
        renpy.restart_interaction()

    def edit_the_value(check_points, old, value_org, int=False):
        value = renpy.invoke_in_new_context(renpy.call_screen, "_input_screen", default=value_org)
        try:
            value = renpy.python.py_eval(value)
            if int:
                value = int(value)
            else:
                value = float(value)
            for i, (v, t, w) in enumerate(check_points):
                if t == old:
                    check_points[i] = (value, t, w)
                    break
        except:
            renpy.notify(_("Please type value"))
        renpy.restart_interaction()

    def edit_the_warper(check_points, old, value_org):
        warper = renpy.invoke_in_new_context(renpy.call_screen, "_warper_selecter", current_warper=value_org)
        if warper:
            for i, (v, t, w) in enumerate(check_points):
                if t == old:
                    check_points[i] = (v, t, warper)
                    break
        renpy.restart_interaction()

    def edit_moved_time(check_points, old):
        v = renpy.invoke_in_new_context(renpy.call_screen, "_input_screen", default=old)
        if v:
            try:
                v = renpy.python.py_eval(v)
                if v < 0:
                    return
                move_keyframe(v, old, check_points)
            except:
                renpy.notify(_("Please type value"))

    def edit_time():
        global time
        v = renpy.invoke_in_new_context(renpy.call_screen, "_input_screen", default=time)
        if v:
            try:
                v = renpy.python.py_eval(v)
                if v < 0:
                    return
                change_time(v)
            except:
                renpy.notify(_("Please type value"))

    def next_time():
        if not sorted_keyframes:
            change_time(0)
            return
        else:
            for i, t in enumerate(sorted_keyframes):
                if time < t:
                    change_time(sorted_keyframes[i])
                    return
            change_time(sorted_keyframes[0])

    def prev_time():
        if not sorted_keyframes:
            change_time(0)
            return
        else:
            for i, t in enumerate(sorted_keyframes):
                if time <= t:
                    change_time(sorted_keyframes[i-1])
                    break
            else:
                change_time(sorted_keyframes[-1])

    def select_default_warper():
        global warper
        v = renpy.invoke_in_new_context(renpy.call_screen, "_warper_selecter")
        if v:
            warper = v

    @renpy.pure
    class ShowImage(renpy.store.Action, renpy.store.DictEquality):
        def __init__(self, default, tag):
            self.string=""
            for e in default:
                self.string += e + " "
            self.string += tag
            self.check = None

        def __call__(self):
            if self.check is None:
                for n in renpy.display.image.images:
                    if set(n) == set(self.string.split()):
                        self.string=""
                        for e in n:
                            self.string += e + " "
                        try:
                            for fn in renpy.display.image.images[n].predict_files():
                                if not renpy.loader.loadable(fn):
                                    self.check = False
                                    break
                            else:
                                self.check = True
                        except:
                            self.check = True #text displayable
            if self.check:
                renpy.show(self.string, at_list=[renpy.store.truecenter], layer="screens", tag="preview")
            else:
                renpy.show("preview", what=renpy.text.text.Text("No files", color="#F00"), at_list=[renpy.store.truecenter], layer="screens")
            renpy.restart_interaction()

        # def get_sensitive(self):
        #     for n in renpy.display.image.images:
        #         if set(n) == set(self.string.split()):
        #             return True
        #     else:
        #         return False
    # @renpy.pure
    # class AddWindow(renpy.store.Action, renpy.store.DictEquality):
    #     def __init__(self):
    #         pass
    #     def __call__(self):
    #         if renpy.shown_window():
    #             renpy.scene("window")
    #         else:
    #             renpy.add_layer("window", below="screens")
    #             renpy.config.empty_window()
    #         renpy.restart_interaction()
    #     def get_selected(self):
    #         if renpy.shown_window():
    #             return True
    #         return False

    def clear_keyframes():
        all_keyframes.clear()
        sorted_keyframes[:]=[]

    def remove_keyframe(remove_time, k):
        remove_list = []
        for (v, t, w) in all_keyframes[k]:
            if t == remove_time:
                if remove_time != 0 or (remove_time == 0 and len(all_keyframes[k]) == 1):
                    remove_list.append((v, t, w))
        for c in remove_list:
            all_keyframes[k].remove(c)
            if not all_keyframes[k]:
                del all_keyframes[k]
        sort_keyframes()
        change_time(time)

    def remove_keyframes(time):
        keylist = [k for k in all_keyframes]
        for k in keylist:
            remove_keyframe(time, k)

    def sort_keyframes():
        global sorted_keyframes
        sorted_keyframes[:] = []
        for keyframes in all_keyframes.values():
            for (v, t, w) in keyframes:
                if t not in sorted_keyframes:
                    sorted_keyframes.append(t)
        sorted_keyframes.sort()

    def move_keyframes(new, old):
        global moved_time
        moved_time = round(new, 2)
        for k, v in all_keyframes.items():
            move_keyframe(new, old, v)
        renpy.restart_interaction()

    def move_keyframe(new, old, check_points):
        new = round(new, 2)
        for i, c in enumerate(check_points):
            if c[1] == old:
                (value, time, warper) = check_points.pop(i)
                for n, (v, t, w) in enumerate(check_points):
                    if new < t:
                        check_points.insert(n, (value, new, warper))
                        break
                    elif new == t:
                        # check_points[n] = (new, (value, new, w))
                        check_points.insert(n, (value, new, warper))
                        break
                else:
                    check_points.append((value, new, warper))
                if old == 0 and new != 0:
                    check_points.insert(0, (value, 0, None))
        sort_keyframes()
        renpy.restart_interaction()

    def keyframes_exist(k):
        if k not in all_keyframes:
            return False
        check_points = all_keyframes[k]
        for c in check_points:
            if c[1] == time:
                return True
        return False

    def change_time(v):
        global time
        time = round(v, 2)
        transform_viewer.play(False)
        camera_viewer.play(False)
        renpy.restart_interaction()

    def rollback():
        renpy.store.camera_move(renpy.store._camera_x, renpy.store._camera_y, renpy.store._camera_z-100, renpy.store._camera_rotate)
        camera_viewer.set_camera_keyframe("_camera_z", renpy.store._camera_z)
        renpy.restart_interaction()

    def rollforward():
        renpy.store.camera_move(renpy.store._camera_x, renpy.store._camera_y, renpy.store._camera_z+100, renpy.store._camera_rotate)
        camera_viewer.set_camera_keyframe("_camera_z", renpy.store._camera_z)
        renpy.restart_interaction()

    def action_editor():
        global time
        if not renpy.config.developer:
            return
        transform_viewer.init()
        camera_viewer.init()
        loops.clear()
        expressions.clear()
        renpy.store._first_load = True
        renpy.invoke_in_new_context(renpy.call_screen, "_action_editor")
        clear_keyframes()
        time = 0
        camera_viewer.layer_reset()
        camera_viewer.camera_reset()

    def last_moves():
        all_keyframes["_camera_x"] = renpy.store._last_camera_arguments[0]["x"]
        all_keyframes["_camera_y"] = renpy.store._last_camera_arguments[0]["y"]
        all_keyframes["_camera_z"] = renpy.store._last_camera_arguments[0]["z"]
        all_keyframes["_camera_rotate"] = renpy.store._last_camera_arguments[0]["rotate"]
        all_keyframes["_camera_z"] = renpy.store._last_camera_arguments[0]["z"]
        for k in renpy.store._last_camera_arguments[1]:
            all_keyframes["layer "+k] = renpy.store._last_camera_arguments[1][k]
        loops["_camera_x_loop"] = renpy.store._last_camera_arguments[2]
        loops["_camera_y_loop"] = renpy.store._last_camera_arguments[3]
        loops["_camera_z_loop"] = renpy.store._last_camera_arguments[4]
        loops["_camera_rotate_loop"] = renpy.store._last_camera_arguments[5]
        expressions["_camera_x"] = renpy.store._last_camera_arguments[6]
        expressions["_camera_y"] = renpy.store._last_camera_arguments[7]
        expressions["_camera_z"] = renpy.store._last_camera_arguments[8]
        expressions["_camera_rotate"] = renpy.store._last_camera_arguments[9]
        for k in renpy.store._last_camera_arguments[10]:
            loops[k] = renpy.store._last_camera_arguments[10][k]
        all_keyframes["_camera_x"].insert(0, (renpy.store._last_camera_arguments[11], 0, None))
        all_keyframes["_camera_y"].insert(0, (renpy.store._last_camera_arguments[12], 0, None))
        all_keyframes["_camera_z"].insert(0, (renpy.store._last_camera_arguments[13], 0, None))
        all_keyframes["_camera_rotate"].insert(0, (renpy.store._last_camera_arguments[14], 0, None))
        for k in renpy.store._last_camera_arguments[1]:
            all_keyframes["layer "+k].insert(0, (renpy.store._last_camera_arguments[15][k], 0, None))
        sort_keyframes()
        change_time(0)

    def put_clipboard():
        camera_check_points = {}
        for coordinate in ["_camera_x", "_camera_y", "_camera_z", "_camera_rotate"]:
            if coordinate in all_keyframes:
                camera_check_points[coordinate[8:]] = all_keyframes[coordinate]
                if len(camera_check_points[coordinate[8:]]) == 1 and camera_check_points[coordinate[8:]][0][0] == getattr(renpy.store._viewers.camera_viewer, coordinate):
                    del camera_check_points[coordinate[8:]]

        layer_check_points = {}
        loop = ""
        expression = ""
        argments = ""
        for layer in renpy.store._3d_layers:
            if "layer "+layer in all_keyframes:
                layer_check_points[layer] = all_keyframes["layer "+layer]
                if len(layer_check_points[layer]) == 1 and layer_check_points[layer][0][0] == camera_viewer._3d_layers[layer]:
                    del layer_check_points[layer]
                if loops[layer+"_loop"]:
                    loop += layer+"_loop=True, "
        for coordinate in ["_camera_x", "_camera_y", "_camera_z", "_camera_rotate"]:
            if loops[coordinate+"_loop"]:
                loop += coordinate[8:]+"_loop=True, "
            if expressions[coordinate]:
                expression += coordinate[8:]+"_express="+expressions[coordinate]+", "
        string = ""

        if camera_check_points:
            argments += "camera_check_points={}, ".format(camera_check_points)
        if layer_check_points:
            argments += "layer_check_points={}, ".format(layer_check_points)
        if expression:
            argments += expression
        if loop:
            argments += loop

        if argments:
            string += """
    $all_moves({})""".format(argments[:-2])

        for layer in transform_viewer.state_org:
            for name, kwargs_org in {k: v for dic in [transform_viewer.state_org[layer], transform_viewer.state[layer]] for k, v in dic.items()}.items():
                kwargs = {k[2]:v for k, v in all_keyframes.items() if isinstance(k, tuple) and k[0] == name and k[1] == layer}
                if kwargs:
                    string += """
    show {} onlayer {}:
        subpixel True """.format(name, layer)
                    for p, d in transform_viewer.props:
                        if p in kwargs and len(kwargs[p]) == 1:
                            string += "{} {} ".format(p, kwargs[p][0][0])
                        elif d != {k2: v2 for dic in [transform_viewer.state_org[layer], transform_viewer.state[layer]] for k2, v2 in dic.items()}[name][p]:
                            string += "{} {} ".format(p, {k2: v2 for dic in [transform_viewer.state_org[layer], transform_viewer.state[layer]] for k2, v2 in dic.items()}[name][p])
                    for p, check_points in kwargs.items():
                        if len(check_points) > 1:
                            string += """
        parallel:"""
                            string += """
            {} {}""".format(p, check_points[0][0])
                            for i, check_point in enumerate(check_points[1:]):
                                string += """
            {} {} {} {}""".format(check_point[2], check_points[i+1][1]-check_points[i][1], p, check_point[0])
                            if loops[name+"_"+layer+"_"+p+"_loop"]:
                                string += """
            repeat"""

        if string:
            try:
                from pygame import scrap, locals
                scrap.put(locals.SCRAP_TEXT, string)
            except:
                renpy.notify(_("Can't open clipboard"))
            else:
                #syntax hilight error in vim
                renpy.notify("Placed\n{}\n\non clipboard".format(string).replace("{", "{{").replace("[", "[["))
        else:
            renpy.notify(_("Nothing to put"))
## 카메라 ################################
init python:
    register_3d_layer('background', 'middle', 'forward')

## 미니게임 Pong ##########################
init python:

        class PongDisplayable(renpy.Displayable):

            def __init__(self):

                renpy.Displayable.__init__(self)


                # The sizes of some of the images.
                self.PADDLE_WIDTH = 12
                self.PADDLE_HEIGHT = 95
                self.PADDLE_X = 240
                self.BALL_WIDTH = 15
                self.BALL_HEIGHT = 15
                self.COURT_TOP = 129
                self.COURT_BOTTOM = 650


                # Some displayables we use.
                self.paddle = Solid("#ffffff", xsize=self.PADDLE_WIDTH, ysize=self.PADDLE_HEIGHT)
                self.ball = Solid("#ffffff", xsize=self.BALL_WIDTH, ysize=self.BALL_HEIGHT)

                # If the ball is stuck to the paddle.
                self.stuck = True

                # The positions of the two paddles.
                self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
                self.computery = self.playery

                # The speed of the computer.
                self.computerspeed = 380.0

                # The position, delta-position, and the speed of the
                # ball.
                self.bx = self.PADDLE_X + self.PADDLE_WIDTH + 10
                self.by = self.playery
                self.bdx = .5
                self.bdy = .5
                self.bspeed = 350.0

                # The time of the past render-frame.
                self.oldst = None

                # The winner.
                self.winner = None

            def visit(self):
                return [ self.paddle, self.ball ]

            # Recomputes the position of the ball, handles bounces, and
            # draws the screen.
            def render(self, width, height, st, at):

                # The Render object we'll be drawing into.
                r = renpy.Render(width, height)

                # Figure out the time elapsed since the previous frame.
                if self.oldst is None:
                    self.oldst = st

                dtime = st - self.oldst
                self.oldst = st

                # Figure out where we want to move the ball to.
                speed = dtime * self.bspeed
                oldbx = self.bx

                if self.stuck:
                    self.by = self.playery
                else:
                    self.bx += self.bdx * speed
                    self.by += self.bdy * speed

                # Move the computer's paddle. It wants to go to self.by, but
                # may be limited by it's speed limit.
                cspeed = self.computerspeed * dtime
                if abs(self.by - self.computery) <= cspeed:
                    self.computery = self.by
                else:
                    self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)

                # Handle bounces.

                # Bounce off of top.
                ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2
                if self.by < ball_top:
                    self.by = ball_top + (ball_top - self.by)
                    self.bdy = -self.bdy

                

                # Bounce off bottom.
                ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
                if self.by > ball_bot:
                    self.by = ball_bot - (self.by - ball_bot)
                    self.bdy = -self.bdy

                    
                        

                # This draws a paddle, and checks for bounces.
                def paddle(px, py, hotside):

                    # Render the paddle image. We give it an 800x600 area
                    # to render into, knowing that images will render smaller.
                    # (This isn't the case with all displayables. Solid, Frame,
                    # and Fixed will expand to fill the space allotted.)
                    # We also pass in st and at.
                    pi = renpy.render(self.paddle, width, height, st, at)

                    # renpy.render returns a Render object, which we can
                    # blit to the Render we're making.
                    r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))

                    if py - self.PADDLE_HEIGHT / 2 <= self.by <= py + self.PADDLE_HEIGHT / 2:

                        hit = False

                        if oldbx >= hotside >= self.bx:
                            self.bx = hotside + (hotside - self.bx)
                            self.bdx = -self.bdx
                            hit = True

                        elif oldbx <= hotside <= self.bx:
                            self.bx = hotside - (self.bx - hotside)
                            self.bdx = -self.bdx
                            hit = True

                        if hit:
                            
                            self.bspeed *= 1.10

                # Draw the two paddles.
                paddle(self.PADDLE_X, self.playery, self.PADDLE_X + self.PADDLE_WIDTH)
                paddle(width - self.PADDLE_X - self.PADDLE_WIDTH, self.computery, width - self.PADDLE_X - self.PADDLE_WIDTH)

                # Draw the ball.
                ball = renpy.render(self.ball, width, height, st, at)
                r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                              int(self.by - self.BALL_HEIGHT / 2)))

                # Check for a winner.
                if self.bx < -50:
                    self.winner = "니논"

                    # Needed to ensure that event is called, noticing
                    # the winner.
                    renpy.timeout(0)

                elif self.bx > width + 50:
                    self.winner = "[name]"
                    renpy.timeout(0)

                # Ask that we be re-rendered ASAP, so we can show the next
                # frame.
                renpy.redraw(self, 0)

                # Return the Render object.
                return r

            # Handles events.
            def event(self, ev, x, y, st):

                import pygame

                # Mousebutton down == start the game by setting stuck to
                # false.
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    self.stuck = False

                    # Ensure the pong screen updates.
                    renpy.restart_interaction()

                # Set the position of the player's paddle.
                y = max(y, self.COURT_TOP)
                y = min(y, self.COURT_BOTTOM)
                self.playery = y

                # If we have a winner, return him or her. Otherwise, ignore
                # the current event.
                if self.winner:
                    return self.winner
                else:
                    raise renpy.IgnoreEvent()
screen pong():

        default pong = PongDisplayable()

        add "bg pong field"

        add pong

        text _("[name]"):
            xpos 240
            xanchor 0.5
            ypos 22
            size 40

        text _("니논"):
            xpos (1280 - 240)
            xanchor 0.5
            ypos 22
            size 40

        if pong.stuck:
            text _("클릭하면 시작"):
                xalign 0.5
                ypos 50
                size 40    

## 미니게임 라벨 ###########################
label play_pong:

        window hide  # Hide the window and  quick menu while in pong
        $ quick_menu = False

        call screen pong

        $ quick_menu = True
        window show

        show stand_Ninon

        if _return == "니논":

            ch_ninon "내가 이겼어!"

        else:

            ch_ninon "네가 이겼네. 축하해."

            $ win_point = win_point + 1

label pong_done:

    show stand_Ninon

    menu:
        ch_ninon "한 판 더 할래?"

        "물론.":

            jump play_pong

        "그만할래.":

            pass
            
    hide stand_Ninon
    return
## 닉네임 글자수제한 ######################
init python:
    def length(name):
        if len(name) > 10:
            return False
        else:
            return True

## 게임 시작 ##############################
## 이름 짓기 #############################
label naming:
    # 아메스 테마 서서히 커지다가 고정
    play music "audio/main/ames.mp3" fadein 3.0
    ch_nar " 당신의 이름, 가르쳐줄래?"

    $ player_name = renpy.input("내 이름...")
    $ name = player_name
    $ finalConso = finalChecker(name)

    if length(name) == True:
        hatena "어서 와, [name]. 그게 당신의 이름이구나."
        hatena "지금부터 당신이 보게 될 것은, 이른바 꿈 같은 거야. 이미 겪어 보았거나, 언젠가 일어날지도 모르는, 한여름 밤의 꿈 같은 일. ‘몽상’이라 불러도 좋겠네."

        menu:
            "당신은 누구죠?":
                hatena "내가 누구냐고? 알 필요 없다."
                ##하스스톤 비밀거는 효과음
                hatena "……호기심도 많네. 내 정체 같은 건 중요하지 않아."
                hatena "당신이 알아야 할 건 단지…… 이제부터 여러 명의 ‘소녀’들을 만나게 된다는 것과,"
                hatena "당신이 어떤 선택을 내리느냐에 따라 그녀들의 운명이 조금씩 바뀌게 된다는 것밖에 없어. 그럼 잘해 봐. 행운을 빌게, 왕자님♪"
            ##텍스트 사라지면서 볼륨 서서히 off
    else:
        hatena "어떻게 사람 이름이 [name]일수가 있지 ㅋㅋ"
        hatena "진짜 이름을 10자 이내로 알려 줘."
        call naming from _call_naming

    return

## 프롤로그 #############################
label start:
    $ camera_reset()
## 이름 생성 여부 ######################
    if (player_name == "가상의 이름 simulated name"):
        call naming from _call_naming_1
    else:
        pass        
## S# 1. 초원 ###
    scene bg_forest onlayer background with fade # 배경화면

    play music "audio/main/nature.mp3"

    hatena "빈틈! 받아라앗...!!"

    ## 마물 cg DIS
    show stand_monster onlayer middle with dissolve

    ## 총소리

    ## 피격효과, 화면 흔들림 효과
    show bg_forest onlayer background with hpunch
    
    monster "커르륵...!"

    hide stand_monster onlayer middle

    ## 모니카 웃는 표정
    show stand_Monica onlayer middle with dissolve

    ch_monica "됐다! 움직임이 봉쇄됐어! 지금이다, 니논! 한 방 먹여!!"
    hide stand_Monica onlayer middle
    show stand_Ninon onlayer middle with dissolve

    ch_ninon "ROGER! 이거나 먹어라, 입니다! 「인법 · 쇙강 줜병 회오뤼」~!!"
    hide stand_Ninon onlayer middle

    ## 마물 cg
    ## 불길이 치솟는 효과 ## E - 불길 치솟음 ## 화면 흔들림 효과(지글지글거리는 느낌 정도로 작게)
    show stand_monster onlayer middle with dissolve
    monster "쿠아아악!! 크르륵..."

    ## 울부짖는 효과, 화면 흔들림 효과
    ## 괴물 울음소리

    monster "크워어어어어!!"

    hide stand_monster onlayer middle


    show stand_Monica onlayer middle with dissolve
    ch_monica "칫… 이 정도로는 어림도 없나. 모두들, 뒤로 물러나! 놈이 반격해 온다!"
    hide stand_Monica onlayer middle
    show stand_Kuka onlayer middle with dissolve

    ch_kuka "이… 이렇게 커다란 마물이라면… 쿠… 쿠우카, 돌아오지 못할 강을 건너 버릴지도…! 크흐흣….츄릅…."
    ##쿠우카 어둡게
    ch_ayumi "쿠…쿠우카 씨…! 혼자 너무 앞에 있으면 위험해요…!"
    hide stand_Kuka onlayer middle
    show stand_Monica onlayer middle with dissolve
    ch_monica "큭! 이건 버틸 수가… 유키, 서포트를!"
    hide stand_Monica onlayer middle
    show stand_Yuki onlayer middle with dissolve
    ch_yuki "뭐? 나는 분명히 말했다? 데려와도 아~무것도 안 할 거라고. 아름다운 내 몸에 생채기라도 나면 책임질 거야?"    
    extend " 앗…… 나뭇잎에 맺힌 이슬…… 내 모습이 비쳐서 너무 예뻐…… 하아……."
    hide stand_Yuki onlayer middle ## 자뻑하는 표정
    show stand_Ninon onlayer middle with dissolve
    ch_ninon "유키 씨, 무사답지 못하다 입니다~! 모름지기 사무라이라면 아무리 YABAI한 상황일지라도…"
    
    ## 니논 화난 표정 주변에 불이 붙는 효과/ 불길 치솟음
    ## 니논 놀란 표정
    ch_ninon "우와아아아앗!!! 불이 옮겨붙었다 입니다!!! 후끼약!!!"

    #둔탁한 피격음
    hide stand_Ninon onlayer middle
    show stand_Kuka onlayer middle with dissolve##쿠우카중앙으로 서서히 작아지다 사라짐
    #멀리 날아가는 소리
    
    ch_kuka "쿠, 쿠우카, 날아가버려요오오옷!!!!"
    hide stand_Kuka onlayer middle with zoomout
    show stand_Monica onlayer middle with dissolve
    ch_monica "니논! 쿠우카!! 이대로면 모두가 위험… 에에잇! 이판사판이다!"
    # 칼을 검집에서 빼는 소리

    ch_monica "자전―"

    ch_monica "―—일섬!!"
    #일순간 까맣게 된 화면을 가로로 베는 효과
    #칼로 베는 소리
    hide stand_Monica onlayer middle with dissolve
    hide bg_forest onlayer background with fade
## 길드 하우스 cg
    scene bg_black
    show bg_guildhouse with fade
    ch_nar "식칼에 베였다."

    ch_nar "콧코로의 눈망울이 연상되는 와인색의 피가 손끝에 맺힌다. 아프다."

    ## 피 묻은 손수건 이미지 팝업

    ch_nar "언젠가 콧코로에게 받았던 손수건으로 피를 닦았다."

    ch_nar "콧코로…… 언제 와? 나 배고파. 무서워."

    ch_nar "콧코로는 돈 많이 벌어오겠다며 집을 나간 뒤로 며칠째 연락이 안 된다."

    ch_nar "페코린느와 배신자는 던전으로 식재료 탐방을 간다길래 따라가고 싶다고 했더니,"

    ch_nar "“아하하, 약해 빠진 주제에 또 누구 발목을 잡으려는 건가요? 장난 아니네요! 얌전히 길드하우스나 지키고 있으세요☆”"

    ch_nar "“하아? 벌레 한 마리도 제대로 못 잡는 멍청한 돼지가 어딜 따라오겠다고? 죽여 버린다?”"

    ch_nar "라며 나만 남겨 두고 가 버렸다."

    ch_nar "수영복만 벗으면 아무것도 아닌 것들이……."

    ch_nar "항상 콧코로가 요리를 해 줬는데 이젠 밥 해 줄 사람이 아무도 없다. 이대로면 정말 굶어 죽을지도 모른다."

    ch_nar "그래서 직접 요리를 해 보려고 식칼을 꺼냈는데 쥐는 법을 몰라서 바로 손가락을 베였다."

    ch_nar "콧코로…… 생전 손에 물 한 번 묻혀 본 적 없는 나에게 이런 수모를 겪게 하다니…… 돌아오면 잘못했다고 울며불며 매달릴 때까지 단식투쟁을 할 것이다."

    ## 대화창 사라짐
    ## 문 두드리는 소리
    ## 잠깐 텀

    player "마망!!!! 내가 잘못했어!! 다시는 반찬 투정 안 할게!!!"    

    ## 대화창 사라짐
    ## 문 열리는 소리
    ## 잠깐 텀
   
    ## 모니카 우는표정 cg
    show stand_Monica with dissolve
    ch_nar "에이씨, 콧코로가 아니잖아." 
    
    ch_monica "훌쩍…… 귀, 귀공…… 훌쩍, 날 좀…… 도와주게…… 으아앙, 우아아앙~"

    menu:
        "뭐야...":
            ch_monica "그, 그게…… 훌쩍."

            player "소난다……"

            ## 모니카 시무룩한 표정
            ch_monica "?"
            pass
        "왜 울고 있는거야?":
            ch_monica "그, 그게…… 훌쩍."

            player "소난다……"

            ## 모니카 시무룩한 표정
            ch_monica "?"
            pass
    
    
    hide stand_Monica
    ## 길드하우스 페이드 아웃
    hide bg_guildhouse with fade
    ## 마을 브금 불륨 페이드 아웃
    
    ## 까만 배경

    centered "몇 시간 전……"

    ## 마을 브금 볼륨 페이드 인
    ## 길드 하우스 cg 페이드 인
    scene bg_guildhouse with fade
    
    ## 모니카 화난 표정 페이드
    show stand_Monica with dissolve
    ch_monica "이대로는 안 돼!"
    show stand_Monica at movetoleft
    ## 모니카가 왼쪽으로 밀리면서 니논 오른쪽에 팝업
    show stand_Ninon at right with dissolve ## 웃는 표정
    ## 모니카 어둡게, 니논 밝게
  
    ch_ninon "모니카 씨~? 무슨 문제라도 있다 입니까? 다시마 초절임 먹을래요?"

    ## 니논 어둡게, 모니카 밝게

    ##모니카 놀란 표정
    ch_monica "뭐, 뭐지 그건? 달콤한 과자인가…?"
    ##모니카 화난 표정
    window hide
    hide stand_Ninon
    
    show stand_Monica at movetocenter
    extend " ……아니, 아니! 그게 중요한 게 아니다!"

    ch_monica "우리는 ‘바이스플뤼겔 랜드솔지부’다! 마물을 소탕하고, 곤란에 빠진 사람들을 도와주는 유능한 모험가 길드!"
    ch_monica "……였어야 했는데, 마지막으로 마물을 토벌했던 게 언제인지 이제는 기억도 안 날 지경이다. 채집 의뢰만 산더미처럼 쌓여 있어! 이게 뭐냐! 우리는 전투 길드란 말이다~!!"

    hide stand_Monica
    show stand_Kuka with dissolve

    ch_kuka "쿠, 쿠우카는 식물 채집도 좋다고 생각해요… 숲에서 가끔 식물형 마물도 튀어나와서… 도끼로도 잘 안 끊어지는 억센 넝쿨로 온몸을 잔뜩 조여오면…"
    ## 쿠우카 망상하는 표정으로 변경

    extend " 크, 크흣, 크헤헤헷…"

    hide stand_Kuka
    show stand_Yuki with dissolve #화난 표정
    ch_yuki "나참~ 대체 뭐가 불만인데? 채집 의뢰도 어쨌든 사람들을 도와주는 거잖아. 그리고 오에도에서 엄청나게 못생긴 마물을 해치웠던 건 머리에서 지워버린 거야?"

    hide stand_Yuki
    show stand_Monica at center with dissolve:
        ease 0.5 yalign 1.0
        ease 0.1 yalign 0.0
        repeat 2 ##팔짝 뛰는 모션
    ch_monica "그래서 더 문제라는 거다!! 그 강력한 마물을 쓰러뜨릴 정도의 역량을 가지고 있으면서, 이전에 비해 바뀐 게 아무것도 없잖아!"

    ch_monica "다들 약속이라도 한 것마냥 비전투 의뢰만 잔뜩 수주해오고! 그대들은 모험가 길드를 대체 뭐라고 생각하는 건가?!"
    hide stand_Monica
    show stand_Ninon with dissolve ##자신만만
    ch_ninon "니논도 할 때는 한다 입니다, 모니카 씨! 명령만 내리신다면 당장이라도 마물녀석들의 모가쥐를 따버릴 수 있습니다~!"
    hide stand_Ninon
    show stand_Monica with dissolve ##자신만만
    
    ch_monica "……그래. 말 잘 했다, 니논!" 
    ## 모니카 웃는 표정
    ch_monica "분명 우리는 숲이나 평원에 돌아다니는 어지간한 마물 정도는 거뜬히 해치울 정도로 강해. 그럼에도 마물 소탕에 있어서는 별다른 성과를 보이지 못하고 있다."

    ch_monica "모든 일에는 타당한 이유가 존재하기 마련. 그렇다면 우리들에게 부족한 건 대체 뭘까? 아유미! 대답해 봐라!"
    ## 호흡 한 번 끊기
    ## 모니카 어둡게

    ch_ayumi "힉, 히이익……? 저, 저, 저 말인가요?! 그건, 그, 저기,"

    ch_ayumi "제… 제가 생각하응기잇!! 흐에… 혀 깨무러써…"
    ## 모니카 밝게/뚱한 표정

    ch_monica "……"
    ## 모니카 화난 표정
    ch_monica "…………바이스플뤼겔에 가장 부족한 것은 바로…………"

    show highlight onlayer forward with hpunch

    hide highlight onlayer forward

    ch_monica "…………‘실전’이다!!"
    ch_monica "아무리 강력한 전사라 해도 실전 경험이 없다면 지나가던 들개 한 마리 상대하는 것도 버거울 터."

    show stand_Monica at movetoleft
    show stand_Ninon_surprise at right with dissolve## 니논 놀란 표정
    ## 모니카 어두워지고 니논 밝게

    ch_ninon "지나가던 들개 씨…… 무섭다 입니다……!"
    hide stand_Ninon_surprise with dissolve
    
    show stand_Monica at movetocenter
    
    ch_monica "요점이 그게 아니지 않나!!!"

    ch_monica "……우리가 실제로 마물을 해치운 전적은 손에 꼽을 정도다. 그마저도 대부분은 요행에 불과했던 것들이지."

    ## 자신만만한 표정
    ch_monica "하지만! 운에 기대지 않고 마물을 쓰러뜨릴 수 있는, 확실한 실력을 쌓는 방법을 우리는 알고 있다! 어떻게?"
    hide stand_Monica
    ## 유키 질색하는 표정
    show stand_Yuki_angry with dissolve
    ch_yuki "잠깐, 설마……."
    hide stand_Yuki_angry
    ## 강조선
    show stand_Monica with dissolve## 자신만만
    show highlight onlayer forward with hpunch

    ch_monica "마물을 왕창 때려잡는 거다!!! 아주 커다랗고 무지막지한 놈들로!!"
    hide highlight onlayer forward
    hide stand_Monica
    show stand_Kuka with dissolve: ## 망상
        ease 0.5 yalign 1.0
        ease 0.1 yalign 0.0
        repeat 1
    ch_kuka "으히익♥"
    hide stand_Kuka
    show stand_Monica with dissolve ## 자신만만

    ch_monica "그런 고로 떠날 채비를 서두르도록, 제군들! 곧바로 프라노 평원으로 출발한다!!"
    hide stand_Monica with dissolve
    show stand_Yuki at left with dissolve ## 질색하는 표정
    
    ch_yuki "아니 아니~~ 마물을 잡으러 가자고? 지금 당장~?! 진심이야?"
    ch_yuki "나는 가서도 아무것도 안 할 거니까! 전투 같이 위험한 일엔 끼어들기 싫어! 피부에 안 좋단 말이야~!"

    ## 유키 어둡게
    ch_ayumi "뭐, 뭐어~ 모니카 씨 말씀이 틀린 것도 아니구요……."
    show stand_Yuki at movetoleft
    show stand_Kuka with dissolve ## 망상

    ch_kuka "힘세고 강한 마물…… 뜨겁고 크고 묵직한…… 크힛, 크흐흣……."

    ## 쿠우카 어둡게
    show stand_Ninon at veryright with dissolve ##자신만만한 표정

    ch_ninon "진군입니다! 찢고 죽인다 입니다!!"

    ## 니논 어둡게
    hide stand_Kuka
    hide stand_Ninon
    hide stand_Yuki

    show stand_Monica with dissolve ## 자신만만
    ch_monica "그럼 출발이다! 바이스플뤼겔의 긍지를 걸고!!"

    hide stand_Monica with dissolve
    ## 배경 페이드 아웃
    hide bg_guildhouse with fade

## 길드하우스 페이드 인
    scene bg_guildhouse with fade
    player "……그렇게 긍지가 박살난 거야?"

    show stand_Monica with dissolve ## 빼애액 표정
    ch_monica "박살나지 않았어!!"
    ## 시무룩한 표정으로 변경
    extend " ……나는 그저……."

    ch_monica "……무작정 부딪혀 보면 어떻게든 될 거라고 생각했건만……. 귀공은 내 방식이 잘못됐다고 생각하나?"

    menu:
        "결과가 말해 주고 있잖아":
            ## 볼빵빵
            ch_monica "……마, 맞는 말이다만……, 그렇게 말하는 귀공에게는 더 좋은 해결책이 있는 거겠지?"
            ch_monica "자세한 이야기는 우리 길드원들 앞에서 하는 게 어떤가? 지금 바로 출발하도록 하지."
        "틀린 방법은 아니었다고 생각해":
            ## 시무룩한 표정
            ch_monica "빈말이라도 고맙군…… 하지만 우리는 실제로 마물에게 이렇다 할 타격도 주지 못하고 당해 버렸어."
            ch_monica "이대로면 부하들이 입는 피해만 늘어갈 터……. 뭔가 다른 방법이 필요해." 
            ch_monica "귀공, 도움을 줄 수 있겠나? 일단 우리 길드하우스로 자리를 옮기도록 하지."
    hide stand_Monica with fade
    window hide
    ## cg 페이드 아웃
    hide bg_guildhouse with fade
    ## 잠깐 텀
## 랜드솔 마을 cg 페이드
    scene bg_town
    show stand_Ninon with dissolve ##웃는표정

    ch_ninon "오오~ 쇼군~! 친히 행차하셨나이까 입니다? 기별도 없이 니논을 만나러 오셨다기에 버선발로 뛰쳐나왔사와요 입니다! 기쁨에 못 이겨 할복 해버릴 것 같습니다~!"

    show stand_Ninon at movetoleft ##어둡게
    show stand_Kuka with fade

    ch_kuka "도, 도S씨, 오랜만이에요…….!! 쿠우카를 도S씨가 없으면 살 수 없는 몸으로 만들어놓고, 쿠우카가 먼저 파렴치한 요구를 입밖으로 꺼낼 때까지 몇 날 며칠을 방치하면서 즐기시다니……! 이상성욕변태! 인격파탄자! 이제 만족하셨나요……!! 크흣…… 크히힛……."
    
    show stand_Kuka at movetoright ##어둡게
    show stand_Yuki with dissolve ## 자뻑하는 모습
    
    ch_yuki "뭐야~ [name]. 오늘도 변함없이 귀여운 내 모습이 보고 싶어서 여기까지 왔구나? 이해해~ 내 미모는 매일매일 언제 봐도 질리지 않으니까. 하아…… 거울 속의 나…… 너무 귀여워……."

    ## 유키 어둡게

    ch_ayumi "히히…… 선배…… 오늘도 잘생겼어…… 히히……"

    ch_nar "예전부터 생각했던 거지만 여긴 제정신인 사람이 아무도 없는 것 같다."

    hide stand_Kuka
    hide stand_Ninon
    hide stand_Yuki
    
    show stand_Monica with dissolve ##자신만만


    ch_monica "모두들, [name]가 반가운 마음은 이해한다만 밖에서 이럴 것이 아니라 어서 안으로 들지. 차라도 한 잔 마시면서 얘기하는 게 좋겠군."

    ## 무심한 표정으로 변경

    ch_monica "그…… 그리고 달콤한 과자도 조금…… 흠흠."
    hide stand_Monica
    hide bg_town
## 길드 하우스 cg 페이드
    show bg_black onlayer background
    scene bg_guildhouse onlayer middle with fade
    show stand_Ninon onlayer forward

    ch_ninon "쇼군! 이것은 마음을 안정시키는 동국의 3대 명차, 우지차라고 하는 것입니다!"

    ## 
    extend " 어서 들이켜 보세요 입니다!"

    hide stand_Ninon onlayer forward

    player "우지챠……."

    show stand_Kuka onlayer forward with dissolve ##기본 표정

    ch_kuka "그, 그러니까 도S씨는…… 정확히 무슨 일 때문에 오신 거죠?"
    ## 쿠우카 망상하는 표정
    ch_kuka "설마…… 어둡고 구석진 골목에 마구잡이로 쿠우카를 밀어붙였던 그날…… 쿠우카가 아직까지도 그날의 쾌락을 잊지 못한 채 추잡스러운 행위를 계속하고 있는지 직접 확인하려고……?!"

    ch_kuka " 쿠, 쿠우카를 나락으로 빠뜨리기 위해 어디까지 계획을 세워 놓은 건가요?! 이…… 인륜배반자! 관음증 변태! 쿠, 쿠훗, 크흐흐……."

    hide stand_Kuka onlayer forward
    show stand_Monica onlayer forward with dissolve

    ch_monica "음! [name]를 이 자리에 호출한 건 다름이 아니라, 바이스플뤼겔의 향후 방향성과 마물 소탕 건에 대해 조언을 구하기 위해서다. 모두 한자리에 모였으니 드디어 이야기를 시작할 수 있겠군."

    ## 모니카 어둡게

    ch_ayumi "역시 선배, 계획이 다 있으신 거군요……!"

    player "그런 거 없는데……."

    ch_ayumi "무계획이 계획인 거네요……! 역시!"
    hide stand_Monica onlayer forward

    show stand_Ninon_down onlayer forward with dissolve ## 시무룩한 표정

    ch_ninon "쇼군! 니논은 최선을 다했다 입니다! 하지만 마물이 너무너무 POWERFUL 했습니다……."

    ch_ninon "「인법 · 쇄우 병쉰 회오뤼감좌」를 정면으로 받아 내고 살아남은 자는 그 녀석이 처음이었다 입니다!"

    ## 니논 어둡게

    show stand_Monica onlayer forward at veryright with dissolve ## 시무룩한 표정

    ch_monica "‘그거, 뭔가 다른 이름이었던 것 같은데……’"

    hide stand_Ninon_down onlayer forward

    show stand_Monica onlayer forward at movetocenter

    ## 모니카 자신만만한 표정

    ch_monica "……걱정할 것 없다, 니논! [name]의 도움이 있다면 그보다 더 강한 놈들도 충분히 상대할 수 있게 될 거다."

    ch_monica "그러면, 우리의 문제가 어떤 것인지 말해 줄 수 있겠나?"

    hide stand_Monica onlayer forward
    show stand_Yuki onlayer forward with dissolve ##자신만만한 표정

    ch_yuki "이렇게나 귀여운 내가 있는데, 무슨 문제가 있다는 거야~? 복잡한 생각 하지 말고 예쁜 내 얼굴이나 감상하라구♪"

    hide stand_Yuki onlayer forward
    show stand_Monica onlayer forward with dissolve ## 화난 표정

    ch_monica "그렇게 건성으로 넘길 문제가 아니다! 귀공, 다시 한 번 정식으로 요청하도록 하지."

    ## 모니카 자신만만한 표정

    ch_monica "‘바이스플뤼겔 랜드솔지부’가 나아갈 길을 제시해 주게! 귀공은 우리의 문제가 무엇이라고 생각하나?"

## 캐릭터 선택 분기 #########################
    menu:
        "어설픈 실력과 저돌적인 행동으로 쉽게 위험에 빠지는 것":
            $love_point = ninon

        "동료를 신뢰하지 않고 독단적으로 행동하는 것":
            $point_point = monica

        "순간의 욕망을 억제하지 못하고 충동적으로 행동하는 것":
            $point_point = kuka

        "자기 자신만을 중시하며 동료를 배려하지 않는 것":
            $point_point = yuki

    show stand_Monica onlayer forward with dissolve ## 기본 표정

    ch_monica "음, 과연……. 귀공을 여기까지 데려온 보람이 있군. 훌륭한 통찰력이다."

    ch_monica "그렇다면 귀공이 지적한 대로, 우리의 문제점을 보완하는 것은 곧 바이스플뤼겔의 전력을 증강하는 길이라 봐도 무방할 터. 이제부터 그 방법을……"

    ## 잠깐 텀
    ## 니논 자신만만한 표정
    show stand_Ninon onlayer forward at veryleft:
        linear 0.5 xalign 0.5 


    ch_ninon "특훈만이 살 길이다!!!!!!!! 입니다!!!"

    show stand_Monica onlayer forward at movetoright ##볼빵빵, 얼굴이 절반정도만 보이도록
    
    ch_ninon "닌자가 강해지는 길은 오직 수련, 또 수련하는 것 뿐!! 천하통일을 위해서라면 그 어떤 지옥훈련이라도 견뎌낼 각오가 되어있소 입니다!!"

    show stand_Monica onlayer forward at movetocenter
    show stand_Ninon onlayer forward at movetoleft

    ## 니논 기본표정, 어둡게/모니카 밝게
    ch_monica "흠, 흠!"

    ## 모니카 진지한 표정

    ch_monica "……확실히 틀린 말은 아니다. 가혹한 훈련은 고통스럽지만 그만큼 효과적일 수 있지."

    ## 모니카 시무룩한 표정

    ch_monica "하지만 니논, 훈련의 강도가 높은 것만이 능사는 아니야. 그건 우리가 누구보다도 뼈저리게 경험하지 않았나."

    ## 모니카 어둡게/니논 시무룩한 표정, 밝게
    hide stand_Ninon onlayer forward
    show stand_Ninon_down onlayer forward at veryleft
    ch_ninon "과연…… 입니다. 그럼 니논은 무엇을 할 수 있다 입니까? 할복 입니까?"

    ## 니논 어둡게/ 모니카 밝게, 기본 표정
    ch_monica "그건……"

    ## 모니카 자신만만한 표정

    ch_monica "우리의 새로운 해결사가 답을 알려 줄 거다!"

    ## 둘 다 어둡게

    ch_nar "갑자기 나한테 떠넘긴다고? 미쳤나?"
    ## 모니카 cg어둡게/니논 밝게, 니논 놀란 표정
    hide stand_Ninon_down onlayer forward
    show stand_Ninon_panic onlayer forward at veryleft

    ch_ninon "우오옷~ 믿고 있었다고 쥐엔장~~!! 입니다!"

    player "아니…… 갑자기 그렇게 말해봤자……"

    hide stand_Monica onlayer forward
    hide stand_Ninon_panic onlayer forward
    show stand_Ninon_wink onlayer forward at veryleft:
        linear 0.5 xalign 0.5
    ch_ninon "DAIJOBU 입니다~! 왜냐하면 쇼군은~"
    hide stand_Ninon_wink onlayer forward
    hide bg_black onlayer background
    hide bg_guildhouse onlayer middle
    show stand_Ninon_daiji onlayer forward
    $ camera_move(0, 0, 400, 0, 6)

    scene bg_surf onlayer middle with dissolve
    ## 배경음 일본풍 bgm
    ch_ninon "……쇼군은…… 언제나 정도만을 걸어온 남자."

    ch_ninon "제아무뤼 겉으로는 언행이 아둔하고 이취에 맞지 않는 듯하여도, 쇼군이 인도하는 길의 끝에는 항시 광명이 우뤼를 비추고 있었소."

    ch_ninon "혹자는 쇼군의 우쥑한 성품을 비방할지도 모르오. 허나 그것은 툇마루 아래의 장사를 알아보지 못하는 붬인의 좁은 식견에 불과할 뿐."

    ch_ninon "일찍이 길이 존재했기에 걷는 것이 아니요, 쇼군의 족줙이 곧 길이라. 참된 쥐도자란 바로 그런 것이오."

    ch_ninon "설령 승리를 목줜에 두고 적에게 소금을 보눼어 되레 위난에 처하게 될지라도, 니논은 쇼군의 뜻을 따르겠소. 그것이 종국에는 우리를 줭토로 이끌리라 믿어 의심치 아니하기에……."

    ##빠르게 원래 크기로 복구
    $ camera_move(0, 0, 0, 0, 0.2)


    hide bg_surf onlayer middle
    ## 길드하우스로 다시 변경
    scene bg_guildhouse
    ## 마을 bgm으로 다시 변경
    ## 니논 윙크하는 표정
    hide stand_Ninon_daiji onlayer forward
    show stand_Ninon_wink

    ch_ninon "……에~ 그러니까~ 부담 가질 필요 없다 입니다~!"

    ## 니논 어둡게/ 오른쪽에 모니카 시무룩한 표정

    show stand_Ninon_wink at movetoleft
    show stand_Monica at right

    ch_monica "미안하군. 아직 니논이 충격에서 벗어나지 못한 것 같아."

    player "괜찮아. 빼놓고 얘기하자!"

    ## 모니카 사라짐/ 니논 밝아지고 화면 중앙으로 이동, 시무룩한 표정
    hide stand_Monica
    hide stand_Ninon_wink
    show stand_Ninon_down at left:
        linear 0.5 xalign 0.5
    
    ch_ninon "HIDOI 입니다……."

    ## 니논 cg 어둡게

    ch_ayumi "‘……멍청해 보인다는 말을 돌려서 얘기한 건 못 알아채신 걸까, 선배…….’"

    hide stand_Ninon_down

    ch_nar "그나저나 큰일이군……."

    ch_nar "있어 보이려고 아무 말이나 지껄인 건데 뒷수습을 못 하겠어……."

    ch_nar "니논이 쌉소리를 하는 동안 뭐라도 생각해 냈어야 했는데…… 어떡하지……?"

    ## 유키 뚱한 표정
    show stand_Yuki_ddung with dissolve

    ch_yuki "저기 저기 [name]."

    player "……응?"

    ch_yuki "좀 전에 니논이 ‘특훈’이니 뭐니 했던 거 말야, 그런 바보 같은 걸 진짜로 하자고 할 건 아니지?"

    ## 니논 억울한 표정 왼쪽/ 유키 cg 어두워짐
    show stand_Yuki_ddung at movetoright
    show stand_Ninon_innocence at left

    ch_ninon "이익……! 먼저 바보라 하는 사람이 바보 입니다!"

    ## 니논 어둡게/ 유키 밝게

    ch_yuki "하? 농담이지? 그런 거 안 해도 내 미모는 나날이 예뻐지거든? 찝찝하게 땀 흘리는 일 같은 건 절대 사절이니까~ 참고하라구. 알았지?"

    ch_nar "음…… 그냥 다 패고 감옥 가고 싶다."
    ch_nar "그런데 잠깐, 방금……."

    hide stand_Ninon_innocence
    hide stand_Yuki_ddung

    player "……땀 흘리는 일이라……."
    
    show stand_Kuka with dissolve ## 기본 표정
    ch_kuka "도…… 도S씨가 뭔가 생각에 잠겼어요……!"

    ## 쿠우카 망상하는 표정

    extend " 어, 어떻게 하면 쿠우카를 더 수치스럽게 능욕할 수 있을지 머리를 쥐어짜내고 있는 게 분명해요!!"

    ch_kuka "아아, 그, 그치만…… 얼마나 심한 짓을 당할지 가늠조차 하지 못하면서, 아니 어쩌면 누구보다도 잘 알고 있으면서!! 무구하고 앳된 소녀의 마음은, 불나방과 같이 그 순결함을 제발로 불사르려는 충동을 떨쳐내지 못하고……!!! 이 얼마나 잔혹하고 달콤한 유혹인가…… 크히, 크히힛…… 쿠후후후훗……"
    
    ## 쿠우카 어두워짐

    ch_ayumi "음, 선배…… 쿠우카 씨가 하는 말은 일단 모르는 척하는 게 좋을 것 같아요……."

    ## 쿠우카 밝아짐

    ch_kuka "히이……♥ 아유미 씨에게 무시당하는 감각……! 이건 굉장히 귀하네요……. 크큭…… 여기서 더 떨어질 바닥이 있을까……."

    ## 쿠우카 어두워짐

    ch_ayumi "그…… 그건 무슨 의미인가요오!!!!"

    hide stand_Kuka
    show stand_Yuki with dissolve ## 자뻑하는 표정

    ch_yuki "참, [name]. 오해는 하지 마? 내 미모는 얼마나 밝은 곳에 있든 간에 빛이 나고, 어두운 곳에 있으면 더욱 돋보이는 범우주적 매력을 갖고 있으니까, 장소는 아무래도 상관없어~"

    ch_yuki "그치만 기왕 뭔가를 할 거라면, 나의 아름다움에 공헌할 수 있는 걸 하는 게 세상에 더 도움이 될 거라구. 내가 예뻐질수록 세계는 한층 더 아름다워질 테니까~"

    ## 유키 웃는 표정

    ch_yuki "예를 들면~ 응, 피부 미용에 좋은 거라든지?"

    ## 유키 어두워지고 화면 오른쪽/ 모니카 시무룩한 표정 왼쪽

    show stand_Yuki at movetoright
    show stand_Monica at left

    ch_monica "……그대는 어째서 그렇게까지 피부에 집착하는 건가……"

    ## 모니카 어두워지고 유키 밝아짐

    ch_yuki "음~ 예쁜 얼굴은 타고나는 거라 해도, 피부는 꾸준히 잘 관리해 줘야 한다구. 이참에 모니카 씨도 신경 좀 써 보는 건 어때? 충분히 귀여운 얼굴인데, 아깝잖아~ 뭐, 나만큼은 아니지만."

    ## 유키 어두워지고 모니카 부끄러워하는 표정 밝아짐

    ch_monica "누…… 누가 귀엽다는 거냐!"

    ## 모니카 시무룩한 표정

    extend " ……애초에 나는 군인이다. 그런 것에 신경 쓸 여유는……"

    player "……생각났어."

    ## 유키 사라짐/ 모니카 놀란 표정, 화면중앙
    hide stand_Yuki
    show stand_Monica at movetocenter

    ch_monica "귀공……? 아아, 특훈에 관한 것 말인가! 허심탄회하게 얘기해 보게!"

    player "특훈을 하면…… 땀이 나."

    ## 모니카 시무룩한 표정
    ch_monica "……?"

    player "땀이 난다는 것은 힘이 든다는 것입니다."

    ## 모니카 cg 어둡게

    ch_ayumi "??"

    player "힘이 들면, 피부에 좋지 않습니다. 그렇기 때문에 나는 생각합니다. 피부에 좋지 않으면, 땀이 나는 것이 아닌가 하고."

    hide stand_Monica
    show stand_Kuka with dissolve ## 쿠우카 망상하는 표정
    ch_kuka "뇌가 겁탈당하고 있어요……!!"

    player "하지만 온천이라면 어떨까?"

    hide stand_Kuka
    show stand_Yuki at left ## 유키 놀라는 표정, 밝게
    show stand_Ninon_surprise at right ## 니논 놀라는 표정, 어둡게

    ch_yuki "온!" ## 유키 줌 인

    #show stand_Yuki at left ## 유키 어둡게
    #show stand_Ninon_surprise at right ##니논 밝게

    ch_ninon "천!" ## 니논 줌 인

    hide stand_Yuki
    hide stand_Ninon_surprise

    show stand_Monica with dissolve ## 시무룩한 표정

    ch_monica "다…… 좋은데, 온천이 특훈과 무슨 관계가 있는 건가……?"

    hide stand_Monica

    show stand_Ninon with dissolve

    ch_ninon "후, 아직 멀었군요 입니다, 모니카 씨!"

    ch_ninon "분명 조금 전 쇼군이 지적한 문제는, 요컨대 TEAMWORK가 부족하다는 사실!"

    ch_ninon "우리가 충분히 강하다는 것은 모니카 씨도 인정하셨다 입니다."

    hide stand_Ninon

    show stand_Ninon_daiji with dissolve ## 니논 비장한 표정

    ch_ninon "그렇다면 우리에게 남은 과제는 바로 「단합」!!"

    ch_ninon "지금까지 니논은 단순무쉭한 수련법만을 고집해왔소 입니다. 하지만 쇼군은! 그보다 한 차원 높은! 격이 다른 강함을 추구하는 것입니다!! 길드 합숙을 통한 유대감 증진, 그리고 이어지는 UNION BURST!!!"

    ch_ninon "동시에 「온천」이라는 명답을 제시하여! 피부를 염려하는 유키 씨의 불만까지 해치워 버린 것이다 입니다!!"

    hide stand_Ninon_daiji

    show stand_Ninon_wink with dissolve

    ch_ninon "역시 쇼군, 실로 지혜로운 판단이 아닐 수 없소 입니다!! 존경하오 입니다~!"

    ## 니논 어둡게

    show stand_Monica at veryleft ## 모니카 놀란 표정

    ch_monica "오오……! 그런 것이었나! 나도 아직 한참 부족하군…….!!"

    ## 모니카 어둡게

    show stand_Yuki at right ## 유키 웃는 표정

    ch_yuki "뭐~ 그런 이유라면 어울려 주지 못할 것도 없긴 해~ 이런 것까지 신경써 주다니, 꽤나 섬세하잖아?"

    hide stand_Monica
    hide stand_Ninon_wink
    hide stand_Yuki

    ch_nar "……뭐지?"

    ch_nar "콧코로한테 온천 여행 가자고 했다가 주인님은 염치도 없냐고 한소리 들었던 게 생각나서 막 던져 본 건데……"

    ch_nar "역시…… 이 정도로 잘생겼으니 무슨 말을 해도 먹히는 건가. 이런 이런……."

    ch_nar "못생겼다는 건 대체 어떤 기분일까……? 하루만 못생겨 봤으면 좋겠다."

    ch_nar "앗, 나도 참. 말도 안 되는 소릴. 하하하."

    ## 니논, 모니카, 유키 cg 어둡게

    show stand_Kuka with dissolve ## 쿠우카 기본 표정

    ch_kuka "그……러면, 온천에 가서는 구체적으로 어떤 일을 하게 되나요……?"

    ## 쿠우카 망상하는 표정

    ch_kuka "여, 역시 혼욕을 노리시는 건가요?! 모두가 지켜보는 가운데 쿠우카의 치부를 억지로 드러내 보이게 하려는 속셈인 거네요!!! 치욕감에 정신을 차리지 못하는 쿠우카의 주변을 수많은 남성들이 에워싸고선…… 으헤헷…… 쿠헤헤헤헷……"

    ## 쿠우카 어둡게

    ch_ayumi "호……호호흐호, 혼, 혼욕?! 서, 스, 서, 선배와 함께?!!?"

    hide stand_Kuka
    show stand_Monica with dissolve ## 뚱한 표정 

    ch_monica "……그대들이 뭘 상상하는 건지 잘은 모르겠다만……"

    ch_monica "최소한 건전한 속내가 아니라는 것만은 분명해 보이는군……."

    ## 모니카 웃는 표정

    ch_monica "그건 그렇다 치고, 귀공."

    ch_monica "먼저 온천이라는 장소를 언급한 만큼 따로 생각해 둔 곳이 있는 거겠지? 우리는 전적으로 귀공의 계획에 따르겠네."

    hide stand_Monica
    
    player "뎃?"

    show stand_Ninon_wink with dissolve

    ch_ninon "장소라면 걱정 맛세이 입니다! 전부 니논에게 맡기는 겁니다~!"

    hide stand_Ninon_wink
    show stand_Ninon with dissolve ## 니논 웃는 표정

    ch_ninon "지난번 마물 토벌 이후, 아직까지도 오에도 여러분의 열화와 같은 INVITATION이 끊이질 않고 있는데……"

    hide stand_Ninon
    show stand_Ninon_down with dissolve ## 니논 시무룩한 표정

    ch_ninon "여기 이중에…… 어…… 어디 있냐 입니다……?"

    hide stand_Ninon_down
    show stand_Ninon ## 니논 웃는 표정

    extend " 앗, 발견 입니다."

    ch_ninon "오에도 사상 최고 이빠이로 큰 대형 온천의 초대장도 잔뜩 왔다 입니다~!"

    ch_ninon "그러면~ 가장 마지막에 온 초대장을 개봉해 보도록 하겠습니다~~!! 두구두구두구……"

    hide stand_Ninon
    show stand_Ninon_surprise ## 니논 놀란 표정

    ch_ninon "………………."

    ch_ninon "………………………………."

    hide stand_Ninon_surprise
    show stand_Yuki_angry ## 유키 화난 표정

    ch_yuki "~~~아, 정말! 답답하게 뭐하는 거야? 안 읽어 줄 거면 차라리……"

    ## 유키 부끄러워하는 표정
    hide stand_Yuki_angry
    show stand_Yuki_shamed with dissolve

    extend "앗…… 화내는 얼굴도 어쩜 이렇게 새침하고 귀여울 수가…… 세상에……. 거울에서 눈을 뗄 수가…"

    hide stand_Yuki_shamed
    show stand_Monica ## 모니카 화난 표정

    ch_monica "둘 다 뭘 하고 있는 건가, 대체?! 니논, 편지를 이리로 넘겨라!"

    hide stand_Monica
    show stand_Ninon_surprise ## 니논 놀란 표정

    ch_ninon "……모니카 씨……? 이거……."

    hide stand_Ninon_surprise
    show stand_Monica ## 모니카 화난 표정

    ch_monica "대관절 무슨……"

    ## 모니카 놀란 표정

    ch_monica "……."

    ## 모니카 화난 표정

    ch_monica "……귀공."

    ch_monica "아무래도……"

    ch_monica "……온천에 가야만 하는 이유가 생긴 것 같다."

    ## 화면 중앙에 피로 휘갈겨 쓴 편지 이미지 show blood_letter
    ## 마을 bgm 멈춤
    ## 충격적인 효과음

    ch_nar "{color=#FF2929}「도와주세요」{/color}"

    ## 대화창 사라짐

    ## 피로 휘갈겨 쓴 편지 이미지, 길드하우스 cg F.O
    
    hide stand_Monica ##(모니카 화난 표정)
    hide bg_guildhouse

    jump black_haikei

## S# 4.검은 배경 라벨 ################################
label black_haikei:

    scene bg_black

    ch_peco "안뇽~☆ [name]! 서프라이즈예요~! 짜잔~~!!"

    ch_peco "……어라? 아무도 없는 건가요? 저~~기요~~~!! [name]~~!! 누구 없나요오~~?"

    ch_kyaru "……뭐야. 코로스케도 없고, 배고파할 것 같아서 급하게 왔더니만…… 어딜 간 거야?"

    ch_kyaru "나가서 찾아 봐야 하나…… 귀찮게 하긴."

    ch_peco "어머? 맨날 돼지니, 죽여버리니 하면서도 은근히 챙겨주려고 하네요~ 이게 바로 츤데레……라고 하는 그런 건가요? 귀여워라~☆ 착하지, 착하지……."

    ch_kyaru "여…… 역겨운 소리 하지 마! 머리도 쓰다듬지 마! 죽여버린다!!"

    ch_kyaru "……딱히 챙겨주려는 게 아니라…… 그, 그녀석한테 무슨 일이라도 생기면 코로스케도 슬퍼할 거고!"

    ch_peco "네에~ 무슨 마음인지 다 이해한답니다~"

    ch_peco "……그나저나 조금…… 쓸쓸하네요."

    ch_peco "따라오면 위험할 것 같아서 일부러 모질게 말한 건데…… 상처 받았으려나요……."

    ch_peco "미식전은 모두와 함께 맛있는 음식을 먹으며 웃고 떠드는 길드인데…… 어디로 가버린 걸까요, 그 사람……."

    ch_kyaru "뭔가 말했어, 바보린느?"

    ch_peco "아아~ 아무것도 아니에요~"

    ch_peco "……정말 아무것도, 아니에요……."

    ch_kyaru "……걱정 끼치긴, 바보가……."

    jump onsen

## S# 5. 노천탕, 길드하우스 #################
label onsen:
    scene bg_onsen with fade
    ## 노천탕 cg ## 동양풍 bgm

    player "이히~ 온천 최고~ 히히히~"

    player "흐허허~~ 바가지로 팽이놀이 해야지~ 헷헤헤~"

    ch_nar "……일단 짚고 넘어가야 할 게 있는데,"

    ch_nar "나는 바보가 아니다."

    ch_nar "바보 같이 행동하고 있지만 바보가 아니다."

    ch_nar "그렇다…… 이건 그저……"

    ch_nar "「연기」일 뿐."

    player "히히. 돌바닥 맛있다."

    ch_nar "이런 어울리지도 않는 바보 연기를 하게 된 이유를 설명하려면 하루 전날로 거슬러 올라가야 한다."

    ch_nar "그래…… 모든 일의 발단은 바로……"

    ch_nar "그 「편지」였어……!"

    player "으에— 콧물 나온다으…… 후루룹……."

    player "짭짤하당. 히히."

    ## 노천탕 cg 내리기
    hide bg_onsen
    ## 동양풍 bgm 서서히 작아지다 끄기

    ## 까만 배경
    scene bg_black ## 까만 배경에 대화창만 팝업

    ch_nar "하루 전……"

    ## 심각한 브금 서서히 커지면서 들어오기

    hide bg_black
    scene bg_guildhouse

    player "흐억……!!"

    player "뭐, 뭐야 이거?! 혈서?!"

    ## 피로 휘갈겨 쓴 편지 이미지 show blood_letter with dissolve

    ch_nar "형형색색의 꽃무늬로 화려하게 장식된 동양풍의 겉봉 속, 편지지의 새하얀 빛깔과 대비되는 검붉은 선혈이 마구잡이로 흩뿌려져 있다."

    ch_nar "벌건 가닥의 틈으로 무질서하게 엉겨 붙어 있는 덩어리들은 본연의 형태를 잃지 않으려 애쓰며 자신의 존재를 관철한다."

    ch_nar "살려 달라고 외치는 듯한 문자의 나열은 꺼림칙한 정도를 넘어 기괴한 분위기까지 자아낸다……."

    player "……”도와주세요” 라니…… 온천 초대장이 아니었어? 누가 장난친 건가?"

    show stand_Ninon_down with dissolve

    ch_ninon "아니…… 장난은 아닌 것 같소 입니다. 뒷면을 보십시오 쇼군."
    
    hide stand_Ninon_down

    ch_nar "완성되지 못한 문장들이 짤막하게 휘갈겨 쓰여 있다."

    ch_nar "알아보기 힘든 글씨체……. 편지가 쓰였을 당시의 상황이 매우 긴박했다는 것을 암시하는 듯하다."

    ## show blood_letter with dissolve

    ch_nar "{color=#FF2929}마 물이 숨 어 드ㄹ었 다{/color}"

    ch_nar "{color=#FF2929}우 리 중 ㄴㅜ 군가{/color}"

    ch_nar "{color=#FF2929}사람 , 이 사라 진{/color}"

    ch_nar "{color=#FF2929}하 ㄹㅜ에 하 나씩{/color}"

    ch_nar "{color=#FF2929}그거ㅅ에 게 들 키면{/color}"

    ch_nar "{color=#FF2929}죽 을ㅁ{/color}"

    ch_nar "{color=#FF2929}입구에서 구라노스케를 찾아주세요.{/color}"

    player "잘 나가다가 이 삐끼 같은 마무리는 뭐야."

    ## hide blood_letter with dissolve

    show stand_Kuka with dissolve ## 쿠우카 놀란 표정

    ch_kuka "저…… 정말 피로 쓴 글씨인가요……?! 히이이……."

    hide stand_Kuka
    show stand_Monica with dissolve ## 모니카 화난 표정

    ch_monica "이렇게 곳곳에 흩뿌려져 있는 형태는 인위적으로 연출했다고 보긴 어려워."

    ch_monica "모종의 이유로 피를 흘리면서까지 편지를 쓸 수밖에 없었던 상황이었을지도……."

    hide stand_Monica
    show stand_Yuki_ddung with dissolve ## 유키 뚱한 표정

    ch_yuki "잠깐, 너무 진지하게 받아들이는 거 아니야? 저 빨간 자국이 진짜 피가 맞다 쳐도, 이상한 점이 한두 개가 아니잖아."

    hide stand_Yuki_ddung
    show stand_Ninon_surprise with dissolve ## 니논 놀란 표정

    ## 니논 어둡게

    ch_ayumi "마지막 힘을 짜내어 써 놓은 편지를…… 다른 누군가가 발견해서 여기로 몰래 보내 준 것 아닐까요……? 우으…… 제가 말하면서도 무서워요……."

    hide stand_Ninon_surprise
    show stand_Monica with dissolve ## 모니카 화난 표정

    ch_monica "뭐…… 자세한 내막은 직접 가서 알아내면 될 뿐이다. 편지의 마지막에 언급된 ‘구라노스케’라는 인물에 대해서도 석연치 않은 부분이 많고……"

    ch_monica "……귀공은 어떻게 할 텐가? 위험할 수도 있는 일이다. 이건 우리가 해결해야 할 문제고, ‘바이스플뤼겔 랜드솔지부’에 소속되지 않은 귀공이 우리와 함께해야 할 의무는 없어."

    show stand_Monica at movetoleft ## 모니카 화난 표정
    show stand_Ninon at right ## 니논 웃는 표정

    ch_ninon "니논도 동의하오 입니다. 비록 쇼군과 떨어지게 되는 것은 애통하나, 쇼군이 다치는 것은 그 무엇과도 비교할 수 없는 비극 입니다!"
    
    player "……."

    hide stand_Monica
    hide stand_Ninon

    ch_nar "이 녀석들과 함께 가지 않으면…… 미식전으로 돌아가는 수밖에 없겠지."

    ch_nar "그런데 돌아간다고 해 봤자……"

    ch_nar "나를 약골에 머저리 취급하는 것들만 있는 데다, 유일하게 내 편이었던 마망도 이제는 없다."

    ch_nar "조금 멍청하긴 해도…… 이 녀석들은 내가 무슨 말을 하든 편들어주고, 귀 기울여 주는데,"

    ch_nar "차라리 여기에 있는 게 낫지 않을까?"

    ## 마을 bgm으로 변경

    player "……저기, 물어볼 게 있는데."

## 선택지 ##########################################
    menu:
        "니논에게 의견을 묻는다.":
            if love_point == ninon:
                $point_ninon += 1
            elif love_point != ninon:
                $point_ninon = 0
            
            player "니논은 내가 어떻게 했으면 좋겠어?"

            show stand_Ninon_surprise ## 니논 매우 놀란 표정

            ch_ninon "니, 니논에게 질문하셨나이까 입니다?!"

            hide stand_Ninon_surprise
            show stand_Ninon_embarassed ## 니논 당황한 표정

            ch_ninon "에……."

            hide stand_Ninon_embarassed
            show stand_Ninon_down ## 니논 시무룩한 표정

            ch_ninon "……쇼군을 보퓔하는 신하로서, 쇼군의 안녕을 최우선으로 여기는 것이 쥐당하오나……"

            hide stand_Ninon_down
            show stand_Ninon_embarassed ## 니논 당황한 표정

            ch_ninon "마음 속 깊은 곳에서는…… 쇼군이 니논들을 이끌어 달라고 외치고 있소 입니다……!!"

            hide stand_Ninon_embarassed
            show stand_Ninon_innocence ## 니논 억울한 표정

            ch_ninon "송구하기 그쥐없사옵니다, 쇼군!!! 니논은 기꺼이 할복할 것입니다!!"

            player "아니…… 할복은 안 해도 되니까……."

            player "아무튼, 니논이 그렇게까지 말한다면……"

            player "같이 갈까, 온천."

            hide stand_Ninon_innocence

            pass

        "모니카에게 의견을 묻는다.":
            if love_point == monica:
                $point_monica += 1
            elif love_point != monica:
                $point_monica = 0
            
            player "모니카는 내가 어떻게 했으면 좋겠어?"

            show stand_Monica with dissolve ## 모니카 놀란 표정

            ch_monica "……내 의견을 묻는 건가?"

            ch_monica "뭐어…… 위험할 것이라 경고하기도 했고, 귀공이 관여할 필요가 없는 일인 것도 사실이지만……"

            ## hide stand_Monica
            ## show stand_Monica ## 모니카 웃는 표정

            ch_monica "개인적인 바람으로는, 우리와 동행해 주었으면 한다."

            ch_monica "염치 없는 부탁인 것은 알고 있네."

            ch_nar "뭐?! 알고 있었다고?!"

            ch_monica "하지만…… 뭐랄까, 귀공과 함께라면 무슨 일이든 잘 풀릴 것만 같은 느낌이 들어. 단지 그뿐이다."

            ## hide stand_Monica
            ## show stand_Monica ## 모니카 당황한 표정

            ch_monica "아, 오해는 말아 다오! 의견을 물었기에 진솔하게 대답한 것일 뿐이다."

            ch_monica "몇 번이고 말하지만, 절대로 강요하지 않아. 귀공의 판단을 존중하겠네."

            player "……그런가."

            player "그럼…… 같이 가지 뭐. 나도 싫지 않아."

            hide stand_Monica

            pass
        
        "쿠우카에게 의견을 묻는다.":
            if love_point == kuka:
                $point_kuka += 1
            elif love_point != kuka:
                $point_kuka = 0

            player "쿠우카는 내가 어떻게 했으면 좋겠어?"

            show stand_Kuka with dissolve ## 쿠우카 부끄러워하는 표정

            ch_kuka "엣? 에?! 쿠, 쿠우카 말인가요?!"

            ## 쿠우카 부끄러워하는 표정으로 변경

            ch_kuka "아, 아뇨, 그…… 저기, 너무 갑작스럽게 물어보셔서……"

            ch_kuka "쿠…… 쿠우카는…………"

            ## 쿠우카 망상하는 표정으로 변경

            ch_kuka "여, 역시 안돼!! 쿠우카를 곧 버릴 물건처럼 심하게 다루어 주셨으면 좋겠다고 말하는 건 역시 무리……!! 그, 그렇군요. 그런 것이었군요! 일부러 쿠우카가 모두의 앞에서 파렴치한 말을 하도록 유도하고, 주변에서 쏟아지는 경멸의 눈빛을 버티지 못해 주저앉은 쿠우카를 들…"

            player "따라오지 말라는 거지?"

            ## 쿠우카 대사 글꼴 크기 크게 + 굵게

            ch_kuka "{size=+ 10}{b}같이 가주세요옷!!!!!!!!{/b}{/size}"

            player "처음부터 그랬으면 됐잖아……."

            player "아무튼…… 그래."

            player "같이 가자, 온천."

            hide stand_Kuka

            pass
        
        "유키에게 의견을 묻는다.":
            if love_point == yuki:
                $point_yuki += 1
            elif love_point != yuki:
                $point_yuki = 0

            player "유키는 내가 어떻게 했으면 좋겠어?"

            show stand_Yuki with dissolve ## 웃는 표정

            ch_yuki "응? 나 말이야?"

            ## 유키 자뻑하는 표정
            hide stand_Yuki
            show stand_Yuki_proud with dissolve

            ch_yuki "……흐흥♪"

            ## 유키 질색하는 표정
            hide stand_Yuki_proud
            show stand_Yuki_angry with dissolve

            ch_yuki "너 같은 건 안 따라왔으면 좋겠는데?"

            player "어?"

            ## 유키 자뻑하는 표정
            hide stand_Yuki_angry
            show stand_Yuki_proud with dissolve

            ch_yuki "……라고 하면, 정말로 안 따라올 거야?"

            player "……어…… 그게……"

            ch_yuki "농담이야~ 나랑 떨어지는 게 그렇게까지 싫었어?"

            ch_yuki "표정으로 다 드러난다구. 귀엽네~"

            ## 유키 웃는 표정
            hide stand_Yuki_proud
            show stand_Yuki with dissolve

            ch_yuki "네가 함께 가는 거라면, 난 찬성이야."

            ch_yuki "온천이니까…… 평소보다 조금 더 대담한 모습을 보여 줄 수 있겠네?"

            ## 유키 자뻑하는 표정
            hide stand_Yuki
            show stand_Yuki_proud with dissolve

            ch_yuki "꺄~ 부끄러워~"

            ch_nar "전혀 부끄러워하는 표정이 아니잖아……"

            player "대담한 모습인지 뭔지는 모르겠고…… 아무튼 같이 가자는 뜻으로 받아들이면 되는 거지?"

            player "같이 가자, 온천."

            hide stand_Yuki_proud

            pass


        "다시 생각해 보니 이것들 의견은 별로 중요하지 않은 것 같다.":
            if love_point == ninon:
                $point_ninon -= 1
            elif love_point == monica:
                $point_monica -= 1
            elif love_point == kuka:
                $point_kuka -= 1
            elif love_point == yuki:
                $point_yuki -= 1
            
            player "아니…… 아무것도 아니야."

            player "기왕 도와주기로 했는데, 갑자기 빠지는 것도 좀 이상하잖아? 같이 가자."

            pass
        
    show stand_Ninon_panic with dissolve ## 니논 놀란 표정

    ch_ninon "니논은 기쁩뉘다만……, 쇼군은 정말 괜찮으신가요 입니다……?"

    hide stand_Ninon_panic

    ch_ayumi "마, 맞아요……! 선배가 위험해지는 건 싫어……!"

    ch_ayumi "……굳이 따라오지 않으셔도 저는 24시간 내내 언제나 선배의 모습을 감상할 수 있는데…… 아, 그래도 온천이라면 유카타 차림의 선배를…… 아니, 아니지, 유카타가 문제가 아니네요……. {cps=*0.8}탕속에들어가신다면수건한장만걸치고있는선배가,거기다운이좋으면수건마저풀어헤친평소에는볼수없었던고혹적인선배의또다른은밀한모습을{/cps}"
        
    show stand_Kuka with dissolve ## 질색하는 표정

    ch_kuka "아유미 씨…… 아무리 그래도 그건 범죄라고 생각해요……"

    ch_nar "진짜 세계관 최강자들의 싸움이다……."

    hide stand_Kuka

    player "뭐…… 위험하다 해 봤자 온천일 뿐이잖아? 편지 자체가 장난일 가능성도 있고……"

    player "무엇보다 정말 위험한 곳이라면, 너희들만 가게 둘 순 없어. 함께 가자."

    ch_nar "방금 쫌 남자다웠다. 오졌다."

    show stand_Monica with dissolve ## 웃는 표정

    ch_monica "귀공의 의사가 그러하다면…… 굳이 반대할 이유는 없지."

    ch_monica "그리고, 여차할 땐 우리가 나서면 문제 없을 거다. 모두들, 이것 또한 특훈의 일환이라고 생각하고 진지하게 임하도록……!"

    hide stand_Monica
    show stand_Ninon at right ## 니논 웃는 표정

    ch_ninon "OUI!! 동국의 온천 문화가 몹쉬 기대된다 입니다!!!"

    ## 니논 어둡게
    show stand_Kuka at left ## 쿠우카 망상하는 표정

    ch_kuka "겨, 결국 가는 건가요…… 가 버리는 건가요오……!!"

    ## 쿠우카 어둡게
    show stand_Yuki with dissolve ## 유키 자뻑하는 표정

    ch_yuki "어떤 옷을 입어도 아름다운 내가 유카타를 입은 모습…… 수건 한 장으로는 감히 숨길 수 없는 미의 결정체. 그 고귀한 모습이 비쳐 흐르는, 한 폭의 그림 같은 노천탕…… 하아…… 너무 기대돼……."

    ## 유키 어둡게

    ch_ayumi "{cps=*0.8}선배가들어갈때아무도눈치채지못하게따라들어가서옷을갈아입는장면을두눈에새길수있고온천에들어가기위해수건을두르는순간도놓치지않는다면귀중한광경을두번이나볼수있는데다숙소로돌아오기위해탈의실에다시들어가는것까지카운트하면평소에절대보지못했던선배의모습을적어도네번이상{/cps}"

    ch_nar "이것들한테 진지한 걸 기대한 내가 잘못했다."

    hide stand_Kuka
    hide stand_Yuki
    show stand_Ninon at movetocenter

    ch_ninon "아, 그리고 모니카 씨—"

    ch_ninon "니논의 『시크릿 · 닌닌 정보망』에 따르면, 온천 내부의 매점에서 다양한 별미를 판매한다고 합니다."

    hide stand_Ninon
    show stand_Ninon_wink with dissolve ## 니논 윙크하는 표정

    ch_ninon "무엇보다 오에도 온천에서만 맛볼 수 있는 한정판 간식이 있다고 하네요 입니다~!"

    ## 니논 어둡게
    show stand_Monica at veryleft ## 모니카 놀란 표정

    ch_monica "뭣, 뭐라고?! 간식이라면 과자도 있다는 말인가?!"

    ch_nar "모니카 너마저……"

    ch_nar "음…… 그래도 너무 축 처지는 분위기보다는 나은가……"

    ch_nar "그래, 편하게 놀러 가는 거라고 생각하자."

    ch_nar "별일이야 있겠어?"

    hide stand_Ninon_wink
    hide stand_Monica
    hide bg_guildhouse

    ## 마을 bgm 점점 작아짐

    jump onsen_inside
## S# 6. 온천 건물 내부 #####################
label onsen_inside:
    show bg_black onlayer background
    scene bg_onsen onlayer middle with fade ## 온천내부 cg 빠르게
    show stand_gura onlayer forward with dissolve## 빠르게

    $ renpy.pause(1.5, hard = True)

    ## 충격적인 효과음

    ## 빠르게 화면전체가 돌아가는 효과
    show bg_onsen onlayer middle at fast_rotating_2

    ## 장난스러운 bgm

    hatena "오에도 온천에 어서옵쇼오————옷!!!!!!!!!!!!!!!"
    hide stand_gura

    player "으아아아악!!!!"

    ## 빠르게 화면 한 바퀴
    show bg_onsen onlayer middle at fast_rotating
    show stand_gura onlayer forward with dissolve

    hatena "입장은 몇 분임까아———앗!!!!!!!!!!!!!!!!"
    hide stand_gura onlayer forward
    
    show stand_Monica onlayer forward ## 모니카 화난 표정

    ch_monica "아아, 다섯 명으로 부탁하지."

    ## 모니카 어둡게

    ch_ayumi "엣? 여…… 여섯 명 아닌가요……?"

    ## 모니카 놀란 표정

    ch_monica "이런, 아유미의 존재를 깜빡 잊고 있었다……. 미안하군. 모습이 보이지 않아서 무심코……"

    ## 모니카 어둡게

    ch_ayumi "차…… 차라리 존재감이 없다고 해 주세요……! 모습이 안 보인다는 말은 좀 너무하잖아요……!!"

    player "아니 과장이 아니라 진짜로 안 보이는데……"

    hide stand_Monica onlayer forward

    show stand_gura onlayer forward with dissolve

    player "그, 그보다 다들, 이 녀석 생김새를 보고도 아무렇지 않은 거야?! 이건 사람이라기보다……"

    show stand_Monica onlayer forward at veryleft ## 모니카 화난 표정

    ch_monica "귀공…… 사람을 외모로 판단하는 건 나쁜 버릇이다."

    hide stand_Monica onlayer forward

    player "외모고 뭐고 사람의 형상이 아니잖……"

    ## 임시 선택지
    menu:
        "게임 이어서 계속하기":
            pass
        "유키 cg 확인하기":
            hide stand_gura onlayer forward
            hide bg_onsen onlayer middle
            hide bg_black onlayer background
            jump cg_yukifirst
        "니논 엔딩 확인하기":
            hide stand_gura onlayer forward
            hide bg_onsen onlayer middle
            hide bg_black onlayer background
            jump ninonHappy

    show stand_Yuki_ddung onlayer forward at right with dissolve ## 유키 뚱한 표정 오른쪽

    ch_yuki "맞아~ 얼른 사과해. 그 누구보다 아름다운 나조차도 남의 외모를 함부로 깎아내리진 않는다구."
    hide stand_Yuki_ddung onlayer forward
    hide stand_gura onlayer forward
    hide bg_onsen onlayer middle
    ## 길드하우스 cg + 유키 회색으로

    show bg_guildhouse onlayer middle with fade
    show stand_Yuki_angry onlayer forward with dissolve ## 회색

    ch_yuki "“……엄청나게 못생긴 마물……”"

    show stand_Yuki_ddung onlayer forward ## 회색
    hide stand_Yuki_angry onlayer forward 

    ch_yuki "“세상에…… 대체 뭘 먹고 자라면 저렇게 못생겨지는 거지……?! 윽…… 역겨워……”"

    ch_yuki "“아아— 못생긴 녀석들은 얼굴만 봐도 토할 것 같단 말이지— 얼른 죽어 주지 않으려나—”"

    hide stand_Yuki_ddung onlayer forward
    show bg_onsen
    hide bg_black onlayer background
    hide bg_guildhouse onlayer middle with fade
    

    show stand_gura with dissolve

    hatena "……홋홋홋. 괜찮습니다. 이런 건 이미 익숙하거든요……."

    hide stand_gura
    show bg_black with fade
    hide bg_onsen
    ## 아련한 bgm

    ## 구라노스케 cg 합성
    show cg_gura_baby at center_center with dissolve

    hatena "저는…… 태어날 때부터 이런 흉측한 모습이었답니다."

    player "뭔데?! 이놈은 뭔데 회상씬까지 있는 건데?!"

    hide cg_gura_baby
    ## 구라노스케 cg 합성: 울고 있는 학동 위치에 합성
    show cg_gura_child at xycenter with dissolve

    player "우와, 아까부터 합성 성의 없어……"

    hatena "당연히 이런 저를 받아 주는 사람이 있을 리 없었고……"

    hatena "단지 이렇게 생겼다는 이유 하나만으로 괴물이라 놀림 받으며, 심한 괴롭힘을 당하는 나날들이 계속되었지요……."

    hide cg_gura_child
    show bg_onsen with fade
    hide bg_black

    show stand_gura with dissolve

    hatena "여기, 오에도 온천이 저의 진가를 알아봐 주기 전까지는 말입니다……!!"

    hatena "모두가 손가락질만 하던 그때, 오에도 온천은 저에게 손을 내밀어 주었죠……"

    hatena "이렇게 웃기게 생긴 놈은 난생 처음 본다며 온천의 마스코트로서 일해 볼 생각이 없냐는 제안을 했습니다."

    player "그게 더 심한 말인 것 같은데……"

    hatena "과거의 아픔은 과거에 묻어 두고, 저는 제가 할 수 있는 일을 해야만 했습니다……!"

    hatena "잘못을 저지른 건 제가 아니라 저를 괴롭혔던 그들인데, 왜 고통받는 건 저여야 하는지 이해할 수 없었죠…… 그래서 더욱 악착같이 노력했습니다."

    hatena "그리고 이제는 아무도 저를 무시하지 못하게 되었어요…… 제가 없는 오에도 온천은 더 이상 오에도 온천이 아니게 되었고, 모두가 저를 믿고 따르는 위치까지 오르게 되었습니다……! 홋홋홋!"
    
    hide stand_gura
    ## 니논 억울한 표정
    show stand_Ninon_innocence with dissolve

    ch_ninon "히끅히끅 입니다…… 너무나도 쮜쮜가 아픈 이야기가 아닐 수 없습니다……!"

    hide stand_Ninon_innocence

    player "근데 그게 동물원 원숭이랑 다를 게 뭐……"

    ## 아련한 bgm off

    ## 장난스러운 bgm

    show stand_gura with dissolve

    hatena "잡설은 이쯤 하고——"

    show bg_onsen at fast_rotating

    ch_gura "제 이름은 구라노스케!!!! 쇼군 여러분!!!!! 모시게 되어 영광임다아———앗!!!!!!"

    hide stand_gura

    ## 모니카 놀란 표정
    show stand_Monica_surprised with dissolve

    ch_monica "뭐…… 이 자가 편지에 적혀 있던 바로 그……!"

    hide stand_Monica_surprised
    show stand_gura with dissolve

    ch_gura "그렇습니다!!!! 당신들에게 편지를 보낸 건 바로 저였슴다아———앗!!!!"

    hide stand_gura
    ## 쿠우카 놀란 표정
    show stand_Kuka_surprised with dissolve

    ch_kuka "그…… 그렇다면 제대로 설명을 해 주세요……!"

    ch_kuka "그 피 묻은 편지는 뭐였고, 정말로 이 온천에 마물이 숨어 있는 건지도……!"

    hide stand_Kuka_surprised
    show stand_gura with dissolve

    ch_gura "홋홋홋! 알겠습니다…… 차근차근 하나씩 설명해 드리도록 하죠."

    ch_gura "그보다, 여기는 너무 눈에 띄는 것 같군요. 조용한 곳으로 자리를 옮깁시다."

    hide stand_gura
    hide bg_onsen with fade

    jump routen
## S# 7. 노천탕 ############################
label routen:
    ## 심각한 bgm으로 변경
    ## 노천탕 cg DIS
    show bg_routen

    show stand_gura with dissolve

    ch_gura "이곳은 오에도 온천이 처음 생겼을 때부터 있었던 유서 깊은 노천탕입니다…… 모종의 이유로 지금은 사용하지 않고 있지만요."

    ch_gura "그럼 우선…… 여러분은 ‘아쿠다이칸’을 기억하십니까?"

    hide stand_gura

    ## 모니카 웃는 표정
    show stand_Monica with dissolve

    ch_monica "우리의 손으로 직접 쓰러뜨린 놈이다, 기억하지 못할 리가 없지."

    hide stand_Monica
    show stand_gura with dissolve

    ch_gura "맞습니다. 쇼군과 여러분의 활약으로 평화를 되찾기 전까지 이곳 오에도를 공포로 몰아넣었던 악당이죠."

    hide stand_gura
    ## 유키 질색하는 표정
    show stand_Yuki_angry with dissolve

    ch_yuki "지독한 녀석이었지~ 마물 주제에 왕궁 세력과 결탁할 생각을 다 하고 말야."

    show stand_Yuki_ddung
    hide stand_Yuki_angry

    ch_yuki "그런데 그건 갑자기 왜? 죽었던 녀석이 부활이라도 한 거야?"

    hide stand_Yuki_ddung

    show stand_gura with dissolve

    ch_gura "아뇨…… 아쿠다이칸은 확실히 사라졌습니다. 하지만……"

    ch_gura "……녀석이 온 마을을 헤집으며 날뛸 때, 또 다른 마물이 어딘가에 몸을 숨기고 있었고……"

    ch_gura "지금, 이곳의 사람들이 쥐도 새도 모르게 사라지는 현상이 그 마물의 소행이라고 하면…… 믿으시겠습니까?"

    ## 구라노스케 어둡게

    ch_ayumi "힉……."

    hide stand_gura

    ## 니논 놀란 표정
    show stand_Ninon_surprise with dissolve

    ch_ninon "NON……!"

    hide stand_Ninon_surprise
    show stand_Monica_surprised with dissolve

    ch_monica "그 말은……"

    ## 모니카 화난 표정
    show stand_Monica_ddung
    hide stand_Monica_surprised

    ch_monica "아쿠다이칸은 눈속임……이었다는 건가?"

    hide stand_Monica_ddung
    show stand_gura with dissolve

    ch_gura "안타깝지만 거기까진 저도 모르겠습니다."

    ch_gura "아쿠다이칸의 난동이 시선을 돌리기 위한 놈의 계획이었을지…… 애초부터 서로 관련이 없었던 것일지…… 현재로서는 알 방법이 없습니다."

    ch_gura "다만 확실한 것은…… 끝난 줄만 알았던 오에도의 공포가, 아직까지도 살아남아 저희를 옥죄고 있다는 점입니다."

    hide stand_gura
    ## 니논 놀란 표정
    show stand_Ninon_surprise with dissolve

    ch_ninon "그…… 그럼 편쥐는 도당채 어떻게 된 것이오 입니다?"

    hide stand_Ninon_surprise
    show stand_gura with dissolve

    ch_gura "아, 편지…… 말입니까."

    ch_gura "홋홋홋. 그다지 유쾌한 이야기는 아닐 테지만…… 설명해 드리겠습니다."

    ch_gura "여러분에게 그 편지를 보낸 것은 제가 맞습니다만……. 편지를 쓴 것은 제가 아닙니다."

    hide stand_gura

    ## 유키 뚱한 표정
    show stand_Yuki_ddung with dissolve

    ch_yuki "그럼……?"

    hide stand_Yuki_ddung
    show stand_gura with dissolve

    ch_gura "……언제부터 였을까요. 이 온천에 이상한 기운이 감돌기 시작했습니다."

    ch_gura "온천의 활기찬 분위기와, 기분 좋은 따뜻함은 이전과 다를 바가 없었죠."

    ch_gura "다만 한 가지……"

    ch_gura "온천의 직원들이 하나둘씩…… 사라져 갔습니다."

    ch_gura "기이한 점은, 직원들 간의 유대가 강해 서로가 서로에 대한 것을 낱낱이 알고 있었음에도 불구하고……"

    ch_gura "누군가 사라지고 난 뒤면, 마치 그 사람이 처음부터 존재하지 않았던 것처럼 행동했습니다. 저를 제외한 모두가요."

    ch_gura "처음에는 제가 꿈을 꾸고 있는 건지, 과로 때문에 정신병에 걸리기라도 한 건지 의심했습니다……."

    ## 피로 휘갈겨 쓴 편지 이미지

    ch_gura "……그 편지를 ‘발견’하기 전까지는 말이죠."

    hide stand_gura
    ## 모니카 화난 표정
    show stand_Monica_ddung with dissolve

    ch_monica "아유미의 추측이 맞았던 건가…… 예리하군."

    ## 모니카 cg 어둡게

    ch_ayumi "아…… 헤헤……."

    hide stand_Monica_ddung
    show stand_gura with dissolve

    ch_gura "놈이 무슨 술수를 쓴 것인지는 모릅니다…… 하지만, 이런 짓을 할 수 있는 건 마물밖에 없을 테죠."

    ch_gura "마물이라는 확신이 들었지만…… 저는 놈의 정체도, 능력도 알 수 없었어요."

    ch_gura "우리 중 한 사람으로 변장하여 연기를 하고 있을지, 온천의 어딘가에 숨어있을지…… 아무것도 알 수 없었습니다."

    ch_gura "그래서 몰래 도움을 요청해야 했습니다. 누구에게도 들키지 않을 방식으로 말이죠."

    hide stand_gura
    ## 쿠우카 놀란 표정
    show stand_Kuka_surprised with dissolve

    ch_kuka "그……그래서 온천의 초대장인 것처럼 위장한 편지를 보낸 거였군요……!"

    hide stand_Kuka_surprised
    show stand_gura with dissolve

    ch_gura "맞습니다. 많이 놀라셨을 테죠…… 하지만 이 방법밖에 없었습니다. 여러분은 아쿠다이칸을 무찌르신 분들이기도 하고요……."

    hide stand_gura
    ## 모니카 화난 표정
    show stand_Monica_ddung with dissolve

    ch_monica "뭐, 상황이 그러했다면 어쩔 수 없지. 어찌 되었든 우리를 이곳으로 불러내는 것에도 성공했으니……"

    ch_monica "……그런데, 우리는 뭘 하면 되지? 정보가 없는 건 이쪽도 마찬가지인데……"

    hide stand_Monica_ddung
    show stand_gura with dissolve

    ch_gura "아, 그것에 대해서 말인데요. 여러분은……"

    ## 장난스러운 bgm
    ## 빠르게 화면 한 바퀴 돌아가는 효과
    show bg_routen at fast_rotating

    ch_gura "편안히 온천을 즐기시면 됨다아———앗!!!!"

    hide stand_gura

    ## 유키 질색하는 표정
    show stand_Yuki_ddung with dissolve

    ch_yuki "…………하?"

    hide stand_Yuki_ddung
    ## 니논 화난 표정
    show stand_Ninon_angry with dissolve

    ch_ninon "지…… 지금 우리랑 장놘치자는 거냐! 입니다!"

    hide stand_Ninon_angry
    show stand_gura with dissolve

    ch_gura "반은 장난이고, 반은 진심입니다."

    ch_gura "분위기가 너무 딱딱해진 것 같아서요. 홋홋홋."

    hide stand_gura
    ## 모니카 화난 표정
    show stand_Monica_ddung with dissolve

    ch_monica "……계속해 보게."

    hide stand_Monica_ddung
    show stand_gura with dissolve

    ch_gura "말씀드렸다시피, 저는 마물에 대해 아는 것이 아무것도 없습니다. 하지만 단신으로 마물의 흔적을 찾는 것은 너무 위험했어요."

    ch_gura "지금까지 제가 무사하다는 건, 아직은 놈이 저의 거동에서 아무런 낌새도 느끼지 못했다는 뜻이겠지요."

    ch_gura "이런 상황에서 섣불리 평소에 하지 않던 행동을 하거나 하면…… 저까지 제거당할지도 모릅니다."

    ch_gura "그래서 여러분의 도움이 절실한 겁니다. 아무것도 모르는 손님인 척 온천을 즐기며, 틈틈이 곳곳에서 단서를 찾아내시면 됩니다! 홋홋홋!"

    hide stand_gura
    ## 니논 시무룩한 표정
    show stand_Ninon_down with dissolve

    ch_ninon "……그런데, 입니다?"

    ch_ninon "그 계회꾸에는 취명적인 헛점이 있는 것 같소 입니다……."

    player "헛점? 무슨……?"

    ch_ninon "이미 오에도 마을의 모두는 쇼군의 활약을 직줩 목도하고, 쇼군의 업줙을 기리기 위해 동상까지 세웠다 입니다."

    ch_ninon "이런 상황에서 니논들이 아무고토 모르는 춱해봤자…… 금방 들통날 것입니다! 쇼군을 알아보지 못할 리가 없다 입니다!!"

    hide stand_Ninon_down
    show stand_gura with dissolve

    ch_gura "날카로우시군요."

    ## 심각한 bgm으로 변경

    ch_gura "하지만 그건.…… 조금 슬픈 일입니다만, 걱정하지 않으셔도 될 겁니다."

    hide stand_gura
    ## 쿠우카 시무룩한 표정
    show stand_Kuka_down with dissolve

    ch_kuka "슬픈 일……? 무슨 말인가요……?"

    hide stand_Kuka_down

    show stand_gura with dissolve

    ch_gura "그나마 여러분들처럼 외부에서 온 관광객들이 온천을 방문하는 경우는 간혹 있지만, 오에도 주민들의 발길은 언제부터인가 뚝 끊겼습니다. 이것도 마물의 영향인지는 모르겠습니다만……"

    ch_gura "그리고, 직원들 중 아쿠다이칸 토벌 작전을 지켜보았던 토박이들은……"

    ch_gura "……전부 사라졌습니다. 부족한 일손은 오에도 마을에 새로 이사 온 이들과 외부인으로 충당되었죠……."

    ## 구라노스케 어둡게

    ch_ayumi "그런……."

    ## 구라노스케 밝게

    ch_gura "하지만 오히려 이것을 무기로 사용할 수 있을지도 모르죠. 만약 쇼군이나 여러분의 정체를 알아보는 이가 있다면…… 그를 의심해 봐도 좋을 겁니다. 불행 중 다행이죠?"

    hide stand_gura
    ## 니논 시무룩한 표정
    show stand_Ninon_down with dissolve

    ch_ninon "쇼군의 동상은 어취합니카? 그걸 보고 쇼군의 얼굴을 알아보면……."

    ## 유키 질색하는 표정 화면 오른쪽에
    show stand_Yuki_angry at right with dissolve

    ch_yuki "아니 그거, 솔직히 안 닮았거든."

    hide stand_Yuki_angry
    hide stand_Ninon_down

    show stand_gura with dissolve

    ch_gura "홋홋홋…… 실물이 훨씬 멋지십니다."

    ch_nar "하긴…… 동상 따위가 내 잘생김을 전부 담을 수 있을 리가 없지……."

    ch_gura "그렇지만 아무래도 확실히 해 두는 게 좋겠죠."

    ch_gura "니논 님의 말씀대로, 여러분이 쇼군과 그 일행분들이라는 사실이 들통날 가능성을 완전히 배제할 순 없습니다."

    ch_gura "마물이 아닌 인간이 여러분의 정체를 눈치챈다면, 그건 아마 오에도 마을에 퍼져 있는 ‘쇼군 영웅담’ 때문일 겁니다."

    ## 모니카 놀란 표정 화면 왼쪽에
    show stand_Monica_surprised at left with dissolve

    ch_monica "그, 그 일화가 아직까지 거론되고 있다고……?! 아니, 동상까지 세워졌으니 어쩌면 당연한 것일지도……"

    ## 모니카 어둡게, 쿠우카 망상하는 표정 화면 오른쪽에
    show stand_Kuka_mousou at right with dissolve

    ch_kuka "히에엑……!! 쿠, 쿠우카는 자신도 모르는 사이에 이야깃거리가 되어 얼굴 한 번 본 적 없는 사람들에게 메차쿠차 소비되고 있었던 거네요……!! 죽을 때까지 대중의 시선으로부터 자유롭지 못한 채 끝없이 능욕당하는 운명!!! 지금까지 겪어 온 수모와는 비교할 수 없을 정도로 자극이 강할지도……!!!! 크흣, 크헤헷……."

    hide stand_Kuka_mousou
    hide stand_Monica_surprised

    show stand_gura with dissolve

    ch_gura "음…… 그러니까 제가 드리고 싶은 말씀은…… 여러분이 영웅담의 주연들이라는 생각이 전혀 들지 않게끔 연기를 하시는 건 어떨까 합니다."

    player "연기를 하라고……?"

    ch_gura "쇼군 님을 예로 들자면……"

    ch_gura "당찬 모습으로 영웅호걸들을 거느리던 바로 그 쇼군이라는 생각이 전혀 들지 않을 정도로, 어딘가 모자란 사람인 것처럼 연기를 하시는 거죠."

    hide stand_gura
    ## 니논 시무룩한 표정
    show stand_Ninon_down with dissolve
    ch_ninon "……확실히…… 쇼군이 바보똥개처럼 행동한다면, 누구도 쇼군을 알아보는 일은 없을 것이다 입니다."

    ## 니논 화난 표정
    show stand_Ninon_angry
    hide stand_Ninon_down

    ch_ninon "그…… 그렇쥐만, 감히 쇼군께 바보똥멍청이 연기를 하라는 건 너무 무례하오 입니다……!"

    hide stand_Ninon_angry

    show stand_gura with dissolve

    ch_gura "그, 그렇게까지 말하지는 않았지만……."

    ch_gura "영웅담 속의 쇼군이 연상되는 모습을 보이는 것만 피하신다면, 크게 문제가 없을 듯합니다."

    hide stand_gura
    ## 니논 시무룩한 표정
    show stand_Ninon_down with dissolve

    ch_ninon "Umm…… 일뤼가 있는 말이긴 합니다만, 쇼군은 바보멍청이해삼똥개말미잘 연기를 하시는 것이 정말 괜찮으신가요 입니다……?"

    hide stand_Ninon_down

    ch_nar "왜 수식어가 점점 늘어나……! 뭘 바라는 거야!"

    show stand_gura with dissolve

    ch_gura "아, 근데 나머지 분들은 평소대로 행동하셔도 상관없을 것 같네요."

    hide stand_gura
    
    ch_nar "나만 해야 되는 거냐고!!"

    show stand_gura with dissolve

    ch_gura "모니카 님의 하늘을 가르는 일섬, 쿠우카 님이 입으신 천녀의 날개옷, 아쿠다이칸을 끝장낸 니논 님의 수리검, 하늘도 질투하는 유키 님의 미모……"

    ch_gura "전투가 벌어지거나 하지 않는 이상, 구전되는 특징만으로 여러분을 알아보는 것은 어렵지 않을까 싶습니다."

    ch_gura "그나마 자세히 묘사된 유키 님의 외모도 ‘미의 화신’, ‘백옥보다 하얗고, 매화보다 아름답다’ 정도로 전해질 뿐이지, 이야기만 듣고서 유키 님이라는 걸 확신하지는 못할 것 같네요."

    hide stand_gura

    ## 유키 자뻑하는 표정
    show stand_Yuki_proud with dissolve

    ch_yuki "뭐, 나보다 아름다운 사람은 이 세상에 없으니, 내 미모를 실제로 보게 된다면 내가 유키 님이라는 걸 알아챌지도 모르겠네♪"

    ch_yuki "그치만, 일부러 못생겨지는 건 불가능하니까…… 나도 참, 너무 예뻐도 곤란한걸……♪"

    ## 유키 어둡게

    ch_ayumi "그보다 제 얘기는 왜 또 빠져 있는 건가요!!!!!"

    hide stand_Yuki_proud

    player "그…… 내키지는 않지만, 나 때문에 계획을 망칠 순 없으니까……"

    player "까짓것 해 보지 뭐. 이제부터 바보처럼 행동하면 되는 거지?"

    ## 니논 억울한 표정
    show stand_Ninon_innocence with dissolve

    ch_ninon "쇼…… 쇼군이 희생하신다니……!!"

    hide stand_Ninon_innocence

    ## 심각한 bgm 멈춤

    player "테에엥 마망……."

    ## 모니카 시무룩한 표정
    show stand_Monica_down with dissolve

    ch_monica "??"

    hide stand_Monica_down

    player "응애 나 애기프붕."

    ## 유키 질색하는 표정
    show stand_Yuki_angry with dissolve

    ch_yuki "……."

    hide stand_Yuki_angry

    player "응애 맘마조."

    ## 쿠우카 질색하는 표정
    show stand_Kuka_hiku with dissolve

    ch_kuka "…………"

    player "바…… 바보처럼 연기하라며……? 반응들이 왜 이래?"

    ## 장난스러운 bgm 점점 커짐

    ## 쿠우카 놀란 표정
    show stand_Kuka_surprised
    hide stand_Kuka_hiku

    ch_kuka "………핫?! 아, 그, 그랬죠……. 너무 실감나게 연기하셔서…… 쿠우카, 순간 진심으로 도S 씨를 경멸할 뻔했어요……"

    hide stand_Kuka_surprised
    ## 모니카 놀란 표정
    show stand_Monica_surprised with dissolve

    ch_monica "귀, 귀공은 과연 굉장하군…… 나도 모르게 검을 뽑을 뻔했어……"

    hide stand_Monica_surprised
    ## 니논 억울한 표정
    show stand_Ninon_innocence with dissolve

    ch_ninon "이 줭도로 열과 성의를 다 하실 줄이야 입니다…… 니논, 몹쉬 감동했소 입니다……!"

    hide stand_Ninon_innocence
    show stand_gura with dissolve

    ch_gura "후…… 훌륭합니다……! 그 누구도 쇼군이라고는 절대 생각지 못할 엄청난 연기……!!"

    hide stand_gura

    ch_nar "음…… 콧코로 앞에선 평소에도 이렇게 한다는 사실은 숨기는 게 좋겠지……."

    player "그러면…… 이제 온천으로 들어갈 수 있는 건가?"

    show stand_gura with dissolve

    ch_gura "아, 네! 웬만한 건 모두 설명 드린 것 같으니…… 바로 안내해 드리겠습니다!"

    ch_gura "그럼, 이쪽으로……"

    hide stand_gura

    ## 장난스러운 bgm 서서히 작아짐

    hide bg_routen


    jump scene_eight
## S# 8. 온천 건물 내부 #####################
label scene_eight:
    ## 동양풍 bgm
    #3 온천 건물 내부 cg 
    scene bg_onsen_heya_01 onlayer middle
    show bg_black onlayer background

    show stand_gura onlayer forward with fade

    ch_gura "이제부터 보여 드릴 것은, 저희 온천의 야심 찬……"

    show bg_onsen_heya_01 onlayer middle at fast_rotating

    ch_gura "『유카타』 임다아————앗!!!!!"

    ch_gura "마음에 드는 걸로 하나씩 골라 줍쇼오————옷!!!!!"

    show bg_onsen_heya_01 onlayer middle at fast_rotating

    hide stand_gura onlayer forward
    ## 니논 놀란 표정
    show stand_Ninon_surprise onlayer forward with dissolve

    ch_ninon "우오오오옷——!!!!! 동국의 의복 문화 스게에———엣!!!!!!!!"

    hide stand_Ninon_surprise onlayer forward

    ch_ayumi "니…… 니논 씨의 상태가 이상해요……?"

    ## 니논 비장한 표정
    show stand_Ninon_daiji onlayer forward with dissolve

    ch_ninon "아무것도 이상할 것 없다 입니다! 이것은 매우 자연스러운 동국의 예법 입니다!"

    ch_ninon "『인법 · 동국의 이런 점이 대단하다』 !!"

    ch_ninon "별것도 아닌 걸 보면서 과도한 GESTURE 와 함께 호들갑을 떠는 인술 입니다! 여러분도 따라해 보세요 입니다!!"

    hide stand_Ninon_daiji onlayer forward

    ## 쿠우카 대사로 넘어갈 때 까지 구라노스케 서서히 축소
    hide bg_onsen_heya_01 onlayer middle with fade
    $ camera_move(0, 0, 600, 0, 0)
    show stand_gura onlayer forward with dissolve 
    $ camera_move(0, 0, 300, 0, 3)

    ch_gura "……별것도……"

    $ camera_move(0, 0, 0, 0, 3)

    ch_gura "………아닌 거………"

    show bg_onsen_heya_01
    hide stand_gura onlayer forward
    hide bg_black onlayer background

    ## 쿠우카 놀란 표정
    show stand_Kuka_surprised with vpunch

    ch_kuka "예, 예뻐요!! 정말 예뻐요!!! 쿠, 쿠우카는 이걸로 할게요……."

    hide stand_Kuka_surprised
    ## 니논 웃는 표정
    show stand_Ninon with dissolve

    ch_ninon "니논은 이것으로 하겠소 입니다~! 동국의 정열적인 SOUL이 느껴진다 입니다!"

    






    

    return
## 미니 게임 CG 라벨 ########################
label ninon_win:

    return
## 니논 루트 ################################
label ninon:
    $ camera_reset()
    scene bg_room onlayer background with fade
    play music "audio/main/LostPrincessmain.mp3"

    centered "니논의 방"

    show stand_Ninon onlayer forward at rotated

    ch_ninon "앗,와줬구나!"

    ch_ninon "탁구 한 판 하지 않을래?"

    menu:
        "응":
            call play_pong from _call_play_pong
    

        "아니":
            pass
    
    if(win_point > 2):
        show ninon_pingping onlayer forward with fade
        
        
        ch_ninon "이것이 사무라이 정신이다, 입니다!\n천하통일의 염원을 담은 SERVE를 받아라 입니다!\n「인법 · 후쥐산 쪼궤기」~! 슈바바바밧!"

        hide ninon_pingping onlayer forward with fade
        
        centered "다시 게임"
    else:
        centered "다시 게임" 

    show stand_Ninon onlayer forward with dissolve

    menu:
        "+1":           
            $love_point = love_point + 1
            
        "0":
            $love_point = love_point
        "-1":
        
            $love_point = love_point - 1

    menu:
        "+1":
            
            $love_point = love_point + 1
        "0":
            $love_point = love_point
        "-1":
            
            $love_point = love_point - 1
    
    menu:
        "+1":
            
            $love_point = love_point + 1
        "0":
            $love_point = love_point
        "-1":
            
            $love_point = love_point - 1
    
    if(love_point == 3):
        jump ninonHappy

    if(love_point == 2):
        jump Success

    if(love_point == 0 or love_point == 1):
        jump Badkyaru
    
    if(love_point == -1 or love_point == -2):
        jump Kimura
    
    if(love_point == -3):
        jump BAD

    return


## 모니카 루트 ###################################
label monica:
    scene bg_room with fade
    play music "audio/main/LostPrincessmain.mp3"
    centered "모니카의 방"
    show stand_Monica with dissolve

    $ camera_move(-70, 130, 1000, 0, 5)

    show stand_Monica at movetoright


    ch_monica "음..."

    show stand_Monica at movetoleft

    ch_monica "아직인걸까..."

    show stand_Monica at movetocenter

    ch_monica "왔구나!"

    menu:
        "+1":           
            $love_point = love_point + 1
            call cg_monicafirst from _call_cg_monicafirst

        "0":
            $love_point = love_point
        "-1":
        
            $love_point = love_point - 1

    menu:
        "+1":
            
            $love_point = love_point + 1

        "0":
            $love_point = love_point
        "-1":
            
            $love_point = love_point - 1
    
    menu:
        "+1":
            
            $love_point = love_point + 1
        "0":
            $love_point = love_point
        "-1":
            
            $love_point = love_point - 1
    
    if(love_point == 3):
        jump monicaHappy

    if(love_point == 2):
        jump Success

    if(love_point == 0 or love_point == 1):
        jump Badkyaru
    
    if(love_point == -1 or love_point == -2):
        jump Kimura
    
    if(love_point == -3):
        jump BAD

    return

## 쿠우카 루트 #############################
label kuka:
    $ camera_reset()
    scene bg_room onlayer background with fade
    play music "audio/main/LostPrincessmain.mp3"
    centered "쿠우카의 방"
    show stand_Kuka with dissolve

    $ layer_move("background", 2000)
    $ layer_move("middle", 1500)
    $ layer_move("forward", 1000)
    show A onlayer middle
    show B onlayer forward
    with dissolve
    $ camera_move(-70, 130, 1000, 0, 5)

    menu:
        "+1":           
            $love_point = love_point + 1
        "0":
            $love_point = love_point
        "-1":
        
            $love_point = love_point - 1

    menu:
        "+1":
            
            $love_point = love_point + 1
        "0":
            $love_point = love_point
        "-1":
            
            $love_point = love_point - 1
    
    menu:
        "+1":
            
            $love_point = love_point + 1
        "0":
            $love_point = love_point
        "-1":
            
            $love_point = love_point - 1
    
    if(love_point == 3):
        jump kukaHappy

    if(love_point == 2):
        jump Success

    if(love_point == 0 or love_point == 1):
        jump Badkyaru
    
    if(love_point == -1 or love_point == -2):
        jump Kimura
    
    if(love_point == -3):
        jump BAD

    return

## 유키 루트 ###########################
label yuki:
    scene bg_room with fade
    play music "audio/main/LostPrincessmain.mp3"
    centered "유키의 방"
    show stand_Yuki with dissolve

    menu:
        "+1":           
            $love_point = love_point + 1
        "0":
            $love_point = love_point
        "-1":
            $love_point = love_point - 1

    menu:
        "+1":
            
            $love_point = love_point + 1
        "0":
            $love_point = love_point
        "-1":
            
            $love_point = love_point - 1
    
    menu:
        "+1":
            
            $love_point = love_point + 1
        "0":
            $love_point = love_point
        "-1":
            
            $love_point = love_point - 1
    
    if(love_point == 3):
        jump yukiHappy

    if(love_point == 2):
        jump Success

    if(love_point == 0 or love_point == 1):
        jump Badkyaru
    
    if(love_point == -1 or love_point == -2):
        jump Kimura
    
    if(love_point == -3):
        jump BAD

    return

## CG ################################   
label cg_ninonfirst:

    centered "목욕가운 차림으로 탕에 몸을 담근 채 부끄러워 하며 주인공을 힐끔 보는 니논"


    return

label cg_ninonsecond:

    centered "열정적으로 탁구를 치는 유카타 차림의 니논"

    return

label cg_monicafirst:

    centered "한 손으로 목욕가운을 붙잡고 부끄러운 표정으로 주인공을 노려보는 볼빵빵 모니카"

    $ persistent.unlock_1 = True

    return

label cg_monicasecond:

    centered "달콤한 화과자를 먹으며 눈빛을 반짝이는 유카타 차림의 모니카"

    return

label cg_kukafirst:

    centered "탕 속에서 망상에 빠져 침을 흘리자 엄지손가락으로 입을 닦아주는 주인공을 깜짝 놀란 표정으로 바라보는 목욕가운 차림의 쿠우카"

    return

label cg_kukasecond:

    centered "오비가 풀려 유카타가 벗겨지려 하자 자신을 껴안아서 가려주는 주인공을 부끄러운 표정으로 바라보는 쿠우카"

    return
## S# 11. 유키 1번 cg
label cg_yukifirst:

    ## 유키 1번 cg 배경
    scene cg_yuki_01 with fade

    ## 동양풍 bgm

    player "후우……"

    player "별로 한 것도 없는데 왜 이리 피곤하지……?"

    ## 유키 1번 cg 표정 1로 변경

    ch_yuki "흥~ 흐흥……♬"

    ch_nar "이 녀석은 뭐가 그렇게 신나는 걸까……"

    ch_nar "……."

    ch_nar "그나저나 보면 볼수록 놀랍다."

    ch_nar "이 녀석이 ‘남자’라는 게……"

    ch_nar "길고 진한 속눈썹."

    ch_nar "잡티 하나 없이 뽀얀 피부."

    ch_nar "호리하고 가냘픈 몸매……"

    ch_nar "어디를 어떻게 봐도 여자애다."

    ch_nar "사실 남자라는 건 거짓말 아닐까……?"

    ch_nar "뭐…… 곧 확인해 볼 수 있겠지만……"

    ## 유키 1번 cg 표정 2

    ch_yuki "응?"

    ch_nar "아…… 눈 마주쳤다."

    ch_nar "너무 빤히 보고 있었나……." 

    ## 유키 1번 cg 표정 3

    ch_yuki "헤에~ [name], 아름다운 내 몸에 관심 있어?"   

    ch_yuki "좀 더 가까이서 봐도 괜찮아~ 백옥 같은 내 살결을 직접 볼 수 있는 기회는 흔치 않으니까."
    
    player "아…… 응……."

    ch_yuki "만져 보고 싶어?"

    player "그런 말은 안 했……"

    ch_yuki "그건 곤란한걸…… 완벽한 내 피부에 흠이라도 생긴다면 그건 곧 전 지구적 손실이라서."
    
    player "그런 말 안 했다고!!!"

    ch_yuki "아니면……"

    ## 충격적인 효과음

    ## 유키 1번 cg 완

    ch_yuki "내 {color=#FF2929}아름다움{/color}이 잔뜩 배어 있는 {color=#FF2929}팬티{/color}라도 가질래?"

    ch_yuki "너에게만 주는 특권이야♪"

    player "필요 없어!!!!"

    ch_yuki "부끄러워하긴~ 나중에 후회해도 모른다?"

    ch_nar "저런 정신 나간 말을 아무렇지 않게 할 수 있는 것도 재능이 아닐까……."

    hide cg_yuki_01

    return

label cg_yukisecond:

    centered "탕에 몸을 반쯤 담근 채 요염한 자세로 주인공을 바라보는 유키"

    return
                
## 엔딩 ##################
## 니논 해피 엔딩 #########
label ninonHappy:

    ## 아련한 bgm

    ## 통학로 cg
    scene bg_tyugaku

    ch_nar "평소와 다를 것 없는 하루,"

    ch_nar "—였다고 생각했다."

    ch_nar "츠바키가오카의 하굣길은 인적이 드문 편이다."

    ch_nar "하염없이 누군가를 기다리는 금발의 미소녀가 눈에 띄지 않는 것이 이상할 정도로 말이다."

    ch_nar "귀가부인 나보다도 한 발 먼저 학교를 빠져나온 뒤, 거리가 꽤 되는 오린도 고교에서부터 쉬지 않고 달려와 매일 같은 자리에서 나를 기다리던 소녀."

    ch_nar "도시전설과도 같은 비일상적 일상."

    ch_nar "그 빈번함에 취해 소중한 것에 감사하는 법을 잊어서일까."

    ch_nar "언제나 모퉁이에 쪼그려 앉아 “인법 · 다랑어의 술!” 따위를 외치며 길고양이들을 규합하던 그녀의 모습은 온데간데없었다."

    ch_nar "구심점을 상실한 패거리만이 갈 곳을 잃은 채 거리를 서성일 뿐이었다."

    player "……."

    hide bg_tyugaku
    show bg_tyugaku_running

    ## 달려가는 효과음

    ch_nar "정신을 차려 보니 나는 달리고 있었다."

    ch_nar "무서웠다."

    ch_nar "그녀의 황금빛 머리칼이,"

    ch_nar "에메랄드처럼 반짝이는 눈동자가,"

    ch_nar "현실이 아닐지도 모른다는 공포."

    ch_nar "하루 정도는 늦을 수도 있다."

    ch_nar "청소 당번이 되었거나, 진로 상담을 하느라 늦어진 것일 수도 있다."

    ch_nar "그러나 그런 것을 생각할 여유가 내게는 없었다."

    ch_nar "그저 달리는 것에만 집중했다."

    hide bg_tyugaku_running
    show bg_tyugaku_stop

    ## 달려가는 효과음 멈춤

    ch_nar "숨이 턱까지 차올랐다."

    ch_nar "벽에 팔을 걸친 채 있는 힘껏 기침을 해 댔다."

    ch_nar "구역질이 나왔다."

    ch_nar "그녀의 모습을 두 눈에 새기기 전까지는 멈출 수 없었다."

    ch_nar "심장이 터질 것 같은 고통조차도,"

    ch_nar "그녀를 다시 볼 수 없을지 모른다는 공포로부터 나를 벗어나게 할 수는 없었다."

    ch_nar "마지막 잡념을 토해내고는 오린도 고교를 향해 고개를 쳐들었다."

    show cg_ninon_happy_01 with dissolve
    hide bg_tyugaku_stop

    $ renpy.pause(1, hard = True)

    ch_nar "……그녀의 모습이 보였다."

    ch_nar "순간 구원을 받는 듯한 감각이 느껴졌다."

    ch_nar "그러나 이내, 더 큰 공포가 나를 덮쳐 왔다."

    show cg_ninon_happy_02 with dissolve
    hide cg_ninon_happy_01

    ch_nar "늘상 헤프게 웃음을 흘리던 그녀의 얼굴이…… 생소한 미소를 머금은 채 나를 응시한다."

    ch_nar "오늘따라 그녀가 낯설게 느껴진다."

    ch_nar "저런 표정도 지을 수 있었구나."

    ch_ninon "쇼군."

    ch_nar "장난스러운 어감이지만, 그녀에게는 동경—"

    ch_nar "—혹은 그 이상의 감정이 담겨 있을지 모르는 호칭."

    ch_nar "장난스럽고, 우스꽝스럽게 들려야 할 그 호칭이,"

    ch_nar "불길할 정도의 고요함을 안고 나지막이 들려온다."

    ch_nar "마치 누군가 목을 죄고 있기라도 한 듯, 그녀는 힘겹게 입을 연다."

    ch_ninon "역시 쇼군에게는…… 못 당하겠네요 입니다."

    ch_nar "무슨 말이야? 왜 그런 말을 하는 거야?"

    ch_nar "의미를 모르겠어."

    ch_ninon "쇼군을 만나면, 차마 발이 떨어질 것 같지 아니하여…… 그래서……"

    ch_ninon "……프랑스, 돌아가야만……"

    ch_nar "그녀는 무언가 말하려는 듯 입술을 달싹대지만, 나의 귀에는 닿지 않는다."

    $ renpy.pause(1, hard = True)

    ch_ninon "……쇼군과의 여정도…… 오늘로 마지막 입니다."

    $ renpy.pause(1, hard = True)

    ch_nar "어떤 표정을 지어야 할지 모르겠다."

    ch_nar "어떻게 반응해야 할지 모르겠다."

    ch_nar "대답하고 싶지 않다."

    ch_nar "이대로 못 들은 척하면 없던 일이 되지 않을까."

    ch_ninon "……그런 표정, 쇼군답지 못합니다. 장차 천하를 호령할 군주라면 고작 이 정도 일로……"

    ch_nar "듣기 싫어."

    ch_ninon "……그렇소 입니다. 고작 이 정도 일일 뿐입니다."

    ch_nar "듣기 싫다고."

    show cg_ninon_happy_01 with dissolve
    hide cg_ninon_happy_02

    ch_ninon "……쇼군."

    ch_nar "그녀의 상냥한 손길이, 고개를 푹 숙인 채 두 귀를 막고 있던 나의 손을 감싼다."

    ch_ninon "쇼군과 함께 했던 나날들은 정말 즐거웠어요 입니다. 니논에게는 평생 잊지 못할 소중한 추억으로 남을 것입니다."

    $ renpy.pause(1, hard = True)

    ch_ninon "하지만 쇼군은…… 쇼군은 그래선 아니되오 입니다."

    ch_ninon "쇼군에게 니논은 불충한 신하들 중 하나에 불과할 뿐. 주군을 떠나는 신하에게 허락될 자비는 없다 입니다."

    ch_nar "……거짓말 하지 마."

    ch_nar "너는……"

    ch_nar "너는 그걸로 된 거야?"

    ch_ninon "……니논은 그걸로 만족하는가…… 입니까?"

    ch_nar "그녀는 숨을 크게 들이쉬고, 별안간 호흡을 멈춘다."

    ch_nar "무언가 터져 나오려는 걸 억지로 막아내는 것처럼 보인다."

    show cg_ninon_happy_03 with dissolve
    hide cg_ninon_happy_01

    ch_ninon "쇼군은……"

    ch_ninon "쇼군은…… 정말로 잔인한 남자에요 입니다."

    ch_ninon "당연히 그럴 리가……"

    ch_ninon "괜찮을 리가 없다는 걸 알고 있으면서……"

    show cg_ninon_happy_05 with dissolve
    hide cg_ninon_happy_03

    ch_nar "그녀는 차마 말을 잇지 못한 채 고개를 떨군다."

    ch_nar "아무 말 없이 그녀를 바라보던 나는,"

    ch_nar "두 팔을 벌리고 그녀를 품에 껴안는다."

    ch_ninon "이렇게 될 것 같아서, 니논도 스스로를 주체하지 못하게 될 것 같아서,"

    ch_ninon "쇼군을…… 만나지 않으려 했는데……"

    $ renpy.pause(1, hard = True)

    ch_ninon "……불경하다는 건 알고 있다 입니다. 그치만……"

    ch_ninon "그치만…… 이건…… 쇼군이 잘못한 거예요 입니다."

    ch_nar "조용히 품에 안겨 있던 그녀가 무언가를 나직이 속삭인다."

    show cg_ninon_happy_04 with dissolve
    hide cg_ninon_happy_05

    ch_ninon "{i}……Je t'aime, à la folie.{/i}"

    $ renpy.pause(1, hard = True)

    show bg_black
    hide cg_ninon_happy_04

    ch_nar "말을 마친 그녀는 잠시 숨을 고른 뒤, 나의 손을 뿌리치고 뛰어간다."

    ch_nar "그녀를 붙잡을 수도,"

    ch_nar "붙잡을 자격도 없는 나는,"

    ch_nar "멀어져 가는 그녀의 모습을 하릴없이 바라보며, 채 식지 않은 그녀의 온기를 애써 기억하려 한다."

    $ renpy.pause(1, hard = True)

    ch_nar "……조용하다."

    ch_nar "“슈바바바밧.”"

    ch_nar "그녀가 전력으로 달려갈 때면 들려오던, 기묘한 음성……"

    ch_nar "영원할 것이라 믿었던 소음의 부재가, 괜시리 콧등을 시큰하게 한다."

    ch_nar "……."

    ch_nar "……안녕, 니논."

    ## 빨려들어가는 효과
    
    ## bgm 서서히 off
    ## 아메스 ####################################
    ## 아메스 테마 bgm 서서히 커지다가 고정
    play music "audio/main/ames.mp3" fadein 3.0
    ## 아메스 cg DIS
    hatena "……와우."

    hatena "엄청난…… 걸 봐버렸네."

    hatena "……대충 예상했겠지만, 방금 당신이 본 건 말이지,"

    hatena "열심히 한 당신에게 주는 상……이었어야 하는데, 원래는."

    hatena "뭐…… 그렇게 기운 빠질 것 없어. 어차피, 금방 잊어버릴 꿈 같은 거니까……"

    hatena "정말로 꿈이 맞냐고? 글쎄, 어떨까나……."

    $ renpy.pause(1, hard = True)

    hatena "……있지, 그런 말 들어본 적 있어?"

    hatena "지나치게 명랑하고 잘 웃는 아이들은……"

    hatena "자신의 아픔을 숨기기 위해 억지로 밝은 척한다는 거."

    hatena "니논은 말이지, 언제나 당신을 진심으로 따르고 있었어."
    
    hatena "하지만…… 당신에게 진심을 보인 적은 단 한 번도 없었어."

    hatena "무슨 차이인지 모르겠다고? 후후, 당신도 아직 한참 멀었네."

    hatena "니논이 마지막으로 했던 말…… 무슨 의미인지 알고 있어?"

    hatena "아니, 알든 모르든 상관없어. 중요한 건……"

    hatena "그 아이가 ‘처음으로’ 당신에게 진심을 말했다는 거야."

    hatena "뭐…… 알아서 잘 할 테지만,"

    hatena "그녀에게 잘해 줘."

    hatena "언제 당신이 그녀를 떠나갈지,"

    hatena "……그녀가 당신을 떠나갈지, 아무도 모르는 법이니까."
    
    hatena "남의 연애사에 참견하는 건 그다지 바람직한 일은 아니지만, 어쩔 수 없어. 이건 여자아이의 본능 같은 거라구, 후후…….♪"

    hatena "도움이 되었길 바랄게. 어떤 의미로든."

    hatena "……어이쿠, 시간을 너무 많이 잡아먹었네."

    hatena "뭐, 오늘은 여기까지 해둘까."

    hatena "그럼 또 봐."

    ## 빨려들어가는 효과

    ## bgm 볼륨 서서히 off
    stop music fadeout 3.0
    ## 랜드솔 마을 #####################

    ## 마을 bgm 서서히 커짐

    show bg_town with fade
    hide bg_black

    show bg_end with fade

    ch_nar "Thank you for playing"

    return

label monicaHappy:

    ch_monica "모니카 해피엔딩"

    show bg_end with fade

    ch_nar "Thank you for playing"

    return

label kukaHappy:

    ch_kuka "쿠우카 해피엔딩"

    show bg_end with fade

    ch_nar "Thank you for playing"

    return

label yukiHappy:

    ch_yuki "유키 해피엔딩"

    show bg_end with fade

    ch_nar "Thank you for playing"

    return

label Success:

    ch_nar "성공적인 토벌"

    show bg_end with fade

    ch_nar "Thank you for playing"

    return

label Badkyaru:

    ch_nar "캬루의 배신"

    show bg_end with fade

    ch_nar "Thank you for playing"

    return

label Kimura:

    play music "audio/main/kimura.mp3"

    ch_nar "키 사 마_!!!!!!!!"

    show bg_end with fade

    ch_nar "Thank you for playing"

    return

label BAD:

    ch_nar " 참피 플뤼겔"

    show bg_end with fade

    ch_nar "Thank you for playing"

    return