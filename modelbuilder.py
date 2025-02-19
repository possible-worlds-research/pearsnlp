import sys
from os import rename
from wikinlp.downloader import Downloader
from wikinlp.trainspm import SPMTrainer
from wikinlp.trainds import DSTrainer
from datetime import date

vocab_size = 16000
num_dumps = 2
today = str(date.today())

def train_spm(lang):
    downloader = Downloader(lang)
    downloader.mk_wiki_data(n_dump_files=num_dumps, tokenize=False, lower=True, doctags=True)

    print("Running TrainSPM")
    trainspm = SPMTrainer(lang, vocab_size)
    trainspm.train_sentencepiece()
    trainspm.model_path = f'spm/{lang}/{lang}wiki.16k.{today}.model'
    trainspm.apply_sentencepiece()

def train_ds(lang):
    print("Running FastText")
    trainds = DSTrainer(lang)
    trainds.spm_model_path = f'spm/{lang}/{lang}wiki.16k.{today}.model'
    trainds.train_fasttext(corpus_size=100000000)

def output_nns(lang):
    trainds = DSTrainer(lang)
    trainds.model_path = f'ds/{lang}/{lang}wiki.16k.{today}.cs100m.ft'
    nns_path = f'ds/{lang}/{lang}wiki.16k.cos'
    nns = trainds.compute_nns(top_words=16000)

    with open(nns_path, 'w', encoding='utf-8') as fout:
        for word,ns in nns.items():
            fout.write(f"{word} : {' '.join(ns)}\n")

if __name__ == "__main__":
    lang = sys.argv[1]
    #train_spm(lang)
    #train_ds(lang)
    output_nns(lang)
    rename(f'spm/{lang}/{lang}wiki.16k.{today}.model',f'spm/{lang}/{lang}wiki.16k.model')
    rename(f'spm/{lang}/{lang}wiki.16k.{today}.vocab',f'spm/{lang}/{lang}wiki.16k.vocab')
