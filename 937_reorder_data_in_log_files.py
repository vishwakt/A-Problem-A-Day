class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # Suffix is tie, sort by identifier
        letters.sort(key=lambda x: x.split()[0])

        # Sort by suffix
        letters.sort(key=lambda x: x.split()[1:])

        return letters + digits


if __name__ == "__main__":
    s = Solution()
    logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
    print (s.reorderLogFiles(logs))