COUNT = 5
THINKING = 0
HUNGRAY = 1
EATING = 2

states = []
mutex = 1
semaphore = []


def think(n):
    print('philosopher -%s is thinking' % n)


def eat(n):
    print('philosopher -%s is eating' % n)


def take_fores
