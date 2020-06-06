## 초기설정 #############################
init python:
    config.rollback_enabled = True

## 스탠딩 ###############################
init:
    image stand_Monica = "Character/monica/monica.png"
    image stand_Kuka = "Character/kuka/kuka.png"
    image stand_Yuki:
        im.FactorScale("Character/yuki/yuki.png", 0.18)
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

    image bg_forest:
        im.FactorScale("bg/forest.jpg", 0.4)
    
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
## 호감도 ################################
init:
    define love_point = 0
    define point_monica = 0
    define point_ninon = 0
    define point_kuka = 0
    define point_yuki = 0
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
image end1 = "library/end1.jpg"
image ninon_pingping:
    im.FactorScale("library/ninon_pingping.png", 0.5)
define persistent.unlock_1 = False  
## 시작 전 로고 화면 ######################
label splashscreen:
    scene logo_head onlayer middle with fade
    $ renpy.pause(3, hard = True)
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
            ypos 25
            size 40

        text _("니논"):
            xpos (1280 - 240)
            xanchor 0.5
            ypos 25
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
        hatena "어서와,[name]. 그게 당신의 이름이구나."
        hatena "지금부터 당신이 보게 될 것은, 이른바 꿈 같은 거야. 이미 겪어보았거나, 언젠가 일어날지도 모르는, 한여름 밤의 꿈 같은 일. ‘몽상’이라 불러도 좋겠네."

        menu:
            "당신은 누구죠?":
                hatena "내가 누구냐고? 알 필요 없다."
                ##하스스톤 비밀거는 효과음
                hatena "……호기심도 많네. 내 정체 같은 건 중요하지 않아."
                hatena "당신이 알아야 할 건 단지…… 이제부터 여러 명의 ‘소녀’들을 만나게 된다는 것과,"
                hatena "당신이 어떤 선택을 내리느냐에 따라 그녀들의 운명이 조금씩 바뀌게 된다는 것밖에 없어. 그럼 잘해봐. 행운을 빌게, 왕자님♪"
            ##텍스트 사라지면서 볼륨 서서히 off
    else:
        hatena "어떻게 사람 이름이 [name]일수가 있지 ㅋㅋ"
        hatena "진짜 이름을 10자 이내로 알려줘."
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
## 진행 ###
    scene bg_forest onlayer background with fade # 배경화면

    play music "audio/main/nature.mp3"

    hatena "빈틈! 받아라앗...!!"

    show bg_forest onlayer background with hpunch

    monster "커르륵...!"

    show stand_Monica onlayer middle with dissolve

    ch_monica "됐다! 움직임이 봉쇄됐어! 지금이다, 니논! 한 방 먹여!!"
    hide stand_Monica onlayer middle
    show stand_Ninon onlayer middle with dissolve

    ch_ninon "ROGER! 이거나 먹어라, 입니다! 「인법 · 쇙강 줜병 회오뤼」~!!"
    hide stand_Ninon onlayer middle

    monster "쿠아아악!! 크르륵..."

    monster "크워어어어어!!"

    show stand_Monica onlayer middle with dissolve
    ch_monica "칫… 이 정도로는 어림도 없나. 모두들, 뒤로 물러나! 놈이 반격해온다!"
    hide stand_Monica onlayer middle
    show stand_Kuka onlayer middle with dissolve

    ch_kuka "이… 이렇게 커다란 마물이라면… 쿠… 쿠우카, 돌아오지 못할 강을 건너버릴지도…! 크흐흣….츄릅…."
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

    ch_nar "콧코로의 눈망울이 연상되는 와인 색의 피가 손끝에 맺힌다. 아프다."

    ch_nar "콧코로…… 언제 와? 나 배고파. 무서워."

    ch_nar "콧코로는 돈 많이 벌어오겠다며 집을 나간 뒤로 며칠 째 연락이 안 된다."

    ch_nar "페코린느와 배신자는 던전으로 식재료 탐방을 간다길래 따라가고 싶다고 했더니,"

    ch_nar "“아하하, 약해빠진 주제에 또 누구 발목을 잡으려는 건가요? 장난 아니네요! 얌전히 길드하우스나 지키고 있으세요☆”"

    ch_nar "“하아? 벌레 한 마리도 제대로 못 잡는 멍청한 돼지가 어딜 따라오겠다고? 죽여버린다?”"

    ch_nar "라며 나만 남겨두고 가버렸다."

    ch_nar "수영복만 벗으면 아무것도 아닌 것들이……."

    ch_nar "항상 콧코로가 요리를 해줬는데 이젠 밥해줄 사람이 아무도 없다. 이대로면 정말 굶어죽을지도 모른다."

    ch_nar "그래서 직접 요리를 해보려고 식칼을 꺼냈는데 쥐는 법을 몰라서 바로 손가락을 베였다."

    ch_nar "콧코로…… 생전 손에 물 한 번 묻혀본 적 없는 나에게 이런 수모를 겪게 하다니…… 돌아오면 잘못했다고 울며불며 매달릴 때까지 단식투쟁을 할 것이다."

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
    ch_monica "이대로는 안돼!"
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
    ch_monica "……였어야 했는데, 마지막으로 마물을 토벌했던 게 언제인지 이제는 기억도 안 날 지경이다. 채집 의뢰만 산더미처럼 쌓여있어! 이게 뭐냐! 우리는 전투 길드란 말이다~!!"

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

    ch_monica "모든 일에는 타당한 이유가 존재하기 마련. 그렇다면 우리들에게 부족한 건 대체 뭘까? 아유미! 대답해봐라!"
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
    show stand_Yuki with dissolve
    ch_yuki "잠깐, 설마……."
    hide stand_Yuki
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

    ch_monica "……무작정 부딪혀보면 어떻게든 될 거라고 생각했건만……. 귀공은 내 방식이 잘못됐다고 생각하나?"

    menu:
        "결과가 말해주고 있잖아":
            ## 볼빵빵
            ch_monica "……마, 맞는 말이다만……, 그렇게 말하는 귀공에게는 더 좋은 해결책이 있는 거겠지?"
            ch_monica "자세한 이야기는 우리 길드원들 앞에서 하는 게 어떤가? 지금 바로 출발하도록 하지."
        "틀린 방법은 아니었다고 생각해":
            ## 시무룩한 표정
            ch_monica "빈말이라도 고맙군…… 하지만 우리는 실제로 마물에게 이렇다 할 타격도 주지 못하고 당해버렸어."
            ch_monica "이대로면 부하들이 입는 피해만 늘어갈 터……. 뭔가 다른 방법이 필요해." 
            ch_monica "귀공, 도움을 줄 수 있겠나? 일단 우리 길드하우스로 자리를 옮기도록 하지."
    hide stand_Monica with fade
    window hide
    ## cg 페이드 아웃
    hide bg_guildhouse with fade
    ## 잠깐 텀
## 랜드솔 마을 cg 페이드
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
## 길드 하우스 cg 페이드
    scene bg_guildhouse with fade
    show stand_Ninon

    ch_ninon "쇼군! 이것은 마음을 안정시키는 동국의 3대 명차, 우지차라고 하는 것입니다!"

    ## 
    extend " 어서 들이켜보세요 입니다!"

    hide stand_Ninon

    player "우지챠……."

    show stand_Kuka with dissolve ##기본 표정

    ch_kuka "그, 그러니까 도S씨는…… 정확히 무슨 일 때문에 오신 거죠?"
    ## 쿠우카 망상하는 표정
    ch_kuka "설마…… 어둡고 구석진 골목에 마구잡이로 쿠우카를 밀어붙였던 그날…… 쿠우카가 아직까지도 그날의 쾌락을 잊지 못한 채 추잡스러운 행위를 계속하고 있는지 직접 확인하려고……?!"

    ch_kuka " 쿠, 쿠우카를 나락으로 빠뜨리기 위해 어디까지 계획을 세워놓은 건가요?! 이…… 인륜배반자! 관음증 변태! 쿠, 쿠훗, 크흐흐……."

    hide stand_Kuka
    show stand_Monica with dissolve

    ch_monica "음! [name]를 이 자리에 호출한 건 다름이 아니라, 바이스플뤼겔의 향후 방향성과 마물 소탕 건에 대해 조언을 구하기 위해서다. 모두 한자리에 모였으니 드디어 이야기를 시작할 수 있겠군."

    ## 모니카 어둡게

    ch_ayumi "역시 선배, 계획이 다 있으신 거군요……!"

    player "그런 거 없는데……."

    ch_ayumi "무계획이 계획인 거네요……! 역시!"
    hide stand_Monica

    show stand_Ninon_down with dissolve ## 시무룩한 표정

    ch_ninon "쇼군! 니논은 최선을 다했다 입니다! 하지만 마물이 너무너무 POWERFUL 했습니다……."

    ch_ninon "「인법 · 쇄우 병쉰 회오뤼감좌」를 정면으로 받아내고 살아남은 자는 그녀석이 처음이었다 입니다!"

    ## 니논 어둡게

    show stand_Monica at veryright with dissolve ## 시무룩한 표정

    ch_monica "‘그거, 뭔가 다른 이름이었던 것 같은데……’"

    hide stand_Ninon_down

    show stand_Monica at movetocenter

    ## 모니카 자신만만한 표정

    ch_monica "……걱정할 것 없다, 니논! [name]의 도움이 있다면 그보다 더 강한 놈들도 충분히 상대할 수 있게 될 거다."

    ch_monica "그러면, 우리의 문제가 어떤 것인지 말해줄 수 있겠나?"

    hide stand_Monica
    show stand_Yuki with dissolve ##자신만만한 표정

    ch_yuki "이렇게나 귀여운 내가 있는데, 무슨 문제가 있다는 거야~? 복잡한 생각 하지 말고 예쁜 내 얼굴이나 감상하라구♪"

    hide stand_Yuki
    show stand_Monica with dissolve ## 화난 표정

    ch_monica "그렇게 건성으로 넘길 문제가 아니다! 귀공, 다시 한 번 정식으로 요청하도록 하지."

    ## 모니카 자신만만한 표정

    ch_monica "‘바이스플뤼겔 랜드솔지부’가 나아갈 길을 제시해주게! 귀공은 우리의 문제가 무엇이라고 생각하나?"

## 캐릭터 선택 분기 #########################
    menu:
        "어설픈 실력과 저돌적인 행동으로 쉽게 위험에 빠지는 것":
            $point_ninon = point_ninon + 1

        "동료를 신뢰하지 않고 독단적으로 행동하는 것":
            $point_monica = point_monica + 1

        "순간의 욕망을 억제하지 못하고 충동적으로 행동하는 것":
            $point_kuka = point_kuka + 1

        "자기 자신만을 중시하며 동료를 배려하지 않는 것":
            $point_yuki = point_yuki + 1

    show stand_Monica with dissolve ## 기본 표정

    ch_monica "음, 과연……. 귀공을 여기까지 데려온 보람이 있군. 훌륭한 통찰력이다."

    ch_monica "그렇다면 귀공이 지적한 대로, 우리의 문제점을 보완하는 것은 곧 바이스플뤼겔의 전력을 증강하는 길이라 봐도 무방할 터. 이제부터 그 방법을……"

    ## 잠깐 텀
    ## 니논 자신만만한 표정
    show stand_Ninon at veryleft:
        linear 0.5 xalign 0.5 


    ch_ninon "특훈만이 살 길이다!!!!!!!! 입니다!!!"

    show stand_Monica at movetoright ##볼빵빵, 얼굴이 절반정도만 보이도록
    
    ch_ninon "닌자가 강해지는 길은 오직 수련, 또 수련하는 것 뿐!! 천하통일을 위해서라면 그 어떤 지옥훈련이라도 견뎌낼 각오가 되어있소 입니다!!"

    show stand_Monica at movetocenter
    show stand_Ninon at movetoleft

    ## 니논 기본표정, 어둡게/모니카 밝게
    ch_monica "흠, 흠!"

    ## 모니카 진지한 표정

    ch_monica "……확실히 틀린 말은 아니다. 가혹한 훈련은 고통스럽지만 그만큼 효과적일 수 있지."

    ## 모니카 시무룩한 표정

    ch_monica "하지만 니논, 훈련의 강도가 높은 것만이 능사는 아니야. 그건 우리가 누구보다도 뼈저리게 경험하지 않았나."

    ## 모니카 어둡게/니논 시무룩한 표정, 밝게
    hide stand_Ninon
    show stand_Ninon_down at veryleft
    ch_ninon "과연…… 입니다. 그럼 니논은 무엇을 할 수 있다 입니까? 할복 입니까?"

    ## 니논 어둡게/ 모니카 밝게, 기본 표정
    ch_monica "그건……"

    ## 모니카 자신만만한 표정

    ch_monica "우리의 새로운 해결사가 답을 알려줄 거다!"

    ## 둘 다 어둡게

    ch_nar "갑자기 나한테 떠넘긴다고? 미쳤나?"
    ## 모니카 cg어둡게/니논 밝게, 니논 놀란 표정
    hide stand_Ninon_down
    show stand_Ninon_panic at veryleft

    ch_ninon "우오옷~ 믿고 있었다고 쥐엔장~~!! 입니다!"

    player "아니…… 갑자기 그렇게 말해봤자……"

    hide stand_Monica
    hide stand_Ninon_panic
    show stand_Ninon_wink at veryleft:
        linear 0.5 xalign 0.5
    ch_ninon "DAIJOBU 입니다~! 왜냐하면 쇼군은~"
    hide stand_Ninon_wink
    show stand_Ninon_daiji onlayer middle
    $ camera_move(0, 0, 400, 0, 6)

    scene bg_surf onlayer background with dissolve
    ## 배경음 일본풍 bgm
    ch_ninon "……쇼군은…… 언제나 정도만을 걸어온 남자."

    ch_ninon "제아무뤼 겉으로는 언행이 아둔하고 이취에 맞지 않는 듯하여도, 쇼군이 인도하는 길의 끝에는 항시 광명이 우뤼를 비추고 있었소."

    ch_ninon "혹자는 쇼군의 우쥑한 성품을 비방할지도 모르오. 허나 그것은 툇마루 아래의 장사를 알아보지 못하는 붬인의 좁은 식견에 불과할 뿐."

    ch_ninon "일찍이 길이 존재했기에 걷는 것이 아니요, 쇼군의 족줙이 곧 길이라. 참된 쥐도자란 바로 그런 것이오."

    ch_ninon "설령 승리를 목줜에 두고 적에게 소금을 보눼어 되레 위난에 처하게 될지라도, 니논은 쇼군의 뜻을 따르겠소. 그것이 종국에는 우리를 줭토로 이끌리라 믿어 의심치 아니하기에……."

    ##빠르게 원래 크기로 복구
    $ camera_move(0, 0, 0, 0, 0.2)


    hide bg_surf onlayer background
    ## 길드하우스로 다시 변경
    scene bg_guildhouse
    ## 마을 bgm으로 다시 변경
    ## 니논 윙크하는 표정
    hide stand_Ninon_daiji onlayer middle
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
    show stand_Yuki with dissolve

    ch_yuki "저기 저기 [name]."

    player "……응?"

    ch_yuki "좀 전에 니논이 ‘특훈’이니 뭐니 했던 거 말야, 그런 바보 같은 걸 진짜로 하자고 할 건 아니지?"

    ## 니논 억울한 표정 왼쪽/ 유키 cg 어두워짐
    show stand_Yuki at movetoright
    show stand_Ninon_innocence at left

    ch_ninon "이익……! 먼저 바보라 하는 사람이 바보 입니다!"

    ## 니논 어둡게/ 유키 밝게

    ch_yuki "하? 농담이지? 그런 거 안 해도 내 미모는 나날이 예뻐지거든? 찝찝하게 땀 흘리는 일 같은 건 절대 사절이니까~ 참고하라구. 알았지?"

    ch_nar "음…… 그냥 다 패고 감옥 가고 싶다."
    ch_nar "그런데 잠깐, 방금……."

    hide stand_Ninon_innocence
    hide stand_Yuki

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

    ch_yuki "음~ 예쁜 얼굴은 타고나는 거라 해도, 피부는 꾸준히 잘 관리해줘야 한다구. 이참에 모니카 씨도 신경 좀 써보는 건 어때? 충분히 귀여운 얼굴인데, 아깝잖아~ 뭐, 나만큼은 아니지만."

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

    ch_yuki "온!"

    #show stand_Yuki at left ## 유키 어둡게
    #show stand_Ninon_surprise at right ##니논 밝게

    ch_ninon "천!"

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
    show stand_Ninon with dissolve

    ch_ninon "지난번 마물 토벌 이후, 아직까지도 오에도 여러분의 열화와 같은 INVITATION이 끊이질 않고 있는데……"

    hide stand_Ninon


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

label cg_yukifirst:

    centered "전라 상태로 수건을 몸에 두르고 고개를 살짝 돌려 주인공을 힐끔 쳐다보는 유키의 뒷모습"

    return

label cg_yukisecond:

    centered "탕에 몸을 반쯤 담근 채 요염한 자세로 주인공을 바라보는 유키"

    return
                
## 엔딩 ##################
label ninonHappy:

    show end1

    ch_ninon "니논 해피엔딩"

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