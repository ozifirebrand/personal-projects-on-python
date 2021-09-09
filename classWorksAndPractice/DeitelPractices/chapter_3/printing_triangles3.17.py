# PRINTING TRIANGLES

for i in range(1, 11):
    print('* ' * i)
print()
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# * * * * * * * *
# * * * * * * * * *
# * * * * * * * * * *


# PRINTING TRIANGLE UPSIDE DOWN

j = 10
while j != 0:
    print('* ' * j)
    j -= 1
print()

# * * * * * * * * * *
# * * * * * * * * *
# * * * * * * * *
# * * * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


# PRINTING TRIANGLE LEFT SIDE UPSIDE DOWN
no_of_rows = 0
no_of_spaces = 0
no_of_asterisks = 10
while no_of_rows != 11:
    print('  ' * no_of_spaces, end='')
    print('* ' * no_of_asterisks, end='')
    print()
    no_of_asterisks -= 1
    no_of_spaces += 1
    no_of_rows += 1
print()
# * * * * * * * * * *
#   * * * * * * * * *
#     * * * * * * * *
#       * * * * * * *
#         * * * * * *
#           * * * * *
#             * * * *
#               * * *
#                 * *
#                   *


# PRINTING TRIANGLE LEFT SIDE BUT UPRIGHT

no_of_rows = 1
no_of_spaces = 9
no_of_asterisks = 1
while no_of_rows != 11:
    print('  ' * no_of_spaces, end='')
    print('* ' * no_of_asterisks, end='')
    no_of_spaces -= 1
    no_of_asterisks += 1
    no_of_rows += 1
    print()
#                  *
#                 * *
#               * * *
#             * * * *
#           * * * * *
#         * * * * * *
#       * * * * * * *
#     * * * * * * * *
#   * * * * * * * * *
# * * * * * * * * * *
