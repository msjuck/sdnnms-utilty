
def file_name(number):
	if number < 10:
		number = "0" + str(number)
	else:
		number = str(number)
	return "./IOrecvtrap_20190529/IOrecvtrap_20190529_part" + number



output = [  open( 'converted_data0.csv', 'w' ),
			open( 'converted_data1.csv', 'w' ),
			open( 'converted_data2.csv', 'w' ),
			open( 'converted_data3.csv', 'w' ),
			open( 'converted_data4.csv', 'w' ),
			open( 'converted_data5.csv', 'w' ),
			open( 'converted_data6.csv', 'w' ),
			open( 'converted_data7.csv', 'w' ),
			open( 'converted_data8.csv', 'w' ),
			open( 'converted_data9.csv', 'w' )
		]


for count in range(1,79,1):
	print(count)
	file = open(file_name(count))
	txt = file.read()
	txt_list = txt.split('#################################################################')
	for chunk in txt_list:
		if "IOrecvtrap" in chunk:
			pass
		#elif "VarBind" in chunk:
		#	pass
		else:
			#print(chunk)
			output[int(count/10)].write("\n")
			row = []
			for line in chunk.split('\n'):
				try:
					#ele = line.split(' = ')[1]
					#print(ele)
					row.append(line.split(' = ')[1].replace(',',' '))
				except:
					pass			
			output[int(count/10)].write(', '.join(row))

for csv in output:
	csv.close()


'''
output = open( 'no_var_bind.txt', 'w' )

for count in range(1,79,1):
	file = open(file_name(count))
	txt = file.read()
	txt_list = txt.split('#################################################################')
	for chunk in txt_list:
		if "IOrecvtrap" in chunk:
			pass
		elif "VarBind" in chunk:
			pass
		else:
			print(chunk)
			output.write("#################################################################")
			for line in chunk.split('\n'):


output.close()


