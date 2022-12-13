from Kafkaesque import ans

def TestAmount():
    assert ans([1,23,18,13,99])==3

if __name__=="__main__":
    TestAmount()