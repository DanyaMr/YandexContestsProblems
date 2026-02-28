from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        template = Counter(s1)

        size_of_window = len(s1)

        left_edge, right_edge = 0, size_of_window - 1

        window = Counter(s2[:size_of_window])

        while right_edge <= len(s2) - 1:
            if template == window:
                return True

            if s2[left_edge] in window:
                if window[s2[left_edge]] == 1:
                    del window[s2[left_edge]]
                else:
                    window[s2[left_edge]] -= 1

            left_edge += 1

            window[s2[right_edge + 1]] += 1

            right_edge += 1

        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion("adc", "dcda"))