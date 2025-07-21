a = "aaabbcccccaa"
count = 1 #That occurence itself is 1
res = " "
for i in range(len(a)):
    if (i+1 < len(a) and a[i] == a[i+1]):
        count += 1
    else:
        res = res +a[i]
        res = res + str(count)
        count = 1
print(res)