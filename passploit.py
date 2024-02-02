import source.args as args, os

arguments=args.args().return_args()
if arguments.setup:
    try:
        print("[+] running setup..")
        os.system("pip install -r requirements.txt")
    except:
        print("[!] Setup failed. Please manually install requirements")

#!/usr/bin/env python3
import rainbowtext
import source.pass_rules as pass_rules
import source.wordlist_gen as wordlist_gen
import source.rulelist_gen as rulelist_gen
import source.identify_hash as identify_hash
import source.brute_force as brute_force

logo = """
██████╗  █████╗ ███████╗███████╗██████╗ ██╗      ██████╗ ██╗████████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
██████╔╝███████║███████╗███████╗██████╔╝██║     ██║   ██║██║   ██║   
██╔═══╝ ██╔══██║╚════██║╚════██║██╔═══╝ ██║     ██║   ██║██║   ██║   
██║     ██║  ██║███████║███████║██║     ███████╗╚██████╔╝██║   ██║   
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   
"""
rainbowtext.colors = ["\033[91m","\033[31m","\033[31;2m","\033[91;1m","\033[31;3m","\033[31;4m","\033[38;5;196m"]
print(rainbowtext.text(logo))

if arguments.setup:
    print("[+] Setup complete")
if arguments.hashfile:
    try:
        for line in open(arguments.hashfile, "r"):
            algorithm=identify_hash.Identify(line)
            passer=pass_rules.pass_rules(algorithm, 
                                  line,
                                  arguments.wordlist,
                                  arguments.rulefile,
                                  arguments.verbose)
            plain=passer.get_plain()
            if plain != "No matches found":
                print(f"[+] Password found: {plain}")
            else:
                print(f"[+] No matches found. Resulting to brute force")
                forced=brute_force.brute_force(line, algorithm).force_string()
                if not forced:
                    print(f"[!] Brute Force failed")
                else:
                    print(f"[+] Brute Force Successful: Password Found: {forced}")
            with open(arguments.outfile, "w") as outfile:
                outfile.write(plain)
                print(f"[+] Plain written to {outfile.name}")
    except Exception as e:
        print(f"[!] {e}")
if arguments.generate:
    try:
        if arguments.generate == "wordlist":
            if not arguments.url:
                raise NameError("--url required for use of --wordlist")
            wordlist_gen.gen_wordlist(arguments.url, arguments.outfile, arguments.verbose)
            print(f"[+] Words written to {arguments.outfile}")
        if arguments.generate == "rulefile":
            num=input("[?] How many rules should I generate: ")
            rulelist_gen.gen_rulelist(int(num), arguments.outfile, arguments.verbose)
            print(f"[+] Rules written to {arguments.outfile}")
    except Exception as e:
        print(f"[!] {e}")
if arguments.hash:
    try:
        algorithm=input(f"[?] What Algorithm should I use: ")
        hash=brute_force.hashlib.new(algorithm, arguments.hash.encode()).hexdigest()
        print(f"[+] Hash Successful: {hash}")
        with open(arguments.outfile, "w") as outfile:
                outfile.write(hash)
                print(f"[+] Hash written to {outfile.name}")
    except Exception as e:
        print(f"[!] {e}")