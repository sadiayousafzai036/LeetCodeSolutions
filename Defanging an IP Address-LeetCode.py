class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        defang=[]

        for i in address:
            if i==".":
                defang.append('[.]')
            else:
                defang.append(i)
        ipaddress = "".join(defang)
        return (ipaddress)


ts=Solution()
print(ts.defangIPaddr("1.1.1.1"))