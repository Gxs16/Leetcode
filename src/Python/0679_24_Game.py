class Solution:
    def select_number(self, cards, num_set):
        if len(num_set) == 6:
            if round(cards[-1], 2) == 24:
                return True
            else:
                return False
        for i, num1 in enumerate(cards):
            if i not in num_set:
                num_set_new1 = num_set + [i]
                for j, num2 in enumerate(cards):
                    if j not in num_set_new1:
                        num_set_new = num_set_new1+[j]

                        new = num1+num2
                        if self.select_number(cards+[new], num_set_new):
                            return True

                        if num1 >= num2:
                            new = num1-num2
                            if self.select_number(cards+[new], num_set_new):
                                return True

                        new = num1*num2
                        if self.select_number(cards+[new], num_set_new):
                            return True

                        if num2 != 0:
                            new = num1/num2
                            if self.select_number(cards+[new], num_set_new):
                                return True
        return False

    def judgePoint24(self, cards) -> bool:
        num_set = []
        return self.select_number(cards, num_set)