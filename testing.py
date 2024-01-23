
def printFile():
    fileReader = open( 'SampleData1.txt','r')
    
    line = fileReader.readline().rstrip('\n')
    
    while line != "im fine, thank you.":
        print(line)
        line = fileReader.readline().rstrip("\n")
        
        
    fileReader.close()

    
printFile()


#thing to copy text from one program to another :DDDD
Reader = open('SampleData1.txt','r')
Writer = open('temp.txt','w')

for line in Reader:
    if line!='OH MAH GAHH':
        Writer.write(line)
