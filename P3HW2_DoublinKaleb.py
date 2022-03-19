#CTI-110
#P3HW2-Pizza Order
#Kaleb Doublin
#03/11/2022
def main():
    import math

    students = int(input('Enter the number of students: '))
    people = float(input('Enter the number of people per pizza: '))

    if(people == 1.5 or people == 2 or people == 3):
	    whole_pizzas =  math.ceil(students / people)
	    price = whole_pizzas * 5
	    price = price + (price * 0.06)
	    print('Number of whole pizzas: ', whole_pizzas)
	    print('Price: $', price)
    else:
	    print('Error: Please enter 1.5, 2, or 3')
	    print('Please run program again')

main()


