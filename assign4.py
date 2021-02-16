#extract strand from the file
file = open("input", "r")
string = file.read()
identifier = string[:string.index("\n")]
strand = string[string.index("\n"):]
strand = strand.replace('\n',"")

# create sp array using linear time function
sp = [0] * len(strand)
j = 0
i = 1
length = len(strand)

while (i < length):
    # if the strand matchs the current value increment j and
    # store it in sp array at the current index and move to 
    # next letter in strand
    if (strand[i] == strand[j]):
        j += 1
        sp[i] = j
        i += 1
    # occurs if there is no match     
    else:
        # resets j to the index of the prefix that is 
        # after the nucleotides in te prefix we already 
        # know match based on the value of j because it is
        # possible that there is matches to the prefix 
        # within the last match if j is larger than 0
        if (j != 0):
            j = sp[j-1]
            
        # if j is 0 we just simply increment to the 
        # next nucleotide in the strand because 0 
        # is stored as default in the sp array
        else:
            i +=1 

# write to outfile
outfile= open("output","w+")
index = 0

for i in sp[:-1]:
    outfile.write(str(i) + " ")
else: 
    outfile.write(str(sp[-1]))
    
outfile.close()