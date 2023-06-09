from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    res = []
    track= []
    
    def backtrack(start: int, n: int, k: int) -> None:
        nonlocal res, track
        if k == len(track):
            res.append(track[::])
            return
        
        for i in range(start, n+1):
            track.append(i)
            backtrack(i + 1, n, k)
            track.pop()
        return res

    backtrack(1, n, k)
    return len(res)




def string_pattern(wordLen:int, maxVowels:int)->int:
    count=0
    for i in range(wordLen+1):
        if i==0:
            print('i==0')
            count += 21**wordLen
            print(21**wordLen)
        elif i<=maxVowels:
            print('i<=maxVowels')
            v_position=combine(wordLen, i)
            count += v_position*(5**i*21**(wordLen-i))   
            print(v_position*(5**i*21**(wordLen-i)) )
        else:
            if i-maxVowels<=wordLen-i:
                print('i>maxVowels')
                v_position=combine(wordLen, i)-combine(wordLen-i+1, 1)
                count += v_position*(5**i*21**(wordLen-i)) 
                print(v_position*(5**i*21**(wordLen-i)) )
    print('#####################')
    return count
    
print(string_pattern(5, 3))
