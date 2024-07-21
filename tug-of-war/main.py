from meowbit import *
from robotbit import RobotBit

deg = 0
start = 0
robot = RobotBit()


deg = 65
start = 1
robot.geekServo9g(1, int(deg))
screen.fill((170, 0, 0))
screen.text('Tug\nof\nWar',26,45,2,(255, 255, 255))
while not start == 0:
  if sensor.btnValue('left'):
    deg += -3
  if sensor.btnValue('a'):
    deg += 3
  if deg < 40 or deg > 90:
    start = 0
  else:
    robot.geekServo9g(1, int(deg))
buzzer.tone(440, 1)
if deg < 40:
  screen.fill((0, 0, 170))
  screen.text('Left wins!',26,45,3,(255, 255, 255))
else:
  screen.fill((170, 0, 0))
  screen.text('Right wins!',26,45,3,(255, 255, 255))
