from meowbit import *
from robotbit import RobotBit
from sonar import *
import time

close_angle = 0
open_angle = 0
open_time = 0
dis = 0
meowSonar_P1 = MeowSonar('P1')
robot = RobotBit()


close_angle = 80
open_angle = 30
open_time = -1
robot.geekServo9g(1, close_angle)
screen.fill(0)
screen.text('Trash Can\nClosed',10,55,2,(0, 170, 170))
while True:
  dis = meowSonar_P1.checkdist()
  if dis < 10 and dis > 1:
    robot.geekServo9g(1, open_angle)
    screen.fill(0)
    screen.text('Trash Can\nOpen',10,55,2,(170, 0, 0))
    open_time = time.ticks_ms()
  if open_time > 0 and time.ticks_ms() - open_time > 5000:
    robot.geekServo9g(1, close_angle)
    open_time = -1
    screen.fill(0)
    screen.text('Trash Can\nClosed',10,55,2,(0, 170, 170))
