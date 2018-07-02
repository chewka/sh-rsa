#open a directory
#open each file
#subtract the values from another file
#other file has values in same position
# OR other file is simply all values stored
# IN which the file has the averages of several blanks
#create new file

file = open("test_csv.csv")

master_list = []
for line in file:
	line = line.rstrip('\n').split(',')
	#print(line)
	master_list.append(line)

#print(master_list)



propane = master_list[71]
n_butane = master_list[73]
methanol = master_list[74]
ethylene_oxide = master_list[75]
n_pentane = master_list[76]
ethanol = master_list[77]
acetone = master_list[78]
isopropyl_alcohol = master_list[79]
# acetonitrile = 
# methylene_chloride = 
# n_hexane = 
# ethyl_acetate = 
# benzene = 
# dichloroethane = #problematic
# heptane = 
# trichloroethylene = 
# toluene = 
# chloroform = 
# mp_xylene = #problematic
# o_xylene = 

print(propane)

chemicals = {
	'propane' : propane[3]
}

#create dictionary
#key : value
#chemical : concentration

print(chemicals)

#go through chemicals and subtract from blank values