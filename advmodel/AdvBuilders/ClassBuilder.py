# ClassBuilder creates an instance of a Class object given a data source
from advmodel.AdvBuilders import AbstractBuilder

from advmodel.AdvDataObjects import Class

class ClassBuilder(AbstractBuilder):
   def Build(self):
      result = Class
