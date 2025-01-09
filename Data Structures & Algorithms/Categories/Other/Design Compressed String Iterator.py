class StringIterator:
    # is this case sensitive? should i return as a lower case? upper case?
    # will I be dealing with any invalid inputs?
    # duplicates possible?
    # by uncompressed, do you mean once you expand the compressed string, you reach the expand, or do you mean when you have reached the final character that needs to be decompressed

    # empty string
    # multiple digit numbers (3)
    # single digit numbers 
    # same letter in consecutive order 
    # same letter in consecutive but with different casing

    def __init__(self, compressedString: str):
        self.uncompressed_str = ""
        self.i = 0

        while self.i < len(compressedString):
            c = compressedString[self.i]
            self.i += 1
            num = ""

            while self.i < len(compressedString) and compressedString[self.i].isdigit():
                num += compressedString[self.i]
                self.i += 1
            
            self.uncompressed_str += int(num) * c

        self.i = 0

    def next(self) -> str:
        self.i += 1
        return self.uncompressed_str[self.i-1] if self.i <= len(self.uncompressed_str) else " "

    def hasNext(self) -> bool:
        return self.i < len(self.uncompressed_str)


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
