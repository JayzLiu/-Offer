class Solution(object):
    def number_of_translation_recurence(self, number):
        def count_translation(string):
            if len(string) == 0:
                return 0
            if len(string) == 1:
                return 1
            if is_legal(string[-2:]):
                return count_translation(string[:-2]) + count_translation(string[:-1])
            else:
                return count_translation(string[:-1])                  
        def is_legal(sub_string):
            assert len(sub_string) == 2
            num = int(''.join(sub_string))
            return 10 <= num and num <= 25 
        
        if not number or not isinstance(number, int) or number < 0:
            return None
        return count_translation(str(number))
    
    def number_of_translation(self, number):
        if not number or type(number) != int or number < 0:
            return None
        number = str(number)
        length = len(number)
        counts = [0] * length
        i = length - 1
        for i in reversed(range(length)):
            if i == length - 1:
                counts[i] = 1
                continue
            double_d = int(number[i]) * 10 + int(number[i+1])
            if 10 <= double_d and double_d <= 25:
                if i < length - 2:
                    counts[i] += counts[i+2]
                else:
                    counts[i] += 1
            counts[i] += counts[i+1]
        return counts[0] 
                

    def test(self):
        number = 12258
        print(number, self.number_of_translation(number))
        print(number, self.number_of_translation(number))


s = Solution()
s.test()