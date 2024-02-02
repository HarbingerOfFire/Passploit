<div style="color:red;">
<pre>
██████╗  █████╗ ███████╗███████╗██████╗ ██╗      ██████╗ ██╗████████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
██████╔╝███████║███████╗███████╗██████╔╝██║     ██║   ██║██║   ██║   
██╔═══╝ ██╔══██║╚════██║╚════██║██╔═══╝ ██║     ██║   ██║██║   ██║   
██║     ██║  ██║███████║███████║██║     ███████╗╚██████╔╝██║   ██║   
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝
</pre>
</div>

# PASSWORD EXPLOITATION FRAMEWORK
## Description
Passploit was made as an alternative to hashcat and works as an all in one system to crack password hashes as well as create wordlists, rule files, and hashes. It is currently created to be run fully with python 3 (being created on python 3.11.6) and as of last commit has no known issues. 

## Setup
This repository can be easily retrieved using 
`git clone https://github.com/HarbingerOfFire/Passploit`

After it is retrieved, it has a built in setup sequence that can be run using the following command:

`python3 passploit.py --setup`

The default wordlist `rockyou.txt` can't be used until it is unzipped. 

## Usage
### Hash Cracking
The main use of this program can bee simply used. Just supply the filename containing the hashes, and we can do the rest. 
The algorithm of the hash is automatically found thanks to an adpation of the [Hash Identifier code created by Zion3R](https://github.com/blackploit/hash-identifier).
The most simple version of running passploit is shown below:

`python3 passploit.py -f hashes.txt`

Using the `-w` or `-r` flags, a wordlist and rule list can be customly defined, respectively. By default, they are set to the `rockyou.txt` wordlist and `OneRuleToRuleThemAll.rule` rulefile. 

### Wordlist generation.
This code also has a wordlist generator in it. To use it use the following command:

`python3 passploit.py -g wordlist -u [http://example.com]`

The wordlist geneerator requires a `--url` flag to retrieve words to make the wordlist. It parses the paragraphs and finds some of the words that seem large enough and common enough to be passwords. It will also find links on the provided url to expand the search of words.

### Rule file generation
The code runs on hashcat rules, and can create a randomized set of rules to a desired length. The following command initiates rulefile generation.

`python3 passploit.py -g rulefile`

It will then inquiry about how many rules you want to create, and then automatically create the rules.

### Hash generator
The hash generator was a last minute add-on and just uses the hashlib library. It can be used with the command

`python3 passploit.py -H [text_to_hash]`

It will then inquiry about the algorithm and hash the text.

### Other Flags
All 4 uses of this program write their results to an outfile. There is a standardized outfile name that will look something like `passploit_1706842959868605000.txt`. The name can manually set using the `-o` flag.

Verbosity can be set to 0 if you want to see what words from the wordlist the cracker is currently on. To do this set the `-v` flag to `0`

## CREDIT
Rule files found from all around github, starting at [OneRuleToRuleThemAll](https://github.com/stealthsploit/Optimised-hashcat-Rule) and drawing from their experience. Those sources also provided numerous wordlists.

Again, the hash identifier code was provided by [Zion3r](https://github.com/blackploit/hash-identifier).
