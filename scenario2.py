
file = open('file.txt')

phone = "+8197753"

for line in file:
    line = line.strip().split(',')[0]
    if term == line[0]:             # <--- You can also stay with "if term in line:" if you doesn't care which field the "model" is. 
    print(line)
file.close()
