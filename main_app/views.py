from django.shortcuts import render
from django.http import HttpResponse
from .models import Treasure

# Create your views here.

# def index(request):
# 	return HttpResponse("<h1>Hello!</h1>")

# def index(request):
# 	return render(request,'index.html')

# def index(request):
# 	name= "Gold Nugget"
# 	value= 1000.0
# 	context ={	'treasure_name' : name,
# 				'treasure_val' : value}
# 	return render(request,'index.html',context)

# def index(request):
# 	return render(request,'index.html',{'treasures':treasures})


# class Treasure:
# 	def __init__(self,name,value,material,location):
# 		self.name=name
# 		self.value=value
# 		self.material=material
# 		self.location=location


# treasures=[
# 	Treasure("Gold Nugget",500.00,"gold","ABC"),
# 	Treasure ("Fools Gold",0.00,"gold","ACd"),
# 	Treasure ("Coffee can",20.00,"gold","AeC")
# ]

def index(request):
	treasures=Treasure.objects.all()
	return render(request,'index.html',{'treasures':treasures})


