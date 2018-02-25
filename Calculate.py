# coding=utf-8
import json
import logging
import numpy as np
from numpy import dot
from numpy.linalg import norm
#from scipy import spatial
from ReadJson import ReadJson
from collections import Counter
from math import log
class Calculate:
	def __init__(self):
		read = ReadJson()
		self.ngram = 1
		self.ngram_list,self.list_of_ngram_list,self.qa_dict = read.readJson(self.ngram)	
		self.ngramSet = set(self.ngram_list)		

	def getVector(self):
		temp_list=[]
		vector_list=[]
		for q in self.list_of_ngram_list:
			temp_list=[]
			for term in self.ngramSet:
				if term in q:
					temp_list.append((q.count(term)/float(len(q)))*self.termIdf(term))
				else:
					temp_list.append(0)
			vector_list.append(temp_list)
		return(vector_list)

	def analyzeUserSentence(self, sentence):
		user_ngram_list=[]
		for i in range(len(sentence)-1):
			user_ngram_list.append(sentence[i:i+self.ngram])
		return(user_ngram_list)		

	def rankScore(self, vector_list, user_q):
		user_vector_list=[]
		result_list=[]
		max_score = 0
		qid = 0
		match_id = 0
		for term in self.ngramSet:
			if term in user_q:
				user_vector_list.append((user_q.count(term)/float(len(user_q)))*self.termIdf(term))
			else:
				user_vector_list.append(0)
		for vector_data in vector_list:
			qid = qid + 1
			#score = 1 - spatial.distance.cosine(vector_data, user_vector_list)
			np.seterr(divide='ignore', invalid='ignore')
			score = dot(vector_data, user_vector_list)/(norm(vector_data)*norm(user_vector_list))
			if (score > max_score):
				max_score = score
				match_id = qid
		if(match_id == 0):
			print("Please describe your question more clear!")
		else:
			self.getRespond(match_id)

	def getRespond(self, match_id):
		qa = self.qa_dict[match_id]
		print("Your Question Is:" + qa[0] + "\nYour Answer Is:" + qa[1])

	def termIdf(self, term):
		countTerm = 0
		for doc in self.list_of_ngram_list:
			if term in doc:
				countTerm = countTerm + 1
		if countTerm > 0:
			return 1.0 + log(float(len(self.list_of_ngram_list)) / countTerm)
		else:
			return 1.0