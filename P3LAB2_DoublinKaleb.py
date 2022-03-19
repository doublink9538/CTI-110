service = ('Oil change','Tire rotation','Car wash')
name = ('oil change','tire rotation','car wash')
price = (35,19,7)
auto_service = input('Enter desired auto service:\n')
if auto_service in service:
    pos=service.index(auto_service)
    print('You entered: {}'.format(auto_service))
    print('Cost of {}: ${}'.format(name[pos], price[pos]))
else:
    print('You entered: {}'.format(auto_service))
    print('Error: Requested service is not recognized')
