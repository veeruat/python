from operator import add


def append_zero_list(diff_list, diff_len):
    cnt = 1

    while cnt <= diff_len:
        diff_list.append(0)
        cnt = cnt + 1

    return diff_list


def get_fibonacci_series(list_length):
    a = 1
    b = 1
    c = 2
    fib_ser = []

    if list_length <= 0:
        print("length expected >= 1")
        return None

    if list_length == 1:
        fib_ser.append(a)
        fib_ser.append(b)
    else:
        fib_ser.append(a)
        fib_ser.append(b)
        while c <= list_length:
            c = a + b
            a = b
            b = c
            if c > list_length:
                break
            fib_ser.append(c)

    return fib_ser


def get_prime_number_list(list_length):
    prime_numbers = []

    if list_length <= 0:
        print("length expected >= 1")
        return None
    if list_length == 2:
        prime_numbers.append(2)
        return prime_numbers

    for num in range(1, list_length + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)

    return prime_numbers


def sum_list(list_length):
    prime_list = get_prime_number_list(list_length)
    fib_list = get_fibonacci_series(list_length)

    len_prime = len(prime_list)
    len_fib = len(fib_list)

    if len_fib > len_prime:
        diff_len = len_fib - len_prime
        prime_list = append_zero_list(prime_list, diff_len)
    else:
        diff_len = len_prime - len_fib
        fib_list = append_zero_list(fib_list, diff_len)

    res_list = list(map(add, prime_list, fib_list))

    print("Prime number list    :", str(prime_list))
    print("Fibonacci series list:", str(fib_list))
    print("Result list          :", str(res_list))


if __name__ == '__main__':

    try:
        print('Enter your input number:')
        length = int(input())

    except ValueError:
        print("Expected Integer input")
        exit(0)

    if length <= 0:
        print("Input number expected >= 1")
        exit(0)

    sum_list(length)
