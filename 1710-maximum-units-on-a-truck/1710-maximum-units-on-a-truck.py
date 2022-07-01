class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1],reverse = True)
        print(boxTypes)
        value=0
        for i in boxTypes:
            if i[0]<=truckSize:
                value+=(i[0]*i[1])
                truckSize-=i[0]
                if truckSize==0:
                    break
                # print(truckSize)
            else:
                # print(truckSize,"1")
                value+=(truckSize*i[1])
                break
        return value
        
        