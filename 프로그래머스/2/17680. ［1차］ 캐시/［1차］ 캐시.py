from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache=deque([])
    time=0
    
    if cacheSize==0:
        return len(cities) * 5
    else:
        for city in cities:
            if city.lower() in cache:
                time+=1
                cache.remove(city.lower())
                cache.append(city.lower())
            else:
                time+=5
                if len(cache) == cacheSize:
                    cache.popleft()
                cache.append(city.lower())
    return time