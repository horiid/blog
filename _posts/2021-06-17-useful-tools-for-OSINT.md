---
layout : post
---
## Useful Tools for OSINT
There are many OSINT tools on market, and that's what I'm about to tell on this post.

### What's OSINT?
**OSINT: Open Source INTelligence** is a methodology for collecting/analyzing information we can get in public. The information we get from this method is literally anything in public, such as:
 - Media Coverage
 - Whitepapers
 - Social Media(Twitter, Facebook, etc)
 - Websites
 - Journals
 - Company Publications
 - Radio Channels

In Cybersecurity, we can use these open-source information for analyzing cyberthreats. Here's a list of Public Tools I've known well so far:
 - Public OSINT Tools(Only part of those)
    - Blocklists
        - [Blocklist.de](https://www.blocklist.de/) - Public blocklist
        - [Spamhaus](https://www.spamhaus.org/) - Public blocklist
        - [Cisco Talos](https://talosintelligence.com/reputation_center/) - Public blocklist but also shows artifacts such as geolocation, owner details, etc
    - Reputations
        - [AlienVault](https://otx.alienvault.com/) - reps and related info
        - [VirusTotal](https://virustotal.com/) - Domain, URL, IP rep
        - [OPSWAT](https://metadefender.opswat.com/) - Domain, URL, IP rep
        - [Cisco Talos](https://talosintelligence.com/) - IP rep
        - [SHODAN](https://www.shodan.io/) - IP rep
        - [AbuseIPDB](https://www.abuseipdb.com/) - IP rep
        - [MXtoolbox](https://mxtoolbox.com/) - Mail rep

These are not particurally for cybersecurity purpose, but still useful sources:
 - WHOIS
    - Ownership of IP address
    - Geolocation of IP address
    - Domain resistrant
    - Name, phone number, location of the registrant
    - Domain creation date
    - Domain updated date
    - Domain expiry date
 - Publishing
    - Reports  published by security vendors
    - Specific web sites such as [krebs on security](https://krebsonsecurity.com/), [piyokango's blog](https://piyolog.hatenadiary.jp/)
    - Media coverage
    - Social Media, especially [Twitter](https://twitter.com)

The methods to utilize these depend on the case, however, considering simple and timely information such as reputation of collected IoCs, or whether the specific host is in public blocklists is a reasonable solution for the assessment of the current threat level of an attacker's campaign.