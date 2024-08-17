from meowbit import *
from robotbit import RobotBit
import random
import time

score = 0
count = 0
deg = 0
min_left_deg = 0
max_right_deg = 0
curr_time = 0
P1 = MeowPin('P1', 'IN')
robot = RobotBit()
sensor.startSchedule()

def on_p1_IRQ_RISING(_):
  global score,count,deg,min_left_deg,max_right_deg,curr_time

  score += 1

# This P1 interrupt does not work in interactive mode, i.e., the Meowbit is connected
# to a PC. To make it work, we can upload the code to Meowbit.
P1.irq(trigger = ExtInt.IRQ_RISING, pull = Pin.PULL_UP, handler = on_p1_IRQ_RISING)


def on_a_pressed():
  global score,count,deg,min_left_deg,max_right_deg,curr_time

  score = 0
  count = 30
  deg = 90
  min_left_deg = 70
  max_right_deg = 110
  curr_time = time.ticks_ms()
  while not count < 1:
    if time.ticks_ms() - curr_time > 1000:
      curr_time = time.ticks_ms()
      count += -1
      deg = random.randint(min_left_deg, max_right_deg)
      # We cannot put `robot.geekServo9g` inside `on_p1_IRQ_RISING()`. If we do that,
      # i.e., put it after `score += 1`, `on_p1_IRQ_RISING()` hangs.
      robot.geekServo9g(1, deg)
    screen.fill(0)
    # The auto-generated code concatenates a string with a number.
    # We manually replace it with string formatting.
    #screen.text('Score: '+str(score),15,30,1,(255, 255, 255))
    #screen.text('Time: '+str(count),15,60,2,(170, 0, 0))
    #screen.text('Position: '+str(deg),15,90,1,(0, 170, 170))
    screen.text('Score: {}'.format(score),15,30,1,(255, 255, 255))
    screen.text('Time: {}'.format(count),15,60,2,(170, 0, 0))
    screen.text('Position: {}'.format(deg),15,90,1,(0, 170, 170))
  buzzer.tone(440, 1)
  screen.fill(0)
  screen.text('Final Score',30,30,1,(0, 170, 170))
  screen.text(score,30,60,3,(255, 255, 255))
  
sensor.btnTrig['a'] = on_a_pressed
