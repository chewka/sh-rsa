from sys import argv
#open a directory
#open each file
#subtract the values from another file
#other file has values in same position
# OR other file is simply all values stored
# IN which the file has the averages of several blanks
#create new file

#python3 sh_rsa.py data_file.txt blank_file.txt > test_output2.txt

#open the customer file and save variables
def create_list(filename):
	file = open(filename)

	master_list = []
	for line in file:
		line = line.rstrip('\n').split('\t')
		#print(line)
		master_list.append(line)

	#print(master_list)


	propane = master_list[71]
	n_butane = master_list[72]
	methanol = master_list[73]
	ethylene_oxide = master_list[74]
	n_pentane = master_list[75]
	ethanol = master_list[76]
	acetone = master_list[77]
	isopropyl_alcohol = master_list[78]
	acetonitrile = master_list[79]
	methylene_chloride = master_list[80]
	n_hexane = master_list[82]
	ethyl_acetate = master_list[83]
	benzene = master_list[84]
	dichloroethane = master_list[85] #problematic
	heptane = master_list[86]
	trichloroethylene = master_list[87]
	toluene = master_list[88]
	chloroform = master_list[89]
	mp_xylene = master_list[90] #problematic
	o_xylene = master_list[91]

	#print(propane)

	chemicals = {
		propane[1] : propane[11],
		n_butane[1] : n_butane[11],
		methanol[1] : methanol[11],
		ethylene_oxide[1] : ethylene_oxide[11],
		n_pentane[1] : n_pentane[11],
		ethanol[1] : ethanol[11],
		acetone[1] : acetone[11],
		isopropyl_alcohol[1] : isopropyl_alcohol[11],
		acetonitrile[1] : acetonitrile[11],
		methylene_chloride[1] : methylene_chloride[11],
		n_hexane[1] : n_hexane[11],
		ethyl_acetate[1] : ethyl_acetate[11],
		benzene[1] : benzene[11],
		dichloroethane[1] : dichloroethane[11],
		heptane[1] : heptane[11],
		trichloroethylene[1] : trichloroethylene[11],
		toluene[1] : toluene[11],
		chloroform[1] : chloroform[11],
		mp_xylene[1] : mp_xylene[11],
		o_xylene[1] : o_xylene[11]
	}


	#for analyte in chemicals:
		#print(chemicals[analyte])

		# if chemicals[analyte] == '':
		# 	chemicals[analyte] == '0'


	#create dictionary
	#key : value
	#chemical : concentration

	return(chemicals)

	#create blank file variables

	#go through chemicals and subtract from blank values

data_file = argv[1]
blank_text = argv[2]

customer_sample = create_list(data_file)
#print(customer_sample)

method_blank = create_list(blank_text)
#print(method_blank)

subtracted_values = {}

for item in customer_sample:
	if customer_sample[item] == '' or method_blank[item] == '':
		continue
	subtracted_values[item] = float(customer_sample[item]) - float(method_blank[item])

#print(subtracted_values)


def create_txt_file(subtracted_values, filename):
	file = open(filename)

	final_list = []
	for line in file:
		line = line.rstrip('\n').split('\t')
		if len(line) > 11 and line[1] in subtracted_values:
			#we have a concentration we want to overwrite
			line[11] = str(subtracted_values[line[1]])
			if line[11] < 0:
				line[11] = - line[11]
			

		final_list.append(line)

	#print(final_list)


	for line in final_list:
		print(('\t').join(line))


create_txt_file(subtracted_values, data_file)
