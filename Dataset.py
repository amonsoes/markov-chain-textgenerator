import collections
import numpy as np
import sklearn as sk
import nltk
import json

from sklearn.feature_extraction.text import CountVectorizer as cv
from scipy.sparse import csr_matrix as csr

NGRAM_RANGE = (1,3)


class Dataset:
    
    def __init__(self, freq_mat, vocab, id_mat):
        self.freq_mat = freq_mat
        self.vocab = vocab
        self.id_mat = id_mat
        
    @classmethod
    def make_dataset(cls,textfiles):
        pass


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