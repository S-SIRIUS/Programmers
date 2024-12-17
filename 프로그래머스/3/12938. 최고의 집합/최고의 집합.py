def solution(n, s):
    standard = s//n
    if standard==0:
        return [-1]
    else:
        result = [standard] * (n)
        distribution = s%n
        for i in range(0, distribution):
            result[n-(1+i)] += 1

        return result