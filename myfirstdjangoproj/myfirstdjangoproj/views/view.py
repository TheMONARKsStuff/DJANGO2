from django.http import HttpResponse
from django.shortcuts import render
def myhome(request):
	return HttpResponse("<h1>Welcome home monark</h1>")
	
def mycontact(request):
		return HttpResponse("<h1>contact 8460752391</h1>")
def mymain(request):
		return render(request,'main.html',{'name':'Hello Monark Zaveri'})	
		
def getcount(request):
		dataFromReq = request.GET['txarea']
		spltdData= dataFromReq.split()
		lengthOfData = len(dataFromReq.split())
		
		wordDictionary= {}
		for word in spltdData:
			if word not in wordDictionary:
				wordDictionary[word] = 1
			else:
				wordDictionary[word]+=1
				
			
		sortedList = sorted(wordDictionary.items(),reverse = True)
		
		return render(request,'count.html',{'lastArea':dataFromReq,'lengthh':lengthOfData,'wordD':sortedList})	