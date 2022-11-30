from DGA import DGAPrediction

# Please run ./test_training.py first to get this h5 file
model_file = "./h5_files/model.h5"

model = DGAPrediction()
model.load_model_h5(model_file)

# Testing
domains = ["microsoft.com", "google.com", "facebook.com"
           "asfawfgwa.net", "asjfafaf32325.xyz", "suyag32svdasad.org"]
predict = model.predict(domains)
print(predict)