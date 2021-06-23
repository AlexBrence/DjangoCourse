from django.shortcuts import render, HttpResponseRedirect
from .forms import NewUserForm
from django.urls import reverse

# Create your views here.


def index(request):
	return render(request, "appTwo/index.html", {})



def users(request):
	form = NewUserForm()

	if request.method == "POST":
		form = NewUserForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return HttpResponseRedirect(reverse("index"))
		else:
			print("ERROR FORM INVALIDA")
	
	return render(request, "appTwo/users.html", {"form": form})
