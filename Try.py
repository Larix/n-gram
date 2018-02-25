# coding=utf-8
from Calculate import Calculate

def __init__(self):
	pass

def main():	
	calculate = Calculate()
	vector_list = calculate.getVector()
	while True:
		sentence = input("Please Enter Your Question:")
		user_list = calculate.analyzeUserSentence(sentence)
		calculate.rankScore(vector_list, user_list)

if __name__ == '__main__':
	main()