n = int(input("Enter the number of terms: "))

fib_series = [0,1]

for i in range(2, n):
    fib_series.append(fib_series[i-2]+fib_series[i-1])

print("Fibonacci Series upto {} terms is: {}".format(n, fib_series))