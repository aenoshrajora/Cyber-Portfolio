from flask import Flask, render_template

app = Flask(__name__)

resume_data = {
    "name": "$ whoami - Aenosh Rajora",
    "title": "Cybersecurity Specialist | Penetration Tester | Ethical Hacker | 345 THM Rank | Google Cybersecurity Certified",
    "email": "aenoshrajora79@gmail.com",
    "location": "Lucknow, India",
    "about": "Passionate about ethical hacking, red teaming, and simulating real-world attack scenarios. I build offensive security tools, publish security research, and solve high-difficulty labs on TryHackMe and HTB. Recognized for Strong Collaboration, adaptability, and a fast learning curve, with 20+ CTF writeups and real-world projects. Seeking to contribute to dynamic security teams that value technical depth and creativity are initiative.",
    "experience": [
        {
            "title": "Offensive Security Researcher",
            "company": "Independent",
            "location": "Remote",
            "dates": "January 2024 - Present",
            "bullet_points": [
                "Designed and deployed 7+ custom labs replicating real-world attacks (AD, RCE, privilege escalation)."
                "Built tools for phishing simulation and recon automation; open-sourced on GitHub with active community use."
                "Reverse - engineered malware using PyCrypto and sandboxing to extract behavior signatures and flag infection indicators."
                ]
        },
        {
            "title": "Cyber Security Intern",
            "company": "Hack Secure",
            "location": "Remote",
            "dates": "April 2025 - May 2025",
            "bullet_points": [
                "Performed reconnaissance, directory brute-forcing, SQL injection, and XSS exploitation on test environments.",
                "Executed credential harvesting, lateral movement, persistence, and C2 setup using Mimikatz, PowerShell Empire, Covenant, and Metasploit.",
                "Developed Python tools: TCP port scanner, password strength evaluator, and file encryption utility (AES - cryptography module).",
                "Analyzed network traffic with Wireshark to extract credentials via intercepted sessions.",
            ]
        },
        {
            "title": "Cyber Security Intern",
            "company": "Hackers10 Pvt Ltd",
            "location": "Remote",
            "dates": "April 2025 - May 2025",
            "bullet_points": [
                "Performed web application vulnerability assessments using OWASP ZAP and Burp Suite.",
                "Simulated Phishing attacks to evaluate user awareness and improve training strategies.",
                "Conducted static and dynamic malware analysis on real-world samples like njRAT.",
                "Assessed home Wi-Fi security for misconfigurations and weak encryption practices.",
                "Audited cloud infrastructure for security misconfigurations using AWS and Azure tools",
                "Gained experience with tools like Burp Suite, SQLMap, Ghidra, Aircrack-ng, and AWS Security Hub.",
                "Delivered technical reports addressing real-world vulnerabilities, threat mitigation, and security hardening strategies."
            ]
        },
        {
            "title": "Cyber Security Intern",
            "company": "Codec Technologies India",
            "location": "Remote",
            "dates": "February 2025 - May 2025",
            "bullet_points": [
                "Engineered security tools across network, web, and cloud.",
                "Built an IDS with Python, Scapy, Snort.",
                "Developed a Python-based vuln scanner using Nmap, OWASP ZAP.",
                "Create a password manager (Python + tinker).",
                "Implemented ML based phishing detection (Scikit-learn, BeautifulSoup).",
                "Built a blockchain voting system (Solidity, Ethereum).",
                "Secured cloud file storage with AES + AWS S3.",
                "Simulated ransomware attacks (PyCrypto, VMs).",
                
            ]
        },
        {
            "title": "Cyber Security Analyst Intern",
            "company": "NullClass",
            "location": "Internship",
            "dates": "September 2024  - Dec 2024",
            "bullet_points": [
                "Developed a web honeypot for testing OWASP TOP 10.",
                "Developed TryHackMe boot to root machine, based on OWASP TOP 10.",
                "Completed HackTheBox insane machines during the time.",
                "Published report on medium regarding hackthebox machines and cybersecurity topics."
            ]
        },
    ],
    "education": [
        {
            "degree": "Bachelor of Technology",
            "major": "Computer Science and Technology",
            "university": "Dr. A.P.J. Abdul Kalam Technical University",
            "location": "Sitapur Road, Lucknow",
            "dates": "November 2022 - Present",
            "gpa": "7.8 / 10.0"
        }
    ],
    "skills": {
        "Programming Languages": ["Python", "C", "C++", "Crystal", "HTML", "Ruby", "Rust", "JavaScript"],
        "Cybersecurity Tools": ["Web Application Security Assessment", "Social Engineering", "CTF", "VAPT", "Intrusion Detection", "Secure Coding", "Windows", "Active Directory", "Firewalls", "OWASP", "Reporting", "Automation", "Red Teaming", "Security Research", "Rish Management", "Kali Linux", "Docker", "Virtualbox", "VMWare", "SOAR", "EDR", "Access Control","Incident Response", "Disaster Recovery", "Surface Analysis", "Attack Surface","Cloud Engineers","DevOps","Code Security","Sonarqube", "Cryptography", "Bug Bounty", "Recon", "Wi-Fi Hacking", "WPA", "Security Testing", "Network Security Testing", "zsh", "shell scripting", "Leadership", "Cybersecurity Incident Management", "Cybersecurity Law", "Cyber Policy", "Internet of Things (IoT)","HTML Scripting", "Hardware Hacking", "Command Line Interface", "Network Administrator", "Cyber Threat Intelligence (CTI)", "Digital Forensics", "Android Testing","OSINT", "Privacy Compliance", "Privacy Compliance", "Source Intelligence", "Source Intelligence", "DevSecOps", "Cyber Defense", "Information Security Management System", "Threat & Vulnerability Management", "Malware Analysis", "Report Writing", "Computer Forensics", "Network Forensics", "Internet Protocol Suite (TCP/IP)", "Networking", "Web Application Security", "Google Hacking", "Security Awareness", "Problem Solving", "Security", "Governance, Risk Management, and Compliance (GRC)","Security Systems", "Security Information and Event Management (SIEM)", "Network Security"," Information Security", "Vulnerability Assessment", "Application Security", "SQL", "Linux", "Python", "Penetration Testing"],
    },
   "ctf": [
	"DreamHack CTF Season 7 #9",
	"Hackfinity - TryHackMe",
	"Advent of Cyber 2024 - TryHackMe"
    ],
    "projects": [
        {"name": "Ghost Phish: Bash based tool for simulating phishing attacks, offering customizable phishing sites, and real-time user tracking to help test and improve cybersecurity defenses", "url":"https://github.com/aenoshrajora/Ghost-Phish"},
        {"name": "Shadow Recon: It is an automated reconnaissance tool that combines top OSINT ad scanning tools into a single seamless process. Ideals for pentesters and bug bounty hunters who want to automate their recon process", "url": "https://github.com/aenoshrajora/Shadow-Recon"},
        {"name": "PhantomMist: A powerful password spraying tool designed for penetration test and security assessments. It automates large-scale authentication attempts while minimizing detection, supporting multiple protocols and customizable attack configurations", "url": "https://github.com/aenoshrajora/PhantomMist"},
        {"name": "VulneraX: It is an advanced, high-performance XSS scanner built with rust, designed to help security researchers and bug bounty hunters detect cross-site payloads, and intelligent request handling to automate web security testing.", "url": "https://github.com/aenoshrajora/VulneraX"},
        {"name": "Ceasar Cipher: A software with GUI compatibility designed for encrypting and decryption test using the Caesar Cipher Algorithm.", "url": "https://github.com/aenoshrajora/Caesar-Cipher-GUI"},
        {"name": "Web Honeypot: A deliberately vulnerable web application covering the OWASP Top 10 vulnerabilities, designed for educational purposes with challenges, solutions, and best practices for remediation.", "url":"https://github.com/aenoshrajora/web-honeypot"},
        {"name": "SOAR EDR Automation: Developed a workflow where the user will get an message whether the victim machine is infected with malware or not. It will isolate the machine from rest of the network, and inform the administrators and client about the risk. The message will be send via Tines to Slack, Email and the detection will be done by LimaCharlie", "url":"https://github.com/aenoshrajora/SOAR-EDR-Automation"},
        {"name": "Network Scanner: A script designed after Nmap which contains the features of changing Mac address, can record keystroke, sniff password and scan for vulnerabilities present in the target ip address", "url":"https://github.com/aenoshrajora/Network-Scanner"},
        {"name": "Packet Sniffer: A versatile packet sniffer tool designed for network analysis and security auditing purposes. The packet sniffer tool offers comprehensive capabilities to capture and analyze network traffic in real-time, providing insights into network activities, protocols, and potential security vulnerabilities", "url": "https://github.com/aenoshrajora/Packet-Sniffer"},
        {"name": "Hash Vanquisher: It is a tool designed to crack various types of hash values using multiple APIs", "url":"https://github.com/aenoshrajora/Hash-Vanquisher"},
        {"name": "Virus Voyager: Unleashing the Power of Analysis, your ultimate malware solution", "url":"https://github.com/aenoshrajora/Virus-Voyager"}
    ],
    "certifications": [
        {"name": "Red Team Learning Path", "company": "TryHackMe", "url":"https://tryhackme.com/certificate/THM-JHHMI99YG3"},
        {"name": "Jr Penetration Tester", "company": "TryHackMe", "url":"https://tryhackme.com/certificate/THM-SGKZKF9FA7"},
        {"name": "Google Cybersecurity Specialization", "company": "Google", "url":"https://www.coursera.org/account/accomplishments/specialization/LHDXX4K52WRB"},
        {"name": "Automate Cybersecurity Tasks", "company": "Google", "url":"https://www.coursera.org/account/accomplishments/records/328YWWWZ1CKD"},
        {"name": "Put it to Work: Prepare for Cybersecurity Jobs", "company": "Google", "url": "https://www.coursera.org/account/accomplishments/records/AFD3MPAT2AZM"},
        {"name": "Certified in Cybersecurity (CC)", "company": "ISC2", "url": "https://isc2.obrizum.io/org/cc/certificate/8056bb16-cd32-41d6-b689-0890c3037dd1"},
        {"name": "Domain 1: Security Principles", "company": "ISC2", "url": "https://isc2.obrizum.io/org/cc/certificate/e9a6391c-98ed-40d5-bfcc-4443005bbdc0"},
        {"name": "Domain 2: Incident Response Business Continuity and Disaster Recovery Concepts", "company": "ISC2", "url":"https://isc2.obrizum.io/org/cc/certificate/e9a6391c-98ed-40d5-bfcc-4443005bbdc0"},
        {"name": "Domain 3: Access Control Concepts", "company":"ISC2", "url":"https://isc2.obrizum.io/org/cc/certificate/9ec1025a-3177-4b52-8648-f179995562db"},
        {"name": "Domain 4: Network Security", "company":"ISC2", "url":"https://isc2.obrizum.io/org/cc/certificate/6bfa261c-af61-43e9-b8a9-b12469761579"},
        {"name": "Domain 5: Security Operations", "company" : "ISC2", "url": "https://isc2.obrizum.io/org/cc/certificate/9570b558-1941-4345-ad8f-174f5ec8266e"},
        {"name": "Cyber Threat Management", "company": "Cisco", "url": "https://www.credly.com/badges/13eff252-9fe4-4de8-86da-49867a79f27e/linked_in_profile"},
        {"name": "Junior Cybersecurity Analyst Career Path", "company": "Cisco", "url": "https://www.credly.com/badges/5fc0c412-a1f9-452b-85d6-81c56b572897/linked_in_profile"},
        {"name": "Sound the Alarm: Detection and Response", "company": "Google", "url": "https://www.coursera.org/account/accomplishments/records/A5R6CY9EBFS6"},
        {"name": "Assets, Threats, and Vulnerabilities", "company": "Google", "url": "https://www.coursera.org/account/accomplishments/records/7WKUEGXVT56Z"},
        {"name": "Endpoint Security", "company": "Cisco", "url": "https://www.credly.com/badges/9bbf12a0-bb8c-471c-9b0c-51a40d4de6db/linked_in_profile"},
        {"name": "Networking Devices and Initial Configuration", "company":"Cisco", "url":"https://www.credly.com/badges/3cbb4131-267c-4749-8f66-3c8884e0aaec/linked_in_profile"},
        {"name": "Tools of the Trade: Linux and SQL", "company":"Google", "url": "https://www.coursera.org/account/accomplishments/records/BBR65PDR3JLT"},
        {"name": "Connect and Protect: Networks and Network Security", "company":"Google", "url":"https://www.coursera.org/account/accomplishments/records/7U7FTWFMUYT7"},
        {"name": "Ethical Hacker", "company":"Cisco", "url":"https://www.credly.com/badges/42719187-8ae9-4190-a3cb-f70c7fde8359/linked_in_profile"},
        {"name": "Network Defense", "company":"Cisco", "url": "https://www.credly.com/badges/45af9c79-b0cf-4549-8eb3-29fd53009fa6/linked_in_profile"},
        {"name": "Foundations of Cybersecurity", "company":"Google", "url":"https://www.coursera.org/account/accomplishments/records/3JY6QEDV6FFQ"},
        {"name": "Play If Safe: Manage Security Risks", "company":"Google", "url": "https://www.coursera.org/account/accomplishments/records/Z9SLFR3Y2MKT"},
        {"name": "Advanced Open Source Intelligence and Privacy", "company": "EC-Council", "url": "https://codered.eccouncil.org/certificate/063e3c6c-5268-4ccd-85aa-1a4c65f44e56"},
        {"name": "Applied Attack Surface Analysis and Reduction for Vulnerability Assessment", "company": "EC-Council", "url": "https://codered.eccouncil.org/certificate/b6bbc0da-d5ed-4dce-aed5-fcfd510aad8a?logged=true"},
        {"name": "Applied HTML5 Security", "company": "EC-Council", "url": "https://codered.eccouncil.org/certificate/64e11389-21df-4e99-af58-b92023a94c4e"},
        {"name": "Code Security with SonarQube", "company":"EC-Council", "url": "https://codered.eccouncil.org/certificate/b9b7ebc4-093a-49c8-99f0-d58c043bf01e"},
        {"name": "Cyber Warfare - Defense Against Nation-State Threats", "company":"EC-Council", "url": "https://codered.eccouncil.org/certificate/65fd17c3-f739-42c8-9832-bc713d76fd00"},
        {"name": "Digital Forensics Essentials (DFE)", "company": "EC-Council", "url": "https://codered.eccouncil.org/certificate/1c0d4c76-f34c-467b-9ae3-82d3e61698b2"},
        {"name": "Ethical Hacking Essentials (EHE)", "company": "EC-Council", "url": "https://codered.eccouncil.org/certificate/c564076a-b462-417c-803c-ee61651819fb"},
        {"name": "Ethical Hacking with Ruby for Beginners", "company": "EC-Council", "url": "https://codered.eccouncil.org/certificate/8673f78a-756d-4ff3-90d5-eafb00503d65"},
        {"name": "Foundations of Hacking and Pentesting Android Apps", "company": "EC-Council", "url": "https://codered.eccouncil.org/certificate/3f76de65-9546-4b87-ad92-0079d3c5b638"},
        {"name": "Hacking WEP/WPA/WPA2 Wi-Fi Networks Using Kali Linux 2.0", "company": "EC-Council", "url": "https://codered.eccouncil.org/certificate/56735e29-faf5-47ec-bc13-b01b3d9cab59"},
        {"name": "Hands-on Cryptography with C++", "company": "EC-Council", "url": "https://codered.eccouncil.org/certificate/178a097e-a36e-45d4-b07f-0c78b3cc5a58"},
        {"name": "Hands-on Linux for DevOps & Cloud Engineers", "company": "EC-Council", "url": "https://codered.eccouncil.org/certificate/215bb27e-b6ab-4cae-9345-16dcab3bc264"},
        {"name": "Linux Command Line - From Zero to Expert", "company": "EC-Council", "url": "https://codered.eccouncil.org/certificate/9c5e10b5-9016-4a0d-8ef7-f087d07195cc"},
        {"name": "Network Defense Essentials (NDE)", "company": "EC-Council", "url": "https://codered.eccouncil.org/certificate/6d888f8e-ae62-4453-b3c0-ad1cf8828e2f"},
        {"name": "Practical DevSecOps with GitHub Actions", "company": "EC-Council", "url": "https://codered.eccouncil.org/certificate/8e189414-2da2-44d6-8b83-5b500a4af6e3"},
        {"name": "Practical Internet of Things Hacking", "company": "EC-Council", "url": "https://codered.eccouncil.org/certificate/78ca05a2-00d9-4697-830d-6123d44d4e28"},
        {"name": "Python for Absolute Beginners", "company": "EC-Council", "url": "https://codered.eccouncil.org/certificate/9b5b8cdb-a2fc-435e-a715-f29458bcd68c"},
        {"name": "Recon for Pentesting & Bug Bounties", "company": "EC-Council", "url": "https://codered.eccouncil.org/certificate/7807ff63-3314-4ac9-94ab-b59c3368db57"},
        {"name": "Shell Scripting with Z Shell", "company": "EC-Council", "url": "https://codered.eccouncil.org/certificate/09b98734-86f3-4604-903e-53b6b01d72b0"},
        {"name": "The Leadership Skills for Cybersecurity Professionals", "company": "EC-Council", "url": "https://codered.eccouncil.org/certificate/843f4031-d540-4617-bc27-5d04f3d07469"},
        {"name": "Web Application Security Testing with Google Hacking", "company": "EC-Council", "url": "https://codered.eccouncil.org/certificate/0f8b2b9c-76b8-4ad8-9397-e73eca1bb770"}   
    ]
}

@app.route('/')
def index():
    return render_template('index.html', resume=resume_data)

if __name__ == '__main__':
    app.run(debug=True)
