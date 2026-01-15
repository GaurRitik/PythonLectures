with open("sample.txt", 'r') as file:
    found=0
    countLine=0

    while(found==0):
        line = file.readline()
        countLine += 1
        if 'Python' in line:
            found=1
            print("Found the target string!")
            break
    print(countLine)