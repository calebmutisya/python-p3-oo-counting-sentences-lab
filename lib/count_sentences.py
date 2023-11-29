#!/usr/bin/env python3
import re

class MyString:
    def __init__(self,value=None):
        self._value= ""
        self.value=value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if isinstance(value, str) :
            self._value = value
        else:
            print("The value must be a string.\n")

    def is_sentence(self):
        if self._value.endswith('.'):
            return True
        else:
            return False
    
    def is_question(self):
        if self._value.endswith("?"):
            return True
        else:
            return False
        
    def is_exclamation(self):
        if self._value.endswith('!'):
            return True
        else:
            return False

    def count_sentences(self):
          # Replace all punctuation marks with a common separator (here, a single space)
          # Split the text into sentences using this separator
          sentences = re.split(r'[.!?]',self._value)
          #Eliminate empty strings from the list
          non_empty_sentences=[sentence.strip() for sentence in sentences if sentence.strip()]

          return len(non_empty_sentences)
    

string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.is_sentence())       # Output: False
print(string.is_question())       # Output: False
print(string.is_exclamation())    # Output: True
print(string.count_sentences())   # Output: 3