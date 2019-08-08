# This code illustrates example of using while loop

i = -1  # initiate variale i
while True:  # loop while True
    # add 1 to the value of i every time we enter the while loop
    i += 1

    # when value of i reaches 20, we break out of the loop
    if(i > 20):
        break

    # print the even values of i <= 20
    # if the value is odd, ignore and continue
    if(i % 2 != 0):
        continue
    print(i)
