 ## 초기설정 #############################
init python:
    config.rollback_enabled = False
init:
    define _dismiss_pause = False
## 스탠딩 ###############################
init:
    ## 모니카
    image stand_Monica:
        im.FactorScale("Character/monica/monica.png", 0.35)
        ypos 1050
    image stand_Monica_crying:
        im.FactorScale("Character/monica/monica_crying.png", 0.35)
        ypos 1050
    image stand_Monica_ddung:
        im.FactorScale("Character/monica/monica_ddung.png", 0.35)
        ypos 1050
    image stand_Monica_dere:
        im.FactorScale("Character/monica/monica_dere.png", 0.35)
        ypos 1050
    image stand_Monica_down:
        im.FactorScale("Character/monica/monica_down.png", 0.35)
        ypos 1050
    image stand_Monica_munen:
        im.FactorScale("Character/monica/monica_munen.png", 0.35)
        ypos 1050
    image stand_Monica_surprised:
        im.FactorScale("Character/monica/monica_surprised.png", 0.35)
        ypos 1050
    image stand_Monica_yukata:
        im.FactorScale("Character/monica/monica_yukata.png", 0.35)
        ypos 1050
    image stand_Monica_yukata_crying:
        im.FactorScale("Character/monica/monica_yukata_crying.png", 0.35)
        ypos 1050
    image stand_Monica_yukata_ddung:
        im.FactorScale("Character/monica/monica_yukata_ddung.png", 0.35)
        ypos 1050
    image stand_Monica_yukata_dere:
        im.FactorScale("Character/monica/monica_yukata_dere.png", 0.35)
        ypos 1050
    image stand_Monica_yukata_down:
        im.FactorScale("Character/monica/monica_yukata_down.png", 0.35)
        ypos 1050
    image stand_Monica_yukata_munen:
        im.FactorScale("Character/monica/monica_yukata_munen.png", 0.35)
        ypos 1050
    image stand_Monica_yukata_surprised:
        im.FactorScale("Character/monica/monica_yukata_surprised.png", 0.35)
        ypos 1050
    ## 쿠우카
    image stand_Kuka:
        im.FactorScale("Character/kuka/kuka.png", 0.30)
        ypos 1000
    image stand_Kuka_down:
        im.FactorScale("Character/kuka/kuka_down.png", 0.30)
        ypos 1000
    image stand_Kuka_hiku:
        im.FactorScale("Character/kuka/kuka_hiku.png", 0.30)
        ypos 1000
    image stand_Kuka_mousou:
        im.FactorScale("Character/kuka/kuka_mousou.png", 0.30)
        ypos 1000
    image stand_Kuka_shamed:
        im.FactorScale("Character/kuka/kuka_shamed.png", 0.30)
        ypos 1000
    image stand_Kuka_surprised:
        im.FactorScale("Character/kuka/kuka_surprised.png", 0.30)
        ypos 1000
    image stand_Kuka_yukata:
        im.FactorScale("Character/kuka/kuka_yukata.png", 0.30)
        ypos 1000
    image stand_Kuka_yukata_down:
        im.FactorScale("Character/kuka/kuka_yukata_down.png", 0.30)
        ypos 1000
    image stand_Kuka_yukata_hiku:
        im.FactorScale("Character/kuka/kuka_yukata_hiku.png", 0.30)
        ypos 1000
    image stand_Kuka_yukata_mousou:
        im.FactorScale("Character/kuka/kuka_yukata_mousou.png", 0.30)
        ypos 1000
    image stand_Kuka_yukata_shamed:
        im.FactorScale("Character/kuka/kuka_yukata_shamed.png", 0.30)
        ypos 1000
    image stand_Kuka_yukata_surprised:
        im.FactorScale("Character/kuka/kuka_yukata_surprised.png", 0.30)
        ypos 1000
    ## 유키
    image stand_Yuki:
        im.FactorScale("Character/yuki/yuki.png", 0.30)
        ypos 1000
    image stand_Yuki_angry:
        im.FactorScale("Character/yuki/yuki_angry.png", 0.30)
        ypos 1000
    image stand_Yuki_ddung:
        im.FactorScale("Character/yuki/yuki_ddung.png", 0.30)
        ypos 1000
    image stand_Yuki_proud:
        im.FactorScale("Character/yuki/yuki_proud.png", 0.30)
        ypos 1000
    image stand_Yuki_shamed:
        im.FactorScale("Character/yuki/yuki_shamed.png", 0.30)
        ypos 1000
    image stand_Yuki_surp:
        im.FactorScale("Character/yuki/yuki_surp.png", 0.30)
        ypos 1000
    image stand_Yuki_yukata:
        im.FactorScale("Character/yuki/yuki_yukata.png", 0.30)
        ypos 1000
    image stand_Yuki_yukata_angry:
        im.FactorScale("Character/yuki/yuki_yukata_angry.png", 0.30)
        ypos 1000
    image stand_Yuki_yukata_ddung:
        im.FactorScale("Character/yuki/yuki_yukata_ddung.png", 0.30)
        ypos 1000
    image stand_Yuki_yukata_proud:
        im.FactorScale("Character/yuki/yuki_yukata_proud.png", 0.30)
        ypos 1000
    image stand_Yuki_yukata_shamed:
        im.FactorScale("Character/yuki/yuki_yukata_shamed.png", 0.30)
        ypos 1000
    image stand_Yuki_yukata_surp:
        im.FactorScale("Character/yuki/yuki_yukata_surp.png", 0.30)
        ypos 1000
    
    ## 니논
    image stand_Ninon:
        im.FactorScale("Character/ninon/ninon.png", 0.27)
        ypos 990
    image stand_Ninon_down:
        im.FactorScale("Character/ninon/ninon_down.png", 0.27)
        ypos 990
    image stand_Ninon_embarassed:
        im.FactorScale("Character/ninon/ninon_embarrassed.png", 0.27)
        ypos 990
    image stand_Ninon_innocence:
        im.FactorScale("Character/ninon/ninon_innocence.png", 0.27)
        ypos 990
    image stand_Ninon_surprise:
        im.FactorScale("Character/ninon/ninon_surprise.png", 0.27)
        ypos 990
    image stand_Ninon_wink:
        im.FactorScale("Character/ninon/ninon_wink.png", 0.27)
        ypos 990
    image stand_Ninon_angry:
        im.FactorScale("Character/ninon/ninon_angry.png", 0.27)
        ypos 990
    image stand_Ninon_daiji:
        im.FactorScale("Character/ninon/ninon_daiji.png", 0.27)
        ypos 990
    image stand_Ninon_panic:
        im.FactorScale("Character/ninon/ninon_panic.png", 0.27)
        ypos 990
    image stand_Ninon_yukata:
        im.FactorScale("Character/ninon/ninon_yukata.png", 0.27)
        ypos 990
    image stand_Ninon_yukata_angry:
        im.FactorScale("Character/ninon/ninon_yukata_angry.png", 0.27)
        ypos 990
    image stand_Ninon_yukata_daiji:
        im.FactorScale("Character/ninon/ninon_yukata_daiji.png", 0.27)
        ypos 990
    image stand_Ninon_yukata_down:
        im.FactorScale("Character/ninon/ninon_yukata_down.png", 0.27)
        ypos 990
    image stand_Ninon_yukata_emb:
        im.FactorScale("Character/ninon/ninon_yukata_emb.png", 0.27)
        ypos 990
    image stand_Ninon_yukata_innocent:
        im.FactorScale("Character/ninon/ninon_yukata_innocent.png", 0.27)
        ypos 990
    image stand_Ninon_yukata_panic:
        im.FactorScale("Character/ninon/ninon_yukata_panic.png", 0.27)
        ypos 990
    image stand_Ninon_yukata_surp:
        im.FactorScale("Character/ninon/ninon_yukata_surp.png", 0.27)
        ypos 990
    image stand_Ninon_yukata_wink:
        im.FactorScale("Character/ninon/ninon_yukata_wink.png", 0.27)
        ypos 990
    ## 구라노스케
    image stand_gura:
        im.FactorScale("Character/gura/gura.png", 1.0)
    image cg_gura_baby:
        im.FactorScale("library/cg_gura_baby.png", 1.0)
    image cg_gura_child:
        im.FactorScale("library/cg_gura_child.png", 1.0)
    image movie = Movie(size=(1280,720))
    ## 마물
    image stand_monster:
        im.FactorScale("Character/monster/monster.png", 0.2)
    ## 프붕
    image cg_babybung:
        im.FactorScale("library/babybung.png", 1.0)
        xalign 0.5 yalign 0.3
    ## 아메스
    image cg_ames:
        im.FactorScale("library/ames.png", 0.67) 
## 트랜스폼
    transform movetoright:
        ease 0.5 xalign 0.8

    transform movetoveryright:
        ease 0.5 xalign 1.1

    transform movetocenter:
        linear 0.5 xalign 0.5
        
    transform movetoleft:
        ease 0.5 xalign 0.2

        
    transform rotated:
        linear .5 rotate 360 yalign 0.3

    transform fast_rotating:
        linear 0.3 rotate 360 yalign 0.5

    transform fast_rotating_2:
        linear 0.3 rotate 720 yalign 0.5
    transform xycenter:
        xalign 0.5 yalign 0.5
## 배경 cg
    image bg_whatsyourname:
        im.FactorScale("bg/whatsYourName.png", 1.0)

    image bg_field:
        im.FactorScale("bg/field.png", 0.67)

    image bg_town:
        im.FactorScale("bg/bg_town.png", 1.0)
    
    image bg_room:
        im.FactorScale("bg/room.jpg", 2.55)

    image bg_end:
        im.FactorScale("bg/bg_end.png", 1.0)  

    image bg_badend:
        im.FactorScale("bg/bg_badend.png", 1.0)

    image highlight:
        im.FactorScale("library/highlight_line.png", 1.1)
    
    image bg_guildhouse:
        im.FactorScale("bg/bg_guildhouse.png", 1.0)
    
    image bg_guildhouse_rev:
        im.FactorScale("bg/bg_guildhouse_reversed.png", 1.0)

    image bg_guildhouse_s:
        im.FactorScale("bg/guildhouse_short.png", 0.67)
    
    image bg_black:
        im.FactorScale("bg/black.png", 2.0)

    image bg_surf:
        im.FactorScale("bg/surf.jpg", 1.75)

    image bg_universe:
        im.FactorScale("bg/bg_universe.png", 1.2)

    image bg_onsen:
        im.FactorScale("bg/bg_onsen.png", 1.0)

    image bg_onsen_dark:
        im.FactorScale("bg/bg_onsen_dark.png", 1.0)

    image bg_routen:
        im.FactorScale("bg/bg_routen.png", 1.0)

    image bg_onsen_heya_01:
        im.FactorScale("bg/bg_onsen_heya_01.png", 0.67)

    image bg_onsen_heya_02:
        im.FactorScale("bg/bg_onsen_heya_02.png", 1.0)

    image bg_onsen_heya_03:
        im.FactorScale("bg/bg_onsen_heya_03.png", 1.0)
    
    image bg_daiyokujyo:
        im.FactorScale("bg/daiyoku.png", 1.0)
    
    image bg_tadami_day: 
        im.FactorScale("bg/tadami_day.png", 0.67)

    image bg_tadami_night:
        im.FactorScale("bg/tadami_night.png", 0.67) 

    image bg_indoor_onsen:
        im.FactorScale("bg/indoor_onsen.png", 1.0)

    image bg_indoor_sauna_day:
        im.FactorScale("bg/indoor_sauna_day.png", 1.0)

    image bg_indoor_sauna_night:
        im.FactorScale("bg/indoor_sauna_night.png", 1.0)
    
    image bg_outside_onsen:
        im.FactorScale("bg/outside_onsen.png", 1.0)
    
    image bg_outside_onsen_2:
        im.FactorScale("bg/outside_onsen_2.png", 1.0)

    image bg_onsen_yado:
        im.FactorScale("bg/onsen_yado.png", 1.0)
    
    image bg_naibu:
        im.FactorScale("bg/onsen_inside.png", 1.0)

    image bg_entrance:
        im.FactorScale("bg/bg_entrance.png", 1.0)

    image bg_entrance_02:
        im.FactorScale("bg/bg_entrance_02.png", 1.0)

    image bg_tyugaku:
        im.FactorScale("bg/bg_tyugaku.png", 0.67)

    image bg_tyugaku_running:
        im.FactorScale("bg/bg_tyugaku_running.png", 1.3)

    image bg_tyugaku_stop:
        im.FactorScale("bg/bg_tyugaku_stop.png", 1.3)

    image logo_head = "logo/logo.png"

    image afewmoment:
        im.FactorScale("library/afewmoment.png", 1.0)

    image sixmonths:
        im.FactorScale("library/sixmonths.png", 1.0)
## 오브젝트 #############################
init:
    image ob_ujitya:
        im.FactorScale("object/ob_ujitya.png", 0.5)
        xpos 650 yalign 0.3
    image ob_wagasi:
        im.FactorScale("object/ob_wagasi.png", 0.5)
    image ob_unagi:
        im.FactorScale("object/tabekakeunagi.png", 0.5)
    image ob_hankachi:
        im.FactorScale("object/hankachi.png", 0.5)
    image ob_tegami:
        im.FactorScale("object/tegami.png", 0.5)
    image ob_key:
        im.FactorScale("object/gura_key.png", 0.5)
    image ob_kiroku:
        im.FactorScale("object/darekanokiroku.png", 0.5)
        xpos 650 yalign 0.3
    image ob_akudaikan:
        im.FactorScale("object/akudaikan.png", 0.5)
        xpos 650 yalign 0.3   

    ## 1컷 만화 ####################################
    image ob_moninon:
        im.FactorScale("object/moninon.png", 0.7)
    image ob_kokkoro:
        im.FactorScale("object/koro.png", 0.7)
    
    image snow = SnowBlossom(im.FactorScale("object/flower_1.png", 0.5), count=50, border=400, xspeed =(30, 60), yspeed=(30, 100), horizontal=True)
    
    ## npc 스탠딩 ###################################
    image npc_1:
        im.FactorScale("object/npc_1.png", 0.8) ## 여자직원
    image npc_2:
        im.FactorScale("object/npc_2.png", 0.8) ## 양아치
    image npc_3:
        im.FactorScale("object/npc_3.png", 0.8) ## 리마
    image npc_4:
        im.FactorScale("object/npc_4.png", 0.8) ## 머리 잘린 양아치

    ## 야스 침팬지 ##################################
    image ob_yas1:
        im.FactorScale("object/yas1.png", 1.0)
        xpos 1000 yalign 0.58
    image ob_yas2:
        im.FactorScale("object/yas2.png", 0.3)
        xalign 0.0 yalign 0.5
    image ob_yas3:
        im.FactorScale("object/yas3.png", 0.3)
        xpos 1100 yalign 0.4

    image ob_yas2_trans:
        im.FactorScale("object/yas2_trans.png", 0.3)
        xalign 0.0 yalign 0.5
    image ob_yas3_trans:
        im.FactorScale("object/yas3_trans.png", 0.3)
        xpos 1100 yalign 0.4
    
    ## 유키 회상 ####################################
    image kaisou_guildhouse = "object/kaisou_g.png"
    image kaisou_field:
        im.FactorScale("object/kaisou_f.png", 0.67) 
    image kaisou_town = "object/kaisou_t.png"

## 이펙트 ###############################
    image fire_big:
        im.FactorScale("effect/fire_big/0.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/1.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/2.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/3.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/4.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/5.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/6.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/7.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/8.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/9.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/10.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/11.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/12.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/13.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/14.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/15.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/16.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/17.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/18.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/19.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/20.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/21.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/22.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/23.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/24.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/25.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/26.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/27.png", 0.80)
        pause 0.05
        im.FactorScale("effect/fire_big/28.png", 0.80)
        pause 0.05
    
    image fire_small:
        im.FactorScale("effect/fire_small/0.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/1.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/2.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/3.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/4.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/5.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/6.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/7.png", 0.55)
        pause 0.05
        repeat
    image fire_small_2:
        im.FactorScale("effect/fire_small/0.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/1.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/2.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/3.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/4.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/5.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/6.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/7.png", 0.55)
        pause 0.05
        repeat
    image fire_small_3:
        im.FactorScale("effect/fire_small/0.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/1.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/2.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/3.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/4.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/5.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/6.png", 0.55)
        pause 0.05
        im.FactorScale("effect/fire_small/7.png", 0.55)
        pause 0.05
        repeat
    image knife_issen:
        im.FactorScale("effect/knife/0.png", 0.67)
        pause 0.05
        im.FactorScale("effect/knife/1.png", 0.67)
        pause 0.05
        im.FactorScale("effect/knife/2.png", 0.67)
        pause 0.05
        im.FactorScale("effect/knife/3.png", 0.67)
        pause 0.05
        im.FactorScale("effect/knife/4.png", 0.67)
        pause 0.05
        im.FactorScale("effect/knife/5.png", 0.67)
        pause 0.05
        im.FactorScale("effect/knife/6.png", 0.67)
        pause 0.05
        im.FactorScale("effect/knife/7.png", 0.67)
        pause 0.05
        im.FactorScale("effect/knife/8.png", 0.67)
        pause 0.05
        im.FactorScale("effect/knife/9.png", 0.67)
        pause 0.05
        im.FactorScale("effect/knife/10.png", 0.67)
        pause 0.05
        im.FactorScale("effect/knife/11.png", 0.67)
        pause 0.05
        im.FactorScale("effect/knife/12.png", 0.67)
        pause 0.05
        im.FactorScale("effect/knife/13.png", 0.67)
        pause 0.05
        im.FactorScale("effect/knife/14.png", 0.67)
        pause 0.05
        im.FactorScale("effect/knife/15.png", 0.67)
        pause 0.05
    
    image pohyo:
        im.FactorScale("effect/pohyo/1.png", 1.5)
        pause 0.07
        im.FactorScale("effect/pohyo/2.png", 1.5)
        pause 0.07
        im.FactorScale("effect/pohyo/3.png", 1.5)
        pause 0.07
        im.FactorScale("effect/pohyo/4.png", 1.5)
        pause 0.07
        im.FactorScale("effect/fire_big/28.png", 1.0)
        pause 0.01
        repeat 5
    
    image smallpohyo:
        im.FactorScale("effect/pohyo/1.png", 1.2)
        pause 0.07
        im.FactorScale("effect/pohyo/2.png", 1.2)
        pause 0.07
        im.FactorScale("effect/pohyo/3.png", 1.2)
        pause 0.07
        im.FactorScale("effect/pohyo/4.png", 1.2)
        pause 0.07
        im.FactorScale("effect/fire_big/28.png", 1.0)
        pause 0.01
        repeat 5
    
    image hit:
        im.FactorScale("effect/hit/1.png", 3.0)
        pause 0.05
        im.FactorScale("effect/hit/2.png", 3.0)
        pause 0.05
        im.FactorScale("effect/hit/3.png", 3.0)
        pause 0.05
        im.FactorScale("effect/hit/4.png", 3.0)
        pause 0.05
        im.FactorScale("effect/fire_big/28.png", 1.0)
        pause 0.01
    
    image ames_swift:
        im.FactorScale("effect/ames_close/1.png", 0.67)
        pause 0.3
        im.FactorScale("effect/ames_close/2.png", 0.67)
        pause 0.07
        im.FactorScale("effect/ames_close/3.png", 0.67)
        pause 0.07
        im.FactorScale("effect/ames_close/4.png", 0.67)
        pause 0.07
        im.FactorScale("effect/ames_close/5.png", 0.67)
        pause 0.07
        im.FactorScale("effect/ames_close/6.png", 0.67)
        pause 0.07
        im.FactorScale("effect/ames_close/7.png", 0.67)
        pause 0.07
        im.FactorScale("effect/ames_close/8.png", 0.67)
        pause 0.07
    
    image ames_reverse:
        im.FactorScale("effect/ames_open/1.png", 1.0)
        pause 2.0
        im.FactorScale("effect/ames_open/2.png", 0.67)
        pause 0.05
        im.FactorScale("effect/ames_open/3.png", 0.67)
        pause 0.05
        im.FactorScale("effect/ames_open/4.png", 0.67)
        pause 0.05
        im.FactorScale("effect/ames_open/5.png", 0.67)
        pause 0.05
        im.FactorScale("effect/ames_open/6.png", 0.67)
        pause 0.05
        im.FactorScale("effect/ames_open/7.png", 0.67)
        pause 0.07
        im.FactorScale("effect/ames_open/9.png", 0.67)
        pause 0.10
        im.FactorScale("effect/ames_open/10.png", 0.67)
        pause 0.06
        im.FactorScale("effect/ames_open/11.png", 0.67)
        pause 0.06
    image town_swift:
        im.FactorScale("effect/town/8.png", 1.0)
        pause 0.03
        im.FactorScale("effect/town/7.png", 1.0)
        pause 0.03
        im.FactorScale("effect/town/6.png", 1.0)
        pause 0.03
        im.FactorScale("effect/town/5.png", 1.0)
        pause 0.03
        im.FactorScale("effect/town/4.png", 1.0)
        pause 0.03
        im.FactorScale("effect/town/3.png", 1.0)
        pause 0.03
        im.FactorScale("effect/town/2.png", 1.0)
        pause 0.03
        im.FactorScale("effect/town/1.png", 1.0)
        pause 0.03
    image raiden_pohyo:
        im.FactorScale("cg/common/raiden1.png", 0.32)
        pause 0.05
        im.FactorScale("cg/common/raiden1.png", 0.32)
        pause 2.0

## BGM & Sound ##################################
    ## Main ##

        ## ## ## ## ## ## ## ## ## ## ## ##
        ## audio/main/ames.mp3
        ## audio/main/2sentou.mp3
        ## audio/main/3town.mp3
        ## audio/main/4japan.mp3
        ## audio/main/5orientalcommon.mp3
        ## audio/main/6orientalcommon.mp3
        ## audio/main/emer.mp3
        ## audio/main/8sad.mp3
        ## audio/main/9bbong.mp3
        ## audio/main/10end.mp3
        ## audio/main/11fun.mp3

    ## Sound ##

        ## ## ## ## ## ## ## ## ## ## ## ##
        ## 문 두드리는 소리 audio/sound/knocking.wav
        ## 문 열리는 소리 audio/sound/opendoor.wav
        ## 충격적인 효과음 audio/sound/surp.mp3
        ## 1박2일 효과음 audio/sound/1bak2il.mp3
        ## 꼬르륵 audio/sound/harapeko.mp3
        ## 꾹꾹 누르는 효과음 audio/sound/gguk.mp3 ##
        ## 숨소리 audio/sound/breathe.mp3
        ## 털썩 audio/sound/down.mp3 ##
        ## 발자국 소리 audio/sound/walking.mp3
        ## 원숭이 울음소리 audio/sound/monkey.mp3
        ## 원숭이 울음소리 2 audio/sound/monkey2.mp3
        ## 괴물 울부짖는 소리 audio/sound/growl.mp3
        ## 괴물 으르렁거리는 소리 audio/sound/exo.mp3
        ## 멀리 날아가는 소리 audio/sound/fly.mp3
        ## 불길이 치솟는 소리 audio/sound/fire.mp3
        ## 소름 돋는 소리 audio/sound/torihada.mp3
        ## 총소리 audio/sound/gunshot.mp3
        ## 키무라 웃음소리 audio/sound/kimura.mp3
        ## 칼 부딪히는 소리 audio/sound/knife1.wav
        ## 둔탁한 피격음 audio/sound/hit.wav
        ## 칼을 검집에서 빼는 소리 audio/sound/baldo.mp3
        ## 칼로 베어가르는 소리 audio/sound/knife2.wav
        ## 뛰어가는 소리 audio/sound/running.mp3
        ## 과자 먹는 소리 audio/sound/snack.wav
        ## A FEW MOMENTS LATER audio/sound/AFEWMOMENTSLATER.mp3
        ## SIX MONTHS LATER audio/sound/SixMonthsLater.mp3
        ## 침 뱉는 소리 audio/sound/spit.mp3
        ## 리마 우는 소리 audio/sound/rima.wav
        ## 책장 넘기는 소리 audio/sound/book.wav
        ## 삐걱거리는 소리 audio/sound/bbiguk.wav
        ## 카메라 소리 audio/sound/camera.mp3
        ## 심장 소리 audio/sound/heart.wav
        ## 문 닫히는 소리 audio/sound/doorclose.mp3
        ## 아메스 여는 소리 audio/sound/amesopen.mp3
        ## 아메스 닫는 소리 audio/sound/amesclose.mp3

    ## Voice ##

        ## ## ## ## ## ## ## ## ## ## ## ##
        ## audio/titlesound/ayumi.mp3
        ## audio/titlesound/kuka.mp3
        ## audio/titlesound/monica.mp3
        ## audio/titlesound/ninon.mp3
        ## audio/titlesound/yuki.mp3


## 캐릭터 ###############################
init:
    image CTC = Image("/menu/ctc_icon.png", xpos = 1125, ypos = 670)
    image CTC_TRANS = Image("/menu/ctc_trans.png", xpos = 1125, ypos = 670)
    image ctc_icon:
        "CTC"
        pause 0.7
        "CTC_TRANS"
        pause 0.7
        repeat
    define ch_ninon = Character('니논', color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed",  image = 'ninon')

    define ch_monica = Character('모니카', image = 'monica', color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed")

    define ch_kuka = Character('쿠우카', image = 'kuka', color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed")

    define ch_yuki = Character('유키', image = 'yuki', color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed")

    define ch_ayumi = Character('아유미', color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed")

    ## 사이드 이미지
    image side ninon panic:
        im.FactorScale("side/ninonpanic.png", 0.3)

    image side ninon surp:
        im.FactorScale("side/ninonsurp.png", 0.3)

    image side ninon wink:
        im.FactorScale("side/ninonwink.png", 0.3)

    image side monica ddung:
        im.FactorScale("side/monicaddung.png", 0.3)

    image side monica dere:
        im.FactorScale("side/monicadere.png", 0.3)

    image side kuka smile:
        im.FactorScale("side/kuka.png", 0.3)

    image side kuka dere:
        im.FactorScale("side/kukadere.png", 0.3)

    image side kuka surp:
        im.FactorScale("side/kukasurp.png", 0.3)

    image side yuki smile:
        im.FactorScale("side/yuki.png", 0.3)

    image side yuki angry:
        im.FactorScale("side/yukiangry.png", 0.3)

    image side yuki proud:
        im.FactorScale("side/yukiproud.png", 0.3)
    
    define player_name = "가상의 이름 simulated name"

    define player = Character("name", dynamic = True, color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed")

    define monster = Character("마물", color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed")

    define ch_peco = Character("페코린느", color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed")

    define ch_kokoro = Character("콧코로", color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed")

    define ch_kyaru = Character("배신자", color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed")

    define ch_gura = Character("구라노스케", color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed")

    define ch_syokuin = Character("여직원", color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed")

    define ch_rima = Character("역겹게 생긴 짐승", color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed")

    define ch_head = Character("머리가 대단한 손님", color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed")

    define ch_head_2 = Character("머리가 대단했던 손님", color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed") 

    define ch_town = Character("마을 주민", color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed")

    define ch_oedo = Character("오에도 주민 1", color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed")

    define ch_oedo2 = Character("오에도 주민 2", color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed")

    define ch_oedo3 = Character("오에도 주민 3", color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed")

    define ch_oedo4 = Character("오에도 주민 4", color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed")
## 나래이터류 ############################
init:
    define narrator = Character(None, kind = nvl)
    define ch_nar = Character(None, ctc = 'ctc_icon', ctc_position = "fixed")
    define centered = Character(what_bold = True, color = "#000000", ctc = 'ctc_icon', ctc_position = "fixed")
    define hatena = Character('???', color = "#ffffff", ctc = 'ctc_icon', ctc_position = "fixed")
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
    define point = 0
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
    ## 쿠우카
    image cg_kuka_ykt_1:
        im.FactorScale("cg/kuka/kuka_yukata_1.png", 1.0)
    image cg_kuka_ykt_2:
        im.FactorScale("cg/kuka/kuka_yukata_2.png", 1.0)
    image cg_kuka_ykt_3:
        im.FactorScale("cg/kuka/kuka_yukata_3.png", 1.0)

    image cg_kuka_onsen_01:
        im.FactorScale("cg/kuka/kuka_onsen_01.png", 0.67)
    image cg_kuka_onsen_02:
        im.FactorScale("cg/kuka/kuka_onsen_02.png", 0.67)
    image cg_kuka_onsen_03:
        im.FactorScale("cg/kuka/kuka_onsen_03.png", 0.67)
    image cg_kuka_onsen_hand_01:
        im.FactorScale("cg/kuka/kuka_onsen_hand_01.png", 0.67)
    image cg_kuka_onsen_hand_02:
        im.FactorScale("cg/kuka/kuka_onsen_hand_02.png", 0.67)
    
    image cg_kuka_end1:
        im.FactorScale("cg/kuka/1.png", 1.0)
    image cg_kuka_end2:
        im.FactorScale("cg/kuka/2.png", 1.0)
    image cg_kuka_end3:
        im.FactorScale("cg/kuka/3.png", 1.0)
    image cg_kuka_end4:
        im.FactorScale("cg/kuka/4.png", 1.0)
    image cg_kuka_end5:
        im.FactorScale("cg/kuka/5.png", 1.0)
    image cg_kuka_end6:
        im.FactorScale("cg/kuka/6.png", 1.0)
    image cg_kuka_end7:
        im.FactorScale("cg/kuka/7.png", 1.0)
    image cg_kuka_end8:
        im.FactorScale("cg/kuka/8.png", 1.0)
    image cg_kuka_end9:
        im.FactorScale("cg/kuka/9.png", 1.0)
    image cg_kuka_end10:
        im.FactorScale("cg/kuka/10.png", 1.0)
    image cg_kuka_end11:
        im.FactorScale("cg/kuka/11.png", 1.0)
    image cg_kuka_end12:
        im.FactorScale("cg/kuka/12.png", 1.0)
    image cg_kuka_end13:
        im.FactorScale("cg/kuka/13.png", 1.0)
    image cg_kuka_end14:
        im.FactorScale("cg/kuka/14.png", 1.0)
    image cg_kuka_end15:
        im.FactorScale("cg/kuka/15.png", 1.0)
    image cg_kuka_end16:
        im.FactorScale("cg/kuka/16.png", 1.0)
    image cg_kuka_end17:
        im.FactorScale("cg/kuka/17.png", 1.0)
    image cg_kuka_end18:
        im.FactorScale("cg/kuka/18.png", 1.0)
    image cg_kuka_end19:
        im.FactorScale("cg/kuka/19.png", 1.0)
    ## 유키
    image bg_cg_yuki_01:
        im.FactorScale("library/bg_cg_yuki_01.png", 1.0)
    image cg_yuki_01:
        im.FactorScale("library/yuki_01.png", 1.0)
    image cg_yuki_02:
        im.FactorScale("library/yuki_02.png", 1.0)
    image cg_yuki_03:
        im.FactorScale("library/yuki_03.png", 1.0)
    image cg_yuki_03_plus:
        im.FactorScale("library/yuki_03_plus.png", 1.0)

    image cg_yuki_onsen_01:
        im.FactorScale("cg/yuki/yuki_01.png", 1.0)
    image cg_yuki_onsen_02:
        im.FactorScale("cg/yuki/yuki_02.png", 1.0)

    image cg_yukiend1:
        im.FactorScale("cg/yuki/1.png", 1.0)
    image cg_yukiend2:
        im.FactorScale("cg/yuki/2.png", 1.0)

    
    ## 모니카
    image cg_monica_first_01:
        im.FactorScale("cg/monica/monica_1_01.png", 1.0)
    image cg_monica_first_02:
        im.FactorScale("cg/monica/monica_1_02.png", 1.0)
    image cg_monica_first_03:
        im.FactorScale("cg/monica/monica_1_03.png", 1.0)    
    
    image cg_monica_onsen_01:
        im.FactorScale("cg/monica/monica_onsen_01.png", 0.2845)
    image cg_monica_onsen_02:
        im.FactorScale("cg/monica/monica_onsen_02.png", 0.2845)
    image cg_monica_onsen_03:
        im.FactorScale("cg/monica/monica_onsen_03.png", 0.2845)

    image cg_monica = "cg/monica/bg.png"

    image cg_monica_basic:
        "cg/monica/1.png"
        pause 2.5
        "cg/monica/1b.png"
        pause 0.08
        repeat
    image cg_monica_bbang:
        "cg/monica/bbang1.png"
        pause 2.5
        "cg/monica/bbang1b.png"
        pause 0.08
        repeat
    image cg_monica_dere1:
        "cg/monica/dere1.png"
        pause 2.5
        "cg/monica/dere1b.png"
        pause 0.08
        repeat
    image cg_monica_dere2:
        "cg/monica/dere2.png"
        pause 2.5
        "cg/monica/dere2b.png"
        pause 0.08
        repeat
    image cg_monica_emb1:
        "cg/monica/emb1.png"
        pause 2.5
        "cg/monica/emb1b.png"
        pause 0.08
        repeat
    image cg_monica_emb2:
        "cg/monica/emb2.png"
        pause 2.5
        "cg/monica/emb2b.png"
        pause 0.08
        repeat
    image cg_monica_emb3:
        "cg/monica/emb3.png"
        pause 2.5
        "cg/monica/emb3b.png"
        pause 0.08
        repeat
    image cg_monica_shame1:
        "cg/monica/shame1.png"
        pause 2.5
        "cg/monica/shame1b.png"
        pause 0.08
        repeat
    image cg_monica_shame2:
        "cg/monica/shame2.png"
        pause 2.5
        "cg/monica/shame2b.png"
        pause 0.08
        repeat
    ## 니논
    image ninon_pingping:
        im.FactorScale("cg/ninon/ninon_pingpong.png", 0.5)
    image ninon_encore:
        im.FactorScale("cg/ninon/ninon_encore.png", 0.5)

    image cg_ninon_onsen_01:
        im.FactorScale("cg/ninon/ninon_onsen_1.png", 1.0)
    image cg_ninon_onsen_02:
        im.FactorScale("cg/ninon/ninon_onsen_2.png", 1.0)
    image cg_ninon_onsen_03:
        im.FactorScale("cg/ninon/ninon_onsen_3.png", 1.0)

    image cg_ninon_happy_01 = "library/cg_ninon_happy_01.png"
    image cg_ninon_happy_02 = "library/cg_ninon_happy_02.png"
    image cg_ninon_happy_03 = "library/cg_ninon_happy_03.png"
    image cg_ninon_happy_04 = "library/cg_ninon_happy_04.png"
    image cg_ninon_happy_05 = "library/cg_ninon_happy_05.png"

    ## 콧코로
    image cg_kokoro_01 = "cg/kokoro/kokoro1.png"
    image cg_kokoro_02 = "cg/kokoro/kokoro2.png"
    image cg_kokoro_03 = "cg/kokoro/kokoro3.png"
    image cg_kokoro_04 = "cg/kokoro/kokoro4.png"

    image cg_kokoro:
        "cg/kokoro/1.png"
        pause 2.0
        "cg/kokoro/2.png"
        pause 0.05
        "cg/kokoro/3.png"
        pause 0.05
        "cg/kokoro/4.png"
        pause 0.05
        "cg/kokoro/5.png"
        pause 0.1
        "cg/kokoro/6.png"
        pause 0.1
        "cg/kokoro/7.png"
        pause 0.05

        repeat


    ## 공통
    image cg_raiden:
        im.FactorScale("cg/common/raiden.png", 0.32)

    image cg_common:
        im.FactorScale("cg/common/common.png", 1.0)
    image cg_common2:
        im.FactorScale("cg/common/common2.png", 1.0)

    image cg_kimura:
        im.FactorScale("cg/common/kimura.png", 1.0)
    image cg_kyaru:
        im.FactorScale("cg/common/kyaru.png", 1.0)
    ## 참피

    image cg_champi = "cg/common/champi.png"

## persistent 변수 ##################################
init:
    define persistent.clue = False  
    define persistent.practicepong = True
    define persistent.clues_hankachi = False
    define persistent.clues_letter = False
    define persistent.clues_key = False
    define persistent.clues_unagi = False
    define persistent.clues_kiroku = False
    define persistent.clues_akudaikan = False
    define persistent.clues_syokuin = False
    define persistent.clues_rima = False
    define persistent.clues_yanki = False
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
    define lose_point = 0
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
                if win_point > 2:
                    self.computerspeed = 1520.0
                else:
                    self.computerspeed = 380.0

                # The position, delta-position, and the speed of the
                # ball.
                self.bx = self.PADDLE_X + self.PADDLE_WIDTH + 10
                self.by = self.playery
                self.bdx = .5
                self.bdy = .5
                if win_point > 2:
                    self.bspeed = 1400.0
                else:
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

        if persistent.practicepong == True:
            show stand_Ninon_yukata_wink with dissolve
            ch_ninon "쇼군~ 쫄보 입니까? 빨리 시작하자 입니다~!!"

            hide stand_Ninon_yukata_wink
            jump pingpong_choice

        if win_point == 0 and persistent.practicepong == False:
            if _return == "니논":
                ## 0승 1패
                $ point_ninon = point_ninon + 1
                play music "audio/main/9bbong.mp3"
                show ninon_pingping with dissolve

                ch_ninon "거기다!!!! 입니다!!!"

                show ninon_pingping with hpunch

                ch_ninon "「인법 {font=NanumGothic.ttf}· {/font}후쥐산 쪼궤기」 !!!!!"

                player "큭……?!!"

                $ renpy.pause(1.0)

                player "져……"

                player "졌다……"

                ch_ninon "후…… 또 시시한 것을 베어 버렸군 입니다."

                ch_ninon "하지만 너무 상심하지 마십시오 입니다~"

                ch_ninon "쇼군이 약한 것이 아니라 니논이 강한 것 입니다~!"

                player "진짜 잘하네……"

                player "허풍이 아니었구나……"

                ch_ninon "엣헴~ 입니다."

                hide ninon_pingping

                stop music
                jump sceneNum16Common
            else:
                ## 1승 0패
                $ win_point = win_point + 1
                show stand_Ninon_yukata_angry with dissolve

                ch_ninon "……"

                ch_ninon "한 번 더 해요 입니다……!!"

                hide stand_Ninon_yukata_angry

                player "얼마든지……!"

                jump play_pong
        elif win_point == 1 and persistent.practicepong == False:
            if _return == "니논":
                ## 1승 1패
                $ point_ninon = point_ninon + 1
                play music "audio/main/9bbong.mp3"
                show ninon_pingping with dissolve

                ch_ninon "거기다!!!! 입니다!!!"

                show ninon_pingping with hpunch

                ch_ninon "「인법 {font=NanumGothic.ttf}·{/font} 후쥐산 쪼궤기」 !!!!!"

                player "큭……?!!"

                $ renpy.pause(1.0)

                player "져……"

                player "졌다……"

                ch_ninon "후…… 또 시시한 것을 베어 버렸군 입니다."

                ch_ninon "하지만 너무 상심하지 마십시오 입니다~"

                ch_ninon "쇼군이 약한 것이 아니라 니논이 강한 것 입니다~!"

                player "……근데 전 판은 내가 이겼……"

                ch_ninon "어허~ 입니다."

                ch_ninon "마지막에 이기는 사람이 이긴 것이다 입니다~"

                ch_nar "무슨 논리야……!!"

                hide ninon_pingping
                stop music
                jump sceneNum16Common
            else:
                ## 2승 0패
                $ win_point = win_point + 1
                stop music
                show stand_Ninon_yukata_daiji with dissolve

                ch_ninon "…………"

                ch_ninon "한 번 더."

                hide stand_Ninon_yukata_daiji

                player "말이 짧아졌어……?!"

                jump play_pong
        elif win_point == 2 and persistent.practicepong == False:
            if _return == "니논":
                ## 2승 1패
                play music "audio/main/9bbong.mp3"
                show ninon_pingping with dissolve

                ch_ninon "거기다!!!! 입니다!!!"

                show ninon_pingping with hpunch

                ch_ninon "「인법 {font=NanumGothic.ttf}·{/font} 후쥐산 쪼궤기」 !!!!!"

                player "큭……?!!"

                $ renpy.pause(1.0)

                player "져……"

                player "졌다……"

                ch_ninon "후…… 또 시시한 것을 베어 버렸군 입니다."

                ch_ninon "하지만 너무 상심하지 마십시오 입니다~"

                ch_ninon "쇼군이 약한 것이 아니라 니논이 강한 것 입니다~!"

                player "……근데……"

                player "따지고 보면 내가 더 많이 이겼……"

                ch_ninon "쓰읍!!"

                ch_ninon "패배를 순순히 인정하는 것도 SAMURAI의 덕목 입니다!!"

                ch_ninon "쇼군으로서 모두의 귀괌이 되십시오 입니다……!!"

                ch_nar "이…… 치사한……"

                hide ninon_pingping
                stop music
                jump sceneNum16Common
            else:
                ## 3승 0패
                $ win_point = win_point + 1
                show ninon_encore with dissolve
                ch_ninon "{b}{size=30}ENCORE.{/size}{/b}"

                player "?!"

                ch_ninon "{b}{size=30}다시.{/size}{/b}"

                player "그림체가……"

                ch_ninon "{b}{size=30}다시!!!!{/size}{/b}"

                player "히익……"
                hide ninon_encore
                jump play_pong
        elif win_point == 3 and persistent.practicepong == False:
            if _return == "니논":
                $ point_ninon = point_ninon - 1
                ## 3승 1패
                play music "audio/main/9bbong.mp3"
                show ninon_pingping with dissolve

                ch_ninon "거기다!!!! 입니다!!!"

                show ninon_pingping with hpunch

                ch_ninon "「인법 {font=NanumGothic.ttf}·{/font} 후쥐산 쪼궤기」 !!!!!"

                player "큭……?!!"

                $ renpy.pause(1.0)

                player "져……"

                player "졌다……"

                ch_ninon "후…… 또 시시한 것을 베어 버렸군 입니다."

                ch_ninon "하지만 너무 상심하지 마십시오 입니다~"

                ch_ninon "쇼군이 약한 것이 아니라 니논이 강한 것 입니다~!"

                player "……근데……"

                player "따지고 보면 내가 더 많이 이겼……"

                ch_ninon "쓰읍!!"

                ch_ninon "패배를 순순히 인정하는 것도 SAMURAI의 덕목 입니다!!"

                ch_ninon "쇼군으로서 모두의 귀괌이 되십시오 입니다……!!"

                ch_nar "이…… 치사한……"

                hide ninon_pingping
                stop music
                jump sceneNum16Common
            else:
                ## 4승 0패
                $ win_point = win_point + 1
                $ point_ninon = point_ninon - 1
                show stand_Ninon_yukata_daiji with dissolve

                ch_ninon "…………"

                ch_ninon "……………………"
                
                ch_ninon "……드러워서 진짜………"

                player "?!"

                ch_ninon "니가 이겼다 입니다."

                player "?!?!"

                ch_ninon "이 악물고 여자애 이겨먹어서 좋겠다 입니다."

                ch_nar "……"

                $renpy.pause(1.0)

                ch_nar "내가 이겼다 히히~"

                hide stand_Ninon_yukata_daiji
                hide bg_naibu
                jump sceneNum16Common
        return


label pong_done:

    show stand_Ninon

    menu:
        ch_ninon "한 판 더 할래?"

        "물론.choice_1":

            jump play_pong

        "그만할래.choice_2":

            pass
            
    hide stand_Ninon
    return

## 게임 시작 ##############################
## 이름 짓기 #############################
label naming:
    scene bg_black
    show bg_whatsyourname onlayer forward with squares
    # 아메스 테마 서서히 커지다가 고정
    
    $ renpy.pause(1.0)
    $ player_name = renpy.input("내 이름...")
    $ name = player_name
    $ finalConso = finalChecker(name)
    hide bg_whatsyourname onlayer forward
    window hide
    if len(name) > 10:
        hatena "어떻게 사람 이름이 [name]일수가 있지 ㅋㅋ"
        hatena "진짜 이름을 10자 이내로 알려 줘."
        jump naming
    elif len(name) == 0:
        hatena "……알려 주고 싶지 않다는 걸까?"

        hatena "곤란한걸…… 다시 한 번 생각해 줘."

        jump naming
    elif name == "페코린느":
        hatena "당신도 제 이름을 뺏어 가려는 걸까요? 장난 아니네요~☆" 
        jump naming    
    elif name == "캬루" or name == "배신자":
        hatena "하? 머리 어떻게 된 거 아니야? 죽여버린다!"
        jump naming  
    elif name == "콧코로":
        hatena "주인님, 남의 이름을 멋대로 사용하시는 것은 「떽」입니다."
        jump naming
    elif name == "니논":
        hatena "두구두구둥~ 그 이름은 아니 되오 입니다, 쇼군~!"
        jump naming
    elif name == "모니카":
        hatena "귀공, 이름 정도는 스스로 생각하는 것이 어떤가……?"
        jump naming
    elif name == "쿠우카":
        hatena "히이이~~!!! 이제는 이름까지 빼앗아, 정체성도 감정도 잃어버린 고기 인형으로 만들어 버리시려는 건가요!!!! 도S 씨의 가학성은 정말이지 상상을 뛰어넘는 수준이네요……!!!!"
        jump naming
    elif name == "유키":
        hatena "후훗…… 아름다운 나를 동경하는 것은 이해하지만, 이름까지 따라하려는 건 참아 줬으면 좋겠는데~"
        jump naming
    elif name == "구라노스케":
        hatena "{b}{size=30}오에도---!!!!!!!!!{/size}{/b}"
        jump naming
    elif name == "아메스":
        hatena "흐응…… 당신은 뭔가 알고 있는 걸까나."

        hatena "그렇지만, 나는 당신의 진짜 이름이 알고 싶은걸."

        jump naming
    elif name == "키무라" or name == "키무라유이토" or name == "키무라 유이토":
        hatena "천장을 찍고 싶습니까, Korean 키시쿤?"

        jump naming
    elif name == "아유미":
        $ renpy.movie_cutscene("library/ames.mpg")
        show cg_ames onlayer middle

        hatena "어서 와, {color=#51f07c}아유미{/color}. 그게 당신의 이름이구나."

        hatena "지금부터 당신이……"

        ch_ayumi "{b}{size=30}잠깐 잠깐 잠깐!!!!!!!{/size}{/b}"

        ch_ayumi "{b}{size=30}잠깐 기다려 주세요!!!!!{/size}{/b}"

        hatena "뭐?!"

        ch_ayumi "어째서 아무렇지도 않게 넘어가시는 건가요!!!"

        ch_ayumi "그건 제 이름이란 말이에요……!!"

        hatena "이건 대체…… 저런 아이는 한 번도 본 적이 없는데……!"

        hatena "뭔가 오류가……?!"

        ch_ayumi "오류 아니에요오!!!!"

        hatena "……뭐……"

        hatena "……뭐가 뭔진 모르겠지만…… 다른 이름을 알려 주겠어……?"

        hatena "이 오류는 내가 고쳐 볼 테니까……"

        ch_ayumi "그러니까 오류 가흔 게…… 우붑!!!!!"

        hide cg_ames onlayer middle
        jump naming
    else:
        play music "audio/main/ames.mp3" fadein 3.0
        $ renpy.movie_cutscene("library/ames.mpg")
        
        show cg_ames onlayer middle
        hatena "어서 와, [name]. 그게 당신의 이름이구나."

        hatena "지금부터 당신이 보게 될 것은, 이른바 꿈 같은 거야. 이미 겪어 보았거나, 언젠가 일어날지도 모르는, 한여름 밤의 꿈 같은 일. ‘몽상’이라 불러도 좋겠네."

        menu:
            "당신은 누구죠?choice_1":
                hatena "내가 누구냐고? 알 필요 없다."
                hatena "……호기심도 많네. 내 정체 같은 건 중요하지 않아."
                hatena "당신이 알아야 할 건 단지…… 이제부터 여러 명의 ‘소녀’들을 만나게 된다는 것과,"
                hatena "당신이 어떤 선택을 내리느냐에 따라 그녀들의 운명이 조금씩 바뀌게 된다는 것밖에 없어. 그럼 잘해 봐. 행운을 빌게, 왕자님♪"
                hide cg_ames onlayer middle
            ##텍스트 사라지면서 볼륨 서서히 off    
                jump start    
    return

## 프롤로그 #############################
label start:
    stop music
    $ camera_reset()
    $ persistent.clue = False
    $ persistent.clues_hankachi = False
    $ persistent.clues_letter = False
    $ persistent.clues_key = False
    $ persistent.clues_unagi = False
    $ persistent.clues_kiroku = False
    $ persistent.clues_akudaikan = False
    $ persistent.clues_syokuin = False
    $ persistent.clues_rima = False
    $ persistent.clues_yanki = False
    $ love_point = 0
    $ point_monica = 0
    $ point_ninon = 0
    $ point_kuka = 0
    $ point_yuki = 0
    $ point = 0
## 이름 생성 여부 ######################
    if (player_name == "가상의 이름 simulated name"):
        jump naming
    else:
        hide bg_whatsyourname
        pass        
## S# 1. 초원 ##########################
    show bg_black
    scene bg_field onlayer background with fade # 배경화면

    play music "audio/main/2sentou.mp3"

    hatena "빈틈! 받아라앗...!!"

    ## 마물 cg DIS
    show stand_monster onlayer middle with dissolve

    ## 총소리
    play sound "audio/sound/gunshot.mp3"
    ## 피격효과, 화면 흔들림 효과
    show hit onlayer forward:
        xalign 0.5 yalign 0.6
    show bg_field onlayer background with hpunch
    
    monster "커르륵...!"
    hide hit onlayer forward
    hide stand_monster onlayer middle

    ## 모니카 웃는 표정
    show stand_Monica onlayer middle with dissolve

    ch_monica "됐다! 움직임이 봉쇄됐어! 지금이다, 니논! 한 방 먹여!!"
    hide stand_Monica onlayer middle
    show stand_Ninon onlayer middle with dissolve

    ch_ninon "ROGER! 이거나 먹어라, 입니다! {font=NanumGothic.ttf}{b}{i}{size=24}「인법 · 쇙강 줜병 회오뤼」{/size}{/i}{/b}{/font}~!!"
    hide stand_Ninon onlayer middle

    ## 마물 cg
    ## 불길이 치솟는 효과 ## E - 불길 치솟음 ## 화면 흔들림 효과(지글지글거리는 느낌 정도로 작게)
    show stand_monster onlayer middle with dissolve
    play sound "audio/sound/fire.mp3"
    show fire_big onlayer forward:
        xpos -100 ypos -70
    show stand_monster onlayer middle with hpunch
    monster "쿠아아악!! 크르륵..."
    hide fire_big onlayer forward
    ## 울부짖는 효과, 화면 흔들림 효과
    $renpy.pause(0.5)
    play sound "audio/sound/growl.mp3"
    show pohyo onlayer forward:
        xalign 0.5 yalign 0.5
    show stand_monster onlayer middle with hpunch
    ## 괴물 울음소리

    monster "크워어어어어!!"
    hide pohyo onlayer forward

    hide stand_monster onlayer middle


    show stand_Monica_ddung onlayer middle with dissolve

    ch_monica "칫… 이 정도로는 어림도 없나. 모두들, 뒤로 물러나! 놈이 반격해 온다!"
    
    hide stand_Monica_ddung onlayer middle

    show stand_Kuka_mousou onlayer middle with dissolve

    ch_kuka "아…… 아무리 쿠우카라도 이렇게 커다란 건…… 쿠…… 쿠우카, 돌아오지 못할 강을 건너 버릴지도……! 크흐흣……"
    ##쿠우카 어둡게
    hide stand_Kuka_mousou onlayer middle

    ch_ayumi "쿠…… 쿠우카 씨……? 무슨 소릴 하는 거예요……?! 혼자 너무 앞에 있으면 위험해요……!!"
    
    
    show stand_Monica_surprised onlayer middle with dissolve

    ## 피격 효과 ## 칼이 부딪히는 금속음
    play sound "audio/sound/knife1.wav"
    show hit onlayer forward:
        xalign 0.5 yalign 0.6

    ch_monica "큭! 이건 버틸 수가… 유키, 서포트를!"
    hide hit onlayer forward
    hide stand_Monica_surprised onlayer middle

    show stand_Yuki_angry onlayer middle with dissolve

    ch_yuki "뭐? 나는 분명히 말했다? 데려와도 아~무것도 안 할 거라고. 아름다운 내 몸에 생채기라도 나면 책임질 거야?"    
    
    show stand_Yuki_shamed onlayer middle
    hide stand_Yuki_angry onlayer middle

    ch_yuki " 앗…… 나뭇잎에 맺힌 이슬…… 내 모습이 비쳐서 너무 예뻐…… 하아……"

    hide stand_Yuki_shamed onlayer middle

    show stand_Ninon_angry onlayer middle with dissolve

    ch_ninon "유키 씨, 무사답지 못하다 입니다~! 모름쥐기 사무라이라면 아무리 YABAI한 상황일지라도…"
    
    ## 니논 화난 표정 주변에 불이 붙는 효과/ 불길 치솟음

    ## 니논 놀란 표정
    hide stand_Ninon_angry onlayer middle

    play sound "audio/sound/fire.mp3"
    
    show fire_small_2 onlayer forward:
        xpos -70 ypos 180
    show fire_small_3 onlayer forward:
        xpos 300 ypos 180
    show fire_small onlayer forward:
        xpos 100 ypos 210
    
    show stand_Ninon_panic onlayer middle at center:
        easeout 0.3 ypos -50
        ease 0.2 ypos 50
        easeout 0.3 ypos -50
        ease 0.2 ypos 50 
    
    ch_ninon "우와아아아앗!!! 불이 옮겨붙었다 입니다!!! 후끼약!!!"

    hide fire_small onlayer forward
    hide fire_small_2 onlayer forward
    hide fire_small_3 onlayer forward

    #둔탁한 피격음
    play sound "audio/sound/hit.wav"
    hide stand_Ninon_panic onlayer middle
    show stand_Kuka_mousou onlayer middle with dissolve##쿠우카중앙으로 서서히 작아지다 사라짐
    #멀리 날아가는 소리
    
    ch_kuka "쿠, 쿠우카, 날아가버려요오오옷!!!!"
    play sound "audio/sound/fly.mp3"
    show stand_Kuka_mousou onlayer middle:
        rotate 0
        linear 0.4 rotate 720 ypos 0
    $renpy.pause(4.0)
    hide stand_Kuka_mousou onlayer middle with dissolve
    show stand_Monica_ddung onlayer middle with dissolve
    ch_monica "니논! 쿠우카!! 이대로면 모두가 위험… 에에잇! 이판사판이다!"
    # 칼을 검집에서 빼는 소리
    stop music fadeout 1.0
    play sound "audio/sound/baldo.mp3"

    ch_monica "자전{font=NanumGothic.ttf}―{/font}"

    show bg_black onlayer middle

    ch_monica "{font=NanumGothic.ttf}―{/font}일섬!!"
    #일순간 까맣게 된 화면을 가로로 베는 효과
    play sound "audio/sound/knife2.wav"
    show knife_issen onlayer forward
    #칼로 베는 소리

    $renpy.pause(1.0)
    hide bg_black onlayer middle
    hide stand_Monica_ddung onlayer middle
    hide bg_field onlayer background
## S# 2.길드 하우스 #########################################
    scene bg_black
    hide knife_issen onlayer forward
    play music "audio/main/3town.mp3" fadein 1.0
    show bg_guildhouse_s with fade
    ch_nar "아야."

    ch_nar "식칼에 베였다."

    ch_nar "콧코로의 눈망울이 연상되는 와인색의 피가 손끝에 맺힌다. 아프다."

    ## 피 묻은 손수건 이미지 팝업
    $ persistent.clues_hankachi = True
    show ob_hankachi with dissolve:
        xpos 430 yalign 0.3

    ch_nar "언젠가 콧코로에게 받았던 손수건으로 피를 닦았다."

    hide ob_hankachi

    ch_nar "콧코로…… 언제 와? 나 배고파. 무서워."

    ch_nar "콧코로는 돈 많이 벌어오겠다며 집을 나간 뒤로 며칠째 연락이 안 된다."

    ch_nar "페코린느와 배신자는 던전으로 식재료 탐방을 간다길래 따라가고 싶다고 했더니,"

    ch_nar "“아하하, 약해 빠진 주제에 또 누구 발목을 잡으려는 건가요? 장난 아니네요! 얌전히 길드하우스나 지키고 있으세요☆”"

    ch_nar "“하아? 벌레 한 마리도 제대로 못 잡는 멍청한 돼지가 어딜 따라오겠다고? 죽여 버린다?”"

    ch_nar "라며 나만 남겨 두고 가 버렸다."

    ch_nar "수영복만 벗으면 아무것도 아닌 것들이……"

    ch_nar "항상 콧코로가 요리를 해 줬는데 이젠 밥 해 줄 사람이 아무도 없다. 이대로면 정말 굶어 죽을지도 모른다."

    ch_nar "그래서 직접 요리를 해 보려고 식칼을 꺼냈는데 쥐는 법을 몰라서 바로 손가락을 베였다."

    ch_nar "콧코로…… 생전 손에 물 한 번 묻혀 본 적 없는 나에게 이런 수모를 겪게 하다니……"

    show ob_kokkoro with dissolve:
        xpos 300 ypos 15
    
    ch_nar "돌아오면 잘못했다고 울며불며 매달릴 때까지 단식투쟁을 할 것이다."

    hide ob_kokkoro

    ## 대화창 사라짐
    window hide
    $ renpy.pause(1.5)
    ## 문 두드리는 소리
    play sound "audio/sound/knocking.wav"
    ## 잠깐 텀
    $ renpy.pause(1.0)

    player "마망!!!! 내가 잘못했어!! 다시는 반찬 투정 안 할게!!!"    

    ## 대화창 사라짐
    window hide
    ## 문 열리는 소리
    play sound "audio/sound/opendoor.wav"
    ## 잠깐 텀
    $ renpy.pause(1.0)

    ## 모니카 우는표정 cg
    show stand_Monica_crying with dissolve
    ch_nar "에이씨, 콧코로가 아니잖아." 
    
    ch_monica "훌쩍…… 귀, 귀공…… 훌쩍, 날 좀…… 도와주게…… 으아앙, 우아아앙~"

    menu:
        "뭐야...choice_1":
            ch_monica "그, 그게…… 훌쩍."

            player "소난다……"

            ## 모니카 시무룩한 표정
            ch_monica "?"
            pass
        "왜 울고 있는거야?choice_2":
            ch_monica "그, 그게…… 훌쩍."

            player "소난다……"

            ## 모니카 시무룩한 표정
            ch_monica "?"
            pass
    
    
    hide stand_Monica_crying
    ## 길드하우스 페이드 아웃
    hide bg_guildhouse_s with fade
    ## 마을 브금 불륨 페이드 아웃
    stop music fadeout 1.0
    
    ## 까만 배경

    centered "몇 시간 전……"

    ## 마을 브금 볼륨 페이드 인
    play music "audio/main/3town.mp3" fadein 1.0
    ## 길드 하우스 cg 페이드 인
    scene bg_guildhouse with fade
    
    ## 모니카 화난 표정 페이드
    show stand_Monica_ddung with dissolve
    ch_monica "이대로는 안 돼!"
    show stand_Monica_ddung at movetoleft
    ## 모니카가 왼쪽으로 밀리면서 니논 오른쪽에 팝업
    show stand_Ninon at right with dissolve ## 웃는 표정
    ## 모니카 어둡게, 니논 밝게
  
    ch_ninon "모니카 씨~? 무슨 문제라도 있다 입니까? 다시마 초절임 먹을래요?"

    ## 니논 어둡게, 모니카 밝게

    ##모니카 놀란 표정
    hide stand_Monica_ddung
    show stand_Monica_surprised at left with dissolve
    ch_monica "뭐, 뭐지 그건? 달콤한 과자인가…?"
    ##모니카 화난 표정
    window hide
    hide stand_Ninon
    
    show stand_Monica_surprised at movetocenter
    show stand_Monica_ddung
    hide stand_Monica_surprised
    extend " ……아니, 아니! 그게 중요한 게 아니다!"

    ch_monica "우리는 ‘바이스플뤼겔 랜드솔지부’다! 마물을 소탕하고, 곤란에 빠진 사람들을 도와주는 유능한 모험가 길드!"
    ch_monica "……였어야 했는데, 마지막으로 마물을 토벌했던 게 언제인지 이제는 기억도 안 날 지경이다. 채집 의뢰만 산더미처럼 쌓여 있어! 이게 뭐냐! 우리는 전투 길드란 말이다~!!"

    hide stand_Monica_ddung
    show stand_Kuka with dissolve

    ch_kuka "쿠, 쿠우카는 식물 채집도 좋다고 생각해요… 숲에서 가끔 식물형 마물도 튀어나와서… 도끼로도 잘 안 끊어지는 억센 넝쿨로 온몸을 잔뜩 조여오면…"
    ## 쿠우카 망상하는 표정으로 변경
    show stand_Kuka_mousou
    hide stand_Kuka

    extend " 크, 크흣, 크헤헤헷…"

    hide stand_Kuka_mousou
    show stand_Yuki_angry with dissolve #화난 표정
    ch_yuki "나참~ 대체 뭐가 불만인데? 채집 의뢰도 어쨌든 사람들을 도와주는 거잖아. 그리고 오에도에서 엄청나게 못생긴 마물을 해치웠던 건 머리에서 지워버린 거야?"

    hide stand_Yuki_angry
    show stand_Monica_ddung at center with dissolve:
        easeout 0.3 ypos -50
        ease 0.2 ypos 50
        easeout 0.3 ypos -50
        ease 0.2 ypos 50 
        ##팔짝 뛰는 모션
    ch_monica "그래서 더 문제라는 거다!! 그 강력한 마물을 쓰러뜨릴 정도의 역량을 가지고 있으면서, 이전에 비해 바뀐 게 아무것도 없잖아!"

    ch_monica "다들 약속이라도 한 것마냥 비전투 의뢰만 잔뜩 수주해오고! 그대들은 모험가 길드를 대체 뭐라고 생각하는 건가?!"
    hide stand_Monica_ddung
    show stand_Ninon with dissolve ##자신만만
    ch_ninon "니논도 할 때는 한다 입니다, 모니카 씨! 명령만 내리신다면 당장이라도 마물녀석들의 모가쥐를 따버릴 수 있습니다~!"
    hide stand_Ninon
    show stand_Monica with dissolve ##자신만만
    
    ch_monica "……그래. 말 잘 했다, 니논!" 
    ## 모니카 웃는 표정
    ch_monica "분명 우리는 숲이나 평원에 돌아다니는 어지간한 마물 정도는 거뜬히 해치울 정도로 강해. 그럼에도 마물 소탕에 있어서는 별다른 성과를 보이지 못하고 있다."

    ch_monica "모든 일에는 타당한 이유가 존재하기 마련. 그렇다면 우리들에게 부족한 건 대체 뭘까? 아유미! 대답해 봐라!"
    ## 호흡 한 번 끊기
    $renpy.pause(1.0)
    ## 모니카 어둡게
    hide stand_Monica
    ch_ayumi "힉, 히이익……? 저, 저, 저 말인가요?! 그건, 그, 저기,"

    ch_ayumi "제… 제가 생각하응기잇!! 흐에… 혀 깨무러써…"
    ## 모니카 밝게/뚱한 표정
    show stand_Monica_down with dissolve
    ch_monica "……"
    ## 모니카 화난 표정
    show stand_Monica_ddung
    hide stand_Monica_down
    ch_monica "…………바이스플뤼겔에 가장 부족한 것은 바로…………"

    show highlight onlayer forward with hpunch

    ch_monica "…………‘실전’이다!!"

    hide highlight onlayer forward

    ch_monica "아무리 강력한 전사라 해도 실전 경험이 없다면 지나가던 들개 한 마리 상대하는 것도 버거울 터."

    show stand_Monica_ddung at movetoleft
    show stand_Ninon_surprise at right with dissolve## 니논 놀란 표정
    ## 모니카 어두워지고 니논 밝게

    ch_ninon "지나가던 들개 씨…… 무섭다 입니다……!"
    hide stand_Ninon_surprise with dissolve
    
    show stand_Monica_ddung at movetocenter with hpunch
    
    ch_monica "요점이 그게 아니지 않나!!!"

    ch_monica "……우리가 실제로 마물을 해치운 전적은 손에 꼽을 정도다. 그마저도 대부분은 요행에 불과했던 것들이지."

    ## 자신만만한 표정
    show stand_Monica
    hide stand_Monica_ddung
    ch_monica "하지만! 운에 기대지 않고 마물을 쓰러뜨릴 수 있는, 확실한 실력을 쌓는 방법을 우리는 알고 있다! 어떻게?"
    hide stand_Monica
    ## 유키 질색하는 표정
    show stand_Yuki_angry with dissolve
    ch_yuki "잠깐, 설마……"
    hide stand_Yuki_angry
    ## 강조선
    show stand_Monica with dissolve## 자신만만
    show highlight onlayer forward with hpunch

    ch_monica "마물을 왕창 때려잡는 거다!!! 아주 커다랗고 무지막지한 놈들로!!"
    hide highlight onlayer forward
    hide stand_Monica
    show stand_Kuka_mousou at center with dissolve: ## 망상
        ease 0.2 ypos -50
        ease 0.2 ypos 50
    ch_kuka "으히익♥"
    hide stand_Kuka_mousou
    show stand_Monica with dissolve ## 자신만만

    ch_monica "그런 고로 떠날 채비를 서두르도록, 제군들! 곧바로 프라노 평원으로 출발한다!!"
    hide stand_Monica with dissolve
    show stand_Yuki_angry at left with dissolve ## 질색하는 표정
    
    ch_yuki "아니 아니~~ 마물을 잡으러 가자고? 지금 당장~?! 진심이야?"
    ch_yuki "나는 가서도 아무것도 안 할 거니까! 전투 같이 위험한 일엔 끼어들기 싫어! 피부에 안 좋단 말이야~!"

    ## 유키 어둡게
    ch_ayumi "뭐, 뭐어~ 모니카 씨 말씀이 틀린 것도 아니구요……"
    show stand_Yuki_angry at movetoleft
    show stand_Kuka_mousou with dissolve ## 망상

    ch_kuka "힘세고 강한 마물…… 뜨겁고 크고 묵직한…… 크힛, 크흐흣……"

    ## 쿠우카 어둡게
    show stand_Ninon at veryright with dissolve ##자신만만한 표정

    ch_ninon "진군입니다! 찢고 죽인다 입니다!!"

    ## 니논 어둡게
    hide stand_Kuka_mousou
    hide stand_Ninon
    hide stand_Yuki_angry

    show stand_Monica with dissolve ## 자신만만
    ch_monica "그럼 출발이다! 바이스플뤼겔의 긍지를 걸고!!"

    hide stand_Monica with dissolve
    ## 배경 페이드 아웃
    hide bg_guildhouse
    show bg_black
    $renpy.pause(1.0)
    ## 길드하우스 페이드 인
    scene bg_guildhouse_s with fade
    player "……그렇게 긍지가 박살난 거야?"

    show stand_Monica_dere with dissolve ## 빼애액 표정
    ch_monica "박살나지 않았어!!"
    ## 시무룩한 표정으로 변경
    show stand_Monica_down
    hide stand_Monica_dere
    extend " ……나는 그저……"

    ch_monica "……무작정 부딪혀 보면 어떻게든 될 거라고 생각했건만…… 귀공은 내 방식이 잘못됐다고 생각하나?"

    menu:
        "결과가 말해 주고 있잖아choice_1":
            ## 볼빵빵
            show stand_Monica_ddung
            hide stand_Monica_down
            ch_monica "……마, 맞는 말이다만……, 그렇게 말하는 귀공에게는 더 좋은 해결책이 있는 거겠지?"
            ch_monica "자세한 이야기는 우리 길드원들 앞에서 하는 게 어떤가? 지금 바로 출발하도록 하지."
            hide stand_Monica_ddung
        "틀린 방법은 아니었다고 생각해choice_2":
            ## 시무룩한 표정
            ch_monica "빈말이라도 고맙군…… 하지만 우리는 실제로 마물에게 이렇다 할 타격도 주지 못하고 당해 버렸어."
            ch_monica "이대로면 부하들이 입는 피해만 늘어갈 터…… 뭔가 다른 방법이 필요해." 
            ch_monica "귀공, 도움을 줄 수 있겠나? 일단 우리 길드하우스로 자리를 옮기도록 하지."
            hide stand_Monica_down
    ## cg 페이드 아웃
    hide bg_guildhouse_s
    show bg_black
## S# 3.랜드솔 마을, 길드하우스
    scene bg_town with fade
    show stand_Ninon with dissolve ##웃는표정

    ch_ninon "오오~ 쇼군~! 친히 행차하셨나이까 입니다? 기별도 없이 니논을 만나러 오셨다기에 버선발로 뛰쳐나왔사와요 입니다! 기쁨에 못 이겨 할복 해버릴 것 같습니다~!"

    show stand_Ninon at movetoleft ##어둡게
    show stand_Kuka_mousou with fade

    ch_kuka "도, 도S씨, 오랜만이에요……!! 쿠우카를 도S씨가 없으면 살 수 없는 몸으로 만들어놓고, 쿠우카가 먼저 파렴치한 요구를 입밖으로 꺼낼 때까지 몇 날 며칠을 방치하면서 즐기시다니……! 이상성욕변태! 인격파탄자! 이제 만족하셨나요……!! 크흣…… 크히힛……"
    
    show stand_Kuka_mousou at movetoright ##어둡게
    show stand_Yuki_proud with dissolve ## 자뻑하는 모습
    
    ch_yuki "뭐야~ [name]. 오늘도 변함없이 귀여운 내 모습이 보고 싶어서 여기까지 왔구나? 이해해~ 내 미모는 매일매일 언제 봐도 질리지 않으니까. 하아…… 거울 속의 나…… 너무 귀여워……"

    ## 유키 어둡게
    hide stand_Kuka_mousou
    hide stand_Ninon
    hide stand_Yuki_proud

    ch_ayumi "히히…… 선배…… 오늘도 잘생겼어…… 히히……"

    ch_nar "예전부터 생각했던 거지만 여긴 제정신인 사람이 아무도 없는 것 같다."

    show stand_Monica with dissolve ##자신만만


    ch_monica "모두들, [name]가 반가운 마음은 이해한다만 밖에서 이럴 것이 아니라 어서 안으로 들지. 차라도 한 잔 마시면서 얘기하는 게 좋겠군."

    ## 무심한 표정으로 변경
    show stand_Monica_munen

    hide stand_Monica

    ch_monica "그…… 그리고 달콤한 과자도 조금…… 흠흠."

    hide stand_Monica_munen

    hide bg_town
    ## 길드 하우스 cg 페이드
    show bg_black onlayer background
    scene bg_guildhouse onlayer middle with fade
    show ob_ujitya onlayer forward with dissolve

    ch_ninon "쇼군! 이것은 마음을 안정시키는 동국의 3대 명차, 우지차라고 하는 것입니다!"

    hide ob_ujitya onlayer forward
    show stand_Ninon onlayer forward

    extend " 어서 들이켜 보세요 입니다!"

    hide stand_Ninon onlayer forward

    player "우지챠……"

    show stand_Kuka onlayer forward with dissolve ##기본 표정

    ch_kuka "그, 그러니까 도S씨는…… 정확히 무슨 일 때문에 오신 거죠?"
    ## 쿠우카 망상하는 표정
    show stand_Kuka_mousou onlayer forward
    hide stand_Kuka onlayer forward
    ch_kuka "설마…… 어둡고 구석진 골목에 마구잡이로 쿠우카를 밀어붙였던 그날…… 쿠우카가 아직까지도 그날의 쾌락을 잊지 못한 채 추잡스러운 행위를 계속하고 있는지 직접 확인하려고……?!"

    ch_kuka " 쿠, 쿠우카를 나락으로 빠뜨리기 위해 어디까지 계획을 세워 놓은 건가요?! 이…… 인륜배반자! 관음증 변태! 쿠, 쿠훗, 크흐흐……"

    hide stand_Kuka_mousou onlayer forward
    show stand_Monica onlayer forward with dissolve

    ch_monica "음! [name]를 이 자리에 호출한 건 다름이 아니라, 바이스플뤼겔의 향후 방향성과 마물 소탕 건에 대해 조언을 구하기 위해서다. 모두 한자리에 모였으니 드디어 이야기를 시작할 수 있겠군."

    hide stand_Monica onlayer forward

    ch_ayumi "역시 선배, 계획이 다 있으신 거군요……!"

    player "그런 거 없는데……"

    ch_ayumi "무계획이 계획인 거네요……! 역시!"

    show stand_Ninon_down onlayer forward with dissolve ## 시무룩한 표정

    ch_ninon "쇼군! 니논은 최선을 다했다 입니다! 하지만 마물이 너무너무 POWERFUL 했습니다……"

    ch_ninon "「인법 {font=NanumGothic.ttf}·{/font} 쇄우 병쉰 회오뤼감좌」를 정면으로 받아 내고 살아남은 자는 그 녀석이 처음이었다 입니다!"

    ## 니논 어둡게

    show stand_Monica_down onlayer forward at veryright with dissolve ## 시무룩한 표정

    ch_monica "‘그거, 뭔가 다른 이름이었던 것 같은데……’"

    hide stand_Ninon_down onlayer forward

    show stand_Monica onlayer forward at veryright
    hide stand_Monica_down onlayer forward
    $ renpy.pause(0.01)
    show stand_Monica onlayer forward at movetocenter

    ## 모니카 웃는 표정

    ch_monica "……걱정할 것 없다, 니논! [name]의 도움이 있다면 그보다 더 강한 놈들도 충분히 상대할 수 있게 될 거다."

    ch_monica "그러면, 우리의 문제가 어떤 것인지 말해 줄 수 있겠나?"

    hide stand_Monica onlayer forward
    show stand_Yuki onlayer forward with dissolve ##자신만만한 표정

    ch_yuki "이렇게나 귀여운 내가 있는데, 무슨 문제가 있다는 거야~? 복잡한 생각 하지 말고 예쁜 내 얼굴이나 감상하라구♪"

    hide stand_Yuki onlayer forward
    show stand_Monica_ddung onlayer forward with dissolve ## 화난 표정

    ch_monica "그렇게 건성으로 넘길 문제가 아니다! 귀공, 다시 한 번 정식으로 요청하도록 하지."

    ## 모니카 자신만만한 표정
    show stand_Monica onlayer forward
    hide stand_Monica_ddung onlayer forward

    ch_monica "‘바이스플뤼겔 랜드솔지부’가 나아갈 길을 제시해 주게! 귀공은 우리의 문제가 무엇이라고 생각하나?"

## 캐릭터 선택 분기 #########################
    menu:
        "어설픈 실력과 저돌적인 행동으로 쉽게 위험에 빠지는 것choice_1":
            $love_point = 1  ## 니논

        "동료를 신뢰하지 않고 독단적으로 행동하는 것choice_2":
            $love_point = 2  ## 모니카

        "순간의 욕망을 억제하지 못하고 충동적으로 행동하는 것choice_3":
            $love_point = 3  ## 쿠우카

        "자기 자신만을 중시하며 동료를 배려하지 않는 것choice_4":
            $love_point = 4 ## 유키
    hide bg_black onlayer background
    hide bg_guildhouse onlayer middle
    hide stand_Monica onlayer forward
    stop music
    jump scene19_2 ## 버그테스트 용

    show stand_Monica onlayer forward with dissolve ## 기본 표정

    ch_monica "음, 과연…… 귀공을 여기까지 데려온 보람이 있군. 훌륭한 통찰력이다."

    ch_monica "그렇다면 귀공이 지적한 대로, 우리의 문제점을 보완하는 것은 곧 바이스플뤼겔의 전력을 증강하는 길이라 봐도 무방할 터. 이제부터 그 방법을……"
    

    ## 잠깐 텀
    $renpy.pause(0.5)

    ## 니논 자신만만한 표정
    show stand_Ninon_wink onlayer forward
        
    ch_ninon "특훈만이 살 길이다!!!!!!!! 입니다!!!"
    
    ch_ninon "닌자가 강해지는 길은 오직 수련, 또 수련하는 것 뿐!! 천하통일을 위해서라면 그 어떤 지옥훈련이라도 견뎌낼 각오가 되어있소 입니다!!"

    hide stand_Ninon_wink onlayer forward with dissolve
    hide stand_Monica onlayer forward
    show stand_Monica_ddung onlayer forward at left
    show stand_Ninon onlayer forward at right

    ## 니논 기본표정, 어둡게/모니카 밝게
    ch_monica "흠, 흠!"

    ch_monica "……확실히 틀린 말은 아니다. 가혹한 훈련은 고통스럽지만 그만큼 효과적일 수 있지."

    ## 모니카 시무룩한 표정
    show stand_Monica_down onlayer forward at left
    hide stand_Monica_ddung onlayer forward

    ch_monica "하지만 니논, 훈련의 강도가 높은 것만이 능사는 아니야. 그건 우리가 누구보다도 뼈저리게 경험하지 않았나."

    ## 모니카 어둡게/니논 시무룩한 표정, 밝게
    hide stand_Ninon onlayer forward
    show stand_Ninon_down onlayer forward at right
    ch_ninon "과연…… 입니다. 그럼 니논은 무엇을 할 수 있다 입니까? 할복 입니까?"

    ## 니논 어둡게/ 모니카 밝게, 기본 표정
    ch_monica "그건……"

    ## 모니카 자신만만한 표정
    show stand_Monica onlayer forward at left
    hide stand_Monica_down onlayer forward
    ch_monica "우리의 새로운 해결사가 답을 알려 줄 거다!"

    ## 둘 다 어둡게

    ch_nar "갑자기 나한테 떠넘긴다고? 미쳤나?"
    ## 모���카 cg어둡게/니논 밝게, 니논 놀란 표정
    hide stand_Ninon_down onlayer forward
    show stand_Ninon_panic onlayer forward at right

    ch_ninon "우오옷~ 믿고 있었다고 쥐엔장~~!! 입니다!"

    player "아니…… 갑자기 그렇게 말해봤자……"

    hide stand_Monica onlayer forward
    hide stand_Ninon_panic onlayer forward
    show stand_Ninon_wink onlayer forward:
        xpos 640
        linear 0.3 ypos 0 xpos 350
    ch_ninon "DAIJOBU 입니다~! 왜냐하면 쇼군은~"
    hide stand_Ninon_wink onlayer forward
    hide bg_guildhouse onlayer middle
    show stand_Ninon_daiji onlayer forward
    $ camera_move(0, -1000, 400, 0, 6)

    scene bg_surf onlayer middle with dissolve

    play music "audio/main/4japan.mp3"

    ch_ninon "{font=NanumGothic.ttf}{b}……쇼군은…… 언제나 정도만을 걸어온 남자.{/b}{/font}"

    ch_ninon "{font=NanumGothic.ttf}{b}제아무뤼 겉으로는 언행이 아둔하고 이취에 맞지 않는 듯하여도, 쇼군이 인도하는 길의 끝에는 항시 광명이 우뤼를 비추고 있었소.{/b}{/font}"

    ch_ninon "{font=NanumGothic.ttf}{b}혹자는 쇼군의 우쥑한 성품을 비방할지도 모르오. 허나 그것은 툇마루 아래의 장사를 알아보지 못하는 붬인의 좁은 식견에 불과할 뿐.{/b}{/font}"

    ch_ninon "{font=NanumGothic.ttf}{b}일찍이 길이 존재했기에 걷는 것이 아니요, 쇼군의 족줙이 곧 길이라. 참된 쥐도자란 바로 그런 것이오.{/b}{/font}"

    ch_ninon "{font=NanumGothic.ttf}{b}설령 승리를 목줜에 두고 적에게 소금을 보눼어 되레 위난에 처하게 될지라도, 니논은 쇼군의 뜻을 따르겠소. 그것이 종국에는 우리를 줭토로 이끌리라 믿어 의심치 아니하기에……{/b}{/font}"

    ##빠르게 원래 크기로 복구
    $ camera_move(0, 0, 0, 0, 0.2)

    hide bg_black onlayer background
    hide bg_surf onlayer middle
    ## 길드하우스로 다시 변경
    scene bg_guildhouse
    play music "audio/main/3town.mp3"
    ## 니논 윙크하는 표정
    hide stand_Ninon_daiji onlayer forward
    show stand_Ninon_wink

    ch_ninon "……에~ 그러니까~ 부담 가질 필요 없다 입니다~!"

    ## 니논 어둡게/ 오른쪽에 모니카 시무룩한 표정

    show stand_Ninon_wink at movetoleft
    show stand_Monica_down at right

    ch_monica "미안하군. 아직 니논이 충격에서 벗어나지 못한 것 같아."

    player "괜찮아. 빼놓고 얘기하자!"

    ## 모니카 사라짐/ 니논 밝아지고 화면 중앙으로 이동, 시무룩한 표정
    hide stand_Monica_down
    hide stand_Ninon_wink
    show stand_Ninon_down at left:
        linear 0.3 ypos 0 xpos 500
    
    ch_ninon "HIDOI 입니다……"

    ## 니논 cg 어둡게

    hide stand_Ninon_down

    ch_ayumi "‘……멍청해 보인다는 말을 돌려서 얘기한 건 못 알아채신 걸까, 선배……’"

    ch_nar "그나저나 큰일이군……"

    ch_nar "있어 보이려고 아무 말이나 지껄인 건데 뒷수습을 못 하겠어……"

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
    ch_nar "그런데 잠깐, 방금……"

    hide stand_Ninon_innocence
    hide stand_Yuki_ddung

    player "……땀 흘리는 일이라……"
    
    show stand_Kuka with dissolve ## 기본 표정
    ch_kuka "도…… 도S씨가 뭔가 생각에 잠겼어요……!"

    ## 쿠우카 망상하는 표정
    show stand_Kuka_mousou
    hide stand_Kuka

    extend " 어, 어떻게 하면 쿠우카를 더 수치스럽게 능욕할 수 있을지 머리를 쥐어짜내고 있는 게 분명해요!!"

    ch_kuka "아아, 그, 그치만…… 얼마나 심한 짓을 당할지 가늠조차 하지 못하면서, 아니 어쩌면 누구보다도 잘 알고 있으면서!! 무구하고 앳된 소녀의 마음은, 불나방과 같이 그 순결함을 제발로 불사르려는 충동을 떨쳐내지 못하고……!!! 이 얼마나 잔혹하고 달콤한 유혹인가…… 크히, 크히힛…… 쿠후후후훗……"
    
    hide stand_Kuka_mousou

    ch_ayumi "음, 선배…… 쿠우카 씨가 하는 말은 일단 모르는 척하는 게 좋을 것 같아요……"

    show stand_Kuka_mousou with dissolve

    ch_kuka "히이……♥ 아유미 씨에게 무시당하는 감각……! 이건 굉장히 귀하네요…… 크큭…… 여기서 더 떨어질 바닥이 있을까……"

    hide stand_Kuka_mousou

    ch_ayumi "그…… 그건 무슨 의미인가요오!!!!"
 
    show stand_Yuki_proud with dissolve ## 자뻑하는 표정

    ch_yuki "참, [name]. 오해는 하지 마? 내 미모는 얼마나 밝은 곳에 있든 간에 빛이 나고, 어두운 곳에 있으면 더욱 돋보이는 범우주적 매력을 갖고 있으니까, 장소는 아무래도 상관없어~"

    ch_yuki "그치만 기왕 뭔가를 할 거라면, 나의 아름다움에 공헌할 수 있는 걸 하는 게 세상에 더 도움이 될 거라구. 내가 예뻐질수록 세계는 한층 더 아름다워질 테니까~"

    ## 유키 웃는 표정
    show stand_Yuki
    hide stand_Yuki_proud

    ch_yuki "예를 들면~ 응, 피부 미용에 좋은 거라든지?"

    ## 유키 어두워지고 화면 오른쪽/ 모니카 시무룩한 표정 왼쪽

    show stand_Yuki at movetoright
    show stand_Monica_down at left

    ch_monica "……그대는 어째서 그렇게까지 피부에 집착하는 건가……"

    ## 모니카 어두워지고 유키 밝아짐

    ch_yuki "음~ 예쁜 얼굴은 타고나는 거라 해도, 피부는 꾸준히 잘 관리해 줘야 한다구. 이참에 모니카 씨도 신경 좀 써 보는 건 어때? 충분히 귀여운 얼굴인데, 아깝잖아~ 뭐, 나만큼은 아니지만."

    ## 유키 어두워지고 모니카 부끄러워하는 표정 밝아짐
    show stand_Monica_dere at left
    hide stand_Monica_down

    ch_monica "누…… 누가 귀엽다는 거냐!"

    ## 모니카 시무룩한 표정
    show stand_Monica_down at left
    hide stand_Monica_dere

    extend " ……애초에 나는 군인이다. 그런 것에 신경 쓸 여유는……"

    player "……생각났어."

    ## 유키 사라짐/ 모니카 놀란 표정, 화면중앙
    hide stand_Yuki
    show stand_Monica_down at movetocenter
    show stand_Monica_surprised
    hide stand_Monica_down

    ch_monica "귀공……? 아아, 특훈에 관한 것 말인가! 허심탄회하게 얘기해 보게!"

    hide stand_Monica_surprised

    player "특훈을 하면…… 땀이 나."

    ## 모니카 시무룩한 표정
    show stand_Monica_down with dissolve

    ch_monica "……?"

    hide stand_Monica_down

    player "땀이 난다는 것은 힘이 든다는 것입니다."

    ch_ayumi "??"

    player "힘이 들면, 피부에 좋지 않습니다. 그렇기 때문에 나는 생각합니다. 피부에 좋지 않으면, 땀이 나는 것이 아닌가 하고."

    show stand_Kuka_mousou with dissolve ## 쿠우카 망상하는 표정
    ch_kuka "뇌가 겁탈당하고 있어요……!!"

    hide stand_Kuka_mousou

    player "하지만 온천이라면 어떨까?"
    
    show bg_guildhouse onlayer middle

    show stand_Yuki_surp onlayer forward at left ## 유키 놀라는 표정, 밝게
    
    show stand_Ninon_surprise onlayer forward at right ## 니논 놀라는 표정, 어둡게
    
    $ camera_move(-2300, -1500, 800, 0, 0.7)

    ch_yuki "온!" ## 유키 줌 인

    $ camera_move(0, 0, 0, 0, 0)
    $ camera_move(2500, -1800, 800, 0, 0.7)
    
    ch_ninon "천!" ## 니논 줌 인
    $ camera_move(0, 0, 0, 0, 0)

    hide stand_Yuki_surp onlayer forward
    hide stand_Ninon_surprise onlayer forward
    hide bg_guildhouse onlayer middle

    show stand_Monica_down with dissolve ## 시무룩한 표정

    ch_monica "다…… 좋은데, 온천이 특훈과 무슨 관계가 있는 건가……?"

    hide stand_Monica_down

    show stand_Ninon with dissolve

    ch_ninon "후, 아직 멀었군요 입니다, 모니카 씨!"

    ch_ninon "분명 조금 전 쇼군이 지적한 문제는, 요컨대 TEAMWORK가 부족하다는 사실!"

    ch_ninon "우리가 충분히 강하다는 것은 모니카 씨도 인정하셨다 입니다."

    show stand_Ninon_daiji
    hide stand_Ninon

    ch_ninon "그렇다면 우리에게 남은 과제는 바로 「단합」!!"

    ch_ninon "지금까지 니논은 단순무쉭한 수련법만을 고집해왔소 입니다. 하지만 쇼군은! 그보다 한 차원 높은! 격이 다른 강함을 추구하는 것입니다!! 길드 합숙을 통한 유대감 증진, 그리고 이어지는 UNION BURST!!!"

    ch_ninon "동시에 「온천」이라는 명답을 제시하여! 피부를 염려하는 유키 씨의 불만까지 해치워 버린 것이다 입니다!!"

    show stand_Ninon_wink
    hide stand_Ninon_daiji

    ch_ninon "역시 쇼군, 실로 지혜로운 판단이 아닐 수 없소 입니다!! 존경하오 입니다~!"

    ## 니논 어둡게

    show stand_Monica_surprised at veryleft ## 모니카 놀란 표정

    ch_monica "오오……! 그런 것이었나! 나도 아직 한참 부족하군……!!"

    ## 모니카 어둡게

    show stand_Yuki at right ## 유키 웃는 표정

    ch_yuki "뭐~ 그런 이유라면 어울려 주지 못할 것도 없긴 해~ 이런 것까지 신경써 주다니, 꽤나 섬세하잖아?"

    hide stand_Monica_surprised
    hide stand_Ninon_wink
    hide stand_Yuki

    ch_nar "……뭐지?"

    ch_nar "콧코로한테 온천 여행 가자고 했다가 주인님은 염치도 없냐고 한소리 들었던 게 생각나서 막 던져 본 건데……"

    ch_nar "역시…… 이 정도로 잘생겼으니 무슨 말을 해도 먹히는 건가. 이런 이런……"

    ch_nar "못생겼다는 건 대체 어떤 기분일까……? 하루만 못생겨 봤으면 좋겠다."

    ch_nar "앗, 나도 참. 말도 안 되는 소릴. 하하하."

    ## 니논, 모니카, 유키 cg 어둡게

    show stand_Kuka with dissolve ## 쿠우카 기본 표정

    ch_kuka "그……러면, 온천에 가서는 구체적으로 어떤 일을 하게 되나요……?"

    ## 쿠우카 망상하는 표정
    show stand_Kuka_mousou
    hide stand_Kuka

    ch_kuka "여, 역시 혼욕을 노리시는 건가요?! 모두가 지켜보는 가운데 쿠우카의 치부를 억지로 드러내 보이게 하려는 속셈인 거네요!!! 치욕감에 정신을 차리지 못하는 쿠우카의 주변을 수많은 남성들이 에워싸고선…… 으헤헷…… 쿠헤헤헤헷……"

    hide stand_Kuka_mousou

    ch_ayumi "호……호호흐호, 혼, 혼욕?! 서, 스, 서, 선배와 함께?!!?"

    show stand_Monica_ddung with dissolve ## 뚱한 표정 

    ch_monica "……그대들이 뭘 상상하는 건지 잘은 모르겠다만……"

    ch_monica "최소한 건전한 속내가 아니라는 것만은 분명해 보이는군……"

    ## 모니카 웃는 표정
    show stand_Monica
    hide stand_Monica_ddung

    ch_monica "그건 그렇다 치고, 귀공."

    ch_monica "먼저 온천이라는 장소를 언급한 만큼 따로 생각해 둔 곳이 있는 거겠지? 우리는 전적으로 귀공의 계획에 따르겠네."

    hide stand_Monica
    
    player "뎃?"

    show stand_Ninon_wink with dissolve

    ch_ninon "장소라면 걱정 맛세이 입니다! 전부 니논에게 맡기는 겁니다~!"

    show stand_Ninon
    hide stand_Ninon_wink
     ## 니논 웃는 표정

    ch_ninon "지난번 마물 토벌 이후, 아직까지도 오에도 여러분의 열화와 같은 INVITATION이 끊이질 않고 있는데……"

    show stand_Ninon_down
    hide stand_Ninon
     ## 니논 시무룩한 표정

    ch_ninon "여기 이중에…… 어…… 어디 있냐 입니다……?"

    hide stand_Ninon_down
    show stand_Ninon ## 니논 웃는 표정

    extend " 앗, 발견 입니다."

    ch_ninon "오에도 사상 최고 이빠이로 큰 대형 온천의 초대장도 잔뜩 왔다 입니다~!"

    ch_ninon "그러면~ 가장 마지막에 온 초대장을 개봉해 보도록 하겠습니다~~!! 두구두구두구……"

    hide stand_Ninon
    show stand_Ninon_surprise ## 니논 놀란 표정

    ch_ninon "………………"

    ch_ninon "………………………………"

    hide stand_Ninon_surprise
    show stand_Yuki_angry ## 유키 화난 표정

    ch_yuki "~~~아, 정말! 답답하게 뭐하는 거야? 안 읽어 줄 거면 차라리……"

    ## 유키 부끄러워하는 표정
    show stand_Yuki_shamed
    hide stand_Yuki_angry

    extend "앗…… 화내는 얼굴도 어쩜 이렇게 새침하고 귀여울 수가…… 세상에…… 거울에서 눈을 뗄 수가…"

    hide stand_Yuki_shamed
    show stand_Monica_ddung ## 모니카 화난 표정

    ch_monica "둘 다 뭘 하고 있는 건가, 대체?! 니논, 편지를 이리로 넘겨라!"

    hide stand_Monica_ddung
    show stand_Ninon_surprise ## 니논 놀란 표정

    ch_ninon "……모니카 씨……? 이거……"

    hide stand_Ninon_surprise
    show stand_Monica_ddung ## 모니카 화난 표정

    ch_monica "대관절 무슨……"

    ## 모니카 놀란 표정
    show stand_Monica_surprised
    hide stand_Monica_ddung

    ch_monica "……"

    ## 모니카 화난 표정
    show stand_Monica_ddung
    hide stand_Monica_surprised

    ch_monica "……귀공."

    ch_monica "아무래도……"

    ch_monica "……온천에 가야만 하는 이유가 생긴 것 같다."

    ## 화면 중앙에 피로 휘갈겨 쓴 편지 이미지 show blood_letter
    $ persistent.clues_letter = True
    show ob_tegami with dissolve:
        xpos 430 yalign 0.3
    stop music fadeout 1.0
    
    play sound "audio/sound/surp.mp3"

    ch_nar "{color=#FF2929}「도와주세요」{/color}"

    ## 대화창 사라짐

    ## 피로 휘갈겨 쓴 편지 이미지, 길드하우스 cg F.O
    hide ob_tegami
    hide stand_Monica_ddung ##(모니카 화난 표정)
    hide bg_guildhouse

    jump black_haikei

## S# 4.검은 배경 라벨 ################################
label black_haikei:
    $renpy.pause(1.5)
    scene bg_black

    ch_peco "안뇽~☆ [name]! 서프라이즈예요~! 짜잔~~!!"

    ch_peco "……어라? 아무도 없는 건가요? 저~~기요~~~!! [name]~~!! 누구 없나요오~~?"

    ch_kyaru "……뭐야. 코로스케도 없고, 배고파할 것 같아서 급하게 왔더니만…… 어딜 간 거야?"

    ch_kyaru "나가서 찾아 봐야 하나…… 귀찮게 하긴."

    ch_peco "어머? 맨날 돼지니, 죽여버리니 하면서도 은근히 챙겨주려고 하네요~ 이게 바로 츤데레……라고 하는 그런 건가요? 귀여워라~☆ 착하지, 착하지……"

    ch_kyaru "여…… 역겨운 소리 하지 마! 머리도 쓰다듬지 마! 죽여버린다!!"

    ch_kyaru "……딱히 챙겨주려는 게 아니라…… 그, 그녀석한테 무슨 일이라도 생기면 코로스케도 슬퍼할 거고!"

    ch_peco "네에~ 무슨 마음인지 다 이해한답니다~"

    ch_peco "……그나저나 조금…… 쓸쓸하네요."

    ch_peco "따라오면 위험할 것 같아서 일부러 모질게 말한 건데…… 상처 받았으려나요……"

    ch_peco "미식전은 모두와 함께 맛있는 음식을 먹으며 웃고 떠드는 길드인데…… 어디로 가버린 걸까요, 그 사람……"

    ch_kyaru "뭔가 말했어, 바보린느?"

    ch_peco "아아~ 아무것도 아니에요~"

    ch_peco "……정말 아무것도, 아니에요……"

    ch_kyaru "……걱정 끼치긴, 바보가……"

    jump onsen

## S# 5. 노천탕, 길드하우스 #################
label onsen:
    scene bg_onsen with fade
    ## 노천탕 cg 
    play music "audio/main/5orientalcommon.mp3"

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

    player "{font=NanumGothic.ttf}—{/font} 콧물 나온다으…… 후루룹……"

    player "짭짤하당. 히히."

    ## 노천탕 cg 내리기
    hide bg_onsen
    stop music fadeout 1.0

    ## 까만 배경
    scene bg_black ## 까만 배경에 대화창만 팝업

    ch_nar "하루 전……"

    ## 심각한 브금 서서히 커지면서 들어오기
    play music "audio/main/emer.mp3" fadein 1.0
    hide bg_black
    scene bg_guildhouse

    player "흐억……!!"

    player "뭐, 뭐야 이거?! 혈서?!"

    ## 피로 휘갈겨 쓴 편지 이미지 show blood_letter with dissolve
    show ob_tegami with dissolve:
        xpos 430 yalign 0.3

    ch_nar "형형색색의 꽃무늬로 화려하게 장식된 동양풍의 겉봉 속, 편지지의 새하얀 빛깔과 대비되는 검붉은 선혈이 마구잡이로 흩뿌려져 있다."

    ch_nar "벌건 가닥의 틈으로 무질서하게 엉겨 붙어 있는 덩어리들은 본연의 형태를 잃지 않으려 애쓰며 자신의 존재를 관철한다."

    ch_nar "살려 달라고 외치는 듯한 문자의 나열은 꺼림칙한 정도를 넘어 기괴한 분위기까지 자아낸다……"

    hide ob_tegami
    
    player "……“도와주세요” 라니…… 온천 초대장이 아니었어? 누가 장난친 건가?"

    show stand_Ninon_down with dissolve

    ch_ninon "아니…… 장난은 아닌 것 같소 입니다. 뒷면을 보십시오 쇼군."
    
    hide stand_Ninon_down

    ch_nar "완성되지 못한 문장들이 짤막하게 휘갈겨 쓰여 있다."

    ch_nar "알아보기 힘든 글씨체…… 편지가 쓰였을 당시의 상황이 매우 긴박했다는 것을 암시하는 듯하다."

    show ob_tegami with dissolve:
        xpos 430 yalign 0.3

    ch_nar "{color=#FF2929}마 물이 숨 어 드ㄹ었 다{/color}"

    ch_nar "{color=#FF2929}우 리 중 ㄴㅜ 군가{/color}"

    ch_nar "{color=#FF2929}사람 , 이 사라 진{/color}"

    ch_nar "{color=#FF2929}하 ㄹㅜ에 하 나씩{/color}"

    ch_nar "{color=#FF2929}그거ㅅ에 게 들 키면{/color}"

    ch_nar "{color=#FF2929}죽 을ㅁ{/color}"

    ch_nar "{color=#FF2929}입구에서 구라노스케를 찾아주세요.{/color}"

    hide ob_tegami

    player "잘 나가다가 이 삐끼 같은 마무리는 뭐야."

    ## hide blood_letter with dissolve

    show stand_Kuka_surprised with dissolve ## 쿠우카 놀란 표정

    ch_kuka "저…… 정말 피로 쓴 글씨인가요……?! 히이이……"

    hide stand_Kuka_surprised
    show stand_Monica_down with dissolve ## 모니카 화난 표정

    ch_monica "이렇게 곳곳에 흩뿌려져 있는 형태는 인위적으로 연출했다고 보긴 어려워."

    ch_monica "모종의 이유로 피를 흘리면서까지 편지를 쓸 수밖에 없었던 상황이었을지도……"

    hide stand_Monica_down
    show stand_Yuki_ddung with dissolve ## 유키 뚱한 표정

    ch_yuki "잠깐, 너무 진지하게 받아들이는 거 아니야? 저 빨간 자국이 진짜 피가 맞다 쳐도, 이상한 점이 한두 개가 아니잖아."

    hide stand_Yuki_ddung
    show stand_Ninon_surprise with dissolve

    ch_ninon "……! 그건 그렇다 입니다. 저렇게 글자를 날려쓸 정도로 일촉즉발의 상황이었다면…… 편지를 보낼 틈도 없었을 터 입니다."

    hide stand_Ninon_surprise

    ch_ayumi "마지막 힘을 짜내어 써 놓은 편지를…… 다른 누군가가 발견해서 여기로 몰래 보내 준 것 아닐까요……? 우으…… 제가 말하면서도 무서워요……"

    show stand_Monica_down with dissolve ## 모니카 화난 표정

    ch_monica "뭐…… 자세한 내막은 직접 가서 알아내면 될 뿐이다. 편지의 마지막에 언급된 ‘구라노스케’라는 인물에 대해서도 석연치 않은 부분이 많고……"

    ch_monica "……귀공은 어떻게 할 텐가? 위험할 수도 있는 일이다. 이건 우리가 해결해야 할 문제고, ‘바이스플뤼겔 랜드솔지부’에 소속되지 않은 귀공이 우리와 함께해야 할 의무는 없어."

    show stand_Monica_down at movetoleft ## 모니카 화난 표정
    show stand_Ninon at right ## 니논 웃는 표정

    ch_ninon "니논도 동의하오 입니다. 비록 쇼군과 떨어지게 되는 것은 애통하나, 쇼군이 다치는 것은 그 무엇과도 비교할 수 없는 비극 입니다!"
    
    player "……"

    hide stand_Monica_down
    hide stand_Ninon

    ch_nar "이 녀석들과 함께 가지 않으면…… 미식전으로 돌아가는 수밖에 없겠지."

    ch_nar "그런데 돌아간다고 해 봤자……"

    ch_nar "나를 약골에 머저리 취급하는 것들만 있는 데다, 유일하게 내 편이었던 마망도 이제는 없다."

    ch_nar "조금 멍청하긴 해도…… 이 녀석들은 내가 무슨 말을 하든 편들어주고, 귀 기울여 주는데,"

    ch_nar "차라리 여기에 있는 게 낫지 않을까?"

    play music "audio/main/3town.mp3" fadein 1.0

    player "……저기, 물어볼 게 있는데."

## 선택지 ##########################################
    menu:
        "니논에게 의견을 묻는다.choice_1":
            if love_point == 1:
                $point_ninon += 1
            elif love_point != 1:
                $point_ninon = 0
            
            player "니논은 내가 어떻게 했으면 좋겠어?"

            show stand_Ninon_surprise ## 니논 매우 놀란 표정

            ch_ninon "니, 니논에게 질문하셨나이까 입니다?!"

            hide stand_Ninon_surprise
            show stand_Ninon_embarassed ## 니논 당황한 표정

            ch_ninon "에……"

            hide stand_Ninon_embarassed
            show stand_Ninon_down ## 니논 시무룩한 표정

            ch_ninon "……쇼군을 보퓔하는 신하로서, 쇼군의 안녕을 최우선으로 여기는 것이 쥐당하오나……"

            hide stand_Ninon_down
            show stand_Ninon_embarassed ## 니논 당황한 표정

            ch_ninon "마음 속 깊은 곳에서는…… 쇼군이 니논들을 이끌어 달라고 외치고 있소 입니다……!!"

            hide stand_Ninon_embarassed
            show stand_Ninon_innocence ## 니논 억울한 표정

            ch_ninon "송구하기 그쥐없사옵니다, 쇼군!!! 니논은 기꺼이 할복할 것입니다!!"

            player "아니…… 할복은 안 해도 되니까……"

            player "아무튼, 니논이 그렇게까지 말한다면……"

            player "같이 갈까, 온천."

            hide stand_Ninon_innocence

            pass

        "       모니카에게 의견을 묻는다.choice_2":
            if love_point == 2:
                $point_monica += 1
            elif love_point != 2:
                $point_monica = 0
            
            player "모니카는 내가 어떻게 했으면 좋겠어?"

            show stand_Monica_surprised with dissolve ## 모니카 놀란 표정

            ch_monica "……내 의견을 묻는 건가?"

            ch_monica "뭐어…… 위험할 것이라 경고하기도 했고, 귀공이 관여할 필요가 없는 일인 것도 사실이지만……"
            
            show stand_Monica
            hide stand_Monica_surprised
             ## 모니카 웃는 표정

            ch_monica "개인적인 바람으로는, 우리와 동행해 주었으면 한다."

            ch_monica "염치 없는 부탁인 것은 알고 있네."

            ch_nar "뭐?! 알고 있었다고?!"

            ch_monica "하지만…… 뭐랄까, 귀공과 함께라면 무슨 일이든 잘 풀릴 것만 같은 느낌이 들어. 단지 그뿐이다."

            show stand_Monica_munen ## 모니카 당황한 표정
            hide stand_Monica

            ch_monica "아, 오해는 말아 다오! 의견을 물었기에 진솔하게 대답한 것일 뿐이다."

            ch_monica "몇 번이고 말하지만, 절대로 강요하지 않아. 귀공의 판단을 존중하겠네."

            player "……그런가."

            player "그럼…… 같이 가지 뭐. 나도 싫지 않아."

            hide stand_Monica_munen

            pass
        "다시 생각해 보니 이것들 의견은 별로 중요하지 않은 것 같다.choice_3":
            if love_point == 1:
                $point_ninon -= 1
            elif love_point == 2:
                $point_monica -= 1
            elif love_point == 3:
                $point_kuka -= 1
            elif love_point == 4:
                $point_yuki -= 1
            
            player "아니…… 아무것도 아니야."

            player "기왕 도와주기로 했는데, 갑자기 빠지는 것도 좀 이상하잖아? 같이 가자."

            pass

        "쿠우카에게 의견을 묻는다.choice_5":
            if love_point == 3:
                $point_kuka += 1
            elif love_point != 3:
                $point_kuka = 0

            player "쿠우카는 내가 어떻게 했으면 좋겠어?"

            show stand_Kuka_surprised with dissolve ## 쿠우카 부끄러워하는 표정

            ch_kuka "엣? 에?! 쿠, 쿠우카 말인가요?!"

            ## 쿠우카 부끄러워하는 표정으로 변경
            show stand_Kuka_shamed
            hide stand_Kuka_surprised

            ch_kuka "아, 아뇨, 그…… 저기, 너무 갑작스럽게 물어보셔서……"

            ch_kuka "쿠…… 쿠우카는…………"

            ## 쿠우카 망상하는 표정으로 변경
            show stand_Kuka_mousou
            hide stand_Kuka_shamed

            ch_kuka "여, 역시 안돼!! 쿠우카를 곧 버릴 물건처럼 심하게 다루어 주셨으면 좋겠다고 말하는 건 역시 무리……!! 그, 그렇군요. 그런 것이었군요! 일부러 쿠우카가 모두의 앞에서 파렴치한 말을 하도록 유도하고, 주변에서 쏟아지는 경멸의 눈빛을 버티지 못해 주저앉은 쿠우카를 들…"

            player "따라오지 말라는 거지?"

            ## 쿠우카 대사 글꼴 크기 크게 + 굵게

            ch_kuka "{size=+ 10}{b}같이 가주세요옷!!!!!!!!{/b}{/size}"

            player "처음부터 그랬으면 됐잖아……"

            player "아무튼…… 그래."

            player "같이 가자, 온천."

            hide stand_Kuka_mousou

            pass
        
        "유키에게 의견을 묻는다.choice_6":
            if love_point == 4:
                $point_yuki += 1
            elif love_point != 4:
                $point_yuki = 0

            player "유키는 내가 어떻게 했으면 좋겠어?"

            show stand_Yuki with dissolve ## 웃는 표정

            ch_yuki "응? 나 말이야?"

            ## 유키 자뻑하는 표정
            hide stand_Yuki
            show stand_Yuki_proud 

            ch_yuki "……흐흥♪"

            ## 유키 질색하는 표정
            hide stand_Yuki_proud
            show stand_Yuki_angry 

            ch_yuki "너 같은 건 안 따라왔으면 좋겠는데?"

            player "어?"

            ## 유키 자뻑하는 표정
            hide stand_Yuki_angry
            show stand_Yuki_proud 

            ch_yuki "……라고 하면, 정말로 안 따라올 거야?"

            player "……어…… 그게……"

            ch_yuki "농담이야~ 나랑 떨어지는 게 그렇게까지 싫었어?"

            ch_yuki "표정으로 다 드러난다구. 귀엽네~"

            ## 유키 웃는 표정
            hide stand_Yuki_proud
            show stand_Yuki 

            ch_yuki "네가 함께 가는 거라면, 난 찬성이야."

            ch_yuki "온천이니까…… 평소보다 조금 더 대담한 모습을 보여 줄 수 있겠네?"

            ## 유키 자뻑하는 표정
            hide stand_Yuki
            show stand_Yuki_proud 

            ch_yuki "꺄~ 부끄러워~"

            ch_nar "전혀 부끄러워하는 표정이 아니잖아……"

            player "대담한 모습인지 뭔지는 모르겠고…… 아무튼 같이 가자는 뜻으로 받아들이면 되는 거지?"

            player "같이 가자, 온천."

            hide stand_Yuki_proud

            pass


        
    show stand_Ninon_panic with dissolve ## 니논 놀란 표정

    ch_ninon "니논은 기쁩뉘다만……, 쇼군은 정말 괜찮으신가요 입니다……?"

    hide stand_Ninon_panic

    ch_ayumi "마, 맞아요……! 선배가 위험해지는 건 싫어……!"

    ch_ayumi "……굳이 따라오지 않으셔도 저는 24시간 내내 언제나 선배의 모습을 감상할 수 있는데…… 아, 그래도 온천이라면 유카타 차림의 선배를…… 아니, 아니지, 유카타가 문제가 아니네요…… {cps=*0.8}탕속에들어가신다면수건한장만걸치고있는선배가,거기다운이좋으면수건마저풀어헤친평소에는볼수없었던고혹적인선배의또다른은밀한모습을{/cps}"
        
    show stand_Kuka_hiku with dissolve ## 질색하는 표정

    ch_kuka "아유미 씨…… 아무리 그래도 그건 범죄라고 생각해요……"

    ch_nar "진짜 세계관 최강자들의 싸움이다……"

    hide stand_Kuka_hiku

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
    show stand_Kuka_mousou at left ## 쿠우카 망상하는 표정

    ch_kuka "겨, 결국 가는 건가요…… 가 버리는 건가요오……!!"

    ## 쿠우카 어둡게
    show stand_Yuki_proud with dissolve ## 유키 자뻑하는 표정

    ch_yuki "어떤 옷을 입어도 아름다운 내가 유카타를 입은 모습…… 수건 한 장으로는 감히 숨길 수 없는 미의 결정체. 그 고귀한 모습이 비쳐 흐르는, 한 폭의 그림 같은 노천탕…… 하아…… 너무 기대돼……"

    ## 유키 어둡게

    ch_ayumi "{cps=*0.8}선배가들어갈때아무도눈치채지못하게따라들어가서옷을갈아입는장면을두눈에새길수있고온천에들어가기위해수건을두르는순간도놓치지않는다면귀중한광경을두번이나볼수있는데다숙소로돌아오기위해탈의실에다시들어가는것까지카운트하면평소에절대보지못했던선배의모습을적어도네번이상{/cps}"

    ch_nar "이것들한테 진지한 걸 기대한 내가 잘못했다."

    hide stand_Kuka_mousou
    hide stand_Yuki_proud
    show stand_Ninon at movetocenter

    ch_ninon "아, 그리고 모니카 씨{font=NanumGothic.ttf}—{/font}"

    ch_ninon "니논의 『시크릿 {font=NanumGothic.ttf}·{/font} 닌닌 정보망』에 따르면, 온천 내부의 매점에서 다양한 별미를 판매한다고 합니다."

    show stand_Ninon_wink
    hide stand_Ninon
    ## 니논 윙크하는 표정

    ch_ninon "무엇보다 오에도 온천에서만 맛볼 수 있는 한정판 간식이 있다고 하네요 입니다~!"

    ## 니논 어둡게
    show stand_Monica_surprised at veryleft ## 모니카 놀란 표정

    ch_monica "뭣, 뭐라고?! 간식이라면 과자도 있다는 말인가?!"

    ch_nar "모니카 너마저……"

    ch_nar "음…… 그래도 너무 축 처지는 분위기보다는 나은가……"

    ch_nar "그래, 편하게 놀러 가는 거라고 생각하자."

    ch_nar "별일이야 있겠어?"

    hide stand_Ninon_wink
    hide stand_Monica_surprised
    hide bg_guildhouse
    stop music fadeout 3.0

    jump onsen_inside
## S# 6. 온천 건물 내부 #####################
label onsen_inside:
    show bg_black onlayer background
    scene bg_onsen onlayer middle with fade ## 온천내부 cg 빠르게
    show stand_gura onlayer forward with dissolve## 빠르게

    $ renpy.pause(1.5)

    
    play sound "audio/sound/surp.mp3"

    ## 빠르게 화면전체가 돌아가는 효과
    show bg_onsen onlayer middle at fast_rotating_2

    play music "audio/main/11fun.mp3"

    hatena "오에도 온천에 어서옵쇼오{font=NanumGothic.ttf}————{/font}옷!!!!!!!!!!!!!!!"
    hide stand_gura

    player "으아아아악!!!!"

    ## 빠르게 화면 한 바퀴
    show bg_onsen onlayer middle at fast_rotating
    show stand_gura onlayer forward with dissolve

    hatena "입장은 몇 분임까아{font=NanumGothic.ttf}———{/font}앗!!!!!!!!!!!!!!!!"
    hide stand_gura onlayer forward
    
    show stand_Monica onlayer forward ## 모니카 화난 표정

    ch_monica "아아, 다섯 명으로 부탁하지."

    ## 모니카 어둡게
    hide stand_Monica onlayer forward

    ch_ayumi "엣? 여…… 여섯 명 아닌가요……?"

    ## 모니카 놀란 표정
    show stand_Monica_surprised onlayer forward with dissolve

    ch_monica "이런, 아유미의 존재를 깜빡 잊고 있었다…… 미안하군. 모습이 보이지 않아서 무심코……"

    ## 모니카 어둡게
    hide stand_Monica_surprised onlayer forward

    ch_ayumi "차…… 차라리 존재감이 없다고 해 주세요……! 모습이 안 보인다는 말은 좀 너무하잖아요……!!"

    player "아니 과장이 아니라 진짜로 안 보이는데……"

    show stand_gura onlayer forward with dissolve

    player "그, 그보다 다들, 이 녀석 생김새를 보고도 아무렇지 않은 거야?! 이건 사람이라기보다……"

    show stand_Monica_ddung onlayer forward at veryleft ## 모니카 화난 표정

    ch_monica "귀공…… 사람을 외모로 판단하는 건 나쁜 버릇이다."

    hide stand_Monica_ddung onlayer forward

    player "외모고 뭐고 사람의 형상이 아니잖……"

    show stand_Yuki_ddung onlayer forward at right with dissolve ## 유키 뚱한 표정 오른쪽

    ch_yuki "맞아~ 얼른 사과해. 그 누구보다 아름다운 나조차도 남의 외모를 함부로 깎아내리진 않는다구."
    hide stand_Yuki_ddung onlayer forward
    hide stand_gura onlayer forward
    hide bg_onsen onlayer middle
    ## 길드하우스 cg + 유키 회색으로

    show kaisou_guildhouse onlayer forward with dissolve

    ch_yuki "“……엄청나게 못생긴 마물……”"

    show kaisou_field onlayer forward with dissolve
    hide kaisou_guildhouse onlayer forward

    ch_yuki "“세상에…… 대체 뭘 먹고 자라면 저렇게 못생겨지는 거지……?! 윽…… 역겨워……”"

    show kaisou_town onlayer forward with dissolve
    hide kaisou_field onlayer forward

    ch_yuki "“아아- 못생긴 녀석들은 얼굴만 봐도 토할 것 같단 말이지- 얼른 죽어 주지 않으려나-”"

    show bg_onsen
    hide kaisou_town onlayer forward
    hide bg_black onlayer background
    

    show stand_gura with dissolve

    hatena "……홋홋홋. 괜찮습니다. 이런 건 이미 익숙하거든요……"

    hide stand_gura
    show bg_black with fade
    hide bg_onsen
    play music "audio/main/10end.mp3"

    ## 구라노스케 cg 합성
    show cg_gura_baby at center_center with dissolve

    hatena "저는…… 태어날 때부터 이런 흉측한 모습이었답니다."

    player "뭔데?! 이놈은 뭔데 회상씬까지 있는 건데?!"

    hide cg_gura_baby
    ## 구라노스케 cg 합성: 울고 있는 학동 위치에 합성
    show cg_gura_child with dissolve

    player "우와, 아까부터 합성 성의 없어……"

    show movie
    play movie "library/cg_gura_child.mpg" noloop

    hatena "당연히 이런 저를 받아 주는 사람이 있을 리 없었고……"

    hatena "단지 이렇게 생겼다는 이유 하나만으로 괴물이라 놀림 받으며, 심한 괴롭힘을 당하는 나날들이 계속되었지요……"

    stop movie
    hide movie
    hide cg_gura_child
    show bg_naibu with fade

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

    play music "audio/main/11fun.mp3"

    show stand_gura with dissolve

    hatena "잡설은 이쯤 하고{font=NanumGothic.ttf}——{/font}"

    show bg_naibu at fast_rotating

    hatena "정식으로 자기소개를 하겠슴다아{font=NanumGothic.ttf}———{/font}앗!!!!!!"

    ch_gura "제 이름은 구라노스케!!!! 쇼군 여러분!!!!! 모시게 되어 영광임다아{font=NanumGothic.ttf}———{/font}앗!!!!!!"

    hide stand_gura

    ## 모니카 놀란 표정
    show stand_Monica_surprised with dissolve

    ch_monica "뭐…… 이 자가 편지에 적혀 있던 바로 그……!"

    hide stand_Monica_surprised
    show stand_gura with dissolve

    ch_gura "그렇습니다!!!! 당신들에게 편지를 보낸 건 바로 저였슴다아{font=NanumGothic.ttf}———{/font}앗!!!!"

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
    hide bg_naibu with fade
    hide bg_black
    jump routen
## S# 7. 노천탕 ############################
label routen:

    play music "audio/main/emer.mp3"
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

    ch_ayumi "힉……"

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

    ch_gura "여러분에게 그 편지를 보낸 것은 제가 맞습니다만…… 편지를 쓴 것은 제가 아닙니다."

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

    ch_gura "처음에는 제가 꿈을 꾸고 있는 건지, 과로 때문에 정신병에 걸리기라도 한 건지 의심했습니다……"

    hide stand_gura
    ## 피로 휘갈겨 쓴 편지 이미지
    show ob_tegami with dissolve:
        xpos 430 yalign 0.3

    ch_gura "……그 편지를 ‘발견’하기 전까지는 말이죠."

    hide ob_tegami
    ## 모니카 화난 표정
    show stand_Monica_ddung with dissolve

    ch_monica "아유미의 추측이 맞았던 건가…… 예리하군."

    ## 모니카 cg 어둡게

    ch_ayumi "아…… 헤헤……"

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

    ch_gura "맞습니다. 많이 놀라셨을 테죠…… 하지만 이 방법밖에 없었습니다. 여러분은 아쿠다이칸을 무찌르신 분들이기도 하고요……"

    hide stand_gura
    ## 모니카 화난 표정
    show stand_Monica_ddung with dissolve

    ch_monica "뭐, 상황이 그러했다면 어쩔 수 없지. 어찌 되었든 우리를 이곳으로 불러내는 것에도 성공했으니……"

    ch_monica "……그런데, 우리는 뭘 하면 되지? 정보가 없는 건 이쪽도 마찬가지인데……"

    hide stand_Monica_ddung
    show stand_gura with dissolve

    ch_gura "아, 그것에 대해서 말인데요. 여러분은……"

    play music "audio/main/11fun.mp3"
    ## 빠르게 화면 한 바퀴 돌아가는 효과
    show bg_routen at fast_rotating

    ch_gura "편안히 온천을 즐기시면 됨다아{font=NanumGothic.ttf}———{/font}앗!!!!"

    hide stand_gura

    ## 유키 질색하는 표정
    show stand_Yuki_angry with dissolve

    ch_yuki "…………하?"

    hide stand_Yuki_angry
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

    ch_ninon "그 계회꾸에는 취명적인 헛점이 있는 것 같소 입니다……"

    player "헛점? 무슨……?"

    ch_ninon "이미 오에도 마을의 모두는 쇼군의 활약을 직접 목도하고, 쇼군의 업적을 기리기 위해 동상까지 세웠다 입니다."

    ch_ninon "이런 상황에서 니논들이 아무고토 모르는 척해봤자…… 금방 들통날 것입니다! 쇼군을 알아보지 못할 리가 없다 입니다!!"

    hide stand_Ninon_down
    show stand_gura with dissolve

    ch_gura "날카로우시군요."

    
    play music "audio/main/emer.mp3"

    ch_gura "하지만 그건…… 조금 슬픈 일입니다만, 걱정하지 않으셔도 될 겁니다."

    hide stand_gura
    ## 쿠우카 시무룩한 표정
    show stand_Kuka_down with dissolve

    ch_kuka "슬픈 일……? 무슨 말인가요……?"

    hide stand_Kuka_down

    show stand_gura with dissolve

    ch_gura "그나마 여러분들처럼 외부에서 온 관광객들이 온천을 방문하는 경우는 간혹 있지만, 오에도 주민들의 발길은 언제부터인가 뚝 끊겼습니다. 이것도 마물의 영향인지는 모르겠습니다만……"

    ch_gura "그리고, 직원들 중 아쿠다이칸 토벌 작전을 지켜보았던 토박이들은……"

    ch_gura "……전부 사라졌습니다. 부족한 일손은 오에도 마을에 새로 이사 온 이들과 외부인으로 충당되었죠……"

    ## 구라노스케 어둡게

    ch_ayumi "그런……"

    ## 구라노스케 밝게

    ch_gura "하지만 오히려 이것을 무기로 사용할 수 있을지도 모르죠. 만약 쇼군이나 여러분의 정체를 알아보는 이가 있다면…… 그를 의심해 봐도 좋을 겁니다. 불행 중 다행이죠?"

    hide stand_gura
    ## 니논 시무룩한 표정
    show stand_Ninon_down with dissolve

    ch_ninon "쇼군의 동상은 어취합니카? 그걸 보고 쇼군의 얼굴을 알아보면……"

    ## 유키 질색하는 표정 화면 오른쪽에
    show stand_Yuki_angry at right with dissolve

    ch_yuki "아니 그거, 솔직히 안 닮았거든."

    hide stand_Yuki_angry
    hide stand_Ninon_down

    show stand_gura with dissolve

    ch_gura "홋홋홋…… 실물이 훨씬 멋지십니다."

    ch_nar "하긴…… 동상 따위가 내 잘생김을 전부 담을 수 있을 리가 없지……"

    ch_gura "그렇지만 아무래도 확실히 해 두는 게 좋겠죠."

    ch_gura "니논 님의 말씀대로, 여러분이 쇼군과 그 일행분들이라는 사실이 들통날 가능성을 완전히 배제할 순 없습니다."

    ch_gura "마물이 아닌 인간이 여러분의 정체를 눈치챈다면, 그건 아마 오에도 마을에 퍼져 있는 ‘쇼군 영웅담’ 때문일 겁니다."

    ## 모니카 놀란 표정 화면 왼쪽에
    show stand_Monica_surprised at left with dissolve

    ch_monica "그, 그 일화가 아직까지 거론되고 있다고……?! 아니, 동상까지 세워졌으니 어쩌면 당연한 것일지도……"

    ## 모니카 어둡게, 쿠우카 망상하는 표정 화면 오른쪽에
    show stand_Kuka_mousou at right with dissolve

    ch_kuka "히에엑……!! 쿠, 쿠우카는 자신도 모르는 사이에 이야깃거리가 되어 얼굴 한 번 본 적 없는 사람들에게 메차쿠차 소비되고 있었던 거네요……!! 죽을 때까지 대중의 시선으로부터 자유롭지 못한 채 끝없이 능욕당하는 운명!!! 지금까지 겪어 온 수모와는 비교할 수 없을 정도로 자극이 강할지도……!!!! 크흣, 크헤헷……"

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

    ch_gura "그, 그렇게까지 말하지는 않았지만……"

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

   
    stop music

    show cg_babybung with dissolve

    player "테에엥 마망……"

    hide cg_babybung
    ## 모니카 시무룩한 표정
    show stand_Monica_down with dissolve

    ch_monica "??"

    hide stand_Monica_down

    show cg_babybung with dissolve

    player "응애 나 애기프붕."

    hide cg_babybung
    ## 유키 질색하는 표정
    show stand_Yuki_angry with dissolve

    ch_yuki "……"

    hide stand_Yuki_angry

    show cg_babybung with dissolve
    player "응애 맘마조."

    hide cg_babybung
    ## 쿠우카 질색하는 표정
    show stand_Kuka_hiku with dissolve

    ch_kuka "…………"

    player "바…… 바보처럼 연기하라며……? 반응들이 왜 이래?"

    play music "audio/main/11fun.mp3" fadein 3.0

    ## 쿠우카 놀란 표정
    show stand_Kuka_surprised
    hide stand_Kuka_hiku

    ch_kuka "………핫?! 아, 그, 그랬죠…… 너무 실감나게 연기하셔서…… 쿠우카, 순간 진심으로 도S 씨를 경멸할 뻔했어요……"

    hide stand_Kuka_surprised
    ## 모니카 놀란 표정
    show stand_Monica_surprised with dissolve

    ch_monica "귀, 귀공은 과연 굉장하군…… 나도 모르게 검을 뽑을 뻔했어……"

    hide stand_Monica_surprised
    ## 니논 억울한 표정
    show stand_Ninon_innocence with dissolve

    ch_ninon "이 정도로 열과 성의를 다 하실 줄이야 입니다…… 니논, 몹쉬 감동했소 입니다……!"

    hide stand_Ninon_innocence
    show stand_gura with dissolve

    ch_gura "후…… 훌륭합니다……! 그 누구도 쇼군이라고는 절대 생각지 못할 엄청난 연기……!!"

    hide stand_gura

    ch_nar "음…… 콧코로 앞에선 평소에도 이렇게 한다는 사실은 숨기는 게 좋겠지……"

    player "그러면…… 이제 온천으로 들어갈 수 있는 건가?"

    show stand_gura with dissolve

    ch_gura "아, 네! 웬만한 건 모두 설명 드린 것 같으니…… 바로 안내해 드리겠습니다!"

    ch_gura "그럼, 이쪽으로……"

    hide stand_gura

    stop music fadeout 3.0

    hide bg_routen


    jump scene_eight
## S# 8. 온천 건물 내부 #####################
label scene_eight:
    $renpy.pause(1.5)
    play music "audio/main/5orientalcommon.mp3"
    #3 온천 건물 내부 cg 
    scene bg_onsen onlayer middle
    show bg_black onlayer background

    show stand_gura onlayer forward

    ch_gura "이제부터 보여 드릴 것은, 저희 온천의 야심 찬……"

    show bg_onsen onlayer middle at fast_rotating

    ch_gura "『유카타』 임다아{font=NanumGothic.ttf}————{/font}앗!!!!!"

    ch_gura "마음에 드는 걸로 하나씩 골라 줍쇼오{font=NanumGothic.ttf}————{/font}옷!!!!!"

    hide stand_gura onlayer forward
    ## 니논 놀란 표정
    show stand_Ninon_surprise onlayer forward with dissolve
    hide bg_onsen onlayer middle
    show bg_onsen onlayer middle at fast_rotating:
        xalign 0.5 yalign 0.5

    ch_ninon "우오오오옷{font=NanumGothic.ttf}——{/font}!!!!! 동국의 의복 문화 스게에{font=NanumGothic.ttf}———{/font}엣!!!!!!!!"

    hide stand_Ninon_surprise onlayer forward

    ch_ayumi "니…… 니논 씨의 상태가 이상해요……?"

    ## 니논 비장한 표정
    show stand_Ninon_daiji onlayer forward with dissolve

    ch_ninon "아무것도 이상할 것 없다 입니다! 이것은 매우 자연스러운 동국의 예법 입니다!"

    ch_ninon "『인법 {font=NanumGothic.ttf}·{/font} 동국의 이런 점이 대단하다』 !!"

    ch_ninon "별것도 아닌 걸 보면서 과도한 GESTURE 와 함께 호들갑을 떠는 인술 입니다! 여러분도 따라해 보세요 입니다!!"

    hide stand_Ninon_daiji onlayer forward

    ## 쿠우카 대사로 넘어갈 때 까지 구라노스케 서서히 축소
    hide bg_onsen onlayer middle with fade
    $ camera_move(0, 0, 600, 0, 0)
    show stand_gura onlayer forward with dissolve 
    $ camera_move(0, 0, 300, 0, 3)

    ch_gura "……별것도……"

    $ camera_move(0, 0, 0, 0, 3)

    ch_gura "………아닌 거………"

    show bg_onsen
    hide stand_gura onlayer forward
    hide bg_black onlayer background

    ## 쿠우카 놀란 표정
    show stand_Kuka_surprised with vpunch

    ch_kuka "예, 예뻐요!! 정말 예뻐요!!! 쿠, 쿠우카는 이걸로 할게요……"

    hide stand_Kuka_surprised
    ## 니논 웃는 표정
    show stand_Ninon with dissolve

    ch_ninon "니논은 이것으로 하겠소 입니다~! 동국의 정열적인 SOUL이 느껴진다 입니다!"

    hide stand_Ninon
    ## 유키 자뻑하는 표정
    show stand_Yuki_proud with dissolve

    ch_yuki "내 아름다움을 온전히 담을 수 있는 옷은 없는 것 같지만, 그나마 이게 가장 나의 미모에 잘 어울릴 것 같네♪"

    hide stand_Yuki_proud

    ch_ayumi "예쁘다…… 이걸 입으면 선배가 나를 귀엽게 봐 줄지도……! 저는 이걸로 할게요!"

    ## 모니카 시무룩한 표정
    show stand_Monica_down with dissolve

    ch_monica "‘뭘 입어도 어차피 안 보일 텐데……?’"

    ch_monica "으음…… 그나저나 여성용 유카타는 하나같이 화려하군. 이런 건 조금 부담스러운데…… 좀 더 수수한 디자인은 없는 건가?"

    hide stand_Monica_down
    show stand_gura with dissolve

    ch_gura "아, 모니카 님은 거기 말고 옆 칸의 어린이용으로 고르시면 됩니다."

    hide stand_gura
    ## 모니카 부끄러워하는 표정
    show stand_Monica_dere at center with dissolve:
        easeout 0.3 ypos -50
        ease 0.2 ypos 50
        easeout 0.3 ypos -50
        ease 0.2 ypos 50  
        ## 팔짝 뛰는 모션
        
    ch_monica "그러니까 어린애가 아니란 말이다{font=NanumGothic.ttf}———{/font}!!!!!!!!"

    ch_nar "화내면서 어린이용을 고르고 있네……"

    hide stand_Monica_dere

    player "나도 골랐는데…… 바로 갈아입으면 돼?"

    show stand_gura with dissolve

    ch_gura "아, 아닙니다! 먼저 몸을 청결히 한 뒤 유카타로 갈아입는 것이 온천의 기본 원칙입니다!"

    ch_gura "모두 유카타를 고르신 것 같군요…… 그럼 탕으로 안내해 드리겠습니다!"

    hide stand_gura
    hide bg_onsen
    

    jump sceneNum9
## S# 9. 온천 건물 내부 (2) #################
label sceneNum9:
    scene bg_black
    show bg_entrance with fade

    show stand_gura with dissolve

    ch_gura "푸른 휘장이 걸린 입구는 남탕, 붉은 휘장은 여탕입니다. 몸을 청결히 씻으신 뒤 탕에 들어가시면 됩니다!"

    ch_gura "유카타는 온천욕이 끝난 후에 갈아입고 나와 주세요!"

    hide stand_gura
    ## 쿠우카 시무룩한 표정
    show stand_Kuka_down with dissolve

    ch_kuka "어, 저기…… 이곳엔 혼욕탕은 없나요?"

    hide stand_Kuka_down
    show stand_gura with dissolve

    ch_gura "혼욕……?"

    ch_gura "아……"
    
    ch_gura "그렇군요…… 혼욕탕이 아니라면 쇼군 님과 함께 행동하지 못할 테니……"

    hide stand_gura
    ## 쿠우카 놀란 표정
    show stand_Kuka_surprised with dissolve

    ch_kuka "……에? 네……엣! 도, 도S 씨와 떨어지게 되면, 위…… 위험해 질 수도 있으니까요! 네!"

    ## 왼쪽에 모니카 시무룩한 표정
    show stand_Monica_down at left with dissolve

    ch_monica "‘……그렇다기보다 사리사욕을 채우려는 목적이 크겠지만……’"

    hide stand_Monica_down
    hide stand_Kuka_surprised

    show stand_gura with dissolve

    ch_gura "음…… ‘그 일’은 항상 밤중에 일어났으니, 당장은 따로 행동하셔도 위험하지 않을 겁니다."

    ch_gura "그리고…… 결론부터 말씀드리자면 현재 혼욕탕은 출입할 수 없습니다."

    hide stand_gura
    ## 니논 시무룩한 표정
    show stand_Ninon_down with dissolve

    ch_ninon "NON……"

    hide stand_Ninon_down

    show stand_gura with dissolve

    ch_gura "원래라면 개방되어 있었겠지만…… 불미스러운 사고가 많이 일어나서요. 좀전에 이야기를 나누었던 곳도 혼욕탕이었습니다."

    hide stand_gura

    ch_ayumi "히잉……"

    ## 모니카 뚱한 표정
    show stand_Monica_ddung with dissolve
    
    ch_monica "그대들…… 그런 표정 짓지 마라! 우리가 혼욕 때문에 온 것은 아니지 않나!"

    hide stand_Monica_ddung

    ch_nar "까비……"

    ## 유키 자뻑하는 표정
    show stand_Yuki_proud with dissolve

    ch_yuki "뭐, 그렇다면 어쩔 수 없네~ 우리는 먼저 들어가 볼게~"

    ch_yuki "[name]~ 어서 들어가자. 손 잡고 갈래? 팔짱도 낄까?"

    ## 니논 억울한 표정 오른쪽

    show stand_Ninon_innocence at right with dissolve

    ch_ninon "으그그극…… 니논은 이 일을 기억할 것입니다……"

    hide stand_Ninon_innocence
    hide stand_Yuki_proud

    show stand_gura with dissolve

    ch_gura "엇, 그쪽은 남탕인데요……"

    hide stand_gura
    ## 유키 기본 표정
    show stand_Yuki with dissolve

    ch_yuki "응? 나는 남자니까, 남탕에 들어가는 게 당연하지."

    hide stand_Yuki

    show stand_gura with dissolve

    ch_gura "……아, 그렇군요! 죄송합니다, 유키 님은 남……"
    
    hide stand_gura

    hide bg_entrance
    $ camera_move(0, 0, 600, 0, 0)
    show bg_universe onlayer middle
    
    stop music
    show stand_gura onlayer forward
    
    $ camera_move(0, 0, 300, 0, 6)

    ch_gura "남…………"

    $ camera_move(0, 0, 0, 0, 6)

    ch_gura "…………………"

    hide bg_universe onlayer middle
    hide stand_gura onlayer forward

    show bg_entrance_02

    play music "audio/main/5orientalcommon.mp3" fadein 3.0

    ## 유키 뚱한 표정
    show stand_Yuki_ddung with dissolve

    ch_yuki "뭐야~ 더 할 말 없으면 들어간다?"

    hide stand_Yuki_ddung
    show stand_gura with dissolve

    ch_gura "……네? 아, 네……"

    ch_gura "부, 부디 온천을 즐겨 주십시오……"

    ch_nar "모르고 있었구나……"

    hide stand_gura

    ## 모니카 웃는 표정
    show stand_Monica with dissolve

    ch_monica "모두들, 이만 들어가자."

    show stand_Monica_munen
    hide stand_Monica

    ch_monica "유키와 귀공도, 으음…… 무, 무사히 돌아오도록……!"

    hide stand_Monica_munen

    ch_nar "‘무사히’ 라는 건 무슨 의미야……!"

    ## 유키 자뻑하는 표정
    show stand_Yuki_proud with dissolve

    ch_yuki "……♪"

    hide stand_Yuki_proud
    hide bg_entrance_02

    
    stop music fadeout 3.0


    jump sceneNum10
## S# 10. 검은 배경 ########################
label sceneNum10:

    $renpy.pause(1.5)
    play music "audio/main/emer.mp3"
    hatena "……"

    hatena "손……님."

    hatena "남자…… 시……작? ……여자."

    hatena "아직…… 살……아있다."

    hatena "먹……고, 싶어? 주문……하신. 저, 기……요?"

    hatena "먹는…… 먹……"

    hatena "먹는다."

    
    stop music fadeout 3.0
    if love_point == 4:
        jump cg_yukifirst
    else:
        jump sceneNum11_2Common
## S# 11-2. 대욕탕 (공통 루트) ################
label sceneNum11_2Common:
    play music "audio/main/5orientalcommon.mp3"
    ## 대욕탕 cg
    scene bg_daiyokujyo onlayer middle with fade
    hide bg_black

    ch_nar "……와."

    ch_nar "여기, 상상 이상으로 넓고 좋네……"

    ch_nar "손님이 많이 없는 게 이해되지 않을 정도로."

    player "……근데 너, 진짜로 안 들어올 거야?"

    ch_yuki angry "그런 곳에 어떻게 몸을 담글 수 있어?!"

    ch_yuki angry "땀 냄새 나는 남자들이 몇 명이나 왔다 갔는지도 모르잖아!"

    player "……"

    player "마음대로 해라……"

    ch_nar "그럼 옷은 왜 갈아입은 거야……"

    $ renpy.pause(1.0)

    ch_nar "아…… 그나저나……"

    ch_nar "온천 진짜 좋네……"

    ch_nar "물 온도도 적당하고, 사람도 없어서 조용하니……"

    ch_nar "……이대로면 잠들 수 있겠"

    ## 화면 흔들리는 효과
    show bg_daiyokujyo onlayer middle with hpunch

    ## 니논 대사 글꼴 크기 크게 + 굵게
    ch_ninon surp "{b}{size=30}우오오오옷!!!!!!!!!!{/size}{/b}"

    ## 나레이션 대사 글꼴 크기 크게 + 굵게
    ch_nar "{b}{size=30}야발!!!!!!!!!{/size}{/b}"

    ch_ninon surp "쿠…… 쿠우카 씨……"

    ch_ninon surp "이건…… 꽤 하잖아 입니다!!!!"

    ch_kuka surp "하으?! 쿠, 쿠우카, 갑자기 그런 곳이 만져지면……!!! 헤으응!!"

    ch_nar "……여탕이 바로 옆에 붙어 있는 구조인가?"

    ch_nar "그렇다고 해도 방음이 전혀 안 될 줄은……"

    ch_nar "근데 무슨 이야기를 하고 있는 거지?"

    ch_kuka dere "니, 니논 씨야말로 엄청나네요……!"

    ch_kuka dere "이것이 말로만 듣던, 서방의 우월한 유전자……!!"

    ch_monica ddung "……뿌우……"

    ch_ninon surp "모니카 씨? 기묘한 소리를 내고 있다 입니다?"

    ch_monica ddung "그…… 그런 지방덩어리 같은 건…… 저, 전투에 방해만 될 뿐이다!"

    ch_ninon wink "모니카 씨는 귀여우니까 아무래도 좋다 입니다~"

    ## 화면 흔들리는 효과
    show bg_daiyokujyo onlayer middle with hpunch

    ch_monica dere "어린애 취급 하지 마아아아!!!!!!!!"

    ch_nar "음…… 뭔가 들으면 안 되는 이야기 같은데……"

    ch_nar "딱히 엿듣는 건 아니니까 괜찮겠지……"

    ch_ninon surp "HEIN……! 실화 입니까……?! 쿠우카 씨……!!"

    ch_kuka surp "햐히익~~!!"

    ch_ninon surp "이…… 이런 것까지 가능한 건가요 입니다……!!"

    ch_kuka dere "쿠…… 쿠우카의 신체를 장난감처럼!!! 헤으응으!!!!"

    ch_nar "어우야……"

    ch_ninon surp "그…… 그렇다면…… 이건 어떠냐 입니다……!! 「인법 {font=NanumGothic.ttf}·{/font} 모찌 선물쉐트」!!!"

    ch_kuka dere "응고오오옥♥"

    ch_nar "대체 무슨 인법인데?! 이름이 저 모양이라 감도 안 와……!"

    ch_ninon surp "C’EST FOU!!! 이건…… 이런 건……!!"

    ch_ninon surp "동국 트뤠디셔널 빨간 췍 『도키뭬키 잉챠잉챠 시리즈』에서나 보던 것인데……!!"

    ch_nar "그…… 그건 또 뭐야……!"

    ch_nar "나중에 빌려 달라고 해야겠다……!"

    ch_yuki smile "[name]!!"

    $renpy.pause(1.0)

    player "예??!!!"

    player "네?!?!?!"

    ch_yuki smile "푸훗~ 반응이 왜 그래?"

    ch_yuki smile "아하…… 긴장한 거구나~?"

    ch_yuki proud "무리도 아니지~ 이토록 아름다운 나와 지금껏 단둘이 있었으니까…… 그것도,"

    ## 대사 출력 느리게

    ch_yuki proud "{cps=*0.5}알. 몸. 인. 채. 로.{/cps}"

    ## 화면 흔들리는 효과
    show bg_daiyokujyo onlayer middle with hpunch

    player "으아아아!!! 말하면서 그런 거 보여 주지 마!!!!"

    ch_yuki proud "후훗…… 아무 때나 볼 수 있는 모습이 아니라구?"

    ch_yuki proud "다시 옷을 입기 전까지 두 눈에 잘 새겨 놓도록 해~"

    ch_nar "…………"

    ch_nar "소…… 속이 안 좋아졌어……"

    ch_nar "빨리 나가야겠다……"

    $renpy.pause(2.5)

    ch_ayumi "…………"

    ch_ayumi "지이이이………"

    hide bg_daiyokujyo onlayer middle

    jump sceneNum12Common
## S# 12. 온천 내부 [여기부터 모든 스탠딩 cg는 유카타 복장으로](공통루트)#######
label sceneNum12Common:
    play music "audio/main/5orientalcommon.mp3"
    scene bg_onsen with fade
    hide bg_black onlayer background

    ## 니논 윙크하는 표정
    show stand_Ninon_yukata_wink with dissolve

    ch_ninon "쇼군, 쇼군~! 니논을 봐 주세요 입니다! 잘 어울린다 입니까?"

    hide stand_Ninon_yukata_wink

    ## 모니카 무심한 척 하는 표정
    show stand_Monica_yukata_munen with dissolve

    ch_monica "이것이 동국의 유카타인가…… 바, 바람이 너무 잘 통해서 조금 민망하군……"

    hide stand_Monica_yukata_munen
    ## 유키 자뻑하는 표정
    show stand_Yuki_yukata_proud with dissolve

    ch_yuki "어쩜…… 예상은 했지만, 이렇게나 아름다울 줄이야…… 나는 대체 어디까지 예뻐질 작정인 걸까? 나조차도 도저히 가늠이 되지 않아……♪"

    hide stand_Yuki_yukata_proud
    ## 쿠우카 부끄러워하는 표정
    show stand_Kuka_yukata_shamed with dissolve

    ch_kuka "……으으…… 지난 번 기모노보단 낫지만…… 유카타도 굉장히 입기 어려운 옷이네요…… 금방이라도 벗겨질 것만 같아요……"

    ## 쿠우카 망상하는 표정
    show stand_Kuka_yukata_mousou
    hide stand_Kuka_yukata_shamed

    ch_kuka "……벗겨져? 모두의 앞에서……? 큿, 크흐흣…… 크헷……"

    hide stand_Kuka_yukata_mousou

    ch_ayumi "‘선배…… 귀엽다고 해 주지 않으려나……’"

    ch_nar "오……"

    ch_nar "4명 다 괜찮네……"

    show stand_gura with dissolve

    ch_gura "저기…… 쇼군 님……"

    player "응?"

    ch_gura "그…… 보셨습니까……?"

    player "……뭘……?"

    ch_gura "유키 님…… 정말 남자인가요……?"

    ## 호흡 끊기
    $renpy.pause(1.0)

    player "…………"

    player "그 얘긴 하고 싶지 않아……"

    ch_gura "……"

    ch_gura "……실례했습니다……"

    hide stand_gura
    
    ## 모니카 웃는 표정
    show stand_Monica_yukata with dissolve

    ch_monica "그나저나, 구라노스케…… 공?"

    ch_monica "동국의 온천 문화에 대해서는 잘 아는 바가 없는데…… 순서에 맞는 예절을 가르쳐 줄 수 있을까?"

    hide stand_Monica_yukata
    show stand_gura with dissolve

    ch_gura "물론입죠!"

    ch_gura "그 전에, 가져오신 짐들이 꽤 많아 보이니…… 먼저 객실로 모시겠습니다!"

    ch_gura "남녀 도합 총 다섯 분이니까, 방 개수는……"

    hide stand_gura
    ## 니논 비장한 표정
    show stand_Ninon_yukata_daiji with dissolve
    ch_ninon "……방 개수는?"

    hide stand_Ninon_yukata_daiji
    show stand_gura with dissolve

    ch_gura "……!!"

    hide stand_gura
    show bg_onsen onlayer middle
    ## 니논 비장한 표정
    show stand_Ninon_yukata_daiji onlayer forward with dissolve

    $ camera_move(0, -1000, 400, 0, 1)

    ch_ninon "……!!!"

    hide stand_Ninon_yukata_daiji onlayer forward
    $ camera_move(0, 0, 0, 0, 0)

    show stand_gura onlayer forward

    $ camera_move(0, 0, 600, 0, 1)

    ch_gura "……!!!!"

    $ camera_move(0, 0, 0, 0, 0.5)

    ch_gura "…………"

    $ camera_move(0, 0, 600, 0, 0.5)

    play sound "audio/sound/1bak2il.mp3"
    show highlight onlayer forward with hpunch

    ch_gura "{b}{size=30}……‘하나’입니다!!!{/size}{/b}" 

    $ camera_move(0, 0, 0, 0, 0)

    hide highlight onlayer forward
    hide stand_gura onlayer forward
    hide bg_onsen onlayer middle

    ## 니논 윙크하는 표정
    show stand_Ninon_yukata_wink with dissolve

    ch_ninon "우효~~"

    hide stand_Ninon_yukata_wink
    show stand_gura with dissolve

    ch_gura "그게…… 자, 작은 객실은 현재 빈 방이 없어서요……"

    ch_gura "워낙 큰 방이니까, 딱히 불편하진 않으실 겁니다. 그럼……"

    hide stand_gura
    show stand_Monica_yukata_down with dissolve

    ch_monica "……분명 손님이 없다고 하지 않았나? 빈 방이 없다는 건 무……"

    show stand_Ninon_yukata_daiji at left with dissolve

    ch_ninon "씁! 모니카 씨!"

    ch_ninon "그만! 거기까지! 쓰읍!"

    show stand_Monica_yukata_surprised
    hide stand_Monica_yukata_down
    hide stand_Monica_yukata_daiji

    ch_monica "?????"

    hide stand_Monica_yukata_surprised
    hide stand_Ninon_yukata_daiji

    ch_ayumi "……왜 인원이 다섯 명이라는 말에는 아무도 반박하지 않는 건가요오!!!!"

    hide bg_onsen

    jump sceneNum13Common
## S# 13. 온천숙소 (다다미 방)(공통루트)#####
label sceneNum13Common:

    $ renpy.pause(1.5)
    play music "audio/main/5orientalcommon.mp3"
    scene bg_tadami_day
    
    ## 니논 당황한 표정
    show stand_Ninon_yukata_surp with dissolve

    ch_ninon "……이건……"

    ch_ninon "꿈에 그리던 동국의 전통 다다뮈 방 입니다……!!"

    ch_ninon "이런 곳에서 하룻밤을 보낼 수 있다니……! 니논은 이제 죽어도 여한이 없다 입니다! 할복 하고 싶습니다!"

    hide stand_Ninon_yukata_surp

    ## 쿠우카 부끄러워하는 표정
    show stand_Kuka_yukata_shamed with dissolve

    ch_kuka "……어, 엣? 그, 그러고 보니……"

    ch_kuka "……방이 하나……라고요……? 그렇다는 건……"

    ## 기본 표정으로 변경
    show stand_Kuka_yukata
    hide stand_Kuka_yukata_shamed

    ch_kuka "도, 도S 씨와 한 방에서…… 하, 하룻, 밤을……?!"

    hide stand_Kuka_yukata
    ## 니논 비장한 표정
    show stand_Ninon_yukata_daiji with dissolve

    ch_ninon "눈치채는 것이 느리군요, 쿠우카 씨……!"

    hide stand_Ninon_yukata_daiji
    ## 쿠우카 망상하는 표정

    show stand_Kuka_yukata_mousou with dissolve

    ch_kuka "……크흣…… 후히힛…… 모두가 잠든 고요한 새벽…… 가혹한 바깥의 추위로부터 소녀를 지키던 따스한 솜이불은, 격렬하고도 은밀한 침범에 속수무책으로 뚫려 버리고…… 더러움을 모르던 순백의 도화지는 검은 얼룩으로 서서히 물들어 가는데……!! 케헤헷!!!"

    hide stand_Kuka_yukata_mousou

    ch_ayumi "서…… 선배와 같은 방에서 잠을……"

    ch_ayumi "아, 뭐어…… 처음은 아니긴 하지만요……"

    ## 니논 비장한 표정
    show stand_Ninon_yukata_daiji with dissolve

    ch_ninon "……아유미 씨?"

    ch_ninon "쇼군의 오른팔로서…… 그냥 넘어갈 이야기는 아닌 듯하오 입니다……?"

    show stand_Ninon_yukata_daiji:
        linear 0.5 xalign 0.8

    ## 유키 뚱한 표정
    show stand_Yuki_yukata_ddung at left with dissolve

    ch_yuki "근데 말야~ 니논……"

    ## 니논 놀란 표정
    show stand_Ninon_yukata_surp at right
    hide stand_Ninon_yukata_daiji

    ch_ninon "니논을 부르셨소 입니다?!"

    ch_yuki "그 쇼군이라고 부르는 거,"

    ch_yuki "슬슬 그만두는 게 낫지 않아?"

    ## 니논 패닉한 표정
    show stand_Ninon_yukata_panic at right
    hide stand_Ninon_yukata_surp

    ch_ninon "무……무머무, MOU, 뭐라고 입니다……?!"

    ## 니논 화난 표정
    show stand_Ninon_yukata_angry at right
    hide stand_Ninon_yukata_panic

    ch_ninon "그, 그 말은, 니논한테…… 감히 쇼군에 대한 충의를 버리라는, 그런 뜻 입니까?!!"

    ch_yuki "아니~ 생각을 좀 해 봐."

    ch_yuki "저 녀석이 바보처럼 보이려고 저렇게 노력하는 이유가 뭐였는데?"

    ch_nar "ㅋㅋ 까먹고 있었는데."

    ch_ninon "그야……"

    ch_ninon "……쇼군이 쇼군이라는 것을…… 들키지 않……?"

    ## 호흡 끊기
    $renpy.pause(1.0)

    ## 니논 패닉한 표정
    show stand_Ninon_yukata_panic at right
    hide stand_Ninon_yukata_angry

    ch_ninon "……이럴수GA……"

    ## 니논 억울한 표정
    show stand_Ninon_yukata_innocent at right
    hide stand_Ninon_yukata_panic

    ch_ninon "니, 니논은…… 대췌 무슨 짓을……"

    ch_ninon "쏭…… 쏭구하옵뉘다, 쇼군!!! 할복을…… 할복을 하겠소 입니다……!"

    hide stand_Ninon_yukata_innocent
    hide stand_Yuki_yukata_ddung

    ch_nar "바로 쇼군이라 부르는 니 능지가 레전드다……"

    ## 모니카 시무룩한 표정

    show stand_Monica_yukata_down with dissolve

    ch_monica "……유키의 말이 맞다. 시정할 필요가 있겠어."

    hide stand_Monica_yukata_down
    ## 니논 억울한 표정
    show stand_Ninon_yukata_innocent with dissolve

    ch_ninon "OH MON DIEU……!! 쇼군을 앞에 두고도 쇼군이라 부를 수 없다니…… 이 무슨 병천척력 입니다……!!!"

    hide stand_Ninon_yukata_innocent

    player "청력병천이겠지, 바보야!"

    show stand_Monica_yukata_down with dissolve

    ch_monica "진심으로 청천벽력 같은 발언들이군……"

    hide stand_Monica_yukata_down

    ch_ayumi "‘혼란스러운 와중에도 똥멍청이 연기를……! 역시 선배는 대단해…… 나도 분발해야지……!’"

    show stand_Monica_yukata_down at left with dissolve

    ch_monica "니논…… 대의를 위해서다. 적어도 온천에 머무르는 동안만은 참아 다오……!"

    ## 니논 억울한 표정 오른쪽에

    show stand_Ninon_yukata_innocent at right with dissolve

    ch_ninon "모니카 쒸……!"

    ch_ninon "……이 니논, 해내 보이고 말겠소 입니다……!"

    ch_ninon "……쇼군을 위해서라면!"

    ch_nar "벌써 실패했어……"

    hide stand_Ninon_yukata_innocent
    hide stand_Monica_yukata_down

    ## 쿠우카 기본 표정
    show stand_Kuka_yukata at left with dissolve

    ch_kuka "그, 그러면……! 도S 씨라 부르는 건 상관없는 거겠죠……!"

    ## 모니카 무심한 척 하는 표정
    show stand_Monica_yukata_munen at right with dissolve

    ch_monica "아, 그건 뭐…… 마음대로 해라……"

    ## 쿠우카 망상하는 표정
    show stand_Kuka_yukata_mousou at left
    hide stand_Kuka_yukata


    ch_kuka "쿠헤헤헷……!"

    ch_nar "그딴 거에 집착하지 마……!"

    hide stand_Kuka_yukata_mousou
    hide stand_Monica_yukata_munen

    ch_ninon "아닛……!! 여러분~~!"

    ch_ninon "이쪽으로 와 보세요 입니다~~!!!"

    ch_nar "저건 또 언제 저기로 기어들어 갔어?"

    hide bg_tadami_day

    jump sceneNum14Common
## S #14. 실내 욕실 (낮) (공통 루트) ########
label sceneNum14Common:
    play music "audio/main/5orientalcommon.mp3"
    scene bg_indoor_sauna_day with fade
    show bg_indoor_sauna_day onlayer middle
    ## 니논 비장한 표정
    show stand_Ninon_yukata_daiji onlayer forward with dissolve

    ch_ninon "이것이 바로 동국의……"

    show highlight onlayer forward with hpunch
    $ camera_move(0, -1000, 400, 0, 1)

    ch_ninon "욕실 입니다!!!"

    hide highlight onlayer forward
    $ camera_move(0, 0, 0, 0, 0)

    ch_ninon "무척이나……"

    hide bg_indoor_sauna_day onlayer middle
    hide stand_Ninon_yukata_daiji onlayer forward

    ## 모니카 시무룩한 표정

    show stand_Monica_yukata_down with dissolve

    ch_monica "좁군."

    ## 유키 질색하는 표정
    show stand_Yuki_yukata_angry at left with dissolve

    ch_yuki "좁아."

    ## 쿠우카 질색하는 표정
    show stand_Kuka_yukata_hiku at right with dissolve

    ch_kuka "좁네요."

    ch_ayumi "어……? 나쁘지 않다고 생각한 건 저 뿐인가요……?"

    hide stand_Kuka_yukata_hiku
    hide stand_Yuki_yukata_angry
    hide stand_Monica_yukata_down

    ## 니논 시무룩한 표정
    show stand_Ninon_yukata_down with dissolve

    ch_ninon "……좁다 입니다."

    ch_ayumi "에…… 이 정도면 넓……"

    ## 니논 당황하는 표정
    show stand_Ninon_yukata_emb
    hide stand_Ninon_yukata_down

    ch_ninon "그…… 그러니까 이, 이것은, 동국의 검소하고 소바쿠한 Culture이 건물 양쉭에 반영된 것으로……"

    hide stand_Ninon_yukata_emb
    ## 유키 질색하는 표정
    show stand_Yuki_yukata_angry with dissolve

    ch_yuki "그 동국이라는 곳에는 거지들밖에 없어?"

    hide stand_Yuki_yukata_angry
    ## 니논 억울한 표정

    show stand_Ninon_yukata_innocent with dissolve

    ch_ninon "…………"

    ## 니논 비장한 표정
    show stand_Ninon_yukata_daiji
    hide stand_Ninon_yukata_innocent

    ch_ninon "맞습니다. 동국은 가난하기 짝이 없는 쓰레기 빈민국입니다."

    hide stand_Ninon_yukata_daiji

    ch_nar "컨셉을 포기했어?!"

    ch_ayumi "아니…… 그렇게까지 작……"
    
    play sound "audio/sound/harapeko.mp3"

    ch_nar "꼬르륵……"

    $renpy.pause(1.0)

    player "?"

    ## 모니카 무심한 척 하는 표정

    show stand_Monica_yukata_munen with dissolve

    ch_monica "……아니다."

    player "뭐? 뭐가 아니야?"

    ## 모니카 부끄러워하는 표정
    show stand_Monica_yukata_dere
    hide stand_Monica_yukata_munen

    ch_monica "내 배에서 난 소리가 아니란 말이다!!"

    hide stand_Monica_yukata_dere

    ch_nar "뭐지?? 어쩌라는 거지?"

    ## 니논 웃는 표정

    show stand_Ninon_yukata with dissolve

    ch_ninon "배고픈 건 부끄러운 것이 아니다 입니다~"

    ## 니논 윙크하는 표정
    show stand_Ninon_yukata_wink
    hide stand_Ninon_yukata

    ch_ninon "모니카 씨~ 맘마 먹으러 가까용~ 입니다."

    hide stand_Ninon_yukata_wink
    ## 모니카 부끄러워하는 표정
    show stand_Monica_yukata_dere with dissolve
    ## 화면 흔들리는 효과
    show bg_indoor_sauna_day with hpunch

    ch_monica "시, 시끄럽다!!!!! 그리고 그런 말투 쓰지 마!!!"

    hide stand_Monica_yukata_dere
    ## 유키 웃는 표정
    show stand_Yuki_yukata with dissolve

    ch_yuki "하긴, 배고플 만하지. 급하게 온다고 여태 아무것도 먹지 않았잖아."

    hide stand_Yuki_yukata
    ## 모니카 무심한 척 하는 표정
    show stand_Monica_yukata_munen with dissolve

    ch_monica "그…… 그렇지? 모두들, 시장할 테니……"

    hide stand_Monica_yukata_munen

    player "난 별로 배 안 고프"

    
    play sound "audio/sound/hit.wav"

    show bg_indoor_sauna_day with hpunch

    ## 모니카 무심한 척하는 표정
    show stand_Monica_yukata_munen with dissolve

    ch_monica "식, 식당이라도 가 보자! 거기서 뭔가 찾을 수 있을지도 모르니!"

    hide stand_Monica_yukata_munen

    ## 니논 웃는 표정
    show stand_Ninon_yukata with dissolve

    ch_ninon "찬성 입니다~ 그러면 식당으로 출발 입니다~!"

    ## 니논 비장한 표정
    show stand_Ninon_yukata_daiji
    hide stand_Ninon_yukata

    ch_ninon "……후후, 모니카 씨."

    ch_ninon "옛정을 생각해서, 미리 말씀드리자면……"

    ch_ninon "서두르는 것이 좋을 것이다 입니다……"

    ch_ninon "빨리 오지 않으면…… 니논이 전부 먹어버릴 수도 있다구요 입니다……?"

    hide stand_Ninon_yukata_daiji
    ## 모니카 시무룩한 표정

    show stand_Monica_yukata_down with dissolve

    ch_monica "……? 무엇을……"

    hide stand_Monica_yukata_down
    ## 니논 비장한 표정
    show stand_Ninon_yukata_daiji with dissolve

    ch_ninon "이론이론…… 잊어버린 겁니까……?"

    ch_ninon "한. 정. 판. 간. 식."

    hide stand_Ninon_yukata_daiji
    
    play sound "audio/sound/surp.mp3"

    ## 모니카 놀란 표정
    show stand_Monica_yukata_surprised with dissolve
    ch_monica "!!!!!"

    hide stand_Monica_yukata_surprised

    ## 니논 비장한 표정
    show stand_Ninon_yukata_daiji with dissolve

    ch_ninon "그러면 안녕닌닌 입니다!!!"

    show stand_Ninon_yukata_daiji:
        rotate 0
        linear 0.4 rotate 360

    hide stand_Ninon_yukata_daiji with dissolve

    ## 모니카 부끄러워하는 표정
    show stand_Monica_yukata_dere with dissolve

    ch_monica "제, 제…… 제군들!!!!!! 하루는 짧다!!!! 서, 서둘러라!!!! 어서!!!!!"

    show stand_Monica_yukata_dere with dissolve:
        xpos 640
        linear 0.5 xpos -500
    
    hide stand_Monica_yukata_dere

    ch_monica "따, 딱히 간식 때문은 아니야! 절대로 오해하지 마라!!!"

    ch_monica "니논!!!! 거기 서!!!!!"

    ch_ninon "헷헤헤!!! 닌자로 빙의한 니논의 SPEED 를 따라잡을 수는 없소 입니다!! 슈바바바밧!!!"

    ch_monica "지, 진짜로 다 먹어버릴 건 아니지?!?! 대답해라!!!! 멈춰~~~!!!!!"

    ch_nar "잘들 노네……"

    $renpy.pause(1.0)

    ## 브금 off
    stop music

    hatena "……쇼……"

    $renpy.pause(1.0)

    player "……?"

    ## 쿠우카 부끄러워하는 표정
    show stand_Kuka_yukata_shamed with dissolve

    ch_kuka "도S 씨……?"

    ch_kuka "왜 그러시는…… 뭐, 뭔가 저지르고 싶어지셨나요?"

    hide stand_Kuka_yukata_shamed

    player "어? 그게……"

    player "아무것도…… 아니 근데 뭐라는 거야? 빨리 나가기나 해."

    ## 쿠우카 망상하는 표정
    show stand_Kuka_yukata_mousou with dissolve

    show stand_Kuka_yukata_mousou with dissolve:
        xpos 640
        easeout 0.6 xpos 300
    hide stand_Kuka_yukata_mousou

    ch_kuka "도S 씨의 손이 억지로 쿠우카를~~~!! 이런 거친 플레이도 맘에 들어요……!!!"

    $renpy.pause(1.0)

    ch_nar "……뭔가,"

    ch_nar "순간 뭔가 이상한 느낌이……"

    ch_nar "……기분 탓인가……?"

    show bg_black with dissolve
    hide bg_indoor_sauna_day

    $renpy.pause(1.0)

    hatena "……"

    hatena "……에서?"

    hatena "않은…… 초이……"

    hatena "……끼……"

    hatena "……긱."

    jump sceneNum15_1Common
## S #15-1. 온천 건물 내부 (식당) (공통 루트)####
label sceneNum15_1Common:
    scene bg_onsen with fade
    
    play music "audio/main/5orientalcommon.mp3"
    show stand_gura with dissolve

    ch_gura "오, 여러분. 오셨습니까?"

    ch_gura "짐 정리를 끝내셨나 보군요."

    hide stand_gura
    ## 유키 웃는 표정
    show stand_Yuki_yukata with dissolve

    ch_yuki "응. 그런데 혹시 모니카 씨 못 봤어?"

    ch_yuki "좀 전에 니논이랑 같이 식당으로 달려갔는데……"

    hide stand_Yuki_yukata
    show stand_gura with dissolve

    ch_gura "아, 두 분이라면…… 벌써 저쪽에 자리를 잡으셨습니다."

    if love_point == 2:
        hide stand_gura
        jump cg_monicafirst
    else:
        pass
    ch_gura "배가 많이 고프신 모양이더군요…… 처음에는 무슨 산짐승 두 마리가 뛰어오는 줄 알았습니다……"

    hide stand_gura

    player "에이…… 아무리 그래도 여자애들한테 산짐승이라니, 말이 너무 심……"

    play music "audio/main/11fun.mp3"

    ch_ninon "{b}{size=30}모니카 씨, 간다 입니다!!!!{/size}{/b}"

    ch_monica "{b}{size=30}좋다!! 와라, 니논!!! 전력을 다해 상대해 주마!!!{/size}{/b}"

    show ob_moninon with dissolve:
        xpos 330 ypos 15

    ch_ninon "「인법 {font=NanumGothic.ttf}·{/font} 진공청소기의 술」 !!!!!!"

    ch_monica "큿……?! 꽤 하는구나, 니논!!!"

    ch_monica "하지만…… 질까 보냐!!!! 나는 평소에도 과자를 산처럼 쌓아 놓고 흡입하는 수련을 한다고!!!!!"

    ch_ninon "슈슈슈슈슛!!!!!"

    ch_monica "모니이이잇!!!!!"

    show highlight with dissolve

    ch_ninon "슈슈슈슛쓔슈슈슈슛!!!!!!!"

    ch_monica "모니이이이이이이이잇!!!!!!!!!"

    hide highlight

    player "……미안, 산짐승 맞는 것 같아."

    hide ob_moninon

    play music "audio/main/5orientalcommon.mp3"

    ## 유키 웃는 표정
    show stand_Yuki_yukata with dissolve

    ch_yuki "우리도 뭔가 먹자~ 나 정도의 아름다움을 유지하려면 제때제때 영양 공급을 잘 해 줘야 한다구."

    hide stand_Yuki_yukata

    ## 쿠우카 망상하는 표정
    show stand_Kuka_yukata_mousou with dissolve

    ch_kuka "영양 공급…… 도S 씨와…… 쿠헤헷……"

    hide stand_Kuka_yukata_mousou

    show stand_gura with dissolve

    ch_gura "그러시죠, 손님도 많이 없어서 재료가 남아도는 실정이니……"

    show bg_onsen at fast_rotating

    ch_gura "배가 빵빵해질 때까지 양껏 드십쇼-----옷!!!!!!"

    hide stand_gura
    ## 쿠우카 놀란 표정
    show stand_Kuka_yukata_surprised with dissolve

    ch_kuka "히이익……!!! 배, 배가 빵빵해질 때까지?!?!"

    show stand_Kuka_yukata
    hide stand_Kuka_yukata_surprised

    ch_kuka "머…… 먹는다는 게 그런 의미였나요!!!!"

    ch_nar "그런 의미가 뭔데……!!!"

    hide stand_Kuka_yukata

    player "음…… 저 둘은 알아서 잘 쳐먹……"

    player "아니…… 먼저 먹고 있으니까, 우리끼리 먹자."

    show stand_gura with dissolve

    ch_gura "그렇게 하시죠! 그러면 이걸……"

    hide stand_gura

    show ob_wagasi with dissolve:
        xpos 430 yalign 0.3
    
    ch_gura "오에도의 명물, 한정판 화과자 디럭스 세트임다----앗!!!!!!!!"

    player "오……"

    ch_yuki "꺄~ 예쁘다. 나보다는 아니지만~"

    ch_kuka "겨…… 경단들이 농후한 꿀에 흠뻑 절여진 채 서로의 몸을 탐하고 있어요……!!! 이 얼마나 상스러운… 케헤헤헷……!!"

    ch_gura "그럼, 맛있게 즐겨주시길 바랍니다!!"

    hide ob_wagasi
    hide bg_onsen

    if love_point == 1:
        show bg_black
        $renpy.pause(1.0)
        jump cg_ninonfirst
    elif love_point == 3:
        show bg_black
        $renpy.pause(1.0)
        jump cg_kukafirst
    else:
        show bg_black
        $renpy.pause(1.0)
        jump sceneNum16Common

    return
## S# 16. 온천 건물 내부 (식당) (공통 루트) ##
label sceneNum16Common:
    
    play music "audio/main/5orientalcommon.mp3"
    scene bg_naibu with fade

    show stand_gura with dissolve

    ch_gura "여러분, 식사는 맛있게 하셨습니까?"

    hide stand_gura

    show stand_Monica_yukata with dissolve

    ch_monica "음……! 굉장하더군…… 특히 그 꿀 바른 경단이 일품이었다……!!"

    hide stand_Monica_yukata

    show stand_gura with dissolve

    ch_gura "!!!!"

    ch_gura "……좀 더 자세히 말씀해 주실 수 있으신지요……?"

    hide stand_gura
    show bg_black with fade
    hide bg_naibu

    $renpy.pause(1.0)

    show bg_naibu with fade
    hide bg_black

    show stand_Monica_yukata at left with dissolve
    show stand_gura at right with dissolve

    ch_monica "……주목할 만했던 점은, 전체적으로 쫀득한 식감과 대비되는 부분이었는데…"

    ch_gura "호오, 호오……"

    show stand_Monica_yukata_surprised at left
    hide stand_Monica_yukata

    ch_monica "……거기에서 상상치도 못한 바삭한 견과류가……!!! 눈물이 나올 정도로 감동적인 맛이었다!!!"

    show bg_naibu at fast_rotating

    ch_gura "과연!!!!! 뭘 좀 아시는군요!!!! 감동임다{font=NanumGothic.ttf}——{/font}앗!!!!!!"

    ch_ayumi "저 둘, 즐거워 보이네요……"

    hide stand_Monica_yukata_surprised
    show stand_gura at movetocenter

    ch_gura "……아앗, 내 정신 좀 봐. 이런 지적인 대화는 너무 오랜만이라……!"

    ch_nar "지적이라기엔 쳐먹는 얘기밖에……"

    ch_gura "저희 온천의 요리를 사랑해주시는 것은 매우 기쁜 일이지만, 더 중요한 일을 깜빡할 뻔 했군요……"

    ch_gura "여러분께 드릴 물건이 있습니다."

    hide stand_gura
    show stand_Yuki_yukata with dissolve

    ch_yuki "물건? 나의 아름다움을 더 돋보이게 해 줄 수 있는 걸까나~?"

    hide stand_Yuki_yukata
    show stand_gura with dissolve

    ch_gura "……그, 그런 건 아니고요……"

    hide stand_gura
    $ persistent.clues_key = True
    show ob_key with dissolve:
        xpos 430 yalign 0.3
    
    play sound "audio/sound/surp.mp3"
    $ renpy.pause(1.0)
    
    ch_yuki "……뭐야, 이…… 극도로 아름답지 못한 건……"
    
    ch_gura "{b}쁘띠 구라노스케 마스터키 입니다.{/b}"

    ch_yuki "으으…… 흉측한 게 갑자기 눈에 들어와서…… 정신을…… 차릴 수가……"

    play sound "audio/sound/down.mp3"

    ch_ninon "유키 씨~~!!! 정신 차리세요 입니다~~~!!!!!"

    hide ob_key

    show stand_Monica_yukata_down with dissolve

    ch_monica "이…… 이게 대체 뭐지……?!"

    hide stand_Monica_yukata_down
    show stand_gura with dissolve

    ch_gura "문자 그대로, 온천의 잠긴 문을 모두 열 수 있는 ‘마스터키’입니다."

    ch_gura "아, 그리고 여기…… 하나 더 드리겠습니다."

    hide stand_gura
    show ob_key with dissolve:
        xpos 430 yalign 0.3
    
    ch_yuki "으으으으…… 흉물스러움이 2배로……"

    play sound "audio/sound/down.mp3"

    ch_ninon "유키 씨~~~!!!!"

    hide ob_key
    show stand_gura with dissolve

    ch_gura "이것을 여러분께 드리는 이유는……"

    ch_gura "지금까지는 손님을 접대한다는 명목으로 행동했지만, 앞으로도 여러분을 에스코트하며 온천 구석구석을 함께 돌아다니는 것은 아무래도 무리가 있을 것 같습니다."

    hide stand_gura
    show stand_Kuka_yukata_down with dissolve

    ch_kuka "그럼…… 이제부터는 저희의 힘만으로 조사를……?"

    hide stand_Kuka_yukata_down
    show stand_gura with dissolve

    ch_gura "네…… 이 이상 눈에 띄는 행동을 하는 건 위험할 것 같네요."

    ch_gura "{b}쁘띠 구라노스케 마스터키{/b}를 부디 잘 활용해 주시길 바라겠습니다."
    hide stand_gura

    player "그런데 이걸 두 개나 주는 이유는 뭐야……? 혹시라도 잃어버릴까 봐?"

    show stand_gura with dissolve

    ch_gura "다섯 분이시니까, 두 그룹으로 나누어 열쇠를 하나씩 가지고 다니시는 편이 효율적이라고 생각했습니다."

    ch_gura "그 정도면 불시의 위험에 대비하기도 적당한 인원일 것 같고요."

    hide stand_gura

    ch_ayumi "그러니까 다섯 명이 아니……"

    show stand_Ninon_yukata_daiji with dissolve

    ch_ninon "두 그룹이라면…… 어느 쪽이 쇼군과 함께 행동할지를 먼저 정해야 할 것 같군요 입니다……!"

    hide stand_Ninon_yukata_daiji

    show stand_Monica_yukata_ddung with dissolve

    ch_monica "음…… 잠깐 기다려라, 니논. 계획 없는 개별 행동은 혼란만을 야기할 뿐이야."

    ch_monica "온천의 내부 구조를 어느 정도 파악할 때까지는 전원이 함께 행동하는 것이 좋을 것 같다. 그룹을 나누는 것은 그 이후에 해도 늦지 않아."

    hide stand_Monica_yukata_ddung
    show stand_Ninon_yukata_surp with dissolve

    ch_ninon "그렇소 입니까…… 니논의 생각이 짧았다 입니다."

    hide stand_Ninon_yukata_surp

    show stand_Kuka_yukata with dissolve

    ch_kuka "그러면…… 어디부터 가는 게 좋을까요?"

    ch_kuka "아무래도 도S 씨가 정해 주시는 편이……"

    hide stand_Kuka_yukata

    player "으음……"

    player "……일단 숙소 쪽부터 둘러볼까?"

    show bg_white
    hide bg_naibu
    $ persistent.clue = True
    narrator "{color=#FF2929}단서{/color} 기능이 해금되었습니다!{vspace=15} \n이제부터 {color=#FF2929}화면 우측 상단의 톱니바퀴{/color} 또는 {color=#FF2929}ESC{/color}를 눌러 \n메뉴에 진입한 뒤 '{color=#FF2929}단서{/color}' 항목에서 수집한 단서들을 열람할 수 있습니다. "

    hide bg_white

    jump sceneNum17Common
## S# 17. 온천 숙소 - 리터칭 1 (공통루트) ####
label sceneNum17Common:
    scene bg_onsen_heya_03 with fade

    player "방이 생각보다 엄청 많네……"

    player "어느 세월에 다 돌지는 모르겠지만…… 여기부터 시작해 보자."

    show stand_Ninon_yukata_surp with dissolve

    ch_ninon "오오~! 뭔가 숨겨져 있을 것만 같은 곳 입니다~~!!!"

    hide stand_Ninon_yukata_surp

    show stand_Kuka_yukata_down with dissolve

    ch_kuka "니, 니논 씨…… 너무 큰 소리는 내지 않는 게 좋을 것 같은데요……!"

    hide stand_Kuka_yukata_down

    show stand_Ninon_yukata_panic with dissolve

    ch_ninon "합……! 큰일 날 뻔했다 입니다……"

    hide stand_Ninon_yukata_panic
    show stand_Yuki_yukata_ddung with dissolve

    ch_yuki "일단은 몰래 들어온 거니까…… 뭐, 차라리 마물이 우리를 알아보고 먼저 덤벼드는 편이 빠르고 편할지도 모르겠지만."

    hide stand_Yuki_yukata_ddung
    show stand_Monica_yukata_ddung with dissolve

    ch_monica "……구라노스케의 말에 따르면, 굉장히 영악한 놈이다. 그렇게 허술할 리가 없지……"

    hide stand_Monica_yukata_ddung
    show stand_Yuki_yukata_ddung with dissolve

    ch_yuki "어디까지나 희망사항일 뿐이라구."

    ch_yuki "하아…… 빨리 끝내고 돌아가서 쉬고 싶어…… 충분히 잠을 자 두지 않으면 피부가 다 상해 버릴 텐데."

    hide stand_Yuki_yukata_ddung
    show stand_Ninon_yukata with dissolve

    ch_ninon "걱정 마세요 입니다, 유키 씨. 니논의 NINJA SOUL에 따르면, 이 방에는 결정적인 단숴가 분명히 존재한다 입니다……!"

    ch_ninon "니논이 금방 놈의 행방을 알아내겠소 입니다. 조금만 기다려 주세요 입니다! 슈바바바밧!!"

    show afewmoment with fade
    play sound "audio/sound/AFEWMOMENTSLATER.mp3"
    hide bg_onsen_heya_03

    $renpy.pause(2.0)

    show bg_onsen_heya_03
    hide afewmoment

    show stand_Ninon_yukata_innocent with dissolve

    ch_ninon "닌자 관두겠소 입니다……"

    hide stand_Ninon_yukata_innocent

    show stand_Kuka_yukata with dissolve

    ch_kuka "뭐, 뭐어…… 이제 겨우 하나 조사했을 뿐이니까요……"

    hide stand_Kuka_yukata
    show stand_Monica_yukata with dissolve

    ch_monica "그래, 벌써부터 낙담하기엔 일러……! 조금만 더 힘을 내자, 제군들!"

    hide stand_Monica_yukata
    show sixmonths with fade
    hide bg_onsen_heya_03

    play sound "audio/sound/SixMonthsLater.mp3"

    $renpy.pause(2.0)

    hide sixmonths
    show bg_onsen_heya_02

    show stand_Monica_yukata_crying with dissolve
    ch_monica "어떻게 아무것도 없을 수가…… 조사한 방만 몇 개째인데……"

    hide stand_Monica_yukata_crying
    
    player "벌써 저녁때가 다 됐어…… 실화야?"

    show stand_Yuki_yukata_angry with dissolve

    ch_yuki "으으~ 너무 힘들어…… 정말이지 땀 흘리는 일은 질색……"

    show stand_Yuki_yukata_shamed
    hide stand_Yuki_yukata_angry

    ch_yuki "……이, 이럴수가……!!"

    ch_yuki "땀에 흠뻑 젖은 내 모습…… 그 어느 때보다 한층 더 아름다워……!! 너무나도 관능적이야…… 스스로에게 뇌쇄될 것만 같아……!! 꾸밈없이 흐트러진 모습을 하고 있어도 반짝반짝 빛이 난다니!! 아아~ 나도 나의 아름다움이 두려워……!!!"

    hide stand_Yuki_yukata_shamed

    player "……"

    player "근데…… 애초에 단서랄 게 있긴 한 걸까……?"

    player "이런 식이면 끝도 없을 것 같아……"

    show stand_Ninon_yukata_angry with dissolve

    ch_ninon "포기하면 안 돼요 입니다~! 포기는 배추를 셀 때와 이럴 때에 쓰는 말입니다!"

    hide stand_Ninon_yukata_angry

    ch_ayumi "그 말은 포기하라는……"

    stop music

    play sound "audio/sound/walking.mp3" loop
    $renpy.pause(1.0)

    play music "audio/main/emer.mp3"
    show stand_Ninon_yukata_panic with dissolve

    ch_ninon "!!!!"

    hide stand_Ninon_yukata_panic

    player "발자국 소리?!?!"

    show stand_Kuka_yukata_surprised with dissolve

    ch_kuka "저, 점점 가까워지고 있어요……!!"

    hide stand_Kuka_yukata_surprised

    show stand_Monica_yukata_ddung with dissolve

    ch_monica "이…… 이런 낭패가 있나. 마땅히 숨을 만한 곳도 없는데……!"

    hide stand_Monica_yukata_ddung

    player "뭐야……?! 망보던 사람이 아무도 없었어?!"

    show stand_Yuki_yukata_ddung with dissolve

    ch_yuki "망볼 틈이 어디 있어? 귀여운 내 얼굴만 감상하기에도 시간이 모자라!"

    hide stand_Yuki_yukata_ddung

    ch_ayumi "저…… 저는 선배만 보고 있느라……"

    ch_ayumi "~~~가 아니라!!! 선배가 딱히 아무 말씀 없으셔서……!"

    ch_nar "이런 멍청이들……!!!"

    show stand_Ninon_yukata_angry with dissolve

    ch_ninon "이익…… 일단 니논이 상황을 파악하겠다 입니다!!"

    show stand_Ninon_yukata_daiji
    hide stand_Ninon_yukata_angry

    ch_ninon "가는 겁니다~~!! 「인법 {font=NanumGothic.ttf}·{/font} 천뤼안」 !!!! 츄츄츄!!!!"

    player "천리안?! 벽 너머를 볼 수 있는 거야?!"

    ch_ninon "그냥 문 틈쇄로 바깥을 내다보는 인법 입니다!!!"

    ch_nar "인법도 뭣도 아니잖아……!!"

    ch_ninon "취취췻{font=NanumGothic.ttf}——{/font}!!!!"

    ch_ninon "이것은 입에서 나는 소리가 아니여 입니다!!"

    $renpy.pause(1.0)

    ch_ninon "푸취췻{font=NanumGothic.ttf}—{/font} 발소리의 주인은……"

    ch_ninon "사람…… 사람 입니다!"

    ch_ninon "옷차림으로 봐선, 아마도 온천의 직원……!!"

    hide stand_Ninon_yukata_daiji    

    show stand_Monica_yukata_surprised with dissolve

    ch_monica "겉모습만으로는 판단할 수 없어……! 직원의 모습을 흉내낸 마물일지도 모른다!"

    hide stand_Monica_yukata_surprised

    show stand_Kuka_yukata_surprised with dissolve

    ch_kuka "그, 그럼…… 이제 어떡해야……!!!"

    hide stand_Kuka_yukata_surprised

    player "……"

    player "……나한테 좋은 생각이 있어."

    player "다들, 내가 시키는 대로만 해 줘……!"

    show bg_black with fade
    hide bg_onsen_heya_02

    stop music
    stop sound

    $renpy.pause(1.0)

    show bg_onsen_heya_02 with fade
    hide bg_black

    show npc_1 with dissolve

    ch_syokuin "……응?"

    ch_syokuin "어라, 이상하다……?"

    ch_syokuin "문이 왜 열려 있지? 좀 전까지만 해도 잠겨……"

    hide npc_1
    show cg_babybung with dissolve

   
    play sound "audio/sound/surp.mp3"

    play music "audio/main/11fun.mp3"

    player "{b}{size=30}응애!!!!!!!!!!!{/size}{/b}"

    hide cg_babybung
    show npc_1 with dissolve
    show bg_onsen_heya_02 with hpunch

    ch_syokuin "꺄{font=NanumGothic.ttf}———{/font}아아악?!!!?!!!!!"

    show npc_1 at movetoleft

    show cg_babybung at right with dissolve

    player "테에엥!!! 마망!!!!"

    ch_syokuin "어, 어린아이……?"

    ch_syokuin "근데 생긴 게……"

    player "싸…… 싸물응애……!"

    ch_syokuin "어……린애…… 맞겠지……?"

    ch_syokuin "길을 잃은 거니? 엄마는 어디 계셔?"

    player "응애…… 맘마조……"

    ch_syokuin "곤란하네…… 여기 있으면 안 돼요. 일단 누나랑 같이 가자."

    player "테에에엥……"

    hide cg_babybung
    hide npc_1

    play music "audio/main/11fun.mp3"

    $renpy.pause(1.0)

    show stand_Monica_yukata_munen with dissolve:
        xpos 200 ypos 250
    
    ch_monica "……갔나?"

    hide stand_Monica_yukata_munen
    show stand_Ninon_yukata_surp with dissolve:
        xpos 200 ypos 250
    ch_ninon "간 것 같아요 입니다……"

    hide stand_Ninon_yukata_surp

    ch_ayumi "선배…… 고생이란 고생은 다 하시네요오……"

    show stand_Yuki_yukata_angry with dissolve:
        xpos 200 ypos 250
    
    ch_yuki "……저기, 그럼 일단 어디로든 이동하지 않을래? 너무 답답해……"

    hide stand_Yuki_yukata_angry
    show stand_Kuka_yukata_mousou with dissolve:
        xpos 200 ypos 250
    
    ch_kuka "쿠…… 쿠우카는 이대로도 나쁘지 않아요……! 마구 짓눌리는 이 느낌이 엄청……!! 케헷, 케…… 헤으극……!!!"

    $ persistent.clues_syokuin = True
    show screen clueFinded
    hide stand_Kuka_yukata_mousou
    $renpy.pause(1.0)
    hide bg_onsen_heya_02

    if love_point == 1 or love_point == 3:
        jump scene18_1
    else:
        jump scene18_2
## S# 18-1. 실내 온천 (니논, 쿠우카 루트) #########
label scene18_1:
    scene bg_indoor_onsen
    
    play music "audio/main/5orientalcommon.mp3"

    show stand_Ninon_yukata_emb with dissolve

    ch_ninon "휴우우…… 좀 전에는 정말 깜짝 놀랐다데스 였습니다……!!"

    hide screen clueFinded
    hide stand_Ninon_yukata_emb
    show stand_Kuka_yukata with dissolve

    ch_kuka "굉…… 굉장히 좋은 경험이었어요……"

    show stand_Kuka_yukata_mousou
    hide stand_Kuka_yukata

    ch_kuka "자그마한 숨소리조차도 허용되지 않는 위태로운 상황…… 절대 들어갈리 없는 좁은 공간에 쿠우카의 신체가 억지로 구겨 넣어지자……!!"

    ch_kuka "그 순간의…… 답답하고 숨 막히는 긴장감……!!! 마치 굵직한 동아줄에 온몸이 결박된 채, 비좁고 냄새나는 지하 창고에 곧바로 처박힌 듯한 그 느낌!!!! 쿠우카의 ‘엑스터시 모멘트’ 탑 3 안에 들어갈 정도였어요……!!! 쿠후훗…… 쿠헤헤헤헷!!!!"

    hide stand_Kuka_yukata_mousou
    if love_point == 3:
        
        player "……나머지 2개는 뭔데……?"

        show stand_Kuka_yukata_mousou with dissolve

        ch_kuka "……에?"

        show stand_Kuka_yukata_shamed
        hide stand_Kuka_yukata_mousou

        ch_kuka "여…… 여기서 말해야만 하는 건가요……?"

        ch_kuka "으으……"

        ch_kuka "……하나는 좀 전에, 쿠우카의 허리가 도S 씨에게 억지로 붙들린 채…… 뜨겁고 거친 숨결이 쿠우카의 목덜미에 닿았을 때……"

        hide stand_Kuka_yukata_shamed
        show stand_Ninon_yukata_daiji with dissolve

        ch_ninon "……"

        hide stand_Ninon_yukata_daiji
        show stand_Kuka_yukata_shamed with dissolve

        ch_kuka "다, 다른 하나는…… 도S 씨를   {nw}"

        stop music
        hide stand_Kuka_yukata_shamed
        show stand_Ninon_yukata_daiji with dissolve

        ch_ninon "{b}{size=30}동작 그만.{/size}{/b}"

        ch_ninon "{b}{size=30}여기 놀러 왔습니까?{/size}{/b}"

        player "다…… 단서 찾으러 왔지……"

        ch_ninon "{b}{size=30}그럼 잔말 말고 일이나 하세요 입니다.{/size}{/b}"

        hide stand_Ninon_yukata_daiji
        show stand_Kuka_yukata with dissolve

        ch_kuka "히이이……!!"
        hide stand_Kuka_yukata
        ## 동양풍 브금 서서히 커짐
        play music "audio/main/5orientalcommon.mp3" fadein 3.0

    show stand_Ninon_yukata with dissolve

    ch_ninon "……그나저나 쇼군, 그 순간에 어떻게 그런 기쥐를……! 정말 대단하오 입니다~!!"

    hide stand_Ninon_yukata

    player "하하…… 뭘……"

    if love_point == 1:

        player "……니논이 잘해 준 덕분이지……"

        show stand_Ninon_yukata_innocent with dissolve

        ch_ninon "……"

        ch_ninon "……실은…… 댑따 엄청 부끄러웠소 입니다……"

        hide stand_Ninon_yukata_innocent

        show bg_black with fade
        hide bg_indoor_onsen

        ch_nar "조금 전……"

        show bg_onsen_heya_02 with fade
        hide bg_black

        
        play music "audio/main/emer.mp3"

        show stand_Ninon_yukata_panic with dissolve

        ch_ninon "……네에……?! 너, 너무 위험해요 입니다……!!! 게다가……"

        hide stand_Ninon_yukata_panic
        show stand_Monica_yukata_ddung with dissolve

        ch_monica "그…… 그렇지만, 지금으로선 그 방법이 최선일 것 같군……! 부탁한다, 귀공!!"

        hide stand_Monica_yukata_ddung
        show stand_Kuka_yukata_surprised with dissolve

        ch_kuka "도S 씨, 아무리 그래도 그건……?! 도, 도M 씨가 되어버린 건가요?!?!"

        hide stand_Kuka_yukata_surprised

        player "실랑이할 시간 없어! 바로 간다!!"

        player "……니논, 뒤를 부탁한다……!!"


        show stand_Ninon_yukata_innocent with dissolve

        ch_ninon "으…… 윽, 긋……"

        ch_syokuin "……응?"

        ch_syokuin "어라, 이상하다……?"

        ch_ninon "쇼…… 쇼군을 위해서라면…… 이 정도 쉬련쯤은……!!"

        player "응애!!!!!!!!!!!"

        ch_syokuin "꺄{font=NanumGothic.ttf}———{/font}아아악?!!!?!!!!!"

        hide stand_Ninon_yukata_innocent

        show bg_black
        $renpy.pause(1.0)

        stop music fadeout 3.0
        show bg_naibu with fade
        hide bg_black

        play music "audio/main/11fun.mp3"

        show cg_babybung with dissolve

        player "테에엥……"

        hide cg_babybung

        show stand_Ninon_yukata_emb with dissolve

        ch_ninon "……"

        hide stand_Ninon_yukata_emb
        show stand_Monica_yukata_munen with dissolve

        ch_monica "……니, 니논……! 지금 바로 가야 한다……!!"

        hide stand_Monica_yukata_munen
        show stand_Ninon_yukata_emb with dissolve

        ch_ninon "아…… 알겠소 입니다. 그, 그렇쥐만……"

        show stand_Ninon_yukata_innocent
        hide stand_Ninon_yukata_emb

        ch_ninon "이, 이건 너무…… 하즈카쉬이 DEATH 입니다……!!"

        hide stand_Ninon_yukata_innocent

        show cg_babybung with dissolve

        player "마망, 마망……!!"

        hide cg_babybung
        show npc_1 with dissolve

        ch_syokuin "이 아이, 엄마가 없는 걸까……?"

        hide npc_1
        show cg_babybung with dissolve

        player "패…… 패드립응앵……"

        hide cg_babybung
        show stand_Ninon_yukata_emb with dissolve

        ch_ninon "……"

        ch_ninon "……저기……"

        hide stand_Ninon_yukata_emb
        show npc_1 with dissolve

        ch_syokuin "아, 네! 손님, 무엇을 도와드릴까요?"

        hide npc_1
        show stand_Ninon_yukata_innocent with dissolve

        ch_ninon "……그……"

        ch_ninon "그 아이……"

        hide stand_Ninon_yukata_innocent
        show npc_1 with dissolve

        ch_syokuin "네?"

        hide npc_1

        show stand_Ninon_yukata_innocent with dissolve

        ch_ninon "그…… 저…… Umm……"

        hide stand_Ninon_yukata_innocent
        show cg_babybung with dissolve

        player "……빨리응애……!"

        hide cg_babybung
        show npc_1 with dissolve

        ch_syokuin "손님, 대단히 죄송합니다만…… 다시 한 번 말씀해 주시겠어요?"

        hide npc_1
        show stand_Ninon_yukata_innocent with dissolve

        ch_ninon "…………"

        $renpy.pause(1.0)

        show stand_Ninon_yukata_emb with dissolve
        hide stand_Ninon_yukata_innocent

        ch_ninon "{b}{size=30}제가 그 아이의 마망 입니다~~~~!!!!!{/size}{/b}"

        hide stand_Ninon_yukata_emb
        show cg_babybung with dissolve
        show bg_naibu with hpunch

        player "마망!!!! 마망~~~!!!!!"

        hide cg_babybung

        show npc_1 with dissolve

        ch_syokuin "어머……!"

        hide npc_1
        show stand_Ninon_yukata_innocent with dissolve

        ch_ninon "그, 긋…… 그, 그러니까…… 그, 그 아이는 제가 데려가겠소 입니다……!"

        hide stand_Ninon_yukata_innocent
        show npc_1 with dissolve

        ch_syokuin "이 아이, 엄마를 애타게 찾고 있었는데…… 정말 다행이에요……!"

        hide npc_1
        show cg_babybung with dissolve

        player "마망~~!!!!"

        hide cg_babybung
        show stand_Ninon_yukata_emb with dissolve

        ch_ninon "그…… 호…… 혼자서 많이 무서웠습니다……? 가 아니고…… 무서웠지 입니다……? 아니 아니……"

        hide stand_Ninon_yukata_emb
        show bg_naibu onlayer middle
        show cg_babybung onlayer forward with dissolve
        $ camera_move(0, 0, 400, 0, 1)

        player "……!!"
        hide cg_babybung onlayer forward
        $ camera_move(0, 0, 0, 0, 0)
        show stand_Ninon_yukata_emb onlayer forward with dissolve

        $ camera_move(0, -1000, 400, 0, 1)
        ch_ninon "……!!!"

        hide stand_Ninon_yukata_emb onlayer forward
        $ camera_move(0, 0, 0, 0, 0)
        show cg_babybung onlayer forward

        $ camera_move(0, 0, 400, 0, 1)
        
        play sound "audio/sound/surp.mp3"

        show highlight onlayer forward with dissolve
        player "{b}{size=30}맘마조!!!!!{/size}{/b}"

        hide cg_babybung onlayer forward

        $ camera_move(0, 0, 0, 0, 0)

        show stand_Ninon_yukata_innocent onlayer forward with dissolve

        $ camera_move(0, -1000, 400, 0, 1)
        
        play sound "audio/sound/surp.mp3"

        ch_ninon "{b}{size=30}어…… 엄마랑 맘마 먹으러 가자용용~~가리!!!!!!{/size}{/b}"

        hide stand_Ninon_yukata_innocent onlayer forward

        $ camera_move(0, 0, 0, 0, 0)

        show bg_black
        hide highlight onlayer forward
        hide bg_naibu onlayer middle

        $renpy.pause(1.5)

        show bg_indoor_onsen with fade
        hide bg_black

        player "응…… 니논이 아니었다면, 자연스럽게 빠져나오지 못했을 거야……"

        show stand_Ninon_yukata_innocent with dissolve

        ch_ninon "쇼군을 위해서라지만…… 이런 일…… 다쉬는 하고 싶지 않아요 입니다…"

        hide stand_Ninon_yukata_innocent

    else:
        player "……쿠우카가 잘해 준 덕분이지……"

        show stand_Kuka_yukata_shamed with dissolve

        ch_kuka "……"

        ch_kuka "그, 그 기억을…… 다시 떠올리게 하시다니……"

        show stand_Kuka_yukata_mousou
        hide stand_Kuka_yukata_shamed

        ch_kuka "이…… 이렇게까지 다양한 방법으로 쿠우카를 학대할 수 있는 사람은…… 이 세상에 도S 씨 말고는 아무도 없을 거예요……!! 쿠후후후훗!!!"

        hide stand_Kuka_yukata_mousou

        show bg_black with fade
        hide bg_indoor_onsen

        ch_nar "조금 전……"

        show bg_onsen_heya_02 with fade
        hide bg_black

        
        play music "audio/main/emer.mp3"

        show stand_Kuka_yukata_surprised with dissolve

        ch_kuka "……네에……?! 도S 씨, 아무리 그래도 그건……?! 도, 도M 씨가 되어버린 건가요?!?!"

        hide stand_Kuka_yukata_surprised

        show stand_Monica_yukata_ddung with dissolve

        ch_monica "그…… 그렇지만, 지금으로선 그 방법이 최선일 것 같군……! 부탁한다, 귀공!!"

        hide stand_Monica_yukata_ddung

        show stand_Ninon_yukata_panic with dissolve

        ch_ninon "지…… 진짜로 하는 건가요 입니다……?!"

        hide stand_Ninon_yukata_panic

        player "실랑이할 시간 없어! 바로 간다!!"

        player "……쿠우카, 뒤를 부탁한다……!!"

        show stand_Kuka_yukata_shamed with dissolve

        ch_kuka "으으…… 도, 도S 씨는 정말이지……"

        ch_syokuin "……응?"

        ch_syokuin "어라, 이상하다……?"

        show stand_Kuka_yukata_mousou
        hide stand_Kuka_yukata_shamed

        ch_kuka "……세계 최고의 사디스트가 분명해요……!!! 쿠헷…… 쿠헤헤헤헷……!!!"

        player "응애!!!!!!!!!!!"

        ch_syokuin "꺄{font=NanumGothic.ttf}———{/font}아아악?!!!?!!!!!"

        hide stand_Kuka_yukata_mousou

        show bg_black
        hide bg_onsen_heya_02
        $renpy.pause(1.0)
        stop music fadeout 3.0

        show bg_naibu with fade
        hide bg_black

        play music "audio/main/11fun.mp3"

        show cg_babybung with dissolve

        player "테에엥……"

        hide cg_babybung

        show stand_Kuka_yukata_shamed with dissolve

        ch_kuka "……"

        hide stand_Kuka_yukata_shamed

        show stand_Monica_yukata_munen with dissolve

        ch_monica "……쿠, 쿠우카……! 지금 바로 가야 한다……!!"

        hide stand_Monica_yukata_munen
        show stand_Kuka_yukata_mousou with dissolve

        ch_kuka "이건…… 단 한 번도 경험해 본 적 없는 종류의 수치심이에요……!!! 케헷, 케헤헤헤헤헥!!!!!!"

        hide stand_Kuka_yukata_mousou

        show cg_babybung with dissolve

        player "마망, 마망……!!"

        hide cg_babybung

        show npc_1 with dissolve

        ch_syokuin "이 아이, 엄마가 없는 걸까……?"

        hide npc_1
        show cg_babybung with dissolve

        player "패…… 패드립응앵……"

        hide cg_babybung
        show stand_Kuka_yukata_shamed with dissolve

        ch_kuka "……"

        ch_kuka "……저, 저기……"

        hide stand_Kuka_yukata_shamed
        show npc_1 with dissolve

        ch_syokuin "아, 네! 손님, 무엇을 도와드릴까요?"

        hide npc_1
        show stand_Kuka_yukata_shamed with dissolve

        ch_kuka "……그……"

        ch_kuka "그 아이……"

        hide stand_Kuka_yukata_shamed
        show npc_1 with dissolve

        ch_syokuin "네?"

        hide npc_1
        show stand_Kuka_yukata_shamed with dissolve

        ch_kuka "그…… 저어……"

        hide stand_Kuka_yukata_shamed
        show cg_babybung with dissolve

        player "……빨리응애……!"

        hide cg_babybung
        show npc_1 with dissolve

        ch_syokuin "손님, 대단히 죄송합니다만…… 다시 한 번 말씀해 주시겠어요?"

        hide npc_1
        show stand_Kuka_yukata_shamed with dissolve

        ch_kuka "…………"

        $renpy.pause(1.0)

        show stand_Kuka_yukata_mousou
        hide stand_Kuka_yukata_shamed

        ch_kuka "{b}{size=30}제, 제가 그 아이의 엄마 입니다아~~~~!!!!!{/size}{/b}"

        hide stand_Kuka_yukata_mousou

        show cg_babybung with dissolve

        player "마망!!!! 마망~~~!!!!!"

        hide cg_babybung
        show npc_1 with dissolve

        ch_syokuin "어머……!"

        hide npc_1
        show stand_Kuka_yukata_mousou with dissolve

        ch_kuka "그, 긋…… 하으…… 그러니까…… 하앗, 하아……"

        ch_kuka "그, 그 아이는…… 헤윽…… 제가 데려……갈게요……! 하아아……"

        hide stand_Kuka_yukata_mousou

        show npc_1 with dissolve

        ch_syokuin "이 아이, 엄마를 애타게 찾고 있었는데…… 정말 다행이에요……!"

        hide npc_1

        show cg_babybung with dissolve

        player "마망~~!!!!"

        hide cg_babybung

        show stand_Kuka_yukata_shamed with dissolve

        ch_kuka "그…… 호…… 혼자서 많이 무서웠죠……? 아, 이…… 이렇게 말하면 안 되나……? 그……"

        hide stand_Kuka_yukata_shamed

        show bg_naibu onlayer middle
        show cg_babybung onlayer forward with dissolve
        $ camera_move(0, 0, 400, 0, 1)

        player "……!!"
        hide cg_babybung onlayer forward
        $ camera_move(0, 0, 0, 0, 0)
        show stand_Kuka_yukata_shamed onlayer forward with dissolve

        $ camera_move(0, -1000, 400, 0, 1)
        ch_kuka "……!!!"

        hide stand_Kuka_yukata_shamed onlayer forward
        $ camera_move(0, 0, 0, 0, 0)
        show cg_babybung onlayer forward

        $ camera_move(0, 0, 400, 0, 1)
        
        play sound "audio/sound/surp.mp3"

        show highlight onlayer forward with dissolve
        player "{b}{size=30}맘마조!!!!!{/size}{/b}"

        hide cg_babybung onlayer forward

        $ camera_move(0, 0, 0, 0, 0)

        show stand_Kuka_yukata_mousou onlayer forward with dissolve

        $ camera_move(0, -1000, 400, 0, 1)
        
        play sound "audio/sound/surp.mp3"

        ch_ninon "{b}{size=30}어…… 엄마랑 맘마 먹으러 갈까요오~~~!!!!!!{/size}{/b}"

        hide stand_Kuka_yukata_mousou onlayer forward

        $ camera_move(0, 0, 0, 0, 0)

        show bg_black
        hide highlight onlayer forward
        hide bg_naibu onlayer middle

        $renpy.pause(1.5)

        show bg_indoor_onsen with fade
        hide bg_black

        player "응…… 쿠우카가 아니었다면, 절대 자연스럽게 빠져나오지 못했을 거야……"

        show stand_Kuka_yukata_mousou with dissolve

        ch_kuka "크흣, 쿠후헤헤헷…… 책임 없는 쾌락도 아니고…… 쾌락 없는 책임이라는 변태적 발상……!! 도S 씨는 정말…… 사고체계부터가 말로 형용할 수 없을 정도로 심각하게 어긋나 있네요!!! 케헷, 케게게게……!!!"

        hide stand_Kuka_yukata_mousou
  
    play music "audio/main/5orientalcommon.mp3"

    player "……아무튼 잘 해결됐으니까 대충 넘어가자……"

    player "그건 그거고, 이제부터 열심히 단서를 찾아보자구."

    show stand_Ninon_yukata_wink with dissolve

    ch_ninon "OUI~~!!! 눈에 흙이 들어가기 전까지 단서를 찾아내고 말겠소 입니다!!"

    hide stand_Ninon_yukata_wink
    show stand_Kuka_yukata with dissolve

    ch_kuka "그, 그건 이럴 때 쓰는 속담은 아닌 것 같아요……"

    ch_kuka "그나저나 다른 분들은 잘 하고 계시려나요……? 얼떨결에 팀이 나눠져서 많이 혼란스러울 텐데……"

    hide stand_Kuka_yukata

    player "모니카랑 유키……라면 뭐……"

    player "어떻게든 될 조합인 것 같은데. 어련히 잘 하겠지."

    show stand_Ninon_yukata_down with dissolve

    ch_ninon "그런데 숙소 쪽은 어떻게 하실 생각인가요 입니다? 이대로 포기하는 겁니까?"

    hide stand_Ninon_yukata_down

    player "당장은 위험하니까 어쩔 수 없지…… 욕탕 조사가 끝나는대로 숙소 쪽도 다시 살펴 보자."

    player "저녁이나 밤 정도가 되면 직원들도 안 돌아다니지 않을까?"

    show stand_Ninon_yukata with dissolve

    ch_ninon "좋은 생각이네요 입니다! 그러면 온천부터 샅사취 뒤져보자 입니다~!"

    hide stand_Ninon_yukata

    show stand_Kuka_yukata with dissolve

    ch_kuka "쿠…… 쿠우카도, 열심히 돕겠습니다……!!"

    hide stand_Kuka_yukata

    $renpy.pause(1.0)

    ch_ayumi "지이이이……"

    show bg_black with fade
    hide bg_indoor_onsen

    $renpy.pause(1.0)

    show bg_indoor_onsen
    hide bg_black

    show stand_Ninon_yukata_angry with dissolve

    ch_ninon "읏……차 입니다. 여기가 마지막이니까……"

    show stand_Ninon_yukata_down
    hide stand_Ninon_yukata_angry

    ch_ninon "안타깝쥐만, 이곳에도 단서는 없는 것 같네요 입니다……"

    hide stand_Ninon_yukata_down
    
    player "또 허탕인가……"

    show stand_Kuka_yukata_down with dissolve

    ch_kuka "쉽지 않네요……"

    hide stand_Kuka_yukata_down
    show stand_Ninon_yukata with dissolve

    ch_ninon "그취만 아직 찾을 곳은 많이 남아 있다 입니다. 힘내 보아요 입니다~!"

    hide stand_Ninon_yukata

    player "그래…… 그럼 이 다음은……"

    player "{b}{size=30}……뭐야 이거?!{/size}{/b}"

    show stand_Ninon_yukata_surp with dissolve:
        easeout 0.3 ypos -50
        ease 0.2 ypos 50
        easeout 0.3 ypos -50
        ease 0.2 ypos 50 
        ## 팔짝
    
    ch_ninon "Waouh!!!! 왜, 왜 그러시나요 입니다?!!"

    hide stand_Ninon_yukata_surp
    show stand_Kuka_yukata with dissolve

    ch_kuka "괘…… 괜찮아요, 도S 씨!! 원래 이 나이대 남자아이들은 길을 걷다가도 갑자기 불끈불끈하게 되는 것이 정상……"

    hide stand_Kuka_yukata

    player "미…… 미친 소리 하지 말고, 이걸 봐!"

    show ob_unagi with dissolve:
        xpos 430 yalign 0.3
    
    ch_kuka "이건……?"

    ch_ninon "이것은…… 장어구이 입니다!"

    ch_kuka "장어라면……! 남자한테 참 좋은데, 어떻게 표현할 방법이 없는 그거……?!"

    ch_kuka "그, 그런데 왜 바닥에 떨어져 있는 걸까요……? 뭔가 섬뜩하네요……"

    ch_ninon "이빨 자국이 있다 입니다…… 누가 먹다가 떨군 거 아닐까요 입니다?"

    player "이거, 자세히 보니…… 먼지가 내려앉아 있네."

    player "그 말은…… 좀 오래 된 거라는 뜻인데…… 이쪽은 청소하는 직원이 없나?"

    $renpy.pause(1.0)

    player "……없을리가 없지!!!"

    player "단서다{font=NanumGothic.ttf}——{/font}!!!!"

    hide ob_unagi
    show stand_Kuka_yukata_surprised with dissolve

    ch_kuka "네에……? 장어구이가 단서……?"

    hide stand_Kuka_yukata_surprised
    show stand_Ninon_yukata_angry with dissolve

    ch_ninon "혼자만 알고 있지 말고 설명해 주세요 입니다~!!"

    hide stand_Ninon_yukata_angry

    player "장어구이 조각이 복도 한복판에 대놓고 떨어져 있었다는 점……"

    player "그럼에도 먼지가 쌓일 때까지 치우지 않았다는 점, 그 말은……"

    ## 단서 발견 효과음

    player "이곳을 청소하던 직원이…… 사라졌다는 것이다……!"

    ch_ayumi "……그 정도는 누구나 생각해 낼 수 있는……"

    show stand_Ninon_yukata_surp with dissolve

    ch_ninon "NARUHODO!!! 상상도 못했다 입니다!!!!"

    hide stand_Ninon_yukata_surp

    ch_ayumi "……"

    show stand_Ninon_yukata_surp with dissolve

    ch_ninon "그렇다면 쇼군은 이빨 자국의 주인에 대한 추리도 끝마친 거군요 입니다?!"

    hide stand_Ninon_yukata_surp

    player "????"

    player "무, 물론이지……!"

    ch_nar "뭔 소리야……? 그딴 걸 내가 어떻게 알아?"

    show stand_Ninon_yukata_daiji with dissolve

    ch_ninon "어쩐쥐 이상하더라니……!"

    ch_ninon "욕탕에는 음식물 반입이 금지되어 있다 입니다. 굳이 여기까지 장어구이를 가져와서 먹을 이유가 전혀 없소 입니다……!"

    ch_ninon "그렇다면, 장어구이를 야무쥐게 한 입 베어 먹은 주인공은……"

    ch_ninon "{b}다리를 쩍 벌린 채로 지하철 좌석을 세 자리나 차지하고 앉아 있는 주제에 누군가 그것을 지적하면 적반하장으로 어린노무쉐리가 어쩌고 시끄럽게 소리를 지르며 가르치려 드는 부류의 술 냄새 나는 배불뚝이 아저씨처럼, 온천의 규정을 깡그리 무시하며 남들이 쳐다보든 말든 신경도 쓰지 않고 욕탕에서 장어를 뜯던 정신병자이거나……{/b}"

    hide stand_Ninon_yukata_daiji
    show stand_Kuka_yukata_mousou with dissolve

    ch_kuka "묘, 묘사가 쓸데없이 구체적이라서 화가 치밀어 올라요……!!"

    hide stand_Kuka_yukata_mousou
    show bg_indoor_onsen onlayer middle with dissolve
    show stand_Ninon_yukata_daiji onlayer forward with dissolve

    ch_ninon "그것도 아니라면……"

    ch_ninon "……여기를 청소하던 직원을 사라지게 만든 마물일 겁니다……!!"

    ch_nar "어……? 그렇게 되나……?"

    ch_ninon "그렇지만, 전자의 배불뚜기 아조쉬는 사실상 말이 안 되는 가정이므로……"

    show highlight onlayer forward with dissolve
    $ camera_move(0, -1000, 400, 0, 1)

    ch_ninon "범인은 사람이 아니라, 마물……!!"

    ch_nar "그…… 그런가……? 듣고 보니 그런 거 같기도……"

    show stand_Ninon_yukata onlayer forward
    hide stand_Ninon_yukata_daiji onlayer forward
    $ camera_move(0, 0, 0, 0, 0)
    show stand_Ninon_yukata
    hide stand_Ninon_yukata onlayer forward
    hide highlight onlayer forward
    hide bg_indoor_onsen onlayer middle

    ch_ninon "장어구이 조각을 보고 여기까지 추리하시다니…… 쇼군은 정말 굉장해요 입니다!!!"

    hide stand_Ninon_yukata
    
    player "이…… 이 정도는 별 거 아니지……!"

    show stand_Kuka_yukata_down with dissolve

    ch_kuka "……저기, 그런데……"

    ch_kuka "장어구이를 베어 먹은 게 마물이라는 결론은 어떻게 나온 건가요……?"

    hide stand_Kuka_yukata_down

    show stand_Ninon_yukata_daiji with dissolve

    ch_ninon "사람이 아니니까요."

    hide stand_Ninon_yukata_daiji
    show stand_Kuka_yukata_hiku with dissolve

    ch_kuka "???"

    hide stand_Kuka_yukata_hiku
    show stand_Ninon_yukata_daiji with dissolve

    ch_ninon "하아…… 쿠우카 씨. 사람이 아니라면 마물의 짓인 게 당연하지 않습니까?"

    hide stand_Ninon_yukata_daiji
    show stand_Kuka_yukata_hiku with dissolve

    ch_kuka "……"

    hide stand_Kuka_yukata_hiku
    
    ch_ayumi "그냥 개소리잖……"

    show stand_Kuka_yukata_surprised with dissolve

    ch_kuka "그렇군요……!!! 세상에!!"

    hide stand_Kuka_yukata_surprised

    ch_nar "와…… 진짜 똑똑하다……"

    ch_ayumi "단체로 맛이 간 것 같아요……"

    $ persistent.clues_unagi = True
    show screen clueFinded
    $renpy.pause(1.0)
    show bg_black with fade
    hide bg_indoor_onsen

    jump scene19_1
## S# 18-2. 실내 온천 (모니카, 유키 루트) #########
label scene18_2:
    scene bg_indoor_onsen
    
    play music "audio/main/5orientalcommon.mp3"

    show stand_Monica_yukata_down with dissolve

    ch_monica "휴우…… 좀 전에는 정말, 꼼짝없이 들키는 줄만 알았다……"
    hide screen clueFinded
    hide stand_Monica_yukata_down
    show stand_Yuki_yukata with dissolve

    ch_yuki "……그나저나 [name]도 제법인걸~? 그 짧은 순간에 그런 임기응변을 해낼 줄이야……"

    hide stand_Yuki_yukata
    
    player "하하…… 뭘……"

    if love_point == 2:

        player "……모니카가 잘해 준 덕분이지……"

        show stand_Monica_yukata_dere with dissolve

        ch_monica "……"

        ch_monica "……겨우…… 겨우 진정이 된 참인데…… 귀공은 정말이지……!"

        hide stand_Monica_yukata_dere

        show bg_black with fade
        hide bg_indoor_onsen
        
        stop music fadeout 3.0

        ch_nar "조금 전……"

        show bg_onsen_heya_02
        hide bg_black

        
        play music "audio/main/emer.mp3"

        show stand_Monica_yukata_dere with dissolve

        ch_monica "……뭐어……?! 그, 그건 너무 위험하다!! 게다가……"

        hide stand_Monica_yukata_dere

        show stand_Ninon_yukata_angry with dissolve

        ch_ninon "그…… 그렇지만, 당장은 그 방법이 최선일 것 같아요 입니다……!"

        hide stand_Ninon_yukata_angry
        show stand_Kuka_yukata_surprised with dissolve

        ch_kuka "도S 씨, 아무리 그래도 그건……?! 도, 도M 씨가 되어버린 건가요?!?!"

        hide stand_Kuka_yukata_surprised

        player "실랑이할 시간 없어! 바로 간다!!"

        player "……모니카, 뒤를 부탁한다……!!"

        show stand_Monica_yukata_dere with dissolve

        ch_monica "윽…… 그읏……"

        hide stand_Monica_yukata_dere

        ch_syokuin "……응?"

        ch_syokuin "어라, 이상하다……?"

        show stand_Monica_yukata_crying with dissolve

        ch_monica "나…… 나 보고 그런 걸…… 어떻게 하라는 말이냐아아~~!!"

        player "응애!!!!!!!!!!"

        ch_syokuin "꺄{font=NanumGothic.ttf}———{/font}아아악?!!!?!!!!!"

        hide stand_Monica_yukata_crying
        show bg_black
        $renpy.pause(1.0)
        stop music fadeout 3.0

        show bg_naibu with fade
        hide bg_black

        play music "audio/main/11fun.mp3"

        show cg_babybung with dissolve

        player "테에엥……"

        hide cg_babybung
        show stand_Monica_yukata_dere with dissolve

        ch_monica "……"

        hide stand_Monica_yukata_dere
        show stand_Ninon_yukata_angry with dissolve

        ch_ninon "……모니카 씨……! 지금 바로 가야 합니다……!!"

        hide stand_Ninon_yukata_angry
        show stand_Monica_yukata_dere with dissolve

        ch_monica "아…… 알고 있다……! 그, 그렇지만……"

        show stand_Monica_yukata_crying with dissolve
        hide stand_Monica_yukata_dere

        ch_monica "이, 이런 건 너무…… 너무 부끄러워……!!"

        hide stand_Monica_yukata_crying
        show cg_babybung with dissolve

        player "마망, 마망……!!"

        hide cg_babybung
        show npc_1 with dissolve

        ch_syokuin "이 아이, 엄마가 없는 걸까……?"

        hide npc_1
        show cg_babybung with dissolve

        player "패…… 패드립응앵……"

        hide cg_babybung
        show stand_Monica_yukata_dere with dissolve

        ch_monica "……"

        ch_monica "……저, 저기……"

        hide stand_Monica_yukata_dere
        show npc_1 with dissolve

        ch_syokuin "아, 네! 손님, 무엇을 도와드릴까요?"

        hide npc_1
        show stand_Monica_yukata_dere with dissolve

        ch_monica "……그……"

        ch_monica "그 아이……"

        hide stand_Monica_yukata_dere
        show npc_1 with dissolve

        ch_syokuin "네?"

        hide npc_1

        show stand_Monica_yukata_dere with dissolve

        ch_monica "그…… 저…… 그게……"

        hide stand_Monica_yukata_dere
        show cg_babybung with dissolve

        player "……빨리응애……!"

        hide cg_babybung
        show npc_1 with dissolve

        ch_syokuin "손님, 대단히 죄송합니다만…… 다시 한 번 말씀해 주시겠어요?"

        hide npc_1
        show stand_Monica_yukata_dere with dissolve

        ch_monica "…………"

        $renpy.pause(1.0)

        show stand_Monica_yukata_crying with dissolve
        hide stand_Monica_yukata_dere

        ch_monica "{b}{size=30}내, 내가 그 아이의 엄마입니다~~~~!!!!!{/size}{/b}"

        hide stand_Monica_yukata_crying
        show cg_babybung with dissolve
        show bg_naibu with hpunch

        player "마망!!!! 마망~~~!!!!!"

        hide cg_babybung

        show npc_1 with dissolve

        ch_syokuin "어머……!"

        hide npc_1
        show stand_Monica_yukata_crying with dissolve

        ch_monica "그, 긋…… 그, 그러니까…… 그, 그 아이는 내가 데려가겠……"

        hide stand_Monica_yukata_crying
        show npc_1 with dissolve

        ch_syokuin "……엄마? 이렇게 조그마한 아이가……? 아가야, 어른한테 장난치면 못 써요~?"

        hide npc_1
        show bg_naibu with hpunch
        show cg_babybung with dissolve

        player "마망!!!! 마망~~~!!!!!"

        hide cg_babybung
        show npc_1 with dissolve

        ch_syokuin "어머……!"
        hide npc_1
        show stand_Monica_yukata_crying with dissolve

        ch_monica "그, 긋…… 그, 그러니까…… 그, 그 아이는 내가 데려가겠……"

        hide stand_Monica_yukata_crying
        show npc_1 with dissolve

        ch_syokuin "……엄마? 이렇게 조그마한 아이가……? 아가야, 어른한테 장난치면 못 써요~?"

        hide npc_1
        show bg_naibu with hpunch
        show stand_Monica_yukata_dere with dissolve:
            easeout 0.3 ypos -50
            ease 0.2 ypos 50
            easeout 0.3 ypos -50
            ease 0.2 ypos 50 

        ch_monica "{b}{size=30}아가 아니야아아!!!!!!!!{/size}{/b}"

        hide stand_Monica_yukata_dere
        show cg_babybung with dissolve

        player "마…… 마망맞는마망!!!"

        hide cg_babybung
        show npc_1 with dissolve

        ch_syokuin "어라……?"

        ch_syokuin "진짜로 엄마가 맞는 거니……?!"

        hide npc_1
        show cg_babybung with dissolve

        player "테엥!! 테에에엥!!!"

        hide cg_babybung
        show npc_1 with dissolve

        ch_syokuin "시……"

        ch_syokuin "시, 실례했습니다!!!"

        ch_syokuin "너, 너무 동안이셔서 그만……!! 정말 죄송합니다!!!"

        hide npc_1
        show stand_Monica_yukata_munen with dissolve

        ch_monica "아, 아니…… 괜찮……"

        hide stand_Monica_yukata_munen
        show npc_1 with dissolve

        ch_syokuin "그, 그나저나 이 아이, 엄마를 애타게 찾고 있었는데…… 다행이에요……!"

        hide npc_1
        show cg_babybung with dissolve

        player "마망~~!!!!"

        hide cg_babybung
        show stand_Monica_yukata_dere with dissolve

        ch_monica "호…… 혼자서 무서웠지, 귀공……이 아니라…… 뭐, 뭐라고 해야……?!"

        hide stand_Monica_yukata_dere
        show bg_naibu onlayer middle
        show cg_babybung onlayer forward with dissolve
        $ camera_move(0, 0, 400, 0, 1)

        player "……!!"
        hide cg_babybung onlayer forward
        $ camera_move(0, 0, 0, 0, 0)
        show stand_Monica_yukata_dere onlayer forward with dissolve

        $ camera_move(0, -1000, 400, 0, 1)
        ch_monica "……!!!"

        hide stand_Monica_yukata_dere onlayer forward
        $ camera_move(0, 0, 0, 0, 0)
        show cg_babybung onlayer forward

        $ camera_move(0, 0, 400, 0, 1)
        
        play sound "audio/sound/surp.mp3"

        show highlight onlayer forward with dissolve
        player "{b}{size=30}맘마조!!!!!{/size}{/b}"

        hide cg_babybung onlayer forward

        $ camera_move(0, 0, 0, 0, 0)

        show stand_Monica_yukata_crying onlayer forward with dissolve

        $ camera_move(0, -1000, 400, 0, 1)
        

        play sound "audio/sound/surp.mp3"

        ch_monica "{b}{size=30}어…… 엄마랑 맘마 먹으러 가자……!!!!!!!{/size}{/b}"

        hide stand_Monica_yukata_crying onlayer forward

        $ camera_move(0, 0, 0, 0, 0)

        show bg_black
        hide highlight onlayer forward
        hide bg_naibu onlayer middle

        $renpy.pause(1.5)

        show bg_indoor_onsen with fade
        hide bg_black

        player "응…… 모니카가 아니었다면, 자연스럽게 빠져나오지 못했을 거야……"

        show stand_Monica_yukata_dere with dissolve

        ch_monica "다, 다시는…… 다시는 이런 일 따위…… 부탁하지 말아 다오……"

        hide stand_Monica_yukata_dere

    else:

        player "……유키가 잘해 준 덕분이지……"

        show stand_Yuki_yukata_shamed with dissolve

        ch_yuki "……"

        ch_yuki "아, 아무리 내가, 그 어떤 여성보다도 예쁘고 아름답다지만…… 설마 그런 일을 부탁할 줄은……"

        hide stand_Yuki_yukata_shamed

        show bg_black with fade
        hide bg_indoor_onsen

        ch_nar "조금 전……"

        show bg_onsen_heya_02 with fade
        hide bg_black

        
        play music "audio/main/emer.mp3"

        show stand_Yuki_yukata_shamed with dissolve

        ch_yuki "뭐어어……?! 그…… 그걸 나 보고 하라는 말이야……?! 진심?!!"

        hide stand_Yuki_yukata_shamed
        show stand_Kuka_yukata_mousou with dissolve

        ch_kuka "도, 도S 씨……!! 정말 무엇을 상상하든 그 이하를 보여 주시네요!!! 히이이……!!"

        hide stand_Kuka_yukata_mousou
        show stand_Monica_yukata_ddung with dissolve

        ch_monica "그…… 그렇지만, 지금으로선 그 방법이 최선일 것 같군……! 부탁한다, 귀공!!"

        hide stand_Monica_yukata_ddung

        player "이 방법뿐이야……!!! 바로 간다!!"

        player "……유키, 뒤를 부탁한다……!!"

        show stand_Yuki_yukata_shamed with dissolve

        ch_yuki "으으…… 예쁘다는 칭찬은 그동안 수도 없이 들어봤지만……"

        ch_syokuin "……응?"

        ch_syokuin "어라, 이상하다……?"

        ch_yuki "이…… 이런 방식은 난생 처음이라구우~~!!!"

        player "응애!!!!!!!!!!!"

        ch_syokuin "꺄{font=NanumGothic.ttf}———{/font}아아악?!!!?!!!!!"

        hide stand_Yuki_yukata_shamed

        show bg_black
        $renpy.pause(1.0)
        stop music fadeout 3.0

        show bg_naibu with fade
        hide bg_black

        play music "audio/main/11fun.mp3"

        show cg_babybung with dissolve

        player "테에엥……"

        hide cg_babybung

        show stand_Yuki_yukata_angry with dissolve

        ch_yuki "……"

        hide stand_Yuki_yukata_angry
        show stand_Monica_yukata_munen with dissolve

        ch_monica "……유, 유키……! 지금 바로 가야 한다……!!"

        hide stand_Monica_yukata_munen
        show stand_Yuki_yukata_angry with dissolve

        ch_yuki "나…… 나도 알아!! 보채지 마……"

        ch_yuki "으으으…… 내가 왜 이런 일을……"

        hide stand_Yuki_yukata_angry

        show cg_babybung with dissolve

        player "마망, 마망……!!"

        hide cg_babybung
        show npc_1 with dissolve

        ch_syokuin "이 아이, 엄마가 없는 걸까……?"

        hide npc_1
        show cg_babybung with dissolve

        player "패…… 패드립응앵……"

        hide cg_babybung
        show stand_Yuki_yukata_angry with dissolve

        ch_yuki "……"

        ch_yuki "……저, 저기……"

        hide stand_Yuki_yukata_angry
        show npc_1 with dissolve

        ch_syokuin "아, 네! 손님, 무엇을 도와드릴까요?"

        hide npc_1
        show stand_Yuki_yukata_shamed with dissolve

        ch_yuki "……그……"

        ch_yuki "그 아이……"

        hide stand_Yuki_yukata_shamed
        show npc_1 with dissolve

        ch_syokuin "네?"

        hide npc_1

        show stand_Yuki_yukata_shamed with dissolve

        ch_yuki "그…… 그게……"

        hide stand_Yuki_yukata_shamed
        show cg_babybung with dissolve

        player "……빨리응애……!"

        hide cg_babybung
        show npc_1 with dissolve

        ch_syokuin "손님, 대단히 죄송합니다만…… 다시 한 번 말씀해 주시겠어요?"

        hide npc_1
        show stand_Yuki_yukata_shamed with dissolve

        ch_yuki "…………"

        $renpy.pause(1.0)

        ch_yuki "{b}{size=30}내…… 내가 그 아이의 엄마야~~!!!!{/size}{/b}"

        hide stand_Yuki_yukata_shamed
        show cg_babybung with dissolve
        show bg_naibu with hpunch

        player "마망!!!! 마망~~~!!!!!"

        hide cg_babybung

        show npc_1 with dissolve

        ch_syokuin "어머……!"

        hide npc_1
        show stand_Yuki_yukata_shamed with dissolve

        ch_yuki "그, 긋…… 그러니까……"

        ch_yuki "그, 그 아이는…… 내가 데려……갈게……!"

        hide stand_Yuki_yukata_shamed
        show npc_1 with dissolve

        ch_syokuin "이 아이, 엄마를 애타게 찾고 있었는데…… 정말 다행이에요……!"

        hide npc_1
        show cg_babybung with dissolve

        player "마망~~!!!!"

        hide cg_babybung
        show stand_Yuki_yukata_shamed with dissolve

        ch_yuki "그…… 호…… 혼자서 많이 무서웠지……? 으으으으…… 뭐, 뭐라고 말해야 하는 거야……"

        hide stand_Yuki_yukata_shamed
        show bg_naibu onlayer middle
        show cg_babybung onlayer forward with dissolve
        $ camera_move(0, 0, 400, 0, 1)

        player "……!!"
        hide cg_babybung onlayer forward
        $ camera_move(0, 0, 0, 0, 0)
        show stand_Yuki_yukata_shamed onlayer forward with dissolve

        $ camera_move(0, -1000, 400, 0, 1)
        ch_yuki "……!!!"

        hide stand_Yuki_yukata_shamed onlayer forward
        $ camera_move(0, 0, 0, 0, 0)
        show cg_babybung onlayer forward

        $ camera_move(0, 0, 400, 0, 1)
        
        play sound "audio/sound/surp.mp3"

        show highlight onlayer forward with dissolve
        player "{b}{size=30}맘마조!!!!!{/size}{/b}"

        hide cg_babybung onlayer forward

        $ camera_move(0, 0, 0, 0, 0)

        show stand_Yuki_yukata_shamed onlayer forward with dissolve

        $ camera_move(0, -1000, 400, 0, 1)
        
        play sound "audio/sound/surp.mp3"

        ch_yuki "{b}{size=30}어…… 엄마랑 맘마 먹으러 가자~~~!!!!!!{/size}{/b}"

        hide stand_Yuki_yukata_shamed onlayer forward

        $ camera_move(0, 0, 0, 0, 0)

        show bg_black
        hide highlight onlayer forward
        hide bg_naibu onlayer middle

        $renpy.pause(1.5)

        show bg_indoor_onsen with fade
        hide bg_black

        player "응…… 유키가 아니었다면, 절대 자연스럽게 빠져나오지 못했을 거야……"

        show stand_Yuki_yukata_shamed with dissolve

        ch_yuki "다, 다음부터는…… 예쁘다는 칭찬은 그냥 말로 해 주면 좋겠어……"

        hide stand_Yuki_yukata_shamed

    ## 이후 정상진행

    play music "audio/main/5orientalcommon.mp3"

    player "……아무튼 잘 해결됐으니까 대충 넘어가자……"

    player "그건 그거고, 이제부터 열심히 단서를 찾아보자구."

    show stand_Monica_yukata_down with dissolve

    ch_monica "그, 그래…… 어쨌든 귀공 덕분에 위기를 넘겼으니, 조사를 재개할 수 있겠어."

    hide stand_Monica_yukata_down
    show stand_Yuki_yukata_ddung with dissolve

    ch_yuki "그나저나…… 저쪽은 잘 하고 있으려나~? 갑작스럽게 팀이 나눠져서 혼란스러울 텐데……"

    hide stand_Yuki_yukata_ddung

    player "니논이랑 쿠우카……라면 뭐……"

    player "……심각하게 걱정되는 조합이긴 하네……"

    player "아, 알아서 잘 하겠지……"

    show stand_Monica_yukata_down with dissolve

    ch_monica "그런데 귀공, 숙소 쪽은 어떻게 할 생각이지? 이대로 포기하는 수밖에 없나……"

    hide stand_Monica_yukata_down

    player "당장은 위험하니까 어쩔 수 없지만…… 저녁이나 밤 정도가 되면 직원들도 안 돌아다니지 않을까?"

    player "욕탕 조사가 끝나는대로 숙소 쪽도 다시 살펴 보자."

    show stand_Monica_yukata with dissolve

    ch_monica "좋은 생각이다. 그러면 온천부터 빠짐없이 조사해야겠군."

    hide stand_Monica_yukata

    $renpy.pause(1.0)

    ch_ayumi "지이이이……"

    show bg_black with fade
    hide bg_indoor_onsen

    $renpy.pause(1.0)

    show bg_indoor_onsen
    hide bg_black

    show stand_Monica_yukata_down with dissolve

    ch_monica "후우…… 이게 마지막인 것 같아."

    hide stand_Monica_yukata_down

    player "……또 허탕이네……"

    show stand_Yuki_yukata_ddung with dissolve

    ch_yuki "피곤해애……"

    hide stand_Yuki_yukata_ddung
    show stand_Monica_yukata_ddung with dissolve

    ch_monica "불평할 시간도 아깝다! 어서 다른 장소로 이동하도록 하자."

    hide stand_Monica_yukata_ddung
    
    player "그래…… 그럼 이 다음은……"

    player "{b}{size=30}……뭐야 이거?!{/size}{/b}"

    show stand_Monica_yukata_surprised with dissolve:
        easeout 0.3 ypos -50
        ease 0.2 ypos 50
        easeout 0.3 ypos -50
        ease 0.2 ypos 50 
        
    ch_monica "우와앗!! 무…… 무슨 일인가, 귀공!!"

    hide stand_Monica_yukata_surprised

    player "여기, 바닥을 봐!"

    show ob_unagi with dissolve:
        xpos 430 yalign 0.3

    ch_yuki "이건……?"

    ch_monica "음…… 장어 요리인가."

    ch_monica "그런데 왜 이런 곳에 떨어져 있는 거지……? 조금 뜬금없군."

    ch_yuki "이빨 자국이 있는데…… 바닥에 떨어진 걸 주워 먹은 걸까? 더러워라……"

    player "이거, 자세히 보니…… 먼지가 내려앉아 있네."

    player "그 말은…… 좀 오래 된 거라는 뜻인데…… 이쪽은 청소하는 직원이 없나?"
    
    $renpy.pause(1.0)

    player "……없을리가 없지!!!"

    player "단서다{font=NanumGothic.ttf}——{/font}!!!!"

    hide ob_unagi
    show stand_Yuki_yukata_ddung with dissolve

    ch_yuki "뭐어~? 갑자기?"

    hide stand_Yuki_yukata_ddung
    show stand_Monica_yukata_ddung with dissolve

    ch_monica "무슨 말이지……? 자세히 설명해 다오."

    hide stand_Monica_yukata_ddung

    player "장어구이 조각이 복도 한복판에 대놓고 떨어져 있었다는 점……"

    player "그럼에도 먼지가 쌓일 때까지 치우지 않았다는 점, 그 말은……"

    ## 단서 발견 효과음

    player "이곳을 청소하던 직원이…… 사라졌다는 것이다……!"

    show stand_Monica_yukata_ddung with dissolve

    ch_monica "……? 으음……"

    ch_monica "그 정도는 누구나 떠올릴 수 있는 생각인 것 같다만, 그게 다는 아닐 테고……"

    ch_nar "그게 다야 뭘 더 바래……!!"

    ch_monica "그러니까 귀공이 말하고자 하는 바는…… 이것을 마물의 정체와 연관지을 수 있다는 이야기겠지? 계속해 보게."

    ch_nar "몰 바라냐고!!!! 그게 다라고!!!! 아악!!!!!!!"

    hide stand_Monica_yukata_ddung
    show stand_Yuki_yukata_ddung with dissolve

    ch_yuki "더 생각할 게 뭐 있어?"

    ch_yuki "식당과 거리가 꽤 먼 곳에 위치한 온천…… 그리고 장어구이."

    ch_yuki "있어서는 안 될 곳에 부자연스럽게 떨어져 있는 음식 조각."

    ch_yuki "거기다 선명하게 남아 있는 이빨자국까지…… 누가 봐도 마물의 소행이잖아? 더 볼 필요가 있나?"

    hide stand_Yuki_yukata_ddung

    player "……"

    player "……내 말이!"

    ch_nar "왤케 똑똑함?"

    show stand_Monica_yukata_ddung with dissolve

    ch_monica "음…… 그거야 그렇다만……"

    ch_monica "……아니야. 흔적을 남긴 것이 무엇이든 간에, 이것이 마물과 관련된 단서라는 점은 의심할 여지가 없겠어."

    show stand_Monica_yukata
    hide stand_Monica_yukata_ddung

    ch_monica "아직 걸리는 게 조금 남아 있지만…… 좋다. 나머지 단서를 찾는다면 조각이 맞춰질 테지. 다음 장소로 이동하자."

    $ persistent.unagi = True
    $ persistent.clues_unagi = True
    show screen clueFinded
    hide stand_Monica_yukata
    $renpy.pause(1.0)
    show bg_black
    hide bg_indoor_onsen
    jump scene19_2
## S# 19-1. 야외 온천 2 (밤) (니논, 쿠우카 루트) ######
label scene19_1:
    scene bg_outside_onsen with fade
    show stand_Kuka_yukata with dissolve

    ch_kuka "음…… 온천은 여기가 마지막인 것 같네요……"

    hide screen clueFinded

    hide stand_Kuka_yukata

    player "여기 되게 분위기 좋다."

    show stand_Ninon_yukata_down with dissolve

    ch_ninon "히잉…… 입니다. 조금 아쉽다 입니다……"

    if love_point == 1:

        ch_ninon "원래라면 지금쯤, 이런 온천에 몸을 담근 채 수면에 아른거뤼는 달빛을 바롸보고 있었을……"

        show stand_Ninon_yukata_emb with dissolve
        hide stand_Ninon_yukata_down

        ch_ninon "……달빛……"

        ch_ninon "……쇼군!"

        hide stand_Ninon_yukata_emb

        player "응?"

        show stand_Ninon_yukata_emb with dissolve

        ch_ninon "그……"

        ch_ninon "다…… 달이 아름답네요 입니다~~!!!!!"

        hide stand_Ninon_yukata_emb

        player "??"

        player "그런가?"

        show stand_Ninon_yukata_emb with dissolve

        ch_ninon "……"

        ch_nar "뭐지? 뭘 쳐다보는 것이지?"

        ch_ninon "그…… 동국에서는, 달이 아름답다는 말을 고……백……"

        show stand_Ninon_yukata_innocent
        hide stand_Ninon_yukata_emb

        ch_ninon "……하…… 아닙니다……"

        ch_nar "? 혼자 왜 저럼?"
        hide stand_Ninon_yukata_innocent

    else:
        
        ch_ninon "원래라면 지금쯤, 이런 온천에 몸을 담근 채 수면에 아른거뤼는 달빛을 바롸보고 있었을 텐데……"

        hide stand_Ninon_yukata_down

        show stand_Kuka_yukata_down with dissolve

        ch_kuka "그, 그러게요…… 너무 아쉽네요……"

        show stand_Kuka_yukata
        hide stand_Kuka_yukata_down

        ch_kuka "노천탕이라면…… 홀딱 벗겨진 채로 야외에 내던져진 듯한 감각을 느낄 수 있었을 텐데……! 쿠헤헤헷……!!"

        hide stand_Kuka_yukata
    
    player "……음…… 나도 뭔가 아쉽긴 한데……"

    player "일만 잘 해결되면 하루 정도 더 있다 가는 건 어때? 모니카한테 이야기해 보자."

    show stand_Ninon_yukata with dissolve

    ch_ninon "오옷~ 그것도 좋은 생……"

    hide stand_Ninon_yukata

    stop music

    show bg_outside_onsen with hpunch

    play sound "audio/sound/rima.wav"

    hatena "꾸에에에엑!!!!!!!"

    player "무…… 무슨 소리야?!!"

    show stand_Kuka_yukata_surprised with dissolve

    ch_kuka "저, 저쪽 구석에서 소리가 났어요!!"

    hide stand_Kuka_yukata_surprised

    show stand_Ninon_yukata_panic with dissolve

    ch_ninon "이 기묘한 울음소뤼는 대체…… 마물?! 마물 입니까?!"

    hide stand_Ninon_yukata_panic

    $renpy.pause(1.0)

    play music "audio/main/11fun.mp3"

    show npc_3 with dissolve

    show bg_outside_onsen with hpunch

    ch_rima "꿰에에에에엑!!!"

    hide npc_3

    show stand_Kuka_yukata_hiku with dissolve

    ch_kuka "……"

    hide stand_Kuka_yukata_hiku
    show stand_Ninon_yukata_down with dissolve

    ch_ninon "………"

    hide stand_Ninon_yukata_down
    
    player "……"

    player "……마물 맞는 것 같아! 죽이자!!"

    show npc_3 with dissolve

    ch_rima "꾸웨에엑??!!"

    play sound "audio/sound/spit.mp3"
    show npc_3:
        linear 0.2 xalign 0.4
        linear 0.2 xalign 0.6
        linear 0.2 xalign 0.5


    ch_rima "퉤에엣! 퉷!! 퉤퉷!!!"

    hide npc_3

    player "저…… 저거 침 뱉는다!!!"

    show stand_Ninon_yukata_panic with dissolve

    ch_ninon "우와앗~~!! 짱 더럽다 입니다~~~!!!"

    show stand_Ninon_yukata_panic:
        linear 0.2 xalign 0.2
        linear 0.2 xalign 0.8
        linear 0.2 xalign 0.2
        linear 0.2 xalign 0.8
        linear 0.2 xalign 0.5

    ch_ninon "회, 회퓌기동!!! 슈바바바밧!!!!"
    
    hide stand_Ninon_yukata_panic

    play sound "audio/sound/spit.mp3"

    show npc_3 with dissolve

    ch_rima "퉤에엑!!! 퉤헷!!!!"

    hide npc_3

    ch_nar "철퍽."

    stop music

    $renpy.pause(1.0)

    player "……"

    player "……철퍽?"

    show stand_Kuka_yukata with dissolve

    ch_kuka "……"

    hide stand_Kuka_yukata

    show stand_Ninon_yukata_surp with dissolve

    ch_ninon "……"

    ch_ninon "……쿠우카 씨."

    ch_ninon "진정하고 심호흡   {nw}"

    hide stand_Ninon_yukata_surp
    
    show stand_Kuka_yukata_mousou with dissolve

    show stand_Kuka_yukata_mousou:
        rotate 0
        linear 0.5 rotate 720 ypos 0
    
    play music "audio/main/11fun.mp3"

    ch_kuka "햐히~~~~~이이익~~~~!!!!!!!"

    show stand_Kuka_yukata_mousou:
        linear 0.5 ypos 1100

    ch_kuka "끄!!!!! 끈적거려!!!!! 최고예요~~~~!!!! 이런 불쾌하고 더러운 감각!!!! 이쪽 업계에서는 포상입니다!!!!! 이…… 이러면 더 이상 이전의 쿠우카로는 돌아갈 수 없어요~~~~!!! 쿠우카를……!!!! 망가질 대로 망가진 쿠우카르을~~~!!!!! 좀 더 심하게 더럽혀 주세요!!!! 키{font=NanumGothic.ttf}——{/font}히히히히힉!!! 케헤헤헥~~~!!!!!"

    hide stand_Kuka_yukata_mousou
    show stand_Ninon_yukata_panic with dissolve

    ch_ninon "쿠…… 쿠우카 씨가 맛이 갔어요 입니다!!!"

    hide stand_Ninon_yukata_panic
    
    player "아니 뭐 원래도 정상은 아니었긴 한데……"

    show npc_3 with dissolve

    ch_rima "쿠에엑!! 끼에에에!!!"

    show npc_3:
        linear 0.3 xalign 0.0
    hide npc_3 with dissolve

    player "도…… 도망간다!!"

    show stand_Ninon_yukata_surp with dissolve

    ch_ninon "어……?! 쇼군!!!"

    ch_ninon "저기 저기…… 녀석이 있던 자리에……! 뭔가 있어요 입니다!!"

    hide stand_Ninon_yukata_surp

    player "뭐?! 똥이라도 싸지른 거 아니야?!"

    show ob_kiroku with dissolve

    play music "audio/main/5orientalcommon.mp3"
    play sound "audio/sound/book.wav"

    player "……이건……?"

    ch_ninon "편지…… 같아요 입니다!"

    hide ob_kiroku
    show stand_Kuka_yukata_mousou with dissolve:
        xpos 200 ypos 250
    
    ch_kuka "힉…… 히힉…… 헤으극…… 기잇……"

    hide stand_Kuka_yukata_mousou
    show stand_Ninon_yukata_down with dissolve

    ch_ninon "형님, 이년 웃는데요?"

    hide stand_Ninon_yukata_down
    
    player "냅둬. 기분 좋은 꿈이라도 꾸나 보지."

    show ob_kiroku with dissolve

    player "그런데 이게 대체 뭘까?"

    player "방금 그 짐승이 떨구고 간 건 아닐 테고…… 먹는 걸로 착각해서 뜯어 먹으려던 건가……?"

    ch_ninon "일단 내용부터 확인해 보는 건 어떻소 입니까?"

    player "그, 그래. 뭐라고 적혀 있는지나 보자."

    ch_nar "“이 편지는 영국에서 최초로 시작되어……”"

    player "에이씨……"

    ch_ninon "쇼, 쇼군!! 잠깐만 입니다!"

    ch_ninon "여기…… 여기를 보십시오 입니다!"

    player "뭐야? 제대로 된 내용이 있긴 하네…… 어디 보자."

    ch_nar "“내 이름은”  {nw}"

    player "응~ 니 이름 안 궁금해~"

    player "넘기고, 넘기고…… 여기부터."

    ch_nar "“……언제부터였을까. 잔병치레도 잘 없이 건강하던 몸에 무언가 이상이 느껴지고, 미묘한 위화감이 들기 시작했다.”"

    ch_nar "“위화감…… 그래, 위화감. 확실히 무언가 잘못되어 가고 있다. 하지만……”"

    ch_nar "“……설명할 수 없다. 이유가 뭐지? 왜 이렇게…… 불안한 걸까? 대체 무엇 때문에……?”"

    ch_nar "“……어느 날, 시설 위생에 문제가 있다는 불만이 수십 건이나 접수되었다. 이상하다. 이런 적은 단 한 번도……”"

    player "여기 직원이 쓴 건가 보군……"

    ch_nar "“그럴 리 없다. 확실하다. 무언가 잘모ㅅ 디ㅗㅇ서ㄷㅏ.”"

    player "응……?"

    ch_nar "“뭔 가 이상ㅎㅏ다. ㅇㅣ사ㅇ해 ..뜨, 거ㅂㄷㅏ. ㄸㅡ거우ㅓ.! 가 ㅇㅑ해 !.. 도마ㅇ, ㅎㅏㄱ싶 ㅓㅓ ㅓ”"

    player "갑자기 뭐야……?!"

    hide ob_kiroku
    show stand_Ninon_yukata_surp with dissolve

    ch_ninon "쇼군……!! 이것은…… 구라노스케 씨가 보낸 초대장이랑 비슷하다 입니다!!"

    hide stand_Ninon_yukata_surp

    player "그러네…… 이걸 쓴 직원도, 기록을 남기던 도중 마물에게 당해 버린 걸까?"

    player "……생각보다 뒤처리가 허술한 녀석인데……? 초대장 때도 그렇고, 꼬리가 밟힐지도 모르는 기록을 그대로 남겨 두다니……"

    show stand_Ninon_yukata_down with dissolve

    ch_ninon "흐므므……"

    show stand_Ninon_yukata_surp
    hide stand_Ninon_yukata_down

    ch_ninon "아! 글자를 모르는 마물이 아닐까요 입니다? 무슨 내용이 적혀 있는쥐도 모르니까……"

    show stand_Kuka_yukata at right with dissolve

    ch_kuka "어쩌면…… 일부러 단서를 흘리고 다닌 걸지도 몰라요……"

    hide stand_Ninon_yukata_surp
    show stand_Ninon_yukata_panic:
        easeout 0.3 ypos -50
        ease 0.2 ypos 50
        easeout 0.3 ypos -50
        ease 0.2 ypos 50 
        ## 팔짝

    ch_ninon "와왓!!! 쿠우카 씨?! 언제 정신 차린 거야 입니까?!!"

    show stand_Kuka_yukata_mousou at right
    hide stand_Kuka_yukata

    ch_kuka "저, 저는 언제나 제정신이었답니다…… 다만 방금은 너무 기분이 좋은 나머지……!! 후히, 키히히히힛……"

    hide stand_Ninon_yukata_panic
    hide stand_Kuka_yukata_mousou

    ch_nar "단서를…… 고의로 남겼다?"

    ch_nar "쿠우카의 가설이 맞다면……"

    ch_nar "……이거, 진짜로 좀 위험할지도 모르겠는데……"

    $ persistent.clues_rima = True
    $ persistent.clues_kiroku = True
    show screen clueFinded
    $renpy.pause(1.0)
    show bg_black
    hide bg_outside_onsen

    jump scene20Common
## S# 19-2. 야외 온천 2 (밤) (모니카, 유키 루트) ######
label scene19_2:
    scene bg_outside_onsen

    show stand_Monica_yukata with dissolve

    ch_monica "음…… 온천은 여기가 마지막인 것 같군."

    hide screen clueFinded

    hide stand_Monica_yukata

    player "여기 되게 분위기 좋다."

    show stand_Yuki_yukata_ddung with dissolve

    ch_yuki "하아~ 처음부터 이런 노천탕을 기대하고 온 건데 말야……"

    ch_yuki "달빛을 머금어 더욱 수려해진 나의 미모를 감상하고 있어도 모자랄 판에…… 지금 이게 뭐하는 거냐구……"

    hide stand_Yuki_yukata_ddung

    player "음…… 나도 뭔가 아쉽긴 한데……"

    player "일만 잘 해결되면 하루 정도 더 있다 가는 건 어때?"

    show stand_Yuki_yukata with dissolve

    ch_yuki "꺄~ 나는 찬성!"

    hide stand_Yuki_yukata

    show stand_Monica_yukata_munen with dissolve

    ch_monica "……으음, 뭐…… 일만 잘 풀린다면야, 하루 정도야 괜찮……"

    hide stand_Monica_yukata_munen

    stop music fadeout 3.0

    show bg_outside_onsen with hpunch

    play sound "audio/sound/rima.wav"

    hatena "꾸에에에엑!!!!!!!"

    player "무…… 무슨 소리야?!!"

    show stand_Yuki_yukata_angry with dissolve

    ch_yuki "기, 기분 나빠……!!"

    hide stand_Yuki_yukata_angry

    show stand_Monica_yukata_surprised with dissolve

    ch_ninon "이 기괴한 울음소리는 대체…… 마물?! 마물인가?!"

    hide stand_Monica_yukata_surprised

    $renpy.pause(1.0)

    play music "audio/main/11fun.mp3"

    show npc_3 with dissolve

    show bg_outside_onsen with hpunch

    ch_rima "꿰에에에에엑!!!"

    hide npc_3

    show stand_Yuki_yukata_angry with dissolve

    ch_yuki "……"

    hide stand_Yuki_yukata_angry
    show stand_Monica_yukata_down with dissolve

    ch_monica "………"

    hide stand_Monica_yukata_down
    
    player "……"

    player "……마물 맞는 것 같아! 죽이자!!"

    show npc_3 with dissolve

    ch_rima "꾸웨에엑??!!"

    play sound "audio/sound/spit.mp3"
 
    show npc_3:
        linear 0.2 xalign 0.4
        linear 0.2 xalign 0.6
        linear 0.2 xalign 0.5

    ch_rima "퉤에엣! 퉷!! 퉤퉷!!!"

    hide npc_3

    player "저…… 저거 침 뱉는다!!!"

    show stand_Monica_yukata_dere with dissolve:
        xalign 0.5
        easeout 0.3 ypos -50
        ease 0.2 ypos 50
        easeout 0.3 ypos -50
        ease 0.2 ypos 50 

    ch_ninon "우와아앗!!! 모, 모두들!! 피해라!!!"

    hide stand_Monica_yukata_dere

    play sound "audio/sound/spit.mp3"

    show npc_3 with dissolve

    ch_rima "퉤에엑!!! 퉤헷!!!!"

    hide npc_3

    ch_nar "철퍽."

    stop music

    $renpy.pause(1.0)

    player "……"

    player "……철퍽?"

    show stand_Yuki_yukata with dissolve

    ch_yuki "……"

    hide stand_Yuki_yukata

    show stand_Monica_yukata_surprised with dissolve

    ch_monica "……"

    ch_monica "……유키."

    ch_monica "진정하고 심호흡   {nw}"

    hide stand_Monica_yukata_surprised
    
    show stand_Yuki_yukata with dissolve

    ch_yuki "가르르……"

    show stand_Yuki_yukata:
        rotate 0
        linear 0.5 rotate 360
    hide stand_Yuki_yukata with dissolve
    
    play music "audio/main/11fun.mp3"

    show stand_Monica_yukata_surprised with dissolve

    ch_monica "유키~~~~~이이이!!!!!!"

    hide stand_Monica_yukata_surprised

    show npc_3 with dissolve

    ch_rima "쿠에엑!! 끼에에에!!!"

    show npc_3:
        linear 0.3 xalign 0.0
    hide npc_3 with dissolve

    player "도…… 도망간다!!"

    show stand_Monica_yukata_surprised with dissolve

    ch_monica "어……?! 귀공!!!"

    ch_monica "녀석이 있던 자리에…… 무언가 떨어져 있다!!"

    hide stand_Monica_yukata_surprised

    player "뭐?! 똥이라도 싸지른 거 아니야?!"

    show ob_kiroku with dissolve

    play music "audio/main/5orientalcommon.mp3"
    play sound "audio/sound/book.wav"

    player "……이건……?"

    ch_monica "편지…… 인가?"

    hide ob_kiroku
    show stand_Yuki_yukata with dissolve:
        xpos 200 ypos 250
    
    ch_yuki "……"

    hide stand_Yuki_yukata
    show stand_Monica_yukata_down with dissolve

    ch_monica "귀공…… 유키가…… 숨을 쉬지 않는 것 같아……"

    hide stand_Monica_yukata_down
    
    player "보내 주자…… 산 사람은 살아야지……"

    show ob_kiroku with dissolve

    player "그런데 이게 대체 뭘까?"

    player "방금 그 짐승이 떨구고 간 건 아닐 테고…… 먹는 걸로 착각해서 뜯어 먹으려던 건가……?"

    ch_monica "흐으음…… 일단 내용부터 확인해 보는 건 어떤가?"

    player "그, 그래. 뭐라고 적혀 있는지나 보자."

    ch_nar "“이 편지는 영국에서 최초로 시작되어……”"

    player "에이씨……"

    ch_monica "귀, 귀공!! 잠깐 기다려라!!!"

    ch_monica "여기…… 여기를 봐!"

    player "뭐야? 제대로 된 내용이 있긴 하네…… 어디 보자."

    ch_nar "“내 이름은”  {nw}"

    player "응~ 니 이름 안 궁금해~"

    player "넘기고, 넘기고…… 여기부터."

    ch_nar "“……언제부터였을까. 잔병치레도 잘 없이 건강하던 몸에 무언가 이상이 느껴지고, 미묘한 위화감이 들기 시작했다.”"

    ch_nar "“위화감…… 그래, 위화감. 확실히 무언가 잘못되어 가고 있다. 하지만……”"

    ch_nar "“……설명할 수 없다. 이유가 뭐지? 왜 이렇게…… 불안한 걸까? 대체 무엇 때문에……?”"

    ch_nar "“……어느 날, 시설 위생에 문제가 있다는 불만이 수십 건이나 접수되었다. 이상하다. 이런 적은 단 한 번도……”"

    player "여기 직원이 쓴 건가 보군……"

    ch_nar "“그럴 리 없다. 확실하다. 무언가 잘모ㅅ 디ㅗㅇ서ㄷㅏ.”"

    player "응……?"

    ch_nar "“뭔 가 이상ㅎㅏ다. ㅇㅣ사ㅇ해 ..뜨, 거ㅂㄷㅏ. ㄸㅡ거우ㅓ.! 가 ㅇㅑ해 !.. 도마ㅇ, ㅎㅏㄱ싶 ㅓㅓ ㅓ”"

    player "갑자기 뭐야……?!"

    hide ob_kiroku
    show stand_Monica_yukata_surprised with dissolve

    ch_monica "……이건…… 구라노스케가 보낸 초대장과 유사한 형태다……!!"

    hide stand_Monica_yukata_surprised

    player "그러네…… 이걸 쓴 직원도, 기록을 남기던 도중 마물에게 당해 버린 걸까?"

    player "……생각보다 뒤처리가 허술한 녀석인데……? 초대장 때도 그렇고, 꼬리가 밟힐지도 모르는 기록을 그대로 남겨 두다니……"

    show stand_Monica_yukata_down with dissolve

    ch_monica "흐음……"

    ch_monica "글자를 모르는 마물이 아닐까? 무슨 내용이 적혀 있는지도 모르니……"

    show stand_Yuki_yukata at right with dissolve

    ch_yuki "어쩌면…… 일부러 단서를 흘리고 다닌 걸지도 몰라……"

    hide stand_Monica_yukata_down
    show stand_Monica_yukata_dere:
        easeout 0.3 ypos -50
        ease 0.2 ypos 50
        easeout 0.3 ypos -50
        ease 0.2 ypos 50 
        ## 팔짝

    ch_monica "우아악!!!!! 유키?!! 정신을 차린 건가?!"

    ch_yuki "……무슨 소리야~"

    show stand_Yuki_yukata:
        linear 0.5 ypos 1000

    hide stand_Yuki_yukata with dissolve

    ch_yuki "마치 내그우웨에…… 기절이라도옥 했다느흐우에웨에에엑{font=NanumGothic.ttf}——{/font}"

    ch_monica "유키~~~~~~~~이이이이이!!!!!!!!!"

    hide stand_Monica_yukata_dere

    ch_nar "단서를…… 고의로 남겼다?"

    ch_nar "유키의 가설이 맞다면……"

    ch_nar "……이거, 진짜로 좀 위험할지도 모르겠는데……"

    $ persistent.clues_rima = True
    $ persistent.clues_kiroku = True
    show screen clueFinded
    $renpy.pause(1.0)
    show bg_black
    hide bg_outside_onsen

    jump scene20Common
    return
## S# 20. 온천 숙소 3 (밤) (공통 루트 - 아쿠다이칸 기계인형 설계도)
label scene20Common:
    scene bg_onsen_heya_01
    show stand_Ninon_yukata_wink with dissolve

    ch_ninon "여러분~~!! 보고 싶었어요 입니다~~~!!!"

    hide screen clueFinded

    ch_ninon "모니카 씨도 안녕 입니까~?"

    hide stand_Ninon_yukata_wink

    show stand_Monica_yukata_dere with dissolve:
        xalign 0.5
        easeout 0.3 ypos -50
        ease 0.2 ypos 50
        easeout 0.3 ypos -50
        ease 0.2 ypos 50 
        ##팔짝 뛰는 모션

    ch_monica "머…… 머리를 쓰다듬지 마아!!!!!"

    hide stand_Monica_yukata_dere

    if love_point == 1 or love_point == 3:
        show stand_Yuki_yukata with dissolve

        ch_yuki "다들 뭐라도 좀 찾았어?"

        show stand_Yuki_yukata_ddung
        hide stand_Yuki_yukata

        ch_yuki "이 이상 나의 미모를 음미할 시간이 낭비되는 건 곤란하다구…… 지고의 아름다움에 도달했음에도 만족할 줄을 모르고, 하루가 다르게 사랑스러워지는 나를 지켜보지 못하다니…… 이건 엄청난 죄악이야~! 알아?"

        hide stand_Yuki_yukata_ddung

        ch_nar "아무것도 안 하고 거울만 쳐다보고 있었을 거면서……"

        show stand_Ninon_yukata_down with dissolve

        ch_ninon "으음, 그게……"

        ch_ninon "뭔가를…… 찾긴 했는데……"

        hide stand_Ninon_yukata_down
        show stand_Kuka_yukata_mousou with dissolve

        ch_kuka "히익♥ 히이이…… 키힛……!! 케게게……"

        hide stand_Kuka_yukata_mousou
        show stand_Monica_yukata_down with dissolve

        ch_monica "……쿠우카는 또 왜 저런 상태인 거냐……?"

        hide stand_Monica_yukata_down
        show stand_Ninon_yukata_down with dissolve

        ch_ninon "그게…… 믿기지 않으쉬겠지만……"

        ch_ninon "{b}……기괴한 생김새의 사족동물이 개구멍을 통해 노천탕 안으로 기어들어 와서 따발총마냥 난사하듯 뱉던 침을 쿠우카 씨가 맞고 한참 정신이 없는 와중 그 짐승이 도망가기 전에 머물렀던 자리에서 온천의 직원이 쓴 것으로 보이는 기록을 발견한 것 때문에 이렇게 되었다……{/b}"

        ch_ninon "……입니다."

        hide stand_Ninon_yukata_down
        show stand_Yuki_yukata_angry with dissolve

        ch_yuki "……??"

        hide stand_Yuki_yukata_angry
        show stand_Monica_yukata_down with dissolve

        ch_monica "……그게 대체 무슨……"

        hide stand_Monica_yukata_down

        player "놀랍게도 거짓말은 하지 않았습니다……"

        show bg_black with dissolve
        hide bg_onsen_heya_01

        $renpy.pause(2.0)

        show bg_onsen_heya_01 with fade

        show stand_Monica_yukata_surprised with dissolve

        ch_monica "그럴 수가……"

        show stand_Monica_yukata_ddung
        hide stand_Monica_yukata_surprised

        ch_monica "사람들을 정신 이상에 빠뜨리고, 무방비한 상태가 되었을 때 습격한 건가……"

        ch_monica "……정신공격 계열의 마물인 것 같군. 우리도 자칫하면 당할 수 있겠어…"

        hide stand_Monica_yukata_ddung

    else:
        show stand_Kuka_yukata_down with dissolve

        ch_kuka "다른 분들은 뭔가 찾으셨나요……?"

        ch_kuka "저희 쪽은…… 딱히 이렇다 할 만한 건 찾지 못했어요……"

        hide stand_Kuka_yukata_down
        show stand_Monica_yukata_down with dissolve

        ch_monica "으음, 그게……"

        ch_monica "뭔가를…… 찾긴 했는데……"

        hide stand_Monica_yukata_down
        show stand_Yuki_yukata with dissolve:
            xpos 200 ypos 250
        
        ch_yuki "……"

        hide stand_Yuki_yukata
        show stand_Ninon_yukata_down with dissolve

        ch_ninon "유키 씨는 왜 선 채로 죽었다 입니까……?"

        hide stand_Ninon_yukata_down
        show stand_Monica_yukata_down with dissolve

        ch_monica "그게…… 믿기 힘들겠지만……"

        ch_monica "{b}……개구멍을 통해 노천탕에 들어온 것으로 추측되는 기괴한 짐승이 우리를 경계하며 마구잡이로 뱉은 침에 유키가 피격당해 혼란스럽던 와중 놈이 도망치기 전까지 머물렀던 지점에서 정황상 온천의 직원이 작성한 것으로 보이는 기록을 발견한 것……{/b}"

        ch_monica "……때문이다."

        hide stand_Monica_yukata_down
        show stand_Ninon_yukata_down with dissolve

        ch_monica "개소리 입니까……?"

        hide stand_Ninon_yukata_down

        player "놀랍게도 거짓말은 하지 않았습니다……"

        show bg_black with dissolve
        hide bg_onsen_heya_01

        $renpy.pause(2.0)

        show bg_onsen_heya_01 with fade

        show stand_Kuka_yukata_surprised with dissolve

        ch_kuka "그럴 수가……"

        show stand_Kuka_yukata_shamed
        hide stand_Kuka_yukata_surprised

        ch_kuka "사람들을 정신 이상에 빠뜨리고, 무방비한 상태가 되었을 때 습격한 건가요……"

        show stand_Kuka_yukata_mousou
        hide stand_Kuka_yukata_shamed

        ch_kuka "……그흐흐흐, 크헤헷…… 최면…… 세뇌……!! Tag : Mind Contr……"

        hide stand_Kuka_yukata_mousou
        show stand_Ninon_yukata_down with dissolve

        ch_ninon "정신을 공격하는 종류의 마물 입니까? 니논은 할복하면 된다 입니다만……"

        hide stand_Ninon_yukata_down

    player "……초대장에 적혀 있던…… 사람이 하루에 하나씩 사라진다는 말 있잖아."

    player "한 번에 여러 명을 공격하지는 못한다는 뜻 아닐까?"

    show stand_Monica_yukata_ddung with dissolve

    ch_monica "으음…… 확실히, 단독행동을 하지 않는다면 괜찮을지도 몰라."

    ch_monica "하지만 속단하긴 이르다. 들키지 않고 안전하게 사냥하기 위해 전략적으로 행동한 것일 수 있어."

    ch_monica "만에 하나 광역 공격이 가능한 놈이라면……"

    show stand_Monica_yukata
    hide stand_Monica_yukata_ddung

    ch_monica "……아니다. 억측에 휘둘려 군의 사기를 떨어뜨리는 건, 지휘관으로서 할 만한 행동이 아니지."

    ch_monica "이제는 직원들이 더 이상 숙소 근처를 배회하지 않는 듯하니, 우선 놈의 정체에 관한 단서를 조금 더 수집하  {nw}"

    hide stand_Monica_yukata
    show stand_Ninon_yukata_panic with dissolve

    ch_ninon "여러분~~~!!! 뭔가 찾았어요 입니다!!!!"

    ch_ninon "그, 그런데! 이상해 입니다!! 이건 분명히……"

    ch_nar "뭘 찾았길래 호들갑이야……?"

    hide stand_Ninon_yukata_panic

    show ob_akudaikan with dissolve

    play music "audio/main/emer.mp3" fadein 3.0

    ch_monica "……!!"

    player "이…… 이게 다 뭐야?"

    player "뇌관식 폭발형 건틀릿…… 단계별 각성 트리거……? 뭔 소리야 이게?"

    ch_ninon "기분이 이상해 입니다…… 이거…… 어디서 본 것 같아요 입니다……!"

    ch_kuka "이건…… 쿠, 쿠우카의 허리띠를 붙잡고 빙글빙글 돌리던……!!!"

    ch_ayumi "그, 그 마물이에요……!!"

    ch_yuki "으으…… 아름답지 못한 것들을 기억에서 지워 버리려고 얼마나 노력했는데…… 못생긴 얼굴이 다시 떠올라 버렸잖아."

    hide ob_akudaikan

    show stand_Monica_yukata_surprised with dissolve

    ch_monica "……아쿠다이칸……이라니."

    ch_monica "이 문서는 대체……"

    hide stand_Monica_yukata_surprised

    if love_point == 1 or love_point == 3:

        player "근데 쿠우카는 어느새 제정신으로 돌아온 거야……?"

        show stand_Kuka_yukata with dissolve

        ch_kuka "크흐흐…… 저걸 보니 그때의 감각이 떠올라 버려서…… 쿠케케케켓……"

        hide stand_Kuka_yukata

    else:
        player "근데 유키는 어느새 정신을 차린 거야……?"

        show stand_Yuki_yukata with dissolve

        ch_yuki "응? 나는 아까부터 거울에 비친 귀여운 나를 감상하고 있었는데…… 무슨 일 있었어~?"

        hide stand_Yuki_yukata

        ch_nar "기억을 지워 버렸어……?!"

    ch_ayumi "저기, 이건…… 설계도일까요……?"

    player "설계도……가 있다는 말은……"

    player "아쿠다이칸을 ‘만든’ 녀석이 따로 있다……는 거야?"

    show stand_Ninon_yukata_panic with dissolve:
        xalign 0.5
        easeout 0.3 ypos -50
        ease 0.2 ypos 50
        easeout 0.3 ypos -50
        ease 0.2 ypos 50 
        ##팔짝 뛰는 모션
    
    ch_ninon "Qoui!! 말도 안 돼 입니다!!"

    hide stand_Ninon_yukata_panic
    show stand_Monica_yukata_ddung with dissolve

    ch_monica "……그것만큼은 아니길 바랐건만."

    ch_monica "그래…… 놈의 배후에 다른 존재가 있었다면, 많은 게 설명이 되는군."

    ch_monica "……마물이 발생하는 요인에 대해서는 아직 정확하게 밝혀진 바가 없다."

    ch_monica "하지만 그걸 감안하더라도, 아쿠다이칸의 등장은 어딘가 부자연스러운 느낌이 강했어."

    ch_monica "동국의 전래 동화에 등장하는 악당을 본뜬 것에 불과한 기계인형이…… 아무런 연유도 없이 강력한 마물로 변모했다라……?"

    ch_monica "어째서 지금까지 이상한 점을 눈치채지 못했던 거지?"

    hide stand_Monica_yukata_ddung

    show stand_Yuki_yukata_angry with dissolve

    ch_yuki "……기모노 허리띠를 인식하면 통제불능 상태에 돌입, 최우선 목표를 기모노 허리띠로 수정……?"

    ch_yuki "확실히…… 쿠우카의 기모노를 보고 격한 반응을 보였던 거 같긴 한데, 이런 쓸데없는 기능은 왜 넣은 거야……? 징그럽고 추해…… 레알 싫다……"

    hide stand_Yuki_yukata_angry    

    show stand_Kuka_yukata_mousou with dissolve

    ch_kuka "그흐흐흐흣…… 덕분에 쿠우카는, 정통으로 벼락을 맞거나 태풍에 휘말려 높은 곳에서 내던져지거나 성층권 밖으로 날아가 버리거나 하는…… 평생 잊지 못할 쾌감을 경험하게 되었지만요……!! 크헤헷, 쿠훗훗훗훗……"

    hide stand_Kuka_yukata_mousou

    show stand_Ninon_yukata_emb with dissolve

    ch_ninon "그런데…… 아쿠다이칸 설계도 같은 것이 온천에 왜 있어 입니까…… 몰라 무서워 입니다……"

    hide stand_Ninon_yukata_emb

    show stand_Monica_yukata_ddung with dissolve

    ch_monica "……아쿠다이칸을 만든 자가…… 이곳에 있다는 것이겠지."

    ch_monica "만약…… 놈이 사람들을 공격한 마물과 동일한 존재라면……"

    show stand_Monica_yukata_down
    hide stand_Monica_yukata_ddung

    ch_monica "위험해…… 상상 이상으로 위험하다. 어떻게 상대해야할지 도저히……"

    hide stand_Monica_yukata_down

    player "……"

    player "……일단…… 우리 방으로 돌아가서 생각을 정리해 보자……"

    stop music fadeout 2.0

    show bg_black
    hide bg_onsen_heya_01
    $renpy.pause(1.0)

    show bg_naibu with fade

    play music "audio/main/5orientalcommon.mp3"

    show stand_Monica_yukata_down with dissolve

    ch_monica "……"

    hide stand_Monica_yukata_down
    show stand_Ninon_yukata with dissolve

    ch_ninon "모니카 씨~ 그렇게 쉐상 다 잃은 표정 하고 있으면 되던 일도 안 풀려요 입니다~"

    ch_ninon "달달구뤼한 과자로 기분 전환이라도……"

    play sound "audio/sound/hit.wav"

    show hit onlayer forward

    show stand_Ninon_yukata_panic
    hide stand_Ninon_yukata

    $renpy.pause(0.5)
    hide hit onlayer forward

    ch_ninon "아이코~~ 입니다!!!"

    show stand_Ninon_yukata_emb
    hide stand_Ninon_yukata_panic

    ch_ninon "미…… 미안하오 입니다!! 딴 생각을……"

    hide stand_Ninon_yukata_emb
    stop music
    show bg_naibu with hpunch

    hatena "{b}{size=30}아앙~~~~~??!!!{/size}{/b}"

    show npc_2 with dissolve

    play music "audio/main/11fun.mp3"

    show bg_naibu with hpunch

    ch_head "이런 건방진 자식이…… 사과하면 다인 줄 알아?!?!!"

    hide npc_2
    show stand_Ninon_yukata_emb with dissolve

    ch_ninon "아, 아우우…… 이걸로는 부족하다 입니까? 그, 그렇다면……「인법 {font=NanumGothic.ttf}·{/font} 동국 트뤠디셔널 도게자」를……!!"

    show stand_Ninon_yukata_emb:
        linear 0.5 ypos 1400

    $renpy.pause(2.0)

    show bg_naibu with hpunch

    hide stand_Ninon_yukata_emb
    show npc_2 with dissolve

    ch_head "장난하냐!!!!!!!"

    hide npc_2
    
    show stand_Ninon_yukata_innocent with dissolve:
        xalign 0.5 ypos 250
    
    show stand_Ninon_yukata_innocent:
        linear 0.5 ypos 0
    
    ch_ninon "우우…… 「인법{font=NanumGothic.ttf} · {/font}동국 트뤠디셔널 도게자」가 통하지 않는다니…… 이보다 더한 것을 요구할 셈인가요 입니다!!"

    hide stand_Ninon_yukata_innocent

    show stand_Kuka_yukata_mousou with dissolve

    ch_kuka "그, 그보다 더한 것이라면…… 알몸 도게자?!!?!"

    ch_kuka "드…… 드디어 도S 씨의 라이벌이 등장하고 만 건가요!!!! 쿠케케케케!!!!"

    hide stand_Kuka_yukata_mousou

    show npc_2 with dissolve

    ch_head "햐~~~하핫하~~~!!!!! 네 녀석들, 어물쩍 넘어갈 생각하지 마라!!!"

    ch_head "이 몸은 오에도 최악의 자해공갈범!!!!!"

    hide npc_2

    ch_ayumi "그…… 그걸 말해 버리면 더 이상 자해공갈이 아니게 되는 것 아닌가요?!"

    show npc_2 with dissolve

    ch_head "얼마나 최악이냐 하면…… 지나가던 꼬맹이와 일부러 부딪혀서, 녀석이 빨고 있던 사탕을 뺏어 먹을 정도지!!!"

    hide npc_2

    show stand_Monica_yukata_down with dissolve

    ch_monica "그…… 그냥 미친놈이잖나……!!"

    hide stand_Monica_yukata_down

    show stand_Ninon_yukata_angry with dissolve

    ch_ninon "나쁜놈 이었습니까……?!! 못된 악당은 처단한다 입니다!!!"

    hide stand_Ninon_yukata_angry

    show npc_2 with dissolve

    ch_head "뭐……?! 이, 이 자시익~~!!!! 방금 네놈과 부딪혀서 생긴 피멍이 보이지 않는 거냐!!!!"

    hide npc_2

    show stand_Ninon_yukata_angry with dissolve

    ch_ninon "뭐가 보인다는 거냐 입니다~~~!!!! 까매서 아무것도 안 보인다 입니다!!!!!"

    hide stand_Ninon_yukata_angry

    player "니논!!! 그건 논란의 여지가 될 수 있는 발언이야!!!!"

    show stand_Ninon_yukata_angry with dissolve

    ch_ninon "받아 보거라 입니다!!! 「인법{font=NanumGothic.ttf} · {/font}가뢔떡 나박썰기」!!!!"

    hide stand_Ninon_yukata_angry

    show npc_2 with dissolve

    ch_head "크아아아아악!!!!"

    hide npc_2

    show bg_black
    hide bg_naibu

    play sound "audio/sound/knife2.wav"
    show knife_issen

    $renpy.pause(0.5)

    show bg_naibu
    hide knife_issen
    hide bg_black

    show npc_4 with dissolve

    ch_head_2 "히이~~~~~이이익!!!!!"

    ch_head_2 "내…… 내 리젠트가아아~~~!!!!!"

    hide npc_4

    show stand_Yuki_yukata_angry with dissolve

    ch_yuki "으윽…… 애매하게 잘려 나가서 더 흉물스러워……"

    hide stand_Yuki_yukata_angry

    show stand_Ninon_yukata_daiji with dissolve

    ch_ninon "후…… 또 시시한 걸 베어 버렸군 입니다."

    hide stand_Ninon_yukata_daiji

    show npc_4 with dissolve

    ch_head_2 "죄송함다, 죄송함다!!!! 목숨만 살려주십쇼~~~!!!!"

    hide npc_4

    show stand_Ninon_yukata with dissolve

    ch_ninon "나쁜놈 씨, 잘못을 뉘우취십시오 입니다~! 또 못된 짓 할 거다 입니까?"

    hide stand_Ninon_yukata

    show npc_4 with dissolve

    ch_head_2 "잘모씀다!! 잘모씀다~~!!!! 다시는 이런 일……"

    ch_head_2 "……어라라?"

    ch_head_2 "그쪽에 있는 아재, 혹시……"

    stop music

    ch_head_2 "……쇼군?"

    hide npc_4

    show stand_Monica_yukata_surprised with dissolve

    ch_monica "……!!!!"

    hide stand_Monica_yukata_surprised

    ch_nar "어……?"

    show npc_4 with dissolve

    ch_head_2 "아…… 아무것도 아님다!!!! 잘못 봐씀다!!!!"

    ch_head_2 "저, 저는 이만……!!!!"

    show npc_4:
        linear 0.3 xpos -1000
    $renpy.pause(0.5)

    hide npc_4

    show stand_Ninon_yukata_surp with dissolve

    ch_ninon "쇼군……?! 잠깐 기다…… 웁!"

    hide stand_Ninon_yukata_surp

    show stand_Monica_yukata_ddung with dissolve

    ch_monica "니논!!! 멈춰라!!!"

    hide stand_Monica_yukata_ddung

    show stand_Ninon_yukata_surp with dissolve

    ch_ninon "모니카 씨?! 왜……!!"

    hide stand_Ninon_yukata_surp

    show stand_Monica_yukata_ddung with dissolve

    ch_monica "단독행동은 금지라고 하지 않았나!! 혼자서 뭘 어쩌려고 한 거냐!"

    hide stand_Monica_yukata_ddung

    show stand_Ninon_yukata_down with dissolve

    ch_ninon "그…… 그취만…… 저 솨람, 쇼군을 알아보……"

    hide stand_Ninon_yukata_down

    show stand_Monica_yukata_ddung with dissolve

    ch_monica "직원이 아니야…… 오에도 주민일 수도 있다."

    ch_monica "……그리고, 만약 함정이라면 어떻게 할 거였나!! 모두를 위험에 빠뜨릴 셈인가?!"

    hide stand_Monica_yukata_ddung

    show stand_Ninon_yukata_innocent with dissolve

    ch_ninon "우우웃……"

    ch_ninon "죄…… 죄송해요 입니다……"

    hide stand_Ninon_yukata_innocent

    show stand_Kuka_yukata with dissolve

    ch_kuka "알몸 도게자……! 알몸 도게자……!!"

    hide stand_Kuka_yukata

    show stand_Yuki_yukata_ddung with dissolve

    ch_yuki "뭐…… 따라가지 않았으니 된 거잖아? 얼른 방에 가자~ 이제 그만 쉬고 싶다구……"

    hide stand_Yuki_yukata_ddung

    show stand_Monica_yukata_down with dissolve

    ch_monica "가더라도 쉴 수는 없을 테지만…… 알겠다."

    ch_monica "……너무 서운해하지 마라, 니논. 모두를 위해서였다."

    hide stand_Monica_yukata_down

    show stand_Ninon_yukata_innocent with dissolve

    ch_ninon "힝힝…… 입니다."

    hide stand_Ninon_yukata_innocent

    $ persistent.clues_yanki = True
    $ persistent.clues_akudaikan = True
    show screen clueFinded
    show bg_black
    hide bg_naibu
    $renpy.pause(2.0)


    jump scene21Common

## S# 21. 온천 숙소 (다다미 방) (공통 루트)#############
label scene21Common:
    scene bg_tadami_day

    play music "audio/main/5orientalcommon.mp3"

    show stand_Yuki_yukata_shamed with dissolve

    ch_yuki "흐아아아아~ 스위트홈~♪"

    hide screen clueFinded

    show stand_Yuki_yukata
    hide stand_Yuki_yukata_shamed

    ch_yuki "성에 찰 정도로 편안하진 않지만…… 귀여운 내가 있으니, 이 공간마저 금세 아름다워지겠지."

    hide stand_Yuki_yukata

    show stand_Kuka_yukata_mousou with dissolve

    ch_kuka "머지않아 도S 씨와 몸을 섞을 거라는 생각에 두근거림이 멈추지 않아요……!"

    hide stand_Kuka_yukata_mousou

    ch_nar "섞인 건 니 머릿속 우동사리겠지……!"

    show stand_Monica_yukata_down with dissolve

    ch_monica "……그나저나, 고민이군……"

    ch_monica "지금까지 수집한 단서들에 의하면…… 상대는 엄청나게 위험한 마물인데,"

    ch_monica "정작 놈의 정체에 대해서는 아무런 실마리도 찾지 못했어……"

    hide stand_Monica_yukata_down
    
    player "하루 정도 더 머물면서 단서를 찾아보는 건 어때?"

    show stand_Ninon_yukata with dissolve

    ch_ninon "니논은 찬성 입니다~!"

    hide stand_Ninon_yukata

    show stand_Monica_yukata_down with dissolve

    ch_monica "아무래도…… 그럴 수밖에 없을 것 같군."

    hide stand_Monica_yukata_down

    show stand_Yuki_yukata_ddung with dissolve

    ch_yuki "나머지는 내일 생각하면 안 될까……? 이 이상 잠을 자지 못한다면 내 아름다움에 치명적인 타격이 갈지도 모른다구우……"

    hide stand_Yuki_yukata_ddung

    show stand_Monica_yukata_ddung with dissolve

    ch_monica "흐음…… 마음 편히 쉴 때가 아닌 것 같지만, 일단 휴식하도록 할까."

    ch_monica "수면 부족은 전투에도 악영향을 미치니까 말이야."

    hide stand_Monica_yukata_ddung

    ch_ayumi "그런데…… 모두가 잠들어 있을 때에 마물이 습격해 오면 어떻게 하죠……?"

    show stand_Monica_yukata_surprised with dissolve

    ch_monica "……!! 그것도 그렇군."

    show stand_Monica_yukata_ddung
    hide stand_Monica_yukata_surprised

    ch_monica "으음…… 뭔가 좋은 방법이……"

    hide stand_Monica_yukata_ddung

    player "불침번을 서는 건 어떨까……?"

    show stand_Yuki_yukata_angry with dissolve

    ch_yuki "{b}{size=30}엑.{/size}{/b}"

    hide stand_Yuki_yukata_angry
    show stand_Ninon_yukata with dissolve

    ch_ninon "오오~ 쇼군~!! IDEA BANK 입니까~?"

    hide stand_Ninon_yukata
    show stand_Kuka_yukata with dissolve

    ch_kuka "부…… 불침번?! 「오늘 밤은 너를 재우지 않겠어」 인가요!!!! 이 얼마나 절륜한……!!!"

    hide stand_Kuka_yukata
    show stand_Monica_yukata with dissolve

    ch_monica "나쁘지 않은 생각이야. 불침번이라면……"

    ch_monica "혼자서는 위험할지도 모르니, 두 명 정도가 적당할 것 같군."

    hide stand_Monica_yukata

    show stand_Yuki_yukata_angry with dissolve

    ch_yuki "으으…… 나는 빼 주면 안 될까……?"

    hide stand_Yuki_yukata_angry
    show stand_Ninon_yukata_daiji with dissolve

    ch_ninon "……안 내면."

    hide stand_Ninon_yukata_daiji

    player "으응……?"

    show stand_Ninon_yukata_daiji with dissolve

    ch_ninon "안 내면 진다!!!!! 가위바위보!!!!!!!!!!!"

    hide stand_Ninon_yukata_daiji

    show stand_Yuki_yukata_shamed with dissolve

    ch_yuki "우…… 우아아악~~~!!! 잠깐만!!!!!"

    hide stand_Yuki_yukata_shamed

    show bg_black
    hide bg_tadami_day

    $renpy.pause(2.0)

    show bg_tadami_day
    hide bg_black

    if love_point == 1:
        show stand_Ninon_yukata_panic with dissolve

        ch_ninon "으엑……!! 졌다 입니다……?!"

        hide stand_Ninon_yukata_panic

        player "윽, 나도……?!"

        show stand_Yuki_yukata_shamed with dissolve

        ch_yuki "휘유…… 다행이다……"

        hide stand_Yuki_yukata_shamed
        show stand_Monica_yukata_munen with dissolve

        ch_monica "……정해진 것 같군."

        ch_monica "그럼 잘 부탁한다, 제군들……!!"

        hide stand_Monica_yukata_munen

        show stand_Ninon_yukata_emb with dissolve

        ch_ninon "쇼…… 쇼군과 함께라면, 얼마든지 힘내겠소 입니다……!!"

        hide stand_Ninon_yukata_emb

    elif love_point == 2:
        show stand_Monica_yukata_surprised with dissolve

        ch_monica "크윽……!! 졌다!!!"

        hide stand_Monica_yukata_surprised

        player "윽, 나도……?!"

        show stand_Yuki_yukata_shamed with dissolve

        ch_yuki "휘유…… 다행이다……"

        hide stand_Yuki_yukata_shamed

        show stand_Monica_yukata_down with dissolve

        ch_monica "어쩔 수 없군……"

        show stand_Monica_yukata
        hide stand_Monica_yukata_down

        ch_monica "이렇게 된 이상 잘 부탁한다, 귀공!"

    elif love_point == 3:
        show stand_Kuka_yukata_surprised with dissolve

        ch_kuka "히이익……!! 져 버렸어요……?!"

        hide stand_Kuka_yukata_surprised
        
        player "윽, 나도……?!"

        show stand_Yuki_yukata_shamed with dissolve

        ch_yuki "휘유…… 다행이다……"

        hide stand_Yuki_yukata_shamed

        show stand_Monica_yukata_munen with dissolve

        ch_monica "……정해진 것 같군."

        ch_monica "그럼 잘 부탁한다, 제군들……!!"

        hide stand_Monica_yukata_munen

        show stand_Kuka_yukata_mousou with dissolve

        ch_kuka "스…… 승부에서 패배한 히로인은 밤새 어떤 수모를 당하게 될까요!!!! 상상만 해도 온몸이 떨려…… 크헤헤헤헷……!!!!"

        hide stand_Kuka_yukata_mousou
    
    else:
        show stand_Yuki_yukata_angry with dissolve

        ch_yuki "으아악……!! 안돼!!!!"

        hide stand_Yuki_yukata_angry

        player "윽, 졌어……?!"

        show stand_Monica_yukata_munen with dissolve

        ch_monica "……정해진 것 같군."

        ch_monica "그럼 잘 부탁한다, 제군들……!!"

        hide stand_Monica_yukata_munen

        show stand_Yuki_yukata_angry with dissolve

        ch_yuki "으으으…… 8시간 이상 잠을 자지 않으면 안 되는데……"

        show stand_Yuki_yukata_ddung

        hide stand_Yuki_yukata_angry

        ch_yuki "……너와 함께라서 그나마 다행이지만……"

        ch_yuki "귀여운 나를 에스코트할 수 있는 걸 영광으로 알아! 밤새도록 나를 제대로 책임져 달라구. 알겠어?"

        hide stand_Yuki_yukata_ddung
        show stand_Kuka_yukata_mousou with dissolve

        ch_kuka "다, 다다단둘이서 밤새도록……!! 후히히힛……!!"
        hide stand_Kuka_yukata_mousou
    
    show stand_Monica_yukata_ddung with dissolve

    ch_monica "그나저나……"

    ch_monica "오늘 하루, 꽤 많은 걸 보고 들은 것 같은데……"

    ch_monica "귀공은 어떻게 생각하나?"

    hide stand_Monica_yukata_ddung

    player "어? 나 말이야?"

    show stand_Monica_yukata_ddung with dissolve

    ch_monica "음. 사소한 것이라도 좋으니, 귀공의 의견을 듣고 싶다."

    ch_monica "오늘 조우한 인물들 중, 의심이 가는 이는 없던가?"

    hide stand_Monica_yukata_ddung

    player "……의심이 간다라고 하면……"

    show stand_Monica_yukata_ddung with dissolve

    ch_monica "……‘마물’로 보이는 존재가 있었나, 라는 질문이다."

    hide stand_Monica_yukata_ddung

    player "음……"

    menu:
        "‘여직원’이 의심스럽다choice_1":
            pass
        "     ‘머리가 대단한 손님’이 의심스럽다choice_2":
            pass
        "‘역겹게 생긴 짐승’이 의심스럽다choice_3":
            pass
    
    stop music
    $renpy.pause(2.0)

    hatena "……킥……"

    play sound "audio/sound/doorclose.mp3"

    show bg_tadami_night with fade

    hide bg_tadami_day

    $renpy.pause(1.0)

    play sound "audio/sound/breathe.mp3" loop

    ch_nar "……어……?"

    ch_nar "이게……"

    ch_nar "무……슨……"

    stop sound
    play sound "audio/sound/down.mp3"
    show bg_black
    hide bg_tadami_night
    
    $renpy.pause(3.0)

    jump scene22Common

## S# 22. 다다미 방 (밤) (공통 루트) ########
label scene22Common:

    scene bg_tadami_night with fade

    ch_nar "…………"

    player "아윽……"

    ch_nar "머리가……"

    ch_nar "머리가…… 깨질 것 같아."

    ch_nar "몸이…… 이상해. 뜨거워……"

    if love_point == 1:

        ch_nar "잠깐, 그런데…… 다들 어디 간 거야……?"

        ch_nar "……불침번을 서기로 했던 니논도 보이지 않아……?"

        ch_nar "뭐가 뭔지 모르겠어…… 일단 니논을 찾으러 가야……"

        menu:
            "여탕으로 이동한다choice_1":
                ch_nar "그래…… 여탕으로 가 보자……"

                ch_nar "이유는 모르겠지만…… 그곳에 있을 것만 같은 느낌이 들어……"

            "화장실로 이동한다choice_2":
                ch_nar "그래…… 화장실에 가 보자……"

                ch_nar "이유는 모르겠지만…… 화장실에 있을 것만 같은 느낌이 들어……"

            "혼욕탕으로 이동한다choice_3":
                ch_nar "그래…… 혼욕탕으로 가 보자……"

                ch_nar "이유는 모르겠지만…… 그곳에 있을 것만 같은 느낌이 들어……"
    elif love_point == 2:

        ch_nar "잠깐, 그런데…… 다들 어디 간 거야……?"

        ch_nar "……불침번을 서기로 했던 모니카도 보이지 않아……?"

        ch_nar "뭐가 뭔지 모르겠어…… 일단 모니카를 찾으러 가야……"

        menu:
            "여탕으로 이동한다choice_1":
                $point_monica -= 1
                ch_nar "그래…… 여탕으로 가 보자……"

                ch_nar "이유는 모르겠지만…… 그곳에 있을 것만 같은 느낌이 들어……"

            "화장실로 이동한다choice_2":
                ch_nar "그래…… 화장실에 가 보자……"

                ch_nar "이유는 모르겠지만…… 화장실에 있을 것만 같은 느낌이 들어……"

            "혼욕탕으로 이동한다choice_3":
                $point_monica += 1
                ch_nar "그래…… 혼욕탕으로 가 보자……"

                ch_nar "이유는 모르겠지만…… 그곳에 있을 것만 같은 느낌이 들어……"
                
    elif love_point == 3:

        ch_nar "잠깐, 그런데…… 다들 어디 간 거야……?"

        ch_nar "……불침번을 서기로 했던 쿠우카도 보이지 않아……?"

        ch_nar "뭐가 뭔지 모르겠어…… 일단 쿠우카를 찾으러 가야……"

        menu:
            "여탕으로 이동한다choice_1":
                $point_kuka -= 1
                ch_nar "그래…… 여탕으로 가 보자……"

                ch_nar "이유는 모르겠지만…… 그곳에 있을 것만 같은 느낌이 들어……"

            "화장실로 이동한다choice_2":
                ch_nar "그래…… 화장실에 가 보자……"

                ch_nar "이유는 모르겠지만…… 화장실에 있을 것만 같은 느낌이 들어……"

            "혼욕탕으로 이동한다choice_3":
                $point_kuka += 1
                ch_nar "그래…… 혼욕탕으로 가 보자……"

                ch_nar "이유는 모르겠지만…… 그곳에 있을 것만 같은 느낌이 들어……"
    
    else:

        ch_nar "잠깐, 그런데…… 다들 어디 간 거야……?"

        ch_nar "……불침번을 서기로 했던 유키도 보이지 않아……?"

        ch_nar "뭐가 뭔지 모르겠어…… 일단 유키를 찾으러 가야……"

        menu:
            "여탕으로 이동한다choice_1":
                $point_yuki -= 1
                ch_nar "그래…… 여탕으로 가 보자……"

                ch_nar "이유는 모르겠지만…… 그곳에 있을 것만 같은 느낌이 들어……"

            "화장실로 이동한다choice_2":
                ch_nar "그래…… 화장실에 가 보자……"

                ch_nar "이유는 모르겠지만…… 화장실에 있을 것만 같은 느낌이 들어……"

            "혼욕탕으로 이동한다choice_3":
                $point_yuki += 1
                ch_nar "그래…… 혼욕탕으로 가 보자……"

                ch_nar "이유는 모르겠지만…… 그곳에 있을 것만 같은 느낌이 들어……"
    
    hide bg_tadami_night
    jump scene23Common

## S# 23. 온천 건물 내부 (2) ##################
label scene23Common:
    scene bg_onsen_dark with fade

    play sound "audio/sound/bbiguk.wav" loop

    ch_nar "……"

    ch_nar "……뭔가 이상하다……"

    ch_nar "이렇게까지 조용한 곳이었나……?"

    ch_nar "아무런 소리도 들리지 않는다……"

    ch_nar "……낡아 빠진 마룻바닥이 규칙적으로 내지르는 비명소리를 제외하면."

    ch_nar "섬뜩하다. 이 세상에 나 혼자만 남겨진 것 같다."

    ch_nar "마치 꿈을 꾸는 것만 같   {nw}"

    stop sound

    if love_point == 1:
        play sound "audio/sound/surp.mp3"

        show bg_onsen_dark onlayer middle
        show stand_Ninon_yukata_surp onlayer forward with dissolve

        $camera_move(0, -1000, 400, 0, 0.2)

        ch_ninon "{b}{size=30}쇼군!!!!!{/size}{/b}"

        $camera_move(0, 0, 0, 0, 0)
        hide stand_Ninon_yukata_surp onlayer forward
        hide bg_onsen_dark onlayer middle

        player "{b}{size=30}으아아악!!!!!{/size}{/b}"

        show stand_Ninon_yukata_surp with dissolve

        ch_ninon "이런 곳에서 혼자 뭘 하시나요 입니다?!"

        hide stand_Ninon_yukata_surp

        player "뭐, 뭘 하냐니……"

        player "널 찾으러 다녔는데…… 그러는 너는 왜 여기 있는 거야……?"

        show stand_Ninon_yukata_down with dissolve

        ch_ninon "니논도 잘 모르겠소 입니다……"

        ch_ninon "갑자기 머엉~ 하다가…… 정신을 차려 보니 이곳에……"

        hide stand_Ninon_yukata_down
        stop sound
        play sound "audio/sound/running.mp3"

        player "?!?!?!?!?!"

        show stand_Ninon_yukata_panic with dissolve

        ch_ninon "무…… 무슨 소리 입니까?!?!"

        hide stand_Ninon_yukata_panic

        play sound "audio/sound/monkey.mp3"

        hatena "끼에!!!!! 끼에에!!! 끼아아아아악!!!!!!!!"

        show ob_yas1 with dissolve
        show ob_yas2 with dissolve

        $renpy.pause(2.0)

        play sound "audio/sound/monkey2.mp3"

        monster "{b}{size=30}야스각이다!!!! 야스각!!!!!{/size}{/b}"

        play sound "audio/sound/hit.wav"

        show hit

        $renpy.pause(2.0)

        hide hit

        hide ob_yas1
        hide ob_yas2

        show bg_black

        hide bg_onsen_dark

        $renpy.pause(2.0)

        jump cg_ninonsecond

    elif love_point == 2:
        play sound "audio/sound/surp.mp3"

        show bg_onsen_dark onlayer middle
        show stand_Monica_yukata_surprised onlayer forward with dissolve

        $camera_move(0, -1000, 400, 0, 0.2)

        ch_monica "{b}{size=30}귀공!!!!!{/size}{/b}"

        $camera_move(0, 0, 0, 0, 0)
        hide stand_Monica_yukata_surprised onlayer forward
        hide bg_onsen_dark onlayer middle

        player "{b}{size=30}으아아악!!!!!{/size}{/b}"

        show stand_Monica_yukata_surprised with dissolve

        ch_monica "이런 곳에서 혼자 뭘 하고 있나?!"

        hide stand_Monica_yukata_surprised

        player "뭐, 뭘 하냐니……"

        player "널 찾으러 다녔는데…… 그러는 너는 왜 여기 있는 거야……?"

        show stand_Monica_yukata_down with dissolve

        ch_monica "……실은, 나도 잘 모르겠다."

        ch_monica "갑자기 정신이 혼미해졌다가…… 정신을 차려 보니 이곳에……"

        hide stand_Monica_yukata_down
        stop sound
        play sound "audio/sound/running.mp3"

        player "?!?!?!?!?!"

        show stand_Monica_yukata_surprised with dissolve

        ch_monica "무…… 무슨 소리냐?!?!"

        hide stand_Monica_yukata_surprised

        play sound "audio/sound/monkey.mp3"

        hatena "끼에!!!!! 끼에에!!! 끼아아아아악!!!!!!!!"

        show ob_yas1 with dissolve

        $renpy.pause(2.0)

        play sound "audio/sound/monkey2.mp3"

        monster "{b}{size=30}야스각이다!!!! 야스각!!!!!{/size}{/b}"

        play sound "audio/sound/hit.wav"

        show hit

        $renpy.pause(2.0)

        hide hit

        hide ob_yas1
        hide ob_yas2

        show bg_black

        hide bg_onsen_dark

        $renpy.pause(2.0)

        jump cg_monicasecond

    elif love_point == 3:
        play sound "audio/sound/surp.mp3"

        show bg_onsen_dark onlayer middle
        show stand_Kuka_yukata_surprised onlayer forward with dissolve

        $camera_move(0, -1000, 400, 0, 0.2)

        ch_kuka "{b}{size=30}도S 씨!!!!!{/size}{/b}"

        $camera_move(0, 0, 0, 0, 0)
        hide stand_Kuka_yukata_surprised onlayer forward
        hide bg_onsen_dark onlayer middle

        player "{b}{size=30}으아아악!!!!!{/size}{/b}"

        show stand_Kuka_yukata_surprised with dissolve

        ch_kuka "이런 곳에서 혼자 뭘 하고 계시나요?!"

        hide stand_Kuka_yukata_surprised

        player "뭐, 뭘 하냐니……"

        player "널 찾으러 다녔는데…… 그러는 너는 왜 여기 있는 거야……?"

        show stand_Kuka_yukata_down with dissolve

        ch_kuka "쿠, 쿠우카도 잘 모르겠어요……"

        ch_kuka "갑자기 꿈을 꾸듯 황홀한 기분이 되었다가…… 정신을 차려 보니 이곳에……"

        hide stand_Kuka_yukata_down
        stop sound
        play sound "audio/sound/running.mp3"

        player "?!?!?!?!?!"

        show stand_Kuka_yukata_surprised with dissolve

        ch_monica "무…… 무슨 소리예요?!"

        hide stand_Kuka_yukata_surprised

        play sound "audio/sound/monkey.mp3"

        hatena "끼에!!!!! 끼에에!!! 끼아아아아악!!!!!!!!"

        show ob_yas1 with dissolve
        show ob_yas2 with dissolve

        $renpy.pause(2.0)

        play sound "audio/sound/monkey2.mp3"

        monster "{b}{size=30}야스각이다!!!! 야스각!!!!!{/size}{/b}"

        play sound "audio/sound/hit.wav"

        show hit

        $renpy.pause(2.0)

        hide hit

        hide ob_yas1
        hide ob_yas2

        show bg_black

        hide bg_onsen_dark

        $renpy.pause(2.0)

        jump cg_kukasecond
    
    else:
        play sound "audio/sound/surp.mp3"

        show bg_onsen_dark onlayer middle
        show stand_Yuki_yukata_shamed onlayer forward with dissolve

        $camera_move(0, -1000, 400, 0, 0.2)

        ch_yuki "{b}{size=30}[name]!!!!!{/size}{/b}"

        $camera_move(0, 0, 0, 0, 0)
        hide stand_Yuki_yukata_shamed onlayer forward
        hide bg_onsen_dark onlayer middle

        player "{b}{size=30}으아아악!!!!!{/size}{/b}"

        show stand_Yuki_yukata_shamed with dissolve

        ch_yuki "이런 곳에서 혼자 뭘 하고 있는 거야?!"

        hide stand_Yuki_yukata_shamed

        player "뭐, 뭘 하냐니……"

        player "널 찾으러 다녔는데…… 그러는 너는 왜 여기 있는 거야……?"

        show stand_Yuki_yukata_ddung with dissolve

        ch_yuki "그게…… 나도 잘 모르겠어."

        ch_yuki "갑자기 나의 아름다움에 취한 듯 야릇한 기분이 되었다가…… 정신을 차려 보니 이곳에……"

        hide stand_Yuki_yukata_ddung
        stop sound
        play sound "audio/sound/running.mp3"

        player "?!?!?!?!?!"

        show stand_Yuki_yukata_shamed with dissolve

        ch_yuki "으……으아악!!! 무슨 소리야?!?!"

        hide stand_Yuki_yukata_shamed

        play sound "audio/sound/monkey.mp3"

        hatena "끼에!!!!! 끼에에!!! 끼아아아아악!!!!!!!!"

        show ob_yas1 with dissolve
        show ob_yas2 with dissolve

        $renpy.pause(2.0)

        play sound "audio/sound/monkey2.mp3"

        monster "{b}{size=30}야스각이다!!!! 야스각!!!!!{/size}{/b}"

        play sound "audio/sound/hit.wav"

        show hit

        $renpy.pause(2.0)

        hide hit

        hide ob_yas1
        hide ob_yas2

        show bg_black

        hide bg_onsen_dark

        $renpy.pause(2.0)

        jump cg_yukisecond



## S# 25. 다다미 방 (공통루트) ##################
label scene25Common:

    if love_point == 1:
        $point = point_ninon
    elif love_point == 2:
        $point = point_monica
    elif love_point == 3:
        $point = point_kuka
    else:
        $point = point_yuki
    scene bg_tadami_day with fade

    play music "audio/main/5orientalcommon.mp3"

    show stand_gura with dissolve

    ch_gura "이야~ 설마하니 정말로 놈들을 무찌를 줄이야!!!!"

    show bg_tadami_day at fast_rotating

    ch_gura "이 구라노스케!!!!! 너무나도 황송하여 몸 둘 바를 모르겠슴다{font=NanumGothic.ttf}————{/font}앗!!!!"

    hide stand_gura

    player "그나저나…… 사라진 사람들은 어떻게 됐어?"

    player "그것도 그 원숭이들의 짓이지……?"

    show ob_yas2_trans with dissolve

    monster "침팬지야, 병신아……!"

    hide ob_yas2_trans

    show stand_gura with dissolve

    ch_gura "아…… 그들에 대해서는 걱정하실 것 없습니다!"

    ch_gura "전부 살아 돌아왔으니까요!!"

    hide stand_gura

    show stand_Monica_yukata_surprised with dissolve

    ch_monica "뭐……?! 모두 살아 있었단 말인가?!"

    hide stand_Monica_yukata_surprised
    show stand_Ninon_yukata_panic with dissolve
    ch_ninon "유…… 유혈이 낭좌한 편지를 남긴 직원 씨도 살아 있다는 겁뉘까?!"

    hide stand_Ninon_yukata_panic
    show stand_gura with dissolve

    ch_gura "그렇습니다!!! 단 한 명도 빠짐없이 돌아왔습니다!!!"

    hide stand_gura

    player "그 정도로 피를 잔뜩 쏟았는데, 살아 있었다고……?!"

    show stand_gura onlayer middle with dissolve

    ch_gura "아, 그게……"

    ch_gura "그 피는 사실……"

    $camera_move(0, 0, 400, 0, 1)

    ch_gura "{b}……야한 것을 보고 코피를 뿜은 거였다고 하더군요……{/b}"

    $camera_move(0, 0, 0, 0, 0)
    hide stand_gura onlayer middle

    show stand_Yuki_yukata_angry with dissolve

    ch_yuki "………"

    hide stand_Yuki_yukata_angry

    show stand_Kuka_yukata_mousou with dissolve

    ch_kuka "대…… 대체 뭘 봤길래……!!! 정말 부러워요!!!!"

    hide stand_Kuka_yukata_mousou

    show stand_gura with dissolve

    ch_gura "놈들은 사람들을 하나둘씩 잡아간 뒤, 정신을 조종하여 야릇한 기분으로 만들어 버렸다고 합니다."

    ch_gura "코피를 흘린 것은 그 과정에서 있었던 일이고요."

    ch_gura "그나마 사람을 잡아먹는 마물이 아니었기에 망정이지…… 하마터면 대참사가 일어날 뻔했습니다."

    hide stand_gura
    show stand_Ninon_yukata_panic with dissolve

    ch_ninon "그…… 그럼, 사라졌던 사람들은 전부 어딘가에서 잉챠잉챠……!!"

    hide stand_Ninon_yukata_panic

    show stand_gura with dissolve

    ch_gura "……네, 뭐……"

    hide stand_gura

    show stand_Kuka_yukata_mousou with dissolve

    ch_kuka "그…… 그런 주지육림이 현실에 존재했다니!!! 쿠우카가 잡혀갔었어야 했는데……!!!!"

    hide stand_Kuka_yukata_mousou

    player "개부럽네……"

    show stand_Monica_yukata_down with dissolve

    ch_monica "어쨌든, 인명 피해 없이 끝나서 다행이다…… 하아암……"

    hide stand_Monica_yukata_down
    show stand_gura with dissolve

    ch_gura "앗…… 그러고보니 시간이 벌써 이렇게!!"

    ch_gura "죄송합니다! 일이 잘 해결되어 너무 기쁜 나머지……!!"

    ch_gura "그러면, 자세한 이야기는 내일 마저 나누도록 하죠. 이만 푹 쉬십쇼!!"

    play sound "audio/sound/doorclose.mp3"

    hide stand_gura with dissolve

    player "……저기, 모니카."

    show stand_Monica_yukata_down with dissolve

    ch_monica "하으…… 으음……? 나를 불렀나, 귀공……?"

    hide stand_Monica_yukata_down

    player "우리…… 하루만 더 놀다 갈까?"

    show stand_Monica_yukata_ddung with dissolve

    ch_monica "……뭐라?"

    ch_monica "우리가 특훈을 위해 이곳에 왔다는 것을 잊은 건 아니겠지……?"

    ch_monica "마물을 퇴치했다고 끝난 것이 아닌……"

    hide stand_Monica_yukata_ddung
    show stand_gura with dissolve

    show bg_tadami_day at fast_rotating

    ch_gura "그렇게 하십쇼{font=NanumGothic.ttf}—————{/font}옷!!!!!!!!"

    player "뭐야!!! 안 갔어?!?!"

    ch_gura "하루 정도는 괜찮지 않습니까? 이대로 여러분을 보내드리는 건 저희에게 있어서도 도리가 아닌 것 같기도 하고요."

    hide stand_gura
    show stand_Monica_yukata_ddung with dissolve

    ch_monica "하지만, 우리에게는 그럴 여유가……"

    hide stand_Monica_yukata_ddung
    show stand_gura onlayer middle with dissolve
    show highlight onlayer forward

    $camera_move(0, 0, 400, 0, 0.5)

    ch_gura "{b}{size=30}한정판 화과자를 무한정 제공해드리겠습니다.{/size}{/b}"

    hide stand_gura onlayer middle
    show stand_Monica_yukata onlayer middle with dissolve

    ch_monica "하루 정도야 문제없지."

    $camera_move(0, 0, 0, 0, 0)
    hide highlight onlayer forward
    hide stand_Monica_yukata onlayer middle

    show stand_gura with dissolve

    ch_gura "제대로 대우해 드리지 못한 것이 마음에 걸렸는데…… 부디 내일 하루만이라도 편하게 즐기시다 가십쇼!"

    ch_gura "이제는 그 원숭이 녀석들도 없으니까요."

    hide stand_gura
    show ob_yas3_trans with dissolve

    monster "아 씹빨!!!!! 원숭이 아니라고!!!!!"

    hide ob_yas3_trans
    show stand_gura with dissolve

    ch_gura "그럼, 최고로 극진한 대접을 기대해 주시길 바라며……"

    show bg_tadami_day at fast_rotating

    ch_gura "이만 편히 쉬십쇼{font=NanumGothic.ttf}————{/font}옷!!!!"

    hide stand_gura
    show bg_black
    hide bg_tadami_day

    $renpy.pause(2.0)

    stop music

    jump scene26Common
## S# 26. 랜드솔 마을 (공통 루트) ##########################
label scene26Common:
    ch_nar "며칠 뒤……"

    show bg_town with fade

    play music "audio/main/3town.mp3"

    show stand_Ninon with dissolve

    ch_ninon "홍~ 호홍~ 호호홍~~"

    show stand_Ninon_wink
    hide stand_Ninon

    ch_ninon "……앗! 쇼군 입니다~ 안녕 입니다?"

    hide stand_Ninon_wink
    show stand_Yuki with dissolve

    ch_yuki "[name]~ 거기서 뭐해?"

    hide stand_Yuki

    player "숨셔."

    player "너희는 어디 가는 길이야?"

    show stand_Monica with dissolve

    ch_monica "음……! 귀공인가. 모두 함께 프라노 평원으로 훈련을 하러 가는 참이었다."

    hide stand_Monica
    show stand_Kuka with dissolve

    ch_kuka "쿠쿠쿳…… 오늘도 쿠우카는 마물들에게 둘러싸여 잔뜩 얻어맞을 거예요……!!! 크히히히……"

    hide stand_Kuka

    player "돌아온지 얼마 되지도 않았는데, 되게 열심이네."

    show stand_Monica_ddung with dissolve

    ch_monica "오히려 더 노력해야 할 때다! 흐름이 끊기면 안 되니까 말이야."

    hide stand_Monica_ddung

    show stand_Ninon_down with dissolve

    ch_ninon "히잉…… 온천 또 가고 싶어요 입니다……"

    hide stand_Ninon_down

    show stand_Monica_ddung with dissolve

    ch_monica "충분히 쉬었으면 만족할 줄도 알아라!!"

    show stand_Monica
    hide stand_Monica_ddung

    ch_monica "그건 그렇고…… 달리 할 일이 없다면, 귀공도 함께 가지 않겠나?"

    hide stand_Monica

    if point == -3:
        jump BAD

    ch_ayumi "선배와 함께라면 저는 좋……!!   {nw}"

    stop music

    show bg_town with hpunch

    ch_town "으아아아악!!!!"

    ch_town "누가 좀 도와줘요!!!"

    show stand_Monica_surprised with dissolve

    ch_monica "무, 무슨 일이지?!"

    hide stand_Monica_surprised

    play music "audio/main/emer.mp3"

    ch_town "마, 마물이다……!!! 마물이 나타났다!!!!!"

    show stand_Kuka_mousou with dissolve

    ch_kuka "흐이이……!! 쿠우카의 몸을 노리고 마을까지 찾아오다니!!! 원정 서비스인가요!!!"

    hide stand_Kuka_mousou
    show stand_Yuki_surp with dissolve

    ch_yuki "어떻게 된 거야……? 마을 경비대는 어디 가고?"

    hide stand_Yuki_surp

    ch_town "경비대원들도 모두 당했어요……!!! 도와주세요!!!!"

    player "뭐……?! 얼마나 강한 놈이길래?!"

    show stand_Monica_ddung with dissolve

    ch_monica "……"

    ch_monica "차라리 잘 됐어…… 특훈의 성과를 보여 줄 때다!!"

    ch_monica "제군들! 마물이 출몰한 장소로 이동한다!! 지금 당장!!!"

    hide stand_Monica_ddung

    show stand_Ninon_angry with dissolve

    ch_ninon "닌닌 입니다!!! 슈바바바밧!!!!"

    hide stand_Ninon_angry

    show bg_black
    hide bg_town

    $renpy.pause(2.0)

    jump scene27Common
## S# 27. 라이덴 전투 cg (공통 루트) ####################
label scene27Common:
    play sound "audio/sound/growl.mp3"
    scene raiden_pohyo with hpunch
    
    monster "{b}{size=30}쿠아아아악{font=NanumGothic.ttf}——{/font}!!!!!!{/size}{/b}"

    show cg_raiden with dissolve
    hide raiden_pohyo

    ch_yuki "저, 저게 뭐야……?!"

    ch_yuki "엄청 비겁하게 못생겼어……!!"

    player "3넴…… 통나무…… 으윽…… 머리가……!!!"

    ch_monica "저건 분명……"

    ch_monica "라이덴……?!"

    ch_monica "바보 같은……!! 저런 녀석이 어떻게 왕도 근처에……?!"

    ch_monica "전원, 전투 준비!!!"

    ch_monica "귀공은 사람들을 대피시키고, 다른 길드에게 협력 요청을 해 다오! 부탁한다!"

    player "아…… 알았어!"

    play sound "audio/sound/growl.mp3"

    show raiden_pohyo with hpunch
    hide cg_raiden
        
    monster "{b}{size=30}키에에에에에!!!!!!!!{/size}{/b}"

    show cg_raiden with dissolve
    hide raiden_pohyo

    ch_monica "큿…… 엄청난 위압감……!!"

    ch_monica "우리가 과연…… 이길 수 있을까……?"

    ch_ninon "할 수 있어요 입니다!! 쇼군의 특훈을 거치고, 마물을 성공적으로 해치운 우리에게…… 불가능이란 없소 입니다!!!"

    ch_kuka "이…… 이런 곳에서 쓰러져 버린다면, 더 이상 망상조차 할 수 없는 몸이 되어버리겠죠…… 그, 그러니까…… 쿠우카, 힘내겠습니다……!!"

    ch_yuki "하아…… 피부가 상하는 건 진짜 싫은데, 그런 걸 따질 만한 상황은 아닌 것 같네. 전투가 끝나면 확실히 보상 받을 테니까 각오하라구……!"

    ch_ayumi "으으…… 자, 자신 없고 무섭지만…… 선배와 모두를 지키기 위해서라면……! 할 수 있는 데까지 힘써 볼게요오……!!"

    ch_monica "모두들……!"

    $renpy.pause(2.0)

    play music "audio/main/9bbong.mp3"

    ch_monica "……제군들, 우리는……"

    ch_monica "우리는…… {b}‘바이스플뤼겔 랜드솔지부’{/b}다."

    ch_monica "……떠올려라, 우리의 본분을."

    ch_monica "긍지를 걸어라, 우리의 가슴에……!!"

    ch_monica "비상하라…… 순백색 날개를 펼치고!!!"

    play sound "audio/sound/baldo.mp3"

    ch_monica "{b}{size=30}바이스플뤼겔!!!! 전원 발도를 허가한다!!!!{/size}{/b}"

    play sound "audio/sound/growl.mp3"
    
    show raiden_pohyo with hpunch
    hide cg_raiden
    monster "{b}{size=30}쿠아아아악!!!!{/size}{/b}"

    show cg_raiden with dissolve
    hide raiden_pohyo

    ch_monica "간다……!!"

    ch_monica "이 검으로, 사람들을……"

    ch_monica "랜드솔을…… 지켜 낸다!!!!"

    show bg_black
    hide cg_raiden
    $renpy.pause(2.0)

    stop music

    play sound "audio/sound/knife2.wav"

    show knife_issen

    $renpy.pause(2.0)

    if point == 0:
        jump Badkyaru
    elif point == -1 or point == -2:
        jump Kimura
    else:
        jump scene28

## S# 28. 길드 하우스 cg (해피, 진, 히든) #############
label scene28:
    scene bg_guildhouse with fade

    play music "audio/main/10end.mp3"

    ch_nar "……"

    ch_nar "‘바이스플뤼겔 랜드솔지부’"

    ch_nar "니논,"

    ch_nar "아유미,"

    ch_nar "모니카,"

    ch_nar "쿠우카,"

    ch_nar "유키……"

    ch_nar "……모두의 이야기 소리와 웃음 소리가 끊이질 않던,"

    ch_nar "정겨웠던…… 길드 하우스."

    ch_nar "이제는……"

    play music "audio/main/11fun.mp3"

    show stand_Ninon_wink:
        rotate 0
        linear 0.5 rotate 360

    ch_ninon "{b}{size=30}파티다~~~!!!!! 입니다!!!!!{/size}{/b}"

    hide stand_Ninon_wink

    show stand_Kuka_mousou:
        rotate 0
        linear 0.5 rotate 360

    ch_kuka "{b}{size=30}우호~~~~!!!!{/size}{/b}"

    hide stand_Kuka_mousou

    ch_nar "……더 시끄러워졌다."

    show stand_Monica_surprised with dissolve

    ch_monica "우왓…… 수제 초콜릿 세트?!"

    ch_monica "이런 걸 선물로 보내다니……!! 굉장한 안목이로군!!!"

    hide stand_Monica_surprised

    player "와…… 거기 쌓여 있는 것들……"

    player "전부 다 선물이야?"

    show stand_Yuki with dissolve

    ch_yuki "마물을 토벌한 공로를 치하하여, 소정의 선물을 보내드립니다…… 라는 공문이 내려 왔던데?"

    ch_yuki "게다가 왕궁에서뿐만 아니라, 마을 사람들까지 잔뜩 보내왔어."

    show stand_Yuki_proud
    hide stand_Yuki

    ch_yuki "꺄아~ 달팽이 크림도 있네? 바로 발라 봐야지~♪"

    hide stand_Yuki_proud

    player "……흐음."

    player "너희들, 정말로 대단하구나……"

    if point == 2:
        pass
    else:
        if love_point == 1:
            show stand_Ninon_surprise with dissolve

            ch_ninon "어? 쇼군, 어디 가시오 입니까?"

            hide stand_Ninon_surprise

            player "응? 그냥…… 바람 좀 쐬려고."

            show stand_Ninon with dissolve

            ch_ninon "기다려 입니다~! 니논도 같이 간다 입니다!"

            hide stand_Ninon
            show bg_town with dissolve
            hide bg_guildhouse

            stop music

            player "……같이 놀고 있지, 뭐하러 따라 나왔어."

            show stand_Ninon with dissolve

            ch_ninon "쇼군이 가는 곳이라면 어디든 함께 간다 입니다~!"

            $renpy.pause(1.0)

            show stand_Ninon_down
            hide stand_Ninon

            ch_ninon "……쇼군."

            player "응?"

            ch_ninon "니논은 쇼군의 모든 것을 꿰뚫고 있소 입니다."

            ch_ninon "지금…… 뭔가 고민이 있는 거죠 입니다……?"

            player "고민……이라."

            player "……글쎄~ 말해 줄까 말까."

            show stand_Ninon_embarassed
            hide stand_Ninon_down

            ch_ninon "에에엥~ 말해 주세요 입니다~~!!!"

            ch_ninon "쇼구우운~~ 제바……"

            show stand_Ninon_surprise
            hide stand_Ninon_embarassed

            ch_ninon "……어?"

            hide stand_Ninon_surprise

            player "응……?"

            play sound "audio/sound/down.mp3"
            show town_swift
            hide bg_town

            ch_ninon "쇼, 쇼군……!! 정신 차리……"

            ch_ninon "윽…… 니논도 갑좌기 어질어질……?!"

            $renpy.pause(2.0)

            if point == 1:
                jump end_kokoro
            else:
                jump ninonHappy
        elif love_point == 2:

            show stand_Monica_surprised with dissolve

            ch_monica "응? 귀공, 어디 가는 거냐?"

            hide stand_Monica_surprised

            player "응? 그냥…… 바람 좀 쐬려고."

            show stand_Monica with dissolve

            ch_monica "그런가…… 나도 같이 가도록 하지! 기다려라!"

            hide stand_Monica
            show bg_town with dissolve
            hide bg_guildhouse

            stop music

            player "……같이 놀고 있지, 뭐하러 따라 나왔어."

            show stand_Monica with dissolve

            ch_monica "신경 쓰지 마라. 마침 나도 바람이 쐬고 싶었던 참이야."

            $renpy.pause(1.0)

            show stand_Monica_down
            hide stand_Monica

            ch_monica "……귀공."

            player "응?"

            ch_monica "무엇을 숨기려 하는 건진 잘 모르겠다만……"

            ch_monica "지금…… 뭔가 고민이 있는 것이지?"

            player "고민……이라."

            player "……글쎄~ 말해 줄까 말까."

            show stand_Monica_ddung
            hide stand_Monica_down

            ch_monica "……나는 아직 귀공에게 그 정도의 믿음조차 주지 못한 건가……?"

            ch_monica "……되었다. 말하기 싫은 비밀도 하나쯤은 있는……"

            show stand_Monica_surprised
            hide stand_Monica_ddung

            ch_monica "……어?"

            hide stand_Monica_surprised

            player "응……?"

            play sound "audio/sound/down.mp3"
            show town_swift
            hide bg_town

            ch_monica "귀, 귀공……?! 정신 차리……"

            ch_monica "큭…… 가, 갑자기 머리가……?!"

            $renpy.pause(2.0)

            if point == 1:
                jump end_kokoro
            else:
                jump monicaHappy
        elif love_point == 3:
            show stand_Kuka_down with dissolve

            ch_kuka "어? 도S 씨……? 어디 가시나요?"

            hide stand_Kuka_down

            player "응? 그냥…… 바람 좀 쐬려고."

            show stand_Kuka with dissolve

            ch_kuka "자, 잠깐만요…… 저도 같이 가요……!!"

            hide stand_Kuka
            show bg_town with dissolve
            hide bg_guildhouse

            stop music

            player "……같이 놀고 있지, 뭐하러 따라 나왔어."

            show stand_Kuka with dissolve

            ch_kuka "아니에요…… 마침 저도 바람이 쐬고 싶었던 참이고……"

            $renpy.pause(1.0)

            show stand_Kuka_down
            hide stand_Kuka

            ch_kuka "……도S 씨."

            player "응?"

            ch_kuka "저어…… 이런 걸 여쭤봐도 될지 모르겠지만……"

            ch_kuka "지금…… 뭔가 고민이 있으신 거죠……?"

            player "고민……이라."

            player "……글쎄~ 말해 줄까 말까."

            show stand_Kuka_shamed
            hide stand_Kuka_down

            ch_kuka "에엣……!! 쿠우카의 선의를 이런 식으로 악용하실 생각인가요…"

            ch_kuka "과연 도S 씨……!! 부조리한 갑을 관계에 놓여 있……"

            show stand_Kuka_surprised
            hide stand_Kuka_shamed

            ch_kuka "……어?"

            hide stand_Kuka_surprised

            player "응……?"

            play sound "audio/sound/down.mp3"
            show town_swift
            hide bg_town

            ch_kuka "도, 도S 씨……?! 정신 차려 보……"

            ch_kuka "으아…… 쿠우카도 갑자기 머리가……?!"

            $renpy.pause(2.0)

            if point == 1:
                jump end_kokoro
            else:
                jump kukaHappy
        else:
            show stand_Yuki_surp with dissolve

            ch_yuki "앗, 너! 어디 가는 거야?"

            hide stand_Yuki_surp

            player "응? 그냥…… 바람 좀 쐬려고."

            show stand_Yuki_ddung with dissolve

            ch_yuki "밖에 나가려는 거지? 나도 같이 가~!"

            hide stand_Yuki_ddung
            show bg_town with dissolve
            hide bg_guildhouse

            stop music

            player "……같이 놀고 있지, 뭐하러 따라 나왔어."

            show stand_Yuki with dissolve

            ch_yuki "신경 쓰지 마~ 나도 잠깐 바깥 공기 좀 마시고 싶었으니까……"

            $renpy.pause(1.0)

            show stand_Yuki_ddung
            hide stand_Yuki

            ch_yuki "……있잖아."

            player "응?"

            ch_yuki "너, 뭘 숨기고 있는지는 모르겠지만……"

            ch_yuki "지금…… 뭔가 고민이 있는 거지?"

            player "고민……이라."

            player "……글쎄~ 말해 줄까 말까."

            show stand_Yuki_shamed
            hide stand_Yuki_ddung

            ch_yuki "에엑, 나만큼 귀여운 애가 먼저 물어봐 준 건데~?!"

            ch_yuki "이런 식으로 나오겠다 이거지……? 그래!! 매료시켜……"

            show stand_Yuki_surp
            hide stand_Yuki_shamed

            ch_yuki "……어?"

            hide stand_Yuki_surp

            player "응……?"

            play sound "audio/sound/down.mp3"
            show town_swift
            hide bg_town

            ch_yuki "뭐, 뭐야……!! 정신 차려……"

            ch_yuki "으극…… 갑자기 머리가……?!"

            $renpy.pause(2.0)

            if point == 1:
                jump end_kokoro
            else:
                jump yukiHappy

    play music "audio/main/10end.mp3"

    show bg_town with dissolve
    hide bg_guildhouse

    ch_nar "……"

    ch_nar "그래, 정말로 대단하네."

    ch_nar "……멍청하고 한심하다며 무시하던 녀석들이었는데……"

    ch_nar "이제는 모두가 인정해 줄 정도로 강해졌구나."

    ch_nar "……그에 비하면,"

    ch_nar "나는…… 뭐지?"

    ch_nar "다른 사람 뒷담은 잘 까고 다니면서…… 정작 혼자서 할 줄 아는 건 아무것도 없네."

    ch_nar "……정말로 한심한 건 나였어."

    ch_nar "미식전에서도 버려졌는데……"

    ch_nar "아쉽지만, 이곳도 곧 떠나야겠네."

    ch_nar "그래…… 말 나온 김에 떠나 버리자."

    ch_nar "지금 당장."

    play sound "audio/sound/walking.mp3"

    $renpy.pause(2.0)

    ch_nar "……안녕, 모두   {nw}"

    stop sound

    show stand_Ninon_angry with dissolve

    ch_ninon "CHOTTO MATTE 입니다!!!!!!"

    hide stand_Ninon_angry

    player "어……?"

    show stand_Yuki_ddung with dissolve

    ch_yuki "이렇게나 귀여운 나를 두고 어딜 가려는 거야? 당장 돌아와!"

    hide stand_Yuki_ddung

    ch_ayumi "선배……!! 갑자기 사라지셔서 놀랐어요!!"

    show stand_Kuka with dissolve

    ch_kuka "도, 도S 씨……!! 쿠우카에게 마구 몹쓸 짓을 하실 땐 언제고…… 이용 가치가 없어지니까 바로 내치시는 건가요……?! 크흐흣……!!"

    hide stand_Kuka

    show stand_Monica_ddung with dissolve

    ch_monica "귀공…… 이렇게 기쁜 날인데, 혼자서 궁상맞게 뭐하는 짓인가?"

    hide stand_Monica_ddung

    player "어, 어……? 다들 왜 여기까지 나온……"

    show stand_Yuki_ddung with dissolve

    ch_yuki "……너, 어딘가로 떠나 버리려는 거지?"

    player "……어떻게……?"

    ch_yuki "그런 음울한 표정을 하고 있는데, 모르는 게 더 이상하잖아?"

    hide stand_Yuki_ddung

    show stand_Ninon_innocence with dissolve

    ch_ninon "쇼군……!! 가 버리시는 겁니까……?! 안돼 입니다……!! 니논이 할복 하겠습니다!!!"

    hide stand_Ninon_innocence

    ch_ayumi "가지 마세요, 선배……!! 어차피 갈 곳도 없으시……"

    stop music
    play sound "audio/sound/down.mp3"
    show town_swift
    hide bg_town

    player "……어라?"

    ch_monica "귀, 귀공!!! 정신……"

    ch_kuka "모, 모니카……씨…… 으우……"

    jump Success 
## CG ####################################

## 니논 루트 ## ## ## ## ## ## ## ## ## ## ## ## ## ## 
##
##  
## S# 15-3. 니논 탁구 CG (니논 루트) ##################
label cg_ninonfirst:

    scene bg_naibu

    ## 니논 시무룩한 표정
    show stand_Ninon_yukata_down with dissolve

    ch_ninon "우우…… 엄청나게 많이 먹었다 입니다."

    ch_ninon "더는 안 들어가요 입니다……"
    
    ## 쿠우카 기본 표정
    show stand_Kuka_yukata at right with dissolve

    ch_kuka "더, 더는 안 들어간다니……!! 끝에 닿을 정도면 대체 얼마나 길고 굵{nw}"

    hide stand_Kuka_yukata
    hide stand_Ninon_yukata_down

    ch_ayumi "아……아아아아~~!!!"

    ch_ayumi "저, 저기 좀 보세요!!"

    ## 모니카 시무룩한 표정
    show stand_Monica_yukata_down with dissolve

    ch_monica "흐음……? 저건……"

    hide stand_Monica_yukata_down
    ## 니논 놀란 표정
    show stand_Ninon_yukata_surp with dissolve

    ch_ninon "오옷!!!!! 저것은……!!!"

    hide stand_Ninon_yukata_surp

    player "탁구대……인가?"

    ## 쿠우카 기본 표정
    show stand_Kuka_yukata with dissolve

    ch_kuka "탁탁탁……"

    hide stand_Kuka_yukata
    ## 유키 뚱한 표정
    show stand_Yuki_yukata_ddung with dissolve
    
    ch_yuki "탁구? 운동 같은 거엔 관심 없으니까, 나는 빠질게~"

    hide stand_Yuki_yukata_ddung

    player "어…… 탁구도 운동이긴 하지……"
    
    ## 니논 웃는 표정
    show stand_Ninon_yukata with dissolve

    ch_ninon "……어떻습니까, 쇼군!! 한 판 뜨자 입니다!!!"

    hide stand_Ninon_yukata

    player "뭐?! 한 판 뜨자고?!"

    ## 쿠우카 망상하는 표정
    show stand_Kuka_yukata_mousou with dissolve

    ch_kuka "히이이~~~!!!! 서방의 문화는 듣던 대로 엄청나게 개방적이네요!!!!"

    hide stand_Kuka_yukata_mousou

    ## 니논 시무룩한 표정
    show stand_Ninon_yukata_down with dissolve

    ch_ninon "……??"

    ch_ninon "탁구를 말하는 것 입니다……?"

    hide stand_Ninon_yukata_down

    player "아……"

    player "타…… 탁구!! 그, 그래!"

    player "하자! 탁구!!"

    show stand_Kuka_yukata_down with dissolve

    ch_kuka "스읍……"

    hide stand_Kuka_yukata_down

    show stand_Ninon_yukata with dissolve
    
    ch_ninon "쇼군, 탁구 실력은 좀 어떠신가요 입니까?"

    hide stand_Ninon_yukata

    player "호오……"

    player "너야말로 자신 있는 건가……?"

    show stand_Ninon_yukata_daiji with dissolve

    ch_ninon "훗……"

    ch_ninon "수리검 던지기 연습을 하루도 거르쥐 않는 저에게 이런 것쯤……"

    ch_ninon "누워서 똥 싸기에 불과……!!"

    ch_nar "앉아서 싸!!!"

    ch_ninon "후후, 미리 말씀드리자면……"

    ch_ninon "니논의 탁구력은…… 530,000 입니다!"

    hide stand_Ninon_yukata_daiji

    ch_ayumi "타, 탁구력이 뭔지는 모르겠지만…… 엄청나게 강해 보여요……!!"

    player "짐바브웨 달러 같은 거 아닐까……?!"

    show stand_Ninon_yukata_daiji with dissolve

    ch_ninon "그렇지만, 물론 전력으로 쇼군과 싸울 생각은 없으니 걱정하지 마세요 입니다……"

    ch_ninon "너무 재미가 없을지도 모르니…… 이 오른손으로만 상대해 드리지요 입니다……!!"

    show stand_Monica_yukata_down at right with dissolve

    ch_monica "‘……탁구는 원래 한 손으로 하는 거 아닌가……?’"

    hide stand_Monica_yukata_down
    show stand_Ninon_yukata
    hide stand_Ninon_yukata_daiji

    ch_ninon "그럼…… 쇼군!!"

    show stand_Ninon_yukata_wink
    hide stand_Ninon_yukata

    ch_ninon "니논이 한 수 가르쳐 드리겠소 입니다~!"

    ch_ninon "마음의 준비가 되었다면 불러주세요 입니다!!"
    jump pingpong_choice
## 탁구 선택지 #########################################
label pingpong_choice:
    menu:
        "그 전에 연습 경기 한 판 어때?choice_1":
            $ persistent.practicepong = True
            show stand_Ninon_yukata
            hide stand_Ninon_yukata_wink

            ch_ninon "후후…… 이 니논이 상대라 긴장하셨나요 입니까?"
            show stand_Ninon_yukata_wink
            hide stand_Ninon_yukata

            ch_ninon "알겠습니다~ 그 대쉰 실전에서는 봐드리지 않겠소 입니다~!"
            hide stand_Ninon_yukata_wink

            narrator "「니논과의 탁구게임 한 판!」 {vspace=15} {p}연습 경기에서는 승패가 기록되지 않습니다. 부담없이 도전해 보세요."
            
            ch_nar "시 - 작 !"
            
            jump play_pong
        "덤벼!choice_2":
            $ persistent.practicepong = False
            ch_ninon "오오, 좋은 기백이다 입니다~!!"

            ch_ninon "그러면…… HAJIMARUYO 입니다!!!"

            hide stand_Ninon_yukata_wink
            jump play_pong


    return

## S# 24-1. 니논 온천 cg (니논 루트) ##################################
label cg_ninonsecond:

    scene cg_ninon_onsen_01 with fade

    play music "audio/main/8sad.mp3"

    ch_ninon "쇼, 쇼군……"

    ch_ninon "무…… 물 온도는 적당하신가요 입니다……?"

    player "응. 기분 좋아……"

    ch_ninon "……"

    player "……무슨 할 말이라도 있어?"

    ch_ninon "아……"

    ch_ninon "저기, 그게……"

    ch_ninon "도…… 동국에 대해, 나름 아는 것이 많다고 자부했다 입니다만……"

    ch_ninon "그게…… 동국에서는…… 남성과 여성이 함께 몸을 씻는 일 정도는 아무렇지도 않다 입니까……?"

    player "혼욕탕에 가자고 먼저 제안한 건 너였잖아?"

    ch_ninon "아, 그…… 그랬던 거 같기도 하고…… 아닌 거 같기도 하고……? 그랬던 거 같기도 하고…… 입니다."

    player "……니논은 나랑 있는 게 싫은 거야?"

    show cg_ninon_onsen_03 with dissolve
    hide cg_ninon_onsen_01

    ch_ninon "다…… 다, 당치도 않소 입니다!!!"

    show cg_ninon_onsen_01 with dissolve
    hide cg_ninon_onsen_03

    ch_ninon "니논은 그저……"

    ch_ninon "……시, 신하된 DORI 로서, 쇼군의 곁을 지키는 것은 영광입니다만……"

    ch_ninon "그…… 너무 빤히 쳐다보시면……"

    show cg_ninon_onsen_02 with dissolve
    hide cg_ninon_onsen_01

    ch_ninon "조, 조금…… 부끄러워 입니다……"

    player "부끄러워……?"

    player "그렇게 말하는 것 치고는…… 꽤 대담한 모습을 하고 있잖아?"

    show cg_ninon_onsen_03 with dissolve
    hide cg_ninon_onsen_02

    ch_ninon "~~~~~!!!!"

    ch_ninon "쇼, 쇼군~~!! 짓궂어 입니다……!!"

    show cg_ninon_onsen_02 with dissolve
    hide cg_ninon_onsen_03

    ch_ninon "……쇼군이 어떤 행동을 하쉬더라도, 니논은 쇼군을 따르겠소 입니다만……"

    ch_ninon "오…… 오늘의 쇼군은 어쩐지…… 쇼군이 아닌 것 같아요 입니다……"

    ch_ninon "영웅은 호색한이라 들었는데…… 그 말이 옳았다 입니까……?"

    player "내가 어떤 행동을 하더라도…… 따르겠다고?"

    player "그렇다면……"

    menu:
        "“내가 나쁜 짓을 한다 해도?”choice_1":
            $point_ninon += 1
            show cg_ninon_onsen_01 with dissolve
            hide cg_ninon_onsen_02

            ch_ninon "쇼군이…… 나쁜 짓을 한다면?"

            ch_ninon "니논의 충성심을 시험하시는 것입니까……?"

            ch_ninon "……"

            ch_ninon "주군에 대한 충의는 절대적. 그러므로……"

            $renpy.pause(1.0)

            ch_ninon "……아니,"

            ch_ninon "따르지 않겠소 입니다."

            ch_ninon "쇼군은……"

            ch_ninon "적어도…… 제가 아는 쇼군은,"

            ch_ninon "어떤 일이 있어도 나쁜 놈이 되지는 않을 것이오 입니다."

            ch_ninon "절대 그럴리 없쥐만, 만에 하나……"

            ch_ninon "쇼군이…… 나쁜놈이 되어 버린다면, 그때는……"

            ch_ninon "쇼군이 제정신을 찾을 때까지, 니논이 때찌때찌 해 줄 것입니다."

            ch_ninon "그러니까, 따를 수 없소이다 입니다."

            player "……"

            player "역시 니논은…… 나를 실망시키지 않는구나."

            show cg_ninon_onsen_03 onlayer middle with dissolve

            $camera_move(200, -500, 600, 0, 1)

            ch_ninon "!!!!!"

            ch_ninon "쇼, 쇼군……!!! 갑자기……?!"
            $camera_move(200, -700, 1000, 0, 0.5)



        "    “이리 가까이 와.”choice_2":
            show cg_ninon_onsen_01 onlayer middle with dissolve

            ch_ninon "가, 가까이…… 입니까?"

            $camera_move(200, -500, 400, 0, 1)

            ch_ninon "……!!"

            show cg_ninon_onsen_02 onlayer middle with dissolve
            hide cg_ninon_onsen_01 onlayer middle

            ch_ninon "쇼…… 쇼군……?!"

            ch_ninon "너무 가까워요 입니다……!!"

            player "더 가까이."

            ch_ninon "에에……?"

            player "더 가까이 와."

            show cg_ninon_onsen_03 onlayer middle with dissolve
            hide cg_ninon_onsen_02 onlayer middle

            $camera_move(200, -700, 1000, 0, 0.5)

            ch_ninon "우우우……"

            ch_ninon "너, 너무 가까워 입니다……"

            ch_ninon "쇼군의…… 체온까지 느껴져요 입니다……!"
  
        "“벗어.”choice_3":
            $point_ninon -= 1
            show cg_ninon_onsen_03 onlayer middle with dissolve
            ch_ninon "?!?!?!!"

            ch_ninon "쇼군……?! 갑자기 무엇을……!!"

            ch_ninon "니, 니논이…… 잘못 들은 것이다 입니까……?"

            player "다시 한 번 말해 줄까?"

            player "{b}{size=30}벗어.{/size}{/b}"

            ch_ninon "…………"

            ch_ninon "이런 거…… 이상해요 입니다……"

            ch_ninon "쇼, 쇼군은…… 흐윽……"

            ch_ninon "이런 파렴치한 행동 따위…… 히끅…… 강요하지 않을 텐데……"

            $camera_move(200, -700, 1000, 0, 0.5)
    
    player "니논……"

    ch_ninon "쇼, 쇼군……"

    player "그대로…… 가만히 있어……"

    ch_ninon "쇼군…… 쇼구운……"

    $renpy.pause(1.0)

    stop music
    play sound "audio/sound/surp.mp3"

    show stand_gura onlayer forward with dissolve:
        xalign 0.5 yalign 0.4

    show highlight onlayer forward

    ch_gura "여러부우우{font=NanumGothic.ttf}————{/font}우운!!!!!!!!!!!"

    ch_gura "구하러 왔슴다{font=NanumGothic.ttf}————{/font}아앗!!!!!!!!!!!!"

    $camera_move(0, 0, 0, 0, 0)

    show bg_outside_onsen_2
    hide highlight onlayer forward
    hide stand_gura onlayer forward
    hide cg_ninon_onsen_03 onlayer middle

    show ob_yas3 with dissolve

    play sound "audio/sound/monkey.mp3"

    play music "audio/main/emer.mp3"

    monster "아 씹빨!!!!! 폭풍야스 왜 안하냐고!!!!!!!!"

    hide ob_yas3

    ch_ninon panic "꺄아아아악~~~!!!! 입니다!!!!!"

    player "뭐, 뭐야!!!!"

    show stand_gura with dissolve

    ch_gura "다들 무사하시군요!!!! 다행히 늦지 않았습니다!!!!!"

    hide stand_gura

    player "뭐가…… 뭐가 어떻게 된 거야……?!"

    player "난 여기서 뭘 하고 있었던 거지?!"

    show stand_gura with dissolve

    ch_gura "자세히 설명할 시간이 없습니다!!!"

    ch_gura "여러분들은 저 마물에게 홀렸던 겁니다!!!"

    hide stand_gura

    show ob_yas1 with dissolve

    play sound "audio/sound/monkey2.mp3"

    monster "우끼긱!!!!!! 우꺅!!!!!!!"

    ch_ninon panic "저게 대체 뭐야 입니다!!!!"

    hide ob_yas1

    show stand_gura with dissolve

    ch_gura "정신 차리십쇼!!!!! 지금 당장 놈을 퇴치해야 합니다!!!!"

    hide stand_gura

    player "퇴치?! 때려잡으면 되는 거야?!"

    show stand_gura with dissolve

    ch_gura "아니오!!!! 놈은 야스를 하지 못하고 죽은 원념이 모여 탄생한 정신체!!!!"

    ch_gura "물리적 공격은 통하지 않습니다!!!!"

    hide stand_gura

    player "그…… 그러면 어떻게 해?!!"

    show stand_gura with dissolve

    ch_gura "방법은 하나!!!!"

    ch_gura "20년이 넘도록 순결을 지켜 온 청년의 피가 스며든 물건을…… 녀석의 눈앞에서 불태우는 의식을 행해야 합니다!!!!"

    hide stand_gura

    play sound "audio/sound/monkey2.mp3"

    show ob_yas3 with dissolve

    monster "우끽!!! 우끽!!! 우끼긱!!!!! 우끽!!!!! 우꺅!!!!"

    hide ob_yas3

    player "아 진짜!!! 어디서부터 태클을 걸어야 할지 모르겠어!!!!"

    player "그리고 그딴 걸 갑자기 어디서 구……"

    player "……"

    $renpy.pause(1.0)

    show ob_hankachi with dissolve:
        xpos 430 yalign 0.3

    player "……이거……"

    player "……불태우면…… 될 것 같은데……"

    ch_gura "전…… 전라 상태인데?! 어디서 그런 걸 꺼내신 겁니까?!!"

    player "그런 건 중요하지 않아!!!!"

    player "불!!! 빨리 불!!!!"

    hide ob_hankachi
    show stand_gura with dissolve

    ch_gura "네…… 넵!!!!!!"

    play sound "audio/sound/fire.mp3"
    show fire_small:
        xpos 100 ypos 210

    ch_gura "퐈이야{font=NanumGothic.ttf}——{/font}!!!!!!!!"

    hide fire_small

    show ob_yas2 with dissolve

    play sound "audio/sound/monkey2.mp3"

    monster "아 ㅋㅋ 야스각이었는데 ㅋ"

    monster "까비아깝송~"

    hide ob_yas2 with squares

    stop music

    show stand_gura with dissolve

    ch_gura "허억…… 후우……"

    ch_gura "해……"

    ch_gura "해치웠다!!!!!! 드디어!!!!!!"

    show bg_outside_onsen_2

    ch_gura "여러분 덕분임다!!!! 감사함다{font=NanumGothic.ttf}———{/font}아앗!!!!!!"

    hide stand_gura

    ch_ninon surp "……쇼군, 그런데……"

    ch_ninon surp "저걸 불태웠다는 건…… 20년 넘게 동정……"

    player "시끄러워……"

    jump scene25Common

## 모니카 루트 ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
##
##
## S# 15-2. 온천 건물 내부 (식당), 모니카 화과자 cg(모니카 루트) ########
label cg_monicafirst:
    $renpy.pause(1.0)

    ## 니논 웃는 표정
    show stand_Ninon_yukata with dissolve

    ch_ninon "여러분~! 어서 와 입니다!"

    hide stand_Ninon_yukata

    ## 모니카 우는 표정 머리 빼꼼

    show stand_Monica_yukata_crying with dissolve:
        xpos 200 ypos 400
        linear 0.5 ypos 250
    
    ch_monica "……과자……"

    ch_monica "과자아아………"
    
    hide stand_Monica_yukata_crying

    player "……모니카는 왜 저러고 있는 거야?"

    ## 니논 웃는 표정
    show stand_Ninon_yukata with dissolve

    ch_ninon "그게…… 얼떨결에 니논을 쫓아 달려왔지만……"

    ch_ninon "일행을 뒤로 하고 사리솨욕을 채우는 것은 도의를 저붜리는 것과도 같다고 생각하여, 여러분이 오실 때까지 음식에 손도 대지 않겠다고 말씀하셨소 입니다."

    ## 니논 시무룩한 표정
    show stand_Ninon_yukata_down
    hide stand_Ninon_yukata

    ch_ninon "근데…… 보시다쉬피……"

    hide stand_Ninon_yukata_down

    ## 모니카 우는 표정 아래쪽
    show stand_Monica_yukata_crying with dissolve:
        xpos 200 ypos 250
    
    ch_monica "쪼꼬…… 쪼꼬렛……"

    hide stand_Monica_yukata_crying
    ## 니논 시무룩한 표정
    show stand_Ninon_yukata_down with dissolve

    ch_ninon "맛이 가 버렸다 입니다……"

    hide stand_Ninon_yukata_down

    show stand_Monica_yukata_crying with dissolve:
        xpos 200 ypos 250
    
    ch_monica "사탕…… 쩰리이……"
    
    hide stand_Monica_yukata_crying

    player "……과자를 먹이면 다시 괜찮아지지 않을까……?"

    ## 니논 놀란 표정
    show stand_Ninon_yukata_surp with dissolve

    ch_ninon "앗, 확실히……! 그럴지도 몰라요 입니다!!"

    show stand_Ninon_yukata
    hide stand_Ninon_yukata_surp

    ch_ninon "모니카 씨~ 일어나 입니다~!"

    ch_ninon "까까 먹을 시간이에용~ 입니다."

    hide stand_Ninon_yukata

    show stand_Monica_yukata_surprised with dissolve:
        xpos 200 ypos 250
        linear 0.3 ypos 0
    
    ch_monica "까까!!!!!"

    ch_monica "단 거!!!!!!!!!"

    $renpy.pause(1.0)

    hide stand_Monica_yukata_surprised
    show stand_Monica_yukata_munen with dissolve

    ch_monica "어……? 귀, 귀공?"

    ch_monica "이…… 이제 온 건가. 먼저 자리를 잡고 기다리고 있었다."

    player "방금……"

    ch_monica "……방금? 무슨 말인지 모르겠다만……?"

    player "까까……"

    play sound "audio/sound/hit.wav"
    show bg_onsen with hpunch

    ch_monica "모, 모두들!! 몹시 배고플 테지?!! 어서 자리에 앉도록!!!"

    hide stand_Monica_yukata_munen
    show ob_wagasi with dissolve:
        xpos 430 yalign 0.3

    player "오, 이게 그 한정판 간식인가?"

    ch_ninon "맞아요 입니다! 오에도의 명물, 한정판 화과자 DELUXE SET 입니다~!"

    ch_monica "………"

    player "……?"

    player "왜 그래?"

    ch_monica "아……?"

    ch_monica "그게…… 이, 이제 먹어도……"

    player "어? 으응……"

    player "참느라 혼났을 텐데 빨리 먹어……"

    ch_monica "고, 고맙군…… 그럼 어디……"

    hide ob_wagasi
    show cg_monica_first_01 with dissolve
    hide bg_onsen

    ch_monica "냠……"

    $renpy.pause(1.0)

    ch_monica "……이건……"

    ch_monica "후아아아……"

    ch_monica "달고 맛있어……"

    ch_monica "하, 한 입만 더……"

    ch_monica "암냠……"

    play sound "audio/sound/snack.wav"

    $renpy.pause(1.0)

    show cg_monica_first_02 with dissolve
    hide cg_monica_first_01

    ch_monica "마딧뎌어어……"

    ch_monica "흐아…… 입에서 살살 녹는다아……"

    player "눈이 풀렸네……"

    player "과자가 그렇게 좋아?"

    show cg_monica_first_03 with dissolve
    hide cg_monica_first_02

    ch_monica "!!!"

    ch_monica "차, 착각하지 마라……!! 처음 보는 음식이기에 잠깐 관심이 생긴 것 뿐이다!"

    ch_monica "어린아이도 아니고, 과자 같은 것에 흥미가 있을 리가……"

    $renpy.pause(1.0)

    ch_monica "……니논, 거기……"

    ch_monica "……하나 남은 모찌는 내가 먹어도 괜찮을까?"

    hide cg_monica_first_03
    
    jump sceneNum16Common

label cg_monicasecond:

    scene cg_monica_onsen_01 with fade

    play music "audio/main/8sad.mp3"

    ch_monica "……"

    ch_monica "귀공, 내 얼굴에…… 뭐라도 묻었나?"

    ch_monica "뭘 그렇게 빤히 쳐다보는 거냐……"

    player "응?"

    player "그냥…… 귀여워서."

    show cg_monica_onsen_03 with hpunch

    hide cg_monica_onsen_01

    ch_monica "캬아악……!!!"

    ch_monica "귀…… 귀공은 아직도 내가 어린아이로밖에 보이지 않는 건가?!"

    player "하악질하는 고양이 같네……"

    show cg_monica_onsen_02 with dissolve
    hide cg_monica_onsen_03

    ch_monica "……"

    ch_monica "……귀공은 언제나 그런 식이다."

    ch_monica "항상…… 나 혼자만 진지하고……"

    ch_monica "……아무리 내가 군인이라 하여도, 이런 상황이라면……"

    $renpy.pause(1.0)

    ch_monica "조, 조금은……"

    ch_monica "……두근거릴 수도 있는 것 아닌가."

    ch_monica "귀공을 보고 있노라면…… 마치 심장에 병이라도 걸린 것처럼, 가슴 한편이 아려 오는데……"

    show cg_monica_onsen_01 with dissolve
    hide cg_monica_onsen_02

    ch_monica "귀공은…… 나를 보면서도,"

    ch_monica "아무런 감정이…… 들지 않는가?"

    ch_monica "대답해 주게. 귀공은……"

    show cg_monica_onsen_02 with dissolve
    hide cg_monica_onsen_01

    ch_monica "……나를…… 어떻게 생각하나?"

    menu:
        "“모두의 귀감이 되는 훌륭한 지휘관이라고 생각해.”choice_1":
            show cg_monica_onsen_01 with dissolve
            hide cg_monica_onsen_02

            ch_monica "훌륭한 지휘관……인가."

            ch_monica "뭐…… 길드 마스터이자 군인이라는 신분으로서 들을 수 있는 최고의 칭찬이긴 하군……"

            show cg_monica_onsen_02 with dissolve
            hide cg_monica_onsen_01

            ch_monica "……기대하던 답변과는 다소 거리가 멀지만."

            player "기대하던 답변?"

            ch_monica "아니, 아무것도 아니다. 괘념치 마라."

            ch_monica "그보다…… 여기서 이럴 게 아니라,"

            ch_monica "함께…… 온천에 들어가는 건 어떤가?"

        "    “예쁘고 어른스러운, 내 이상형이야.”choice_2":
            $point_monica += 1
            show cg_monica_onsen_03 with hpunch
            hide cg_monica_onsen_02

            ch_monica "~~~~?!?!?!?!"

            ch_monica "그……"

            ch_monica "긋……!!"

            show cg_monica_onsen_03 with hpunch

            ch_monica "가…… 갑자기 그런 말을 해 버리는 건…… 반칙이잖나!!!!"

            player "왜 그래?"

            player "솔직하게 대답했을 뿐인데……"

            show cg_monica_onsen_03 with hpunch

            ch_monica "너무 솔직해!!!!!!!"

            ch_monica "으으…… 귀공은 정마아알……!!"

            show cg_monica_onsen_02 with dissolve
            hide cg_monica_onsen_03

            ch_monica "……되었다. 조금 민망하지만……"

            ch_monica "……아니, 사실은 엄청나게 부끄럽지만……!!"

            ch_monica "귀공이…… 그렇게 말해주었으니……"

            ch_monica "……"

            ch_monica "여, 여기서 이럴 게 아니라!"

            ch_monica "함께 온천에 몸을 담그지 않겠나……?"

        
        "“집으로 데려가서 키우고 싶어.”choice_3":
            $point_monica -= 1
            show cg_monica_onsen_03 with dissolve
            hide cg_monica_onsen_02

            ch_monica "……뭐, 뭐……?!?!"

            ch_monica "그건 또 무슨……!!"

            show cg_monica_onsen_03 with hpunch

            ch_monica "이, 이제는 어린애 취급도 모자라…… 애완동물 취급까지 하는 거냐!!!!"

            ch_monica "실망스럽군! 귀공은 조금이나마 다를 줄 알았는데……"

            show cg_monica_onsen_02 with dissolve
            hide cg_monica_onsen_03

            ch_monica "……나도 노력하고 있단 말이다……"

            ch_monica "하루도 거르지 않고 우유를 마셔 보거나…… 성장 호르몬이 많이 분비된다는 시간에 맞춰 잠자리에 드는데……"

            ch_monica "아무리 노력해도 바뀌지 않는 것을…… 나보고 어떡하란 말이냐……"

            ch_monica "다른 사람도 아니고, 귀공에게만큼은…… 어린아이처럼 보이고 싶지 않은데."

    player "모니카……"

    show cg_monica_onsen_03 onlayer middle with dissolve
    hide cg_monica_onsen_02

    $camera_move(-200, -500, 400, 0, 1)

    ch_monica "귀, 귀공?!"

    ch_monica "갑자기…… 무슨?!"

    player "됐으니까, 그대로……"

    player "가만히 있어……"

    show cg_monica_onsen_02 onlayer middle with dissolve
    hide cg_monica_onsen_03 onlayer middle

    ch_monica "……"

    ch_monica "……사, 상냥하게 해 다오……"

    $renpy.pause(1.0)

    stop music

    play sound "audio/sound/surp.mp3"

    show stand_gura onlayer forward with dissolve:
        xalign 0.5 yalign 0.4

    show highlight onlayer forward

    ch_gura "여러부우우{font=NanumGothic.ttf}————{/font}우운!!!!!!!!!!!"

    ch_gura "구하러 왔슴다{font=NanumGothic.ttf}————{/font}아앗!!!!!!!!!!!!"

    $camera_move(0, 0, 0, 0, 0)

    show bg_outside_onsen_2
    hide highlight onlayer forward
    hide stand_gura onlayer forward
    hide cg_monica_onsen_02 onlayer middle

    show ob_yas3 with dissolve

    play sound "audio/sound/monkey.mp3"

    play music "audio/main/emer.mp3"

    monster "아 씹빨!!!!! 폭풍야스 왜 안하냐고!!!!!!!!"

    hide ob_yas3

    ch_monica dere "우…… 우아아아악~~~!!!!"

    player "뭐, 뭐야!!!!"

    show stand_gura with dissolve

    ch_gura "다들 무사하시군요!!!! 다행히 늦지 않았습니다!!!!!"

    hide stand_gura

    player "뭐가…… 뭐가 어떻게 된 거야……?!"

    player "난 여기서 뭘 하고 있었던 거지?!"

    show stand_gura with dissolve

    ch_gura "자세히 설명할 시간이 없습니다!!!"

    ch_gura "여러분들은 저 마물에게 홀렸던 겁니다!!!"

    hide stand_gura

    show ob_yas1 with dissolve

    play sound "audio/sound/monkey2.mp3"

    monster "우끼긱!!!!!! 우꺅!!!!!!!"

    ch_monica dere "저, 저게 대체 뭐냐!!!"

    hide ob_yas1

    show stand_gura with dissolve

    ch_gura "정신 차리십쇼!!!!! 지금 당장 놈을 퇴치해야 합니다!!!!"

    hide stand_gura

    player "퇴치?! 때려잡으면 되는 거야?!"

    show stand_gura with dissolve

    ch_gura "아니오!!!! 놈은 야스를 하지 못하고 죽은 원념이 모여 탄생한 정신체!!!!"

    ch_gura "물리적 공격은 통하지 않습니다!!!!"

    hide stand_gura

    player "그…… 그러면 어떻게 해?!!"

    show stand_gura with dissolve

    ch_gura "방법은 하나!!!!"

    ch_gura "20년이 넘도록 순결을 지켜 온 청년의 피가 스며든 물건을…… 녀석의 눈앞에서 불태우는 의식을 행해야 합니다!!!!"

    hide stand_gura

    play sound "audio/sound/monkey2.mp3"

    show ob_yas3 with dissolve

    monster "우끽!!! 우끽!!! 우끼긱!!!!! 우끽!!!!! 우꺅!!!!"

    hide ob_yas3

    player "아 진짜!!! 어디서부터 태클을 걸어야 할지 모르겠어!!!!"

    player "그리고 그딴 걸 갑자기 어디서 구……"

    player "……"

    $renpy.pause(1.0)

    show ob_hankachi with dissolve:
        xpos 430 yalign 0.3

    player "……이거……"

    player "……불태우면…… 될 것 같은데……"

    ch_gura "전…… 전라 상태인데?! 어디서 그런 걸 꺼내신 겁니까?!!"

    player "그런 건 중요하지 않아!!!!"

    player "불!!! 빨리 불!!!!"

    hide ob_hankachi
    show stand_gura with dissolve

    ch_gura "네…… 넵!!!!!!"

    play sound "audio/sound/fire.mp3"
    show fire_small:
        xpos 100 ypos 210

    ch_gura "퐈이야{font=NanumGothic.ttf}——{/font}!!!!!!!!"

    hide fire_small

    show ob_yas2 with dissolve

    play sound "audio/sound/monkey2.mp3"

    monster "아 ㅋㅋ 야스각이었는데 ㅋ"

    monster "까비아깝송~"

    hide ob_yas2 with squares

    stop music

    show stand_gura with dissolve

    ch_gura "허억…… 후우……"

    ch_gura "해……"

    ch_gura "해치웠다!!!!!! 드디어!!!!!!"

    show bg_outside_onsen_2

    ch_gura "여러분 덕분임다!!!! 감사함다{font=NanumGothic.ttf}———{/font}아앗!!!!!!"

    hide stand_gura

    ch_monica ddung "……귀공, 그런데……"

    ch_monica ddung "저걸 불태웠다는 것은…… 20년 넘게 동정……"

    player "시끄러워……"

    jump scene25Common

## 쿠우카 루트 ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
##
##
## S# 15-4. 온천 건물 내부 (식당), 쿠우카 유카타 cg (쿠우카 루트) #######
label cg_kukafirst:
    scene bg_naibu

    player "너무 잘 먹었다……"

    show stand_Yuki_yukata with dissolve

    ch_yuki "맛있었어~ 그치? 아유ㅁ……"

    hide stand_Yuki_yukata

    ch_ayumi "‘헉…… 다른 사람도 아니고 유키 씨가…… 제 이름을 먼저……?!‘"

    show stand_Yuki_yukata with dissolve

    ch_yuki "……아유…… 아…… 아유……나……? 뭐더라?"

    hide stand_Yuki_yukata

    ch_ayumi "{b}{size=30}아 유 미 예요오!!!!!!!{/size}{/b}"

    show stand_Yuki_yukata with dissolve

    ch_yuki "뭐, 상관 없나~"

    hide stand_Yuki_yukata

    ch_ayumi "{b}{size=30}상관 없지 않아요!!!!!!!{/size}{/b}"

    show stand_Kuka_yukata_shamed with dissolve

    ch_kuka "……"

    ch_kuka "으으……"

    hide stand_Kuka_yukata_shamed

    ch_nar "응……?"

    ch_nar "멀찍이 떨어져서 뭘 하는 거야?"

    player "쿠우카, 아까부터 뒤에서 뭐 해……?"

    player "너무 많이 먹었어?"

    show stand_Kuka_yukata_shamed with dissolve

    ch_kuka "아…… 아뇨, 그…… 유카타가……"

    ch_kuka "아무래도…… 처, 처음 입을 때부터 뭔가 잘못됐는지,"

    ch_kuka "이게…… 자꾸 흘러내려서 발에 밟히……"

    show bg_naibu with hpunch

    show stand_Kuka_yukata_surprised with dissolve
    hide stand_Kuka_yukata_shamed

    ch_kuka "꺄악……?!?!!"

    hide stand_Kuka_yukata_surprised

    player "엇……!!"

    ch_kuka "너, 넘어져 버렷……!!!"

    show bg_black with dissolve
    hide bg_naibu

    stop music

    ch_kuka "……"

    ch_kuka "에……"

    $ renpy.pause(1.0)

    play music "audio/main/11fun.mp3"

    show cg_kuka_ykt_1 with fade

    show cg_kuka_ykt_1 with hpunch

    ch_kuka "{b}{size=30}에에에엣~~?!!!{/size}{/b}"

    ch_kuka "{b}{size=30}도S 씨?!?!?!{/size}{/b}"

    ch_kuka "{b}{size=30}이…… 이이, 이런 곳에서 저질러 버릴 생각인가요?!!{/size}{/b}"    

    ch_kuka "{b}{size=30}이 무슨 대담함……!! 이…… 인격파탄자!!!{/size}{/b}"

    ch_kuka "벗겨질락 말락 하는 유카타를 홀딱 벗겨 누구에게도 보여준 적 없는 쿠우카의 쿠우카를 만천하에 드러내고…… 수치심에 어쩔 줄 몰라하는 쿠우카의 귀에 {b}너도 사실은 이런 걸 원하고 있었지{/b} 라고 속삭이며, 남자는 욕망의 골짜기에 두 손을 뻗친다…… 쿠헤헷……"    
    
    player "아니…… 넘어질 뻔한 걸 잡아 준 것 뿐이고……"

    show cg_kuka_ykt_2 with dissolve
    hide cg_kuka_ykt_1

    ch_kuka "라…… 랄까, 그, 그보다 도, 도, 도, 도S 씨……!"

    ch_kuka "너, 너, 너무…… 가…… 가깝지 않나요……?!"

    player "응?"

    ch_kuka "그, 수, 숨, 숨결……"

    show cg_kuka_ykt_3 with dissolve
    hide cg_kuka_ykt_2

    ch_kuka "목에, 숨결이 닿아서…… 아우우……"

    ch_nar "숨결……?"

    ch_nar "그러네…… 이런 자세라면……"

    ch_nar "……장난 좀 쳐 줄까?"

    player "후우우우……"

    show cg_kuka_ykt_1 with hpunch
    hide cg_kuka_ykt_3

    ch_kuka "{b}{size=30}히이~~~~!!!!!{/size}{/b}"

    ch_nar "까, 깜짝이야."

    ch_nar "너무 심했나……?!"

    show cg_kuka_ykt_2 with dissolve
    hide cg_kuka_ykt_1

    ch_kuka "………"

    player "미…… 미안……! 장난이 과했……"

    ch_kuka "더어……"

    player "??"

    show cg_kuka_ykt_1 with hpunch
    hide cg_kuka_ykt_2

    ch_kuka "더 해 주세요오오!!!!!!!"

    player "뭐?!?!"

    ch_kuka "방금, 방금 거……!!!"

    ch_kuka "버르읏♥ 버릇이 될 것 같아요오!!!!!"

    ch_kuka "이…… 이런 걸 당해 버리면…… 쿠우카……!!!"

    show cg_kuka_ykt_1 with hpunch

    ch_kuka "도S 씨 이외에는 만족할 수 없는 몸이 되어 버려요!!!!!! 케헤헷!!!! 케게게게!!!!!"

    player "내, 내가 뭘 했……?!"

    ch_monica "쿠우카! 무슨 일이냐! 큰 소리가 났는데……!"

    ch_kuka "도S 씨가…… 도S 씨가……!!! 누구에게도 만져진 적 없는 쿠우카의 스위치를……"

    show bg_black
    hide cg_kuka_ykt_1

    extend " 우브부붑~~~!!!!"

    player "뭐, 뭔 소리야!!!! 그런 적 없어!!!!!!"

    ch_kuka "우그응……!! 응큿, 응보옵……♥"

    player "이…… 이상한 소리 내지 마!!!!!"

    ch_ninon "쇼군……?! 쉐상에 만솽에……"

    ch_monica "……귀공, 대체 무슨 짓을……"

    player "아무 짓도 안 했어어~~!!!!!!"

    ch_kuka "쿠헤헤헤헷……!!"

    stop music

    jump sceneNum16Common

label cg_kukasecond:

    scene cg_kuka_onsen_01 with fade

    play music "audio/main/8sad.mp3"

    ch_kuka "으헤…… 흐헤헤헷……♥"

    player "뭐가 그렇게 좋은 거야?"

    ch_kuka "크흐흐…… 좋지 않을 리가 있나요……!"

    ch_kuka "반나체 상태로 야외에 쫓겨나, 부끄러운 몰골을 누군가에게 들킬세라 근처의 물웅덩이에 허겁지겁 몸을 숨긴 채 행여 지나가는 사람이 없는지 불안에 떨며 날밤을 지새워야 하는 비합리적 상황!!!"

    ch_kuka "거기다 좋아하는 도S 씨와 단둘이 있을 수 있어서……!"

    show cg_kuka_onsen_02 with dissolve
    hide cg_kuka_onsen_01

    ch_kuka "……아, 바…… 방금 말은…… 못 들은 걸로 해 주세요……"

    show cg_kuka_onsen_01 with dissolve
    hide cg_kuka_onsen_02

    ch_kuka "그흐흐…… 떨림이 멈추지 않아…… 흥분할 대로 흥분한 나머지, 견딜 수 없을 만큼 뜨거워진 쿠우카의 몸과 마음이…… 차디찬 밤공기를 격렬하게 달구고 있어요……!!! 이건 마치 음양의 조화…… 남과 여의 화합!!!! 츄르르릅……"

    player "……쿠우카, 가만히 있어 봐."

    show cg_kuka_onsen_hand_01 with dissolve
    hide cg_kuka_onsen_01

    ch_kuka "……"

    show cg_kuka_onsen_03 with hpunch
    hide cg_kuka_onsen_hand_01

    ch_kuka "{b}{size=30}……햐앗?!?!!{/size}{/b}"

    ch_kuka "으, 아우, 으아……?!"

    ch_kuka "어, 도…… 도S 씨!?"

    ch_kuka "가, 가, 가, 갑자기 무슨……?!"

    show cg_kuka_onsen_hand_01 with dissolve
    hide cg_kuka_onsen_03

    ch_kuka "여, 역시 도S씨는…… 쿠우카가 방심하는 순간만을 기다렸던 것이군요!!!"

    ch_kuka "이대로 쿠, 쿠우카는, 「아름다운 꽃이로구나. 꺾어서 내가 가져야겠어」 라며 덮쳐 오는 음흉한 손길에 저항할 새도 없이 어른의 계단을 오르게 되고…… 크흣, 크흐흐……"

    ch_kuka "이…… 이제 쿠우카는 몸도 마음도 도S씨에게 사로잡힌 채 절대복종하는 노예가 되어버리는 거네요!!!"

    player "……?"

    player "침을 너무 흘리길래 닦아 주려던 건데."

    ch_kuka "……에?"

    ch_kuka "……침…… 말인가요?"

    player "응."

    ch_kuka "그러니까…… 쿠우카의 침을 닦아 주기 위해 손을 내밀었을 뿐이고, 다른 의도는 없었다…… 라고요?"

    player "응."

    show cg_kuka_onsen_hand_02 with dissolve
    hide cg_kuka_onsen_hand_01

    ch_kuka "…………"

    ch_kuka "쿠…… 쿠우카는 도S 씨의 꿍꿍이를 알고 있어요……"

    ch_kuka "이, 이렇게 상냥한 모습을 보여 주면서 안심시킨 뒤……"

    show cg_kuka_onsen_hand_01 with dissolve
    hide cg_kuka_onsen_hand_02

    show highlight

    ch_kuka "{b}완전히 경계심이 풀어졌을 때!!! 쿠우카를 온전히 취할 수 있는 그 순간을 노리신다는 것을!!!! 쿠헤헤헤헷!!!!{/b}"

    menu:
        "“그딴 거 관심 없어.”choice_1":
            $point_kuka -= 1
            show cg_kuka_onsen_01 with dissolve
            hide cg_kuka_onsen_hand_01

            ch_kuka "{b}{size=30}엣.{/size}{/b}"

            ch_kuka "……도S 씨…… 방금 뭐라고……?"

            player "못 들었어?"

            player "관심 없다고."

            ch_kuka "엣…… 에에?"

            player "그…… 그럴 리가? 도S 씨 정도의 음탕한 남성이…… 이런 일에 관심이 없다니……?!"

            $renpy.pause(1.0)

            ch_kuka "……그, 그렇군요!!!"

            ch_kuka "도S 씨가 혼자 쏙 빠져 나가면…… 쿠우카만 정신 나간 변태가 되는 거니까!!!!"

            ch_kuka "순진한 쿠우카를 변태로 몰아, 억울함과 수치심에 몸서리치는 상황을 유도하신 거였네요!!!"

            ch_kuka "역시 도S 씨는…… 최악이에요!!!! 이…… 도덕 분쇄자!! 두 발로 걷는 짐승!!!!"

            ch_kuka "쿠히히히히!!! 이제 만족하시나요!!! 좀 더…… 좀 더 쿠우카를 괴롭혀 주세요……!!! 지금 당장……!!!"

        "   “그런 심한 짓은 하지 않아.”choice_2":
            $point_kuka += 1

            ch_kuka "거, 거짓말……!!"

            ch_kuka "지…… 지금도 기회를 호시탐탐 노리고 있는 도S 씨의 손이 그것을 증명……"

            show cg_kuka_onsen_01 with dissolve
            hide cg_kuka_onsen_hand_01

            ch_kuka "……에?"

            player "쿠우카는……"

            player "정말로 나를…… 그런 놈이라고 생각해?"

            show cg_kuka_onsen_02 with dissolve
            hide cg_kuka_onsen_01

            ch_kuka "……"

            ch_kuka "도S 씨가 그런 무뢰한이 아니라는 것쯤은…… 저도 알아요……"

            ch_kuka "그, 그치만……"

            show cg_kuka_onsen_01 with dissolve
            hide cg_kuka_onsen_02

            ch_kuka "{b}{size=30}오…… 오히려 쿠우카의 욕망이……!!! 도S 씨가 그렇게 해 주기를 바라고 있어요!!!!!{/size}{/b}"

            ch_kuka "{b}{size=30}도S 씨!!!! 지금 당장…… 쿠우카에게 심한 짓을 해 주세요!!!!! 쿠헤헤헤헷!!!!{/size}{/b}"


        "“들켰네?”choice_3":
            show cg_kuka_onsen_01 with dissolve
            hide cg_kuka_onsen_hand_01

            ch_kuka "여…… 역시……!!!"

            ch_kuka "도S 씨는 갱생조차 불가능한 인간쓰레기네요!!!"

            ch_kuka "……아니, 오히려 좋아……!!"

            ch_kuka "더 이상 더러워질 수도 없는 도S 씨의 시커먼 욕망을…… 전부!!! 쿠우카에게 쏟아부어 주세요!!!!"

    show cg_kuka_onsen_01 onlayer middle
    hide cg_kuka_onsen_01

    $camera_move(-100, -500, 500, 0, 1)

    ch_kuka "크히히히히…… 도S 씨……!!!"

    ch_kuka "어서…… 어서 쿠우카를……!!! 엉망진창 덮쳐 주세요오오……!!!! 케케케켓!!!"

    $renpy.pause(1.0)
    stop music

    play sound "audio/sound/surp.mp3"

    show stand_gura onlayer forward with dissolve:
        xalign 0.5 yalign 0.4

    show highlight onlayer forward

    ch_gura "여러부우우{font=NanumGothic.ttf}————{/font}우운!!!!!!!!!!!"

    ch_gura "구하러 왔슴다{font=NanumGothic.ttf}————{/font}아앗!!!!!!!!!!!!"

    $camera_move(0, 0, 0, 0, 0)

    show bg_outside_onsen_2
    hide highlight onlayer forward
    hide stand_gura onlayer forward
    hide cg_kuka_onsen_01 onlayer middle

    show ob_yas3 with dissolve

    play sound "audio/sound/monkey.mp3"

    play music "audio/main/emer.mp3"

    monster "아 씹빨!!!!! 폭풍야스 왜 안하냐고!!!!!!!!"

    hide ob_yas3

    ch_kuka surp "꺄아아아악~~~?!?!!"

    player "뭐, 뭐야!!!!"

    show stand_gura with dissolve

    ch_gura "다들 무사하시군요!!!! 다행히 늦지 않았습니다!!!!!"

    hide stand_gura

    player "뭐가…… 뭐가 어떻게 된 거야……?!"

    player "난 여기서 뭘 하고 있었던 거지?!"

    show stand_gura with dissolve

    ch_gura "자세히 설명할 시간이 없습니다!!!"

    ch_gura "여러분들은 저 마물에게 홀렸던 겁니다!!!"

    hide stand_gura

    show ob_yas1 with dissolve

    play sound "audio/sound/monkey2.mp3"

    monster "우끼긱!!!!!! 우꺅!!!!!!!"

    ch_kuka surp "저…… 저게 대체 뭔가요……!!!"

    hide ob_yas1

    show stand_gura with dissolve

    ch_gura "정신 차리십쇼!!!!! 지금 당장 놈을 퇴치해야 합니다!!!!"

    hide stand_gura

    player "퇴치?! 때려잡으면 되는 거야?!"

    show stand_gura with dissolve

    ch_gura "아니오!!!! 놈은 야스를 하지 못하고 죽은 원념이 모여 탄생한 정신체!!!!"

    ch_gura "물리적 공격은 통하지 않습니다!!!!"

    hide stand_gura

    player "그…… 그러면 어떻게 해?!!"

    show stand_gura with dissolve

    ch_gura "방법은 하나!!!!"

    ch_gura "20년이 넘도록 순결을 지켜 온 청년의 피가 스며든 물건을…… 녀석의 눈앞에서 불태우는 의식을 행해야 합니다!!!!"

    hide stand_gura

    play sound "audio/sound/monkey2.mp3"

    show ob_yas3 with dissolve

    monster "우끽!!! 우끽!!! 우끼긱!!!!! 우끽!!!!! 우꺅!!!!"

    hide ob_yas3

    player "아 진짜!!! 어디서부터 태클을 걸어야 할지 모르겠어!!!!"

    player "그리고 그딴 걸 갑자기 어디서 구……"

    player "……"

    $renpy.pause(1.0)

    show ob_hankachi with dissolve:
        xpos 430 yalign 0.3

    player "……이거……"

    player "……불태우면…… 될 것 같은데……"

    ch_gura "전…… 전라 상태인데?! 어디서 그런 걸 꺼내신 겁니까?!!"

    player "그런 건 중요하지 않아!!!!"

    player "불!!! 빨리 불!!!!"

    hide ob_hankachi
    show stand_gura with dissolve

    ch_gura "네…… 넵!!!!!!"

    play sound "audio/sound/fire.mp3"
    show fire_small:
        xpos 100 ypos 210

    ch_gura "퐈이야{font=NanumGothic.ttf}——{/font}!!!!!!!!"

    hide fire_small

    show ob_yas2 with dissolve

    play sound "audio/sound/monkey2.mp3"

    monster "아 ㅋㅋ 야스각이었는데 ㅋ"

    monster "까비아깝송~"

    hide ob_yas2 with squares

    stop music

    show stand_gura with dissolve

    ch_gura "허억…… 후우……"

    ch_gura "해……"

    ch_gura "해치웠다!!!!!! 드디어!!!!!!"

    show bg_outside_onsen_2

    ch_gura "여러분 덕분임다!!!! 감사함다{font=NanumGothic.ttf}———{/font}아앗!!!!!!"

    hide stand_gura

    ch_kuka dere "……도S 씨, 그런데……"

    ch_kuka dere "저, 저걸 불태웠다는 건…… 20년 넘게 동정……"

    player "시끄러워……"
    
    jump scene25Common

## 유키 루트 ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
##
##
## S# 11. 유키 1번 cg
label cg_yukifirst:
    show bg_black
    ## 유키 1번 cg 배경
    scene bg_cg_yuki_01 with fade

    play music "audio/main/5orientalcommon.mp3"

    player "후우……"

    player "별로 한 것도 없는데 왜 이리 피곤하지……?"

    ch_nar "……탈의실에 다른 손님이 아무도 없다."

    ch_nar "손님 네댓 명으로는 이 정도로 규모 있는 온천을 운영하기 힘들 텐데……"

    ch_nar "이것도 그 마물의 영향인가."

    ch_nar "이래저래 고생이 많아 보이네. 난 마망이 알아서 먹여 살려 주는데. ㅋㅋ루삥빵뽕"

    ch_nar "참, 콧코로 도망갔지."

    ch_nar "빼애앵……"

    ## 유키 1번 cg 표정 1로 변경
    show cg_yuki_01 with dissolve
    hide bg_cg_yuki_01

    ch_yuki "흥~ 흐흥……♬"

    ch_nar "이 녀석은 뭐가 그렇게 신나는 걸까……"

    ch_nar "……그보다 벌써 탈의가 끝났어?!"

    ch_nar "입는 것도 벗는 것도 엄청나게 어려워 보이는 옷이었는데?"

    ch_nar "여자들은 원래 옷 갈아입는 속도가 이렇게 빠른 건가?!"

    ## 호흡 끊기
    $renpy.pause(1.0)

    ch_nar "……잠깐, 무슨 쌉소리야."

    ch_nar "이 자식 남자라고."

    ch_nar "……"

    ch_nar "보면 볼수록 놀랍다."

    ch_nar "방심하면 뇌가 멋대로 여자라고 착각해 버리지만,"

    ch_nar "이 녀석은 명실상부한 ‘남자’라는 사실이……"

    ch_nar "길고 진한 속눈썹."

    ch_nar "잡티 하나 없이 뽀얀 피부."

    ch_nar "호리하고 가냘픈 몸매……"

    ch_nar "어디를 어떻게 봐도 여자애다."

    ch_nar "사실 남자라는 건 거짓말 아닐까……?"

    ch_nar "뭐…… 곧 확인해 볼 수 있겠지만……"

    ## 유키 1번 cg 표정 2
    show cg_yuki_02 with dissolve
    hide cg_yuki_01

    ch_yuki "응?"

    ## 호흡 끊기
    $renpy.pause(1.0)

    ch_nar "아…… 눈 마주쳤다."

    ch_nar "너무 빤히 보고 있었나……" 

    ## 유키 1번 cg 표정 3
    show cg_yuki_03 with dissolve
    hide cg_yuki_02

    ch_yuki "헤에~ [name], 아름다운 내 몸에 관심 있어?"   

    ch_yuki "좀 더 가까이서 봐도 괜찮아~ 백옥 같은 내 살결을 직접 볼 수 있는 기회는 흔치 않으니까."
    
    player "아…… 응……"

    ch_yuki "만져 보고 싶어?"

    player "그런 말은 안 했……"

    ch_yuki "그건 곤란한걸…… 완벽한 내 피부에 흠이라도 생긴다면 그건 곧 전 지구적 손실이라서."
    
    player "그런 말 안 했다고!!!"

    ch_yuki "아니면……"

    play sound "audio/sound/surp.mp3"

    ## 유키 1번 표정 3 cg 완
    show cg_yuki_03_plus with dissolve
    hide cg_yuki_03

    ch_yuki "내 {color=#FF2929}아름다움{/color}이 잔뜩 배어 있는 {color=#FF2929}팬티{/color}라도 가질래? 너에게만 주는 특권이야♪"

    ## 호흡 끊기
    $renpy.pause(1.0)

    player "필요 없어!!!!"

    player "그보다 남자 팬티가 왜 저 따위로 생긴 건데?!"

    ch_yuki "부끄러워하긴~ 나중에 후회해도 모른다?"

    ch_yuki "천재일우의 기회를 놓치다니, 너도 참 둔감하네~"

    ch_nar "저런 정신 나간 말을 아무렇지 않게 할 수 있는 것도 재능이 아닐까……"

    ch_nar "덕분에 더 피곤해졌다. 자고 싶어……"

    hide cg_yuki_03_plus

    jump sceneNum11_2Common

label cg_yukisecond:
    scene cg_yuki_onsen_01 with fade
    play music "audio/main/8sad.mp3"

    ch_yuki "아아~ 곤란한걸."

    ch_yuki "그렇지 않아도 눈부시던 나의 미모가…… 달빛을 받아 더욱 환하게 빛나고 있어."

    ch_yuki "이대로라면, 나의 아름다움만으로 온 세상의 어둠을 걷어 낼 수 있을지도 모르겠네……♪"

    ch_yuki "그나저나 참 신기해."

    ch_yuki "땀냄새 나는 남자들이 몸을 담갔던 곳이라 생각하면 불쾌해야 할 텐데……"

    ch_yuki "왠지 모르게 좋은 기분이 들어…… 구름 위에 둥둥 떠있는 느낌♪"

    ch_yuki "……너와 단둘이 있어서일까?"

    $renpy.pause(1.0)

    ch_yuki "그보다…… 아까부터 왜 그러고 있어~?"

    ch_yuki "{b}남자끼리인데도{/b} 부끄러운 거야? 귀엽긴~"

    ch_yuki "자꾸 그러면, {color=#FF2929}여기 아래{/color}…… 들춰서 보여줘 버릴까나……♬"

    menu:
        "“그건 좀……”choice_1":
            $point_yuki -= 1
            show cg_yuki_onsen_02 with dissolve
            hide cg_yuki_onsen_01

            ch_yuki "흐응…… 김새네."

            ch_yuki "뭐냐고, 그 미적지근한 반응."

            ch_yuki "세계 최고로 예쁘고 귀여운 나를 이런 식으로 대한 사람은 네가 처음이야."

            ch_yuki "보는 눈이 없는 것도 정도가 있다구. 알아?"

            ch_yuki "흥! 유키 삐졌어!"

        "  “보여 줘!!!!”choice_2":

            ch_yuki "아핫, 좋은 반응~♪"

            ch_yuki "그렇게까지 보고 싶은 거야?"

            show cg_yuki_onsen_01 with hpunch
            player "{b}{size=30}보고 싶어!!!!!!!!!!!{/size}{/b}"

            ch_yuki "응응, 평소보다 훨씬 격렬하게 나를 원하고 있구나?"

            ch_yuki "뭐…… 이렇게나 아름다운 모습을 보는 건 처음일 테니, 이상할 것도 없지."

            ch_yuki "그럼…… 제대로 봐 줘야 해?"

        "“만지게 해 줘!!!!!”choice_3":
            $point_yuki += 1
            ch_yuki "만지게 해 달라구?"

            ch_yuki "흐음…… 보여주는 것 이상은 NG인데……"

            ch_yuki "……어쩔까나~?"

            player "{b}{size=30}나…… 나도!!!{/size}{/b}"

            player "{b}{size=30}나도 만질 거야!!!!{/size}{/b}"

            show cg_yuki_onsen_02 with dissolve
            hide cg_yuki_onsen_01

            ch_yuki "……오늘의 너는 조금…… 무섭네……"

            show cg_yuki_onsen_01 with dissolve
            hide cg_yuki_onsen_02

            ch_yuki "뭐, 상관 없나."

            ch_yuki "좋아! 그렇게까지 바란다면…… 어쩔 수 없네."

            ch_yuki "그치만, 착각은 금물이야."

            ch_yuki "……너니까 허락해 준 거라구?"

            ch_yuki "세계 최고로 귀여운 나를 아무나 만지게 해 줄 리가 없잖아? 영광으로 알아~♪"


    show cg_yuki_onsen_01 onlayer middle with dissolve

    $camera_move(0, 0, 400, 0, 0.3)

    ch_yuki "우왓? 가까워……"

    ch_yuki "꺄아~ 드디어 할 마음이 생긴 거야?"

    ch_yuki "원래라면, 누구에게도 허락하지 않겠지만……"

    ch_yuki "너라면…… 괜찮을지도."

    ch_yuki "응, 좋아."

    ch_yuki "와 줘……♪"

    $renpy.pause(2.0)

    stop music
    play sound "audio/sound/surp.mp3"

    show stand_gura onlayer forward with dissolve:
        xalign 0.5 yalign 0.4

    show highlight onlayer forward

    ch_gura "여러부우우{font=NanumGothic.ttf}————{/font}우운!!!!!!!!!!!"

    ch_gura "구하러 왔슴다{font=NanumGothic.ttf}————{/font}아앗!!!!!!!!!!!!"

    $camera_move(0, 0, 0, 0, 0)

    show bg_outside_onsen_2
    hide highlight onlayer forward
    hide stand_gura onlayer forward
    hide cg_yuki_onsen_01 onlayer middle

    show ob_yas3 with dissolve

    play sound "audio/sound/monkey.mp3"

    play music "audio/main/emer.mp3"

    monster "아 씹빨!!!!! 폭풍야스 왜 안하냐고!!!!!!!!"

    hide ob_yas3

    ch_yuki angry "으아아악~~!!"

    player "뭐, 뭐야!!!!"

    show stand_gura with dissolve

    ch_gura "다들 무사하시군요!!!! 다행히 늦지 않았습니다!!!!!"

    hide stand_gura

    player "뭐가…… 뭐가 어떻게 된 거야……?!"

    player "난 여기서 뭘 하고 있었던 거지?!"

    show stand_gura with dissolve

    ch_gura "자세히 설명할 시간이 없습니다!!!"

    ch_gura "여러분들은 저 마물에게 홀렸던 겁니다!!!"

    hide stand_gura

    show ob_yas1 with dissolve

    play sound "audio/sound/monkey2.mp3"

    monster "우끼긱!!!!!! 우꺅!!!!!!!"

    ch_yuki angry "저…… 저게 대체 뭐야!!! 더럽고 흉측해!!!!"

    hide ob_yas1

    show stand_gura with dissolve

    ch_gura "정신 차리십쇼!!!!! 지금 당장 놈을 퇴치해야 합니다!!!!"

    hide stand_gura

    player "퇴치?! 때려잡으면 되는 거야?!"

    show stand_gura with dissolve

    ch_gura "아니오!!!! 놈은 야스를 하지 못하고 죽은 원념이 모여 탄생한 정신체!!!!"

    ch_gura "물리적 공격은 통하지 않습니다!!!!"

    hide stand_gura

    player "그…… 그러면 어떻게 해?!!"

    show stand_gura with dissolve

    ch_gura "방법은 하나!!!!"

    ch_gura "20년이 넘도록 순결을 지켜 온 청년의 피가 스며든 물건을…… 녀석의 눈앞에서 불태우는 의식을 행해야 합니다!!!!"

    hide stand_gura

    play sound "audio/sound/monkey2.mp3"

    show ob_yas3 with dissolve

    monster "우끽!!! 우끽!!! 우끼긱!!!!! 우끽!!!!! 우꺅!!!!"

    hide ob_yas3

    player "아 진짜!!! 어디서부터 태클을 걸어야 할지 모르겠어!!!!"

    player "그리고 그딴 걸 갑자기 어디서 구……"

    player "……"

    $renpy.pause(1.0)

    show ob_hankachi with dissolve:
        xpos 430 yalign 0.3

    player "……이거……"

    player "……불태우면…… 될 것 같은데……"

    ch_gura "전…… 전라 상태인데?! 어디서 그런 걸 꺼내신 겁니까?!!"

    player "그런 건 중요하지 않아!!!!"

    player "불!!! 빨리 불!!!!"

    hide ob_hankachi
    show stand_gura with dissolve

    ch_gura "네…… 넵!!!!!!"

    play sound "audio/sound/fire.mp3"
    show fire_small:
        xpos 100 ypos 210

    ch_gura "퐈이야{font=NanumGothic.ttf}——{/font}!!!!!!!!"

    hide fire_small

    show ob_yas2 with dissolve

    play sound "audio/sound/monkey2.mp3"

    monster "아 ㅋㅋ 야스각이었는데 ㅋ"

    monster "까비아깝송~"

    hide ob_yas2 with squares

    stop music

    show stand_gura with dissolve

    ch_gura "허억…… 후우……"

    ch_gura "해……"

    ch_gura "해치웠다!!!!!! 드디어!!!!!!"

    show bg_outside_onsen_2

    ch_gura "여러분 덕분임다!!!! 감사함다{font=NanumGothic.ttf}———{/font}아앗!!!!!!"

    hide stand_gura

    ch_yuki smile "……저기, 있잖아……"

    ch_yuki smile "저걸 불태웠다는 건…… 너, 20년 넘게 동정……"

    player "시끄러워……"

    jump scene25Common
           
## 엔딩 ########################################
##
##
## 니논 해피 엔딩 #############
label ninonHappy:

    play music "audio/main/8sad.mp3"

    ## 통학로 cg
    scene bg_tyugaku

    ch_nar "평소와 다를 것 없는 하루,"

    ch_nar "{font=NanumGothic.ttf}―{/font} 였다고 생각했다."

    ch_nar "츠바키가오카의 하굣길은 인적이 드문 편이다."

    ch_nar "하염없이 누군가를 기다리는 금발의 미소녀가 눈에 띄지 않는 것이 이상할 정도로 말이다."

    ch_nar "귀가부인 나보다도 한 발 먼저 학교를 빠져나온 뒤, 거리가 꽤 되는 오린도 고교에서부터 쉬지 않고 달려와 매일 같은 자리에서 나를 기다리던 소녀."

    ch_nar "도시전설과도 같은 비일상적 일상."

    ch_nar "그 빈번함에 취해 소중한 것에 감사하는 법을 잊어서일까."

    ch_nar "언제나 모퉁이에 쪼그려 앉아 “인법 {font=NanumGothic.ttf}·{/font} 다랑어의 술!” 따위를 외치며 길고양이들을 규합하던 그녀의 모습은 온데간데없었다."

    ch_nar "구심점을 상실한 패거리만이 갈 곳을 잃은 채 거리를 서성일 뿐이었다."

    player "……"

    hide bg_tyugaku
    show bg_tyugaku_running

    play sound "audio/sound/running.mp3" loop

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

    stop sound

    ch_nar "숨이 턱까지 차올랐다."

    ch_nar "벽에 팔을 걸친 채 있는 힘껏 기침을 해 댔다."

    ch_nar "구역질이 나왔다."

    ch_nar "그녀의 모습을 두 눈에 새기기 전까지는 멈출 수 없었다."

    ch_nar "심장이 터질 것 같은 고통조차도,"

    ch_nar "그녀를 다시 볼 수 없을지 모른다는 공포로부터 나를 벗어나게 할 수는 없었다."

    ch_nar "마지막 잡념을 토해내고는 오린도 고교를 향해 고개를 쳐들었다."

    show cg_ninon_happy_01 with dissolve
    show snow onlayer forward
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

    ch_nar "장난스러운 어감이지만, 그녀에게는 동경 {font=NanumGothic.ttf}―{/font}"

    ch_nar "{font=NanumGothic.ttf}―{/font} 혹은 그 이상의 감정이 담겨 있을지 모르는 호칭."

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

    ch_ninon "쇼군은…… 정말로 잔인한 남자예요 입니다."

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

    ch_ninon "{i}……Je t'aime, a' la folie.{/i}"

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

    ch_nar "……"

    ch_nar "……안녕, 니논."

    hide snow onlayer forward
    hide bg_black
    ## 빨려들어가는 효과
    play sound "audio/sound/amesopen.mp3"
    show ames_reverse with dissolve
    $renpy.pause(4.0)
    
    stop music fadeout 1.0
    ## 아메스 ####################################
    play music "audio/main/ames.mp3" fadein 3.0
    ## 아메스 cg DIS
    show cg_ames with dissolve
    hide ames_reverse
    hatena "……와우."

    hatena "엄청난…… 걸 봐버렸네."

    hatena "……대충 예상했겠지만, 방금 당신이 본 건 말이지,"

    hatena "열심히 한 당신에게 주는 상……이었어야 하는데, 원래는."

    hatena "뭐…… 그렇게 기운 빠질 것 없어. 어차피, 금방 잊어버릴 꿈 같은 거니까……"

    hatena "정말로 꿈이 맞냐고? 글쎄, 어떨까나……"

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
    
    hatena "남의 연애사에 참견하는 건 그다지 바람직한 일은 아니지만, 어쩔 수 없어. 이건 여자아이의 본능 같은 거라구, 후후……♪"

    hatena "도움이 되었길 바랄게. 어떤 의미로든."

    hatena "……어이쿠, 시간을 너무 많이 잡아먹었네."

    hatena "뭐, 오늘은 여기까지 해둘까."

    hatena "그럼 또 봐."

    ## 빨려들어가는 효과
    play sound "audio/sound/amesclose.mp3"
    show ames_swift
    $renpy.pause(3.0)
    stop music fadeout 3.0
    ## 랜드솔 마을 #####################


    play music "audio/main/8sad.mp3"
    show bg_town with fade
    hide ames_swift

    show stand_Ninon_embarassed with dissolve

    ch_ninon "……쇼군, 쇼군! 정신차리시오 입니다!"

    hide stand_Ninon_embarassed

    player "……니논?"

    show stand_Ninon_panic with dissolve

    ch_ninon "오옷! 니논을 알아보시는 겁니까!"

    show stand_Ninon_innocence
    hide stand_Ninon_panic

    ch_ninon "휘유~ 한시름 놨다 입니다~ 쇼군이 잘못되기라도 하면…… 니논은 할복할 수밖에 없다 입니다……!"

    hide stand_Ninon_innocence

    player "니논, 혹시……"

    player "이상한 꿈…… 같은 거 꾸지 않았어?"

    show stand_Ninon_embarassed with dissolve

    ch_ninon "……네? 꿈 말입니다?"

    ch_ninon "그, 글쎄올시다~ 입니다."

    ch_ninon "니논은 그냥 잠시 정신을 잃었다가, 깨어나보니 쇼군이 옆에 대자로 드러누워 있었다 입니다!"

    ch_ninon "뭐 안 좋은 꿈이라도 꾸었나요 입니까?"

    show stand_Ninon_panic
    hide stand_Ninon_embarassed

    ch_ninon "설마…… 귀신 씨가 나오는 꿈……? Non~!! 니논은 무서운 건 질색 팔색 패왕색 입니다~!!"

    ch_monica "니논! [name]!! 무사한가?!"

    show stand_Ninon
    hide stand_Ninon_panic

    ch_ninon "앗! 여러분! 쇼군이 정신을 차렸다 입니다~! 여기 여기~ 여기에요 입니다~~!!"

    hide stand_Ninon

    ch_nar "……여전하네."

    ch_nar "너는 언제나 어설픈 게 문제라고, 귀에 못이 박히도록 이야기했는데……"

    ch_nar "그런 어설픈 거짓말에 속아줄 리가 없잖아."

    ch_nar "그렇게 눈시울을 잔뜩 붉힌 채로 횡설수설하면, 누구라도 눈치챌 거라고."

    ch_nar "……"

    ch_nar "그래, 그거면 됐어."

    ch_nar "어리숙하고 바보 같은 모습이어도 좋아."

    ch_nar "그래야 네 곁을 지킬 이유가 생기니까."

    ch_nar "눈이 마주칠 때면 나를 향해 웃어 줘."

    ch_nar "나도 너를 보며 미소 지을 수 있게."

    ch_nar "늘 그래 왔듯이……"

    ch_nar "언젠가 끝이 온다 해도,"

    ch_nar "슬픈 내일 따위는 생각하지 말고,"

    ch_nar "행복한 오늘만을 살아 줘."

    ch_nar "……늘, 그래 왔듯이."

    ch_nar "앞으로도 잘 부탁해, 니논."

    stop music fadeout 3.0

    show bg_black with fade
    hide bg_town

    $renpy.pause(2.0)

    show stand_Ninon_wink with dissolve

    ch_ninon "……닌닌♪"

    show bg_end with dissolve

    $renpy.pause(1.0)

    ch_nar "Thank you for playing"

    return
## 모니카 해피 엔딩 ############
label monicaHappy:

    play music "audio/main/11fun.mp3"

    scene cg_monica onlayer middle with fade

    player "……"

    player "……으읏, 젠장……!!"

    player "더는 못 기다리겠어……!!!"

    player "모, 모니카!!"

    player "아직이야……?!"

    ch_monica "……귀공은 왜 이렇게 참을성이 없는 건가!"

    ch_monica "지금 몇 번째 물어보는 건지 알고는 있나?!"

    show cg_monica onlayer middle with hpunch

    player "일곱 번!!!!!"

    ch_monica "그걸 또 세는 건 대체……"

    ch_monica "에에잇, 아무튼……!"

    ch_monica "이제 들어갈 테니 그만 보채도록 해라!!"

    $camera_move(3000, 1500, 750, 0, 0.5)

    show cg_monica_basic onlayer middle with dissolve
    hide cg_monica onlayer middle

    $renpy.pause(1.5)

    $camera_move(-3000, -1500, 750, 0, 2)

    $renpy.pause(3.0)

    $camera_move(0, 0, 0, 0, 0.4)
    

    ch_monica "부탁한 대로 입어봤다만……"

    ch_monica "……애초에 이게 뭐라고 큰절까지 해 가며 부탁한 건지……"

    ch_monica "귀공은 가끔씩 이해하기 어려운 행동을 한단 말이야……"

    ch_monica "……그건 그렇고."

    show cg_monica_shame2 with dissolve
    hide cg_monica_basic onlayer middle

    ch_monica "아, 아무래도 이런 하늘하늘한 옷은…… 나와 어울릴 거라고 생각하진 않는데 말이지……"

    player "……"

    show cg_monica_shame1 with dissolve
    hide cg_monica_shame2

    ch_monica "귀공……?"

    ch_monica "……뭘 그렇게 빤히 보고만 있나?"

    player "………"

    ch_monica "그…… 그렇게까지 이상하다는 건가?"

    player "…………"

    ch_monica "무슨 말이라도 좀……!"

    player "아니, 그……"

    player "생각보다 너무……"

    $renpy.pause(1.0)

    player "……너무 귀여워서……"

    $renpy.pause(1.0)

    show cg_monica_dere2 with dissolve
    hide cg_monica_shame1

    ch_monica "……무……"

    show cg_monica_dere2 with hpunch

    ch_monica "무, 무무무…… 무, 무슨 소리를 하는 건가, 대체?!?!!"

    ch_monica "그…… 그, 그래, 그 말이로군!! 내가 어린아이 같다는 것이지?!! 귀, 귀공은 내가 어린애 취급 당하는 것을 싫어한……"

    player "아니…… 어린애 같다는 게 아니고,"

    player "진짜 예쁘고 귀여워서…… 이렇게까지 잘 어울릴 줄은 생각도 못 했어……"

    player "아마도 나는…… 오늘만을 위해 지금까지 살아온 게 아닑"

    show cg_monica_dere2 with hpunch

    ch_monica "시, 시끄럽다, 시끄럽다!!!! 시끄러워~~~!!!!! 더 말하지 마라!!!!!!"

    show cg_monica_shame2 with dissolve
    hide cg_monica_dere2

    player "……"

    player "저기……"

    ch_monica "……또 뭔가?!"

    player "한 번만 안아 봐도 될까요……?"

    show cg_monica_dere2 with dissolve
    hide cg_monica_shame2

    ch_monica "~~~~!!!!!"

    ch_monica "아아, 정말……!!"

    show cg_monica_shame2 onlayer middle with dissolve
    hide cg_monica_dere2

    ch_monica "……이젠 됐다. 귀공 마음대로 해라……"

    player "무야호!!!!!"

    show cg_monica_dere1 onlayer middle with dissolve
    hide cg_monica_shame2 onlayer middle

    show highlight onlayer forward

    $camera_move(-1000, -1000, 500, 0, 0.5)

    ch_monica "?!?!?!?!!??!?!?!"

    hide highlight onlayer forward

    ch_monica "우아아~~~악!!!!!!!!!!"

    show bg_black onlayer middle with dissolve

    $camera_move(0, 0, 0, 0, 0)

    hide cg_monica_dere1 onlayer middle

    play sound "audio/sound/hit.wav"

    $renpy.pause(1.0)

    hide bg_black onlayer middle
    show cg_monica_emb2 with fade

    ch_monica "……"

    ch_monica "……좀 어떤가?"

    player "아파……"

    ch_monica "아니…… 아, 아무리 마음대로 하라고 했다지만……!"

    ch_monica "그렇다고 냅다 돌진해 버리는 놈이 어디 있나……!!"

    player "그치만……"

    player "너무 귀엵"

    play sound "audio/sound/hit.wav"

    show cg_monica_emb2 with hpunch

    ch_monica "긋!!!!! 그나저나!!!!! 이…… 이 옷 말이다!!!"

    player "‘맞은 데 또 때렸어……’"

    show cg_monica_emb3 with dissolve
    hide cg_monica_emb2

    ch_monica "구, 군인인 나로서는 도저히 이해가 되지 않는 복장인데……"

    ch_monica "불필요한 장식이 너무 많고, 큰 동작을 취하기에도 제약이 심해…… 도대체 이런 옷은 누가 입는 거지?"

    player "메이드."

    show cg_monica_basic with dissolve
    hide cg_monica_emb3

    ch_monica "……메이드……?"

    ch_monica "하녀들이 주인의 시중을 들기 위해 입는 옷……이라고?"

    show cg_monica_bbang with dissolve
    hide cg_monica_basic

    ch_monica "귀…… 귀공은 나를 하대하고 싶은 건가? 불쾌하군! 이 건에 대해서는 나중에 제대로……"

    $renpy.pause(1.0)

    show cg_monica_emb3 with dissolve
    hide cg_monica_bbang

    ch_monica "아니, 농담이다! 농담!! 무릎을 꿇을 것까진 없지 않나! 당장 일어……"

    player "……왱알앵알."

    ch_monica "뭐라고? 목소리가 작아서 잘 안 들린……"

    ch_monica "………뭐라? ‘주인님’이라 불러달라고? 하트까지 붙여서 사랑스럽게……?"

    show cg_monica_bbang with dissolve
    hide cg_monica_emb3

    ch_monica "지, 지금 사과를 해도 모자랄 판에……! 귀공은 대체!"

    $renpy.pause(1.0)

    show cg_monica_emb2 with dissolve
    hide cg_monica_bbang

    ch_monica "…………알겠다."

    ch_monica "알겠으니까, 버려진 강아지마냥 불쌍한 표정으로 쳐다보는 건 이제 그만둬!"

    show cg_monica_shame2 with dissolve
    hide cg_monica_emb2

    ch_monica "나참…… 그렇게 필사적으로 매달리면 거절할 수도 없지 않나……"

    player "지, 진짜 해 주는 거야?!"

    player "진짜로?!?!!"

    show cg_monica_dere2 with dissolve
    hide cg_monica_shame2

    ch_monica "한다고, 한다니까!! 호들갑 떨지 마라!!!"

    show cg_monica_emb1 with dissolve
    hide cg_monica_dere2

    ch_monica "……"

    ch_monica "……흠, 흠!"

    ch_monica "그…… 주…… 주인……"

    player "아아아~~~~~"

    player "기다리다 늙어 죽는다아아아~~~~~"

    show cg_monica_emb2 with dissolve
    hide cg_monica_emb1

    ch_monica "보, 보채지 마라!!!!"

    ch_monica "큿…… 이 무슨 굴욕적인……"

    show cg_monica_emb1 with dissolve
    hide cg_monica_emb2

    ch_monica "……"

    show cg_monica_emb3 with dissolve
    hide cg_monica_emb1

    ch_monica "……주, 주……"

    ch_monica "……주인님……♥"

    $renpy.pause(1.0)

    show cg_monica_emb1 with dissolve
    hide cg_monica_emb3

    ch_monica "……"

    ch_monica "…………"

    $renpy.pause(1.0)

    show cg_monica_dere2 onlayer middle with hpunch
    hide cg_monica_emb1
    $camera_move(-1000, -1000, 500, 0, 0.5)

    ch_monica "……우아아아아아아악!!!!!!!!!!!!"

    $camera_move(0, 0, 0, 0, 0.5)

    show cg_monica_dere2 onlayer middle with hpunch
    
    ch_monica "방금 일은 잊어버려, 잊어버려라!!!!!!"

    player "모…… 모니카."

    player "방금 거…… 너무………"

    player "너무 귀여워서 심장읽"

    play sound "audio/sound/hit.wav"

    show cg_monica_dere1 onlayer middle with hpunch
    hide cg_monica_dere2 onlayer middle

    ch_monica "귀, 귀엽다고 하지 마아아아!!!!!!!!!"

    player "흐…… 흐헤헷…… 헤헤헤헤……"

    show cg_monica_dere1 onlayer middle with hpunch

    ch_monica "기분 나빠아아!!!!!!! 웃지 마라!!!! 죽일 거다!!!!!!!"

    show cg_monica_dere1 onlayer middle with hpunch

    ch_monica "우그으으으!!!!!! 지금 이 자리에서 귀공을 죽이고 나도 죽을 테다!!!!!!"

    ch_monica "바이스플뤼겔의 명예를 걸고 반드시!!!!!! 죽일 거다!!!!!!!!"

    player "히히 무서워. 도망가야징."

    player "아, 그 전에…… 우는 얼굴 귀여우니까 사진 찍어 놔야겠다."

    play sound "audio/sound/camera.mp3"

    ch_monica "뭣?!?! 사, 사진……?!?!!!"

    ch_monica "이……!!! 다…… 당장 지우지 못해!!!!!"

    show bg_black
    hide cg_monica_dere1 onlayer middle

    ch_monica "거기 서어어어어!!!!!!!!!!! 으아아앙!!!!!!!"

    stop music

    $renpy.pause(2.0)

    play sound "audio/sound/amesopen.mp3"
    show ames_reverse
    $renpy.pause(4.0)
    
    ## 아메스 ####################################
    play music "audio/main/ames.mp3" fadein 3.0
    show cg_ames with dissolve
    hide ames_reverse

    hatena "자, 수고하셨습니다."

    hatena "……랄까, 너무 괴롭히는 거 아니야?!"

    hatena "뭐어……? 반응이 귀여우니까 어쩔 수 없다고?"

    hatena "남자들이란 참…… 그러다 미움 받게 되더라도 난 모르는 일이다?"

    hatena "하긴…… 당신의 그런 점까지도 좋아하니까, 저렇게 잘 지낼 수 있는 거겠지."

    hatena "그래도 적당히 해. 너무 심하게 놀리면 정말로 화낼지도 모른다구."

    hatena "……그럴 땐 과자를 사 주면 금방 기분이 풀린다고……?"

    hatena "당신…… 아무리 모니카가 단 것을 좋아한다지만, 그렇게까지 단순할……"

    hatena "……단순……한가?"

    hatena "뭐…… 그것도 모니카가 귀여운 이유 중 하나이긴 하지."

    hatena "그렇지만, 모르는 사람이 과자를 사 준다고 해서 쫄래쫄래 따라가거나 하진 않을 테니, 너무 걱정하지 마."

    hatena "아무리 모니카가 작고 귀여운 아이 같아 보여도…… 일단은 ‘군인’이니까."

    hatena "……과자를 사 주면 금방 기분이 풀린다고 했지?"

    hatena "모니카처럼 똑 부러지는 아이가, 정말 그렇게 단순할 거라고 생각해?"

    hatena "그건…… 달고 맛있는 걸 사 주는 사람이 당신이라서,"

    hatena "맛있는 걸 함께 먹으며 웃을 수 있는 사람이, 바로 당신이라서야."

    hatena "모니카는 당차고 굳센 아이지만…… 혼자서 너무 많은 것을 짊어지려 해."

    hatena "그래도……"

    hatena "당신이 함께 있어 줄 때면, 잠깐이나마 그런 것을 잊을 수 있으니까."

    hatena "당신의 앞에서라면, 전장을 누비는 군인이 아니라……"

    hatena "귀여운 데코레이션을 곁들인 달콤한 디저트를 좋아하고,"

    hatena "어떤 옷을 입어야 남자친구가 더 좋아해 줄지 거울 앞에서 수십 번을 고민하는,"

    hatena "한 명의 순진한 ‘소녀’로 있을 수 있으니까."

    hatena "……그러니까!"

    hatena "앞으로도 그녀를 잘 부탁해."

    hatena "너무 괴롭히지 말고, 과자도 많이 사 주고!"

    hatena "그럼…… 또 봐."

    stop music fadeout 3.0
    play sound "audio/sound/amesclose.mp3"
    show ames_swift
    hide cg_ames

    $renpy.pause(3.0)

    play music "audio/main/3town.mp3"
    show bg_town with fade
    hide ames_swift

    show stand_Monica_down with dissolve

    ch_monica "으음……"

    hide stand_Monica_down

    player "……으…… 머리야……"

    show stand_Monica_down with dissolve

    ch_monica "귀공, 정신을 차렸나……?"

    hide stand_Monica_down

    player "여기가 어디……?"

    show stand_Monica_down with dissolve

    ch_monica "마을이다. 우리 둘 다 갑자기 쓰러져 버려서……"

    $renpy.pause(1.5)

    ch_monica "……뭘 그렇게 빤히 보는 거냐?"

    hide stand_Monica_down

    player "……"

    player "……귀여워."

    show stand_Monica_dere with dissolve

    ch_monica "?!?!?!?!"

    ch_monica "다…… 다짜고짜 무슨 헛소리를!!!! 아직 잠이 덜 깬……"

    hide stand_Monica_dere

    player "……메이드복……"

    show stand_Monica_dere with dissolve

    ch_monica "!!!!!"

    ch_monica "귀, 귀공, 설마…… 나와 같은 꿈을……?"

    hide stand_Monica_dere

    player "……"

    player "너 되게 귀엽더라."

    play music "audio/main/11fun.mp3"

    show bg_town with hpunch

    show stand_Monica_dere with dissolve

    ch_monica "우아아아아악~~~~!!!!!"

    ch_monica "왜!!!! 왜!!!!!!! 어떻게!!!!!"

    ch_monica "바보바보바보~~~!!!! 귀공은 바보야!!!!"

    hide stand_Monica_dere

    player "흐, 흥분하지 마……"

    player "크레페 먹으러 갈래?"

    show stand_Monica_down with dissolve

    ch_monica "어? 크레페……?"

    hide stand_Monica_down

    player "딸기에다 크림까지 올려서……"

    show stand_Monica with dissolve:
        xalign 0.5
        easeout 0.3 ypos -50
        ease 0.2 ypos 50
        easeout 0.3 ypos -50
        ease 0.2 ypos 50 
        ##팔짝 뛰는 모션
    
    ch_monica "가, 갈래 갈래……!!"

    hide stand_Monica
    show stand_Monica_dere with dissolve

    ch_monica "{b}{size=30}……가 아니라!!!! 뭐하자는 거냐!!!!{/size}{/b}"

    hide stand_Monica_dere

    player "우와, 방금 진짜……"

    player "귀여운 꼬마아이 같았어……!"

    show stand_Monica_crying with dissolve

    ch_monica "이이이!!!! 어린애 취급하지 말라고 몇 번을~~!!!!"

    hide stand_Monica_crying
    play sound "audio/sound/running.mp3"

    player "이, 이번에 잡히면 죽을지도 모른다!!"

    show stand_Monica_crying with dissolve

    ch_monica "또…… 또 도망가는 거냐!!!! 거기서!!!!"

    hide stand_Monica_crying
    stop sound
    stop music fadeout 3.0

    show bg_black with dissolve

    hide bg_town

    ch_monica "{b}{size=30}그러니까 나는!!!!!{/size}{/b}"

    show stand_Monica_dere with dissolve

    ch_monica "{b}{size=30}어린애가 아니란 말이다~~~~!!!!{/size}{/b}"

    show bg_end with fade

    $renpy.pause(1.0)

    ch_nar "Thank you for playing"

    return
## 쿠우카 해피 엔딩 ############
label kukaHappy:

    scene cg_kuka_end15 onlayer middle with fade

    $camera_move(-400, -750, 600, 0, 0.5)

    play music "audio/main/10end.mp3"

    ch_kuka "도, 도S 씨에게는…… 이래저래 신세를 많이 지게 되네요……"

    ch_kuka "오늘 누군가를 만날 거라곤 상상도 못했는데…… 이렇게 쿠우카와 함께 있어 주셔서 감사해요……"

    player "신세는 무슨……"

    player "안 그래도 만날 사람이 없어서 심심하던 참이었어. 부담 가지지 마."

    ch_kuka "그, 그렇지만……"

    ch_kuka "“이번 크리스마스에도 쿠우카는 홀몸으로 방치되는 거네요, 쿠후훗{font=NanumGothic.ttf}—{/font}”"

    ch_kuka "……하고, 지나가듯 한 마디 던졌을 뿐인데…… 정말로 만나주실 줄은……"

    $renpy.pause(1.0)

    show cg_kuka_end3 onlayer middle with dissolve
    hide cg_kuka_end15 onlayer middle

    ch_kuka "……"

    player "……쿠우카?"

    player "왜 그래……? 어디 안 좋은 데라도 있어?"

    show cg_kuka_end11 onlayer middle with dissolve
    hide cg_kuka_end3 onlayer middle

    ch_kuka "아…… 네, 넷?! 부, 부르셨나요?!"

    ch_kuka "아뇨! 아뇨! 시…… 신경 쓰실 것 없어요!"

    show cg_kuka_end15 onlayer middle with dissolve
    hide cg_kuka_end11 onlayer middle

    ch_kuka "그…… 나, 남자랑 둘이서 이런 엄청난 걸 하는 건 처음이라……"
    
    ch_kuka "쿠우카, 조금 긴장했을지도……"

    player "……그런 거였구나. 걱정했잖아."

    show cg_kuka_end7 onlayer middle with dissolve
    hide cg_kuka_end15 onlayer middle

    ch_kuka "죄, 죄송해요……"

    player "이럴 때엔…… 긴장을 푸는 데 좋은 방법을 하나 알고 있지."

    ch_kuka "……에? 긴장을 푸는 데 좋은 방법……?"

    show cg_kuka_end18 onlayer middle with dissolve
    hide cg_kuka_end7 onlayer middle

    $camera_move(0, 0, 0, 0, 0.5)

    ch_kuka "?!?!?!?!"

    player "자…… 어때?"

    ch_kuka "으, 에에?!!"

    ch_kuka "으……앗, 에에……??!!"

    ch_kuka "자, 자, 자, 잠깐, 만요……!!"

    ch_kuka "길 한복판에서 이런 부끄러운 행위를 아무렇지도 않게……!"

    ch_kuka "쿠, 쿠우카, 이대로는 도저히……!!"

    player "……쿠우카는 나랑 손 잡는 거 싫어?"

    ch_kuka "……에? 시…… 싫냐고 물으시면……"

    ch_kuka "따, 딱히 그런 건…… 아니지만…… 그게……"

    show cg_kuka_end6 onlayer middle with dissolve
    hide cg_kuka_end18 onlayer middle

    ch_kuka "……도S 씨의 손…… 너무 따뜻해서……"

    ch_kuka "나, 남자 손을 잡아 보는 건 처음이기도 하고……"

    ch_kuka "……누군가가 먼저 쿠우카의 손을 잡아 준 것도, 처음이라……"

    show cg_kuka_end10 onlayer middle with dissolve
    hide cg_kuka_end6 onlayer middle

    ch_kuka "……후에?! 하, 하, 하마터면, 넘어가 버릴 뻔했네요……!!"

    ch_kuka "여, 역시 도S 씨는…… 처음부터 이런 일을 목적으로 쿠우카를……!"

    player "그런 목적으로 만나자고 한 게 맞다면?"

    show cg_kuka_end18 onlayer middle with dissolve
    hide cg_kuka_end10 onlayer middle

    ch_kuka "………?!?!"

    ch_kuka "마, 맞……"

    player "있잖아, 나……"

    player "쿠우카의 처음을 가져가고 싶어."

    $renpy.pause(1.0)

    show cg_kuka_end16 onlayer middle with dissolve
    hide cg_kuka_end18 onlayer middle

    ch_kuka "아, 네에……? 쿠우카도 도S 씨와 처음을 보내고 싶으에엣?"
    
    show cg_kuka_end18 onlayer middle with dissolve
    hide cg_kuka_end16 onlayer middle

    ch_kuka "에? 엣?! 에?!?!"

    ch_kuka "도S 씨?! 방, 방금 뭐라고 하셨……?!"

    ch_kuka "쿠, 쿠, 쿠우카의 처음을?! 가, 가, 가, 가져가고 싶다?!! 에엣? 에?!?!"

    $renpy.pause(1.0)

    show bg_black onlayer middle with dissolve
    hide cg_kuka_end18 onlayer middle

    $renpy.pause(1.5)

    show cg_kuka_end14 onlayer middle with dissolve
    hide bg_black onlayer middle

    ch_kuka "네……? 이상한 의미가 아니라……"

    ch_kuka "쿠우카가 경험해 보지 못한 많은 일들을, 앞으로도 단둘이서 함께 하고 싶다……는 말이었다구요……?"

    show cg_kuka_end6 onlayer middle with dissolve
    hide cg_kuka_end14 onlayer middle

    ch_kuka "으으…… 쿠우카는 또 무슨 굉장한 착각을……"

    show cg_kuka_end10 onlayer middle with dissolve
    hide cg_kuka_end6 onlayer middle

    ch_kuka "그, 그런데, 그…… 그건 그것대로 엄청나게 부끄러운 말……인데요……!!"

    ch_kuka "어, 어째서 그런 말과 행동을 아무렇지도 않다는 듯이……!!!"

    show cg_kuka_end4 onlayer middle with dissolve
    hide cg_kuka_end10 onlayer middle

    ch_kuka "……그렇군요."

    ch_kuka "도S 씨는 이런 게 익숙하신가 보네요……"

    ch_kuka "뭐…… 그렇겠죠. 어디에 있든 반짝반짝 빛이 나는 도S 씨라면……"

    ch_kuka "모두에게 사랑받고, 누구에게도 미움받지 않는…… 그런, 멋진 삶을 살아왔을 테니까……"

    ch_kuka "……기분 나쁜 망상이나 하는 음침한 외톨이와는 다르게 말이에요."

    ch_kuka "하긴, 도S 씨 정도의 남자가 쿠우카 따위를 만나 준다는 것부터 눈치챘어야 했는데."

    ch_kuka "역시…… 쿠우카와의 만남은……"

    ch_kuka "……도S 씨에게는 그저, 쾌락을 탐닉하는 엔조이 정도에 불과……"

    show cg_kuka_end12 onlayer middle with hpunch
    hide cg_kuka_end4 onlayer middle

    $camera_move(-400, -750, 600, 0, 0.3)

    ch_kuka "꺅?!!"

    ch_kuka "도……S 씨?! 쿠, 쿠우카, 이상한 소리를 내 버렸……"

    player "……쿠우카."

    player "앞으로는…… 장난으로라도 그런 말은 하지 마."

    show cg_kuka_end14 onlayer middle with dissolve
    hide cg_kuka_end12 onlayer middle

    $camera_move(0, 0, 0, 0, 0.5)

    ch_kuka "……네……? 장난으로라도, 라니……"

    ch_kuka "그치만, 도S 씨는 진심이……"

    player "……"

    show cg_kuka_end10 onlayer middle with dissolve
    hide cg_kuka_end14 onlayer middle

    ch_kuka "……!"

    ch_kuka "……지,"

    ch_kuka "진……심……이라는…… 건가요……?"

    show cg_kuka_end6 onlayer middle with dissolve
    hide cg_kuka_end10 onlayer middle

    ch_kuka "아…… 안 되는데……"

    ch_kuka "쿠, 쿠우카는 이런 상황에 면역이 없어서……"

    ch_kuka "그런 말을, 들어 버리면……"

    ch_kuka "어, 어떻게 반응해야 할지, 잘 모르……"

    player "……지금,"

    player "무슨 생각 하고 있어?"

    show cg_kuka_end10 onlayer middle with dissolve
    hide cg_kuka_end6 onlayer middle

    ch_kuka "에……?"

    player "지금 당장, 쿠우카의 솔직한 감정을……"

    player "있는 그대로…… 숨김없이 말해 줘."

    ch_kuka "솔……직한 감정을…… 말해달라구요?"

    ch_kuka "이…… 이렇게나 남부끄러운 행위를 쿠우카에게 강요하시다니, 도S 씨의 가학성은 과연 보통이 아니네요……"

    show cg_kuka_end6 onlayer middle with dissolve
    hide cg_kuka_end10 onlayer middle

    ch_kuka "……"

    ch_kuka "있는 그대로, 인가요……"

    $renpy.pause(1.0)

    show cg_kuka_end10 onlayer middle with dissolve
    hide cg_kuka_end6 onlayer middle

    ch_kuka "……도S 씨의 손……"

    ch_kuka "따뜻, 하니까……"

    ch_kuka "……언제까지고, 놓지 말아 주세요…… 그냥 이대로……"

    ch_kuka "쿠우카의 처음을…… 앞으로도 쿠우카와…… 함께해 주세요."

    $renpy.pause(1.0)

    show cg_kuka_end18 onlayer middle with hpunch
    hide cg_kuka_end10 onlayer middle

    ch_kuka "마…… 말해 버렸어어어~~~?!!?!"

    ch_kuka "쿠, 쿠, 쿠우카, 방금 대체 무슨 짓을!!!!!!"

    ch_kuka "쳐…… 쳐다보지 말아 주세요!!!!"

    ch_kuka "지, 지금 분명 엄청난 얼굴을 하고 있…… 아우우……"

    show cg_kuka_end6 onlayer middle with dissolve
    hide cg_kuka_end18 onlayer middle

    ch_kuka "……"

    ch_kuka "……도S 씨."

    player "응."

    ch_kuka "……정말, 쿠우카로 괜찮으신가요……?"

    player "괜찮아."

    ch_kuka "남의 시선은 신경도 쓰지 않고, 시도 때도 없이 기분 나쁜 망상을 밥먹듯 내뱉는…… 이런 저라도요……?"

    player "상관없어."

    ch_kuka "쿠우카와 함께 다니는 건…… 도S 씨에게도 부끄러운 일일 텐데요……"

    player "전혀."

    ch_kuka "……이상해요."

    ch_kuka "아무리 생각해도…… 도S 씨가 쿠우카 따위를 만날 이유가 없는데……"

    player "……너를 좋아하는 데 이유가 필요해?"

    ch_kuka "……"

    ch_kuka "……몇 명으로 할까요?"

    player "응……?"

    show cg_kuka_end19 onlayer middle with dissolve
    hide cg_kuka_end6 onlayer middle
    show highlight onlayer forward

    $camera_move(-1200, -1200, 800, 0, 0.3)

    play music "audio/main/11fun.mp3"

    ch_kuka "{b}{size=30}아…… 아이는 몇 명으로 할까요??!?!{/size}{/b}"

    hide highlight onlayer forward

    player "?!?!"

    ch_kuka "크히히히히!!! 꾸…… 꿈에 그리던 도S 씨와…… 정식으로 교제……!!!!"

    ch_kuka "{b}{size=30}이건 즉…… 엉망진창 해 버려도 합법이라는 거네요!!!!!{/size}{/b}"

    ch_kuka "무…… 무려 SM 커플이라니!!!!! 이, 이제 우리 사이를 막을 수 있는 건 아무것도 없어요!!!!!"

    player "쿠, 쿠우카……?! 조금만 진정……"

    ch_kuka "시, 심한 짓…… 심한 짓을…… 케헤헤……!! 전보다 훨씬 더 과감하게 즐길 수 있어요!!!"

    ch_kuka "여…… 여자친구니까!!!! 이 정도는 요구할 수 있는 거죠?!?! 네?!?!?!"

    ch_kuka "도S 씨!!! 하아, 하앗…… 쿠…… 쿠우카를……!!!"

    show cg_kuka_end19 onlayer middle with hpunch
    show highlight onlayer forward

    ch_kuka "{b}{size=30}쿠우카를…… 질펀한 연인의 방식으로!!!! 사랑을 담아 괴롭혀 주세요오오!!!! 쿠헤헤헤헤헷!!!!{/size}{/b}"

    hide highlight onlayer forward
    show bg_black onlayer forward with dissolve

    player "저, 저리 가아아아~~~!!!!!"

    $camera_move(0, 0, 0, 0, 0)
    hide cg_kuka_end19 onlayer middle
    hide bg_black onlayer forward

    $renpy.pause(2.0)
    play sound "audio/sound/amesopen.mp3"
    show ames_reverse
    $renpy.pause(4.0)
    
    stop music fadeout 3.0
    ## 아메스 ####################################
    play music "audio/main/ames.mp3" fadein 3.0
    show cg_ames with dissolve
    hide ames_reverse

    hatena "자, 수고했어."

    hatena "……그러니까 내 말은, 정말로 수고했다고."

    hatena "뭔가…… 엄청나게 혼란스러웠네. 무슨 일이 있었는지 기억하기 힘들 정도야."

    hatena "뭐, 그런 정신없는 언행이 쿠우카의 매력이긴 하지."

    hatena "때와 장소를 가리지 않고 물흐르듯 망상하는 능력…… 저것도 일종의 재능일지도."

    hatena "……너무 거리낌이 없어서 이따금씩 곤란한 상황에 처할 때도 있지만."

    hatena "그래도, 나름 귀엽다고 생각하지 않아?"

    hatena "하긴…… 그러니까 당신도 그녀를 좋아하는 거겠지♪"

    hatena "그나저나 쿠우카도 제법인걸. 설마 그 자리에서 바로 고백을 할 줄이야……"

    hatena "전혀 예상 못했다구. 보고 있는 나까지 두근두근했어♪"

    hatena "아무튼, 기정사실을 만들어 버렸으니…… 제대로 그녀를 책임져야 해?"

    hatena "그녀를 감당할 수 있는 건 오직 당신뿐이니까."

    hatena "뭐…… 애초에 당신의 앞이 아니라면, 언제 그랬냐는 듯 얌전한 아이가 되지만……"

    hatena "쿠우카만의 애정 표현 방식인 걸까……? 그렇게 생각하니 깜찍한걸."

    hatena "……SM 커플이라……"

    hatena "아! 아무것도 아니야! 신경 쓰지 마, 신경 쓰지 마~!"

    hatena "……시간이 벌써 이렇게 됐네! 그럼 또 봐!"

    play sound "audio/sound/amesclose.mp3"
    show ames_swift
    hide cg_ames
    stop music fadeout 3.0

    $renpy.pause(3.0)
    ## 랜드솔 마을
    play music "audio/main/3town.mp3" fadein 3.0
    show bg_town with fade

    show stand_Kuka_shamed with dissolve

    ch_kuka "……"

    hide stand_Kuka_shamed

    player "……으음……"

    show stand_Kuka_shamed with dissolve

    ch_kuka "……도S 씨? 깨어나신 건가요……?"

    hide stand_Kuka_shamed

    player "으응…… 여기가 어디야……?"

    show stand_Kuka_shamed with dissolve

    ch_kuka "마, 마을 안이에요…… 길 한복판에서 갑자기 정신을 잃어서 그만……"

    hide stand_Kuka_shamed

    player "아, 그랬던가……"

    player "……쿠우카, 혹시……"

    player "이상한 꿈…… 같은 거, 꾸지 않았어?"

    show stand_Kuka_shamed with dissolve

    ch_kuka "……!!!"

    ch_kuka "꾸…… 꿈 말인가요?"

    ch_kuka "그, 글쎄요…… 저는 잘……"

    ch_kuka "아, 그, 깨…… 깨어나신 걸 확인했으니까, 쿠우카는 이만 가 볼게요……!!"

    hide stand_Kuka_shamed

    player "어? 으응……"

    ch_nar "급한 일이라도 있나……? 왜 저리 서두르지……"

    play music "audio/main/11fun.mp3"

    ch_kuka "……크히히……"

    ch_kuka "SM 커플…… 케케케켓……!!"

    player "뭐, 뭐?!"

    player "야…… 야!!! 너 나랑 같은 꿈 꾼 거지!!!"

    player "거…… 거기 서!!!! 얘기 좀 하자고!!!! 쿠우카~~~~!!!!!!"

    ch_kuka "그흐흐…… 크헤헤헷……!!!"

    stop music fadeout 3.0

    show bg_black

    hide bg_town

    $renpy.pause(2.0)

    show stand_Kuka_mousou with dissolve

    ch_kuka "쿠후후훗……!!!"

    show bg_end with dissolve

    $renpy.pause(1.0)

    ch_nar "Thank you for playing"

    return
## 유키 해피 엔딩 ##############
label yukiHappy:
    play music "audio/main/11fun.mp3"
    scene cg_yukiend1 onlayer middle with dissolve

    $camera_move(2500, 1500, 750, 0, 0.5)

    $renpy.pause(1.5)

    $camera_move(-2500, -1500, 750, 0, 2)

    $renpy.pause(3.0)

    $camera_move(0, 0, 0, 0, 0.4)

    ch_yuki "[name], 이거 봐!"

    ch_yuki "나 어때? 귀여워~?"

    ch_nar "…………"

    ch_nar "귀엽다……"

    ch_nar "너무 귀엽다."

    ch_nar "어떻게 이렇게 귀여운 생물이 존재할 수 있지?"

    ch_nar "아니, 귀엽다기보다 아름답다는 말이 더 어울릴까……?"

    ch_nar "귀엽…… 아름답……?"

    ch_nar "귀여…… 아르……"

    player "르므엑……"

    ch_nar "시각에 너무 강한 자극이 들어와서일까……"

    ch_nar "어휘 체계가 고장난 것 같다. 마땅한 표현이 떠오르지 않는다."

    ch_nar "……아니, 고장난 건 내가 아니다."

    ch_nar "인간의 언어로 표현할 수 있는 방식에는 명확한 한계가 있다."

    ch_nar "말로 형용할 수 없는 아름다움이란 얼마든지 존재한다."

    ch_nar "이를테면, 지금 내 눈 앞에 피어 있는 {b}꽃이라거나{/b}……"

    ch_nar "……‘꽃’이다, ‘꽃’."

    ch_nar "발음할 때 각별히 주의해야 한다. 잘못 발음하면 재앙이 일어난다."

    ch_yuki "저기~ [name], 내 말 듣고 있어?"

    ch_yuki "이 옷 어떠냐구~ 나랑 잘 어울려?"

    player "아…… 억……? 으응……"

    show cg_yukiend2 onlayer middle with dissolve
    hide cg_yukiend1 onlayer middle

    ch_yuki "……응응, 물어볼 필요도 없었네."

    player "응…… 으에……?"

    ch_yuki "부끄러워하긴♪"

    ch_yuki "숨기려고 해도 얼굴에 다 드러난다니까."

    ch_yuki "후훗…… 바보 같아~"

    player "우…… 우응……"

    show cg_yukiend1 onlayer middle with dissolve
    hide cg_yukiend2 onlayer middle

    ch_yuki "그래서, 감상은?"

    player "응……?"

    ch_yuki "정신을 쏙 빼놓을 정도로 예쁘다는 건 나도 알지만 말야~"

    ch_yuki "그래도, 네가 직접 말해 주는 걸 듣고 싶어."

    ch_yuki "나…… 예뻐?"

    player "……"

    player "……진짜 예뻐."

    player "인형 같아……"

    ch_yuki "에이, 설마~"

    ch_yuki "나만큼 예쁜 인형이 어디 있어?"

    player "헤헤……"

    show cg_yukiend2 onlayer middle with dissolve
    hide cg_yukiend1 onlayer middle

    ch_yuki "아하핫! 표정 너무 웃겨~"

    show cg_yukiend1 onlayer middle with dissolve
    hide cg_yukiend2 onlayer middle

    ch_yuki "……그 얼굴, 나 말고 다른 사람한테 보여 주면 안 된다?"

    player "그…… 그렇게 한심해 보여……?"

    ch_yuki "응. 지~~~인짜 바보 같아."

    player "힝……"

    ch_yuki "그러니까, 나만 볼 거야."

    player "……응?"

    ch_yuki "어쩔 줄 몰라 하는 귀여운 표정도,"

    ch_yuki "바보 같은 얼굴도……"

    ch_yuki "전부, 나만 볼 거니까."

    show cg_yukiend2 onlayer middle with dissolve
    hide cg_yukiend1 onlayer middle

    ch_yuki "알았지? 약속한 거다♪"

    player "……그럼,"

    player "너도 약속해 줘."

    ch_yuki "우웅~?"

    player "천진난만하게 미소 짓는 귀여운 얼굴도,"

    player "가슴이 두근거릴 정도로 청순하고 예쁜 모습도……"

    player "남들에게 보여주고 싶지 않아. 너를 독점하고 싶어……"

    player "그러니까……"

    show cg_yukiend1 onlayer middle with dissolve
    hide cg_yukiend2 onlayer middle

    $camera_move(-2500, -1500, 750, 0, 0.5)
    ch_yuki "……쉬잇♪"

    ch_yuki "그 다음 말은…… 조금 뒤에 해 줄래?"

    player "어……?"

    ch_yuki "오늘 우리 집에…… 부모님 안 계시는데……♥"

    ch_yuki "{color=#FF2929}넷X릭스{/color}…… 보고 갈래?"

    show cg_yukiend1 onlayer middle with hpunch

    player "{b}{size=30}갈 래 !!!!!!!!!!!!{/size}{/b}"

    player "{b}{size=30}자고 가도 될까요!!!!{/size}{/b}"

    ch_yuki "뭐어~? 네가 내 남친이라도 돼?"

    player "어……? 그게……"

    ch_yuki "남자친구 아니잖아?"

    show cg_yukiend2 onlayer middle with dissolve

    

    ch_yuki "{b}아. 직. 은~{/b}"

    show bg_black onlayer middle with dissolve

    $camera_move(0, 0, 0, 0, 0)

    hide cg_yukiend1 onlayer middle
    hide cg_yukiend2 onlayer middle

    player "{b}{size=30}우…… 우오오오오옷!!!!!{/size}{/b}"

    player "{b}{size=30}빠, 빨리 가자!!!! 너희 집!!!!!!{/size}{/b}"

    ch_yuki "우웅…… 나 배고픈데."

    player "{b}{size=30}전부 다 사 줄게!!!!! 뭐 먹고 싶어!!!!!!{/size}{/b}"

    ch_yuki "음…… 파스타 먹고 싶어~"

    player "{b}{size=30}가자!!!!!! 내가 길을 알아!!!!!!!{/size}{/b}"

    hide bg_black onlayer middle
    stop music
    play sound "audio/sound/amesopen.mp3"
    show ames_reverse
    $renpy.pause(4.0)
    
    ## 아메스 ####################################
    play music "audio/main/ames.mp3" fadein 3.0
    show cg_ames with dissolve
    hide ames_reverse

    hatena "자, 수고했어."

    hatena "뭔가…… 되게 필사적이네, 당신……"

    hatena "그렇게나 유키를 좋아하는 거야?"

    hatena "하긴…… 유키 정도로 예쁘고 귀여운 아이라면, 사랑에 빠지지 않는 게 더 이상하지♪"

    hatena "이렇게 귀여운 아이가 남자라니, 믿기 힘들 정도야~"

    hatena "뭐……? 남자아이라서 귀여운 거라고?"

    hatena "그렇구나…… 응원할게……"

    hatena "음…… 근데 말야."

    hatena "남자애가 같은 남자애를 집에 들이는 건……"

    hatena "부모님이 집에 계셔도…… 딱히 상관 없는 거 아니야?"

    $renpy.pause(1.0)

    hatena "앗…… 미안해! 너무 섬세하지 못한 질문이었나? 못 들은 걸로 해 줘~"

    hatena "……응? 아직 마지막 말을 전하지 못했다고……?"

    hatena "네네~ 지금 바로 돌려보내 줄 테니, 직접 말하라구."

    hatena "그럼, 또 봐~"

    stop music fadeout 3.0
    play sound "audio/sound/amesclose.mp3"
    show ames_swift
    hide cg_ames

    $renpy.pause(3.0)

    play music "audio/main/3town.mp3"
    show bg_town with fade
    hide ames_swift

    player "……"

    player "으음……"

    show stand_Yuki_ddung with dissolve

    ch_yuki "으응…… 일어났어……?"

    player "여기가 어디……?"

    ch_yuki "마을이야. 너랑 나, 갑자기 정신을 잃어서……"

    show stand_Yuki_proud
    hide stand_Yuki_ddung

    ch_yuki "……그나저나, 나는 꿈속에서조차 엄청 귀엽구나~♪"

    player "……"

    player "……꿈?"

    show stand_Yuki
    hide stand_Yuki_proud

    ch_yuki "앗, 그러고 보니 너도 꿈에 나왔었어!"

    ch_yuki "너무나도 귀여운 내 모습에 정신을 못 차리고……"

    player "……"

    show stand_Yuki_ddung
    hide stand_Yuki

    ch_yuki "……?"

    ch_yuki "너 왜 눈을 그렇게 떠……?"

    player "…………"

    ch_yuki "……설마, 너……"

    show stand_Yuki_shamed
    hide stand_Yuki_ddung

    ch_yuki "나랑…… 똑같은 꿈을 꾼 거야?!"

    player "그, 그게……"

    show stand_Yuki_proud
    hide stand_Yuki_shamed

    ch_yuki "……흐흥♪"

    ch_yuki "나한테 뭔가 할 말 있지 않아?"

    player "어……?"

    ch_yuki "뭐였더라……"

    ch_yuki "‘{b}너를 독점하고 싶어{/b}’……?"

    player "으…… 으아아악!!!!"

    ch_yuki "그런 쑥스러운 말을 아무렇지 않게 하다니…… 꺄아~ 남자다워!"

    ch_nar "니…… 니가 남자답다고 하니까 기분이 이상해……!!"

    show stand_Yuki
    hide stand_Yuki_proud

    ch_yuki "그래서?"

    player "응……?"

    ch_yuki "그때 못다 한 말……"

    ch_yuki "지금이라면 들어줄 수 있는걸?"

    player "아……"

    ch_yuki "……아핫, 밖에서 말하긴 부끄러운 거야~?"

    show stand_Yuki_shamed
    hide stand_Yuki

    ch_yuki "얼마나 사랑스러운 말을 해 주려고……! 너무너무 기대된다♪"

    player "으아악…… 그게 아니라……"

    $renpy.pause(1.0)

    show stand_Yuki
    hide stand_Yuki_shamed

    play music "audio/main/8sad.mp3"

    ch_yuki "……먼저 말해 주지 않는다면,"

    ch_yuki "내가 먼저 말해 버릴 거야."

    player "……네?"

    ch_yuki "손…… 잡아 줄래?"

    player "아, 응……"

    ch_yuki "……있잖아, 예전에 내가 했던 말……"

    ch_yuki "아직 기억하고 있어?"

    player "무슨 말……?"

    ch_yuki "“어떤 보석보다도 가치 있는 나를……”"

    ch_yuki "“언젠간 너에게 선물할게.”"

    ch_yuki "……마음의 준비는…… 됐으려나?"

    ch_yuki "세상 무엇보다 소중한, 아름답고 귀여운 나를……"

    ch_yuki "선물 받을 준비…… 말이야♪"

    player "그……"

    player "그래도…… 될까?"

    ch_yuki "후훗♪"

    ch_yuki "나…… 오직 너만을 위해,"

    ch_yuki "앞으로도 더욱 예뻐질 테니까……♪"

    ch_yuki "이 손…… 언제까지고 놓으면 안 된다?"

    player "그……"

    player "자, 잘 부탁드립니다……"

    show stand_Yuki_shamed
    hide stand_Yuki

    ch_yuki "저기, 있지……"

    hide stand_Yuki_shamed

    stop music fadeout 3.0
    show bg_black with dissolve
    hide bg_town

    ch_yuki "츄~ 해줘……♥"

    $renpy.pause(1.0)

    show stand_Yuki with dissolve

    ch_yuki "헤롱헤롱 해져라~♪"

    show bg_end with fade

    $renpy.pause(1.0)

    ch_nar "Thank you for playing"

    return
## 진엔딩 #######################
label Success:
    play music "audio/main/11fun.mp3"
    scene cg_common2 onlayer middle with fade

    $camera_move(-3000, -1900, 1000, 0, 0.5)

    ch_yuki "[name]~ 이쪽 봐봐."

    ch_yuki "자…… 아앙~♥"

    ch_yuki "후훗…… 잘 먹네."

    ch_yuki "나처럼 귀여운 애가 상냥하게 떠먹여 주는 거, 로망이었지?"

    ch_yuki "어때? 두근두근했어?"

    ch_yuki "자극이 좀 강했으려나~♪"

    $camera_move(-3500, -1000, 800, 0, 0.5)

    ch_ninon "으그극…… 쇼군을 보필하는 신하는 니논 하나로 충분해 입니다, 유키 씨!!"

    $renpy.pause(1.5)

    ch_ninon "……과연, 이해했다 입니다."

    ch_ninon "{color=#FF2929}여자력{/color}으로 승부하자는 것이었습니까!!!"

    ch_ninon "질까 보냐 입니다!! 자자, 쇼군~ 아앙~♥ 입니다~!"

    $camera_move(1500, -1800, 800, 0, 0.5)

    ch_monica "그대들, 활발한 건 좋지만 공공장소에서 너무 시끄럽게 하지는 말……"

    show cg_common onlayer middle with dissolve
    hide cg_common2 onlayer middle

    ch_monica "엣? 어?!"

    ch_monica "자, 잠깐, 니논!!"

    ch_monica "그, 그 초콜릿은 맨 마지막에 먹으려고 아껴놨던 거란 말이다!!!"

    ch_monica "으아앙, 귀공~~!!! 다시 뱉어 내!!! 흐에에엥~~"

    $camera_move(1500, 1000, 450, 0, 0.5)

    ch_kuka "아……아이스크림이 질척질척하게…… 와플과 몸을 섞고 있어요……!!"

    ch_kuka "주변의 시선에도 아랑곳 않고 이렇게나 끈적한 합일이라니…… 와플 군……!! 도대체 얼마나 뜨겁고 격렬한 테크닉을 가지고 있는 건가요!!! 크힛…… 쿠헤헤헷……"

    $camera_move(0, 0, 0, 0, 0)

    ch_ayumi "우우…… 머…… 먼발치에서 바라만 보던 선배와 합석이라니……"

    ch_ayumi "시, 심호흡……! 진정하자, 진정하자……"

    ch_ayumi "지, 진정…… 진정할 수 있을리가 없잖아요오오……!! 아와와와……"

    ch_ayumi "……어? 내 자리…… 거기 제 자리인데……"

    ch_yuki "나를 봐~ 내가 더 귀엽지?"

    ch_ninon "니, 니논도 KAWAII 합니다!! 봐 주세요 입니다~!! 「인법 {font=NanumGothic.ttf}·{/font} 흥 니논 삐져쪄」 !!"

    ch_monica "으에엥~ 내 쪼꼬렛~~!!"

    ch_kuka "쿠후훗…… 케헤헤헤헷……"

    ch_ayumi "저기…… 제 자리……"

    show bg_black with dissolve
    hide cg_common onlayer middle

    stop music 

    $renpy.pause(2.0)

    show bg_town with fade
    hide bg_black

    play music "audio/main/11fun.mp3"

    show stand_Ninon_embarassed with dissolve

    ch_ninon "푸하~~~~아앗~~~!!! 입니다."

    hide stand_Ninon_embarassed
    show stand_Monica_surprised with dissolve

    ch_monica "바…… 방금, 무슨 일이……?!"

    hide stand_Monica_surprised

    ch_ayumi "제 자리인데!! 비켜 주……!! 에? 꿈……이었나요?"

    show stand_Kuka_mousou with dissolve

    ch_kuka "끄…… 끈적한 와플!!!!"

    hide stand_Kuka_mousou
    show stand_Yuki_proud with dissolve

    ch_yuki "어쩜…… 나는 꿈속에서조차 귀엽네~♪"

    hide stand_Yuki_proud

    player "뭐야……?"

    player "방금…… 모두 같은 꿈을 꾼 거야?"

    show stand_Ninon_embarassed with dissolve

    ch_ninon "쇼, 쇼군도 입니까?! 그렇다면……"

    show stand_Ninon_innocence
    hide stand_Ninon_embarassed

    ch_ninon "이이익…… 유키 씨!! 승부는 아직 끝나지 않았소 입니다!!!"

    hide stand_Ninon_innocence
    show stand_Yuki_proud with dissolve

    ch_yuki "어머~ 귀여움 대결을 말하는 거야? 몇 번을 해도 결과는 똑같을걸~?"

    hide stand_Yuki_proud
    show stand_Ninon_innocence with dissolve

    ch_ninon "멋대로 결과를 내지 마라 입니다~~~!!!"

    hide stand_Ninon_innocence

    player "어떻게 동시에 같은 꿈을……"

    player "꿈이 아니었나……?"

    show stand_Monica_ddung with dissolve

    ch_monica "……귀공."

    ch_monica "이래도 부정할 테냐?"

    hide stand_Monica_ddung

    player "……뭘?"

    show stand_Monica with dissolve

    ch_monica "귀공과 우리의……"

    ch_monica "{b}인연{/b}을 말이다."

    hide stand_Monica

    player "뭐……?"

    play music "audio/main/8sad.mp3"

    show stand_Monica with dissolve

    ch_monica "귀공. 분명히…… 우리의 곁을 떠나려고 했었지?"

    ch_monica "방금 벌어진 일이 무슨 조화였는지는 나도 잘 모른다. 헌데……"

    ch_monica "이런 일을 겪고도…… 귀공과 맺어진 우리의 인연을, 부정할 셈이냐?"

    hide stand_Monica
    show stand_Ninon with dissolve

    ch_ninon "맞아요 입니다~!! 쇼군과 이어진 붉은 실은 절대 끊어지지 않는다 입니다!!"

    hide stand_Ninon

    player "너희와 같이 있을 이유가 없잖아……"

    player "나…… 민폐덩어리인걸. 할 줄 아는 것도 없고……"

    player "무엇보다…… 너희 길드 소속도 아니고."

    show stand_Monica with dissolve

    ch_monica "……"

    ch_monica "나, 모니카 바이스빈트가……"

    ch_monica "‘바이스플뤼겔 랜드솔지부’를 대표하여, 귀공에게 제안한다."

    player "뭐……?"

    ch_monica "우리의……"

    ch_monica "‘동료’가 되어 다오."

    hide stand_Monica
    show stand_Ninon_wink with dissolve

    ch_ninon "오오~ 씹덕 같고 좋습니다~~!!"

    hide stand_Ninon_wink

    show stand_Monica with dissolve

    ch_monica "이 결정에 이의 있는 사람은 없을 테지?"

    hide stand_Monica

    player "……"

    player "나 같은 게 뭐라고…… 이렇게까지 해 주는 거야."

    show stand_Monica with dissolve

    ch_monica "……공통점이라고는 찾아보기 힘든 우리가 결속할 수 있었던 것."

    ch_monica "순백의 날개를 펼쳐, 천공을 높이 비상할 수 있었던 것……"

    ch_monica "전부…… 귀공의 덕분이다."

    ch_monica "그러니까…… 앞으로도 잘 부탁한다, 귀공."

    hide stand_Monica
    show stand_Ninon_wink with dissolve

    ch_ninon "잘 부탁드린다 입니다, 쇼군~!!"

    hide stand_Ninon_wink

    ch_ayumi "언제까지고 열심히 선배를 관찰할 테니까요…… 잘 부탁합니돠앗!! 우윽……"

    show stand_Kuka with dissolve

    ch_kuka "아, 앞으로도 많이 많이 괴롭혀 주세요……!!"

    hide stand_Kuka
    show stand_Yuki with dissolve

    ch_yuki "네가 곁에 있다면, 더욱 귀여워지도록 힘낼 테니까…… 기대하라구~"

    hide stand_Yuki

    player "……"

    player "……나도……"

    player "잘 부탁해."

    show bg_black with dissolve
    hide bg_town

    stop music

    $renpy.pause(1.0)

    ch_oedo "오오, 이보게들!! 이리 와서 이것 좀 보게!!"

    ch_oedo "쇼군님 일행으로부터 편지가 왔어!!!"

    ch_oedo2 "뭐?! 쇼군이라고?!! 어디 어디!!! 같이 좀 봅세!!!"

    $renpy.pause(1.5)

    ch_nar "아유미 입니다!"

    ch_nar "설마 누구냐고 묻지는 않으시겠죠……?"

    ch_nar "선배와 모두의 활약으로 마물을 쓰러뜨린지도 꽤 오랜 시간이 지났네요!"

    ch_nar "오에도 마을에서는 참 많은 일들을 경험한 것 같아요."

    ch_nar "즐거운 일들도 있었지만, 그만큼 두렵고 위험한 일들도 많았죠……"

    ch_nar "하지만 그런 경험들을 발판 삼아, 한층 더 성장할 수 있었던 것 같아요!"

    ch_nar "지금 이 편지를 쓰는 이유도 그것 때문이에요! 사실은 저희……"

    ch_nar "랜드솔 마을을 위협하던, 아주 무서운 마물을 해치웠거든요……!"

    ch_nar "예전이었다면 승리를 장담하지 못 했을 텐데, 오에도에서 경험한 일들이 저희들의 결속력을 강하게 만든 것 같아요!"

    ch_nar "자랑하려고 편지를 보낸 거냐구요? 헤헤……"

    ch_nar "기회가 된다면, 모두와 함께 온천에 또 가고 싶어요. 마을 분들도 보고 싶구요!"

    ch_nar "추신 : 아! 모니카 씨 말인데요…… 온천의 화과자를 엄청 그리워 하시더라고요."

    ch_nar "“그…… 달콤한 과자들을 다시 한 번 먹을 수만 있다면……!” 하고, 입버릇처럼 말씀하신답니다."

    ch_nar "그러니까…… 에또…… 조만간 찾아뵐 수 있을 것 같기도 해요!"

    ch_nar "그럼 오에도 여러분, 그리고 구라노스케 씨!"

    ch_nar "다시 만날 때까지 건강하세요!"

    $renpy.pause(1.5)

    ch_oedo3 "……근데 말여."

    ch_oedo4 "잉?"

    ch_oedo3 "……우리 마을에 온천이 있었남……?"

    $renpy.pause(1.5)

    play sound "audio/sound/surp.mp3"

    $camera_move(0, 0, 400, 0, 0)
    show stand_gura onlayer middle with dissolve:
        xalign 0.5 yalign 0.5

    $renpy.pause(2.0)
    hide stand_gura onlayer middle
    $camera_move(0, 0, 0, 0, 0)
    show bg_end with fade

    $renpy.pause(1.0)
    ch_nar "Thank you for playing"

    return
## 히든 엔딩 #####################
label end_kokoro:
    scene bg_black
    stop music
    ## 검은 배경
    $renpy.pause(1.0)

    hatena "……인님."

    hatena "주인님……"

    show cg_kokoro_02 with fade

    play music "audio/main/8sad.mp3"

    ch_kokoro "주인님……!"

    ch_kokoro "정신이 드십니까……?!"

    player "……"

    player "……마망?"

    show cg_kokoro_01 with dissolve
    hide cg_kokoro_02

    ch_kokoro "아아, 다행이다……"

    ch_kokoro "저, 저는…… 주인님이, 어딘가 먼 곳으로 떠나 버리시는 줄만 알고……"

    player "콧코로……?"

    player "내가 맨날 말썽 부리고, 속만 썩여서……"

    player "못 버티고 도망가 버린 게…… 아니었어……?"

    show cg_kokoro_02 with dissolve
    hide cg_kokoro_01

    ch_kokoro "……!"

    ch_kokoro "……주인님, 설마…… 그렇게 생각하고 계실 줄은……"

    ch_kokoro "저는 단지…… 주인님이 조금이라도 더 행복하게 지내시길 바라는 마음에……"

    $renpy.pause(1.0)

    ch_kokoro "……저의 불찰입니다."

    ch_kokoro "가이드 역으로서, 단 한순간이라도 주인님의 곁을 비워서는 안 되었는데……"

    ch_kokoro "제가 잠시 어떻게 됐었나 봅니다…… 주인님을 며칠씩이나 방치하다니……"

    ch_kokoro "앞으로는…… 절대 주인님을 혼자 두지 않겠습니다."

    ch_kokoro "그러니 다시는…… 다시는 콧코로의 곁을 떠나지 말아주십시오."

    ch_kokoro "주인님은 저의 모든 것. 주인님이 없으면 저는……"

    $renpy.pause(1.0)

    ch_kokoro "……주인님, 부디…… 콧코로를 미워하지 말아주세요……"

    player "무슨 소리야……"

    player "내가 콧코로를 미워할 리가 없잖아……"
    show cg_kokoro_01 with dissolve
    hide cg_kokoro_02

    ch_kokoro "아아, 주인님……"

    ch_kokoro "어찌 이리도 상냥하신지……"

    ch_kokoro "역시, 주인님의 곁에는……"

    stop music

    show cg_kokoro_04 with dissolve
    hide cg_kokoro_01

    ch_kokoro "{size=30}{b}{cps=*3}아무도 없{/cps}어야{cps=*3}만 합니{/cps}다.{/b}{/size}"

    $renpy.pause(1.0)

    player "뭐……?"

    ch_kokoro "해로운 것으로부터 주인님을 안전하게 지키는 일이야말로…… 제가 태어난 이유이자, 저의 사명."

    ch_kokoro "주인님…… 콧코로가 자리를 비운 사이, 온갖 추악하고 더러운 것들을 보고 들으셨을 테지요."

    ch_kokoro "언제나 상대방을 먼저 배려하는 따뜻한 마음씨…… 부탁을 거절하지 못하는 상냥함."

    ch_kokoro "어느 누가 그런 주인님을 사랑하지 않을 수 있을까요……?"

    ch_kokoro "본분을 지키지 못한 저의 오판 때문에, 주인님께서 얼마나 고통스러우셨을지…… 저는 감히 상상조차 할 수 없습니다."

    player "콧코로……?"

    ch_kokoro "괜찮습니다, 주인님…… 안심하십시오."

    ch_kokoro "이제부터는, 어느 누구도 주인님께 접근하지 못하게 할 테니까요."

    ## 상하좌우로 불규칙하게 흔들리는 효과


    play music "audio/sound/heart.wav"

    ch_kokoro "그 누구도……"

    ch_kokoro "그 누구도 저와 주인님을 떨어뜨려 놓을 수 없습니다."

    ch_kokoro "설령 그것이, 아메스 님이라 할지라도……"

    player "코, 콧코로……!"

    $renpy.pause(1.0)

    show cg_kokoro_03 with dissolve
    hide cg_kokoro_04

    ch_kokoro "오야……?"

    ch_kokoro "주인님, 겁먹으신 걸까요……?"

    ch_kokoro "귀여워라…… 후후, 마치 어린아이 같습니다……♪"

    ch_kokoro "착하지…… 착하지……♪"

    ch_kokoro "주인님은…… 착한 아이……♪"

    ch_kokoro "착한 아이는…… 엄마 말을 잘 듣는답니다……♪"

    player "콧……코로, 무, 무서우니까…… 이제 그만……"

    ch_kokoro "쉬~잇……♪"

    ch_kokoro "주인님은 그저 가만히……"

    ch_kokoro "착한 아이로, 있어 주시면 됩니다……♪"

    ch_kokoro "언제까지고 콧코로가,"

    ch_kokoro "주인님의 모든 것을 준비하고, 관리해 드릴 테니까요."

    show bg_black with fade
    hide cg_kokoro_03


    stop music

    $renpy.pause(1.0)

    ch_kokoro "콧코로가,"

    ch_kokoro "주인님을,"

    ch_kokoro "영원히,"

    ch_kokoro "지켜드릴 테니까요."

    ch_kokoro "영원히……"

    $renpy.pause(1.0)
    play sound "audio/sound/surp.mp3"

    show cg_kokoro with dissolve
    hide bg_black

    ch_kokoro "영 원 히 ."

    hide cg_kokoro

    $renpy.pause(1.0)

    show bg_badend with dissolve

    $renpy.pause(1.0)

    ch_nar "{color=#FF2929}DEAD END{/color}"
    return
## 캬루 엔딩 #####################
label Badkyaru:

    scene bg_black

    play sound "audio/sound/hit.wav"

    $renpy.pause(2.0)

    ch_nar "……어……?"

    ch_nar "모, 모두들……"

    ch_nar "왜…… 바닥에 쓰러져 있는 거야……?"

    ch_nar "어, 어째서……"

    $renpy.pause(1.0)

    show cg_kyaru with fade

    play sound "audio/sound/surp.mp3"

    player "캬루!!!!!! 어째서!!!!!!"

    ch_kyaru "……"

    ch_kyaru "{b}난 언제나 강한 자의 편이다.{/b}"

    ch_kyaru "그보다…… 명이 질기구나!"

    show cg_kyaru with hpunch

    ch_kyaru "{b}이만 죽어라!!! 그림 버스트!!!!!{/b}"

    show bg_black with dissolve

    play sound "audio/sound/fire.mp3"

    player "{b}크아아아아악!!!!!!! 3545!!!!!!!!!!!!{/b}"

    show bg_badend with fade

    $renpy.pause(1.0)

    ch_nar "{color=#FF2929}DEAD END{/color}"

    return
## 키무라 엔딩 ####################
label Kimura:

    scene bg_black

    play music "audio/sound/fire.mp3"

    play sound "audio/sound/hit.wav"

    $renpy.pause(2.0)

    ch_nar "……어……?"

    ch_nar "모, 모두들……"

    ch_nar "왜…… 바닥에 쓰러져 있는 거야……?"

    ch_nar "아, 아니야……"

    ch_nar "이럴…… 이럴 리 없어……"

    ch_nar "아니야…… 이건…… 현실이……"

    ch_nar "이, 이런 게…… 현실일 리가……!!!"

    ch_nar "키, 키……"

    play sound "audio/sound/surp.mp3"
    show cg_kimura onlayer middle with hpunch

    player "{b}{size=30}키 사 마ㅡ!!!!!!!!!!!!!!!!!!!!!!{/size}{/b}"

    player "{b}{size=30}도오시테 와라우노카!!!!{/size}{/b}"

    hatena "고레가 겐지츠… 타다 소레 다케."

    player "{b}이츠카… 카나라즈{/b}"

    show cg_kimura onlayer middle with hpunch

    player "{b}{size=30}부치코로스!!!!!!{/size}{/b}"

    hatena "헤에……"

    $camera_move(0, -200, 400, 0, 0.2)

    play sound "audio/main/kimura.mp3"

    hatena "{b}{size=30}{color=#FF2929}“야 떼 미 로”{/color}{/size}{/b}"

    show bg_badend with fade

    $renpy.pause(1.0)

    ch_nar "{color=#FF2929}DEAD END{/color}"

    return
## 참피 엔딩 #######################
label BAD:

    scene bg_town

    ch_ayumi "선배와 함께라면 저는 좋아요……!"

    player "음…… 그럴까?"

    player "좋아, 같이 가자!"

    stop music fadeout 2.0

    $renpy.pause(2.0)

    show bg_black
    hide bg_town

    $renpy.pause(1.0)

    play sound "audio/sound/amesopen.mp3"
    show ames_reverse

    $renpy.pause(4.0)
    hide bg_black

    show cg_ames
    hide ames_reverse

    play music "audio/main/ames.mp3" fadein 3.0

    hatena "하아……"

    hatena "당신, 대체 무슨 짓을 한 거야?"

    hatena "확실히, 당신의 선택에 따라 그녀들의 운명이 바뀌게 될 거라고 말했었지만……"

    hatena "이런 결말을 보고 싶어서 당신에게 선택할 권리를 준 게 아니란 말야……"

    hatena "……뜬금없이 튀어 나와서는 무슨 알 수 없는 소릴 하는 거냐구?"

    hatena "……"

    hatena "……잘 들어."

    hatena "이제 당신에게 주어진 선택지는 단 2개뿐이야."

    hatena "모든 것을 잊고 처음으로 돌아가서 다시 시작할 것인지, 아니면……"

    hatena "{b}……그녀들의 {color=#FF2929}참혹한 파멸{/color}을 두 눈으로 지켜볼 것인지.{/b}"

    hatena "뭐…… 사실은, 당신을 탓할 것도 없어."

    hatena "당신은 그저, 스스로의 신념에 따라 선택한 것일 뿐이잖아?"

    hatena "물론 그 결정에 대한 책임은 당신이 져야 할 테지만."

    hatena "그래서…… 어떡할래?"

    hatena "어쩌면 이것이, 운명을 바꿀 수 있는 마지막 기회일지도 모르지."

    hatena "당신이 만들어 낸 운명을 직접 지켜보겠어? 아니면…… 부정할 테야?"

    menu:
        "모든 것을 잊고 다시 시작한다.choice_1":

            hatena "……그래."

            hatena "당신의 선택을 존중할게."

            hatena "착각은 하지 말아 줘. 다시 시작한다 해도, 무언가 극적으로 바뀌는 일은 없을지도 몰라."

            hatena "그렇지만…… 다음 번에는 부디, 같은 실수를 반복하지 않길 바랄게."

            hatena "그럼, 또 봐."

            play sound "audio/sound/amesclose.mp3"
            show ames_swift
            hide ames
            $renpy.pause(3.0)

            stop music fadeout 3.0

            show bg_badend

            $renpy.pause(1.0)

            ch_nar "Thank you for playing"

            return

        "파멸을 맞이한다.choice_2":   

            hatena "……그래."

            hatena "부디, 후회 없는 선택을 했길 바랄게."

            hatena "그럼…… 또 봐." 

            play sound "audio/sound/amesclose.mp3"
            show ames_swift
            hide ames

            $renpy.pause(3.0)
            stop music fadeout 3.0

            show bg_field with fade

            play music "audio/main/emer.mp3"

            ch_ayumi "꺄…… 꺄아아아아악!!!!"

            show stand_Ninon_panic with dissolve

            ch_ninon "아유미 씨가 비명을?!"

            ch_ninon "어…… 어디인가요 입니까!!! 모습이 보이지 않아서 찾을 수 없다 입니다!!!"

            hide stand_Ninon_panic

            ch_ayumi "저, 저기, 하, 하늘…… 햐느렛!!! 혀, 혀 씹었……"

            show stand_Yuki_ddung with dissolve

            ch_yuki "하늘……? 그러고 보니, 뭔가 주변이 어두워진 것 같은……"

            hide stand_Yuki_ddung

            $renpy.pause(2.0)

            show bg_field with hpunch

            play sound "audio/sound/growl.mp3"

            monster "크르아아아아아!!!!!!!!"

            show stand_Yuki_surp with dissolve

            ch_yuki "……뭐……야, 저게……?"

            hide stand_Yuki_surp

            show stand_Monica_surprised with dissolve

            ch_monica "저건…… 분명……"

            ch_monica "……그럴 리 없어…… 베리오 화산에나 서식하는 개체가 어째서……"

            ch_monica "게다가 저 크기는 대체……! 아종……? 아종이라 해도, 저래서는 마치……"

            hide stand_Monica_surprised

            player "무…… 무슨 말이야? 알아듣게 얘기해……! 저게 뭔데?!"

            show stand_Monica_ddung with dissolve

            ch_monica "……드래곤……"

            ch_monica "드래곤이다……!"

            ch_monica "바보 같은……!! 영역의 경계를 벗어나는 것조차 꺼리는 놈들일 터인데……?!"

            hide stand_Monica_ddung

            show stand_Ninon_angry with dissolve

            ch_ninon "모니카 씨!!! 지금은 그런 것을 따질 때가 아니에요 입니다!!"

            ch_ninon "저 녀석을 이대로 두면, 마을이 쑥뒈밭이 될 것 입니다!!!"

            hide stand_Ninon_angry
            show stand_Monica_ddung with dissolve

            ch_monica "전원, 전투 준비!!!"

            ch_monica "귀공은 사람들을 대피시키고, 다른 길드에게 협력 요청을 해 다오! 부탁한다!"

            player "아…… 알았어!"

            hide stand_Monica_ddung with dissolve

            show bg_field with hpunch

            play sound "audio/sound/growl.mp3"

            monster "크워어어어어!!!!!!!!"

            show stand_Monica_down with dissolve

            ch_monica "큿…… 엄청난 위압감……"

            ch_monica "드래곤 토벌, 우리가 과연…… 할 수 있을까……?"

            hide stand_Monica_down
            show stand_Ninon with dissolve

            ch_ninon "할 수 있어요 입니다!! 쇼군의 특훈을 거치고, 마물을 성공적으로 해치운 우리에게…… 불가능이란 없소 입니다!!!"

            show stand_Kuka at left with dissolve

            ch_kuka "이…… 이런 곳에서 쓰러져 버린다면, 더 이상 망상조차 할 수 없는 몸이 되어버리겠죠…… 그, 그러니까…… 쿠우카, 힘내겠습니다……!!"

            show stand_Yuki_ddung at right with dissolve

            ch_yuki "하아…… 피부가 상하는 건 진짜 싫은데, 그런 걸 따질 만한 상황은 아닌 것 같네. 전투가 끝나면 확실히 보상 받을 테니까 각오하라구……!"

            ch_ayumi "으으…… 자, 자신 없고 무섭지만…… 선배와 모두를 지키기 위해서라면……! 할 수 있는 데까지 힘써 볼게요오……!!"

            hide stand_Yuki_ddung
            hide stand_Kuka
            hide stand_Ninon
            show stand_Monica with dissolve

            ch_monica "모두들……!"

            $renpy.pause(2.0)

            play music "audio/main/9bbong.mp3"

            show stand_Monica_ddung
            hide stand_Monica

            ch_monica "……제군들, 우리는……"

            ch_monica "우리는…… {b}‘바이스플뤼겔 랜드솔지부’{/b}다."

            ch_monica "……떠올려라, 우리의 본분을!!!"

            ch_monica "긍지를 걸어라, 우리의 가슴에……!!"

            ch_monica "비상하라…… 순백색 날개를 펼치고!!!"

            play sound "audio/sound/baldo.mp3"

            ch_monica "{b}{size=30}바이스플뤼겔!!!! 전원 발도를 허가한다!!!!{/size}{/b}"

            show bg_field with hpunch

            play sound "audio/sound/growl.mp3"

            monster "크라라라아아아아!!!!!!!!!!"

            ch_monica "간다……!!"

            ch_monica "이 검으로, 사람들을……"

            ch_monica "랜드솔을…… 지켜 낸다!!!!"

            hide stand_Monica_ddung

            show bg_black with dissolve

            hide bg_field

            stop music

            play sound "audio/sound/knife1.wav"

            ch_nar "파킨-"

            $renpy.pause(2.0)

            show cg_champi with hpunch

            ch_monica "데샤아아아악!!!!!!!"

            show cg_champi with hpunch

            ch_kuka "화끈해진 레후!!!!!!"

            show cg_champi with hpunch

            ch_yuki "똥닌겐 상!!!!! 뭐라도 해보는 테치!!!!!!! 세레브한 와타시가 죽어버리는 테챠아아앗!!!!!!!"

            show cg_champi with hpunch

            ch_ninon "레훼에에엑!!!! 도라곤 상!!!!! 이런 아픈 메테오는 그만두길 바라는 레후!!!!!!"

            show cg_champi with hpunch

            ch_ayumi "일가실각 테챠아아앗!!!!!!!"

            show bg_black with dissolve
            hide cg_champi

            ch_nar "그날 랜드솔은 해골 다섯 개를 받았다……"

            show bg_badend

            $renpy.pause(1.0)

            ch_nar "{color=#FF2929}DEAD END{/color}"
            
            return