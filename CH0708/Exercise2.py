str = 'X-DSPAM-Confidence: 0.8475'

start = str.find(':')
end = len(str)


number = str[start+1:end]
fpnumber = float(number)

print(fpnumber)
