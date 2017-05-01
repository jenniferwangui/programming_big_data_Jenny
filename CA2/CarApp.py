
#importing the classes
from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar, Dealership


#declaring the object            
dealership = Dealership()
dealership.create_current_stock()

proceed = 'y'
while proceed == 'y':
    dealership.process_rental()
    proceed = raw_input('continue on rental or enter N for return\n').lower()
   
proceed = 'y'
while proceed == 'y':
    dealership.process_returnCar()
    proceed = raw_input('continue? Y/N \n').lower()
    
    
print 'Thank you for using our services'

