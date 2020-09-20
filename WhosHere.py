import requests
import json
print("""
░░     ░░ ░░   ░░  ░░░░░░  ░░░░░░░ ░░░░░░░     ░░   ░░ ░░░░░░░ ░░░░░░  ░░░░░░░ 
▒▒     ▒▒ ▒▒   ▒▒ ▒▒    ▒▒ ▒▒      ▒▒          ▒▒   ▒▒ ▒▒      ▒▒   ▒▒ ▒▒      
▒▒  ▒  ▒▒ ▒▒▒▒▒▒▒ ▒▒    ▒▒ ▒▒▒▒▒▒▒ ▒▒▒▒▒       ▒▒▒▒▒▒▒ ▒▒▒▒▒   ▒▒▒▒▒▒  ▒▒▒▒▒   
▓▓ ▓▓▓ ▓▓ ▓▓   ▓▓ ▓▓    ▓▓      ▓▓ ▓▓          ▓▓   ▓▓ ▓▓      ▓▓   ▓▓ ▓▓      
 ███ ███  ██   ██  ██████  ███████ ███████     ██   ██ ███████ ██   ██ ███████ 
                                                    
----------------------------------------by peel1------------------------------
""")

Post_Code = str(input("Input the post code you want to search for (Must be full caps and be one word). Example: EC1M4NP:"))
class Form:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def fullGDork():
    global splicedPC1
    global splicedPC2
    if len(Post_Code) == 6:
        splicedPC1 = Post_Code[:3]
        splicedPC2 = Post_Code[3:]
    else:
        splicedPC1 = Post_Code[:4]
        splicedPC2 = Post_Code[4:]
    print(Form.UNDERLINE + "Websites Containing postcode")
    print("https://www.google.co.uk/search?source=hp&ei=aBxaX6znDYrXkwWv9bCADA&q=intext%3A%22{0}+{1}%22&oq=intext%3A%22{0}+{1}%22&gs_lcp=CgZwc3ktYWIQAzoOCAAQ6gIQtAIQmgEQ5QI6BQgAELEDOggIABCxAxCDAToCCAA6BAgAEApQhAxYgzdgmThoBHAAeACAAWmIAaENkgEEMTguMZgBAKABAaoBB2d3cy13aXqwAQY&sclient=psy-ab&ved=0ahUKEwisu9Xfy97rAhWK66QKHa86DMAQ4dUDCAg&uact=5".format(splicedPC1, splicedPC2))
    print(Form.UNDERLINE + "Websites Related to postcode")
    print("https://www.google.co.uk/search?ei=kR5aX6-dOIrosAeN6464DQ&q=related%3A+%22{0}+{1}%22&oq=related%3A+%22{0}+{1}%22&gs_lcp=CgZwc3ktYWIQA1CcQVicQWCQQ2gAcAB4AIABZIgBtAGSAQMxLjGYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=psy-ab&ved=0ahUKEwjvqdjnzd7rAhUKNOwKHY21A9cQ4dUDCA0&uact=5".format(splicedPC1, splicedPC2))
    print(Form.UNDERLINE + "Websites that contain information about the postcode")
    print("https://www.google.com/search?source=hp&ei=RBxaX424NZHSa5v2t6AK&q=info%3A+%22{0}+{1}%22&btnK=Google+Search&oq=intext%3A%22{0}+{1}%22&gs_lcp=CgZwc3ktYWIQAzoOCC4QsQMQxwEQowIQkwI6CAgAELEDEIMBOgsILhCxAxDHARCjAjoFCAAQsQM6AgguOgUILhCxAzoCCAA6CAguELEDEJMCOggILhDHARCvAToLCC4QxwEQrwEQkwI6BAgAEApQ2g5Yu1FgqFNoCXAAeACAAX2IAc8QkgEEMTguNpgBAKABAaoBB2d3cy13aXqwAQA&sclient=psy-ab&ved=0ahUKEwiN6ufOy97rAhUR6RoKHRv7DaQQ4dUDCAg&uact=5".format(splicedPC1, splicedPC2))
    print(Form.UNDERLINE + "Websites that contain Misc information about the postcode")
    print("https://www.google.com/search?ei=lSBaX_fbJsHTkwXJ5L_AAw&q=define%3A+%22{0}+{1}%22&oq=define%3A+%22{0}+{1}%22&gs_lcp=CgZwc3ktYWIQA1CkI1iJK2CuLGgAcAB4AIABcIgBkwSSAQM1LjGYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=psy-ab&ved=0ahUKEwi3-szdz97rAhXB6aQKHUnyDzgQ4dUDCA0&uact=5".format(splicedPC1, splicedPC2))
    pass

def QikInfo():
    global Req
    global ReqI
    global info
    url = "https://api.postcodes.io/postcodes/{0}%20{1}".format(splicedPC1, splicedPC2)
    payload = {}
    headers = {
        'authority': 'api.postcodes.io',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'accept': '*/*',
        'origin': 'https://www.which.co.uk',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.which.co.uk/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.text.encode('utf8')
    Tmp = json.loads(response)
    info = Tmp['result']
    Adv = info['codes']
    Req = Adv['parish']
    ReqI = info['admin_county']



def HQWebsites():
    print(Form.BOLD + "Specific Houses Tax Bands (Provides Approx on house value)")
    print("http://www.mycounciltax.org.uk/results?postcode={0}+{1}".format(splicedPC1, splicedPC2))
    print(Form.BOLD + "Large Amount of Information on Postcode including Census Data")
    print("https://www.streetcheck.co.uk/postcode/{0}".format(Post_Code))
    print(Form.BOLD + "Credit Card Acceptance and Housing Research + Misc Data")
    print("https://www.checkmyfile.com/postcode-check/{0}-{1}.htm".format(splicedPC1, splicedPC2))
    print(Form.BOLD + "Parish Information (Highly Detailed and mostly precise)")
    print("https://www.nomisweb.co.uk/reports/localarea?compare={0}".format(Req))
    print(Form.BOLD + "Most Local Information Highly Detailed and as precise as possible")
    print("https://www.postcodearea.co.uk/postaltowns/{0}/{1}/".format(ReqI, Post_Code.lower()))
    print(Form.BOLD +"Postcode located in the parish of {0} in {1}".format(info['parish'], info['nhs_ha']))
    print(Form.BOLD +"Postcode is at exactly: Longitude: {0} and latitude {1}".format(info['longitude'], info['latitude']))
    print(Form.BOLD +"List of Codes assosiated with postcode (these are for census or other more niche lookups): {}".format(info['codes']))


fullGDork()
QikInfo()
HQWebsites()
