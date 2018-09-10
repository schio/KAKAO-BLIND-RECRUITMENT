def solution(cacheSize, cities):
    runtime = 0
    cache =[None] * cacheSize

    if cacheSize==0:
        return len(cities)*5

    cities=map(str.lower,cities)

    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.append(city)
            runtime += 1 #hit

        else:
            runtime += 5 #miss
            if len(cache)==cacheSize:
                del cache[0]    
            cache.append(city)

    return runtime