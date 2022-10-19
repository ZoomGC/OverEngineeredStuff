# THIS CODE DOES NOT WORK AS OF NOW... WIP

def main(num1, num2):
    result = 0
    results = []

    if num2 == 0:
        print("1")
        quit()
    elif num2 == 1:
        print(num1)
        quit()
    else:
        num2 = str(int(num2) - 1)

    for k in range(1, int(num2)+1):
        print("num1", num1, "num2", num2)
        print(k)
        u = 1
        for i in range(0, len(num1)):
            t = 1
            for j in range(0, len(num1)):
                if i == 0 and j == 0:
                    results.append(int(num1[-(i + 1):]) * u * int(num1[-(j + 1):]) * t * k)
                elif i == 0 and j != 0:
                    results.append(int(num1[-(i + 1):]) * u * int(num1[-(j + 1):-j]) * t * k)
                elif i != 0 and j == 0:
                    results.append(int(num1[-(i + 1):-i]) * u * int(num1[-(j + 1):]) * t * k)
                else:
                    results.append(int(num1[-(i + 1):-i]) * u * int(num1[-(j + 1):-j]) * t * k)
                print(results)
                t *= 10
            u *= 10

    for res in range(len(results)):
        result += results[res]
    print(result)


def userinput():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    main(str(num1), str(num2))


userinput()
