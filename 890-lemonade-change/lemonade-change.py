class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        freq = {}
        for num in [5,10,20]:
            freq[num] = 0


        for i in range(len(bills)):
            if bills[i]==5:
                freq[5]+=1
            elif bills[i]==10:
                if freq[5]==0:
                    return False
                freq[5]-=1
                freq[10]+=1
            elif bills[i]==20:
                if freq[10]>=1 and freq[5]>=1:
                    freq[10]-=1
                    freq[5]-=1
                    freq[20]+=1
                elif freq[5]>=3:
                    freq[5]-=3
                    freq[20]+=1
                else:
                    return False
        return True