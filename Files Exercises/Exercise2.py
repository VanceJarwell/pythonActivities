fileName = input("Enter file name: ")
if len(fileName) == 0:
    fileName = 'mbox-short.txt'
file = open(fileName)
counter = 0
total = 0
answer = 0
for line in file:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    counter = counter + 1
    num = float(line[21:])
    total = num + total
answer = total / counter
print("Average spam confidence:", answer)
