data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('The file has been completely accessed, there is totally', len(data), 'information in the file')

sum_len = 0
for d in data:
	sum_len += len(d)
	print(sum_len)

print('The average length of information is', sum_len/len(data))