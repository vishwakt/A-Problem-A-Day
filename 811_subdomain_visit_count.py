from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dict = {}
        for domain in cpdomains:
            count, domain = domain.split(' ')
            subs = domain.split('.')
            # for subdomain in domain:
            for i in range(len(subs)):
                sub = ".".join(subs[i:])
                dict[sub] = dict.get(sub, 0) + int(count)
        list_ = [" ".join([str(val), key]) for key, val in dict.items()]
        return list_


if __name__ == "__main__":
    s = Solution()
    print(s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))