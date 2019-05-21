# 此飞机大战项目是根据黑马课程的讲解,而写的代码

此项目主要有两个python文件.
 (1) plane_sprites.py  精灵组的类和方法的定义
 背景精灵类, 敌机精灵类, 英雄精灵类,子弹精灵类
 (2) plane_main.py  飞机大战的主要入口
 里面主要定义七个方法:
    游戏的初始化 __init__()
    创建精灵组 __create_sprites()
    事件检测   __event_handler()
    碰撞检测   __check_collide()
    更新精灵组  __update_sprites()
    游戏开始运行 start_game()
    静态的游戏结束方法 __game_over()


 定时器: pygame.time.set_timer(enventid, 毫秒)
   如果事件类型是我们定义的eventid,则定时器事件就被触发

由于我是使用的python2.7写的,继承父类方法不能使用 super().方法名()
     可以使用 super(子类名, self).方法名() 来继承父类的方法
