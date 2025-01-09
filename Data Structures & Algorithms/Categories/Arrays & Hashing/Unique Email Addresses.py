class Solution:
    def numUniqueEmails(self, emails):
        numSet = set()

        for email in emails:
            localName, domainName = email.split('@')
            localName = localName.split('+')[0]
            localName = localName.replace('.', '')
            numSet.add(localName + '@' + domainName)
        
        return len(numSet)
