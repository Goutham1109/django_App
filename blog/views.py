from django.shortcuts import render,get_object_or_404
from .models import Blogs

# Create your views here.
def all_blog(request):
    blogs = Blogs.objects.all()
    return render(request,'blogs.html',{'blogs':blogs})


def blogDetail(request,id):
    blogDetail = get_object_or_404(Blogs,pk=id)
    return render(request,'blogDetails.html',{'id':blogDetail})
