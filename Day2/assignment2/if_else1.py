"""A student will not be allowed to sit in exam 
if his/her attendence is less than 75%.  
Take following input from user Number of classes held 
Number of classes attended. And print percentage of class 
attended Is student is allowed to sit in exam or not."""

total_class=int(input("Total no. of classes:"))
att_class=int(input("Total attended classes:"))
print(total_class,att_class)
per_att=(att_class/total_class)*100
print("percentage of class attended:->",per_att)
if(per_att>75):
    print("Allowed for exam.")
else:
    print("Not allowed for exam.")
