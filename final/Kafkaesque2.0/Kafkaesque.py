import sys
def main():
    amount=1
    check=0
    #print("Enter the amount of signatures needed")
    sig=int(input())
    for i in range(0,sig,1):
        #print("Enter the numbers of the clerk's desk")
        clerk=int(input())
        if check>clerk:
            amount=amount+1
        check=clerk
    print(amount)
    #print("You will have to go though the line", amount, "times")
# def ans(clerk):
#     amount=1
#     check=0
#     if check>clerk:
#         amount=amount+1
#     check=clerk
#     return amount
# def test():
#     assert ans([1,23,18,13,99])==5

if __name__ == "__main__":
    main()