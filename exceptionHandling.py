from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
	html = urlopen('https://www.youtube.com/')
except HTTPError as e:
	print(e)
except URLError as e:
	print("The server could not be found.")
except AttributeError as e:
	print("Tag not found.")
else:
	print("It worked!")
