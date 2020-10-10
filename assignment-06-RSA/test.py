import time
from multiprocessing import Pool

def sum_sqare(number):
    s = 0
    print(number)
    for i in range(100000):
        s += i*i
    return s



def multiThread():
    pass
def main():
    pass




if __name__ == '__main__':
    p = Pool(8)
    alkøsdj=range(100127)
    test=p.map(sum_sqare,alkøsdj)
    print(test)
    p.close()
    p.join()