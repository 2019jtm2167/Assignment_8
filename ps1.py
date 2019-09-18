def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result
#
def Reverse(lst):
    lst.reverse()
    return lst

# List initialization   # Converting to int
bit=int(input("Enter the transmitted bit :"))
count1=0
count0=0

# Output list initialization
output = []

while (bit > 0):
    rem = bit % 10
    bit = int(bit / 10)
    output.append(rem)
print(Reverse(output))
# Printing output
# print(output)
# print(output[2])
i=0
for i in range(0, len(output)):
    if(output[i]==1):
        count1+=1

remen = count1 / 10

if(count1%2==0):
    # print("This Number is Even")
    output.append(1)
    # print(output)
else:
    print(output)
####################################### second code #############################
print("Parity bit data")
print(concatenate_list_data(output))              #
buffer=concatenate_list_data(output)
for i in range(0, len(output)):
    if (output[i] == 0 and output[i+1] == 1 and output[i+2] == 0):
        output.insert(i+3,"0")
print(output)
print("Transmitting data:")
print(concatenate_list_data(output))
buffer=concatenate_list_data(output)+"0101"
print(buffer)