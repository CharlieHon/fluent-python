"""
Python的序列协议只需要 __len__ 和 __getitem__ 两个方法。只要实现了这两个方法，就能用在任何期待序列的地方。
这种类型被称为鸭子类型(duck typing)
"""
from collections import namedtuple

# 纸牌类
Card = namedtuple('Card', 'rank suit')

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._card = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._card)

    def __getitem__(self, index):
        return self._card[index]


"""
FrenchDeck类实现了序列，说它是序列，因为它的行为像序列，这才是重点。
"""
