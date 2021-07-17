import csv
import psutil


class translator:

	def __init__(self,MainFile,WordFile,DictFile,toWriteFile):
		print("Execution Started........")
		self.MainFile = MainFile
		self.WordFile = WordFile
		self.DictFile = DictFile
		self.toWriteFile = toWriteFile
		self.Frequency_Maintainer = {}

	
	def Trans(self):
		punctuations = '''!()-[]{};:'",<>\n./?@#$%^&*_~s'''
		wordstofind = self.WordsToFind

		print("Replacing English Words with French Words....")

		with open(self.MainFile) as F:
			punc_mark = ''
			contents = F.readlines();
			
			for line in contents: 
				for word in line.split(" "):
					for each in word:
						
						if each in punctuations:
							punc_mark = each;
					
					new_word = word.replace(punc_mark,"")
					new_word = new_word.lower()	
					
					if new_word in wordstofind:
						translated_word = self.Frequency_Replacer(new_word)
						self.Frequency_Counter(new_word)
						toWriteFile.write(translated_word + " ")
					else:
						toWriteFile.write(word + " ")

	def WordReader(self):
		
		WordsToFind = [];
		with open(self.WordFile) as W:
			Words = W.read();
			for each in Words.split("\n"):
				WordsToFind.append(each)

			self.WordsToFind = WordsToFind		

	def DictFetcher(self):
		
		french_dictionary = {}
		
		with open(self.DictFile) as df:
			
			csv_reader = csv.reader(df,delimiter=',')

			for row in csv_reader:   
				french_dictionary[row[0]] = row[1]

		self.fr_dt = french_dictionary


	def Frequency_Replacer(self,word):
	
		fr_dt = self.fr_dt
		
		return fr_dt[word]

	def Frequency_Counter(self,word):

		Frequency_Maintainer = self.Frequency_Maintainer

		if word not in Frequency_Maintainer:
			Frequency_Maintainer[word] = 0
		else:
			Frequency_Maintainer[word] = Frequency_Maintainer.get(word) + 1

	def Frequency_Adder(self):

		header = ['English Words','French Words', 'Frequency']
		data = []

		with open('frequency.csv','w', encoding='UTF8', newline='') as f:

			writer = csv.writer(f)

			writer.writerow(header)

			Frequency_Maintainer = self.Frequency_Maintainer
			fr_dt = self.fr_dt

			for key_word in Frequency_Maintainer:
				if key_word in fr_dt:
					data.append(key_word)
					data.append(fr_dt[key_word])
					data.append(Frequency_Maintainer[key_word])
				
				writer.writerow(data)
				data.clear()

		print("Conversion Successfull")


toWriteFile = open("t8.shakespeare.translated.txt","w+")
DictFile = "french_dictionary.csv"
File = "t8.shakespeare.txt"
WordFile = "find_words.txt"
T1 = translator(File,WordFile,DictFile,toWriteFile)
T1.WordReader()
T1.DictFetcher()
T1.Trans()
T1.Frequency_Adder()


