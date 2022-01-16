#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
def convert():
	celsius = eval(input("Enter celsius: "))
	fahrenheight = 9/5 * celsius + 32
	print("the fahrenheight temp is", fahrenheight)

convert()
"""
"""
def main():
	print("This program illustrates a chaotic function")
	x = float(input("Enter a number between 0 and 1: "))
	for i in range(10):
		x= 3.9 * x * (1 - x)
		print(x)

main()
"""

# Dentist time making a new module while getting 
# fucked in the pockets


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import gc
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
from datetime import datetime
import multiprocessing
from functools import partial




SAFE_DIV=0.0001
BUCKET_SIZE = 5000
STOP_WORDS=stopwords.words('english')

def preprocess(x):
    x=str(x).lower()
    x=x.replace(",000,000", "m").replace(",000", "k").replace("′", "'").replace("’", "'")
    .replace("won't", "will not").replace("cannot", "can not").replace("can't", "can not")
    .replace("n't", " not").replace("what's", "what is").replace("it's", "it is")
    .replace("'ve", " have").replace("i'm", "i am").replace("'re", " are")
    .replace("he's", "he is").replace("she's", "she is").replace("'s", " own")
    .replace("%", " percent ").replace("₹", " rupee ").replace("$", " dollar ")
    .replace("€", " euro ").replace("'ll", " will")
    
    x = re.sub(r"([0-9]+)000000", r"lm", x)
    x = re.sub(r"([0-9]+)000", r"lk", x)
    
    
    porter=PorterStemmer()
    pattern=re.compile('\W')
    
    if type(x) == type(''):
        x = re.sub(pattern, ' ', x)
    
    
    if type(x) == type(''):
        x = porter.stem(x)
        example1 = BeautifulSoup(x, 'lxml')
        x = example1.get_text()
               
    return x        

def run_process(df, start):
    df = df[start:start+BUCKET_SIZE]
    print(start, "to ",start+BUCKET_SIZE)
    temp = df["question"].apply(preprocess)

    
if __name__=="__main__":

    df = pd.read_csv("train/train.csv")
    list_of_questions = set(list(df['question1'])+list(df['question2']))
    print(len(list_of_questions))

    df_temp = pd.DataFrame()
    df_temp['question'] = list(list_of_questions)
    df_temp = df_temp.fillna("")


    sample_size = [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    bucket = [1000, 2500, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]
    single_process_time = []
    multi_process_time = []
    
    for x,b in zip(sample_size, bucket):
        df = df_temp.sample(frac=x)
        BUCKET_SIZE = b
        print("Data Shape: ", df.shape)
        print("BUCKET SIZE: ", BUCKET_SIZE)

        print("Single Processing Starting")
        st = datetime.now()
        temp = df["question"].apply(preprocess)
        end = datetime.now()
        print("Single processing Time: ",end-st)
        single_process_time.append(end-st)

        
        print("Multiprocessing Starting")
        
        st = datetime.now()
        chunks  = [x for x in range(0,df.shape[0],BUCKET_SIZE)]        
        pool = multiprocessing.Pool()
        func = partial(run_process, df)
        temp = pool.map(func,chunks)
        pool.close()
        pool.join()
        end = datetime.now()
        print("Multiprocessing Time: ",end-st)
        multi_process_time.append(end-st)
        print()
        print()

    out_time = pd.DataFrame()
    out_time['sample size'] = sample_size
    out_time['bucket size'] = bucket
    out_time['single_process_time'] = single_process_time
    out_time['multi_process_time'] = multi_process_time
    out_time.to_csv("Benchmark.csv", index=False)
                
        