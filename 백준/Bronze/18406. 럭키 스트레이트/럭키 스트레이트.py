# 럭키스트레이트(브론즈2)
s = list(input())
left = s[0:len(s)//2]
right = s[len(s)//2:len(s)]
left_sum=0
right_sum=0
for i in range(0, len(s)//2):
    left_sum+=int(left[i])
    right_sum+=int(right[i])

if left_sum==right_sum:
    print("LUCKY")
else:
    print("READY")