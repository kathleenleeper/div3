
# coding: utf-8

# In[135]:

from __future__ import division
from genderComputer import GenderComputer #import gendercomputer - more fully featured
import pprint as pp
import os
import bibtexparser as b #module for bibtexin'
from bibtexparser.bparser import BibTexParser #import to add customization
from bibtexparser.customization import *


# In[136]:

gc = GenderComputer(os.path.abspath('./nameLists')) #make gendercomputer


# In[137]:

bib = 'CriticalOpenNeuro.bib' #bring that bib file in


# In[138]:

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


# In[139]:

with open(bib) as bibtex_file: 
    parser = BibTexParser()
    parser.homogenize = True
    parser.customization = customizations
    data = b.load(bibtex_file, parser = parser)


# In[144]:

"""
initialize variables 
"""
women = 0
men = 0
uni = 0
notav = 0
auCount = 0


# In[145]:

for entry in data.entries:
    title = entry["title"]
    if "author" in entry:
        authors = entry["author"] 
    else:
        print "no author in", title
    for j in authors:
        auCount = auCount + 1
        gender = gc.resolveGender(j, None) #resolve gender, yay
        if gender == 'male':
            men += 1
        elif gender == 'female':
            women += 1
        elif gender == 'unisex':
            uni += 1
        else:
            notav += 1


# In[146]:

print "authors ungendered:", notav
percentMen = men/auCount*100
percentWomen = women/auCount*100
percentUni = uni/auCount*100
percentNotAv = notav/auCount*100
print 'author count total:', auCount
print 'women:', women,",", "%.2f" % percentWomen, '%'
print 'men:', men,",", "%.2f" %  percentMen, '%'
print 'unisex:', uni,",", "%.2f" %  percentUni, '%'
print 'unassigned:', notav,",", "%.2f" %  percentNotAv, '%'


# In[ ]:



