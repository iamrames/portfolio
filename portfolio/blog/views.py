from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import MyForm

# Create your views here.

class index(TemplateView):
    template_name = "blog/index.html"

class about(TemplateView):
    template_name = "blog/about.html"

class portfolio(TemplateView):
    template_name = "blog/portfolio.html"

class photos(TemplateView):
	template_name = "blog/photos.html"

class rames(TemplateView):
	template_name = "blog/rames.html"

def form_name_view(request):
    form = MyForm()

    if request.method == "POST":
        form = MyForm(request.POST)

        if form.is_valid:
            form.save(commit=True)
            return render(request,'blog/index.html')

        else:
            print("Error! Form invalid")

    return render(request,'blog/contact.html',{'form':form})
