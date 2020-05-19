purchase = float(input('What is the total of the purchase? £'))
option = int(input('''Choose between the following payment options
[1] Cash - Full payment
[2] Card - Full payment
[3] Card - 2x
[4] Card - 3x plus
Enter you option? '''))

if option == 1:
    payment = purchase - (purchase * .10)
    print(f'The total with 10% of discount will be £{payment:.2f}')
elif option == 2:
    payment = purchase - (purchase *.05)
    print(f'The total with 5% of discount will be £{payment:.2f}')
elif option == 3:
    payment = purchase
    installment = purchase / 2
    print(f'Your total will be £{payment:.2f} paid in 2 x of £{installment:.2f}')
elif option == 4:
    cardpay = int(input('How many times you want to split the payments? '))
    payment = purchase + (purchase * .20)
    installment = payment / cardpay
    print(f'Your purchase of £{purchase:.2f} will be split in {cardpay}x of £{installment:.2f} \nThe purchase total with interest will be £{payment:.2f}')

