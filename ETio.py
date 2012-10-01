#from MainStory import Menu

class Output:
   @classmethod
   def Main(cls,string):
      print(string)
      
class Input:
   @classmethod
   def GetKeypress(cls):
      return raw_input()
   @classmethod
   def GetKeyPressWithPrompt(cls,prompt):
      return raw_input(prompt)
   @classmethod
   def GetKeyPressWithMenu(cls,menu,default_menu):
      choice = raw_input(menu.text + "\n" + default_menu.text + "\nMake a selection(" + ",".join(menu.choices) + "," + ",".join(default_menu.choices) + "): ")
      choice = choice.lower().strip()
      try:
         response = (menu.choices + default_menu.choices).index(choice)
      except ValueError:
         response = -1;
      return response
      