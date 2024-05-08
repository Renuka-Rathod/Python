"""Modify the above question Q1 to allow student to sit if he/she has medical cause. 
Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly. """

medical_cause= input("Do you have a medical cause? (Y/N):")
print(medical_cause)
if medical_cause.upper()=='Y':
    print("allowed")
else:

   if medical_cause.upper()=='N':
      print("not allowed.")
    else:
         print("Invalid input.")