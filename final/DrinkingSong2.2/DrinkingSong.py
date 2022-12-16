# https://open.kattis.com/problems/drinkingsong

def main(amount,drink):
    for i in range(0,amount,1):
        if amount>2:
            print(f"{amount} bottles of {drink} on the wall, {amount} bottles of {drink}.")
            print(f"Take one down, pass it around, {amount-1} bottles of {drink} on the wall.\n")
            amount=amount-1
        elif amount==2:
            print(f"{amount} bottles of {drink} on the wall, {amount} bottles of {drink}.")
            print(f"Take one down, pass it around, 1 bottle of {drink} on the wall.\n")
            amount=amount-1
        elif amount==1:
            print(f"1 bottle of {drink} on the wall, 1 bottle of {drink}.")
            print(f"Take it down, pass it around, no more bottles of {drink}.\n")

def inputs():
    amount=int(input())
    drink=input()
    main(amount,drink)

if __name__ == "__main__":
    inputs()

# I used https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/ to help me with this problem