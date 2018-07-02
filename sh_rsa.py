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
# ethylene_oxide = 
# n_pentane = 
# ethanol = 
# acetone = 
# isopropyl_alcohol = 
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
