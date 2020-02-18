class Solutin(object):
    def get_the_digit(self, pos):
        if not (pos and isinstance(pos, int)):
            return None
        if pos <= 9:
            return pos
        cur_digit = 2
        cur_pos = 10
        left_pos = pos - cur_pos
        while left_pos > cur_digit * 9 * 10**(cur_digit - 1):
            left_pos -= cur_digit * 9 * 10**(cur_digit - 1)
            cur_digit += 1
        offset = left_pos // cur_digit
        res = left_pos % cur_digit
        target = 10**(cur_digit - 1) + offset
        return str(target)[res]

    def get_the_digit_v2(self, index):
        if not (index and isinstance(index, int)):
            return None
        if index <= 9:
            return index

    def test(self):
        position = 1001
        print(position, self.get_the_digit(position))


s = Solutin()
s.test()
