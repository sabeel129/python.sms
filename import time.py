import  time

def linear_time(n):
    print(f"\n(n) num={n}")
    start = time.time()
    for i in range(n):
        pass
    end = time.time()
    print(f"Time taken: {end - start} seconds")

linear_time(10000)
linear_time(20000)
linear_time(30000)