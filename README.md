# Collatz-Conjecture-Python
Python code using bitwise operations to test if the Collatz Conjecture holds true for a given number.  

It uses optimizations described by [GonzoMath](https://www.reddit.com/user/GonzoMath/) in his threads about optimizing python code for calculation Collatz Conjecture sequences which can be found [here](https://www.reddit.com/r/Collatz/comments/1k5plwn/collatz_shortcuts_implementation_in_python_part_1/) and [here](https://www.reddit.com/r/Collatz/comments/1k5plwn/collatz_shortcuts_implementation_in_python_part_1/).   

## Benchmarking  
I wrote a simple program for checking in the Collatz Conjecture is true with no bit shifting.  
```
import sys
import time

sys.set_int_max_str_digits(1_000_000)

number = int(input("Enter a number: "))

num = (2**number) + 1

step = 0
start = time.time()
while num > 1:
    if num % 2 == 1:
        num = (num * 3) + 1
    else:
        num = num // 2

    if step % 100000 == 0:
        print(f"Step {step:,}")
    step += 1

print("Total steps: {step:,}")
print("Time taken:", time.time() - start)
```

Starting from (2^150,000) + 1:
- Unoptimized: 17.5777 seconds.
- Optimized: 3.6853 seconds.
Roughly 4.76 times faster

## To Do  
- [ ] Add functionality to save the initial seed, number of 3n+1 steps, n/2 steps, and the ratio of those steps into a json array for analysis.
- [ ] Update code to detect if a cycle has been found (tortois and hare algorithm?) and if it has, save the starting seed.
