def main():
    outputsum = 0
    for i in range(0,1000):
        if(i % 3 == 0):
            outputsum += i
        elif(i % 5 == 0):
            outputsum += i
        else:
            continue
    print(outputsum)

main()
