# Write a function that takes two numbers and finds the average between the two.

def avg(a,b):
    sum = a + b
    avg = sum / 2
    return avg

avg_1 = avg(0, 10)
avg_2 = avg(8, 10)
    
final = avg(avg_1, avg_2)
print("avg_1", avg_1)
print("avg_2", avg_2)
print("final", final)