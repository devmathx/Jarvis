import yaml
import numpy as np

data = yaml.safe_load(open('nlu\\train.yaml', 'r', encoding='utf-8').read()) # Estudar melhor YAML com python

inputs, outputs = [], []

for command in data["commands"]:
    inputs.append(command['input'].lower())
    outputs.append(f"{command['entity']}\{command['action']}")

# Processar texto
chars = set()

for input in inputs + outputs:
    for ch in input:
        if ch not in chars:
            chars.add(ch)
    
# Maoear char-idx
char2idx = {}
idx2char = {}

for i, ch in enumerate(chars):
    char2idx[ch] = i
    idx2char[i] = ch
    
max_seq = max([len(x) for x in inputs])

# Criar o dataset
input_data = np.zeros((len(inputs), max_seq, len(chars)), dtype='int32')

for i, input in enumerate(inputs):
    for k, ch in enumerate(input):
        input_data[i, k, char2idx[ch]] = 1.0
        
        
print(input_data[0])