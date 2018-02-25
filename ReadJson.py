# coding=utf-8
import json
import logging

class ReadJson:
	def __init__(self):
		pass

	def readFile(self):
		logging.basicConfig(level=logging.INFO)
		try:
			self.readJson()
			logging.info("load success!!")
		except Exception as e:
			logging.info(repr(e))
			logging.info("Please Check the dir of data")

	def readJson(self,n=0):
		ngram_list=[]
		qa_dict={}
		list_of_ngram_list = []
		with open('your_file_name','r', encoding='utf8') as json_data:
			jdata = json.loads(json_data.read())
		for i in range(len(jdata)):
			qdata = (jdata[i]['question'])
			adata = (jdata[i]['answer'])
			qa_temp=[]
			qa_temp.append(qdata)
			qa_temp.append(adata)
			qa_dict[i+1]=qa_temp
			temp_list=[]
			for j in range(len(qdata)-1):
				ngram_list.append(qdata[j:j+n])
				temp_list.append(qdata[j:j+n])
			list_of_ngram_list.append(temp_list)
		#print(ngram_list)		
		#print(qa_dict.items())	
		#print(list_of_ngram_list)	
		return (ngram_list,list_of_ngram_list,qa_dict)