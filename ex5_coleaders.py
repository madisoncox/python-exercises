import csv
chapters_file = open('./llc-chapters.csv') #open the book
chapters_data = csv.DictReader(chapters_file) #organize in csv (how to read the book)
chapter=chapters_data.next() #tells computer to read CSV data line by line

#for line in chapters_data:
    #print(line.next)
   # if line['City'] == "Ottawa":
     #   print line

    #if line['Province'] == "AB":
      #  print line

    #if line['Chapter Lead(s)'] == "Nancy & Cassie":
       # print line

    #if line ['City'] == "Ottawa":
        #print("Thank you " + line['Chapter Lead(s)'])
        #print line['Chapter Lead(s)']


chapters_count = 0
chapters_with_colead = 0
for line in chapters_data:
    if line['Chapter Lead(s)'].find("&")>0:
        print(line['Chapter Lead(s)'] + " are co-leads.")
        chapters_with_colead += 1
    chapters_count += 1
print("There are " + str(chapters_count) + " chapters.")
print("There are " + str(chapters_with_colead) + " chapters with co-lead.")


