#RULES GOTTEN AND DEFINED FROM
#https://hashcat.net/wiki/doku.php?id=rule_based_attack
import json

class rules:
    def __init__(self) -> None:
        self.ln=self.__letter_to_num
        self.memory=""

    def __letter_to_num(self, letter:str):
        dict=json.load(open("json/alphabet.json", "r"))
        return dict[letter]

    def passthrough(self, string, rule:str):
        return string, rule[1:]
    
    def uppercase(self, string, rule:str):
        try:
            string=string.upper()
            return string, rule[1:]
        except:
            return "REJECTED", rule[1:]
    
    def lowercase(self, string:str, rule):
        try:
            string=string.lower()
            return string, rule[1:]
        except:
            return "REJECTED", rule[1:]
    
    def C_first(self, string:str, rule):
        try:
            string=string[0].upper()+string[1:]
            return string, rule[1:]
        except:
            return "REJECTED", rule[1:]
    
    def L_first(self, string: str, rule):
        try:
            string=string[0].lower()+string[1:]
            return string, rule[1:]
        except:
            return "REJECTED", rule[1:]
    
    def togglecase(self, string:str, rule):
        try:
            string=string.swapcase()
            return string, rule[1:]
        except:
            return "REJECTED", rule[1:]

    def toggle_at_n(self, string:str, rule):
        try:
            string=list(string)
            string[self.ln(rule[1])%len(string)]=string[self.ln(rule[1])%len(string)].swapcase()
            string="".join(string)
            return string, rule[2:]
        except:
            return "REJECTED", rule[2:]
    
    def reverse(self, string:str, rule):
        try:
            string=string[::-1]
            return string, rule[1:]
        except:
            return "REJECTED", rule[1:]
    
    def duplicate(self, string, rule):
        try:
            string=string*2
            return string, rule[1:]
        except:
            return "REJECTED", rule[1:]
    
    def duplicate_n(self, string:str, rule):
        try:
            string=string*self.ln(rule[1])
            return string, rule[2:]
        except:
            return "REJECTED", rule[2:]
    
    def reflect(self, string:str, rule):
        try:
            string=string+string[::-1]
            return string, rule[1:]
        except:
            return "REJECTED", rule[1:]
    
    def rotate_left(self, string, rule):
        try:
            string=string[1:]+string[0]
            return string, rule[1:]
        except:
            return "REJECTED", rule[1:]

    def rotate_right(self, string, rule):
        try:
            string=string[-1]+string[:-1]
            return string, rule[1:]
        except:
            return "REJECTED", rule[1:]
    
    def append(self, string, rule):
        try:
            string+=rule[1]
            return string, rule[2:]
        except:
            return "REJECTED", rule[2:]
    
    def prepend(self, string, rule):
        try:
            string=rule[1]+string
            return string, rule[2:]
        except:
            return "REJECTED", rule[2:]

    def trunc_left(self, string, rule):
        try:
            string=string[1:]
            return string, rule[1:]
        except:
            return "REJECTED", rule[1:]
    
    def trunc_right(self, string, rule):
        try:
            string=string[:-1]
            return string, rule[1:]
        except:
            return "REJECTED", rule[1:]
    
    def delete_n(self, string:str, rule):
        try:
            num=self.ln(rule[1])%len(string)
            string=list(string)
            string[num]=""
            string="".join(string)
            return string, rule[2:]
        except:
            return "REJECTED", rule[2:]
    
    def extract(self, string:str, rule):
        try:
            string=string[self.ln(rule[1]):self.ln(rule[2])]
            return string, rule[3:]
        except:
            return "REJECTED", rule[3:]
    
    def omit(self, string:str, rule):
        try:
            ranges=(self.ln(rule[1]),self.ln(rule[2]))
            string=string.replace(string[ranges[0]:ranges[1]], "")
            return string, rule[3:]
        except:
            return "REJECTED", rule[3:]
    
    def insert(self, string, rule):
        try:
            string=list(string)
            num=self.ln(rule[1])%len(string)
            string[num-1]+=rule[2]
            string="".join(string)
            return string, rule[3:]
        except:
            return "REJECTED", rule[3:]
    
    def overwrite(self, string, rule):
        try:
            string=list(string)
            num=self.ln(rule[1])%len(string)
            string[num]=rule[2]
            string="".join(string)
            return string, rule[3:]
        except:
            return "REJECTED", rule[3:]
    
    def trunc_at_n(self, string, rule):
        try:
            num=self.ln(rule[1])%len(string)
            string=string[:num]
            return string, rule[2:]
        except:
            return "REJECTED", rule[2:]
    
    def replace(self, string:str, rule):
        try:
            string=string.replace(rule[1],rule[2])
            return string, rule[3:]
        except:
            return "REJECTED", rule[3:]

    def purge(self, string, rule):
        try:
            string=string.replace(rule[1], "")
            return string, rule[2:]
        except:
            return "REJECTED", rule[2:]

    def duplicate_first(self, string, rule):
        try:
            string=(string[0]*(self.ln(rule[1])+1))+string[1:]
            return string, rule[2:]
        except:
            return "REJECTED", rule[2:]
    
    def duplicate_last(self, string, rule):
        try:
            string=string[:-1]+(string[-1]*(self.ln(rule[1])+1))
            return string, rule[2:]
        except:
            return "REJECTED", rule[2:]
    
    def duplicate_all(self, string, rule):
        try:
            new_string=''
            for char in string:
                new_string+=char*2
            return new_string, rule[1:]
        except:
            return "REJECTED", rule[1:]
    
    def swap_first(self, string, rule):
        try:
            string=list(string)
            string=string[1]+string[0]+"".join(string[2:])
            return string, rule[1:]
        except:
            return "REJECTED", rule[1:]

    def swap_last(self, string, rule):
        try:
            string=list(string)
            string="".join(string[:-2])+string[-1]+string[-2]
            return string, rule[1:]
        except:
            return "REJECTED", rule[1:]
    
    def swap_at_n(self, string, rule):
        try:
            num=self.ln(rule[1])
            num2=self.ln(rule[2])
            string=list(string)
            string[num], string[num2] = string[num2], string[num]
            string="".join(string)
            return string, rule[3:]
        except:
            return "REJECTED", rule[3:]
    
    def increment(self, string, rule):
        try:
            num=self.ln(rule[1])%len(string)
            string=list(string)
            string[num]=chr(ord(string[num])+1)
            string="".join(string)
            return string, rule[2:]
        except:
            return "REJECTED", rule[2:]
    
    def decrement(self, string, rule):
        try:
            num=self.ln(rule[1])%len(string)
            string=list(string)
            string[num]=chr(ord(string[num])-1)
            string="".join(string)
            return string, rule[2:]
        except:
            return "REJECTED", rule[2:]
    
    def replace_n_increment(self, string, rule):
        try:
            num=self.ln(rule[1])%len(string)
            string=list(string)
            string[num]=string[num+1]
            string="".join(string)
            return string, rule[2:]
        except:
            return "REJECTED", rule[2:]
    
    def replace_n_decrement(self, string, rule):
        try:
            num=self.ln(rule[1])%len(string)
            string=list(string)
            string[num]=string[num-1]
            string="".join(string)
            return string, rule[2:]
        except:
            return "REJECTED", rule[2:]
    
    def duplicate_block_front(self, string, rule):
        try:
            num = self.ln(rule[1])
            string=string[:num]+string
            return string, rule[2:]
        except:
            return "REJECTED", rule[2:]
    
    def duplicate_block_back(self, string, rule):
        try:
            num = self.ln(rule[1])
            string=string+string[-num:]
            return string, rule[2:]
        except:
            return "REJECTED", rule[2:]

    def title_case(self, string: str, rule):
        try:
            string=string.title()
            return string, rule[1:]
        except:
            return "REJECTED", rule[1:]
    
    def title_case_sep(self, string:str, rule):
        try:
            delimeter=rule[1]
            string=string.split(delimeter)
            string = delimeter.join([part.capitalize() for part in string])
            return string, rule[2:]
        except:
            return "REJECTED", rule[2:]

    def toggle_after_n(self, string, rule):
        try:
            num=self.ln(rule[1])
            delimeter=rule[2]
            parts=string.split(delimeter)
            part_of_parts=list(parts[num+1])
            part_of_parts[0]=part_of_parts[0].swapcase()
            parts[num+1]="".join(part_of_parts)
            return delimeter.join(parts), rule[3:]
        except:
            return "REJECTED", rule[3:]

    def append_memory(self, string, rule):
        try:
            string+=self.memory
            return string, rule[1:]
        except:
            return "REJECTED", rule[1:]
    
    def prepend_memory(self, string, rule):
        try:
            string=self.memory+string
            return string, rule[1:]
        except:
            return "REJECTED", rule[1:]
    
    def memorize(self, string, rule):
        try:
            self.memory=string
            return string, rule[1:]
        except:
            return "REJECTED", rule[1:]

    def reject_less(self, string, rule):
        try:
            if len(string) < self.ln(rule[1]):
                return "REJECTED", rule[2:]
            else:
                return string, rule[2:]
        except:
            return "REJECTED", rule[2:]

    def reject_greater(self, string, rule):
        try:
            if len(string) > self.ln(rule[1]):
                return "REJECTED", rule[2:]
            else:
                return string, rule[2:]
        except:
            return "REJECTED", rule[2:]
        
    def reject_equal(self, string, rule):
        try:
            if len(string) == self.ln(rule[1]):
                return "REJECTED", rule[2:]
            else:
                return string, rule[2:]
        except:
            return "REJECTED", rule[2:]
        
    def reject_contain(self, string:str, rule):
        try:
            if string != string.replace(rule[1], ""):
                return "REJECTED", rule[2:]
            else:
                return string, rule[2:]
        except:
            return "REJECTED", rule[2:]
        
    def reject_not_contain(self, string:str, rule):
        try:
            if string == string.replace(rule[1], ""):
                return "REJECTED", rule[2:]
            else: 
                return string, rule[2:]
        except:
            return "REJECTED", rule[2:]
        
    def reject_equal_first(self, string:str, rule):
        try:
            if string[1] != rule[1]:
                return "REJECTED", rule[2:]
            else:
                return string, rule[2: ]
        except:
            return "REJECTED", rule[2:]
        
    def reject_equal_last(self, string:str, rule):
        try:
            if string[-1] != rule[1]:
                return "REJECTED", rule[2:]
            else:
                return string, rule[2:]
        except:
            return "REJECTED", rule[3:]
        
    def reject_char_at_n(self, string:str, rule):
        try:
            num = self.ln(rule[1])
            if string[num] != rule[2]:
                return "REJECTED", rule[3:]
            else:
                return string, rule[3:]
        except:
            return "REJECTED", rule[3:]
        
    def __count_char(self, string, target_char):
        count = 0
        for char in string:
            if char == target_char:
                count+=1
        return count
    
    def reject_char_n_times(self, string, rule):
        try:
            if self.__count_char(string, rule[2]) < self.ln(rule[1]):
                return "REJECTED", rule[3:]
            else:
                return string, rule[3:]
        except:
            return "REJECTED", rule[3:]
        
    def reject_memory(self, string, rule):
        try:
            if string ==self.memory:
                return "REJECTED", rule[1:]
            else:
                return string, rule[1:]
        except:
            return "REJECTED", rule[1:]
        
    def left_bit_shift(self, string, rule):
        try:
            index=self.ln(rule[1])
            char_at_index = string[index]
            shifted_char = chr(ord(char_at_index) << 1)
            string = string[:index] + shifted_char + string[index+1:]
            return string, rule[2:]
        except:
            return "REJECTED", rule[2:]
    
    def right_bit_shift(self, string, rule):
        try:
            index=self.ln(rule[1])
            char_at_index = string[index]
            shifted_char = chr(ord(char_at_index) >> 1)
            string = string[:index] + shifted_char + string[index+1:]
            return string, rule[2:]
        except:
            return "REJECTED", rule[2:]

    def extract_memory(self, string, rule):
        try: 
            extraction=self.memory[self.ln(rule[1]):self.ln(rule[1])+self.ln(rule[2])]
            string=list(string)
            index=self.ln(rule[3])
            string[index]=string[index]+extraction
            string="".join(string)
            return string, rule[4:]
        except:
            return "REJECTED", rule[4:]

class analyze_rules(rules):
    def __init__(self) -> None:
        super().__init__()

    def analyze(self, string, rule):
        with open("json/rules.json", "r") as rules:
            rules=json.load(rules)
        while rule != "" and string != "REJECTED":
            string, rule=eval(f"self.{rules[rule[0]]}(string, rule)")
        return string


if __name__=='__main__':
    analyze=analyze_rules()
    plain="p@ssW0rd"
    print(analyze.analyze(plain, ":"))
    print(analyze.analyze(plain, "l"))
    print(analyze.analyze(plain, "u"))
    print(analyze.analyze(plain, "c"))
    print(analyze.analyze(plain, "C"))
    print(analyze.analyze(plain, "t"))
    print(analyze.analyze(plain, "T3"))
    print(analyze.analyze(plain, "r"))
    print(analyze.analyze(plain, "d"))
    print(analyze.analyze(plain, "p2"))
    print(analyze.analyze(plain, "f"))
    print(analyze.analyze(plain, "{"))
    print(analyze.analyze(plain, "}"))
    print(analyze.analyze(plain, "$1$2"))
    print(analyze.analyze(plain, "^1^2"))
    print(analyze.analyze(plain, "["))
    print(analyze.analyze(plain, "]"))
    print(analyze.analyze(plain, "D3"))
    print(analyze.analyze(plain, "x04"))
    print(analyze.analyze(plain, "O12"))
    print(analyze.analyze(plain, "i4!"))
    print(analyze.analyze(plain, "o3$"))
    print(analyze.analyze(plain, "'6"))
    print(analyze.analyze(plain, "ss$"))
    print(analyze.analyze(plain, "@s"))
    print(analyze.analyze(plain, "z2"))
    print(analyze.analyze(plain, "Z2"))
    print(analyze.analyze(plain, "q"))
    print(analyze.analyze(plain, "lMX428"))
    print(analyze.analyze(plain, "uMl4"))
    print(analyze.analyze(plain, "rMr6"))
    print(analyze.analyze(plain, "lMuX084"))
    print(analyze.analyze(plain, "<G"))
    print(analyze.analyze(plain, ">8"))
    print(analyze.analyze(plain, "_7"))
    print(analyze.analyze(plain, "!z"))
    print(analyze.analyze(plain, "/e"))
    print(analyze.analyze(plain, "(h"))
    print(analyze.analyze(plain, ")t"))
    print(analyze.analyze(plain, "=1a"))
    print(analyze.analyze(plain, "%2a"))
    print(analyze.analyze(plain, "rMrQ"))
    print(analyze.analyze(plain, "k"))
    print(analyze.analyze(plain, "K"))
    print(analyze.analyze(plain, "*34"))
    print(analyze.analyze(plain, "L2"))
    print(analyze.analyze(plain, "R2"))
    print(analyze.analyze(plain, "+2"))
    print(analyze.analyze(plain, "-1"))
    print(analyze.analyze(plain, ".1"))
    print(analyze.analyze(plain, ",1"))
    print(analyze.analyze(plain, "y2"))
    print(analyze.analyze(plain, "Y2"))
    print(analyze.analyze(plain, "E"))
    print(analyze.analyze(plain, "e-"))
    print(analyze.analyze(plain, "30-"))