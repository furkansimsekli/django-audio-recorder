import base64
import uuid
import json
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def save_audio(request):
    data_str = request.body.decode('ascii')
    data = json.loads(data_str)
    audio = data['audio']
    title = f'record_{str(uuid.uuid4())[:8]}'
    wav_file = open(f'records/{title}.mp3', 'wb')
    decode_string = base64.b64decode(audio)
    wav_file.write(decode_string)
    return HttpResponse('Saved')
