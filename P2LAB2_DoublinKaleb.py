current_price = int(input())
last_months_price = int(input())
change = current_price - last_months_price
mortgage = (current_price * 0.051) / 12
print('This house is $' + str(current_price) +'. The change is $' + str(change) + ' since last month.')
print('The estimated monthly mortgage is ${:.2f}.'.format(mortgage))
