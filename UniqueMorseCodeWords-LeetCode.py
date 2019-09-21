class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morselist=[]
        count=0

        morsed={'a':".-"  ,'b':"-..." ,'c':"-.-." ,'d':"-.."  ,'e':".",'f':"..-.",'g':"--." ,
                'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",
                'p':".--." ,'q':"--.-" ,'r':".-." ,'s':"...",'t':"-" ,'u':"..-",
                'v':"...-"  ,'w':".--" ,'x':"-..-"  ,'y':"-.--",'z':"--.."}

        for i in range(0,len(words)):
            unique = ""
            wordtmp = ""
            wordtmp+=(words[i])
            for j in range(0,len(wordtmp)):
                unique+=morsed[wordtmp[j]]
                wordslist = ""
            if unique not in morselist:
                wordslist+=unique
                morselist.append(wordslist)
                count+=1
        return (count)


ts=Solution()
#print(ts.rangeSumBST([10,5,15,3,7,None,18],7,15))

print(ts.uniqueMorseRepresentations(["mevzi","mevzi","gvgs","qhiwg","qhijn","b","b","b","b","b"]))