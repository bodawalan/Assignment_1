def max_string():
	str1=input("Enter the string\t")
	str2=input("enter the string\t")

	if len(str1) > len(str2):
		print ("max length of string is {}".format(str1))
	elif len(str1) == len(str2):
		print ("length of both strind is same")
		print ([str1])
		print ([str2])
	else:
		print ("max length of string is {}".format(str2))

max_string()
