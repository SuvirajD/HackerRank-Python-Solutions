import hashlib

if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()[:n]))
    tuple_list = tuple(integer_list)
    print(hash(tuple_list))

