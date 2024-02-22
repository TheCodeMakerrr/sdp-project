from django.shortcuts import render
from .models import URL
import random
import string
# Create your views here.
def url_shortener(request):
    if request.method ==  'post':
        long_url = request.POST['long_url']
        short_url = generate_short_url()
        URL.objects.create(long_url=long_url, short_url=short_url)
        return render(request, 'url_shortener.html',{'short_url': short_url})
    return render(request, 'url_shortener.html')
def redirect_to_original(request, short_url):
    url = URLS.objects.get(short_url=short_url)
    return render(url.long_url)

def generate_short_url():
    character = string.ascii_letters + string.digits
    return ''.join(random.choice(character) for i in range(6))