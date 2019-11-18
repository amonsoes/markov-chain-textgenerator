import numpy as np
import sklearn as sk
import nltk
import json
import os

from sklearn.feature_extraction.text import CountVectorizer as cv
from scipy.sparse import csr_matrix as csr

NGRAM_RANGE = (1,3)


class Dataset:
    
    def __init__(self, freq_mat, vocab, doc_dict):
        self.freq_mat = freq_mat
        self.vocab = vocab
        self.doc_dict = doc_dict
        
    @classmethod
    def load_dataset(cls, path):
        ls = []
        for _, _, filenames in os.walk(path):
            for file in filenames:
                if file.endswith(".json"):
                    ls.append(Datafile.from_json(path))
        return cls.make_dataset(ls)

    @classmethod
    def make_dataset(cls, lst):
        textfiles = [datafile.json.text for datafile in lst]
        cv = cv.fit(textfiles,ngram_range=NGRAM_RANGE)
        freq_mat = cv.transform(textfiles)
        doc_dict = {datafile.id:datafile for datafile in lst}
        vocab =  cv.get_feature_names()
        return cls(freq_mat,vocab,doc_dict)
        
            

class Datafile:
    
    cls_id = 0
    
    def __init__(self, id, text=None, json=None):
        self.text = text
        self.json = json
        self.id = id
    
    @classmethod
    def from_textfile(cls, path):
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        id = cls_id
        cls_id += 1
        return cls(id,text)
    
    @classmethod
    def from_json(cls,path):
        with open(path, "r", encoding="utf-8") as f:
            json = json.load(f)
        id = cls_id
        cls_id += 1
        return cls(id,json)