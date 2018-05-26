# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from forms import MessageForm
def message_to_user(request):
	if request.method == "POST":
		form = MessageForm(request, data=request.POST)
		if form.is_valid():
		# do something with the form
			return redirect("message_to_user_done")
	else:
		form = MessageForm(request)
    	
    	return render(request,"message_to_user.html",{'form':form})
