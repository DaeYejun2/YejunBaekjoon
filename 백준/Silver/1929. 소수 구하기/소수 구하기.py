n, m = map(int, input().split())

def eratosthenes(n, m):
    is_prime = [True] * (m + 1)
    is_prime[0] = False
    is_prime[1] = False
    
    limit = int(m**0.5)  #반복은 2부터 m의 제곱근 까지만 하면됨. 어차피 약수니께
    
    for i in range(2, limit+1):
        if is_prime[i]:
            for j in range(i*i, m+1, i):
                is_prime[j] = False
                
    result = []
    for num in range(n, m+1):
        if is_prime[num]:
            result.append(num)
            
    return result
prime_list = eratosthenes(n, m)
print(*prime_list,sep="\n")