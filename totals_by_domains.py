# Write a function that takes this input as a parameter and returns a data structure containing the
# number of hits that were recorded on each domain AND each domain under it. For example, an impression
# on "mail.yahoo.com" counts for "mail.yahoo.com", "yahoo.com", and "com". (Subdomains are added to the
# left of their parent domain. So "mail" and "mail.yahoo" are not valid domains. Note that "mobile.sports"
# appears as a separate domain as the last item of the input.)

# Sample output (in any order/format):

# getTotalsByDomain(counts)
# 1320    com
#  900    google.com
#  410    yahoo.com
#   60    mail.yahoo.com
#   10    mobile.sports.yahoo.com
#   50    sports.yahoo.com
#   10    stackoverflow.com
#    3    org
#    3    wikipedia.org
#    2    en.wikipedia.org
#    1    es.wikipedia.org
#    1    mobile.sports
#    1    sports

count = ["900,google.com",
         "60,mail.yahoo.com",
         "10,mobile.sports.yahoo.com",
         "40,sports.yahoo.com",
         "300,yahoo.com",
         "10,stackoverflow.com",
         "2,en.wikipedia.org",
         "1,es.wikipedia.org",
         "1,mobile.sports",
         "5555, foo.com.org"]


def getTotalsByDomain(count):
    dict = {}
    for element in count:
        value, domain = element.split(',')
        domain = domain.split('.')
        temp = ""
        for x, new_domain in reversed(list(enumerate(domain))):
            if x != len(domain) - 1:
                temp = '.' + temp
            temp = new_domain + temp
            if temp in dict:
                dict[temp] += int(value)
            else:
                dict[temp] = int(value)
    return sorted(dict.items(), key=lambda k: k[1], reverse=True)


print getTotalsByDomain(count)