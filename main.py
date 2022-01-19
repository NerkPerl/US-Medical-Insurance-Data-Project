import csv

# declaration of variables for future examination
bmi = []
charges = []
region = []

#declaration of counter to insure code isn't ignoring any datapoints as it iterates
counter = 0

#declaration of dictionary to store ages of insured_persons being examined 
ages_dict = {}

#iterates through rows of CSV file and generates a dictionary of ages that meet provided criteria 
with open('insurance.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  age_temp = 0
  for row in reader:
    if row['age'] not in ages_dict and row['sex'] == 'male' and row['smoker'] == 'no' and row['children'] == '0':
      ages_dict[row['age']] = 1
    elif row['age'] in ages_dict and row['sex'] == 'male' and row['smoker'] == 'no' and row['children'] == '0':
      age_counter = ages_dict.get(row['age'])
      age_counter += 1
      ages_dict[row['age']] = age_counter
      #come back to this portion later, it can be done better. 

#print results of compilation of insured ages for visual inspection. then proceed to simple code to return the top ages represented.
print('Ages: Number of insured_persons\n' + str(ages_dict) + '\n')

#declare variables to find most represented ages. Initialize temp_dict as a copy of ages_dict for altering in the following code. 
temp_dict = ages_dict
highest_keys_list = []
#Enter INT value for number of ages you want to include in study.
top_n_ages = 8 

# examines keys/values of temp_dict and finds the top n ages where n = the value of top_n_ages, appends those ages to highest_keys_list.
for i in range(top_n_ages):
  highest_key = max(zip(temp_dict.values(), temp_dict.keys()))[1]
  highest_keys_list.append(highest_key)
  temp_dict.pop(highest_key)


print('The ' + str(top_n_ages) + ' ages with the most insured_persons: \n' + str(highest_keys_list) + '\n')


#input the int value of the age you want to test. following code will convert it to str, search CSV keys for matching age, and pull relevant data to construct dataset. 
age_to_test = 18

#constructs lists to analyze the BMI, REGION, and CHARGES of non-smoker males with no children whose age was input to test. 
with open('insurance.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    if row['sex'] == 'male' and row['smoker'] == 'no' and row['children'] == '0' and row['age'] == str(age_to_test):
      bmi.append(float(row['bmi']))
      charges.append(float(row['charges']))
      region.append(row['region'])
      #counts the number of datapoints added to lists.
      counter+= 1

#constructs a list of lists where each insured_person's region, bmi, and charges are gathered and then sorted by region. 
age_dataset = list(zip(region, bmi, charges))
age_dataset.sort()

#declare variables to examine which regions current age dataset includes. 
ne = 0
nw = 0
se = 0 
sw = 0

#counts datapoints by region and increments region variables. 
for i in range(len(age_dataset)):
  if age_dataset[i][0] == 'northeast':
    ne += 1
  elif age_dataset[i][0] == 'northwest':
    nw += 1
  elif age_dataset[i][0] == 'southeast':
    se += 1
  elif age_dataset[i][0] == 'southwest':
    sw += 1

print('Examining insured ' + str(age_to_test)  + '-year-olds provides ' + str(counter)+" datapoints with the following regional demographics:\nNortheast: " + str(ne) + "\n" + "Northwest: " + str(nw) + "\n" + "Southeast: " + str(se) + "\n" + "Southwest: " + str(sw) + "\n")

for i in range(len(age_dataset)):
  print(str(i) + ': ' + str(age_dataset[i]))
print('\n')

     

