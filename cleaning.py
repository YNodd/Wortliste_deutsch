
filetoprocess = "basis_wuertlescht_DE.csv"

messylist = []
listtowrite = []
newwordfile = "Wortliste_deutsch.csv"

"""there are in the file:
20501 with parantheses included  (Bsp: 'achtundfünfzigste(r,s)')
19976 with parentheses removed  
18848 when just accepting words (without spaces etc)"""

with open(filetoprocess, "r") as readfile:
    for line in readfile:
        #print(line, end = "")
        messylist.append(line[:-1])  # the last character is an enter \n

#print(messylist[:20])
#print(len(messylist))


# check if there are mistakes in the words or special characters:
for singleword in messylist:
    if not singleword.isalpha():
        #print(singleword)  # there are words with .. or space or -
        # todo: eventuell die Wörter mit "sich" behalten/herausziehen und nur das sich löschen (zB "verirren" aus "sich verirren") - im Moment werden die alle nicht genommen
        pass

#print("verirren" in listtowrite)  # not included


for word in messylist:
    if word.isalpha() and word not in listtowrite:
        listtowrite.append(word)

#print(listtowrite[:20])
print(len(listtowrite))

# commented out to not accidentally change the finished file (when running the program again):
# with open(newwordfile, "a") as writefile:
#     for singleword in listtowrite:
#         if singleword != listtowrite[-1]:
#             #print(singleword)
#             writefile.write(singleword + "," + "\n")
#         else:
#             writefile.write(singleword + ",")  # after the last word should not be an empty row
