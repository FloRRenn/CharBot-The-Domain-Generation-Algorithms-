import numpy as np
from tensorflow.keras.models import load_model

class DGAPrediction:
    def __init__(self):
        self.CHAR2IDX = {
                        '-': 0, '.': 1, '0': 2, '1': 3, '2': 4, '3': 5,
                        '4': 6, '5': 7, '6': 8, '7': 9, '8': 10, '9': 11,
                        '_': 12, 'a': 13, 'b': 14, 'c': 15, 'd': 16, 'e': 17,
                        'f': 18, 'g': 19, 'h': 20, 'i': 21, 'j': 22, 'k': 23,
                        'l': 24, 'm': 25, 'n': 26, 'o': 27, 'p': 28, 'q': 29,
                        'r': 30, 's': 31, 't': 32, 'u': 33, 'v': 34, 'w': 35,
                        'x': 36, 'y': 37, 'z': 38
                        }
        
    def load_model_h5(self, h5_model_file):
        self.model = load_model(h5_model_file)
        
    def modify_input(self, domains):
        return [domain.lower() for domain in domains]
        
    def get_prob(self, domains):
        vector = np.zeros((len(domains), 82))
        
        for i, domain in enumerate(domains):
            for j, char in enumerate(domain):
                vector[i, j] = self.CHAR2IDX[char] if char in self.CHAR2IDX else -1

        prob = self.model(vector).numpy()
        prob = prob.transpose()[0]
        
        return list(zip(domains, list(prob)))
    
    def predict(self, domains):
        domains = self.modify_input(domains)
        raw_probs = self.get_prob(domains)
        
        result = []
        for domain, prob in raw_probs:
            output = {
                "domain": domain,
                "probability" : prob,
                "isDGA" : True if prob >= 0.5 else False
            }
            
            result.append(output)
            
        return result