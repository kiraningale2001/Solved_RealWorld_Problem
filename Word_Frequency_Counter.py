import os

class Word_frequency_counter:
    Words={}
    Characters={}
    def __init__(self,file_name):
        with open(file_name,'r') as file:
            file_content=file.read()
            self.Words=self._Freq_counter_words(file_content)
            self.Characters=self._Freq_counter_character(file_content)
   
    def _Freq_counter_words(self,file_content):
        words={}
        for word in file_content.split(' '):
            if word in words:
                words[word]+=1
            else:
                words[word]=1
        return words
    
    
    def _Freq_counter_character(self,file_content):
        character={}
        for char in file_content:
            if char in character:
                character[char]+=1
            else:
                character[char]=1
        return character
            
