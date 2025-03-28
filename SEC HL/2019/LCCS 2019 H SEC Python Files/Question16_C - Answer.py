# Question 16(c)
# Examination Number:

bmi_values = [24, 19, 33, 35, 27, 18, 15, 33, 35, 23, 32, 23]
bmi_values.sort()
underweight_c = 0
normal_c = 0
overweight_c = 0
obese_c = 0


for i in bmi_values:
    if i < 18.5: 
        underweight_c+=1
    elif i >=18.5 and i <=25.9:
        normal_c +=1
    elif i >=25 and i <=29.9:
        overweight_c +=1
    else:
        obese_c +=1
        
print(f'Obese: {obese_c}')
print(f'Largest: {max(bmi_values)}')
smaxval = 0
for i in range(len(bmi_values)):
    if bmi_values[i] == max(bmi_values):
        continue
    if bmi_values[i] > smaxval:
        smaxval = bmi_values[i]
    elif bmi_values[i] <smaxval:
        continue
    else:
        continue
print(f'Second Largest: {smaxval}')
newlist = []
for i in range(len(bmi_values)):
    if bmi_values[i] not in newlist:
        newlist.append(bmi_values[i])
    else:
        continue
newlist.sort()
newlist.reverse()
print(newlist)

def find_nth_largest(n, list_of_values):
    return list_of_values[n-1]
        
    
print(find_nth_largest(3, newlist))