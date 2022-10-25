def format_dates(dates):
	for item in dates:
		if item[0:4].isdigit():
			print(''.join(filter(str.isdigit, item)))
		else:
			formated = ''.join(filter(str.isdigit, item))
			day = formated[0:2]
			month = formated[2:4]
			year = formated[4:8]
			print(year + month +day)

dates = ['20220802', '2022/08/03', '04/08/2022', '05.08.2022', '2022.08.06']
format_dates(dates)

#will work without 02082022 as I don't know how to recognize its format