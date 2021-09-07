# Assume that the tax on a restaurant bill is 6.25% and that the
# bill amount is $37.45. Use type Decimal to calculate the bill
# total, then print the result with two digits to the right of the
# decimal point.
from decimal import Decimal
print(f"{Decimal('37.45') * Decimal('1.0625'):.2f}")