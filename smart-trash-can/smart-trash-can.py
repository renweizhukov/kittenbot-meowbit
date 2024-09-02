from meowbit import *
from robotbit import RobotBit
from sonar import *
import time

close_angle = 0
open_angle = 0
dis = 0
old_time = 0
meowSonar_P1 = MeowSonar('P1')
robot = RobotBit()


close_angle = 80
open_angle = 20
robot.geekServo9g(1, close_angle)
screen.fill(0)
screen.text('Trash Can',10,55,2,(0, 170, 170))
while True:
  dis = meowSonar_P1.checkdist()
  if dis < 10 and dis > 1:
    robot.geekServo9g(1, open_angle)
    old_time = time.ticks_ms()
  if old_time - time.ticks_ms() > 5000:
    robot.geekServo9g(1, close_angle)
