def main():
    stay=0
    paid=[]
    for i in range(3):
        hold=int(input())
        paid.append(hold)
    # print (paid[2])
    LotA=[]
    for i in range(101):
        i=stay
        hold=i
        LotA.append(hold)
    print(type(LotA[0]))
    LotB=[]
    for i in range(101):
        i=stay
        hold=i
        LotB.append(hold)
    # print(LotB)
    LotC=[]
    for i in range(101):
        i=stay
        hold=i
        LotC.append(hold)
    # print(LotC)
    val=1
    num1=int(input())
    num2=int(input())
    for i in range(num1,num2,1):
        i=val
        hold=i
        LotA.append(hold)
    # print(LotA)
    num1=int(input())
    num2=int(input())
    for i in range(num1,num2,1):
        i=val
        hold=i
        LotB.append(hold)
    #print(LotB)
    num1=int(input())
    num2=int(input())
    for i in range(num1,num2,1):
        i=val
        hold=i
        LotC.append(hold)
    #print(LotC)
    amount=0
    for i in range(1,101,1):
        add=LotA+LotB+LotC
        paid=[LotA,LotB,LotC]
        print(type(paid[0]))
        # stay=paid*add
        amount=amount+add
    print(amount)

if __name__ == "__main__":
    main()