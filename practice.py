def int_toBinary(num):
    output = [0] * 9
    for i in range(9):
        if num % 2 == 1:
            output[i] = 1
        else:
            output[i] = 0
        num = num // 2

    # Reverses the output and joins the list of integers into a string
    output = "".join(str(x) for x in output)

    return output

def split_and_list(userInToBin):
    userInToBin.split() 
    binLists = [userInToBin[0:3], userInToBin[3:6], userInToBin[6:10]]
    return binLists

def grid(binLists):
    print()
    for i in range(len(binLists)):
        result = ""
        for j in binLists[i]:
            if j == "0":
                result += "H"
            else:
                result += "T"
        print(result)
    print()

def main():
    endOfLine = "111111111"
    loopy = True
    grid(split_and_list("000000000"))
    while loopy:
        userInput = input("Enter a number between 1-9: ")
        if userInput == "" or int(userInput) > 9:
            print("\nPlease enter a vaild number\n")    
        else: 
            userInToBin = int_toBinary(int(userInput))
            if userInToBin == endOfLine:
                grid(split_and_list(userInToBin))
                print("Goodbye!")
                loopy = False
            else:  
                grid(split_and_list(userInToBin))
                userInToBin = list(userInToBin)
                userInToBin.reverse()
                userInToBin = "".join(str(x) for x in userInToBin)
                print(f"You chose node {userInToBin}")

main()