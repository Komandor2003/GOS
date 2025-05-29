import pandas as pd
import random 

def get_random ():
    randomReport = random.sample(range(1, 10), 4) 
    randomSales = random.sample(range(100, 1000), 4) 
    result = [] 
    for i in range(len(randomReport)): 
        result.append([randomReport[i], randomSales[i]]) 
    return result

cities1 = pd.DataFrame(data = get_random(), index = [ 'Moscow', 'Tula', 'Yaroslavl', 'Tver'], columns=['report', 'sales'])
cities2 = pd.DataFrame(data = get_random(), index = [  'Moscow', 'Tula', 'Volgograd', 'Novgorod'], columns=['report', 'sales'])

cities3 = cities1.add(cities2, fill_value=0)

ans1 = cities3.sum(axis=0)
ans2 = cities3.sum(axis=1)
print(cities1)
print(cities2)
print(cities3)
print(ans1)
print(ans2)