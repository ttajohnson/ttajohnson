"""
Make Change

"""

def make_change():
    dollar_amount = float(input("Enter a dollar amount: "))

    pennies = int(dollar_amount * 100)
    quarters = pennies // 25
    dimes = (pennies - quarters * 25) // 10
    nickels = ((pennies - quarters * 25) - (dimes * 10)) //5
    final_pennies = ((pennies - quarters * 25) - (dimes * 10)) % 5


    print(f'{quarters} quarters, {dimes} dimes, {nickels} nickels, {final_pennies} pennies.')

make_change()




