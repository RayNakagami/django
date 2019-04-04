from django.template.response import TemplateResponse
from django.utils import timezone
def index(request):
    """メイン画面."""
    time = timezone.localtime(timezone.now())
    if(6<=time.hour<12):
        greeting = greetings['morning']
    elif(12<=time.hour<18):
        greeting = greetings['afternoon']
    else:
        greeting = greetings['night']
        title = name + 'の野菜販売'
        return TemplateResponse(request,'garden/index.html',{'title':title,'greeting':greeting})

