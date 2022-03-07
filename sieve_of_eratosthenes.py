# sieve_of_eratosthenes.py
# Author : Yasin ETLİ
# Date created: 03/03/2022
# This script finds prime numbers up to any number entered with the sieve of Eratosthenes algorithm.

def eratosthenes():
    number_list = []
    prime_list = []
    range_input = int(input("What number do you want to find prime numbers up to? \n"))
    for i in range(2, range_input):
        number_list.append(i)

    for num in number_list:
        prime_list.append(num)
        times_num = int(range_input / num)+1
        for tn in range(2, times_num):
            times = num * tn
            if times in number_list:
                number_list.remove(times)

    print(prime_list)
    print(len(prime_list))


eratosthenes()
