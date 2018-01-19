import os
os.chdir('C:/Users/cschonberg/Desktop/Research/Causal Action (Scott)')

f = open('CausalAction1_for_SAS.csv', 'r')

subject_array = []
for i in range(1,65):
    subject_dictionary =  {}
#adding subject screwed up columns but good enough
    subject_dictionary['Subject'] = 0
    subject_dictionary['Age'] = 0
    subject_dictionary['Gender'] = 'p'
    subject_dictionary['NumberCondition'] = 0
    subject_dictionary['Hits_total'] = 0
    subject_dictionary['PredHits_total'] = 0
    subject_dictionary['Hits_1-12'] = 0
    subject_dictionary['PredHits_1-12'] = 0
    subject_dictionary['Hits_13-24'] = 0
    subject_dictionary['PredHits_13-24'] = 0
    subject_dictionary['Hits_25-36'] = 0
    subject_dictionary['PredHits_25-36'] = 0
    subject_dictionary['Hits_37-48'] = 0
    subject_dictionary['PredHits_37-48'] = 0
    subject_dictionary['FP_total'] = 0
    subject_dictionary['PredFP_total'] = 0
    subject_dictionary['FP_1-12'] = 0
    subject_dictionary['FP_13-24'] = 0
    subject_dictionary['FP_25-36'] = 0
    subject_dictionary['FP_37-48'] = 0
    subject_array.append(subject_dictionary)
    
for line in f:
    linearray = line.split(',')
    subj_index = int(linearray[0]) - 1
    subject_array[subj_index]['Age'] = int(linearray[2])
    subject_array[subj_index]['Gender'] = linearray[3]
    subject_array[subj_index]['NumberCondition'] = int(linearray[6])
    if (linearray[9] == 'TRUE'):
        if (int(linearray[8]) >= 1) and (int(linearray[8]) <= 12):
            subject_array[subj_index]['Hits_1-12'] += 1
            if(linearray[12] != ''):
                subject_array[subj_index]['PredHits_1-12'] += 1
        elif (int(linearray[8]) > 12) and (int(linearray[8]) <= 24):
            subject_array[subj_index]['Hits_13-24'] += 1
            if(linearray[12] != ''):
                subject_array[subj_index]['PredHits_13-24'] += 1
        elif (int(linearray[8]) > 24) and (int(linearray[8]) <= 36):
            subject_array[subj_index]['Hits_25-36'] += 1
            if(linearray[12] != ''):
                subject_array[subj_index]['PredHits_25-36'] += 1
        elif (int(linearray[8]) > 36) and (int(linearray[8]) <= 48):
            subject_array[subj_index]['Hits_37-48'] += 1
            if(linearray[12] != ''):
                subject_array[subj_index]['PredHits_37-48'] += 1
        subject_array[subj_index]['Hits_total'] += 1
        if(linearray[12] != ''):
            subject_array[subj_index]['PredHits_total'] += 1
    elif (linearray[9] == 'FALSE'):
        if (int(linearray[8]) >= 1) and (int(linearray[8]) <= 12):
            subject_array[subj_index]['FP_1-12'] += 1
        elif (int(linearray[8]) > 12) and (int(linearray[8]) <= 24):
            subject_array[subj_index]['FP_13-24'] += 1
        elif (int(linearray[8]) > 24) and (int(linearray[8]) <= 36):
            subject_array[subj_index]['FP_25-36'] += 1
        elif (int(linearray[8]) > 36) and (int(linearray[8]) <= 48):
            subject_array[subj_index]['FP_37-48'] += 1
        subject_array[subj_index]['FP_total'] += 1
        if(linearray[12] != ''):
            subject_array[subj_index]['PredFP_total'] += 1

f.close()

f = open('CA1_CSprocessed_blocks.csv', 'w')

writeString = 'Subject,Age,Gender,NumberCondition,Hits_total,PredHits_total,Hits_1-12,PredHits_1-12,Hits_13-24,PredHits_13-24,Hits_25-36,PredHits_25-36,Hits_37-48,PredHits_37-48,FP_total,PredFP_total,FP_1-12,FP_13-24,FP_25-36,FP_37-48'
writeString += '\n'
f.write(writeString)

for i in range(0,64):
    writeString = ''
    writeString += str(i+1)
    keyArray = ['Subject','Age','Gender','NumberCondition','Hits_total','PredHits_total','Hits_1-12','PredHits_1-12','Hits_13-24','PredHits_13-24','Hits_25-36','PredHits_25-36','Hits_37-48','PredHits_37-48','FP_total','PredFP_total','FP_1-12','FP_13-24','FP_25-36','FP_37-48']
    for key in keyArray:
        writeString += ','
        writeString += str(subject_array[i][key])
    writeString += '\n'
    f.write(writeString)
    
f.close()
    