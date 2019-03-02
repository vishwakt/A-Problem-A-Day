class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        valid_emails = []
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = "".join(local_name.split('+')[0].split('.'))
            email = local_name+"@"+domain_name
            valid_emails.append(email)
        return len(list(set(valid_emails)))


if __name__ == "__main__":
    s = Solution()
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    print s.numUniqueEmails(emails)