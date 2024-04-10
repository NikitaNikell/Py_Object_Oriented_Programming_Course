import sys

def runCase():
    k = int(input())
    arr = list(map(int, input().split()))
    input()
    res = compress(arr)
    print(len(res))
    print(*res)

def compress(arr):
    if len(arr) == 1:
        return [arr[0], 0]
    res = []
    ci = 0
    temp = arr[0]
    toWrite = temp
    for i, v in enumerate(arr):
        if i == 0:
            continue
        if (ci < 0 or ci == 0) and v+1 == temp:
            ci -= 1
            if i == len(arr)-1:
                res.append(toWrite)
                res.append(ci)
            temp -= 1
            continue
        if (ci > 0 or ci == 0) and v-1 == temp:
            ci += 1
            if i == len(arr)-1:
                res.append(toWrite)
                res.append(ci)
            temp += 1
            continue
        if ci > 0 or ci < 0:
            res.append(toWrite)
            res.append(ci)
            ci = 0
            temp = v
            toWrite = temp
            if i+1 == len(arr):
                res.append(v)
                res.append(0)
            continue
        res.append(toWrite)
        res.append(0)
        if i+1 != len(arr):
            toWrite = v
            temp = v
        else:
            res.append(v)
            res.append(0)
    return res

def main():
    n = int(input())
    for _ in range(n):
        runCase()

if __name__ == "__main__":
    main()

# 5
# 9
# 3 2 1 0 -1 0 6 6 7
# 1
# 1000
# 7
# 1 2 3 4 5 6 7
# 7
# 1 3 5 7 9 11 13
# 11
# 100 101 102 103 19 20 21 22 42 41 40
