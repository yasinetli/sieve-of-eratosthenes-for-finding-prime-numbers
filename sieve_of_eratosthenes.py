# sieve_of_eratosthenes.py
# Author : Yasin ETLİ
# Date created: 03/03/2022
# This script finds prime numbers up to any number entered with the sieve of Eratosthenes algorithm.

def eratosthenes():
    prime_list = []
    not_prime_list = []
    range_input = int(input("What number do you want to find prime numbers up to? \n"))
    for i in range(2, range_input):
        number_list = [i]
        for num in number_list:
            division_number = round(len(prime_list) / 2)
            for item in range(0, division_number):
                if num % prime_list[item] == 0:
                    not_prime_list.append(i)

            if num not in not_prime_list:
                prime_list.append(i)
                npr_num = int(range_input / num)
                for number in range(1, npr_num):
                    if num * number in number_list:
                        number_list.remove(num * number)
    print(prime_list)
    print(len(prime_list))


eratosthenes()
