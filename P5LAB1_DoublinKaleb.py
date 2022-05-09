def laps_to_miles(user_laps):
    return user_laps * 0.25

if __name__ == '__main__':
    user_laps = float(input())
    num_miles = laps_to_miles(user_laps)
    print(f'{num_miles:.2f}')
