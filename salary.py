print("!!! PLEASE INPUT THE FOLLOWING INFORMATION CORRECTLY !!!")
name=input("PLEASE ENTER YOUR NAME: ")
number_hours=int(input("PLEASE ENTER NUMBER OF HOURS WORKED: "))
number_children=int(input("PLEASE ENTER NUMBER OF CHILDREN: ")) 
gender=input("PLEASE ENTER YOUR GENDER M OR F: ")
if gender=='m' or gender=='M':
    if (number_hours<=40):
        gross_pay=500*number_hours
    elif (number_hours>40):
        gross_pay=500*40+(number_hours-40)*1.5
if (number_children>3):
    edu_fund=(number_children-3)*10    
elif (gender=='f' or 'F'):
    if (number_hours<=40):
        gross_pay=550*number_hours
    elif (number_hours>40):
        gross_pay=550*40+(number_hours-40)*1.5
if (number_children>3):
    edu_fund=(number_children-3)*20        
income_tax=gross_pay*0.15
district_tax=gross_pay*0.01
tax=gross_pay*0.025
total_tax=income_tax+district_tax+edu_fund+tax
net_pay=gross_pay-total_tax
print("YOUR NET PAY IS GHC",net_pay)

   
                    
        
    
    
