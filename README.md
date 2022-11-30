# CharBot: The Domain Generation Algorithms (DGA)
This code is implemented based on paper [CharBot: A Simple and Effective Method for Evading DGA Classifiers](https://arxiv.org/pdf/1905.01078.pdf)

## Usage
```
python charbot.py
```
The output file is a list of domains

## Testing
We have 2 DGA Detecting Algorithms, which is used to test the effect of Charbot on these one. All of these are stored in folder `./tests`
*  Folder `algo_1` is using Random Forest method
*  Folder `algo_2` is using LSTM method

#### How to use
Open these files below to see more details

**1. Train your own model**
```
python test_training.py
```

**2. Predict domain**
```
python test_predicting.py
```
