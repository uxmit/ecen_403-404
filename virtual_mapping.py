from motor_control import motor1_setup, motor2_setup, motor1_control , motor2_control
import math
import time

#greenhouse dimensions in feet
# x_axis= 1 #feet
# y_axis= 1 #feet

# xaxis_conv_ft_to_cm = x_axis * 30.48
# yaxis_conversion_ft_to_cm = y_axis * 30.48
# # print(xaxis_conv_ft_to_cm)
# # print(yaxis_conversion_ft_to_cm)


# motor_circumference = 2*math.pi * (0.5/2) #distance traveled from one rotation (cm)
# motor_step = round(motor_circumference / 400, 3) #distance of 1 step
# # print("motor circumference: ",motor_circumference)
# # print("motor step:", motor_step)

# x_axis_num_of_rotations = round(xaxis_conv_ft_to_cm / motor_circumference , 1)
# y_axis_num_of_rotations = round(yaxis_conversion_ft_to_cm / motor_circumference, 1)
# x_axis_num_of_rotations = 5
# y_axis_num_of_rotations = 5
# print("Number of rotations needed on x axis", x_axis_num_of_rotations)
# print("Number of rotations needed on y axis", y_axis_num_of_rotations)
# motor1_control(400)
# motor2_control(400)

# rotation_x = 0
# for x in range(int(x_axis_num_of_rotations)):
#     motor1_control(400)
#     rotation_x = rotation_x +1
#     print("Rotation ", rotation_x, "out of ", x_axis_num_of_rotations)

# rotation_y = 0
# for x in range(int(y_axis_num_of_rotations)):
#     motor2_control(400)
#     rotation_y = rotation_y +1
#     print("Rotation", rotation_y, "out of ", y_axis_num_of_rotations)

def x_axis_rotation(x_axis):
    xaxis_conv_ft_to_cm = x_axis * 30.48
    motor_circumference = 2*math.pi * (0.5/2) #distance traveled from one rotation (cm)
    motor_step = round(motor_circumference / 400, 3) #distance of 1 step
    x_axis_num_of_rotations = round(xaxis_conv_ft_to_cm / motor_circumference , 1)

    rotation_x = 0
    for x in range(int(x_axis_num_of_rotations)):
        motor1_control(400)
        rotation_x = rotation_x +1
        print("x-axis rotation ", rotation_x, "out of ", x_axis_num_of_rotations)
    time.sleep(1)

    x_axis_leftover_rotation = int(round(x_axis_num_of_rotations - int(x_axis_num_of_rotations), 1) / motor_step)
    print('Now moving leftover nonfull rotations...', x_axis_leftover_rotation)
    motor1_control(x_axis_leftover_rotation)
# x_axis_rotation(19.4)



def y_axis_rotation(y_axis):
    yaxis_conversion_ft_to_cm = y_axis * 30.48
    motor_circumference = 2*math.pi * (0.5/2) #distance traveled from one rotation (cm)
    motor_step = round(motor_circumference / 400, 3) #distance of 1 step
    y_axis_num_of_rotations = round(yaxis_conversion_ft_to_cm / motor_circumference, 1)

    rotation_y = 0
    for x in range(int(y_axis_num_of_rotations)):
        motor2_control(400)
        rotation_y = rotation_y +1
        print("y-axis rotation", rotation_y, "out of ", y_axis_num_of_rotations)
    time.sleep(1)

    y_axis_leftover_rotation = int(round(y_axis_num_of_rotations - int(y_axis_num_of_rotations),1) / motor_step)
    print("Now moving leftover nonfull rotations..." ,y_axis_leftover_rotation)
    motor2_control(y_axis_leftover_rotation)

# x_axis_rotation(0.5)
# y_axis_rotation(0.5)

def x_axis_reset(x_axis):
    xaxis_conv_ft_to_cm = x_axis * 30.48
    motor_circumference = 2*math.pi * (0.5/2) #distance traveled from one rotation (cm)
    motor_step = round(motor_circumference / 400, 3) #distance of 1 step
    x_axis_num_of_rotations = round(xaxis_conv_ft_to_cm / motor_circumference , 1)

    rotation_x = 0
    for x in range(int(x_axis_num_of_rotations)):
        motor1_control(-400)
        rotation_x = rotation_x +1
        print("x-axis rotation ", rotation_x, "out of ", x_axis_num_of_rotations)
    time.sleep(1)

    x_axis_leftover_rotation = int(round(x_axis_num_of_rotations - int(x_axis_num_of_rotations), 1) / motor_step)
    print('Now moving leftover nonfull rotations...', -x_axis_leftover_rotation)
    motor1_control(-x_axis_leftover_rotation)


def y_axis_reset(y_axis):
    yaxis_conversion_ft_to_cm = y_axis * 30.48
    motor_circumference = 2*math.pi * (0.5/2) #distance traveled from one rotation (cm)
    motor_step = round(motor_circumference / 400, 3) #distance of 1 step
    y_axis_num_of_rotations = round(yaxis_conversion_ft_to_cm / motor_circumference, 1)

    rotation_y = 0
    for x in range(int(y_axis_num_of_rotations)):
        motor2_control(-400)
        rotation_y = rotation_y +1
        print("y-axis rotation", rotation_y, "out of ", y_axis_num_of_rotations)
    time.sleep(1)

    y_axis_leftover_rotation = int(round(y_axis_num_of_rotations - int(y_axis_num_of_rotations),1) / motor_step)
    print("Now moving leftover nonfull rotations..." ,-y_axis_leftover_rotation)
    motor2_control(-y_axis_leftover_rotation)

x_axis_reset(0.5)
y_axis_reset(0.5)



# print(int(x_axis_num_of_rotations))
# print(int(y_axis_num_of_rotations))
# x_axis_leftover_rotation = int(round(x_axis_num_of_rotations - int(x_axis_num_of_rotations), 1) / motor_step)
# print(x_axis_leftover_rotation)
# motor1_control(x_axis_leftover_rotation)
# y_axis_leftover_rotation = int(round(y_axis_num_of_rotations - int(y_axis_num_of_rotations),1) / motor_step)
# print(y_axis_leftover_rotation)
# motor2_control(y_axis_leftover_rotation)