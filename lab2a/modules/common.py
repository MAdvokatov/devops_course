def counting_up_to_100(boolean):
	
	if boolean:
		num = 0
		num_max = 100

		while num <= num_max:
			print(num)
			num = num + 2
	elif not boolean:
		num = 1
		num_max = 100
		
		while num < num_max:
			if num % 2 == 1:
				print(num)
			num = num + 1	
