class Solution(object):
    def test(self):
        string = "We are happy!"
        res = self.replace(string)
        print(res)

    # Time: O(n)
    def replace(self, string):
        string = list(string)
        org_len = len(string)
        if org_len <= 0:
            return None
        num_of_blank = 0
        for char in string:
            if char == ' ':
                num_of_blank += 1
        string += ' ' * 2 * num_of_blank
        new_len = org_len + 2 * num_of_blank
        front_index = org_len - 1
        back_index = new_len - 1
        while front_index != back_index:
            if string[front_index] == ' ':
                string[back_index-2] = "%"
                string[back_index-1] = "2"
                string[back_index] = "0"
                back_index -= 2
            else:
                string[back_index] = string[front_index]
            front_index -= 1
            back_index -= 1
        return ''.join(string)


s = Solution()
s.test()