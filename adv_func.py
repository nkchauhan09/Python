def average_finder(*args):
    average = []
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average 
avg = lambda *args : [sum(i) / len(i) for i in zip(*args)]
print(average_finder([1, 2, 3], [4, 5, 6], [7, 8, 9]))
print(avg([1, 2, 3], [4, 5, 6], [7, 8, 9]))