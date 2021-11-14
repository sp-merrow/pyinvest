from os import system, name
clear = lambda: system('cls' if name == 'nt' else 'clear') # OS agnostic clear function

yearlyGrowth = 0.2309 # Average yearly growth rate of asset, expressed as a decimal percentage
dividend = 5.66 # Dollar amount of dividend, set to 0 if no dividend
starting = 92.95 # Initial investment
invested = starting
investPerMonth = 50.00 # Amount of your own money you are investing into this account per month
sharePrice = 467.27 # Current share price of asset
years = int(input('Enter number of years until payout (must be a WHOLE NUMBER): '))
years = years*12
payouts = []

for i in range(1, years+1):
    sharePrice += sharePrice*yearlyGrowth
    invested += investPerMonth
    shares = invested/sharePrice

    if i % 12 == 0:
        invested += (invested * yearlyGrowth)
        invested += (dividend * shares)
        payouts.append( f'Account total after {int(i/12)} year(s): ${round(invested, 2)}' )

clear()
print(f'Starting account value: ${round(starting, 2)}')
print(f'Total in account after {int(years/12)} year(s): ${round(invested, 2)}')
conf = input('\nShow yearly account values? (y/n): ')
if conf == 'y':
    print('\n')
    for p in payouts:
        print(p)

input('\n\nPress enter to exit.')