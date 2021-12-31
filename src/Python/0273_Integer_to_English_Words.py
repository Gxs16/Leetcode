class Solution:
    def threeToWords(self, num: int, suffix) -> str:
        result = ''
        if num >= 100:
            digit_three = num//100
            result += ' '+self.singles[digit_three]+' Hundred'
        num_temp = num%100
        if num_temp >= 20:
            result += ' '+self.tens[num_temp//10]
            digit_one = num_temp%10
            if digit_one > 0:
                result += ' '+self.singles[num_temp%10]
        elif num_temp >= 10:
            result += ' '+self.teens[num_temp-10]
        elif num_temp > 0:
            result += ' '+self.singles[num_temp]
        if suffix and result:
            result += ' '+suffix
        return result

    
    def numberToWords(self, num: int) -> str:
        self.singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        self.teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

        result = ''
        base = 1000
        i = 0
        if num == 0:
            return 'Zero'
        while num > 0:
            num_split = num%base
            suffix = self.thousands[i]
            num //= base
            i += 1
            result = self.threeToWords(num_split, suffix)+result
        return result[1:]