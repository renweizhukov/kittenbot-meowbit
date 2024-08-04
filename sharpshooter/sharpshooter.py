from meowbit import *
import time

score = 0
count = 0
curr_time = 0
P1 = MeowPin('P1', 'IN')
sensor.startSchedule()

def on_p1_IRQ_RISING(_):
  global score,count,curr_time

  score += 1

# This P1 interrupt does not work in interactive mode, i.e., the Meowbit is connected
# to a PC. To make it work, we can upload the code to Meowbit.
P1.irq(trigger = ExtInt.IRQ_RISING, pull = Pin.PULL_UP, handler = on_p1_IRQ_RISING)


def on_a_pressed():
  global score,count,curr_time

  score = 0
  count = 30
  curr_time = time.ticks_ms()
  while not count < 1:
    if time.ticks_ms() - curr_time > 1000:
      curr_time = time.ticks_ms()
      count += -1
    screen.fill(0)
    screen.text(score,60,30,2,(170, 0, 0))
    screen.text(count,60,60,3,(170, 0, 0))
  buzzer.tone(440, 1)
  screen.fill(0)
  screen.text('Final Score',5,10,1,(0, 170, 170))
  screen.text(score,30,40,3,(170, 0, 0))
  
sensor.btnTrig['a'] = on_a_pressed

