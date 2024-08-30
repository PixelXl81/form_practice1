from django.shortcuts import render
from .forms import Inputforms


def home_view(request):
    # بررسی اینکه آیا فرم ارسال شده است یا خیر
    if request.method == 'POST':
        form = Inputforms(request.POST)
        if form.is_valid():
            # پردازش داده‌های فرم اینجا
            print(form.cleaned_data)
    else:
        form = Inputforms()

    # ارسال فرم به قالب
    return render(request, 'home.html', {'form': form})
