class Solution:
    def sortTheStudents(self, score, k):

        return sorted(score, key= lambda score: score[k], reverse=True)
