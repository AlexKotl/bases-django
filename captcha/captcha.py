import requests

def validate(request, secret_key):
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
        'secret': secret_key,
        'response': request.POST.get('g-recaptcha-response')
    })
    result = r.json()
    return result['success']
