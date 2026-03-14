import sys
import time

sys.set_int_max_str_digits(1_000_000)

number = int(input("Enter a number: "))
num = (2**number) + 1
step = 0
start = time.time()
three_x = 0
divide_two = 0

while num > 1:
    if num & 1:
        num = (((num << 1) + num) + 1)
        trailing = (num & -num).bit_length() - 1
        num >>= trailing
        step += 1 + trailing
        three_x += 1
        divide_two += trailing
    else:
        trailing = (num & -num).bit_length() - 1
        num >>= trailing
        divide_two += trailing
        step += trailing

print(f"Sequence Length: {step:,}")
print(f"3x+1 steps: {three_x:,}")
print(f"Divide by 2 steps: {divide_two:,}")
print("Time taken:", time.time() - start)

