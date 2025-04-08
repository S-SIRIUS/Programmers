# 소트인사이트(손코딩 연습)
data = list(map(int, input()))
for i in range(0, len(data)):
    for j in range(i+1, len(data)):
        if data[i] < data[j]:
            temp = data[j]
            data[j] = data[i]
            data[i] = temp
for i in data:
    print(i,end="")