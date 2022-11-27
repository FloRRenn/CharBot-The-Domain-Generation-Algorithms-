import random
from time import mktime, strptime
        
class CharBot:
    def __init__(self, benign_url_file : str, TLD_file : str, output_file, seed : int):
        # init pseudo-randomization
        self.pseudoRandomization(seed)
        
        # Alphanumeric characters and dash
        self.characters = "abcdefghijklmnopqrstuvwxyz0123456789-"
        
        # Read pre-data
        self.benign_url = self.readFile(benign_url_file)
        self.TLDs = self.readFile(TLD_file)
        
        self.output_file = output_file
        
    def pseudoRandomization(self, seed : int):
        random.seed(seed)
        
    def readFile(self, filename : str):
        with open(filename, "r", encoding = 'utf-8') as f:
            data = f.readlines()
        return data
    
    def rand_2_index(self, lenght : int):
        i = random.randint(0, lenght)
        
        while True:
            j = random.randint(0, lenght)
            if i != j:
                break
            
        return i, j

    def replace_char(self, domain_name : list, index : int):
        letters = self.characters.replace(domain_name[index], "")
        domain_name[index] = random.choice(letters)
        return domain_name

    def generate_name(self, old_name : list, i : int, j : int):
        new_name = self.replace_char(old_name, i)
        new_name = self.replace_char(new_name, j)
        return "".join(new_name)
    
    def produce(self):
        with open(self.output_file, 'w+') as f:
            count = 0
            
            for domain in self.benign_url:
                # Get domain name
                name = list(domain.split('.')[0])
                
                # Get 2 random indexes
                i, j = self.rand_2_index(len(name) - 1)
                
                # Generate malicious domain
                malicious_name = self.generate_name(name, i, j)
                malicious_domain = malicious_name + "." + random.choice(self.TLDs)
                
                f.write(malicious_domain)
                
                count += 1
                print(f"Generating {count} domains...", end = "\r")
            
        print(f"Finished. All {count} domains are generated.")

if __name__ == '__main__':
    date = '27/11/2022'
    seed = int(mktime(strptime(date, '%d/%m/%Y'))) 
    
    benign_domain = "./dataset/benign_domains.txt"
    tld_domain = "./dataset/top_level_domains.txt"
    output_file = "./dataset/malicious_domains.txt"
    
    charBot = CharBot(benign_domain, tld_domain, output_file, seed)
    charBot.produce()


