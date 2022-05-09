import string 
from django.utils.text import slugify 
import random 
  
def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size)) 
  
def unique_slug_generator(instance, instance_string, new_slug = None): 
    if new_slug is not None: 
        slug = new_slug 
    else:
        if len(instance_string) > 20:
            slug = slugify(instance_string[:20])
        else:
            slug = slugify(instance_string) 
    Klass = instance.__class__ 
    qs_exists = Klass.objects.filter(slug = slug).exists() 
    if qs_exists: 
        new_slug = "{slug}-{randstr}".format( 
            slug = slug, randstr = random_string_generator(size = 4)) 
              
        return unique_slug_generator(instance, instance_string, new_slug = new_slug) 
    return slug 