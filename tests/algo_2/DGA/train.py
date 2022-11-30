import numpy as np
import pandas 

import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.layers import Input, LSTM, Dropout, Embedding, Dense, Conv1D, MaxPooling1D
from tensorflow.keras.preprocessing.sequence import pad_sequences

class DGATrain:
    def __init__(self, domains_file, output_file):
        self.dataset = self.create_pre_training_data(domains_file)
        self.output_file = output_file
        
    def create_pre_training_data(self, domains_file):
        domains = pandas.read_csv(domains_file)
        
        vocab = sorted(set(''.join(domains['domain'].to_list())))
        char2idx = {u:i for i, u in enumerate(vocab)}

        lines = []
        for i, line in enumerate(domains.iloc[:, 0]):
            lines.append([char2idx[c] for c in line])
          
        tensor = pad_sequences(lines, padding = 'post')
        targets = np.array(domains.iloc[:, 1], dtype = np.int32)

        data = tf.data.Dataset.from_tensor_slices(tensor)
        pred = tf.data.Dataset.from_tensor_slices(targets)
        dataset = tf.data.Dataset.zip((data, pred))

        return dataset.batch(1500, drop_remainder = True)
    
    def create_model(self):
        domain_input = Input(shape = (82,), dtype = 'int32', name = 'domain_input')
        
        embedding = Embedding(input_dim = 39, output_dim = 128, input_length = 82, batch_input_shape = [1500, None])(domain_input)
        conv = Conv1D(filters = 128, kernel_size = 3, padding = 'same', activation = 'relu', strides = 1)(embedding)
        pool = MaxPooling1D(pool_size = 2, padding = 'same')(conv)
        lstm = LSTM(64, return_sequences = False)(pool)
        drop = Dropout(0.5)(lstm)
        output = Dense(1, activation = 'sigmoid')(drop)
        
        model = Model(inputs = domain_input, outputs = output)
        return model
    
    def train(self):
        model = self.create_model()
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        
        EPOCHS = 6 
        for i in range(EPOCHS):
            model.fit(self.dataset)
            
        model.save(self.output_file)