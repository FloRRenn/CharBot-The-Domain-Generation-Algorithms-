from DGA import DGATrain

domain_file = "./dataset/domain_data.csv"
output_file = "./h5_files/model.h5"

# Training
model = DGATrain(domain_file, output_file)
model.train()