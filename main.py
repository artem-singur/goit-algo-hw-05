from task1 import caching_fibonacci
from task2 import generator_numbers, sum_profit

# task1
# fibonacci = caching_fibonacci()
# print(fibonacci(13))
# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5))
# print(fibonacci(6))
# print(fibonacci(-3))

# task2
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
print(sum_profit(text, generator_numbers))
