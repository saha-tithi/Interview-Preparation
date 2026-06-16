class Solution:
    def fractionalKnapsack(self, val, wt, cap):
        items=[]
        for i in range(len(val)):
            items.append((val[i]/wt[i],val[i],wt[i]))
        items.sort(reverse=True)
        total_value=0.0

        for ratio,value,weight in items:
            if cap>=weight:
                total_value+=value
                cap-=weight
            else:
                total_value+=ratio*cap
        return round(total_value, 6)

