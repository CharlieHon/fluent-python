import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit']) # 也可用空格分割的字符串

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()  # 黑桃 方块 梅花 红桃

    def __init__(self) -> None:
        self._card = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    
    def __len__(self):
        """
        定义了一个实例方法，返回实例属性_card的长度.。
        此时，len指令没有什么关于len本身的特定含义，只是简单地映射这个方法
        """
        return len(self._card)
    
    def __getitem__(self, position):
        """
        定义了方法__getitem__()以后，这个对象成为iterable(可迭代对象)
        """
        return self._card[position]


# 创建一个对象deck
deck = FrenchDeck()
# 返回纸牌对象的长度
print(len(deck))    # 52
# 第一张和最后一张纸牌
print(deck[0], deck[-1])    # Card(rank='2', suit='spades') Card(rank='A', suit='hearts') 

# 从一个iterable对象中随机选取一个
for _ in range(3):
    print(choice(deck))

# 这里会调用__getitem__方法
for card in deck:
    print(card)

# 反向迭代
for card in reversed(deck):
    print(card)

# in方法会遍历deck，有返回True，否则返回False
print(Card('Q', 'hearts') in deck)  # True
print(Card('B', 'hearts') in deck)  # False

# 排序 ['spades♠', 'hearts♥', 'diamonds♦', 'clubs♣']
suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)   # 给花色赋权重

def deck_high(card: Card):
    """根据牌的suit, rank属性排序"""
    # 在实例deck中，每一个元素都是一个具名元组(namedtuple)，获取其属性rank，即得到了扑克牌的点数
    # 然后用index()得到点数在列表FrenchDeck.ranks中对应的索引，即为扑克牌的次序
    rank_value = FrenchDeck.ranks.index(card.rank) # rank的值
    # rank_value * 4 + suit_value
    return rank_value * len(FrenchDeck.suits) + suit_value[card.suit]


# 迭代通常是隐式的，如果一个集合类型没有实现__contains__方法，那么in运算符会按顺序做一次迭代搜索
for card in sorted(deck, key=deck_high):
    print(card)

# magic method
print(deck.__len__())
print(len(deck))        # 推荐