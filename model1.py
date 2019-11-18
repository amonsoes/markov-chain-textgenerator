import numpy as np
import sklearn as sk

from sklearn.feature_extraction.text import CountVectorizer as cv

from Dataset import Dataset, Datafile



class MarkovChain:
    
    def __init__(self,matrix):
        self.matrix = matrix

    @classmethod
    def make_Chain(cls,dataset):
        pass
    
    def highest_ngram_likelihood(self):
        pass
    
    def predict(self):
        pass
    
    
    