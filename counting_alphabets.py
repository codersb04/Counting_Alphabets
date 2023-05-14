#Below is one of the question I have been asked for a coding test

""" Instructions to candidate.

1. A basic string compression operation works by counting sequences of repeating characters and stores this as one character and a count.
Given "AABBBCCCD" it should return "A2B3C3D1". 

Sample Input:
AABBBCCCD
ABCDE
KKKKK

Sample Output:
A2B3C3D1
A1B1C1D1E1
K5

2. Consider adding further tests to runTests
3. Implement the function compressString correctly
"""

def compressString(st):
    count = 1
    x=[]
    i=0
    while (i < len(st)):
        for j in range(i,len(st)):
            if j==len(st)-1:
                x.append(st[j])
                x.append(count)
            elif st[j] == st[j+1]:
                count +=1
            elif st[j]!=st[j+1]:
                x.append(st[j])
                x.append(count)
                count = 1
                break
                
        i= j +1

    return ''.join(str(value) for value in x)

def runTests():
    """ Returns True if all tests pass. Otherwise returns False. """
    tests = [["AABBBCCCD", "A2B3C3D1"],
             ["ABCDE", "A1B1C1D1E1"],
             ["KKKKK", "K5"],
             ["AABBBCCCDAA", "A2B3C3D1A2"],
             ["ABCa", "A1B1C1a1"]]

    for test in tests:
        if not (compressString(test[0]) == test[1]):
            return False
    return True

def main():
    if (runTests()):
        print( "Test(s) passed")
    else:
        print( "Test(s) failed")

if __name__ == '__main__':
    main()