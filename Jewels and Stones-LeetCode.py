class Solution(object):
    def numJewelsInStones(self, J, S):
        Jewels=[]
        Stones=[]
        result=0
        for i in range (0,len(J)):
            Jewels.append(J[i])

        for i in range(0,len(S)):
            if S[i] in Jewels:
                result+=1

        return result


ts=Solution()
print(ts.numJewelsInStones("aA","aAAbbbb"))