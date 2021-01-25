import sys
import webbrowser
import urllib.parse

def pyverflow():
  err = sys.last_value
  url = f"https://stackoverflow.com/search?q={err}"
  webbrowser.open_new_tab(urllib.parse.quote(url))
