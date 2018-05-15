from picar import front_wheels
from picar import back_wheels
import time
import picar
picar.setup()
fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
fw.turning_max = 45
forward_speed = 75
backward_speed = 0

def test():
        #forward
        fw.turn_straight()
        bw.forward()
        bw.speed=forward_speed
        time.sleep(1.5)
        bw.speed=backward_speed
        #initial turn
        fw.turn_right()
        time.sleep(0.15)
        bw.backward()
        bw.speed=forward_speed
        time.sleep(0.35)
        bw.speed=backward_speed
        #straight @ angle
        fw.turn_straight()
        bw.backward()
        bw.speed=forward_speed
        time.sleep(0.55)
        bw.speed=backward_speed
        #secondary turn
        fw.turn_left()
        time.sleep(0.15)
        bw.backward()
        bw.speed=forward_speed
        time.sleep(0.55)
        fw.turn_straight()
        time.sleep(0.15)
        bw.backward()
        bw.speed=forward_speed
        time.sleep(0.25)
        bw.speed=backward_speed
        #straighten out
        fw.turn_straight()
        time.sleep(0.05)
        #center
         bw.forward()
        bw.speed=forward_speed
        time.sleep(0.45)
        bw.stop()

def stop():
        bw.stop()
        fw.turn_straight()

try: test()

except KeyboardInterrupt:
	stop()
