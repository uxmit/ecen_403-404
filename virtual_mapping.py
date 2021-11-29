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

#moves x axis motors to a set x axist distance in feet
def x_axis_rotation(x_axis):
    xaxis_conversion_ft_to_cm = x_axis * 30.48
    motor_circumference = 2*math.pi * (0.5/2) #distance traveled from one rotation (cm)
    motor_step = round(motor_circumference / 400, 3) #distance of 1 step
    x_axis_num_of_rotations = round(xaxis_conversion_ft_to_cm / motor_circumference , 1)
    print("Need to move", xaxis_conversion_ft_to_cm, "cm which converts to", x_axis_num_of_rotations, "rotations clockwise...")
    print("Starting x axis motor movement...")

    rotation_x = 0
    #takes image every rotation
    for x in range(int(x_axis_num_of_rotations)):
        motor1_control(400)
        rotation_x = rotation_x +1
        print("x-axis rotation", rotation_x, "out of", x_axis_num_of_rotations)
        print("Taking image...") #insert camera image taking code here
        time.sleep(1)
    time.sleep(1)

    x_axis_leftover_rotation = int(round(x_axis_num_of_rotations - int(x_axis_num_of_rotations), 1) / motor_step)
    print('Now moving leftover x axis nonfull rotations...', x_axis_leftover_rotation)
    motor1_control(x_axis_leftover_rotation)
    time.sleep(1)
    print("Taking last x axis image...")

# x_axis_rotation(19.4)


#moves y axis motors to set y axis distance in feet
def y_axis_rotation(y_axis):
    yaxis_conversion_ft_to_cm = y_axis * 30.48
    motor_circumference = 2*math.pi * (0.5/2) #distance traveled from one rotation (cm)
    motor_step = round(motor_circumference / 400, 3) #distance of 1 step
    y_axis_num_of_rotations = round(yaxis_conversion_ft_to_cm / motor_circumference, 1)
    print("Need to move", yaxis_conversion_ft_to_cm, "cm which converts to ", y_axis_num_of_rotations, "rotations clockwise...")
    print("Starting y axis motor movement...")

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

#resets x axis back to origin (0,0)
def x_axis_reset(x_axis):
    xaxis_conversion_ft_to_cm = x_axis * 30.48
    motor_circumference = 2*math.pi * (0.5/2) #distance traveled from one rotation (cm)
    motor_step = round(motor_circumference / 400, 3) #distance of 1 step
    x_axis_num_of_rotations = round(xaxis_conversion_ft_to_cm / motor_circumference , 1)
    print("Reseting x axis motors back to origin...")
    print("Need to move", -xaxis_conversion_ft_to_cm, "cm which converts to ", x_axis_num_of_rotations, "rotations counterclockwise...")
    print("Starting x axis motor movement...")

    rotation_x = 0
    for x in range(int(x_axis_num_of_rotations)):
        motor1_control(-400)
        rotation_x = rotation_x +1
        print("x-axis rotation ", rotation_x, "out of ", x_axis_num_of_rotations)
    time.sleep(1)

    x_axis_leftover_rotation = int(round(x_axis_num_of_rotations - int(x_axis_num_of_rotations), 1) / motor_step)
    print('Now moving leftover nonfull rotations...', -x_axis_leftover_rotation)
    motor1_control(-x_axis_leftover_rotation)
    # print("Taking last x axis image...")


#resets y axis back to origin (0,0)
def y_axis_reset(y_axis):
    yaxis_conversion_ft_to_cm = y_axis * 30.48
    motor_circumference = 2*math.pi * (0.5/2) #distance traveled from one rotation (cm)
    motor_step = round(motor_circumference / 400, 3) #distance of 1 step
    y_axis_num_of_rotations = round(yaxis_conversion_ft_to_cm / motor_circumference, 1)
    print("Resetting y axis motors back to origin...")
    print("Need to move", -yaxis_conversion_ft_to_cm, "cm which converts to ", y_axis_num_of_rotations, "rotations counterclockwise...")
    print("Starting y axis motor movement...")

    rotation_y = 0
    for x in range(int(y_axis_num_of_rotations)):
        motor2_control(-400)
        rotation_y = rotation_y +1
        print("y-axis rotation", rotation_y, "out of ", y_axis_num_of_rotations)
    time.sleep(1)

    y_axis_leftover_rotation = int(round(y_axis_num_of_rotations - int(y_axis_num_of_rotations),1) / motor_step)
    print("Now moving leftover nonfull rotations..." ,-y_axis_leftover_rotation)
    motor2_control(-y_axis_leftover_rotation)

# x_axis_reset(0.5)
# y_axis_reset(0.5)

def virtual_mapping(x_axis, y_axis):
    x_axis_rotation(x_axis) #goes across initial x axis and takes images of first row
    x_axis_reset(x_axis) #reset x axis back to origin
    yaxis_conversion_ft_to_cm = y_axis * 30.48
    motor_circumference = 2*math.pi * (0.5/2) #distance traveled from one rotation (cm)
    motor_step = round(motor_circumference / 400, 3) #distance of 1 step
    y_axis_num_of_rotations = round(yaxis_conversion_ft_to_cm / motor_circumference, 1)
    print("Need to move", yaxis_conversion_ft_to_cm, "cm which converts to ", y_axis_num_of_rotations, "rotations clockwise...")
    print("Starting y axis motor movement...")

    rotation_y = 0
    #loops through y axis and every rotation, runs x axis rotation function and takes image
    for x in range(int(y_axis_num_of_rotations)):
        rotation_y = rotation_y +1
        print("Rotating y axis...", rotation_y, "out of ", y_axis_num_of_rotations)
        motor2_control(400) #rotate y axis
        time.sleep(3)
        print("Starting x axis tranverse and image taking...")
        x_axis_rotation(x_axis) #loop through x axis on new y axis and takes images
        x_axis_reset(x_axis) #reset x axis back to origin

        # print("y-axis rotation", rotation_y, "out of ", y_axis_num_of_rotations)
    time.sleep(1)

    y_axis_leftover_rotation = int(round(y_axis_num_of_rotations - int(y_axis_num_of_rotations),1) / motor_step)
    print("Now moving leftover y axis nonfull rotations..." ,y_axis_leftover_rotation)
    motor2_control(y_axis_leftover_rotation)
    print("Final x axis tranverse and image taking...")
    x_axis_rotation(x_axis)
    print("Reseting x axis back to origin...")
    x_axis_reset(x_axis)
    print("Reseting y axis back to origin...")
    y_axis_reset(y_axis)
    print("All x and y axis motors reset back to origin. Virtual greenhouse mapping complete..")


# virtual_mapping(0.5,0.5)
# motor1_control(50)
motor2_control(-400)


# print(int(x_axis_num_of_rotations))
# print(int(y_axis_num_of_rotations))
# x_axis_leftover_rotation = int(round(x_axis_num_of_rotations - int(x_axis_num_of_rotations), 1) / motor_step)
# print(x_axis_leftover_rotation)
# motor1_control(x_axis_leftover_rotation)
# y_axis_leftover_rotation = int(round(y_axis_num_of_rotations - int(y_axis_num_of_rotations),1) / motor_step)
# print(y_axis_leftover_rotation)
# motor2_control(y_axis_leftover_rotation)