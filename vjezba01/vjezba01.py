import socket, time, re

def connect_to_server(ip, port, retry = 10):
    s = socket.socket()
    try:
        s.connect((ip, port))
    except Exception as e:
        print(e)
        if retry > 0:
            time.sleep(1)
            retry -=1
            connect_to_server(ip, port, retry)       

    return s

def get_source(s, ip, page):

    CRLF = '\r\n'
    get = 'GET /' + page + ' HTTP/1.1' + CRLF
    get += 'Host: '
    get += ip
    get += CRLF
    get += CRLF

    print(get)
    s.send(get.encode('utf-8'))
    response = s.recv(10000000).decode('latin-1')
    return response

def get_links(response):
    beg = 0
    while True:

        if len(links) >= 50:
            break

        beg_str = response.find('href="', beg)   
        if beg_str == -1:
            return links
        
        end_str = response.find('"', beg_str + 6)      
        link = response[beg_str + 6:end_str]
    

        if link[-4:] == "html" and link not in links:
            links.append(link)

        beg = end_str + 1
  

def get_the_rest():
    for check_links in links[1:]:
        print(check_links, "provjera")
        s = connect_to_server(ip,port)
        response = get_source(s,ip,check_links)
        print(get_links(response), "getano")


ip = 'www.optimazadar.hr'
port = 80
page = '1280/djelatnost1280.html'
links = [page]

s = connect_to_server(ip, port)
response = get_source(s, ip, page)
print(get_links(response))
print("novo")
get_the_rest()
print(links)

s.close()
