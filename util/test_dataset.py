with open("../data/camera_event_historic.csv") as input_file:
	row = input_file.readlines()

for i in range(1, len(row)):
	row_data = row[i].strip().split(',')
	if (int(row_data[2]), int(row_data[3])) not in [(1, 2), (2, 3)]:
		print(int(row[2]), int(row[3]))