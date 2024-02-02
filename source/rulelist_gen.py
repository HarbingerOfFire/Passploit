import string, random, json

class gen_rulelist:
    def __init__(self, num, outfile, verbose) -> None:
        self.num=num
        self.X = list(string.printable[:-4])
        self.len = [1, 2, 3, 4, 5, 6]
        self.rule=json.load(open("json/rule_rules.json", "r"))
        self.alphabet=json.load(open("json/alphabet.json", "r"))
        self.letter_nums=list(self.alphabet.keys())
        self.keys=list(self.rule.keys())
        self.outfile=open(outfile, "w")
        self.verbose=verbose
        self.write_rules()

    def create_rule(self):
        rule=""
        for i in range(random.choice(self.len)):
            key=random.choice(self.keys)
            value=self.rule[key]
            for i in value:
                if i=="N":
                    key+=random.choice(self.letter_nums)
                if i=="X":
                    key+=random.choice(self.X)
            rule+=key
        return rule
    
    def write_rules(self):
        for i in range(self.num):
            rule=self.create_rule()
            if self.verbose == '0':
                print(f"[+] Writing rule: {rule}")
            self.outfile.write(rule+"\n")


if __name__=='__main__':
    generator=gen_rulelist(152016, "rulelist.rule")