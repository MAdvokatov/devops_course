#Task 2.1
print("Вградена Константа", False , 123, "Whatever")
#----------------------------------------

#Task 2.2
A={"Sth" , "Sth else" , "Whatever"}
print(len(A), "equals" , round(3.3))
#----------------------------------------

#Task 2.3
A=3
B=5
if int(A)+int(B)==8:
	print("The sum is 8")
else:
	print("The sum is not 8")
#------------------------------------------

#Task2.4
C = "5"
try:
    print(C/A)
except Exception as e:
    print(e)
finally:
    print("That will always be printed")
#-----------------------------------------

#Task2.5
with open("README.md", "r") as f:
	for line in f:
		for word in line:
			print(word)
#----------------------------------------

#Task2.6
this_is_lambda = lambda first, last: f'Цей код написав: {first} {last}'
print("Це просто функція:", this_is_lambda)
print("Це її виклик:", this_is_lambda('Богдан', 'Бугиль'))



#I understand this as a normal function , just declared on one row instead of this 

def this_is_not_lambda(first_name,last_name):
	return f"code written by: {first_name} {last_name}"
print("Just a function:" , this_is_not_lambda)
print("Not sure what this means", this_is_not_lambda("Mario","Adv"))




