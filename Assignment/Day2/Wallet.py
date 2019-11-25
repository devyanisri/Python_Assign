
def wallet(initial):
    balance=initial
    def deposit(amt):
        nonlocal balance
        balance=balance+amt-balance1()
    def spending(amt):
        nonlocal balance
        if(balance<0):
            print("insufficient balance")
        else:
            balance=balance-amt+balance1()
            print("current balance is:",balance)
    li=[deposit,spending]
    return li


def wallet1(initial1):
    balance1=initial1
    def deposit1(amt1):
        nonlocal balance1
        balance1=balance1+amt1-balance()
    def spending1(amt1):
        if(balance1<0):
            print("insufficient funds")
        else:
            balance1=balance1+amt1-balance()
            print("current balance of wallet1 is:",balance1)
    li1=[deposit1,spending1]
out=wallet(1000)
out[0](2000)
out[1](200)
out1=wallet1(2000)
out1[0](1000)
out1[1](300)








