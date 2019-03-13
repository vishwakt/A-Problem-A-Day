class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for index, s in enumerate(strs):
            x = ''.join(sorted(s))
            if x in dict:
                dict[x].append(s)
            else:
                dict[x] = [s]
        str_list = list(dict.values())
        return str_list


if __name__ == "__main__":
    s = Solution()
    print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
