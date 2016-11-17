#!/usr/bin/python
import gridgen

class rooms():
  grid_gen=gridgen.grid_gen()
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
    print self.room_number
    self.room_count+=1
    for room,data in self.room_list.iteritems():
      for row in data:
	print " ".join(map(str,row))

  def main(self):
    self.create_room()

if __name__=='__main__':
  demo=rooms()
  demo.main()
  
  ## Displays the generated board with a space in between "."s
#  for room, data in room_list.iteritems():
#    for row in data:
#      print " ".join(map(str,row))
