#!/usr/bin/python
import gridgen

class rooms():
  grid_gen=grid.grid_gen()
  room_list={}

  def __init__(self):
    self.room_count=0
    self.room_number=""
    self.current_room=[]

  def create_room(self):
    room=self.grid_gen.generator()
    self.room_number="room"
    self.room_number+=str(self.room_count)
    self.room_list[self.room_number]=room 
    self.room_count+=1

if __name__=='__main__':
  rooms.create_room()
  
  ## Displays the generated board with a space in between "."s
#  for room, data in room_list.iteritems():
#    for row in data:
#      print " ".join(map(str,row))
