## Arvind's Insight H1B Project
### Table of Contents
1. [Problem](README.md#problem)
2. [Approach](README.md#approach)
3. [Testing](README.md#testing)
4. [Remarks](README.md#remarks)
### Problem 
A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

As a data engineer, you are asked to create a mechanism to analyze past years data, specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

Your code should be modular and reusable for future. If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) and puts it in the `input` directory, running the `run.sh` script should produce the results in the `output` folder without needing to change the code.

### Approach
Following the problem statement, the code takes in one csv file as input from the /input folder and returns two text files to the output folder with the required file name and structure.

#### Variable Defenitions
`filename` defaults to **r"./input/h1b_input.csv"** due to the folder structure of the problem.  
`fileAsList` holds each row of records in the input file as a list element.  
`colNames` column names of records in the file.  
`numCertified` number of certified applications in the file.  
`stIndex`, `nameIndex`, `stateIndex` index number of the columns corresponding to *Status*, *Occupation Name* and *Worksite State*  
`stateDict` and `socNameDict` key value mapped pair of State/Occupations and the number of certified cases for each key.  
`N` indicator of top N statistics for occupations and states. 10 within the scope of the problem.  
`sortedOccDict` List of 3 member tuples where each tuple contains Occupation Name, number of certified applications and percentage of overall certified applications.  
`sortedStateDict` List of 3 member tuples where each tuple contains State, number of certified applications and percentage of overall certified applications.  

#### Fucntion Defentions
`h1b_counting` main function.  
`trueSorted` helper function that takes the dictionary of all State/Occupations and number in each and returns a list of 3 element tuples sorted by value and then by alphabet if the values are the same.  
`outputWrite` helper function that takes the header for the specific output file, the path to save it in and the list of 3 element tuples to write to the file.  

#### Program Flow
The program reads in the input file from the input folder, loops through and save each row as a list of lists. The column names are then extracted from the list and compared against the required measures of `STATUS`, `SOC CODE` and `WORKSITE STATE` to return the column index of the records.

The count of each occupation and state that are certified are then mapped to a dictionary as a key value pair.  
The helper function `trueSort` is now called. trueSort takes a dictionary input. It first strips the *""* around the keys in the dictionary to facilitate error free sorting. The cleaned dictionary is initially sorted into a list of 2 element tuples by descending order of values upto the top 10 records. The `lenUniqe` and `lenAll` variables capture the length of the unique values and total length of the sorted list.  
If there are multiple keys with the same value, trueSorted now sorts the entire list by alphabetical order and then loops through each tuple with the same value and sorts them by alphabetical order and thus modifies the sorted list. If all values are unique the sorted list is not modified.  

trueSort now returns the sorted list with a mutated third variable which is the percentage of certified applications compared to the overall.  

Finally `outputWrite` is called to take the list returned by trueSort and print them to a file.  

#### Assumed Pre-conditions
* Input is a single file that is named h1b_input.csv placed in the input folder
* Only two output files of the specified name are to be generated.
* The empty output folder exists before the program is executed.

### Testing
The default tests provided with the `h1b_statistics` repo have been implemented and the current output folder contains the files that are the output of the test file. The function has been tested to work on the datastes provides on the Drive folder as well.
### Remarks
The program can be exented to a modular approach by changing the top N statistics required. New variables can also be defined for other factors like the name of the company that applied. It can also be extended to let the program sequentially take in input files for each year and genrate output files for the respective years. The code has passed the test provided in the `h1b_statistics` repo.
