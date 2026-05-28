#1)calculate_salary()
#Create a function to calculate employee salary after bonus and tax deduction.
#Inputs:
#basic salary
#bonus percentage
#tax percentage
#Return final salary.

def calculate_salary(salary, bonus_per, tax_per):
    bonus = (bonus_per / 100) * basic_salary
    salary_with_bonus = salary + bonus
    tax = (tax_per / 100) * salary_with_bonus
    final_salary = salary_with_bonus - tax
    return final_salary
result = calculate_salary(50000, 10, 5)
print(result)



#check_wifi_signal()
#Create a function to show WiFi signal strength based on signal percentage.
#Conditions:
#0–30 → Weak
#31–70 → Moderate
#71–100 → Strong
def signal():
    sig = int(input("enter signal strength"))
    if 0<=sig<=30:
        print("weak")
    elif 31<=sig<=70:
        print("moderate")
    else:
        print("strong")
signal()

#movie_rating()
#Create a function that returns movie category based on rating.
#Conditions:
#Above 8 → Excellent
#5–8 → Good
#Below 5 → Average
def movie():
    sui=int(input("enter movie rating"))
    if sui>8:
        print("excellent")
    elif 5<=sui<=8:
        print("good")
    elif sui<5:
        print("average")
movie()


     
    
    
