from urllib.request import urlopen
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from dynamic.models import Subdomain

a = ["RicoDarrow ",
     "Tracy Michelle Story"]

phns = [
    '16303412098',
    '17064576681',
]

b = [i.split(' ')[0] for i in a]

for i in range(len(b)):
    name = b[i] + " businessbuilders"
    subn = name.replace(" ", '')
    sub = Subdomain(sub_name=subn.lower(), title=name, favicon_title=name, seo_description=name, phno=phns[i])
    gile = 'https://getdinerotodaybucket2.s3.amazonaws.com/documents/22dc7618-4078-4e9d-8f7a-e6c854c0a42d/bcb-removebg-preview.png'
    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(urlopen(gile).read())
    img_temp.flush()
    sub.logo.save(f"image_{i}.png", File(img_temp))
    sub.save()


from django.core.mail import send_mail

send_mail(
    'Subject here',
    'Here is the message.',
    'millennialbusinessbuilders@gmail.com',
    ['vassili.kiritsenko@gmail.com'],
    fail_silently=False,
)