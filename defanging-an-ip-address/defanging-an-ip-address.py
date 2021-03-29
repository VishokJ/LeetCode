class Solution(object):
    def defangIPaddr(self, address):
        add = ""
        for i in address:
            if i == ".": add+="[.]"
            else: add+=i
        return add