# Collatz-Conjecture-Python
Python code using bitwise operations to test if the Collatz Conjecture holds true for a given number.  

It uses optimizations described by [GonzoMath](https://www.reddit.com/user/GonzoMath/) in his threads about optimizing python code for calculation Collatz Conjecture sequences which can be found [here](https://www.reddit.com/r/Collatz/comments/1k5plwn/collatz_shortcuts_implementation_in_python_part_1/) and [here](https://www.reddit.com/r/Collatz/comments/1k5plwn/collatz_shortcuts_implementation_in_python_part_1/).  

This code will be updated to notify the user if a cycle has been found.  

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
