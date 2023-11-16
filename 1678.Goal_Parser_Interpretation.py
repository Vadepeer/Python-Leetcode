class Solution:
    def interpret(self, command: str) -> str:
        s = ''
        for i in range(len(command)):
            if command[i] == '(':
                if command[i+1] == 'a':
                    s += 'al'
                else:
                    s += 'o'
            if command[i] == 'G':
                s += 'G'
        return s