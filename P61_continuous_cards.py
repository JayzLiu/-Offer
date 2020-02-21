class Solution(object):
    def is_straight_flush(self, cards):
        if not cards or len(cards) != 5 or max(cards) > 13 or min(cards) < 0:
            return None
        cards.sort()
        num_of_0 = 0
        num_of_gap = 0
        i = 0
        while i < 5 and cards[i] == 0:
            num_of_0 += 1
            i += 1
        ahead = num_of_0
        behind = ahead + 1
        while behind < 5:
            if cards[ahead] == cards[behind]:
                return False
            num_of_gap = cards[behind] - cards[ahead] - 1
            ahead = behind
            behind = ahead + 1
        if num_of_gap <= num_of_0:
            return True
        else:
            return False

    def test(self):
        cards = [1, 2, 3, 4, 5]
        print(cards, self.is_straight_flush(cards))


s = Solution()
s.test()