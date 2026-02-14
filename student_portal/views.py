from django.shortcuts import render, redirect

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
