#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from books.models import Book


# Create your views here.

def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    #error = False
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
	    errors.append('输入待搜索的内容.')
 	elif len(q)>20:
	    errors.append('请输入小于20个字符的内容.')
  	else:
	    books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',{'books': books, 'query': q})
    return render_to_response('search_form.html',{'errors': errors})
