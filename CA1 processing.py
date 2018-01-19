import os
os.chdir('C:/Users/cschonberg/Desktop/Research/Causal Action (Scott)')

f = open('CausalAction1_for_SAS.csv', 'r')

subject_array = []
for i in range(1,65):
    subject_dictionary =  {}
    subject_dictionary['Age'] = 0
    subject_dictionary['Gender'] = 'p'
    subject_dictionary['NumberCondition'] = 0
    subject_dictionary['Hits_total'] = 0
    subject_dictionary['PredHits_total'] = 0
    subject_dictionary['Hits_10-48'] = 0
    subject_dictionary['Hits_10-30'] = 0
    subject_dictionary['FP_total'] = 0
    subject_dictionary['PredFP_total'] = 0
    subject_dictionary['FP_10-48'] = 0
    subject_dictionary['FP_10-30'] = 0
    subject_array.append(subject_dictionary)
    
for line in f:
    linearray = line.split(',')
    subj_index = int(linearray[0]) - 1
    subject_array[subj_index]['Age'] = int(linearray[2])
    subject_array[subj_index]['Gender'] = linearray[3]
    subject_array[subj_index]['NumberCondition'] = int(linearray[6])
    if (linearray[9] == 'TRUE'):
        if (int(linearray[8]) >= 10):
            if(int(linearray[8]) <= 30):
                subject_array[subj_index]['Hits_10-30'] += 1
            subject_array[subj_index]['Hits_10-48'] += 1
        subject_array[subj_index]['Hits_total'] += 1
        if(linearray[12] != ''):
            subject_array[subj_index]['PredHits_total'] += 1
    elif (linearray[9] == 'FALSE'):
        if (int(linearray[8]) >= 10):
            if(int(linearray[8]) <= 30):
                subject_array[subj_index]['FP_10-30'] += 1
            subject_array[subj_index]['FP_10-48'] += 1
        subject_array[subj_index]['FP_total'] += 1
        if(linearray[12] != ''):
            subject_array[subj_index]['PredFP_total'] += 1

f.close()

f = open('CA1_CSprocessed.csv', 'w')

writeString = 'Subject,Age,Gender,NumberCondition,Hits_total,PredHits_total,Hits_10-48,Hits_10-30,FP_total,PredFP_total,FP_10-48,FP_10-30'
writeString += '\n'
f.write(writeString)

for i in range(0,64):
    writeString = ''
    writeString += str(i+1)
    keyArray = ['Age','Gender','NumberCondition','Hits_total','PredHits_total','Hits_10-48','Hits_10-30','FP_total','PredFP_total','FP_10-48','FP_10-30']
    for key in keyArray:
        writeString += ','
        writeString += str(subject_array[i][key])
    writeString += '\n'
    f.write(writeString)
    
f.close()
    