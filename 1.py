from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import re, time
import random
import socket
def writeFileUrlStr(urls):
    print(urls)
    bdurl = 'https://www.baidu.com/s?wd=site%3A'
    url = bdurl+urls
    # time.sleep(1)
    agnetsList = ["User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"]
    agnetStr = random.choice(agnetsList)
    req = urllib.request.Request(url)
    req.add_header("User-Agent", agnetStr)
    responses = urllib.request.urlopen(req).read().decode()
    soup = BeautifulSoup(responses, features='lxml')
    txt = soup.find_all('h3', {'class': 't'})
    if txt == []:
        return
    if re.findall('娱乐', str(txt)):
        return
    elif re.findall('平台', str(txt)):
        return
    elif re.findall('注册', str(txt)):
        return
    elif re.findall('国际', str(txt)):
        return
    elif re.findall('澳门', str(txt)):
        return
    elif re.findall('威尼斯', str(txt)):
        return
    elif re.findall('在线', str(txt)):
        return
    elif re.findall('体育', str(txt)):
        return
    elif re.findall('看片', str(txt)):
        return
    elif re.findall('视频', str(txt)):
        return
    elif re.findall('pk10', str(txt)):
        return
    elif re.findall('PK10', str(txt)):
        return
    elif re.findall('游戏', str(txt)):
        return
    elif re.findall('万博', str(txt)):
        return
    elif re.findall('果博', str(txt)):
        return
    elif re.findall('开奖', str(txt)):
        return
    elif re.findall('开码', str(txt)):
        return
    elif re.findall('滚球', str(txt)):
        return
    elif re.findall('老虎机', str(txt)):
        return
    elif re.findall('彩票', str(txt)):
        return
    elif re.findall('时时彩', str(txt)):
        return
    elif re.findall('医院', str(txt)):
        return
    elif re.findall('官网', str(txt)):
        return
    elif re.findall('啪啪', str(txt)):
        return
    elif re.findall('申博', str(txt)):
        return
    elif re.findall('申搏', str(txt)):
        return
    elif re.search('腾博', str(txt)):
        return
    elif re.findall('伦理', str(txt)):
        return
    elif re.findall('六合', str(txt)):
        return
    elif re.findall('皇冠', str(txt)):
        return
    elif re.findall('熟女', str(txt)):
        return
    elif re.findall('做爱', str(txt)):
        return
    elif re.findall('直播', str(txt)):
        return
    elif re.findall('成人', str(txt)):
        return
    elif re.findall('偷偷', str(txt)):
        return
    elif re.findall('种子', str(txt)):
        return
    elif re.findall('乱伦', str(txt)):
        return
    elif re.findall('无码', str(txt)):
        return
    elif re.findall('少女', str(txt)):
        return
    elif re.findall('德赢', str(txt)):
        return
    elif re.findall('骚女', str(txt)):
        return
    elif re.findall('永利', str(txt)):
        return
    elif re.findall('赌球', str(txt)):
        return
    elif re.findall('番号', str(txt)):
        return
    elif re.findall('北京赛车', str(txt)):
        return
    else:
        for i in txt:
            txt = i.get_text()
            if re.findall('www', str(txt)):
                return
            elif re.findall('com', str(txt)):
                return
            elif re.findall('Domain', str(txt)):
                return
            elif re.findall('net', str(txt)):
                return
            elif re.findall('AG', str(txt)):
                return
            else:
                toPath = r"D:\domain\domain\domain.txt"
                with open(toPath, "a") as f:
                    print(urls)
                    f.write(str(urls))
                    break
if __name__ == "__main__":
    file = open(r"D:\domain\domain\domaintest1.txt")
    #hostname = socket.gethostname()
    #ip = socket.gethostbyname(hostname)
    #if ip == "10.60.224.14":
    with file as f:
        for line in f.readlines():
            writeFileUrlStr(line)
    #else:
       # print("The current IP cannot be used ！！！ Please contact the administrator.")

