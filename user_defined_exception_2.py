class BalanceException(Exception):
    pass


def checkalance():
    money = 10000
    withdraw = 5000
    balance = money - withdraw

    if balance <= 9000:
        raise BalanceException("Insufficient Balance")
    print(balance)


try:
    checkalance()

except BalanceException as be:
    print(be)
