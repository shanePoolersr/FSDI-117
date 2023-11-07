from django.shortcuts import render

# Create your views here.

def project_new(request):
    return render(request,'projects/projects_list.html')


#HOMEWORK!
#Display the form in the html
