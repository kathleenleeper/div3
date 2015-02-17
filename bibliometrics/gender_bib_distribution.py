from __future__ import division
from genderComputer import GenderComputer #import gendercomputer - more fully featured
import pprint as pp
import os
import bibtexparser as b #module for bibtexin'
from bibtexparser.bparser import BibTexParser #import to add customization
from bibtexparser.customization import *

""""""""""""""""""""""
initializing variables 
"""""""""""""""""""""
gc = GenderComputer(os.path.abspath('./nameLists')) #make gendercomputer
women = 0
men = 0
uni = 0
notav = 0
auCount = 0
bib = 'CriticalOpenNeuro.bib' #bring that bib file in

def customizations(record):
    """Use some functions delivered by the library
    
    :param record: a record
    :returns: -- customized record
    """
    record = type(record)
    record = doi(record)
    record = convert_to_unicode(record) #clean up for parsing
    record = author(record) #parse authors into array
    return record

def loadBibFile():
    with open(bib) as bibtex_file:
        parser = BibTexParser()
        parser.homogenize = True
        parser.customization = customizations
        data = b.load(bibtex_file, parser = parser)


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
            #print j, title
            notav += 1 

#'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
#calculate percents #hacks
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

