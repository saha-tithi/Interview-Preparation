class Solution:
    def JobScheduling(self, Jobs):
        Jobs.sort(key=lambda x: x[2], reverse=True)
        max_deadline=max(job[1] for job in Jobs)
        slots=[-1]*(max_deadline+1)
        count=0
        profit=0
        for job_id,deadline,P in Jobs:
            for t in range(deadline,0,-1):
                if (slots[t]==-1):
                    slots[t]=job_id
                    count=count+1
                    profit=profit+P
                    break
        return count,profit

