from django.shortcuts import render, redirect
from .models import User, Friend
from django.contrib import messages
from django.contrib.auth import logout

def index(request):
	return render (request, "new_app/index.html")

def register(request):
	if request.method == 'POST':
		user_tuple2 = User.userManager.register(request.POST['name'], request.POST['alias'], request.POST['email'], request.POST['pw'], request.POST['c_pw'], request.POST['dob'])
		if user_tuple2[0]:
			request.session['id'] = user_tuple2[1].id
			request.session['name'] = user_tuple2[1].name

			return redirect('/success')
		else:
			for i in user_tuple2[1]:
				messages.info( request, user_tuple2[1][i], extra_tags = 'rg')
		 	return redirect('/')
		
	
def success(request):
	user1 = User.objects.get(id = request.session['id'])
	not_friend = User.objects.exclude(f2__user1 = user1)
	context = {
		"all_friends": Friend.objects.filter(user1=request.session['id']),
		"not_friends": not_friend,
		"current_user": user1,
	}
	print not_friend
	return render (request, "new_app/friends.html", context)

def login(request):
	if request.method == 'POST':
		user_tuple = User.userManager.login(request.POST['elogin'] , request.POST['Lpw'])
		if user_tuple[0]:
			request.session['id'] = user_tuple[1].id
			request.session['name'] = user_tuple[1].name
			return redirect('/success')
		else:	
			for i in user_tuple[1]:
				messages.info( request, user_tuple[1][i], extra_tags = 'lg')
			return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/')

def add_friend(request, id):
	user1_id = request.session['id'] #logged in user
	user2_id = id #user being friended
	user_tuple = Friend.userManager.add(user1_id, user2_id)
	return redirect('/success')


def show(request, id):
	context = {
		"users": User.objects.get(id=id)
	}
	return render(request, "new_app/profile.html", context)

def remove(request,id):
	instance1 = Friend.objects.get(user1=request.session['id'], user2=id)
	instance1.delete()
	instance2 = Friend.objects.get(user1=id, user2=request.session['id'])
	instance2.delete()
	return redirect('/success')

