# https://open.kattis.com/problems/kafkaesque\
def main():
    total=1
    check=0
    sig=int(input())
    for i in range(0,sig,1):
        clerk=int(input())
        total, check=answer(clerk,check,total)
        # if check>clerk:
        #     amount=amount+1
        # check=clerk
    print(total)
def answer(clerk,check,total):
        if check>clerk:
            total=total+1
        check=clerk
        return total, check

if __name__ == "__main__":
    main()