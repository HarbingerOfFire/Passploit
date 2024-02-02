import argparse, time

class args:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser("Passploit")
        self.init_args()

    def init_args(self):
        self.parser.add_argument("-w", "--wordlist", action="store", default="wordlists/rockyou.txt")
        self.parser.add_argument("-r", "--rulefile", action="store", default="rules/OneRuleToRuleThemAll.rule")
        self.parser.add_argument("-f", "--hashfile", action="store")
        self.parser.add_argument("-o", "--outfile", action="store", default=f"passploit_{time.time_ns()}.txt")
        self.parser.add_argument("-g", "--generate", action="store", choices=["wordlist", "rulefile"])
        self.parser.add_argument("-u", "--url", action="store")
        self.parser.add_argument("-v", "--verbose", action="store", default=1, choices=['0', '1'])
        self.parser.add_argument("-H", "--hash", action="store")
        self.parser.add_argument("-s", "--setup", action="store_true")
    
    def return_args(self):
        return self.parser.parse_args()