


f = open("/home/anmol/Downloads/3_2_loot.in", "r")
all_lines = f.readlines()

for i in range(len(all_lines)):
	all_lines[i] = all_lines[i][:-1]

a = all_lines[0].split(" ")
n_items = int(a[0])
backpack_val =  int(a[1])

print all_lines
print n_items
print backpack_val
