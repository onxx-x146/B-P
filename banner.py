#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyfiglet
import sys
import os
import time
import random
import subprocess
from datetime import datetime

current_time = datetime.now().strftime("%H:%M:%S")

print(f"\033[38;5;214m[{current_time}]\033[0m \033[1;32m[INFO]:\033[0m Opening GitHub in Chrome...")

try:
    subprocess.run([
        "am",
        "start",
        "-a", "android.intent.action.VIEW",
        "-d", "https://github.com/onxx-x146",
        "com.android.chrome"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

except subprocess.CalledProcessError:
    print(f"\033[38;5;214m[{current_time}]\033[0m \033[1;33m[WARNING]:\033[0m Could not open Chrome.")
# ============ COLORS ============
class Colors:
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    BOLD    = "\033[1m"
    RESET   = "\033[0m"

BANNER_COLORS = [Colors.RED, Colors.GREEN, Colors.YELLOW, Colors.BLUE,
                 Colors.MAGENTA, Colors.CYAN, Colors.WHITE]

def banner_text(text, font="slant"):
    fig = pyfiglet.Figlet(font=font)
    banner = fig.renderText(text)
    color = random.choice(BANNER_COLORS)
    print(color + banner + Colors.RESET)

def animated_banner(text, font="slant", delay=0.02):
    fig = pyfiglet.Figlet(font=font)
    lines = fig.renderText(text).split("\n")
    color = random.choice(BANNER_COLORS)
    for line in lines:
        print(color + line + Colors.RESET)
        time.sleep(delay)

def loader():
    for i in range(1, 21):
        bar = "█" * i + "░" * (20 - i)
        percent = (i * 5)
        sys.stdout.write(f"\r  [{bar}] {percent}% ")
        sys.stdout.flush()
        time.sleep(0.05)
    print(f"\n  {Colors.GREEN}✅ Banner Ready!{Colors.RESET}\n")

def menu():
    print(f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════╗
║       🚀  BANNER MAKER TOOL 🚀              ║
║       Created by: [YOUR NAME]                ║
╚══════════════════════════════════════════════╝
{Colors.RESET}
{Colors.GREEN}  [1] 🎨 Cool Banner Generator
{Colors.YELLOW}  [2] 🔥 Animated Banner
{Colors.BLUE}  [3] 📋 Available Fonts List
{Colors.MAGENTA}  [4] 🛡️  Random Hacker-Style Banner
{Colors.RED}  [5] ❌ Exit
{Colors.RESET}
""")

def list_fonts():
    fonts = sorted(pyfiglet.FigletFont.getFonts())
    print(f"\n{Colors.CYAN}Available Fonts ({len(fonts)} total):\n{Colors.RESET}")
    for i, f in enumerate(fonts, 1):
        print(f"  {Colors.YELLOW}{i:3}. {Colors.WHITE}{f}{Colors.RESET}")
    print()

def random_hacker_banner():
    hackers = [
        "SYSTEM HACKED", "ROOT ACCESS", "1337 H4X0R",
        "TERMINAL MASTER", "CYBER PUNK", "UNAUTHORIZED",
        "ACCESS GRANTED", "PWNED", "PENTEST LAB",
        "DEEP WEB", "GHOST MODE", "BLADE RUNNER",
        "NEON CYBER", "ZERO DAY", "TORMENTA NET"
    ]
    fonts = ["slant", "3-d", "5lineoblique", "big", "doh",
             "lean", "mini", "ogre", "sharp", "speed"]
    target = random.choice(hackers)
    font = random.choice(fonts)
    animated_banner(target, font=font, delay=0.01)

def main():
    os.system("clear")
    banner_text("BANNER MAKER", font="slant")
    print(f"\n  {Colors.CYAN}Made with ❤️ in Termux{Colors.RESET}\n")
    loader()

    while True:
        menu()
        choice = input(f"  {Colors.GREEN}[!] Select: {Colors.RESET}").strip()

        if choice == "1":
            text = input(f"  {Colors.YELLOW}[?] Enter text: {Colors.RESET}").strip()
            font = input(f"  {Colors.YELLOW}[?] Font (default=slant): {Colors.RESET}").strip()
            if not font:
                font = "slant"
            try:
                banner_text(text, font=font)
            except Exception:
                print(f"  {Colors.RED}Font not found, using default slant{Colors.RESET}")
                banner_text(text, font="slant")
            print()

        elif choice == "2":
            text = input(f"  {Colors.YELLOW}[?] Enter text: {Colors.RESET}").strip()
            font = input(f"  {Colors.YELLOW}[?] Font (default=slant): {Colors.RESET}").strip()
            if not font:
                font = "slant"
            try:
                animated_banner(text, font=font)
            except Exception:
                animated_banner(text, font="slant")
            print()

        elif choice == "3":
            list_fonts()

        elif choice == "4":
            print()
            random_hacker_banner()
            print()

        elif choice == "5":
            print(f"\n  {Colors.RED}Bye! 👋{Colors.RESET}\n")
            sys.exit(0)

        else:
            print(f"  {Colors.RED}Invalid choice! Try again.{Colors.RESET}")

if __name__ == "__main__":
    main()
    
