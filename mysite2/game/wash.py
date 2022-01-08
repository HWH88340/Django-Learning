# 随机生成一手桥牌
# m是牌，n是花色
#  ♠spade(黑桃)、 ♥ heart(红心)、 ♣ club(梅花)、 ♦ diamond(方块)


def get_hand():
    import random
    hand = [[], [], [], []]
    for m in [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]:
        for n in ['s', 'h', 'c', 'd']:
            index = random.randint(0, 3)
            while len(hand[index]) == 13:
                index = random.randint(0, 3)
                continue
            else:
                hand[index].append(str(m) + n)
    return hand


if __name__ == '__main__':
    print(get_hand())
