class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        #MyIterator が __next__()を実装しているので self をイテレータとして返す
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration()
        value = self.data[self.index]
        self.index = self.index + 1
        return value
        
#シーケンスの一列として大文字を渡す
itr = MyIterator("spam")
for char in itr:
    print(char, end=" ")
