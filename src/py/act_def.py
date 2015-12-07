# -*- coding: UTF-8 -*- 
class act_def:
  CAR_ACT_TYPE_MOVE = 0 #               //移动
  CAR_ACT_TYPE_MOVE_TO_DEST =1 #
  CAR_ACT_TYPE_TURN =2#              //转向
  CAR_ACT_TYPE_TURN_TO_DIRECTION =3 #  //转到指定的方向
  CAR_ACT_TYPE_ORIAIANL_CTRL = 4 #    //最原始的电机控制
  CAR_ACT_TYPE_SLEEP=5 #        #停止 单位ms
  CAR_ACT_TYPE_LIFT=6 #       #举升 单位ms
  CAR_ACT_TYPE_LOWER=7 #        #降低 单位ms
  CAR_ACT_TYPE_MOVE_NO_CHECK=8 #
  CAR_ACT_TYPE_TURN_NO_CHECK = 9 #
  CAR_ACT_TYPE_NULL = 0xFF