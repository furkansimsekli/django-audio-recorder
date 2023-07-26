import base64
import json
import uuid

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def save_audio(request):
    data = json.loads(request.body.decode('ascii'))  # Skipping decoding still works, it even creates smaller file
    audio = data['audio']                            # Yet, I don't know why the original author decided to decode.
    audio_type = data['audioType']
    title = f'record_{str(uuid.uuid4())[:8]}'

    with open(f'records/{title}.{audio_type}', 'wb') as f:
        decode_string = base64.b64decode(audio)
        f.write(decode_string)

    return HttpResponse()
