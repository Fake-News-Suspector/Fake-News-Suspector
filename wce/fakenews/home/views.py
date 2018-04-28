from django.shortcuts import render

from .api import search
from .classifier	import vector 
from .ApiTweet import  twitter  
from .categorizer import cate
def index(request):
	return render(request,'home/index.html')

def Search(request):
	sname = request.GET.get('sname')
	final=twitter.tweet(sname)
	# final2=vector.vector_search(sname)
	final3=[]
	final3.append(final)
	#final3.append(final2)
	return render(request,'home/result.html',{'final3':final3})
def Search2(request):
	sname = request.GET.get('sname')

	final=cate.scat(sname)
	final3=[]

	final3.append(final)
	return render(request,'home/result2.html',{'final3':final3})