# import en_core_web_lg # Large SpaCy model for English language
import numpy as np
import re # regular expressions
import spacy # NLU library

from collections import defaultdict
from sklearn.svm import SVC # Support Vector Classification model

output_format = "IN: {input}\nOUT: {output}\n" + "_"*50
# hard-coded exact questions
responses_exact = {
    "How was your day today? Any up and low moments?": "I just found out that I lost my job",
    "How are you feeling right now?": "Am pretty sad to be honest",
    "default": "It only gets better with time"
}

def respond_exact(text):
    response = responses_exact.get(text, responses_exact['default'])
    return(output_format.format(input=text, output=response))
    

print(respond_exact("How was your day today? Any up and low moments?"))
print("_"*50)
print(respond_exact("What time will you be home tonight?"))
print("_"*50)
print(respond_exact("I just found out my boss is leaving the company."))