#!/usr/bin/python
################################################################################
### This generates a dot array with random dimensions based on a fixed range ###
### and is set up as a function to be called by other modules.               ###
### Last edit by Jemuel Pavlic on 3/16/2016 1:34pm                           ###
################################################################################

import numpy
from random import randint

class grid_gen():
  ## Generate random board dimensions
  mapx = randint(5,19)
  mapy = randint(5,19)

  ## Creates a nested (2D) list based on the randomly generated dimensions
  matrix = [["." for x in range(mapx)] for x in range(mapy)]

  ## Store the finished grid here:
  grid=[]

  ## Displays the generated board with a space in between "."s
  for row in matrix:
    ## To do:  make this output to grid so it can be edited:
    print " ".join(map(str,row))
