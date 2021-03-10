def prime(max_prime):
    my_primes=[]

    for number in range(1, max_prime + 1):
        if number < 3:
            my_primes.append(number)

            continue
        for divider in range(2, number):
            if number % divider == 0:

                break
        else:
            my_primes.append(number)
    return my_primes

def encripted(text,number=144):
    my_list=[]
    for letter in text:
        my_letter=chr(ord(letter).__xor__(number))
        my_list.append(my_letter)
    resoult="".join(my_list)
    return resoult

print(encripted(text))
