import requests


def get_facebook_share_count(self, request):
    url = 'https://graph.facebook.com/?id=' + request.build_absolute_uri()
    r = requests.get(url)
    data = r.json()
    print data['share']['share_count']


def get_linkedin_share_count(self, request):
    url = 'https://www.linkedin.com/countserv/count/share?format=json&url=' + request.build_absolute_uri()
    r = requests.get(url)
    data = r.json()
    print data['count']
