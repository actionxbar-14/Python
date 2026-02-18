


                                                # Rent Calculator



# :: INPUT WE NEED FROM THE USER :

# - hostal / flat rent.
# - Amount of food oreder.
# - electricity_spend.
# - charge_per_unit.
# - person living in room / flat.


# :: OUTPUT WE NEED : 

# - Total amount you've to pay per person



rent = int(input("Enter the total Hostal / Flat rent : "))
Food_order = int(input("Enter the total Amount of food order : "))
electricity_spend = int(input("Enter the Electricity_spend :"))
charge_per_unit = int(input("Enter the charge_per_unit :"))
Person_Living = int(input("Enter the total Person living :"))
total_bill = electricity_spend * charge_per_unit

Amount_per_person = ( rent + Food_order + Person_Living + total_bill) // Person_Living

print("Total Amount per person :", Amount_per_person)







