

train_acc = []
test_acc = []

train_loss = []
test_loss = []

with open("output.txt", "r") as f:

	while True:
		line = f.readline()
		if not line:
			break
		tmp = line.strip().split()
		print(tmp)
		if len(tmp)!=0:
			if tmp[0]=='Train':
				train_acc.append(tmp[9])
				train_loss.append(tmp[6])
			if tmp[0]=='Test':
				test_acc.append(tmp[9])
				train_loss.append(tmp[6])

print(train_acc)
print(len(train_acc))