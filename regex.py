import re

def check_email(text):
  pattern = r"^[a-zA-Z0-9_\.\-\+]*\.[a-zA-Z]*$"
  result = re.search(pattern, text)
  return result != None

print(check_email("gmail.com")) # True
print(check_email("www@google")) # False
print(check_email("www.Globo.com")) # True
print(check_email("web-address.com/homepage")) # False
print(check_email("My_Favorite-Blog.US")) # True