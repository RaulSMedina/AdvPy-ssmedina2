# https://open.kattis.com/problems/driversdilemma

def main(gallons,leak,distance):
    remain=float(gallons)/2
    total=10000000000
    for i in range(6):
        speed,effi=input().split()
        hours=float(distance)/float(speed)
        num1=hours*float(leak)
        num2=float(distance)/float(effi)
        answer=num1+num2
        if answer<remain:
            real=speed
            total=answer
    if total<remain:
        print("YES", real)
    else:
        print("NO")
def Inputs():
    gallons,leak,distance=input().split()
    main(gallons,leak,distance)

if __name__ == "__main__":
    Inputs()
# I used https://www.math.wsu.edu/kcooper/M300/pythontypes.php to help with this program