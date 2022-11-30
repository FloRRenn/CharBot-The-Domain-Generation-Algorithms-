### Model Selection
Finally once suitable features had been identified, then model selection was performed. This was achieved by fitting a number of naive models from a variety of model families.
Of the model families fitted, Random Forrest was identified as the most suitable.

# Installation and Overview of Solution

All you need is a Google account, run this repo in a light weight temporary cloud session.

## Installation

It is assumed you have Python 3.6 or above installed.

Setup scripts are included for Windows and Linux based environments.
The setup scripts do the following

* Install virtualenv
* Create a virtualenv `.venv`
* Active the virtual env `.venv`
* Install the Python packages in `requirements.txt`
* Register an IPython kernel as used in the Notebooks
* Run the `unittests` with pytest
* Run the `integrationtests` with pytest
* Train the model
* Runs a simple test of the model
* Enters an interactive mode where you can query the model

### Windows

```
setup\windows.bat
```

### MacOS and Linux

You may need to set executable permission on the bash script.

```bash
sudo chmod +x setup\linux.sh
setup\linux.sh
```

## Usage

If you've run the setup scripts above you will have a trained model ready for use.
However if you choose to setup your environment manually here is an overview of the steps that need to be taken.

The following commands assume you're in the root folder of this git repo.

### Training the model

*Windows*
```bash
python train_model.py -p data\raw\dga_domains.csv -o models
```

*Linux and MacOS*
```bash
python train_model.py -p data/raw/dga_domains.csv -o models
``` 

The model training script expects at least two parameters to be passed in:
* `-p` for the path to the source data.
* `-o` where the trained model will be written out.

#### Testing the model
*Windows, Linux, and MacOS*
```bash
python test_model.py
```

Runs a trivial test on the model to ensure it has been built.

#### Querying the model
*Windows, Linux, and MacOS*

For an interactive session, where you can type in domains
````
python dga_classify.py -i
````

To get the prediction for a single or comma separated list of domains
````
python dga_classify.py reddit,facebook.com,google.co.uk
````

##### Query Return Codes
* `0` - No dga domains were predicted from any of the inputs.
* `2` - No predictions were made, e.g. empty or invalid inputs.
* `3` - Dga domains were predicted
