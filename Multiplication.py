def userinput():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    numstr = str(num1)
    numstr2 = str(num2)
    main(numstr, numstr2)


def main(num1, num2):
    result = 0
    results = []

    u = 1
    for i in range(0, len(num1)):
        t = 1
        for j in range(0, len(num2)):
            if i == 0 and j == 0:
                results.append(int(num1[-(i + 1):]) * u * int(num2[-(j + 1):]) * t)
            elif i == 0 and j != 0:
                results.append(int(num1[-(i + 1):]) * u * int(num2[-(j + 1):-j]) * t)
            elif i != 0 and j == 0:
                results.append(int(num1[-(i + 1):-i]) * u * int(num2[-(j + 1):]) * t)
            else:
                results.append(int(num1[-(i + 1):-i]) * u * int(num2[-(j + 1):-j]) * t)
            t *= 10
        u *= 10

    for res in range(len(results)):
        result += results[res]
    print(result)


userinput()
