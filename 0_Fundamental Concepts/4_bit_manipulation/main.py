
# Bit Manipulation 

class Solution:
    @staticmethod 
    def main():
        num = 124
        print(format(num, 'b'))
        print(format(num, 'x'))
        print(format(num, 'd'))
        print("format(1<<4, 'b')= ", format(1<<4, 'b'))
        print("format(1<<4, 'b')= ", format(~(1<<4), 'x'))

        num2 = num & ~1<<4
        print(format(num2, 'x'))
        print("Done!")


Solution.main()