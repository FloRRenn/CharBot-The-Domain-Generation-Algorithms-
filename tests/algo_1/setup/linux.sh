#!
sudo pip3 install virtualenv
virtualenv .venv
source .venv/bin/activate 
pip3 install -r requirements.txt
python train_model.py -p data/raw/dga_domains.csv -o models -v 2
python test_model.py
