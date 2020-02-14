file1=open('output.txt', 'r')
lines=file1.readlines()
for line in lines:
	print(line.strip())
#	print("Line{}: {}".format(count, line.strip())) 
