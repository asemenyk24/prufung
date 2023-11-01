def sum_digits_in_num(number):
	if len(str(number)) > 1:
		res = int(str(number)[0]) + int(str(number)[1])
		sum_digits_in_num(res)
	elif len(str(number)) == 1:
		print(number)
		return number


sum_digits_in_num(98)