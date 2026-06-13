# crackx3
A lightweight, high-performance Python hash cracker featuring automatic hash type detection and multi-algorithm brute-force support.
![crackx3-demo](result.png)

## About crackx3
**crackx3** is an efficient CLI tool designed for security professionals and enthusiasts to crack cryptographic hashes. It utilizes `multiprocessing` to maximize CPU usage, ensuring fast and reliable performance during dictionary attacks.

## Features
* **Auto-Detection:** Automatically identifies MD5, SHA1, SHA256, and SHA512 based on hash string length.
* **Brute-Force Mode:** Supports testing against multiple algorithms simultaneously if the hash format is unknown.
* **Optimized Performance:** Built with `ProcessPoolExecutor` for high-speed concurrent processing.
* **User-Friendly CLI:** Clear interface with robust error handling and progress monitoring.

## Requirements & Setup

### Prerequisites
* **Python 3.x**
* A wordlist file (e.g., `rockyou.txt`).

### Installation
1. **Clone the repository:**
```bash
git clone https://github.com/x3bdulaziz/Crackx3.git
```
```bash 
cd Crackx3
```
## 💻 Usage & Options
```bash
python3 crackx3.py --help

-h, --help  show this help message and exit
  -hash HASH  target hash
  -w W        Wordlist path
  -d          Detect Mode
  -b          Brute-force Mode
example:
    python3 crackx3.py -d -hash xws1r5... -w /usr/share/wordlists/rockyou.txt
    python3 crackx3.py -b -hash qef9o4... -w rockyou.txt
```
## Usage Example

You can run the tool as follows:
```bash
python3 crackx3.py -d -hash f7c3bc1d808e04732adf679965ccc34ca7ae3441 -w /usr/share/wordlists/rockyou.txt
```
## output
```bash
==========================================
Welcome to crackx3 Tool
Created by x3bdulaziz
Starting crack... target: f7c3bc1d808e04732adf679965ccc34ca7ae3441
Mode: -d | Algorithm: SHA1
==========================================

[+]Password Found: `123456789`
finished in 0.42seconds. 
```
## Wordlist Preparation:
To keep the repository lightweight and portable, this tool does not include large wordlists. Users are expected to provide their own wordlist.

`Tip` for Kali Linux users: You can typically find a pre-installed wordlist at:`/usr/share/wordlists/rockyou.txt`
