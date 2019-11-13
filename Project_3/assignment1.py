# EDIT THE FILE WITH YOUR SOLUTION
import re

filename = input('Which text file do you want to use for the puzzle?')
with open(filename, 'r') as files:
    text = files.read()
    sentences = text.replace('\n', ' ').replace('."', '*.').replace('?"', '*.').replace('!"', '*.').replace(',"',
                                                                                                            '*').replace(
        '"', '*')
    sentences = re.split('\.', sentences)[:-1]

namelist = []
nwant = ['Yesterday,', 'Then', 'I', 'Sir', 'Sirs', 'Knaves', 'Knave', 'Knights', 'Knight']
for line in sentences:
    wordlist = line.split()
    for word in wordlist:
        if word.strip('*') not in nwant and list(word)[0].isupper():
            namelist.append(word.strip('*').strip(',').strip('!'))
namelist = sorted(set(namelist))

pattern = "\*(.+)\*"
staments_pairs = {}
for name in namelist:
    staments_pairs[name] = ''
for line in sentences:
    if '*' in line:
        stament = re.findall("\*(.+)\*", line)
        if stament != []:
            for name in namelist:
                if (name in line) & (name not in stament[0]):
                    whosay = name

            if 'I' in stament[0]:
                stament[0] = stament[0].replace('I', whosay)
            staments_pairs[whosay] = stament[0]

for whosay, stament in staments_pairs.items():
    if 'are Knaves' in stament:
        intername = []
        for word in stament.split():
            if word.istitle() and (word not in nwant):
                intername.append(word)
        staments_pairs[whosay] = '(({}&(({})==0))|(~{}&(({})!=0)))'.format(whosay, '+'.join(intername), whosay,
                                                                           '+'.join(intername))

    if 'at least' in stament:
        intername = []
        for word in stament.split():
            if word.istitle() and (word not in nwant):
                intername.append(word)
        staments_pairs[whosay] = '(({}&({}&~{}==1))|(~{}&(~{}==1&{}==1)))'.format(
            whosay, whosay, intername[0], whosay, whosay, intername[0])

    if 'am a Knight' in stament:
        intername = []
        for word in stament.split():
            if word.istitle() and (word not in nwant):
                intername.append(word)
        staments_pairs[whosay] = 'True'

    if 'am a Knave' in stament:
        intername = []
        for word in stament.split():
            if word.istitle() and (word not in nwant):
                intername.append(word)
        staments_pairs[whosay] = 'False'
    if stament == '':
        staments_pairs[whosay] = 'True'

judge = '&'.join(staments_pairs.values())

condition = []
role_pairs = []
if len(namelist) == 2:
    for a1 in [0, 1]:
        locals()[namelist[0]] = a1
        for a2 in [0, 1]:
            locals()[namelist[1]] = a2
            if eval(judge) == 1:
                condition.append([eval(namelist[0]), eval(namelist[1])])

if len(namelist) == 3:
    for a1 in [0, 1]:
        locals()[namelist[0]] = a1
        for a2 in [0, 1]:
            locals()[namelist[1]] = a2
            for a3 in [0, 1]:
                locals()[namelist[2]] = a3
                if eval(judge) == 1:
                    condition.append([eval(namelist[0]), eval(namelist[1]), eval(namelist[2])])

if len(namelist) == 4:
    for a1 in [0, 1]:
        locals()[namelist[0]] = a1
        for a2 in [0, 1]:
            locals()[namelist[1]] = a2
            for a3 in [0, 1]:
                locals()[namelist[2]] = a3
                for a4 in [0, 1]:
                    locals()[namelist[3]] = a4
                    if eval(judge) == 1:
                        condition.append([eval(namelist[0]), eval(namelist[1]), eval(namelist[2]), eval(namelist[3])])

len(condition)
print('The Sirs are: ' + ' '.join(namelist))
if condition == []:
    print('There is no solution.')

if len(condition) == 1:
    print('There is a unique solution:')

    flat_list = sum(condition, [])
    for index in range(len(flat_list)):
        if flat_list[index] == 0:
            flat_list[index] = 'Knave'
        elif flat_list[index] == 1:
            flat_list[index] = 'Knight'
    for i in range(len(namelist)):
        print('Sir {} is a {}.'.format(namelist[i], flat_list[i]))

if len(condition) > 1:
    print('There are {} solutions.'.format(len(condition)))