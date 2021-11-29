from motor_control import motor1_setup, motor2_setup, motor1_control , motor2_control

import threading


#running both motors at the same time
# if __name__ == "__main__":
#     # motor1_setup

#     t1 = threading.Thread(target=motor1_control, args=(400, ))
#     t2 = threading.Thread(target=motor2_control, args=(-400, ))

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()

motor1_control(400)
motor2_control(-400)
motor1_control(400)
motor2_control(400)