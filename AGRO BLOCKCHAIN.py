import csv 
import random
def addbooking():
	bookings = []
	
	bookingref = random.randint(0, 100) 
	bookingref = str(bookingref)
	
	print("The file reference:", bookingref) 
	surname = input ("Please enter your surname: ") 
	forename = input ("Please enter your forename: ")
	category = input ("Please enter the category you want to : ") 
	to= input ("to whom u need to transfer:")
	
	bookings.append(bookingref) 
	bookings.append(surname) 
	bookings.append(forename) 
	bookings.append(category) 
	bookings.append (to)
	
	with open("farmer.csv","a", newline='') as csvfile:
	
		writer = csv.writer(csvfile) 
		writer.writerow (bookings)



print ("Welcome to the application")
print ("Select an option below to continue")

for i in range(100):	
		print("Press 1 to transfer the data") 
		print ("Press 2 to search by category ")
		print("press 3 to exit")
		choice = input ("Please select an option from above: ")
		
		
		if choice == "1":
					addbooking ()
				
		elif choice == "2":
				
					print("property\nyeild\nshare\nloan\nincome")
				
		else:
			
					break
