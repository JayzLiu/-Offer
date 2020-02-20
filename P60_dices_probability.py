class Solution(object):
    def compute_prob_by_recurence(self, n_d):
        def count_dices(n_d, count, sum, i):
            if i == n_d:
                count[sum - n_d] += 1
            else:
                for point in range(1, d_max+1):
                    count_dices(n_d, count, sum + point, i + 1)

        if not isinstance(n_d, int) or n_d < 0:
            return
        count = [0] * (n_d * d_max - n_d + 1)
        for point in range(1, d_max+1):
            count_dices(n_d, count, point, 1)
        count_sum = d_max ** n_d
        for i in range(len(count)):
            count[i] = count[i] / count_sum
            print(str(i+n_d), count[i])

    def compute_prob(self, n_d):
        counts = [[0] * (n_d * d_max + 1) for i in range(2)]
        counts[0][1 : d_max + 1] = [1] * d_max
        flag = 0
        for i in range(2, n_d + 1):
            flag = 1 - flag
            for cur_sum in range(i, i * d_max + 1):
                for point in range(1, min(cur_sum + 1, d_max + 1)):
                    counts[flag][cur_sum] += counts[1 - flag][cur_sum - point]
        count_sum = d_max ** n_d
        # print(counts)
        for i in range(len(counts[flag]) - n_d):
            print(str(i + n_d), counts[flag][i + n_d] / count_sum)


    def test(self):
        global d_max
        d_max = 6
        n = 3
        self.compute_prob_by_recurence(n)
        print()
        self.compute_prob(n)


s = Solution()
s.test()
