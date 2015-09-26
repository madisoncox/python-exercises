import csv
workshop_file = open('./llc-workshop-data.csv')
workshop_data = csv.DictReader(workshop_file)
workshop = workshop_data.next

workshop_count = 0
learn_count= 0
kids_count = 0
girls_count = 0
for line in workshop_data:
    if line['Event Name'].find("Day") > 0:
        learn_count += 1
    if line['Event Name'].find("Kids") > 0:
        kids_count += 1
    if line['Event Name'].find("Girls") > 0:
        girls_count += 1
print("There are " + str(learn_count) + " participating in National Learn to Code Day.")
print("There are " + str(kids_count) + " participating in Kids Coding Events.")
print("There are " + str(girls_count) + " participating in Girls Coding Events.")
print("There are " + (str(girls_count) + str(kids_count)) + " youth participating in National Learn To Code Day.")

