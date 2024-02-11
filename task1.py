def caching_fibonacci():

    cache = {1: 1}

    def fibonacci(n: int) -> int:

        if n <= 0: return 0 # Послідовність Фібоначчі тільки для додатних чисел

        if cache.get(n) is None:
            # print(f"Обчислення fibonacci({n})")
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci
