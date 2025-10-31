# 🔍 Nmap Scan Analyzer

A beginner-friendly Python CLI tool that parses and analyzes Nmap XML scan results with AI-powered service explanations.

![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## ✨ Features

- 📄 **XML Parser** - Extracts host IPs, status (up/down), open ports, and service information
- 🎨 **Beautiful Output** - Color-coded, formatted console display using Rich library
- 🤖 **AI-Powered Explanations** - Local dictionary providing detailed service explanations
- 🔒 **Security Insights** - Risk assessment for each discovered service
- 📊 **Security Summary** - Overview of risk distribution across all hosts
- 🚀 **Easy to Use** - Simple command-line interface
- 📚 **Well-Documented** - Beginner-friendly with comprehensive comments

## 🎯 Perfect For

- **Students** learning about network security and Nmap
- **Security enthusiasts** analyzing their own networks
- **System administrators** documenting network scans
- **Anyone** wanting to understand Nmap scan results better

## 📋 Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

## 🚀 Quick Start

### Installation

1. **Clone or download this repository**
   ```bash
   git clone <your-repo-url>
   cd nmap-scan-analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the analyzer with a sample scan file:

```bash
python main.py samples/scan1.xml
```

## 📖 Usage Examples

### Basic Analysis
```bash
python main.py samples/scan1.xml
```

### Analyze Your Own Scan
```bash
# First, create an Nmap scan with XML output
nmap -sV -oX myscan.xml 192.168.1.0/24

# Then analyze it
python main.py myscan.xml
```
## 📂 Explore the Project

- 📄 [main.py](main.py) — CLI entry point  
- 📄 [nmap_analyzer.py](nmap_analyzer.py) — Core analyzer logic  
- 📄 [test_nmap_analyzer.py](test_nmap_analyzer.py) — Unit test for analyzer  
- 📄 [filter_by_ip.py](filter_by_ip.py) — Filter results by IP address  
- 📄 [filter_by_port.py](filter_by_port.py) — Filter results by port  
- 📄 [filter_by_protocol.py](filter_by_protocol.py) — Filter results by protocol  
- 📄 [requirements.txt](requirements.txt) — Python dependencies  
- 📄 [LICENSE](LICENSE) — MIT License  
- 📄 [README.md](README.md) — Project overview  
- 📄 [GETTING_STARTED.md](GETTING_STARTED.md) — Beginner’s guide  
- 📄 [scan1.xml](scan1.xml) — Sample Nmap scan file




## 📁 Project Structure

```
nmap-scan-analyzer/
├── main.py                      # Main CLI application
├── src/
│   └── nmap_analyzer/
│       ├── __init__.py          # Package initialization
│       ├── parser.py            # XML parser module
│       ├── analyzer.py          # Service analyzer with AI dictionary
│       └── display.py           # Results display formatter
├── samples/
│   └── scan1.xml                # Sample Nmap scan file
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── GETTING_STARTED.md           # Beginner's guide
├── LICENSE.txt                  # MIT License
└── .gitignore                   # Git ignore rules
```

## 🔍 What It Analyzes

For each host, the tool extracts and displays:

- **IP Address** - The target's IP address
- **Hostname** - DNS name (if available)
- **Status** - Whether the host is up or down
- **Open Ports** - All discovered open ports
- **Services** - Service name running on each port
- **Product** - Software product name and version
- **AI Explanation** - Detailed explanation of what the service does
- **Security Assessment** - Risk level and security notes

## 🤖 AI-Powered Service Dictionary

The tool includes a curated dictionary with detailed explanations for common services including:

- SSH, Telnet, RDP, VNC (Remote Access)
- HTTP, HTTPS (Web Servers)
- FTP, SMB (File Sharing)
- MySQL, PostgreSQL, MongoDB, Redis, Elasticsearch (Databases)
- SMTP, DNS (Network Services)
- And more!

Each service explanation includes:
- Purpose and common use cases
- Security considerations
- Risk level assessment

## 🛡️ Security Summary

The tool provides a comprehensive security overview:
- Total number of open ports
- Risk distribution (Critical, High, Medium, Low)
- List of critical services requiring immediate attention


## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

- Add more services to the AI dictionary
- Improve service explanations
- Add new features (export to JSON, filtering, etc.)
- Fix bugs or improve documentation
- Share your feedback

## 📝 License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## ⚠️ Disclaimer

This tool is for educational purposes and authorized security testing only. Always ensure you have permission to scan networks and systems. Unauthorized scanning may be illegal.

## 🙏 Acknowledgments

- Built with [Rich](https://github.com/Textualize/rich) for beautiful console output  
- Inspired by the need for beginner-friendly security tools  
- Sample scan data is fictional and for demonstration purposes  
- Project hosted at [github.com/LetsLearn-08/NmapScanAnalyzer](https://github.com/LetsLearn-08/NmapScanAnalyzer)


## 📧 Support

If you encounter any issues or have questions:
1. Check [GETTING_STARTED.md](GETTING_STARTED.md) for common solutions
2. Review the code comments for implementation details
3. Open an issue on GitHub

## 🗺️ Roadmap

Future enhancements planned:
- Export results to JSON, CSV, or HTML
- Filter results by port, service, or risk level
- Compare multiple scans
- Visual statistics and charts
- Vulnerability database integration

---

**Happy Scanning! 🚀**

Made with ❤️ for the security community
