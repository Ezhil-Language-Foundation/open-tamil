import html
import requests
from bs4 import BeautifulSoup
from requests.exceptions import (
    HTTPError, Timeout, ConnectionError, RequestException
)

  

class TamilNLPWeb:
        
        baseurl = 'http://sangam.tamilnlp.com/'
        @staticmethod
        def getListOfPoems():
            try:
                List = list()
                result = requests.get(TamilNLPWeb.baseurl+"glossing.php")   
                response = BeautifulSoup(result.content,'html.parser')  
                for poem in response.body.find_all("ul"):
                    List.append(poem.get_text())
                return List
            except Timeout:
                print("⛔ Request timed out")

            except ConnectionError:
                print("⛔ Network problem (DNS failure, refused connection, etc.)")

            except HTTPError as e:
                print(f"⛔ HTTP error: {e.response.status_code} — {e.response.text}")

            except ValueError:
                print("⛔ Invalid response")

            except RequestException as e:
                print(f"⛔ General error: {e}")
            
        @staticmethod
        def getPoemByName(name):
            try:
                List = list()
                result = requests.get(TamilNLPWeb.baseurl+"url_gloss.php",params={"url":"export/etext_copy/"+name.lower()+".txt"})
                response = BeautifulSoup(result.content,'html.parser')
                for word_link in response.body.find_all():
                    text = word_link.get_text()
                    if text=="":
                        List.append("\n")
                    else: 
                        List.append(text+" ")
                return "".join(List)
            except Timeout:
                print("⛔ Request timed out")

            except ConnectionError:
                print("⛔ Network problem (DNS failure, refused connection, etc.)")

            except HTTPError as e:
                print(f"⛔ HTTP error: {e.response.status_code} — {e.response.text}")

            except ValueError:
                print("⛔ Invalid response")

            except RequestException as e:
                print(f"⛔ General error: {e}")
        @staticmethod
        def getRawTextPoemByName(name):
             try:
                result = requests.get(TamilNLPWeb.baseurl+"/export/etext_copy/"+name.lower()+".txt")
                response = BeautifulSoup(result.content,'html.parser')
                return html.unescape(response.encode('latin1').decode('utf-8'))
             except Timeout:
                print("⛔ Request timed out")

             except ConnectionError:
                print("⛔ Network problem (DNS failure, refused connection, etc.)")

             except HTTPError as e:
                print(f"⛔ HTTP error: {e.response.status_code} — {e.response.text}")

             except ValueError:
                print("⛔ Invalid response")

             except RequestException as e:
                print(f"⛔ General error: {e}")
        
        def glossary(word):
             #TODO
             return 

# Usage              
for name in TamilNLPWeb.getListOfPoems():
    with open("test.text","w+") as text:
        print("Fetching "+name)
        print(TamilNLPWeb.getPoemByName(name),file=text)
        break

