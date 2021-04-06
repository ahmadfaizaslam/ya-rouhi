from functools import total_ordering


class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    """object representation"""

    def __repr__(self):
        return "Account({!r}, {!r})".format(self.owner, self.amount)

    def __str__(self):
        return "Account of {} with starting amount: {}".format(self.owner, self.amount)

    """iteration"""

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]

    def __reversed__(self):
        return self[::-1]

    """Operator Overloading for Comparing Accounts"""

    @total_ordering
    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    """Operator Overloading for Merging Account"""

    def __add__(self, other):
        # owner = "{}&{}".format(self.owner, other.owner)
        # start_amount = self.amount + other.amount
        # acc = Account(owner, start_amount)
        # for t in list(self) + list(other):
        #     acc.add_transaction(t)
        # return acc
        owner = self.owner + " & " + other.owner
        start_amount = self.balance + other.balance
        return Account(owner, start_amount)

    """Callable Python Objects"""

    def __call__(self):
        print("Start amount: {}".format(self.amount))
        print("Transactions: ")
        for transaction in self:
            print(transaction)
        print("\nBalance: {}".format(self.balance))

    """Context Manager Support and the With Statement"""

    def __enter__(self):
        print("ENTER WITH: Making backup of transactions for rollback")
        self._copy_transactions = list(self._transactions)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("EXIT WITH:", end=" ")
        if exc_type:
            self._transactions = self._copy_transactions
            print("Rolling back to previous transactions")
            print("Transaction resulted in {} ({})".format(exc_type.__name__, exc_val))
        else:
            print("Transaction OK")

    def validate_transaction(acc, amount_to_add):
        with acc as a:
            print('Adding {} to account'.format(amount_to_add))
            a.add_transaction(amount_to_add)
            print('New balance would be: {}'.format(a.balance))
            if a.balance < 0:
                raise ValueError('sorry cannot go in debt!')

acc = Account("bob", 10)

print(acc)
print(str(acc))
print(repr(acc))

"""calculate the balance on the account """
print("Account balance before transaction", acc.balance)
[acc.add_transaction(x) for x in (20, 10, -10, 50, -20, 30)]
print("Account balance after transaction", acc.balance)

print("number of transactions ", len(acc))  #
print("list of transactions")
[print(x) for x in acc]


print("Reversed transaction list", list(reversed(acc)))


print("======================================\nsecond account")
acc2 = Account("Tim", 100)
[acc2.add_transaction(x) for x in (20, 40)]
print("Account balance after transaction", acc2.balance)


print("Is acc2 > acc", acc2 > acc)


acc3 = acc2 + acc
print(acc3)


print(acc)