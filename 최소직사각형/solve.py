# if card fits in size of wallet, return True
def fit(wallet, card):
    if card[0] <= wallet[0] and card[1] <= wallet[1]:
        return True
    if card[0] <= wallet[1] and card[1] <= wallet[0]:
        return True
    return False

def solution(sizes):
    w = 0 # width of wallet
    h = 0 # height of wallet

    for size in sizes:
        if fit([w, h], size) == False:
            size1 = max(w, size[0]) * max(h, size[1])
            size2 = max(w, size[1]) * max(h, size[0])
            
            if size1 < size2:
                w = max(w, size[0])
                h = max(h, size[1])
            else:
                w = max(w, size[1])
                h = max(h, size[0])

    return w * h