class Solution(object):
    def test(self):
        len_of_rope = 10
        max_product = self.compute_max_product_by_dp(len_of_rope)
        print("Result of DP: " + str(max_product))
        max_product = self.compute_max_product_by_ga(len_of_rope)
        print("Result of GA: " + str(max_product))

    def compute_max_product_by_dp(self, length):
        # Dynamic Programing
        assert isinstance(length, int)
        if length <= 1:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        max_products = [0] * (length + 1)
        max_products[1] = 1
        max_products[2] = 2
        max_products[3] = 3
        for i in range(4, length+1):
            for j in range(1, i//2+1):
                cur_product = max_products[j] * max_products[i - j]
                if max_products[i] < cur_product:
                    max_products[i] = cur_product
        return max_products[length]

    def compute_max_product_by_ga(self, length):
        # Greedy Algorithm
        assert isinstance(length, int)
        if length <= 1:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        left_length = length % 3
        if left_length == 1:
            left_length += 3
        time_of_3 = (length - left_length) // 3
        time_of_2 = left_length // 2
        max_product = 3**time_of_3 * 2**time_of_2
        return max_product

s = Solution()
s.test()