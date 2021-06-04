try:

    from selenium import webdriver
    import re
    from webdriver_manager.chrome import ChromeDriverManager
    import requests
    import time
    from datetime import datetime
    from selenium import webdriver
    from urllib.request import unquote
    from bs4 import BeautifulSoup
    import requests
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    import time
    from datetime import datetime
    import urllib3
    import random
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    import pdfplumber
except:
    print("library not found")
start = time.time()
now = datetime.now()

chrome_options=webdriver.ChromeOptions()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 ' \
                 'Safari/537.36'
chrome_options.headless=True
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")


f= open("log_countries_all.txt","a+")
urllib3.disable_warnings()
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)
def responsecode_success(cntry: str,validatedelem:str,responscode:str):
    f1=open("log_allcount.txt","a+")
    f1.write("\n")
    f1.write("\n")
    f1.write("-" * 65)
    f1.write("\n")
    f1.write("-" * 65)
    f1.write("\n")
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    f1.write("Date:%s" % dt_string)
    f1.write("\n")
    f1.write('Country:%s'%cntry)
    f1.write("\n")
    f1.write('Validated:%s' %validatedelem)
    f1.write("\n")
    f1.write('Result:Sucess   %s'%responscode)
    f1.close()
def responsecode_unsuccess(cntry: str,validatedelem:str,responscode:str):
    f1 = open("log_allcount.txt", "a+")
    f1.write("\n")
    f1.write("\n")
    f1.write("-" * 65)
    f1.write("\n")
    f1.write("-" * 65)
    f1.write("\n")
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    f1.write("Date:%s" % dt_string)
    f1.write("\n")
    f1.write('Country:%s' % cntry)
    f1.write("\n")
    f1.write('Validated:%s' %validatedelem)
    f1.write("\n")
    f1.write('Result:UnSucess')
    f1.write("\n")
    f1.write('Remarks:Check The Status code   %s' % responscode)
    f1.close()
def datavalidation_sucess(cntry: str,validatedelem:str,keyelm:str):
    f1 = open("log_allcount.txt", "a+")
    f1.write("\n")
    f1.write("-" * 65)
    f1.write("\n")
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    f1.write("Date:%s" % dt_string)
    f1.write("\n")
    f1.write('Country:%s'%cntry)
    f1.write("\n")
    f1.write('Validated:%s '%validatedelem)
    f1.write("\n")
    f1.write('Result:Sucess')
    f1.write("\n")
    f1.write('Scraped Element   %s' % keyelm)
    f1.write("\n")
    f1.write("\n")
    f1.write("-" * 65)
    f1.write("\n")
    f1.write("-" * 65)
def datavalidation_Unsucess(cntry: str,validatedelem:str,keyelm:str):
    f1 = open("log_allcount.txt", "a+")
    f1.write("\n")
    f1.write("-" * 65)
    f1.write("\n")
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    f1.write("Date:%s" % dt_string)
    f1.write("\n")
    f1.write('Country:%s'%cntry)
    f1.write("\n")
    f1.write('Validated:%s '%validatedelem)
    f1.write("\n")
    f1.write('Result:UnSucess')
    f1.write("\n")
    f1.write('Remarks:Check The Element   %s' % keyelm)
    f1.write("\n")
    f1.write("-" * 65)
    f1.write("\n")
    f1.write("-" * 65)

class Random_Proxy(object):

    def __init__(self):
        self.__url = 'https://www.sslproxies.org/'
        self.__headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.wikipedia.org/',
            'Connection': 'keep-alive',
            }
        self.random_ip = []
        self.random_port = []

    def __random_proxy(self):

        """
        This is Private Function Client Should not have accesss
        :return: Dictionary object of Random proxy and port number
        """

        r = requests.get(url=self.__url, headers=self.__headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        # Get the Random IP Address
        for x in soup.findAll('td')[::8]:
            self.random_ip.append(x.get_text())

        # Get Their Port
        for y in soup.findAll('td')[1::8]:
            self.random_port.append(y.get_text())

        # Zip together
        z = list(zip(self.random_ip, self.random_port))

        # This will Fetch Random IP Address and corresponding PORT Number
        number = random.randint(0, len(z)-50)
        ip_random = z[number]

        # convert Tuple into String and formart IP and PORT Address
        ip_random_string = "{}:{}".format(ip_random[0],ip_random[1])

        # Create a Proxy
        proxy = {'https':ip_random_string}

        # return Proxy
        return proxy

    def Proxy_Request(self,request_type='get',url='',**kwargs):
        """

        :param request_type: GET, POST, PUT
        :param url: URL from which you want to do webscrapping
        :param kwargs: any other parameter you pass
        :return: Return Response
        """
        while True:
            try:
                proxy = self.__random_proxy()
                print("Using Proxy {}".format(proxy))
                r = requests.request(request_type,url,proxies=proxy,headers=self.__headers ,timeout=8, **kwargs)
                return r
                break
            except:
                pass
proxy = Random_Proxy()

def uk_country():
    url = "https://www.admiralty.co.uk/maritime-safety-information/radio-navigational-warnings/low-bandwidth/navarea-1"
    #options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    # browser = webdriver.Chrome("D:\Projects\webscrap\chromedriver\chromedriver.exe")
    browser.get(url)
    header = []
    # r = requests.get(url)
    # print(r.status_code)
    try:
        a = browser.find_element_by_id('chkSelectAllOption')
        a.click()
        # WebDriverWait(browser, 50).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='submain']/div/div/div/div/ul/li"))).click()
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='Show Selection']"))).click();
        page = browser.page_source
        soup = BeautifulSoup(page, 'html.parser')
        tab = soup.find("table", {"class": "radio-navigational-warning-table table-accordion"})

        keylist = []
        h3 = soup.find_all("h3")

        for i in h3:
            st = str(i)
            #print(st)
            if (st.__contains__("NAVAREA I")):
                r = st.strip('<h3>')
                r1 = r.strip('</')
                keylist.append(r1)
            # print(i)

        # print(i)
        # print(keylist)
        indices = []
        for ind in keylist:
            sentence = str(tab.text)
            ress = sentence.index(ind)
            indices.append(ress)
        # print(indices)
        #print(len(keylist))
        #print([sentence])
        vallist = [sentence[i:j] for i, j in zip(indices, indices[1:] + [None])]
        #print(len(vallist))
        # print(vallist)
        res = {}
        for key in keylist:
            for value in vallist:
                res[key] = value
                vallist.remove(value)
                break
        print(res)

        # validation part start
        responsecode = requests.get(url)
        if (responsecode.ok):
           responsecode_success('UK','Responsecode',responsecode.status_code)
        else:
            responsecode_unsuccess('UK','Responsecode',responsecode.status_code)

        header = browser.find_elements_by_xpath("//*[@id='rnw4937102200']/td/h3")
        for i in header:
            # print(i.text)
            length_expected = len("NAVAREA I 042/21")
            batRegex = re.compile(r'NAVAREA')
            mo = batRegex.search(str(i.text))
            if (mo == None):
                rrt = ''
            else:
                if (length_expected == len(i.text)):
                    datavalidation_sucess('UK','Length of key',i.text)


                else:
                    datavalidation_Unsucess('UK','Length of key',i.text)

            # validation part end

            # print(i.text)
            # print(mo3)
            # print(allinform)
            # if(i==)
            # print(i.text)
        # print(header)
        browser.close()
    except Exception as e:
        print("Expected Format is not performed")
        datavalidation_Unsucess('UK', 'Response', e)
        browser.close()

    #f.close()
def argentina():
    url = "http://www.hidro.gov.ar/Nautica/inv.asp"
    browser = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    browser.get(url)
    try:
        a = browser.find_elements_by_xpath("/html/body/main/section[2]/article/div/p[1]")[0].text
        b = browser.find_elements_by_xpath("/html/body/main/section[2]/article/div/p[2]")[0].text
        c = browser.find_elements_by_xpath("/html/body/main/section[2]/article/div/p[3]")[0].text
        d = browser.find_elements_by_xpath("//*[@id='main']/section[2]/article/div/pre/h2")

        Maincontent = browser.find_elements_by_xpath("//*[@id='main']/section[2]/article/div/pre")[0].text
        maincontentstr = str(Maincontent)
    except Exception as e:
        print("Browser Not giving any Elment")
        browser.close()
        responsecode_unsuccess('Argentina','Responsecode',e)
    # print(Maincontent)

    keylist = []
    vallist = []

    try:

        message = browser.find_elements_by_tag_name('h2')

        for i in message:
            keylist.append(i.text)
        # print(i.text)

        posli = []
        for k in keylist:
            keylisstr = str(k)
            pos = maincontentstr.find(keylisstr)
            posli.append(pos)

        i = 0
        for j in posli:

            if (i == 0):
                i = i + 1

            else:
                out = maincontentstr[posli[i - 1]:posli[i]]
                i = i + 1
                vallist.append(out)
        res = {}
        for key in keylist:
            for value in vallist:
                res[key] = value
                vallist.remove(value)
                break
        # validation part start
        responsecode = requests.get(url)
        if (responsecode.ok):
            responsecode_success('Argentina','Responsecode',responsecode.status_code)
        else:
            responsecode_unsuccess('Argentina','Responsecode',responsecode.status_code)

            # print("Unsucessfull", responsecode.status_code)

        # validation part end

        for i in d:
            expected_strlen = len("NAVAREA - 0129 - 06/04/2021")
            scraped_strlen = len(str(i.text))
            if (expected_strlen == scraped_strlen):
                datavalidation_sucess('Argentina','Length Of the Key',str(i.text))


            else:
                datavalidation_Unsucess('Argentina','Length Of the Key',str(i.text))
        print(res)
        # print(res)
        browser.close()
        #f.close()
    except Exception as e:
        print("Expected Schema Is not formed ")
        browser.close()
        datavalidation_Unsucess('Argentina','DataValidation Fail',e)
def Austrelia():
    url = "https://www.operations.amsa.gov.au/AMSA.Web.MSIPublication/Home"
    browser = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    # browser = webdriver.Chrome("D:\Projects\webscrap\chromedriver\chromedriver.exe")
    browser.get(url)
    try:
        browser.find_element_by_id('SelectAll').is_selected();
        e = browser.find_element_by_id('Search')
        e.click()
        e1 = browser.find_elements_by_xpath("//*[@id='theForm']")
    except Exception as e:
        print("Browser Not Get any Element", e)
        responsecode_unsuccess('Austrelia','Responsecode',e)

    # print(e1)
    def first_substring(strings, substring):
        return next(i for i, string in enumerate(strings) if substring in string)

    def find(lst, predicate):
        return (i for i, j in enumerate(lst) if predicate(j)).next()

    # indexlist1=[]
    parts_indexlist = []

    for i in e1:
        try:
            tempstr = str(i.text)
            # print("am in",tempstr)
            part2_index = tempstr.find('Part 2. NAVAREA X warnings:')
            part3_index = tempstr.find('Part 3. Coastal warnings:')

            parts_indexlist.append(part2_index)
            parts_indexlist.append(part3_index)

            indexlist1 = [m.start() for m in re.finditer('SECURITE', tempstr)]

            total_parts = [tempstr[i:j] for i, j in zip(indexlist1, indexlist1[1:] + [None])]
            navarea_part = tempstr[part2_index: part3_index]

            navarea_part_secur_indexlist = [m.start() for m in re.finditer('SECURITE', navarea_part)]
            ref_length_sec = len(navarea_part_secur_indexlist)
            navarea_part_list = [navarea_part[i:j] for i, j in
                                 zip(navarea_part_secur_indexlist, navarea_part_secur_indexlist[1:] + [None])]
        except Exception as e:
            print("An Error Occurred ", e)
            responsecode_unsuccess('Austrelia','Responsecode',e)
    # print(navarea_part_list
    keylist = []
    for i in navarea_part_list:
        try:

            eachstr = str(i)
            pgstr = ''.join([i for i in eachstr if i.isalnum()])
            total_raw_strg_key = pgstr[23:48]
            number_strg = total_raw_strg_key[20:23]
            year_string = total_raw_strg_key[23:25]
            total_key = "NAVAREA X " + number_strg + '/' + year_string
            keylist.append(total_key)
        except Exception as e:
            print("No such Element found in slicing", e)
            datavalidation_Unsucess('Austrelia','DataValidationFail',e)

    res = {}
    for key in keylist:
        for value in navarea_part_list:
            res[key] = value
            navarea_part_list.remove(value)
            break

    responsecode = requests.get(url)
    if (responsecode.ok):
        responsecode_success('Austrelia','Responsecode',responsecode.status_code)

    else:
        responsecode_unsuccess('Austrelia', 'Responsecode', responsecode.status_code)
    print(res)
    # print(res)
    if (ref_length_sec == len(res)):
        datavalidation_sucess('Austrelia','Count of SECURITE',str(ref_length_sec))

    else:
        datavalidation_Unsucess('Austrelia','Count of SECURITE',str(ref_length_sec))
    browser.close()
    #f.close()
def Brazil():
    try:
        url = "https://www.marinha.mil.br/chm/dados-do-segnav-avradio-script/navarea-v-0"
        browser = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)

        # browser = webdriver.Chrome("D:\Projects\webscrap\chromedriver\chromedriver.exe")
        browser.get(url)
        try:
            a = browser.find_elements_by_xpath(
                "/html/body/div[3]/div/section/div/section/div/article/div/div/div/div/div/p/spam")
            for i in a:
                print("Update:" + i.text)

            b = browser.find_elements_by_xpath("//*[@id='node-86818']/div")

            keylist = []
            vallist = []
            for k in b:
                l = k.find_elements_by_xpath("//*[@id='avradio-avisos']/b")
                for m in l:
                    keylist.append(m.text)
            # print(m.text)
            # print(k.text)

            for m in b:
                l = k.find_elements_by_xpath("//*[@id='avradio-avisos']")
                for n in l:
                    str2 = str(n.text)
                    print(str2)

            # print(keylist)
            posli = []
            for k in keylist:
                str3 = str(k)
                pos = str2.find(str3)
                posli.append(pos)

            i = 0

            for j in posli:
                if (i == 0):
                    i = i + 1

                else:
                    out = str2[posli[i - 1]:posli[i]]
                    i = i + 1
                    vallist.append(out)
            res = {}
            try:
                for key in keylist:
                    for value in vallist:
                        res[key] = value
                        vallist.remove(value)
                        break
            except Exception as e:
                print("key val list not arranged")
                datavalidation_Unsucess('Brazil','DataValidationFail',e)

        # validation start
            responsecode = requests.get(url)
            if (responsecode.ok):
                responsecode_success('Brazil','Responsecode',responsecode.status_code)
            else:
                responsecode_unsuccess('Brazil','Responsecode',responsecode.status_code)
            for i in keylist:

                expected_strlen = len("0070/21")
                scraped_strlen = len(str(i))
                if (expected_strlen == scraped_strlen):
                    # print("Validated Succesfull Key")
                    datavalidation_sucess('Brazil','LengthOfkey',str(i))



                else:
                    # print("Please Check Key",i.text)
                    datavalidation_Unsucess('Brazil','LengthOfkey',str(i))


        # 0151 / 21
        # validation End
        # print(res)
            print(res)
            browser.close()
            #f.close()
        except Exception as e:
            print("Expected Schema Is not Arranaged")
            datavalidation_Unsucess('Brazil','DataValidationFail',e)
            browser.close()
    except Exception as e:
        print("Expected Schema Is not Arranaged")
        datavalidation_Unsucess('Brazil', 'DataValidationFail', e)
        browser.close()
def canadaXVII():
    try:
        url = "http://inter-w02.ccg-gcc.gc.ca/Central-And-Artic/Notship/report?todo=warning&area_id=1&date_start=&date_end="
        # browser = webdriver.Chrome("D:\Projects\webscrap\chromedriver\chromedriver.exe")
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        browser.get(url)
        responsecode = requests.get(url)
        if (responsecode.ok):
            responsecode_success('canadaXVII', 'Responsecode', responsecode.status_code)
        else:
            responsecode_unsuccess('canadaXVII', 'Responsecode', responsecode.status_code)
        a = browser.find_elements_by_class_name("center")
        myDict = dict()
        vallist = []
        keylist = []
        for i in a:
            try:
                l = i.find_elements_by_xpath("/html/body/div/div/div[6]/div/p")
                for k in l:
                    set = str(k.text)
                    keylis = set.partition('\n')[0]

                    match = re.search(r'NAVAREA XVII+ \w+/\w+', keylis)
                    if match:
                        datavalidation_sucess('CanadaXVII', 'Match Patteren of Key', keylis)
                    else:
                        datavalidation_Unsucess('CanadaXVII', 'Match Patteren of Key', keylis)
                    # print("Validated Sucessfull Key", match)

                    vallis = set.partition('\n')[2]
                    doc = vallis.replace('\n', ' ')
                    keylist.append(keylis)
                    vallist.append(doc)
            # print(keylis)
            # print(vallis)
            # see=k.partition('\n')[0]
            # print(see)
            # print(k.text)
            # print(i.text)
            except Exception as e:
                print("error found", e)
                browser.close()
        res = {}
        for key in keylist:
            for value in vallist:
                res[key] = value
                vallist.remove(value)
                break
        print(res)
        browser.close()
    except Exception as e:
        datavalidation_Unsucess('CanadaXVII', 'Failed To Validate', e)
    #f.close()
def canadaxviii():
    try:
        url = "http://inter-w02.ccg-gcc.gc.ca/Central-And-Artic/Notship/report?todo=warning&area_id=2&date_start=&date_end="
        # browser = webdriver.Chrome("D:\Projects\webscrap\chromedriver\chromedriver.exe")
        browser = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        browser.get(url)
        responsecode = requests.get(url)
        if (responsecode.ok):
            responsecode_success('canadaXVIII','Responsecode',responsecode.status_code)
        else:
            responsecode_unsuccess('canadaXVIII','Responsecode',responsecode.status_code)
        a = browser.find_elements_by_class_name("center")
        myDict = dict()
        vallist = []
        keylist = []
        for i in a:
            try:
                l = i.find_elements_by_xpath("/html/body/div/div/div[6]/div/p")
                for k in l:
                    set = str(k.text)
                    keylis = set.partition('\n')[0]

                    match = re.search(r'NAVAREA XVIII+ \w+/\w+', keylis)
                    if match:
                        datavalidation_sucess('CanadaXVIII', 'Match Patteren of Key', keylis)
                    else:
                        datavalidation_Unsucess('CanadaXVIII', 'Match Patteren of Key', keylis)
                # print("Validated Sucessfull Key", match)

                    vallis = set.partition('\n')[2]
                    doc = vallis.replace('\n', ' ')
                    keylist.append(keylis)
                    vallist.append(doc)
            # print(keylis)
            # print(vallis)
            # see=k.partition('\n')[0]
            # print(see)
            # print(k.text)
        # print(i.text)
            except Exception as e:
                print("error found", e)
                browser.close()
        res = {}
        for key in keylist:
            for value in vallist:
                res[key] = value
                vallist.remove(value)
                break
        print(res)
        browser.close()
    except Exception as e:
        datavalidation_Unsucess('CanadaXVIII', 'Failed To Validate', e)
    # responsecode = requests.get(url)
    # if (responsecode.ok):
    # print("Sucessfull", responsecode.status_code)
    # else:
    # print("Unsucessfull", responsecode.status_code)


    #f.close()
def chilie():
    url = "http://www.shoa.mil.cl/radio/index.php?idioma=1#"
    browser = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    # browser = webdriver.Chrome("D:\Projects\webscrap\chromedriver\chromedriver.exe")
    browser.get(url)
    try:

        e = browser.find_element_by_id("buttonu1330")
        e.click()

        WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, "//*[@id='cuerpo-modal']/br")))
        html_source = browser.page_source
        soup = BeautifulSoup(html_source, 'html.parser')
        header_text = soup.find_all('div', {'class': 'header-modal'})  # for header text
        br_tags = soup.find('br').next_siblings
        res = []
        for n in br_tags:
            s = str(n)
            res_br_tag = s.split('<br/>')
            res.append(res_br_tag)
    except Exception as e:
        print("error found", e)
        responsecode_unsuccess('Chile','NoTagFoundError',e)
        browser.close()
    indexedstr = []
    refkeylis = []
    vallis = []
    try:
        for i in res:
            resst = str(i[0])
            if (resst == ''):
                rer = ''
            else:
                indexedstr.append(i)
        for j in indexedstr:
            for k in j:
                try:

                    temp_str = str(k)
                    temp_str1 = temp_str.strip('</p>')
                    res_str_val = temp_str1.strip()
                # print([res_str_val])
                    if not res_str_val:
                        rer = ''
                    else:
                        if (res_str_val.__contains__('NAVAREA XV')):
                         refkeylis.append(res_str_val)

                        vallis.append(res_str_val)
                # print([vallis])
                except Exception as e:
                    print("error found ", e)
                    browser.close()
    # yearlis=vallis[3:6]
    # print(len(keylis))
    # for i in yearlis:

    # print("keylistlist",keylis)
        restotalstr = ''.join(str(e) for e in vallis)
        bad_chars = ['\xa0']
        tes_str = ''
        for i in bad_chars:
            test_string = restotalstr.replace(i, '')
            tes_str += test_string

        test_sub = "YEAR "
        # All occurrences of substring in string
        indexlis = [i for i in range(len(tes_str)) if tes_str.startswith(test_sub, i)]
        parts_totalstr = [tes_str[i:j] for i, j in zip(indexlis, indexlis[1:] + [None])]

        yearlis = []
        stringlist = []
        for i in parts_totalstr:
            match = re.search(r'YEAR \d{4}:', i)
            if match:
                yearlis.append(match)
            else:
                stringlist.append(i)

        vallisi = []
        keylis = []
        for i in stringlist:
            match = re.findall(r'NAVAREA XV \d{4}', i)
            if match:
                keylis.append(match)
    #print(keylis)
        indexlis = []
        partsli = []
        my_li = []
        cnt = 0
        for i in keylis:
            for j in i:
                s1 = str(j)
                # print(s1)
                ind1 = stringlist[cnt].index(s1)
                indexlis.append(ind1)
            parts_totalstr = [stringlist[cnt][i:j] for i, j in zip(indexlis, indexlis[1:] + [None])]
            my_li.extend(parts_totalstr)
            print(len(parts_totalstr))
            indexlis.clear()
            cnt += 1

        print(len(partsli))

        print(indexlis)

        for i in stringlist:
            year = i[:9]
            year1 = year[-4:]
            # print(year1)
            y = re.findall(r'NAVAREA XV \d{4}', i)
            if y:
                for z in y:
                    a = z + "/" + year1
                    print(a)
                    vallisi.append(a)

        res3 = {}
        for key in vallisi:
            for v in my_li:
                res3[key] = v
                my_li.remove(v)
                break
        print(res3)
    # print(len(res3))

        responsecode = requests.get(url)
        if (responsecode.ok):
            responsecode_success('Chile', 'Responsecode', responsecode.status_code)
        # print("Sucessfull", responsecode.status_code)
        else:
            responsecode_unsuccess('Chile', 'Responsecode', responsecode.status_code)
        if (len(refkeylis) == len(res3)):
            datavalidation_sucess('Chile','Count of Matched Patteren Elements',str(len(refkeylis)))

        # f.write("\n")
        # print("all Key values data ssucessfully Scraped")
        else:
            datavalidation_Unsucess('Chile','Count of Matched Patteren Elements',str(len(refkeylis)))


        browser.close()
    except Exception as e:
        print("error found", e)
        responsecode_unsuccess('Chile','FoundError',e)
        browser.close()
    #end = time.time()
    #f.close()
def France():
    try:


        #r = proxy.Proxy_Request(url="https://gan.shom.fr/navarea/NavareaIIenVigueur.txt", request_type='get')
        r=requests.get("https://gan.shom.fr/navarea/NavareaIIenVigueur.txt")
        if (r.ok):
            responsecode_success('France', 'Responsecode', r.status_code)
        else:
            responsecode_unsuccess('France', 'Responsecode', r.status_code)

        # print("Response Status code",r.status_code)
        res_stri = r.text
        # res_stri="ENGLISH VERSION --------------------------------------------------------------------------------------------------\r\nNAVAREA II WARNINGS IN FORCE ON 11 MAR 2021 AT 04H30 UTC.\r\n\r\n\r\n\r\nNAVAREA II 112/21\r\nCAP BLANC.\r\n1. CABLE LAYING OPERATIONS IN PROGRESS BY CABLE SHIPS PETER FABER AND\r\n   ILE DE BREHAT UNTIL 262359 UTC MAR 21 IN AREA BOUNDED BY:\r\n   24-22N 016-58W / 24-19N 016-49W / 23-42N 015-58W / 23-41N 015-59W\r\n   24-18N 016-50W / 24-21N 016-58W.\r\n   WIDE BERTH REQUESTED.\r\n2. CANCEL THIS MESSAGE 270100 UTC MAR 21.\r\n\r\n\r\nNAVAREA II 109/21\r\nCAP TIMIRIS.\r\nGULF OF GUINEA.\r\n1. LAST KNOWN POSITIONS OF MOBILE OIL RIGS AND DRILL SHIPS\r\n   AT 09 MAR 21:\r\n   PACIFIC SANTA ANNA   17-43.9N  016-46.1W\r\n   TRIDENT VIII         04-34.6N  008-25.3E  \r\n2. CANCEL NAVAREA II 025/21.\r\n\r\n\r\nNAVAREA II 108/21\r\nCANARIAS.\r\n1. WHITE WOODEN BOAT, 10 METER LENGTH, ADRIFT\r\n   IN VICINITY 26-12.7N 016-52.9W AT 082135 UTC MAR 21.\r\n2. CANCEL THIS MSG 112300 UTC MAR 21.\r\n\r\n\r\nNAVAREA II 106/21\r\nAGADIR-TARFAYA.\r\n1. GUNNERY EXERCISES FROM 110001 UTC TO 132359 UTC MAR 21.\r\n   A. WITHIN 20 MILES OF 29-53N 010-15W BETWEEN 270 DEGREES \r\n      AND 360 DEGREES.\r\n   B. IN AREA BOUNDED BY: \r\n      29-18N 011-06W / 28-46N 010-48W / 28-42N 010-56W / 29-08N 011-28W\r\n2. CANCEL THIS MSG 140100 UTC MAR 21.\r\n\r\n\r\nNAVAREA II 105/21\r\n1. NAVAREA II WARNINGS IN FORCE AT 071630 UTC MAR 21.\r\n   2020 SERIES: 083.\r\n   2021 SERIES: 025, 039, 041, 074, 096, 100, 102, 103, 105.\r\n2. ONLY THOSE LESS THAN 42 DAYS OLD ARE DAILY BROADCAST ON SAFETY\r\n   NET AT 04H30 AND 16H30 UTC.\r\n3. THE COMPLETE TEXTS OF ALL IN-FORCE NAVAREA II WARNINGS ARE\r\n   AVAILABLE FROM THE SHOM WEBSITE AT: DIFFUSION.SHOM.FR\r\n4. ALTERNATIVELY, THESE MAY BE REQUESTED BY E-MAIL AT:\r\n   COORD.NAVAREA2@SHOM.FR\r\n5. CANCEL NAVAREA II 092/21.\r\n\r\n\r\nNAVAREA II 100/21\r\nGULF OF GUINEA - POINTE NOIRE.\r\n1. UNDERWATER OPERATIONS BY M/V THALASSA FROM 09 TO 31 MAR 21\r\n   IN FOLLOWING POSITIONS:\r\n   A. 00-00S 010-00W.\r\n   B. 00-00S 000-00W.\r\n   C. 06-00S 010-00W.\r\n   WIDE BERTH REQUESTED.\r\n2. CANCEL THIS MSG 01 APR 21.\r\n\r\n\r\nNAVAREA II 096/21\r\nTARFAYA.\r\nCHART 7270 FR 1082 INT.\r\nSIDI IFNI LIGHTHOUSE 29-23N 010-11W UNLIT.\r\n\r\n\r\nNAVAREA II 074/21\r\nPAZENN - IROISE.\r\n1. ODAS BUOYS ESTABLISHED IN:\r\n   A. 47-44.06N 005-52.48W\r\n   B. 47-21.90N 006-11.03W \r\n   IT IS REQUESTED NOT TO ANCHOR, DREDGE, TRAWL OR FISH \r\n   WITHIN A RADIUS OF 700 METERS AROUND THESE POSITIONS.\r\n2. SCIENTIFIC INSTRUMENT MOORED IN 47-35.44N 007-22.28W. \r\n   LEAST DEPTH OF INSTRUMENT 15 METERS. \r\n   IT IS REQUESTED NOT TO ANCHOR, DREDGE, TRAWL OR FISH \r\n   AROUND THIS POSITION.\r\n3. CANCEL NAVAREA II 073/21.\r\n\r\n\r\nNAVAREA II 041/21\r\nCASABLANCA.\r\n1. GUNNERY EXERCISES 0000 UTC TO 2359 UTC DAILY \r\n   08 FEB THRU 31 MAR 21 WITHIN 20 MILES OF 33-41N 008-03W\r\n   BETWEEN 270 DEGREES AND 360 DEGREES.\r\n2. CANCEL THIS MSG 010100 UTC APR 21.\r\n\r\n\r\nNAVAREA II 083/20\r\nMOROCCO.\r\n1. DUE SAFETY MEASURES TO COMBAT COVID-19, ALL MOROCCAN PORTS  \r\n   WILL KEEP CLOSED TO PASSENGER SHIPS AND PLEASURE CRAFTS \r\n   UNTIL FURTHER NOTICE.\r\n2. CANCEL NAVAREA II 082/20.\r\n\r\n\r\n\r\n"
        res_index = []
        res_index1 = []
        res_index2 = []

        def printIndex(str, s):
            flag = False;
            if (s == '\r\n\r\n\r\n'):
                for i in range(len(str)):
                    if (str[i:i + len(s)] == s):
                        # print(i, end=" ");
                        res_index1.append(i)
                        flag = True;
            elif (s == '\r\n\r\n\r\n\r\n'):
                for i in range(len(str)):
                    if (str[i:i + len(s)] == s):
                        # print(i, end=" ");
                        res_index.append(i)
                        flag = True;
            elif (s == '\r\n'):
                for i in range(len(str)):
                    if (str[i:i + len(s)] == s):
                        # print(i, end=" ");
                        res_index2.append(i)
                        flag = True;
            if (flag == False):
                print("NONE");

        france_index = res_stri.find('VERSION FRANCAISE')
        english_index = res_stri.find('ENGLISH VERSION')
        slicedresultstring = res_stri[english_index:france_index]
        # print([slicedresultstring])
        printIndex(slicedresultstring, '\r\n')
        # print([res_index2[0]])
        head_str = slicedresultstring[0:res_index2[0]]
        # print(head_str)
        inforce_str = slicedresultstring[res_index2[0]:res_index2[1]]
        # print(inforce_str)
        content_string = slicedresultstring[res_index2[1]:]

        # match = re.search(r'NAVAREA XII, key)
        # print(content_string)
        # =content_string.find('\r\n\r\n\r\n\r\n')
        # slicedcontentstring=slicedresultstring[]
        printIndex(content_string, '\r\n\r\n\r\n\r\n')
        # print(res_index)
        contentstart_string = res_stri[res_index[0]:res_index[1]]
        printIndex(content_string, '\r\n\r\n\r\n')
        # print(res_index1)
        onepagestringparts = [content_string[i:j] for i, j in zip(res_index1, res_index1[1:] + [None])]
        # print(onepagestringparts)
        webextractedkeylis = []
        for i in onepagestringparts:
            # print("am content String", [content_string])
            match = re.findall(r'NAVAREA II +\w+/\w+', i)
            if (len(match) > 1):
                match.pop(1)
                webextractedkeylis.append(match)
                # print(match)
            else:
                webextractedkeylis.append(match)
                # print(match)
            # match1 = re.findall(r'CANCEL NAVAREA II +\w+/\w+', i)
            # print(match)
            # print(match1)
        # print("before",webextractedkeylis)
        without_empty_strings = [ele for ele in webextractedkeylis if ele != []]
        # print("after",without_empty_strings)
        len_sourcekey = len(without_empty_strings)
        # print(len(onepagestringparts))
        # print([onepagestringparts])#total val list
        vallist = []
        for i in onepagestringparts:
            if (i == '\r\n'):
                s = ''
            else:
                vallist.append(i)
        # print(vallist)
        # [item.strip() for item in my_string.split(',')]
        total_parts = []
        for i in onepagestringparts:
            parts = [item.strip() for item in i.split('\r\n')]
            total_parts.append(parts)

        empty_space_removedlist = []
        for j in total_parts:
            test_list = [i for i in j if i]

            if (test_list == []):
                s = ''
            else:
                empty_space_removedlist.append(test_list)
        # print(len(j))
        # print(j[1])
        # print(j[2])
        # print(empty_space_removedlist)
        keylist = []
        for k in empty_space_removedlist:
            key_val = k[0]
            if (
                    key_val == 'ENGLISH VERSION --------------------------------------------------------------------------------------------------'):
                s = ''
            else:
                keylist.append(key_val)
            # print(keylist)
        # print(keylist)
        res = {}
        for key in keylist:
            for value in vallist:
                res[key] = value
                vallist.remove(value)
                break
        if (len_sourcekey == len(res)):
            datavalidation_sucess('France','Founded Key Elements In source Website',str(len_sourcekey))


            # print("Sucessfully")
        else:
            datavalidation_Unsucess('France','Founded Key Elements In source Website',str(len_sourcekey))

        print(res)
        # print(len(res))
    except Exception as e:
        print("An error occured while arrangig schema ")
        datavalidation_Unsucess('France','Found Errror',e)
    # print(temp)
    # print([slicedresultstring])
    #f.close()


def Japan():
    try:
        #start = time.time()
        #now = datetime.now()
        #f = open("log.txt", "a+")
        url = "https://www1.kaiho.mlit.go.jp/TUHO/keiho/navarea11_en.html"
        browser = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        #browser = webdriver.Chrome("D:\Projects\webscrap\chromedriver\chromedriver.exe")
        browser.get(url)
        responsecode = requests.get(url)
        if (responsecode.ok):
            responsecode_success('Japan', 'Responsecode', responsecode.status_code)
        else:
            responsecode_unsuccess('Japan', 'Responsecode', responsecode.status_code)
        temp_year_list = browser.find_elements_by_class_name('tb_keiho')
        list_year = []
        for i in temp_year_list:
            year = str(i.get_attribute('id'))
            list_year.append(year)

            like = browser.find_elements_by_xpath("//ul[@class='slideTab ClearFix']/li")
    except Exception as e:
        print("browser not find any element")
        browser.close()
        responsecode_unsuccess('Japan', 'Responsecode', e)

    # print(len(like))#len(like)
    for x in range(0, len(like)):
        try:
            if like[x].is_displayed():
                # print(like[x].text)
                like[x].click()

        except Exception as e:
            browser.close()
            responsecode_unsuccess('Japan', 'Responsecode', e)
    # //*[@id="tb_keiho_2020"]/tbody/tr/td
    # print(list_year)
    lisstee = []
    hreflis = []
    list_len = []
    try:
        for i in list_year:
            # print("//*[@id='"+i+"']/tbody/tr/td")
            a = browser.find_elements_by_xpath("//*[@id='" + i + "']/tbody/tr/td")
            if (len(a) > 0):
                print("//table[@class='" + i + "']//tbody//tr/td")
                elements = browser.find_elements_by_xpath("//table[@id='" + i + "']//tbody//tr//td");
                elements1 = browser.find_elements_by_xpath("//table[@id='" + i + "']//tbody//tr")
                leng = len(elements1) - 1
                list_len.append(leng)
                for j in elements:
                    ref = j.find_elements_by_xpath("//*[@id='" + i + "']/tbody/tr/td")
                    # print("table",len(ref))
            for k in ref:
                anct = k.find_elements_by_tag_name('a')
                # print(len(anct))
                for m in anct:
                    hrefstr = str(m.get_attribute('href'))
                    if (hrefstr.__contains__("LANG=EG")):
                        hreflin = m.get_attribute('href')
                        hreflis.append(hreflin)
                        # print(m.get_attribute('href'))
    except Exception as e:
        print("No element found ")

        browser.close()
        responsecode_unsuccess('Japan', 'Responsecode', e)
    try:
        previousanch = browser.find_elements_by_xpath("//*[@id='submain']/div/div[2]/div[1]/a")
        previouslis = []
        for m in previousanch:
            hres = m.get_attribute('href')
            previouslis.append(hres)
            # list_len.append(len(hres))
            # print(hres)
            # print("am previous lis",len(previouslis))
            list_len.append(len(previouslis))
        for n in previouslis:
            url = str(n)
            wait = WebDriverWait(browser, 10)
            # browser2 = webdriver.Chrome(ChromeDriverManager().install())
            browser2 =  webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
            browser2.get(url)
            responsecode = requests.get(url)
            if (responsecode.ok):
                print("Sucessfull", responsecode.status_code)
                # outputfile = open('log.txt', 'w')
                # outputfile.write("Sucessfull",responsecode.status_code)
                # outputfile.close()
            else:
                print("Unsucessfull", responsecode.status_code)

            a = browser2.find_elements_by_xpath("//*[@id='submain']/div/div[1]/table/tbody/tr[2]/td[4]/a")
            # print("am",len(a))
            for m in a:
                hrefstr = str(m.get_attribute('href'))
                # print(hrefstr)
                hreflis.append(hrefstr)
            browser2.close()
    except Exception as e:
        print("browser2 not find any element")
        browser.close()
        browser2.close()
        responsecode_unsuccess('Japan', 'Responsecode', e)

    # browser.close()
    # //*[@id="submain"]/div/div[2]/div[1]/a
    # (hreflis)
    try:
        vallist = []
        for j in hreflis:
            url = str(j)
            wait = WebDriverWait(browser, 10)
            browser1 = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
            #browser1 = webdriver.Chrome("D:\Projects\webscrap\chromedriver\chromedriver.exe")
            browser1.get(url)
            responsecode = requests.get(url)
            if (responsecode.ok):
                print("Sucessfull", responsecode.status_code)
            else:
                print("Unsucessfull", responsecode.status_code)

            a = browser1.find_elements_by_xpath("/html/body")
            for k in a:
                textstr = str(k.text)
                vallist.append(textstr)
            # print(textstr)
            browser1.close()
    except Exception as e:
        print("Browser1 not found any element")
        browser.close()
        browser2.close()
        browser1.close()
        responsecode_unsuccess('Japan', 'Responsecode', e)
    try:

        keylist = []
        for k in vallist:
            st1 = str(k)
            st2 = st1.split('\n\n')
            st3 = str(st2[0])
            st4 = st3.split('\n')
            match = re.findall(r'[\w\.-]+Date:[\w\.-]+', st4[1])
            # print("",match)

            # print(st4[1])
            keylist.append(str(st4[1]))

        res = {}
        for key in keylist:
            for value in vallist:
                res[key] = value
                vallist.remove(value)
                break

        sum_allelem = sum(list_len)

        if (sum_allelem == len(res)):
            datavalidation_sucess('Japan','Total Sum Of Each Year Rows',str(sum_allelem))

            # print("All given rows in the source website and scrapped elements are equal")
        else:
            datavalidation_Unsucess('Japan', 'Total Sum Of Each Year Rows', str(sum_allelem))

            # print("Check the Data Validation Unsucessfull")
        print(res)
        browser.close()
    except Exception as e:
        print("Expected Schema is not found")
        browser.close()
        browser2.close()
        browser1.close()
        responsecode_unsuccess('Japan', 'Responsecode', e)
        browser.close()
def Norway():
    try:
        #start = time.time()
        #now = datetime.now()
        #f = open("log.txt", "a+")
        url = "http://kyvreports.kystverket.no/NavcoReport/navareaxixvarsler.aspx"
        # https://msi.nga.mil/api/publications/download?type=view&key=16694640/SFH00000/DailyMemIV.txt
        browser = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        # browser = webdriver.Chrome("D:\Projects\webscrap\chromedriver\chromedriver.exe")
        browser.get(url)

        vallis = browser.find_elements_by_xpath("//*[@id='mainContent']/div/div/div")
        # //*[@id="GridView1"]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]
        key = browser.find_elements_by_xpath("//*[@id='GridView1']/tbody/tr/td/table/tbody/tr[1]/td[2]")
        websiteelementlength = len(key)
    except Exception as e:
        print("broweser Not get any element ")
        responsecode_unsuccess('Norway','Browser Error',e)
        browser.close()
    try:

        myDict = dict()
        vallist = []
        keylist = []
        for j in key:
            # print(j.text)
            keylist.append(j.text)
            # print(j.text)
        cnt = 0

        for i in vallis:
            r = str(i.text)
            print([r])
            doc = r.split('Number:')

            for i in doc:
                if (cnt == 0):
                    cnt = cnt + 1
                    # print(cnt)
                else:
                    print("am",cnt)
                    vallist.append(doc[cnt])
                    cnt=cnt+1

            # print(i)
        # cou=len(doc)
        # con=cou-1
        # print(con)
        # print("am doc 0",doc[0])
        # print("am doc 1",doc[1])
        # print("am doc 2",doc[2])
        # print(doc)
        # for doc in con:

        # vallist.append(doc[i])
        # vallist.append(doc[1])
        # vallist.append(doc[2])
        # vallist.append(doc[3])
        # print(i.text)
        res = {}
        for key in keylist:
            for value in vallist:
                res[key] = value
                vallist.remove(value)
                break
        finalformatdict = len(res)
        responsecode = requests.get(url)
        if (responsecode.ok):
            responsecode_success('Norway', 'Responsecode', responsecode.status_code)
        else:
            responsecode_unsuccess('Norway', 'Responsecode', responsecode.status_code)

        if (websiteelementlength == finalformatdict):
            datavalidation_sucess('Norway','Total Table Element Rows Count',str(websiteelementlength))

            # print("Validated sucessfull")
        else:
            datavalidation_Unsucess('Norway','Total Table Element Rows Count',str(websiteelementlength))


        browser.close()
        #f.close()
        # browser.close()
        print(res)

    except Exception as e:
        print("Expected Schema Is not Arranaged", e)
        datavalidation_Unsucess('Norway','Error Found',e)
        browser.close()
def NewZelanad():
    try:
        #start = time.time()
        #now = datetime.now()
        #f = open("log.txt", "a+")
        url = "https://services.maritimenz.govt.nz/navigational-warnings/"
        browser = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        browser.get(url)
        a = browser.find_elements_by_class_name("main-block")
        target = browser.find_elements_by_class_name("standard-block")
        header = browser.find_elements_by_xpath("//*[@id='content']/div/div/div[1]/div[2]/p")
        key = browser.find_elements_by_xpath("//*[@id='content']/div/div/div/div/h3")
        toatlbody = browser.find_element_by_class_name('main-block')
        # print([toatlbody.text])
        toatlbody_text = toatlbody.text
        spli_body = str(toatlbody_text).split("NZ Coastal Navigation warnings")[0]
        # print([spli_body])
    except Exception as e:

        print("browser not find any element")
        browser.close()
        responsecode_unsuccess('NewZeland','Browser NotGet Element',e)
    try:
        myDict = dict()
        vallist = []
        keylist = []
        for j in key:
            keylist.append(j.text)
        keylist_remo = []
        for i in keylist:
            if i not in keylist_remo:
                keylist_remo.append(i)
        # doc=spli_body.replace('\n', ' ')
        # vallist.append(doc)
        # print([doc])
        # for j in spli_body:
        # r = j.text
        # doc = j.replace('\n', ' ')
        # vallist.append(doc)
        # print("am doc", [doc])

        # old
        indices = []
        for ind in keylist_remo:
            sentence = str(spli_body)
            if (str(ind) in sentence):
                ress = sentence.index(ind)
                indices.append(ress)
            else:
                ss = ''
                # indices.append(ress)

        vallist = [spli_body[i:j] for i, j in zip(indices, indices[1:] + [None])]
        #

        """
        #old
        for j in target:
            r=j.text
            doc = r.replace('\n', ' ')
            vallist.append(doc)
            print("am doc",[doc])
        """
        # print(keylist)
        # print(vallist)
        responsecode = requests.get(url)
        if (responsecode.ok):
            responsecode_success('NewZeland', 'Responsecode', responsecode.status_code)
            # print("Sucessfull", responsecode.status_code)
        else:
            responsecode_unsuccess('NewZeland', 'Responsecode', responsecode.status_code)
            # print("Unsucessfull", responsecode.status_code)
        res = {}
        scrapedlen = []
        for key in keylist:
            match = re.search(r'\w+/\w+', key)

            # print("sucessfull Key Validation",match)
            for value in vallist:
                res[key] = value
                vallist.remove(value)
                break

        if (len(indices) == len(res)):
            datavalidation_sucess('New Zealand','Key Elements Indices length',str(len(indices)))

        else:
            datavalidation_Unsucess('New Zealand','Key Elements Indices length',str(len(indices)))

        browser.close()
        #f.close()
        print(res)

    except Exception as e:
        print("Expected Schema Is not formed ")
        browser.close()
        datavalidation_Unsucess('New Zeland','Found Error',e)
def Pakistan():
    try:
        domain = "https://www.paknavy.gov.pk/hydro/"
        # page = proxy.Proxy_Request(url="https://www.paknavy.gov.pk/hydro/n_navwarn.asp", request_type='get', verify=False)
        page = requests.get("https://www.paknavy.gov.pk/hydro/n_navwarn.asp")
        # responsecode=requests.get(page)
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        if (page.ok):
            responsecode_success('Pakistan', 'Responsecode', page.ok)
        else:
            responsecode_unsuccess('Pakistan', 'Responsecode', page.ok)
        soup = BeautifulSoup(page.content, "html.parser")
        # print(soup)
        myDict = dict()
        vallist = []
        keylist = []
        links = soup.find_all('a')
        inc = 0
        for i in links:
            string_extr = i['href']
            # print(string_extr)
            match = re.search(r'b_securite+/|b_securite+/\w+', string_extr)
            if match:
                inc += 1
                # print(match)
            else:
                s = ''

        # print(inc)
        # print("am the length",len(links))
        # print(links.text)
        for link in links:
            # print(link)
            textfile = link['href']
            if ".txt" in textfile:
                try:
                    data = str(textfile)
                    # page1=proxy.Proxy_Request(url=domain + data,request_type='get',verify=False)
                    page1 = requests.get(domain + data, verify=False)
                    soup1 = BeautifulSoup(page1.content, "html.parser")
                    srt = data.split("/", 3)[-1].split()[0:]
                    s2 = ' '.join(srt)
                    # print(data)

                    keylist.append(s2)
                    vallist.append(soup1)
                except Exception as e:
                    print("Error:", e)
                    responsecode_unsuccess('Pakistan','Browser error',e)
                # print(s2)
                # print(soup)

        res = {}
        for key in keylist:
            for value in vallist:
                try:
                    res[key] = value
                    # print(value)
                    vallist.remove(value)
                    break
                except Exception as e:
                    print("Error:", e)
                    datavalidation_Unsucess('Pakistan','Values Error',e)

        if (inc == len(res)):
            datavalidation_sucess('Pakistan', 'Rows In The Main Page', str(inc))

            # print("Sucessfully all rows are validated sucessfully")
        else:
            datavalidation_Unsucess('Pakistan', 'Rows In The Main Page', str(inc))

        print(res)
    except Exception as e:
        datavalidation_Unsucess('Pakistan','Error Occured',e)
    #f.close()
def peru():
    try:
        url = "https://www.dhn.mil.pe/radioavisos"
        # browser = webdriver.Chrome("D:\Projects\webscrap\chromedriver\chromedriver.exe")
        browser = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        browser.get(url)
        ids = browser.find_elements_by_xpath('//*[@id="accordion"]/div/div/h4/a')
        lissp = []
        for i in ids:
            try:

                href = i.get_attribute('href')
                # print(href)
                hreflis = str(href).split('#')
                stt = str(hreflis[1])
                lissp.append(stt)
            except Exception as e:
                print("error found", e)
                responsecode_unsuccess('Peru','ItemsMissing',e)
    # print(lissp)
        try:
            domain = "https://www.dhn.mil.pe/radioavisos"
            page = requests.get("https://www.dhn.mil.pe/radioavisos")
            # page = requests.get("https://www.paknavy.gov.pk/hydro/b_securite/20190329SEC%20096%20.txt")
            soup = BeautifulSoup(page.content, "html.parser")
            data = soup.find("div", class_="panel-group")
            target = data.find("div", class_="panel-body").find_all(text=True, recursive=False)
            # print("leangth",len(target))
        except Exception as e:
            print("No element found error", e)
        vallist = []
        keylist = []
        for i in lissp:
            dt = soup.find("div", id=i)
            ress = str(dt.text)
            vallist.append(ress)

        try:
            spp = soup.find_all("h4", class_="panel-title")
            scrapedheaderslen = len(spp)
            cars = soup.find_all('h4', attrs={'class': 'panel-title'})
            for tag in cars:
                i = str(tag.text.strip())
                keylist.append(i)
            # print(i)
            # print(tag.text.strip())
            res = {}
            for key in keylist:
                for value in vallist:
                    res[key] = value
                    vallist.remove(value)
                    break
            responsecode = requests.get(url)
            if (responsecode.ok):
                responsecode_success('Peru', 'Responsecode', responsecode.status_code)
            else:
                responsecode_unsuccess('Peru', 'Responsecode', responsecode.status_code)
        except Exception as e:
            print("error found", e)
            browser.close()
        print(res)

        if (scrapedheaderslen == len(res)):
            datavalidation_sucess('Peru','Key Elements Indices length',str(scrapedheaderslen))

        else:
            datavalidation_Unsucess('Peru','Key Elements Indices length',str(scrapedheaderslen))


        browser.close()
    except Exception as e:
        datavalidation_Unsucess('Peru','Error Occured',e)
    #end = time.time()
    #f.close()
def south_africa():
    url = "http://www.sanho.co.za/notices_mariners/navarea_v11_messages.htm"
    # url="http://www.sanho.co.za/notices_mariners/navarea_v11_messages.htm?b2=NAVAREA+VII"
    browser = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    # browser = webdriver.Chrome("D:\Projects\webscrap\chromedriver\chromedriver.exe")
    browser.get(url)
    responsecode = requests.get(url)
    if (responsecode.ok):
        responsecode_success('SouthAfrica', 'Responsecode', responsecode.status_code)
    else:
        responsecode_unsuccess('SouthAfrica', 'Responsecode', responsecode.status_code)
    try:
        a = browser.find_elements_by_class_name("content")
        rss = []
        j = 0
        res = browser.find_elements_by_xpath("/html/body/div/p")
        res1 = browser.find_elements_by_xpath("/html/body/div/p")

        patterens = ["CANCEL THIS MESSAGE", "Nil Prior to these Messages", "UNTIL FURTHER NOTICE"]
        s2 = ""
        s3 = ''
        splitted = ''
        l = []
        for k in res1:
            l.append(k.text)
        for i in a:
            s2 = ""
            strres = str(i.text)
            l1 = strres.split("Nil Prior to these Messages")[1:]
    except Exception as e:
        print("Browser content not Found")
        responsecode_unsuccess('SouthAfrica','ElementNotFoundIn browser',e)
    res = []
    res1 = []
    resstr = ""
    for sub in l:
        res.append(re.sub(r'\n', '$', sub))
    resstr = str(res[0])
    reslis = list(resstr)
    indexlist = []
    try:

        for i in range(len(reslis) - 1):
            if (i == 0):
                i += 1
            elif (reslis[i] == reslis[i + 1]):
                if (reslis[i] == str("$") and reslis[i + 1] == str("$")):
                    indexlist.append(i)
            i += 1
        parts = [resstr[i:j] for i, j in zip(indexlist, indexlist[1:] + [None])]
    except:
        print("Indexes Are Giving Error")
    eachpart = []
    vallist = []
    keylist = []
    try:

        for i in parts:
            splite = i.split('$')
            eachpart.append(splite)
        # print(i)
        # print(eachpart)
        for i in eachpart:
            i = list(filter(None, i))
            # print(i)
            if (i == []):
                strere = ""
            # print("empty")
            else:
                sds = i[0]
                keylist.append(sds)
                vallist.append(i)
        res = {}
        for key in keylist:
            for value in vallist:
                string1 = ''.join(value)
                res[key] = string1
                vallist.remove(value)
                break
        print(res)

        scrapedelem = []
        expected_string = "NAVAREA VII 226 OF 2020: (15 OCT 20)"
        char_removed_string = ''.join(char for char in expected_string if char.isalnum())
        expected_string_len = len(char_removed_string)
        for k in keylist:
            scra_stri = k
            scraped_string = ''.join(char for char in scra_stri if char.isalnum())
            scraped_strlen = len(scraped_string)
            if (expected_string_len == scraped_strlen):
                #print("Validated Succesfull Key")
                scrapedelem.append(k)
                datavalidation_sucess('SouthAfrica','ScrapedStringLength',str(scraped_string))
            else:
                if (k.__contains__("Series")):
                    print("accept")
                else:
                    s=''
                    #datavalidation_Unsucess('SouthAfrica','Length of Key','scra_stri')


        #if (len(scrapedelem) == len(res)):
            #datavalidation_sucess('SouthAfrica','TotalKeys',str(len(scrapedelem)))

        #else:
            #datavalidation_Unsucess('SouthAfrica','TotalKeys',str(len(scrapedelem)))

        #f.close()
        browser.close()
    except Exception as e:
        print("Expected Schema Is not Arranaged")
        datavalidation_Unsucess('SouthAfrica','ErrorFound',e)
        browser.close()
def Spain():
    try:
        #start = time.time()
        #now = datetime.now()
        #f = open("log.txt", "a+")
        url = "https://armada.defensa.gob.es/ihm/Aplicaciones/Navareas/Index_Navareas_xml_en.html"
        browser = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        browser.get(url)
        s1 = browser.find_element_by_name('listado_length').text
        srr = str(s1)
        ressr = str(srr[8:])
        select = Select(browser.find_element_by_name('listado_length'))
        select.select_by_index(3)
        # logging.basicConfig(filename=LOG_FILENAME, format='%(levelname)s %(asctime)s :: %(message)s', level=logging.DEBUG)
    except Exception as e:
        # print("browser not found element")
        datavalidation_Unsucess('Spain','BrowserElement',e)

        browser.close()
        #f.close()
    urllib3.disable_warnings()
    urls = []
    res = []
    vallist = []
    keylist = []
    try:
        ids = browser.find_elements_by_xpath('//*[@href]')
        button = browser.find_element_by_id("btn_todos")
        button.click()
        wait = WebDriverWait(browser, 10)
        text_allitems = browser.find_element_by_xpath('//*[ @ id = "divResultado"]/ h3/kbd/b')
        sourcelegnthoftb = text_allitems.text
        print(sourcelegnthoftb)
        element = browser.find_elements_by_class_name("impresion")
        html_source = browser.page_source
        soup = BeautifulSoup(html_source, 'html.parser')
        t = soup.find_all('span', {'class': 'impresion'})
        for i in t:
            res2 = i.get_text()
            vallist.append(res2)
        for id in ids:
            href = id.get_attribute('href')
            oncc = id.get_attribute('onclick')
            ress = str(oncc)
            er = ress.split("Mostrar_Nav")
            ser = er[-1].split(',')
            ser1 = str(ser[-1]).strip(')')
            replacedstrin = "NAVAREA III " + ser1.replace("'", '')
            # print('Ser',replacedstrin)
            if (ser1 == "None"):
                ss = ""
                # print("am in none ")
            else:
                keylist.append(replacedstrin)
                # print(ser1)

    except Exception as e:
        print("Body of the content is not Identified")
        browser.close()
        responsecode_unsuccess('Spain','Body Of elements Missing',e)
    responsecode = requests.get(url)

    # logging.basicConfig(filename=LOG_FILENAME,format='%(levelname)s %(asctime)s :: %(message)s',level=logging.DEBUG)
    # logging.info(tes)
    # logging.warning('This is The warning')
    # logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    # logging.debug(tes2)
    try:
        if (responsecode.ok):
            responsecode_success('Spain', 'Responsecode', responsecode.status_code)



        else:
            responsecode_unsuccess('Spain', 'Responsecode', responsecode.status_code)
            browser.close()
        res = {}
        for key in keylist:
            try:
                for value in vallist:
                    res[key] = value
                    vallist.remove(value)
                    break
            except Exception as e:
                print("Key value elements not formed")
                datavalidation_Unsucess('Spain','Values Not formatted',e)
                browser.close()
        scrappedlen_key = str(len(res))

        finalscrapstr = "(" + scrappedlen_key + " items" + ")"
        print(finalscrapstr)

        if (finalscrapstr == sourcelegnthoftb):
            datavalidation_sucess('Spain','TableData', finalscrapstr)

        # f.write("\nAll table rows are validated sucessfully %s" %finalscrapstr )
        else:
            datavalidation_Unsucess('Spain','TableData', finalscrapstr)

        # f.write("\n")
        # f.write("\nAll table rows are not matched please check key %s" % str(i))

        browser.close()
        #f.close()
        print(res)
    except Exception as e:
        datavalidation_Unsucess('Spain','ErrorFound',e)

def usa_iv():
    url = "https://msi.nga.mil/api/publications/download?type=view&key=16694640/SFH00000/DailyMemIV.txt"
    browser = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    browser.get(url)
    try:

        a = browser.find_elements_by_xpath("/html/body/pre")
        indexlist = []
        length_mainwebsitekeys = 0
        for i in a:
            set = str(i.text)
            # match = re.findall(r'NAVAREA IV+ \w+/\w+', set)
            # length_mainwebsitekeys=len(match)
            # print("matches in main string",match)
            # print([set])
            keylis = set.partition('\n')[0]
            vaallis = set.partition('\n')[0:]

        reslis = list(set)
        resstr = str(set)
        for i in range(len(reslis) - 1):
            if (i == 0):
                i += 1
            elif (reslis[i] == reslis[i + 1]):
                if (reslis[i] == str('\n') and reslis[i + 1] == str('\n')):
                    # print("am in loop ",i,reslis[i])
                    indexlist.append(i)

                # newst=.join(reslis)
        i += 1
        parts = [resstr[i:j] for i, j in zip(indexlist, indexlist[1:] + [None])]
        keylist = []
        vallist = []
        for i in parts:
            k = i.partition('.\n')[0]
            keylist.append(k)
            v = i.partition('\n')[2]
            doc = v.replace('\n', ' ')
            vallist.append(doc)

        # print(k)
        # print(v)
        keylist.pop(0)
        vallist.pop(0)
        res = {}
        responsecode = requests.get(url)
        if (responsecode.ok):
            responsecode_success('USA-IV', 'Responsecode', responsecode.status_code)
            # print("Sucessfull", responsecode.status_code)
        else:
            responsecode_unsuccess('USA-IV', 'Responsecode', responsecode.status_code)
        for key in keylist:
            match = re.search(r'NAVAREA IV+ \w+/\w+', key)
            if match:
                datavalidation_sucess('USA-IV','Match Patteren of Key',key)

                for value in vallist:
                    res[key] = value
                    vallist.remove(value)
                    break
            else:
                datavalidation_Unsucess('USA-IV','Match Patteren of Key',key)

        # val = list(res.keys())[0]
        # res.pop(val)

        print(res)


        # if(length_mainwebsitekeys==len(res)):
        # print("Keys are Sucessfully Validated with the source website")
        # else:
        # print("please check the keys")
        browser.close()
    except Exception as e:
        print("Expected Schema Is not formed ")
        datavalidation_Unsucess('USA-IV','Error Found',e)
        browser.close()
    #end = time.time()
    #f.close()
def usa_xii():


    url = "https://msi.nga.mil/api/publications/download?type=view&key=16694640/SFH00000/DailyMemXII.txt"
    # https://msi.nga.mil/api/publications/download?type=view&key=16694640/SFH00000/DailyMemIV.txt
    browser = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    # browser = webdriver.Chrome("D:\Projects\webscrap\chromedriver\chromedriver.exe")
    browser.get(url)
    responsecode = requests.get(url)
    if (responsecode.ok):
        responsecode_success('USA-XII', 'Responsecode', responsecode.status_code)
    else:
        responsecode_unsuccess('USA-XII', 'Responsecode', responsecode.status_code)

    try:

        a = browser.find_elements_by_xpath("/html/body/pre")
        indexlist = []

        for i in a:
            set = str(i.text)

            keylis = set.partition('\n')[0]
            vaallis = set.partition('\n')[0:]
            # print(keylis)
            # print(vaallis)
        reslis = list(set)
        resstr = str(set)
        for i in range(len(reslis) - 1):
            if (i == 0):
                i += 1
            elif (reslis[i] == reslis[i + 1]):
                if (reslis[i] == str('\n') and reslis[i + 1] == str('\n')):
                    # print("am in loop ",i,reslis[i])
                    indexlist.append(i)

                    # newst=.join(reslis)
        i += 1

        parts = [resstr[i:j] for i, j in zip(indexlist, indexlist[1:] + [None])]
        keylist = []
        vallist = []
        for i in parts:
            k = i.partition('.\n')[0]
            keylist.append(k)
            v = i.partition('\n')[2]
            doc = v.replace('\n', ' ')
            vallist.append(doc)
        keylist.pop(0)
        vallist.pop(0)
        # print(k)
        # print(v)

        res = {}
        for key in keylist:
            match = re.search(r'NAVAREA XII+ \w+/\w+', key)
            if match:
                datavalidation_sucess('USA-XII','Match Patteren of Key',key)
                # match = re.search(r'NAVAREA IV+ \w+/\w+', key)
                # if match:

                for value in vallist:
                    res[key] = value
                    vallist.remove(value)
                    break
            else:
                datavalidation_Unsucess('USA-XII', 'Match Patteren of Key', key)

        # val = list(res.keys())[0]
        # res.pop(val)

        print(res)
    except Exception as e:
        print("expected format is not performed")
        datavalidation_Unsucess('USA-XII','ErrorFound',e)
        browser.close()
    # res.pop(val)
    # del res[0]
    # print(res)

    # print(b)
    # print(res)
    # print(parts[2])
    browser.close()
    #end = time.time()
    #f.close()


def India():
    #f.close()
    try:
        f = open("log_allscrip.txt", "a+")
        page = requests.get("https://hydrobharat.gov.in/navarea-warnings/")
        if (page.ok):
            responsecode_success('India', 'MainResponsecode', page.status_code)
            # print("Sucessfull", page.status_code)
        else:
            responsecode_unsuccess('India', 'MainResponsecode', page.status_code)
        # print("Unsucessfull", page.status_code)

        soup = BeautifulSoup(page.content, "html.parser")
        links = soup.find_all("a")

        for link in links:
            try:
                if "pdf" in link['href']:
                    # print(link['href'])
                    pdf_url = ""
                    if "http" not in link['href']:
                        pdf_url = 'https://hydrobharat.gov.in/navarea-warnings' + link['href']
                    # print(pdf_url)
                    else:
                        pdf_url = link['href']

                    pdf_response = requests.get(pdf_url)
                    # responsecode = requests.get(url)
                    if (pdf_response.ok):
                        responsecode_success('India', 'PdfFileResponse', page.status_code)
                    else:
                        responsecode_unsuccess('India', 'PdfFileResponse', page.status_code)
                    # print("Unsucessfull", pdf_response.status_code)
                    filename = unquote(pdf_response.url).split('/')[-1]
                    # print(filename)
                    with open('./pdf_' + filename, 'wb') as fd:
                        fd.write(pdf_response.content)
            except Exception as e:
                print("Error:", e)
                datavalidation_Unsucess('India','PdfReadingError',e)

        pdfFileObject = open(r"C:\Users\nanip\PycharmProjects\Navarea_Scripts3\venv\Scripts\pdf_navarea_warnings_in_force.pdf",
                         'rb')
        bad_chars = ['-', '-',
                 '-------------------------------------------------------------------------------------------------------------------------------------']

        pdflis = []
        pdflis1 = []
        pdfpagestringlist = []
        total_pages_string = ""
        with pdfplumber.open(pdfFileObject) as pdf:
            try:

                first_page = pdf.pages
                for i in first_page:
                    sss = str(i.extract_text())
                    pgstr = ''.join([i for i in sss if i.isalnum()])
                    total_pages_string += sss
                    pdfpagestringlist.append(pgstr)
                    dtg_index = [m.start() for m in re.finditer('DTG', sss)]
                    indexlist1 = [m.start() for m in re.finditer('FROM   N', sss)]
                    parts = [sss[i:j] for i, j in zip(indexlist1, indexlist1[1:] + [None])]
                    parts1 = [sss[i:j] for i, j in zip(dtg_index, dtg_index[1:] + [None])]
                    pdflis.append(parts)
                    pdflis1.append(parts1)
            except Exception as e:
                print("Item Not Found", e)
                datavalidation_Unsucess('India','ItemNotfound',e)
    # print(total_pages_string)
    #f.close()
        to_remove = [
            '\n------------------------------------------------------------------------------------------------------------------------------------- \n',
            '\n-------------------------------------------------------------------------------------------------------------------------------------- \n',
            '\n--------------------------------------------------------------------------------------------------------------------------------------  \n',
            '\n-------------------------------------------------------------------------------------------------------------------------------------    \n',
            '\n-------------------------------------------------------------------------------------------------------------------------------------   \n',
            '\n-------------------------------------------------------------------------------------------------------------------------------------    \n',
            '\n------------------------------------------------------------------------------------------------------------------------------------ \n',
            '\n-------------------------------------------------------------------------------------------------------------------------------------  \n',
            '\n-------------------------------------------------------------------------------------------------------------------------------------  \n',
            '\n-------------------------------------------------------------------------------------------------------------------------------------\n',
            '\n-------------------------------------------------------------------------------------------------------------------------------------\n',
            '\n------------------------------------------------------------------------------------------------------------------------------------   \n',
            '\n-------------------------------------------------------------------------------------------------------------------------------------     \n',
            '\n ------------------------------------------------------------------------------------------------------------------------------------- \n']
        try:

            dtg_index_totalstring = [m.start() for m in re.finditer('DTG', total_pages_string)]
            index_dtg_len = len(dtg_index_totalstring)
            parts_pages = [total_pages_string[i:j] for i, j in
                        zip(dtg_index_totalstring, dtg_index_totalstring[1:] + [None])]
            p = re.compile('|'.join(map(re.escape, to_remove)))  # escape to handle metachars
            stroe = [p.sub('#', s) for s in parts_pages]
            # print(stroe)
            vallist = []
            for i in stroe:
                string_i = str(i).strip('#')
                valstring = string_i.split('#')[1]
                vallist.append(valstring)
        except Exception as e:
            print("Pages String Not Arranged", e)
            datavalidation_Unsucess('India','PagesStringNotArrange',e)

    # print("am the length ofVal:",len(vallist))
        finalstrlis1 = []
        monthlis = []
        exctractedlist = []
        for i in pdflis1:
            for j in i:
                try:
                    tempstr = str(j)
                    setstr = ''.join([i for i in tempstr if i.isalnum()])
                    extractedstring = setstr[0:57]
                    exctractedlist.append(extractedstring)
                    navreastr = setstr[39:42]
                    monthstr = setstr[10:15]
                    timezonstr = setstr[3:10]
                    resstr = monthstr + "-" + timezonstr
                    monthlis.append(resstr)
                    finalstrlis1.append(tempstr)
                except Exception as e:
                    print("String Slicing Not Done", e)
                    datavalidation_Unsucess('India','StringSlicingNotDone',e)

        finalstrlis = []
        navlist = []
        for i in pdflis:
            for j in i:
                try:

                    tempstr = str(j)
                    setstr = ''.join([i for i in tempstr if i.isalnum()])
                    navreastr = setstr[39:42]
                    monthstr = setstr[10:15]
                    resstr = navreastr
                    navlist.append(resstr)
                    finalstrlis.append(tempstr)
                except Exception as e:
                    print("Slicing for Navaraea Stirng Not done", e)
                    datavalidation_Unsucess('India','SlicingForNavareaNotdone',e)

        keylist = ["NAVAREA VIII - " + m + "/" + str(n) for m, n in zip(navlist, monthlis)]
        res = {}
        for key in keylist:
            for value in vallist:
                try:
                    res[key] = value
                    vallist.remove(value)
                    break
                except Exception as e:
                    print("Expected Schema Not Perfomrmed", e)
                    datavalidation_Unsucess('India','ErrorFound',e)
    #f = open("log.txt", "a+")
        if (len(res) == index_dtg_len):
            datavalidation_sucess('India','DTG Count In The Pdf',str(index_dtg_len))

            # print("Validated Sucessfuly with the dtg index")
        else:
            datavalidation_Unsucess('India', 'DTG Count In The Pdf', str(index_dtg_len))

        f.close()
        print(res)
    except Exception as e:
        datavalidation_Unsucess('India','ErrorFound',e)
uk_country()
argentina()
Austrelia()
Brazil()
India()
canadaXVII()
canadaxviii()
chilie()
France()

Japan()
Norway()
NewZelanad()
Pakistan()
peru()
south_africa()
Spain()
usa_iv()
usa_xii()

end = time.time()
seconds=end-start
f.close()
print(f"Runtime of the program is",convert(seconds))