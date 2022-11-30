# Run Setup
```bash
// For Linux
sudo chmod +x setup/linux.sh
setup/linux.sh

// For Windows
setup/windows.bat
```

# Training the model

```bash
python train_model.py -p data/raw/dga_domains.csv -o models
``` 

The model training script expects at least two parameters to be passed in:
* `-p` for the path to the source data.
* `-o` where the trained model will be written out.

# Testing the model 
```bash
python test_model.py
```

Runs a trivial test on the model to ensure it has been built.

#  Predict domain name
For an interactive session, where you can type in domains
````
python dga_classify.py <domain>
````

*Query Return Codes*
* `0` - No dga domains were predicted from any of the inputs.
* `2` - No predictions were made, e.g. empty or invalid inputs.
* `3` - Dga domains were predicted
