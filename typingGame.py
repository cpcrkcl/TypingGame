import time 
import pandas as pd
import numpy as np
from word2number import w2n


words = pd.read_csv('4000-most-common-english-words-csv.csv')

amount_of_time = input("How many seconds would you like the test to be? ")
amount_of_time =  w2n.word_to_num(amount_of_time)
