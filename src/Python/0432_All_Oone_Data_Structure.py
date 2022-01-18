class AllOne:
    def __init__(self):
        self.key_value = {}
        self.key_index = {}
        self.key_list = []

    def inc(self, key: str) -> None:
        if key in self.key_value:
            self.key_value[key] += 1
            value = self.key_value[key]
            index = self.key_index[key]
            while index > 0:
                key_left = self.key_list[index-1]
                value_left = self.key_value[key_left]
                if value_left < value:
                    self.key_list[index] = key_left
                    self.key_index[key_left] += 1
                    self.key_list[index-1] = key
                    self.key_index[key] = index-1
                    index -= 1
                else:
                    break
        else:
            self.key_value[key] = 1
            self.key_list.append(key)
            self.key_index[key] = len(self.key_list)-1

    def dec(self, key: str) -> None:
        value = self.key_value[key]
        if value == 1:
            index = self.key_index[key]
            key_right = self.key_list[-1]
            self.key_list[index] = key_right
            self.key_list.pop()
            self.key_value.pop(key)
            self.key_index[key_right] = index
        else:
            self.key_value[key] -= 1
            value = self.key_value[key]
            index = self.key_index[key]
            while index < len(self.key_list)-1:
                key_right = self.key_list[index+1]
                value_right = self.key_value[key_right]
                if value_right > value:
                    self.key_list[index] = key_right
                    self.key_index[key_right] -= 1
                    self.key_list[index+1] = key
                    self.key_index[key] = index+1
                    index += 1
                else:
                    break
            

    def getMaxKey(self) -> str:
        if self.key_list:
            return self.key_list[0]
        else:
            return ''


    def getMinKey(self) -> str:
        if self.key_list:
            return self.key_list[-1]
        else:
            return ''



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()