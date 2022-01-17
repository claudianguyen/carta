class Transaction:

    def __init__(self, src="", dest="", amount=0, transaction_id=""):
        self.src = src
        self.dest = dest
        self.amount = amount
        self.transactionId = transaction_id

    # getter method
    def get_src(self):
        return self.src

    # setter method
    def set_src(self, x):
        self.src = x

    # getter method
    def get_dest(self):
        return self.dest

    # setter method
    def set_dest(self, x):
        self.dest = x

    # getter method
    def get_amount(self):
        return self.amount

    # setter method
    def set_amount(self, x):
        self.amount = x

    # getter method
    def get_transactionId(self):
        return self.transactionId

    # setter method
    def set_transactionId(self, x):
        self.transactionId = x
