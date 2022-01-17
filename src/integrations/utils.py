
import Transaction
from collections import defaultdict

def get_max_average_withdrawal_account(data):

    # test
    data = [Transaction(1, 2, 1000, 1234), Transaction(1, 8, 1000, 1236), Transaction(6, 9, 1, 1237),
                 Transaction(7, 8, 1, 1238)]

    withdrawals_total = defaultdict(int)
    withdrawals_count = defaultdict(int)

    for transaction in data:
        src_account = transaction.get_src()
        withdrawals_total[src_account] += transaction.get_amount()
        withdrawals_count[src_account] += 1

    max_average_amount = 0
    max_average_account = None

    for account, total in withdrawals_total.items():
        num_withdrawals = withdrawals_count[account]
        average = total / num_withdrawals
        if average > max_average_amount:
            max_average_amount = average
            max_average_account = account

    return [max_average_amount, max_average_account]
















