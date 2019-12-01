def rec_alg_amount(monthly_withdraw, remaining, interest, months):
    if months > 360 or remaining < 0:
        return
    new_remaining = (remaining - monthly_withdraw)*interest
    print(f'Month: {months}')
    print(f'\tStarting Amount: {remaining}')
    print(f'\tEnding Amount: {new_remaining}')
    print(f'\tDifference: {monthly_withdraw}')
    new_months = months + 1
    return rec_alg_amount(monthly_withdraw, new_remaining, interest, new_months)

rec_alg_amount(7972.70, 1690000, 1.00327373978, 1)