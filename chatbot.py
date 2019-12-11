# import en_core_web_lg # Large SpaCy model for English language
import numpy as np
import re # regular expressions
import spacy # NLU library

from collections import defaultdict
from sklearn.svm import SVC # Support Vector Classification model

output_format = "IN: {input}\nOUT: {output}\n" + "_"*50
# hard-coded exact questions
responses_exact = {
    "what would you like to eat tonight?": "Pasta with salmon and red pesto please!",
    "what time will you be home tonight?": "I will be home around 6 pm.",
    "default": "I love you too!"
}

def respond_exact(text):
    response = responses_exact.get(text.lower(), responses_exact['default'])
    return(output_format.format(input=text, output=response))
    

print(respond_exact("What would you like to eat tonight?"))
print("_"*50)
print(respond_exact("What time will you be home tonight?"))
print("_"*50)
print(respond_exact("I just found out my boss is leaving the company."))