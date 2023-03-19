#This is lab 6 by Lornzo Rey

def encode():
	#this is asking for the original 8 digit password)
	OG_encoded=input('Please enter an 8 digit password: ')
	#This is turning that list of strings into integers
	nums_to_int= [int(x) for x in OG_encoded]

	#this is adding 3 to each of them and then using modulus to get remainder
	encoded_nums= []
	for x in nums_to_int:
		if x+3>9:
			encoded_nums.append((x+3)%10)
		else:
			encoded_nums.append(x+3)

	#str_encode is putting it back into strings from integers
	str_encode = ''.join(str(x) for x in encoded_nums)

	print(f'Your encoded Password is: {str_encode}' )
	return str_encode

#str_encode is being returned to be able to run it through the decode function


def decode(encoded_password):
	result = ''
	for c in encoded_password:
		if 3 <= int(c) <= 9:
			result += str(int(c)-3)
		else:
			result += str(int(c)+7)
	return result


def menu(): #this is for the menu
	loop_continue=True
	encoded_password=''
	while loop_continue:
		print('Menu')
		print('-------------')
		print('1. Encode')
		print('2. Decode')
		print('3. Quit')
		print()
		option= int(input('Select a Menu Option: '))
		if option == 1:
			encoded_password=encode()
		if option ==2:
			decoded_password = decode(encoded_password)
			print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
		if option ==3:
			loop_continue=False






def main():
	menu()



if __name__ == "__main__":
	main()