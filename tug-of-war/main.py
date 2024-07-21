from meowbit import *
from robotbit import RobotBit

deg = 0
start = 0
robot = RobotBit()


deg = 65
start = 1
robot.geekServo9g(1, deg)
screen.fill((255, 193, 204))
screen.text('Tug\nof\nWar',26,45,2,(255, 255, 255))
while not start == 0:
  if sensor.btnValue('left'):
    deg += -0.02
  if sensor.btnValue('a'):
    deg += 0.02
  if deg < 40 or deg > 90:
    start = 0
  else:
    robot.geekServo9g(1, deg)
buzzer.tone(440, 1)
if deg < 40:
  screen.fill((255, 95, 150))
  screen.text('Left wins!',26,45,3,(255, 255, 255))
else:
  screen.fill((220, 150, 207))
  screen.text('Right wins!',26,45,3,(255, 255, 255))
