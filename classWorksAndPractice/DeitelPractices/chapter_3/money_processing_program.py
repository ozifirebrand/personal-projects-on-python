from decimal import Decimal

# principal = Decimal('1000.00')
# print(principal)
# rate = Decimal('0.05')
# print(rate)
# A person invests $1000 in a savings account yielding 5% interest. Assuming that
# the person leaves all interest on deposit in the account, calculate and display the
# amount of money in the account at the end of each year for 10 years. Use the following
# formula for determining these amounts:
# a = p(1 + r)n
# where
# p is the original amount invested (i.e., the principal),
# r is the annual interest rate,
# n is the number of years and
# a is the amount on deposit at the end of the nth year.
#
principal = Decimal('1000.00')
rate = Decimal('0.05')
for year in range(1, 11):
    amount = principal * (1 + rate) ** year
    print(f'{year:>2} {amount:>10.2f}')
