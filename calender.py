month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
month_name = ['January','February','March','April','May','June','July','August','September','October','November','December']


def determine_days(year):
	d1 =(year - 1)/4 
	d2 =(year - 1)/100
	d3 =(year - 1)/400
	code = int((year + d1 - d2 + d3)%7)
	return code


def leapyear(year):
	if (year %4 == 0 and year %100 != 0 or year%400 == 0 ):
		month_days[1]=29
		return 1
	else:
		month_days[1]=28
		return 0


def calendar(year,code):
	for x in range(0,12):

		print("\n           ",month_name[x])
		print("Sun  Mon  Tue  Wed  Thu  Fri  Sat ")
		# for i in range(1,1+int(code)*5):
		# 	print("test")
		print("     "*code, end="")
		for i in range(1,1+month_days[x]):
			if(len(str(i)) == 1):
				print(" ", end="")
			print(f" {i}",end="")
			if ((i+code)%7>0):
				print("  ",end="")
			else:
				print()

		print()
		code= ((code + month_days[x])%7)

year=int(input("Enter year: "))
print()
daycode = determine_days(year)
leapyear(year)
calendar(year,daycode)



