class Solution(object):
    def reverse(self, string, start, end):
        assert string and isinstance(string, list)
        while start <= end:
            string[start], string[end] = string[end], string[start]
            start += 1
            end -= 1

    def reverse_sentence(self, sentence):
        if not sentence:
            return None
        sentence = list(sentence)
        length = len(sentence)
        self.reverse(sentence, 0, length - 1)
        w_s = 0
        w_e = 0
        while w_e < length:
            if w_e == length - 1 or sentence[w_e] == ' ':
                self.reverse(sentence, w_s, w_e-1)
                w_s = w_e + 1
            w_e += 1
        return ''.join(sentence)

    def rotate_sentence(self, sentence, n):
        if not sentence or not isinstance(n, int):
            return None
        sentence = list(sentence)
        length = len(sentence)
        self.reverse(sentence, 0 , length - 1)
        self.reverse(sentence, 0, length - 1 - n)
        self.reverse(sentence, length - n, length - 1)
        return ''.join(sentence)


    def test(self):
        string = 'I am a student.'
        print(string, self.reverse_sentence(string))
        string = 'abcdefg'
        print(string, self.rotate_sentence(string, 2))


s = Solution()
s.test()