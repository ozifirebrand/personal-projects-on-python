print('Price of this house in Lekki starts from #7500')
print("How much are you paying first for this house?")
offer = abs(int(input()))

print('Enter your best price for it')
best = int(input())

print('How much more will you like to add to your money?')
increment = abs(int(input()))

offer_accepted = False
while offer <= best:
    if offer >= 7500:
        offer_accepted = True
        print('Your offer of', offer, ' hash been accepted!')
        break
    if offer < 7500:
        print('We are sorry, you don\'t qualify cos of your meagre', offer, 'offer')
