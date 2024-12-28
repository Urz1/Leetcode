class Solution:
    def defangIPaddr(self, address: str) -> str:
        Ip = []
        for i in address:
            if i == '.':
                Ip.append("[.]")
            else:
                Ip.append(i)
        return ''.join(Ip)