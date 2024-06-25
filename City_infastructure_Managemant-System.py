# Task 1

class Vehicle:

    def __init__(self, reg_num, type, owner):
        self.license_plate_number = reg_num
        self.type = type
        self.owner = owner
    
    def update_owner(self, new_owner):
        if self.owner == new_owner:
            return self.owner

car1 = Vehicle("ABC123", "Car", "Ava")
car2 = Vehicle("DEF456", "Bus", "Jake")
car3 = Vehicle("GHI789", "Motorcycle", "Anthony")



print(f" The Current Owner For The '{[car1.type]}' is: {[car1.owner]}")
print(f" The Current Owner For The '{[car2.type]}' is: {[car2.owner]}")
print(f" The Current Owner For The '{[car3.type]}' Is: {[car3.owner]}")
  
car1.update_owner("Jake")
car2.update_owner("Anthony")
car3.update_owner("Ava")

print(f"The New Owner For The '{[car1.type]}' With The License Plate {[car1.license_plate_number]} Is Now: {car2.owner}")
print(f"The New Owner for The '{[car2.type]}' With The License Plate {[car2.license_plate_number]} Is Now: {car3.owner}")
print(f"The New Owner For The '{[car3.type]}' With The License Plate {[car3.license_plate_number]} Is Now: {car1.owner}")










