def confusingNumber(self, N: int) -> bool:
    confuse = {'0':'0', '1':'1', '6':'9', '9':'6', '8':'8'}
    new = []
    for i in str(N):
        if i not in confuse:
            return False
        new.append(str(confuse[i]))
    return N != int(''.join(new[::-1]))

