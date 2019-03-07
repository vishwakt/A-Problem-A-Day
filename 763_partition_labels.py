class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return []

        dict = {}
        result = []

        for index, char in enumerate(S):
            if char in dict:
                dict[char][1] = index
            else:
                dict[char] = [index, index]

        sorted_list_dictionary = sorted(dict.items(), key=lambda x: x[1][0])

        start, end = sorted_list_dictionary[0][1]

        for char in sorted_list_dictionary[1:]:
            if char[1][0] > start and char[1][1] < end:
                continue
            elif char[1][0] < end:
                end = char[1][1]
            else:
                result.append(end - start + 1)
                start = char[1][0]
                end = char[1][1]

        result.append(end - start + 1)
        return result


if __name__ == "__main__":
    s = Solution()
    print s.partitionLabels("ababcbacadefegdehijhklij")