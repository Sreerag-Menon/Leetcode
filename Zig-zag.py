'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 or numRows>=len(s):
            return s
        rows=[""]*numRows
        current=0
        going_down=False
        for char in s:
            rows[current]+=char
            if current==0 or current==numRows-1:
                going_down=not going_down
                
            if going_down:
                current+=1
            else:
                current-=1
        result=''.join(rows)
        return result
        