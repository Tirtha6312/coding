class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        answer = []
        current_group = 1

        for bracket in seq:
            if bracket == '(':
                answer.append(1 - current_group)
            else:
                answer.append(current_group)

            current_group ^= 1

        return answer