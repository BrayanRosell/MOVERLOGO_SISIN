import serial

import time

import pygame

from pygame.locals import *

arduino = serial.Serial('COM3',9600)

time.sleep(2)

def main():

  #inicializar el pygame

  pygame.init()

  # crear el formulario

  screen = pygame.display.set_mode((600,400))

  pygame.display.set_caption("Sistemas Inteligentes")

  background_color = (255,255,255)

  MyFont = pygame.font.SysFont("monospace",20)

  color_texto = (0,0,0)
  color_texto2 = (1,1,1)

  milogo = pygame.image.load("milogo.jpg").convert()

  screen.fill(background_color)

  while True:

    valorH = arduino.readline().strip()
    valorV = arduino.readline().strip()
    

    mivalorH = valorH.decode()
    mivalorV = valorV.decode() 
    
    screen.blit(MyFont.render("Valor:"+str(mivalorH)+", "+str(mivalorV),1,color_texto),(215,15))
    screen.blit(MyFont.render("GRUPO 07",1,color_texto),(0,0))
    
    screen.blit(milogo,(int(mivalorH),int(mivalorV)))
    #screen.blit(milogo,(200,int(mivalor)))

    pygame.display.flip()

    screen.fill(background_color)



    for event in pygame.event.get():

      if event.type==pygame.QUIT:

        sys.exit()

if __name__=="__main__":

  main()

arduino.close()
