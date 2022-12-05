inputFile = open('input', 'r')
lines = inputFile.readlines()
inputFile.close()

found = 0

for line in lines:
    line = line.strip()

    bags = line.split(" bags contain ")
    bag_color = bags[0]
    shg_color = 'shiny gold'

    if bag_color == shg_color :
        found += 1
        
    for bag in bags[1].split(","):
        bag_in_bag = bag.strip().replace(".","").replace(" bags","").replace(" bag","")
        print(bag_in_bag)
        if bag_in_bag.find("no other") == -1 :
            bib_count = [int(s) for s in bag_in_bag.split() if s.isdigit()][0]
            bib_color = bag_in_bag[bag_in_bag.find(" ") : len(bag_in_bag)].strip()
            print(bib_color + shg_color)
            if bib_color == shg_color :
                found += bib_count

print(found)
