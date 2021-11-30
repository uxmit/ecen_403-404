from motor_control import motor1_setup, motor2_setup, motor1_control , motor2_control
import math
import time

# GPIO.setwarnings(False)

# x_axis = 800
# y_axis = 800

# def detect_out_bounds():


#x and y list of numbers indicating target location
#1 motor step = 1 move unit (ease of demo)
def motor_move(distance, motor_control, name):
    # for x in x_list:
        print(f"{name} location value", distance)

        #if absolute x value is <= 10, throw error and skip
        if abs(distance) <= 10:
            print("Error: Distance", distance, "is too small to move, skipping to next value.")
            # continue
            return

        rotation_x = 0
        if abs(distance) > 400: #if more than 1 rotation
            x_num_of_rotations = round((distance / 400), 1)
            print(distance, "is",x_num_of_rotations, "number of rotations")
            for i in range(int(abs(x_num_of_rotations))):
                if distance > 400: #if x is positive
                    # print("Rotating", i+1, "out of ", x_num_of_rotations)
                    rotation_x = rotation_x +1
                    print("Rotating", rotation_x, "out of ", x_num_of_rotations)
                    motor_control(400)
                    # print("Taking image...") #insert camera image taking code here
                    time.sleep(1)
                if distance < -400:
                    # print("rotating" ,x)
                    rotation_x = rotation_x +1
                    print("Rotating", -rotation_x, "out of ", x_num_of_rotations)
                    motor_control(-400)
                    # rotation_x = rotation_x +1
                    # print("Rotating", rotation_x, "out of ", x_num_of_rotations)
                    # print("Taking image...") #insert camera image taking code here
                    time.sleep(1)

            time.sleep(2)
            motor_step = 1
            x_axis_leftover_rotation = round(x_num_of_rotations - int(x_num_of_rotations), 1)
            # print(round(x_num_of_rotations - int(x_num_of_rotations), 1))
            converted_x_axis_leftover_rotation = x_axis_leftover_rotation * 400 #converts leftover nonfull rotatons
            print(f'Now moving leftover {name} axis nonfull rotations...', x_axis_leftover_rotation)
            print('Moving motor', int(x_axis_leftover_rotation * 400), "out of 400")
            time.sleep(1)
            motor_control(int(x_axis_leftover_rotation*400))
            # time.sleep(2)
            print("Done rotating nonfull rotations, continuing to next value..")
            time.sleep(1)
            # continue
            return
            # print("Taking last x axis image...")
        
        #if x value <= 400
        print(f"Motor moving {name}...", distance)
        motor_control(distance)
        time.sleep(2)



# def y_motor_move(y):
#     # for y in y_list:
#         print("y location value", y)

#         #if absolute y value is <= 10, throw error and skip
#         if abs(y) <= 10:
#             print("Error: Distance", y, "is too small to move, skipping to next value.")
#             # continue

#         rotation_y = 0
#         if abs(y) > 400: #if more than 1 rotation
#             y_num_of_rotations = round((y / 400), 1)
#             print(y, "is",y_num_of_rotations, "number of rotations")
#             for i in range(int(abs(y_num_of_rotations))):
#                 if y > 400: #if y is positive
#                     # print("Rotating", i+1, "out of ", x_num_of_rotations)
#                     rotation_y = rotation_y +1
#                     print("Rotating", rotation_y, "out of ", y_num_of_rotations)
#                     motor2_control(400)
#                     # print("Taking image...") #insert camera image taking code here
#                     time.sleep(1)
#                 if y < -400:
#                     # print("rotating" ,y)
#                     rotation_y = rotation_y +1
#                     print("Rotating", -rotation_y, "out of ", y_num_of_rotations)
#                     motor2_control(-400)
#                     # rotation_x = rotation_x +1
#                     # print("Rotating", rotation_x, "out of ", x_num_of_rotations)
#                     # print("Taking image...") #insert camera image taking code here
#                     time.sleep(1)

#             time.sleep(2)
#             motor_step = 1
#             y_axis_leftover_rotation = round(y_num_of_rotations - int(y_num_of_rotations), 1)
#             # print(round(x_num_of_rotations - int(x_num_of_rotations), 1))
#             converted_y_axis_leftover_rotation = y_axis_leftover_rotation * 400 #converts leftover nonfull rotatons
#             print('Now moving leftover y axis nonfull rotations...', y_axis_leftover_rotation)
#             print('Moving motor', int(y_axis_leftover_rotation * 400), "out of 400")
#             time.sleep(1)
#             motor2_control(int(y_axis_leftover_rotation*400))
#             # time.sleep(2)
#             print("Done rotating nonfull rotations, continuing to next value..")
#             time.sleep(1)
#             # continue
#             # print("Taking last y axis image...")
        
#         #if y value >= 400
#         # if abs(y) <= 400:
#         print("Motor moving y...", y)
#         motor2_control(y)
#         time.sleep(2)


# # x_motor_move(400)

def get_coor(filename, deminsions = 2):
    rvalue = []
    for i in range(deminsions):
        rvalue.append([])
    with open(filename, "r") as f:
        for line in f:
            arr = [int(float(x.strip())) for x in line.split(",")] #TODO: Do error checking on conversion to float.
            if len(arr) != deminsions:
                raise RuntimeError(f"Invalid number demensions found in cvs file. Expected {deminsions}. Line: {line}")
            for i in range(deminsions):
                rvalue[i].append(arr[i])
            # for i in range(0, deminsions, 2):
                # print(f"{arr[i]}, {arr[i + 1]}")
    return rvalue

#MAIN
if __name__ == "__main__":
    motor1_control(50)
    motor2_control(50)
    # x_location = [0, 50, 250, -400, 10, -10, 800, -450,  -850]#, -900, -10, 1000]#, 5, -5, 1, -1, 0, -800, -600, 600, 400]
    # y_location = [0, 50, 250, -400, 10, -10, 800, -450,  -850]#[200, 400, 200, 400]
    coors = get_coor("test.csv")
    x_location = coors[0]
    y_location = coors[1]
    for i in range(len(x_location)):
        print(x_location[i])
        print("MOVING X-AXIS DISTANCE:")
        # print(f"x, y = : {x_location[i]}, {y_location[i]}")
        motor_move(x_location[i], motor1_control, "x")
        print("MOVING Y-AXIS DISTANCE:")
        motor_move(y_location[i], motor2_control, "y")

    # x_motor_move(x_location)
    # y_motor_move(y_location)

    # motor1_control(-40)
    # y_motor_move(y_location)


