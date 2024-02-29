class BalanceException(
    Exception
):  # Build in Exception class inherited in this BalanceException class
    pass


def checkbalance():
    money = 10000
    withdraw = 9000

    try:
        balance = money - withdraw
        if balance <= 2000:
            raise BalanceException("Insufficiant balance ")
        print(balance)

    except BalanceException as be:
        print(be)


checkbalance()
