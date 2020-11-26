vexcode_brain_precision = 0
vexcode_controller_1_precision = 0
vexcode_controller_2_precision = 0
x = 0
y = 0
z = 0
_E6_B6_88_E6_81_AF1 = Event()
a1 = Event()
a2 = Event()
a3 = Event()
a = Event()

#横向移动模块，左边是正数，右边是负数
def sidesway_n1(sidesway_n1__n1):
    global x, y, z, _E6_B6_88_E6_81_AF1, a1, a2, a3, a, vexcode_brain_precision, vexcode_controller_1_precision, vexcode_controller_2_precision
    left_motor_a.set_velocity(70, PERCENT)
    left_motor_b.set_velocity(70, PERCENT)
    right_motor_a.set_velocity(70, PERCENT)
    right_motor_b.set_velocity(70, PERCENT)
    left_motor_a.spin_for(REVERSE, sidesway_n1__n1, DEGREES, wait=False)
    left_motor_b.spin_for(FORWARD, sidesway_n1__n1, DEGREES, wait=False)
    right_motor_a.spin_for(REVERSE, sidesway_n1__n1, DEGREES, wait=False)
    right_motor_b.spin_for(FORWARD, sidesway_n1__n1, DEGREES, wait=True)

#左斜向移动模块，左前是正，右后是负
def LFmove_n2(LFmove_n2__n2):
    global x, y, z, _E6_B6_88_E6_81_AF1, a1, a2, a3, a, vexcode_brain_precision, vexcode_controller_1_precision, vexcode_controller_2_precision
    left_motor_b.set_velocity(70, PERCENT)
    right_motor_a.set_velocity(70, PERCENT)
    left_motor_b.spin_for(FORWARD, LFmove_n2__n2, DEGREES, wait=False)
    right_motor_a.spin_for(FORWARD, LFmove_n2__n2, DEGREES, wait=True)

#右斜向移动模块，右前是正，左后是负
def RFmove_n3(RFmove_n3__n3):
    global x, y, z, _E6_B6_88_E6_81_AF1, a1, a2, a3, a, vexcode_brain_precision, vexcode_controller_1_precision, vexcode_controller_2_precision
    left_motor_a.set_velocity(70, PERCENT)
    right_motor_b.set_velocity(70, PERCENT)
    left_motor_a.spin_for(FORWARD, RFmove_n3__n3, DEGREES, wait=False)
    right_motor_b.spin_for(FORWARD, RFmove_n3__n3, DEGREES, wait=True)

# 吸球模块
def around_sec(around_sec__sec):
    global x, y, z, _E6_B6_88_E6_81_AF1, a1, a2, a3, a, vexcode_brain_precision, vexcode_controller_1_precision, vexcode_controller_2_precision
    AoundUp.spin(FORWARD)
    AoundDown.spin(FORWARD)
    wait(around_sec__sec,SECONDS)
    AoundUp.stop()
    AoundDown.stop()

# 预设线程1
def when_started1():
    global x, y, z, _E6_B6_88_E6_81_AF1, a1, a2, a3, a, vexcode_brain_precision, vexcode_controller_1_precision, vexcode_controller_2_precision
    jinqiuL.set_velocity(100, PERCENT)
    jinqiuR.set_velocity(100, PERCENT)
    AoundUp.set_velocity(100, PERCENT)
    AoundDown.set_velocity(100, PERCENT)
    AoundUp.set_stopping(HOLD)
    AoundDown.set_stopping(HOLD)
    jinqiuL.set_stopping(HOLD)
    jinqiuR.set_stopping(HOLD)
    left_motor_a.set_stopping(BRAKE)
    left_motor_b.set_stopping(BRAKE)
    right_motor_a.set_stopping(BRAKE)
    right_motor_b.set_stopping(BRAKE)
    

#遥控模块
def ondriver_drivercontrol_0():
    global x, y, z, _E6_B6_88_E6_81_AF1, a1, a2, a3, a, vexcode_brain_precision, vexcode_controller_1_precision, vexcode_controller_2_precision
    while True:
        y = controller_1.axis3.position()
        x = controller_1.axis4.position()
        z = controller_1.axis1.position()
        if math.fabs(x) > 30 or math.fabs(y) > 30 or math.fabs(z) > 5:
            left_motor_a.set_velocity(((x + y) + z), PERCENT)
            left_motor_b.set_velocity(((x - y) - z), PERCENT)
            right_motor_a.set_velocity(((y - x) - z), PERCENT)
            right_motor_b.set_velocity(((x + y) - z), PERCENT)
            left_motor_a.spin(FORWARD)
            left_motor_b.spin(REVERSE)
            right_motor_a.spin(FORWARD)
            right_motor_b.spin(FORWARD)
        else:
            left_motor_a.stop()
            left_motor_b.stop()
            right_motor_a.stop()
            right_motor_b.stop()
        wait(5, MSEC)

# 预设线程2 
def when_started2():
    global x, y, z, _E6_B6_88_E6_81_AF1, a1, a2, a3, a, vexcode_brain_precision, vexcode_controller_1_precision, vexcode_controller_2_precision
    while True:
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        brain.screen.print(drivetrain.heading(), precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
        brain.screen.next_row()
        brain.screen.print(drivetrain.rotation(), precision=6 if vexcode_brain_precision is None else vexcode_brain_precision)
        wait(5, MSEC)


# 15秒自动程序
def onauton_autonomous_0():
    global x, y, z, _E6_B6_88_E6_81_AF1, a1, a2, a3, a, vexcode_brain_precision, vexcode_controller_1_precision, vexcode_controller_2_precision
    drivetrain.set_turn_velocity(70, PERCENT)
    drivetrain.turn_for(RIGHT, 90, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, 200, MM, wait=True)
    drivetrain.turn_for(LEFT, 90, DEGREES, wait=True)
    a1.broadcast()
    around_sec(3)


def onevent_controller_1buttonR1_pressed_0():
    global x, y, z, _E6_B6_88_E6_81_AF1, a1, a2, a3, a, vexcode_brain_precision, vexcode_controller_1_precision, vexcode_controller_2_precision
    jinqiuL.spin(FORWARD)
    jinqiuR.spin(FORWARD)

def onevent_controller_1buttonB_released_0():
    global x, y, z, _E6_B6_88_E6_81_AF1, a1, a2, a3, a, vexcode_brain_precision, vexcode_controller_1_precision, vexcode_controller_2_precision
    AoundUp.stop()
    AoundDown.stop()

def onevent_controller_1buttonR2_pressed_0():
    global x, y, z, _E6_B6_88_E6_81_AF1, a1, a2, a3, a, vexcode_brain_precision, vexcode_controller_1_precision, vexcode_controller_2_precision
    jinqiuL.stop()
    jinqiuR.stop()

def onevent_controller_1buttonX_pressed_0():
    global x, y, z, _E6_B6_88_E6_81_AF1, a1, a2, a3, a, vexcode_brain_precision, vexcode_controller_1_precision, vexcode_controller_2_precision
    AoundUp.spin(FORWARD)
    AoundDown.spin(REVERSE)

def onevent_controller_1buttonL1_pressed_0():
    global x, y, z, _E6_B6_88_E6_81_AF1, a1, a2, a3, a, vexcode_brain_precision, vexcode_controller_1_precision, vexcode_controller_2_precision
    AoundUp.spin(FORWARD)
    AoundDown.spin(FORWARD)

def onevent_controller_1buttonL2_pressed_0():
    global x, y, z, _E6_B6_88_E6_81_AF1, a1, a2, a3, a, vexcode_brain_precision, vexcode_controller_1_precision, vexcode_controller_2_precision
    AoundUp.stop()
    AoundDown.stop()

def onevent_a1_0():
    global x, y, z, _E6_B6_88_E6_81_AF1, a1, a2, a3, a, vexcode_brain_precision, vexcode_controller_1_precision, vexcode_controller_2_precision
    jinqiuL.spin(FORWARD)
    jinqiuR.spin(FORWARD)
    wait(5, SECONDS)
    jinqiuL.stop()
    jinqiuR.stop()

# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    auton_task_0 = Thread( onauton_autonomous_0 )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks
    auton_task_0.stop()

def vexcode_driver_function():
    # Start the driver control tasks
    driver_control_task_0 = Thread( ondriver_drivercontrol_0 )
    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks
    driver_control_task_0.stop()

# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )

# system event handlers
controller_1.buttonR1.pressed(onevent_controller_1buttonR1_pressed_0)
controller_1.buttonB.released(onevent_controller_1buttonB_released_0)
controller_1.buttonR2.pressed(onevent_controller_1buttonR2_pressed_0)
controller_1.buttonX.pressed(onevent_controller_1buttonX_pressed_0)
controller_1.buttonL1.pressed(onevent_controller_1buttonL1_pressed_0)
controller_1.buttonL2.pressed(onevent_controller_1buttonL2_pressed_0)
a1(onevent_a1_0)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

ws1 = Thread( when_started2 )
when_started1()
