from src.integrations.transaction import Transaction
from collections import defaultdict

"""
Parses the Gringott's file into Transaction Data format
Return type: defaultdict(list) 

{"batch_id": 
    [Transaction(src, dest, transaction_id, amount),
     Transaction(src, dest, transaction_id, amount),
     ...
    ], 
  ...
}
"""
def parse_helper(filename):
    batches = defaultdict(list)
    transactions = []

    # Opening file
    file = open(filename, 'r')

    current_batch = file.readline()

    while True:
        line = file.readline()
        if not line:
            break

        if "GTTB" in line:
            if len(transactions) > 0:
                batches[current_batch] = transactions
                transactions = []
                current_batch = line
        else:
            transaction = Transaction()
            transaction_id = line
            src = file.readline()
            dest = file.readline()
            amount = file.readline()
            transaction.set_transactionId(transaction_id)
            transaction.set_src(src)
            transaction.set_dest(dest)
            transaction.set_amount(int(amount[3:]))
            transactions.append(transaction)
    # tail case
    batches[current_batch] = transactions

    # Closing files
    file.close()

    return batches




