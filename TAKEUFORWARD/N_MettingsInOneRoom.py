class Solution:
    def maxMeetings(self, start, end):
        meetings=[]
        for i in range(len(start)):
            meetings.append((end[i],start[i]))
        meetings.sort()
        count=1
        end_time=meetings[0][0]
        for i in range(1,len(meetings)):
            current_end=meetings[i][0]
            current_start=meetings[i][1]
            if current_start>end_time:
                count=count+1
                end_time=current_end
        return count