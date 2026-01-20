class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors = 0
        for detail in details:
            age = int(detail[11] + detail[12])
            if age > 60:
                seniors += 1
        return seniors
