# Explaining Model upload field

```python
# I wrote a function before that I can use to generate favicon and zipfile
# Let's create an icon and use it in result. That icon will represent the uploaded file. We will get that one from post request
# The code below make assumption that I am in views, note it won't work directly cos I am note writing in functions. Just assume that request is availabe to us now. It is usually the first argument of functional view
from conficon_app import Icon, Result, Profile

# on get getting the uploaded image from post request,
# we will generate various size icons specific to user

# We will create Icons from the uploaded image and favicons
favicons = []
for icon_name in list_of_icons_generated_their_string:
  with open(icon_name, 'r') as icon:
    icon = Icon.objects.create(
      name='uploaded.png',
      image=image_from_post_data,
      user=request.user
      )
    favicons.append(icon)


# lets say we have zipped files in favicons to file named favicons.zip, we can then assign it to zip_file field and the first(favicon[0]) of the list which is the originally uploaded image will be saved in upload field
# now how the upload works
zipped_file=open('favicon.zip', 'r')  
zipped_file.close()
result = Result.object.create(
    name='favicon.zip',
    upload=favicons[0],
    zip_file=zipped_file
    )
```
