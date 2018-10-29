def h1b_counting(filename,N=10):
    fileAsList = [] #Defining an empty list to store each record as a list element
    with open(filename, newline='', encoding="utf8") as file:
        for row in file:
            row = row.strip().split(';')
            fileAsList.append(row)
    #Gathering colum names in a single variable to index necessary variables
    colNames = fileAsList[0]
    numCertified = 0 # Variable capturing the number of certified across all records.
    #Index of status in the file
    stIndex = colNames.index([i for i in colNames if "STATUS" in i][0])
    #Index of the Occupation name in the file
    nameIndex = colNames.index([i for i in colNames if "SOC_NAME" in i][0])
    #Index of the State of work in the file
    stateIndex = colNames.index([i for i in colNames if "WORK" in i and "STATE" in i][0])
    stateDict = {} #Storing the number of times a certified application is in a particular state
    socNameDict = {} #Storing the name of the Occupation name associated with the code
    #Looping through each record, stopping at the previously generated indices
    #and adding elements to the empty dictionaries
    for row in fileAsList[1:]:
        if row[stIndex] == "CERTIFIED":
            numCertified += 1
            if (row[stateIndex]) in stateDict.keys():
                stateDict[(row[stateIndex])] += 1
            else:
                stateDict[row[stateIndex]] = 1
            if (row[nameIndex]) in socNameDict.keys():
                socNameDict[(row[nameIndex])] += 1
            else:
                socNameDict[row[nameIndex]] = 1
    def trueSorted(dictIn):
        """
        True sorted takes as arguments a dictionary with values representing the 
        number of occurences of the Key in the data set for the top N items
        and it returns a list of tuples with three elements of (Key,Value,Percentage of overall)
        and they are sorted by value first and by alphabetical order if the values are the same
        """
        #Cleans the dictionary by stripping additional quotation marks in the keys
        dictIn = {key.strip('\"'): item for key, item in dictIn.items()}
        #Sorting the input dictionary by value
        sortedDictIn = sorted(((value,key) for (key,value) in dictIn.items()), reverse = True)[:N]
        #Returning a value for length of all unique values in the value of the dict
        lenUnique = len(list(set([elem[0] for elem in sortedDictIn])))
        #Variable defenitions to count the number of unique occurences
        a = list(dictIn.values())
        seta = set(a)
        b = [a.count(el) for el in seta]
        a = list(seta)
        #Overall length of the dict. Will be N-1 due to our inputs.
        lenAll = N
        #Once the dictionay is value sorted it is again sorted by key alphabetical order
        
        #List of the number of equal value items to sort.
        #The items with the smalles values is in alphabetical order
        k = [k for k in b[::-1]]            
        tC = 0 #Index variable to loop through each set of values.
        if lenUnique < lenAll: #Additional sorting based on more than one pair having the same value.
            sortedDictIn = sorted(sortedDictIn, key = lambda x: x[1], reverse = False)
            for elem in k[:-1]:
                for i in range(tC,tC+elem):
                    o = sortedDictIn.index(max(sortedDictIn[i:]))
                    sortedDictIn.insert(tC,sortedDictIn[o])
                    del sortedDictIn[o+1]
                tC += elem        
        return [(i[1],i[0], round((i[0]/numCertified)*100,1)) for i in sortedDictIn]
    
    def outputWrite(header, path,dictIn):
        """
        Takes in the header for the output file and the path to save and the
        values to write into it and write the output file
        """
        outFile = open(path,'w')
        outFile.write(header)
        for row in dictIn:
            outFile.write(str(row[0])+';' + str(row[1])+';'+str(row[2])+'%'+'\n')
        outFile.close()
        
    sortedOccDict = trueSorted(socNameDict)
    sortedStateDict = trueSorted(stateDict)
    #Header and output path defenitions
    occOutPut = r"./output/top_10_occupations.txt"
    occHeader = "TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE" +"\n"
    outputWrite(occHeader,occOutPut,sortedOccDict)
    stateOutput = r"./output/top_10_states.txt"
    stateHeader = "TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE"+"\n"
    outputWrite(stateHeader,stateOutput,sortedStateDict)



if __name__ =='__main__':
    filename = r"./input/h1b_input.csv"
    h1b_counting(filename)
    