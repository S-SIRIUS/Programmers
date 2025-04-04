# A와B(골드5)
start = input()
end = input()

while len(end) > len(start):
    if end[-1]=='A':
        end = end[0:-1]
    elif end[-1]=='B':
        end = end[0:-1]
        end = list(end)
        end.reverse()
        end = "".join(end)
    else:
        break
if end==start:
    print(1)
else:
    print(0)