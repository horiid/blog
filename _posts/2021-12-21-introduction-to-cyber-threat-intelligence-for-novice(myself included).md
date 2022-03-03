---
layout : post
---
#### disclaimer: 
 - I'm non-native, so the following content may have incorrect grammars or misspellings. Thank you for your understanding.
 - I only spread the idea of CTI here as a countermeasure against cyberthreats and a memo for study, hence, shall not be liable for any damages incurred by others as a result of using content.

## Introduction to Cyber Threat Intelligence
Cyber Threat Intelligence has already been an essential idea for cybersecurity among threat analysts overseas especially in the US, since the idea was  came out of  American intelligence specialists, such as threat analysts worked in Military or Intelligence Agencies. The premises of CTI is "Actionable, otherwise it's no good". Good CTI urges proper actions to those who utilizes them, otherwise it's regarded as just an information, not intelligence. And that pretty much expresses the biggest difference between "Information" and "Intelligence", that information is simply a chunk of facts or data and itself won't do anything if we don't process them to a handy format for our actions we take.

## What exactly can be regarded as CTI?
CTI is relatively a new concept in cybersecurity and so many security vendors and national intelligences are still groping the better way to leverage them. However, there are some useful frameworks to categorize information which I'm about to introduce to you.
### Indicator of Compromise (IoC)
You may have heard of Indicator of Compromise (IoC) because it's a very common term in cybersecurity. But **any** information about cyberthreats can be utilized. IoCs basically mean those: 
 - **Network Indicators**
    - IP addresses
    - Host names
    - Domains(FQDN)
    - HTML Paths
    - Filetypes
    - SSL Certificates(X.509)
 - **Filesystem Indicators**
    - File hashes
    - File names
    - Strings
    - Paths
    - Sizes
    - Filetypes
    - Certificates
 - **Memory Indicators**
    - Strings
    - Memory artifacts

Note that IoC is just a very common form of technical intelligence, however, not as same as threat intelligence. 
### Pyramid of Pain
Pyramid of Pain is a framework to categorize information by the amount of pains attackers take. As we get the higher layer of intelligence, the attackers get more hurt.

![pyramid-of-pain](https://media-exp1.licdn.com/dms/image/C4D12AQHs72730iDByw/article-inline_image-shrink_1000_1488/0/1615011967281?e=1651708800&v=beta&t=53Uli7f7G42xum2C8kYKY-X9nKEoAX2QrUD7W86NoeA)

Most of IoCs I described above fit in to lower layers of the pyramid such as hash values, IP addresses, and domains. 
 - ### Network and Host Artifacts: ***Annoying***
Knowing about the activity that diffirentiates malicious activities from legit ones. These exactly are URL patterns, C&C information, registry objects, files, directories, etc. Think of yourself became as an attacker and your targets using these information to deny/detect malicious activities or intrusions. It's annoying for sure, isn't it?
 - ### Tools: ***Challenging***
Cyberattacks get gradually as sophisticated as the tools they use. These tools are such as follow: vulnerability scanners, malicious code generators, brute force password crackers, C&C, etc. Identifying and denying the abuse of those tools may significantly decrease the successful possibilities of cyberattacks.

 - ### Tactics, Techniques and Procedures (TTPs): ***Tough!***
TTP stands for "Tactics, Techniques and Procedures". This expresses the attackers' methodology, meaning their methods on delivery, installation, command & control, and execution of a cyberattack included with information of specific techniques they use. When you detect foes compromising your territories at this level, you will directly know what to do for shutting them out and there will be a very low chance of succeed of cyberattacks.

### Intelligence Cycle
Intelligence cycle is a methodology for utilizing CTI and consists of six phases. This cycle model eventually focuses on understanding the decision-making processes of everyone concerned. What you see below is the Intelligence Cycle - some experts insert "Feedback" phase after "Dissemination" phase but we don't mention here.
![intelligence-cycle](https://upload.wikimedia.org/wikipedia/commons/5/58/The_Intelligence_Process_JP_2-0.png)
 - ### Direction
 The first phase is Direction phase. In this phase we formulate to which questions we answer. The questions may be brought from external sources, intelligence team, and  sometimes it's created by them and stakeholders together (The phase is sometimes called RFI: Request For Information). The ideal closing of this phase is to set a simple and clear question that stakeholders can leverage.
 - ### Collection
 The following phase is collecting every data needed to answer the question we set earlier. In this phase we must focus on only to collect data, not analyzing them because it's hard to know which of them is actually informative, so building a function to collect and covers various data is essential. Keep in mind that it is not done one-off but repeatedly to gather further information utilizing those we get in the previous phase.
 - ### Processing
 Data we gathered in the previous phase is not always well-formatted(Natural Languages, etc) or formed in the same format, so we need to process those to a uniformed data format. Regularization to uniformed format is essential for analysis, especially if you want to make those machine-readable for the purposes of visualization, sharing, etc.
 - ### Analysis
 Analysis Phase focuses on to answer the question we set in Direction Phase. The answers aren't always be solid or can't be determined with dualism of yes/no. But it's important to clarify what kind of information is lacking and why the questions are unanswerable. 
 **Every Intelligence Analysis must be done by humans.** In other words, introducing an automated process can be an implementation of Processing, but not Analysis.
 - ### Dissemination
Being in this phase means we already have created intelligence. However, intelligence reports need to be disseminated to stakeholders who utilize them, otherwise they have no value more than bunch of sentences. **We should make sure of sharing intelligence reports in the most convenient format with related stakeholders**. In simple words, we need to think to whom are you going to share this report with. They might be management, or externals. You need to format it in the most favorable style for them.

## Adopting to Incident Response
Running Incident Response(IR) according to CTI-driven frameworks is a great methodology to properly respond to cyberthreats both in normal and emergency situations. These are the most common and known framework for doing this: The former is called **OODA Loop** of which you may already have heard, and the latter is called **F3EAD**, the Incident Response model with Intelligence Cycle processes combined.
 - ### OODA Loop
 OODA Loop is developed by American Air Force Colonel John Boyd in the 1960s. Each character of OODA stands for its phases:
 - **Observe**
    - Conduct a reconnaissance and obtain any information that seems to be useful. Monitoring logs and gathering information from external sources are the main tasks in this phase.
 - **Orient**
    - Use those information we have had in the previous phase and compare them with what we have already known. Checking captured data from logs with network environments, related APT Groups, knwon malicious IP addresses, and processes is what we do in this phase.
 - **decide**
    - Making a decision is what we have to do in this phase. For example, Whether we keep monitoring these logs? initiate incident response or just ignore the case? and so on.
 - **Act**
    - This phase is fairly simple compared to other phases, because it simply do what we decided to do in the previous phase. this phase doesn't assure the hundred percent success, however, the evaluation of this phase is done in the next Observe phase and utilize the result, by starting the whole cycle from the beginning again.
 - ### F3EAD
F3EAD is a combination of Intelligence Cycle and Incident Response. The name is also stand for its phases:
 - **Find**
    - Find the target we should respond: in other words, specify the threat we have to deal with.
 - **Fix**
    - Set up the method to monitor the network and decide where the threat is and either we have threat's tracks we can chase after.
 - **Finish**
    - Execute the actual incident response.
 - **Exploit**
    - This phase is mapped to Collection phase of Intelligence Cycle. The objective is to collect any information as many as possible:
        - IoCs such as IP address, URLs, E-Mail addresses.
        - Automatically enhancing IOCs: WHOIS, DNS Lookups, etc
        - Delivery method
        - Sample of malwares
        - Abused CVEs and malicious codes
        - Incident reports
        - Contact with the attackers
        - TTPs identified before
        - Objectives and motivations of attackers
 - **Analyze**
    - This phase is mapped to Analyze phase of Intelligence Cycle. Creating an intelligence report from what we have is the point.
        - Summary of TTP
        - Timelines and analysis according to Killchain model
        - Autopsy of malware
 - **Disseminate**
    - Disseminate the intelligence focused on to whom we distribute it.
        - Tactical
            - Incident Response Team, which uses IoCs and summarized TTPs.
        - Strategic
            - Managements who invest the security team. They tend to focus on the highly generalized TTPs and actual campaigns.
        - Third Party
            - Many organizations are in the Threat Information sharing group in any forms. Each organization needs to make the rules or standards on how to work with the group.