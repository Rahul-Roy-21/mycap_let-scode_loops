rangeInp = list(map(int, input("Enter Range: ").split()))

positives = []

for num in rangeInp:
    if num>0:
        positives.append(num)

print(positives)