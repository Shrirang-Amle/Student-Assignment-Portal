from django.shortcuts import redirect, render
from .models import Assignment
from .forms import AssignmentForm

def set_preferences(request):
    if request.method == "POST":
        theme = request.POST.get("theme")
        subject = request.POST.get("subject")

        response = redirect('show_preferences')
        response.set_cookie('theme', theme, max_age=3600)
        response.set_cookie('subject', subject, max_age=3600)
        return response

    return render(request, 'set_preferences.html')

def show_preferences(request):
    theme = request.COOKIES.get('theme')
    subject = request.COOKIES.get('subject')

    return render(request, 'show_preferences.html', {
        'theme': theme,
        'subject': subject
    })

def submit_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            request.session['username'] = form.cleaned_data['name']
            form.save()
            return redirect('list_assignments')
    else:
        form = AssignmentForm()

    return render(request, 'submit.html', {'form': form})


def list_assignments(request):
    assignments = Assignment.objects.all()
    username = request.session.get('username')

    return render(request, 'list.html', {
        'assignments': assignments,
        'username': username
    })
