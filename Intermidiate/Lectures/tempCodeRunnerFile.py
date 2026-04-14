
def FindComplement(num):
    binary_num = bin(num)[2:]
    complement_result = ''
    for bit in binary_num:
        if bit == '1':
            complement_result += '1'
        else:
            complement_result += '0'
            


num_input = int(input("Enter the num :"))
print(f"The complement of {num_input} is : {FindComplement(num_input)}")

