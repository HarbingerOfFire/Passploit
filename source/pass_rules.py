import source.rule as rule, hashlib

class pass_rules:
    def __init__(self, _algorithm, _hash, _wordlist, _rulelist, verbose) -> None:
        self.rules = rule.analyze_rules()
        self._algorithm=_algorithm
        self._hash=_hash
        self._filename=_wordlist
        self._rulelist=open(_rulelist, "r").read().splitlines()
        self._wordlist=open(_wordlist, "r", encoding="KOI8-R")
        self.verbose=verbose
    
    def get_plain(self):
        while True:
            plain=self._wordlist.readline().strip()
            if not plain:
                plain=self._wordlist.readline().strip()
                if not plain:
                    return "No matches found"
            if self.verbose == '0':
                print(f"[+] Trying plain: {plain}...", end=" ")
            applied = self.apply_rules(plain)
            if applied != None:
                print("Success")
                return applied
            else: 
                if (self.verbose=='0'): 
                    print("Failed")

    def apply_rules(self, plain):
        for rule in self._rulelist:
            if rule[0] != "#":
                applied=self.rules.analyze(plain, rule.strip())
                if self.test_hash(applied):
                    return applied
        
    def get_hash(self, plain):
        try:
            return hashlib.new(self._algorithm, plain.encode()).hexdigest()
        except:
            print(f"[!] Algorithm {self._algorithm} not usable. Exiting...")
            quit()
    
    def test_hash(self, plain):
        if self.get_hash(plain) == self._hash:
            return True

if __name__=="__main__":
    hash=hashlib.new("SHA512", b"Paossword5").hexdigest()

    pass_r=pass_rules("SHA512", hash, "wordlists/RockYou2021.txt", "rules/OneRuleToRuleThemAll.rule", "0")
    print(f"password: {pass_r.get_plain()}") 