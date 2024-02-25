class MyList:

  def __init__(self):
    self.size=1
    self.n=0
    #create a C type array with size = self.size
    self.A=self.__make_array(self.size)

  def __len__(self):
    return self.n
  

  def append(self,item):
    if self.n==self.size:
      self.__resize(self.size*2)

      #resize
    self.A[self.n]=item
    self.n=self.n+1
    
  def __resize(self,new_capacity):
    #create a new array with new capacity
    B=self.__make_array(new_capacity)
    self.size=new_capacity



  def __make_array(self,capacity):
     #creates a c type array(static,referential) with size capacity
     return (capacity*ctypes.py_object)()
