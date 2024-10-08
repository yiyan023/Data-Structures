class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            i = local.find("+")

            if i >= 0:
                local = local[:i]
                
            unique_emails.add(f"{local}@{domain}")
        
        return len(unique_emails)
