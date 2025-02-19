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

Then, clone PeARSNLP, make your virtual environment and install the necessary dependency (the Wikipedia-processing package [WikiNLP](https://github.com/possible-worlds-research/wikinlp)):

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
* a .cos file in the ds/\<language-code\> folder.


## Telling your PeARS install about the new language

PeARS needs to know that a new language has been added to your instance. To do this, you should:

* copy the three files referenced above (*.vocab*, *.model* and *.cos*) to your PeARS install, inside a newly created *app/api/models/<language-code>* folder (see the *api/models/en* for an example);
* modify your .env file in the root directory of your PeARS install and add the language code to the PEARS_LANGS variable (see [the docs](https://pears.readthedocs.io/en/latest/dotenv.html#language-settings) for more information on the .env file).

