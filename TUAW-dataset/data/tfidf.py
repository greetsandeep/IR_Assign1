"""
	ASSIGNMENT #1
	Project : To build an IR model based on a vector space model 
  
	Instructor : Dr. Aruna Malapati
  
	Contributors : G V Sandeep 2014A7PS106H
                 Kushagra Agrawal 2014AAPS334H
                 Snehal Wadhwani 2014A7PS430H

	Course No : CS F469 Information Retrieval

	Working of tfidf.py:
    	1. Calculates the idf score for every word in the dictionaries for title, blogger and post.
    	2. Calculates the tf score for all the words in every document separately for title, blogger and post.
    	3. Normalises the document vector (which is the tf score) by converting it to a unit vector. 

"""
from new_inverted import *
from main import *
from math import log, pow, sqrt


#dictionaries to hold idf values for words in title, blogger and post 
idf_title = {}
idf_blogger = {}
idf_post = {}

#dictionaries to hold tf values for words in title, blogger and post for each document
tf_title = {}
tf_blogger = {}
tf_post = {}

def normalize_query(wt):
	''' 
		converts the query vector(wt) into a unit vector
	'''
	l = 0.0
	for word in wt.keys():
		l = l + pow(wt[word],2)
	l = sqrt(l)
	for word in wt.keys():
		if l != 0:
			wt[word] = wt[word]/l
		else:
			wt[word] = 0.0

def calc_tf_idf(tf,idf,org,N): 	
	'''
		calculates the tf and idf for all the words in the dictionary 'org', size of the corpus being 'N'
	'''	
	for key,val in org.iteritems():
		raw_tf = {}
		#idf value for token 'key'
		idf[key] = (log((float(N)/len(val.keys())),10))		
		for doc_key,doc_val in val.iteritems():
			if len(doc_val)>0:
				#tf value for token 'key' and document 'doc_key'
				raw_tf[doc_key] = 1 + log(len(doc_val),10)		
			else:
				raw_tf[doc_key] = 0
		tf[key] = raw_tf

#calculates tf-idf for title
calc_tf_idf(tf_title,idf_title, dictTitle, len(megaList))	
#calculates tf-idf for blogger
calc_tf_idf(tf_blogger,idf_blogger, dictBlogger, len(megaList))	
#calculates tf-idf for post
calc_tf_idf(tf_post, idf_post, dictPost, len(megaList))	

def normalize_doc(k):	
	'''
		converts all the document vectors (tf values) to unit vectors
	'''
	for i in xrange(len(megaList)):
		temp = []
		l = 0.0
		for word in megaList[i][k]:
			if word not in temp:
				temp.append(word)
		for word in temp:
			if k == 0:
				l = l + pow(tf_title[word][i],2)
			elif k == 2:
				l = l + pow(tf_blogger[word][i],2)
			elif k == 4:
				l = l + pow(tf_post[word][i],2)
		l = sqrt(l)
		for word in temp:
			if k == 0:
				tf_title[word][i] = tf_title[word][i]/l
			elif k == 2:
				tf_blogger[word][i] = tf_blogger[word][i]/l
			elif k == 4:
				tf_post[word][i] = tf_post[word][i]/l

#normalizes title for all documents
normalize_doc(0)
#normalizes blogger for all documents
normalize_doc(2)
#normalized post for all documents 
normalize_doc(4)




		