"""
Sufiaan Shaikh - 1859029

CIS-2348-18349

Coding Problem 2
"""

import datetime

months = {"JANUARY": "1", "FEBRUARY": "2", "MARCH": "3", "APRIL": "4",
               "MAY": "5", "JUNE": "6", "JULY": "7", "AUGUST": "8",
               "SEPTEMBER": "9", "OCTOBER": "10", "NOVEMBER": "11",
               "DECEMBER" : "12"}

file = open("inputDates.txt", "r")
file2 = open("parsedDates.txt", "w")

for lines in file:
    index1 = lines.find(" ")
    
    #print(index1)
    index2 = lines.find(" ", index1 + 1, -1)
    
    #print(index2)
    
    if index1 != -1:
        m = lines[0:index1]
        #print(m)
        
        y = lines[index2 + 1:-1]
        #print(y)
        
        d = lines[index1 + 1: index2 - 1]
        #print(d)
        
        if m.upper() in months:
            num = months[m.upper()]
            
            expected = num + "/" + d + "/" + y
            #print(expected)
            
            output = datetime.datetime(int(y), int(num), int(d))
            today = datetime.datetime.now()
          
            if today >= output:
            
                print(expected)
                file2.write(expected)
                file2.write("\n")
                    
file.close()                        
file2.close()
                                        
                   
            
                            
                        
                
