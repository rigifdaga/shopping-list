from django.shortcuts import render
def show_main(request):
    context = {
        'name': 'Rifda Aulia N',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
