# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request, 'index/index.html')

def index1(request):
	return render(request, 'index/index1.html')

def technology(request):
	return render(request, 'index/technology.html')

def faq(request):
	return render(request, 'index/pricing.html')

def contactus(request):
	return render(request, 'index/contact.html')

def landlord(request):
	return render(request, 'index/landlords.html')

def wells(request):
	return render(request, 'index/wells.html')

def household(request):
	return render(request, 'index/household.html')	