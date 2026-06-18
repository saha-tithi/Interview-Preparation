class Solution:
    def findMaximumCookieStudents(self, Student, Cookie):
        Cookie.sort()
        Student.sort()
        i=0
        j=0
        count=0
        while i<len(Student) and j<len(Cookie):
            if Cookie[j]>=Student[i]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        return count
       
