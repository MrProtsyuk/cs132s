def intToBin(value):
    output = [0] * 9
    for i in range(9):
        if value % 2 == 1:
            output[i] = 1
        else:
            output[i] = 0
        value = value // 2

    # Reverses the output and joins the list of integers into a string
    output = "".join(str(x) for x in output)

    return output

def grid(value, userInput):
    binary = list(binary)
    value = list(value)
    binary.reverse()
    result = []
    for i in range(len(binary)):
        if binary[i] != value[i]:
            result.append("T")
        else:
            result.append("H")
    
    print(f"{"".join(result[:3])}\n{"".join(result[3:6])}\n{"".join(result[6:10])}\n")
    
    

def main():
    userinput = input("Enter a number between 1-9: ")
    value = intToBin(11)
    print(value)
    grid(value, userinput)

main()