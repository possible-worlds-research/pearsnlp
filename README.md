# PeARSNLP

A script collection to do NLP work for the PeARS search engine.

## Installation

We recommend installing the PeARSNLP package in a virtual environment. If you do not have virtualenv installed, you can get it in the following way: 

```
sudo apt update
sudo apt install python3-setuptools
sudo apt install python3-pip
sudo apt install python3-virtualenv
```

Then, create a directory for PeARSNLP, make your virtual environment and install the package and necessary dependency (the code for [WikiNLP](https://github.com/possible-worlds-research/wikinlp)):

```
git clone https://github.com/possible-worlds-research/pearsnlp.git
cd pearsnlp
virtualenv env && source env/bin/activate
pip install git+https://github.com/possible-worlds-research/wikinlp.git
```

## Train a PeARS model for your own language

Training a model for your language simply consists in running the *modelbuilder.py* script. For instance, if you want to train a model for Faroese (language code 'fo'), you would run the following command:


```
python3 modelbuilder.py fo
```

At the end of the process, you should have three files available in your local folders:

* a .vocab file in the spm/\<language-code\> folder;
* a .model file in the spm/\<language-code\> folder;
* a .ds file in the ds/\<language-code\> folder.

All you have to do is copy them to your PeARS install, inside a newly created api/models/<language-code> folder (see the *api/models/en* for an example).
