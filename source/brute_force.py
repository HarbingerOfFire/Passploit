import itertools, string, hashlib

class brute_force:
    def __init__(self, hash, algorithm):
        self.hash=hash
        self.characters=string.printable
        self.algorithm=algorithm

    def force_string(self):
        for length in range(1, 25):
            for guess in itertools.product(self.characters, repeat=length):
                hashed_guess=hashlib.new(self.algorithm, "".join(guess).encode()).hexdigest()
                if hashed_guess == self.hash:
                    return ''.join(guess)

if __name__=="__main__":
    target = hashlib.new("sha-512", b"abc").hexdigest()
    bf=brute_force(target, "SHA-512").force_string()
    print(bf)
