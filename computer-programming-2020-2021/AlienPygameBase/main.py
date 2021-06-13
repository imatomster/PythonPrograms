import pgzrun
from random import *
import time

alien = Actor('alien')
WIDTH = 400
HEIGHT = 400
alien.center = (200,200)
score = 0
start_time = time.time()
time_elapsed = 0
game_over = False

def update():
  global time_elapsed, start_time, game_over
  if(game_over == False):
    time_elapsed = int(time.time() - start_time)
  if(time_elapsed >= 10):
    game_over = True
  if(game_over == False):
    alien.left += randint(-15,15)
    if alien.left > WIDTH:
      alien.right = 0
    if alien.right < 0:
      alien.left = WIDTH
    
    alien.top += randint(-15,15)
    if alien.top > HEIGHT:
      alien.bottom = 0
    if alien.bottom < 0:
      alien.top = HEIGHT

def draw():
  global score, time_elapsed
  screen.clear()
  screen.draw.text(f"Score: {score}",topleft = (10,10),fontsize = 32)
  screen.draw.text(f"Time: {time_elapsed}",topright = (390,10),fontsize = 32)
  alien.draw()
  if(game_over == True):
    screen.draw.text('Game Over!', center = (200,200), fontsize = 64)
    alien.center = (200,200)

def on_mouse_down(pos):
  global score
  if(game_over == False):
    if alien.collidepoint(pos):
      score += 1
      set_alien_hurt()
    else:
      score -= 1
        
def set_alien_hurt():
  alien.image = 'alien_hurt'
  clock.schedule_unique(set_alien_normal, 1.0)
    
def set_alien_normal():
  alien.image = 'alien'

pgzrun.go()