from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import todolist,item
from .forms import createnewlist

# Create your views here.
# def index(response):
# 	return HttpResponse("<h1>Doug De Muro</h1>")

# def index(response, id):
# 	ls  = todolist.objects.get(id = id)
# 	itm = ls.item_set.get(id = 1)
# 	return HttpResponse('<h1>%s</h1></br><p>%s</p>' % (ls.name,itm.text))

# def index(response,id):
# 	cnt = todolist.objects.get(id = id)
# 	return render(response,'main/list.html',{'cnt':cnt})

def index(response,id):
	cnt = todolist.objects.get(id = id)

	if cnt in response.user.todolist.all():
		if response.method == 'POST':
			print(response.POST)
			if response.POST.get('save'):
				for item in cnt.item_set.all():
					if response.POST.get("c" + str(item.id)) == 'clicked':
						item.complete = True
					else:
						item.complete = False
					item.save()

			elif response.POST.get('newItem'):
				txt = response.POST.get("new")
				if  len(txt) > 2:
					cnt.item_set.create(text=txt,complete=False)
				else:
					print('INVALID')

		return render(response,'main/list.html',{'cnt':cnt})
	return render(response,'main/home.html',{})

def home(response):
	return render(response,'main/home.html',{})

# this gets the form at the forms.py and render it in create.html
def create(response):
	# we set it to post so its always
	if response.method == 'POST':
		form = createnewlist(response.POST)
		# asks if the data you enter fills the need info
		if form.is_valid():
			# get the raw data name
			n = form.cleaned_data['name']
			# adds it to as our new todolist
			t = todolist(name=n)
			t.save()
			response.user.todolist.add(t)	#to get and save the users data
		# redirect us to the object we created
		return HttpResponseRedirect('/%i' % t.id)

	else:
		form = createnewlist()
	return render(response,'main/create.html',{'form':form})

def lists(response):
	return render(response,'main/lists.html',{})