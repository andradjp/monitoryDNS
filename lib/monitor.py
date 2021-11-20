import whois

class Monitor():

    def getDNS(self, domain):
        try:
            w = whois.whois(domain)
            print('Domain: ', w['domain_name'])
            print('Date of creation: ', w['creation_date'])
        except whois.parser.PywhoisError:
            print('Domain %s not registered.' % (domain))