def solution(price, money, count):
    total_price = price * count * (count + 1) / 2 # price * (1 + 2 + ... + count)

    if total_price <= money: # if there is enough money
        return 0
    else:
        return int(total_price) - money