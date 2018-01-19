import os
os.chdir('C:/Users/cschonberg/Desktop/Research/Causal Action (Scott)/CA4')

f = open('concatenation-2016-10-03_133622.csv', 'r')
headerLine = f.readline()

subject_array = []
for i in range(1,33):
    subject_dictionary =  {}
    subject_dictionary['Condition'] = 0
    subject_dictionary['PredHits_total'] = 0
    subject_dictionary['PredHits_1-12'] = 0
    subject_dictionary['PredHits_13-24'] = 0
    subject_dictionary['PredHits_25-36'] = 0
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
    subj_index = int(linearray[len(linearray)-1]) - 1
    subject_array[subj_index]['Condition'] = linearray[2]
    if(linearray[11] != '.'):
        if (linearray[4] == 'TRUE'):
            if (int(linearray[11]) <= 2250):
                subject_array[subj_index]['PredHits_total'] += 1
            
            if (int(linearray[1]) >= 1) and (int(linearray[1]) <= 12) and (int(linearray[11]) <= 2250):
                subject_array[subj_index]['PredHits_1-12'] += 1
            elif (int(linearray[1]) > 12) and (int(linearray[1]) <= 24) and (int(linearray[11]) <= 2250):
                subject_array[subj_index]['PredHits_13-24'] += 1
            elif (int(linearray[1]) > 24) and (int(linearray[1]) <= 36) and (int(linearray[11]) <= 2250):
                subject_array[subj_index]['PredHits_25-36'] += 1
            elif (int(linearray[1]) > 36) and (int(linearray[1]) <= 48) and (int(linearray[11]) <= 2250):
                subject_array[subj_index]['PredHits_37-48'] += 1
        elif (linearray[4] == 'FALSE'):
            if (int(linearray[1]) >= 1) and (int(linearray[1]) <= 12) and (int(linearray[11]) <= 2250):
                subject_array[subj_index]['FP_1-12'] += 1
            elif (int(linearray[1]) > 12) and (int(linearray[1]) <= 24) and (int(linearray[11]) <= 2250):
                subject_array[subj_index]['FP_13-24'] += 1
            elif (int(linearray[1]) > 24) and (int(linearray[1]) <= 36) and (int(linearray[11]) <= 2250):
                subject_array[subj_index]['FP_25-36'] += 1
            elif (int(linearray[1]) > 36) and (int(linearray[1]) <= 48) and (int(linearray[11]) <= 2250):
                subject_array[subj_index]['FP_37-48'] += 1
            
            if (int(linearray[11]) <= 2250):
                subject_array[subj_index]['PredFP_total'] += 1

f.close()

f = open('CA4_processed_blocks.csv', 'w')

writeString = 'Condition,PredHits_total,PredHits_1-12,PredHits_13-24,PredHits_25-36,PredHits_37-48,FP_total,PredFP_total,FP_1-12,FP_13-24,FP_25-36,FP_37-48'
writeString += '\n'
f.write(writeString)

for i in range(1,33):
    writeString = ''
    writeString += str(i)
    keyArray = ['Condition','PredHits_total','PredHits_1-12','PredHits_13-24','PredHits_25-36','PredHits_37-48','FP_total','PredFP_total','FP_1-12','FP_13-24','FP_25-36','FP_37-48']
    for key in keyArray:
        writeString += ','
        writeString += str(subject_array[i-1][key])
    writeString += '\n'
    f.write(writeString)
    
f.close()
    