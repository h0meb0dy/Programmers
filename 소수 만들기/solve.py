is_prime = [True for number in range(3001)] # if n is prime number, is_prime[n] = True

def prime_init():
    is_prime[0] = False # 0 is not prime number
    is_prime[1] = False # 1 is not prime number

    for num in range(4, 3001):
        for divider in range(2, int(num / 2) + 1):
            if is_prime[divider] == False:
                continue
            if num % divider == 0: # num is not prime number
                is_prime[num] = False
                break

def solution(nums):
    prime_init() # get prime numbers between 1 and 3000

    answer = 0

    for idx1 in range(len(nums)):
        for idx2 in range(idx1 + 1, len(nums)):
            for idx3 in range(idx2 + 1, len(nums)):
                if is_prime[nums[idx1] + nums[idx2] + nums[idx3]] == True:
                    answer += 1

    return answer