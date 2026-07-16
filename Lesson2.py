def total_calc(bill_amount, tip_perc):
    tip = bill_amount * (tip_perc / 100)
    total = bill_amount + tip
    print("Total amount to pay is :", total)

total_calc(100, 15)
