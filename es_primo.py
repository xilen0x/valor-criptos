''' from pip import main



def es_primo(num_a: int) -> bool:
    
    if num_a <= 1:
        print(False)
    
    elif num_a == 2:
        print(True)
    
    else:
        for x in range(2, num_a):
            if num_a % x == 0:
                print(False)
        
        print(True)
        

def main():
    num_a = int(input("Ingresa un numero: "))
    es_primo(num_a)




if __name__ == '__main__':
    main()
     '''
#---------------------------------------------------
"""Python module to know if a number is prime"""


def is_prime(number: int) -> bool:
    """Returns True if number is prime or False if the number is not prime"""
    results_list = [x for x in range(2, number) if number % x == 0]
    return len(results_list) == 0


def run():
    number: int = int(input("Ingresa un numero: "))
    number_is_prime: bool = is_prime(number)
    print(f'Is {number} a prime number? {number_is_prime}')


if __name__ == '__main__':
    run()