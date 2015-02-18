
# coding: utf-8

# In[1]:

from __future__ import division

"""gendering"""
from genderComputer import GenderComputer 

"""bibtex parsing"""
import os
import bibtexparser as b #module for bibtexin'
from bibtexparser.bparser import BibTexParser #import to add customization
from bibtexparser.customization import *

"""plotting functions"""
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


# In[2]:

bib = 'CriticalOpenNeuro.bib' #bring that bib file in
gc = GenderComputer(os.path.abspath('./nameLists')) #make gendercomputer


# In[3]:

def customizations(record):
    """Use some functions delivered by the library

    :param record: a record
    :returns: -- customized record
    """
    record = type(record)
    record = doi(record)
    record = convert_to_unicode(record)
    record = author(record)
    return record


# In[4]:

def parseFile(bib_file):
    """parse the bib file
    
    :param bib_file: bibtex file to be parsed
    :returns: -- a bibtex file object
    """
    with open(bib_file) as bibtex_file: 
        parser = BibTexParser()
        parser.homogenize = True        
        parser.customization = customizations
        data = b.load(bibtex_file, parser = parser)
        return data


# In[5]:

def countGender(ts=True):
    """take the bib database and count genders of authors
    """ 
    global auCount
    global notav
    global uni
    global men
    global women
    for entry in data.entries:
        title = entry["title"]
        if "author" in entry:
            authors = entry["author"] 
        elif ts==True:
            print "no author in", title
        for j in authors:
            auCount += 1
            gender = gc.resolveGender(j, None) #resolve gender, yay
            if gender == 'male':
                men += 1
            elif gender == 'female':
                women += 1
            elif gender == 'unisex':
                uni += 1
            else:
                notav += 1 
                if ts == True:
                    print j, title
            


# In[6]:

women = 0
men = 0
uni = 0
notav = 0
auCount = 0


# In[7]:

data = parseFile(bib) #run the parse file
countGender(ts=False)
print auCount


# In[8]:

stats = {'Women':women, 'Men':men, 'Unisex':uni, 'Not Available':notav}
percents = {'Women':women, 'Men':men, 'Unisex':uni, 'Not Available':notav}


# In[10]:

for key in stats:
    value = stats[key]
    percent = value/auCount*100 #probably should fix so it can't break if dividing by zero
    percents[key] = percent


# In[11]:

plt.bar(range(len(stats)), percents.values(), align='center', alpha=0.1)
plt.xticks(range(len(percents)), percents.keys())
plt.xlabel('Gender Assigned')
plt.ylabel('Percents')


# In[12]:

plt.savefig('gender_distr.png', bbox_inches='tight')

