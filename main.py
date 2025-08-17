#!/usr/bin/env python3

import sys
import subprocess

# Auto-install missing dependencies
required = ["python-nmap", "colorama"]
for pkg in required:
    try:
        __import__(pkg.replace("-", ""))
    except ImportError:
        print(f"[!] Missing package: {pkg}. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

import argparse
from scanner import scan_target

def main():
    parser = argparse.ArgumentParser(description="Automated Vulnerability Scanner (CLI)")
    parser.add_argument("-t", "--target", required=True, help="Target host or IP")
    args = parser.parse_args()

    scan_target(args.target)

if __name__ == "__main__":
    main()