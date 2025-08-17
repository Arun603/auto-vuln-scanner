🔍 Auto Vulnerability Scanner

An automated vulnerability scanning tool that helps security researchers and system administrators detect potential security risks in their applications and networks.

📌 Features

✅ Automated scanning of targets (IP, domain, or web app)

✅ Detects common vulnerabilities (SQLi, XSS, CSRF, etc.)

✅ Lightweight & easy to use

✅ Extensible modular design

✅ Generates structured reports

⚙ Installation

1. Clone the repository



git clone https://github.com/aravind603/auto-vuln-scanner.git

cd auto-vuln-scanner

2. Install dependencies



pip install -r requirements.txt

3. Run the scanner



python main.py -u http://example.com

🛠 Example Usage

python main.py -u http://testphp.vulnweb.com

Output:

[+] Scanning target: http://testphp.vulnweb.com
[!] Found SQL Injection vulnerability at /search.php?q=
[!] Found XSS vulnerability at /comment.php

📊 Roadmap

[ ] Add multi-threading for faster scans

[ ] Integrate with vulnerability databases (CVE, ExploitDB)

[ ] Generate HTML/PDF reports

[ ] Add support for authenticated scanning


🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

📜 License

This project is licensed under the MIT License.


If you like this project, dont forget to star the repo!

