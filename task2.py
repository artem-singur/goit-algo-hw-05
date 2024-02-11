from typing import Callable

def generator_numbers(text: str):

    for i in text.split():
        try:
            number = float(i)
            yield number
        except:
            pass

    return 0

def sum_profit(text: str, func: Callable):

    sum = 0

    for i in func(text):
        sum += i

    return sum
