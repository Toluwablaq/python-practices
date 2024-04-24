import time
class cylinder:
     def __init__(self, gas,burner):
          self.burner=burner
          self.gas=gas
    
     def gas_exhuast(self):
          count=0
          if(self.burner<=2):
               while self.gas>0:
                    t_time=time.sleep(.02)
                    self.gas -=0.02
                    print(self.gas)
                    count+=0.02
          print(count)
          
first_cook = cylinder(5,2)
first_cook.gas_exhuast()


























start=time.time()              
gas=8              
while gas>0:
     current=(time.time()/1000)%60
     gas -=0.02
     #print(gas)
     t_time=time.sleep(0.01)
     
#print(current)

     
