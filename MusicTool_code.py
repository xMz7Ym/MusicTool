import requests
import re
import json
import base64
import binascii
import random
import string
from urllib import parse
from Crypto.Cipher import AES
import os
# 歌曲url解析出id
songURL = lambda x:re.findall('\/song\?id=(\d+)',x)[0]




# 歌单url解析出id
playlistURL = lambda x:re.findall('\/playlist\?id=(\d+)',x)[0]




# 根据歌单id 解析出歌曲id与歌曲名 分为两个列表为Id与Name
def palylistInfo(id):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/84.0.4147.89 "
                      "Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
    }

    url = "https://music.163.com/playlist?id=" + str(id)
    rs = requests.get(url=url ,headers=headers)
    Id = re.findall("/song\?id=(\d*)\"",rs.text)
    Name =re.findall("(?:a href=\")/song\?id=(?:\d+)\">([^<].*?)[<]",rs.text)
    return Id,Name


# 根据歌曲id找到歌曲的名字
def idToname(id):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/84.0.4147.89 "
                      "Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
    }

    url = "https://y.music.163.com/m/song?id=" + str(id)
    r2 = requests.get(url=url, headers=headers)
    Name = re.findall("\"description\": \"歌曲名《(.*?)》.*由(.+)演唱", r2.text)[0]
    return str(Name[0])+'——'+str(Name[1]).strip()



# 以下均为根据名字找到id


# 一个专属的模块
def _LyricDownload2(id,name,LU):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/84.0.4147.89 "
                      "Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
    }

    url = "https://music.163.com/api/song/media?id=" + str(id)
    r3 = requests.get(url=url, headers=headers).text
    r = json.loads(r3)
    Yric = str(r["lyric"])

    with open(f'{LU}/{name}.lrc', 'w') as f:
        f.write(Yric)

# 从a-z,A-Z,0-9中随机获取16位字符
def get_random():
    random_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    return random_str


# AES加密要求加密的文本长度必须是16的倍数，密钥的长度固定只能为16,24或32位，因此我们采取统一转换为16位的方法
def len_change(text):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    text = text.encode("utf-8")
    return text


# AES加密方法
def aes(text, key):
    # 首先对加密的内容进行位数补全，然后使用 CBC 模式进行加密
    iv = b'0102030405060708'
    text = len_change(text)
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(text)
    encrypt = base64.b64encode(encrypted).decode()
    return encrypt


# js中的 b 函数，调用两次 AES 加密
# text 为需要加密的文本， str 为生成的16位随机数
def b(text, str):
    first_data = aes(text, '0CoJUm6Qyw8W8jud')
    second_data = aes(first_data, str)
    return second_data


def c(text):
    e = '010001'
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    text = text[::-1]
    result = pow(int(binascii.hexlify(text.encode()), 16), int(e, 16), int(f, 16))
    return format(result, 'x').zfill(131)


# 获取最终的参数 params 和 encSecKey 的方法
def get_final_param(text, str):
    params = b(text, str)
    encSecKey = c(str)
    return {'params': params, 'encSecKey': encSecKey}


# 通过参数获取搜索歌曲的列表
def get_music_list(params, encSecKey):
    url = "https://music.163.com/weapi/cloudsearch/get/web?csrf_token="

    payload = 'params=' + parse.quote(params) + '&encSecKey=' + parse.quote(encSecKey)
    headers = {
        'authority': 'music.163.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'origin': 'https://music.163.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://music.163.com/search/',
        'accept-language': 'zh-CN,zh;q=0.9',
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text



def nameToOneid(song_name):
    d = {"hlpretag": "<span class=\"s-fc7\">", "hlposttag": "</span>", "s": song_name, "type": "1", "offset": "0",
         "total": "true", "limit": "30", "csrf_token": ""}
    d = json.dumps(d)
    random_param = get_random()
    param = get_final_param(d, random_param)
    song_list = get_music_list(param['params'], param['encSecKey'])
    music_info = json.loads(song_list)['result']['songs']
    for i in range(len(music_info)):
        if music_info[i]["ar"][0]["name"] in song_name:
            return music_info[i]["id"]
    else :
        return music_info[1]["id"]
def nameToAllid(song_name):
    d = {"hlpretag": "<span class=\"s-fc7\">", "hlposttag": "</span>", "s": song_name, "type": "1", "offset": "0",
         "total": "true", "limit": "30", "csrf_token": ""}
    d = json.dumps(d)
    random_param = get_random()
    param = get_final_param(d, random_param)
    song_list = get_music_list(param['params'], param['encSecKey'])
    music_info = json.loads(song_list)['result']['songs']
    name = []
    id = []
    f = '-'
    for i in range(min(len(music_info),10)):
        b = music_info[i]["ar"][0]["name"]
        c = music_info[i]["name"]
        e = music_info[i]["id"]
        name.append(b+f+c)
        id.append(e)
    return id, name


#  歌曲下载模块
def musicDownload(name=None,id=None,switch=True):
    if switch !=True:
        pass
    else:
        if name == None and id ==None:
            return 'error'
        elif name == None:
            name = idToname(id)
        elif id ==None:
            id = nameToOneid(name)
        else:
            pass
        os.makedirs('./Download', exist_ok=True)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/84.0.4147.89 "
                          "Safari/537.36",
            "Accept-Encoding": "gzip, deflate",
        }

        url = f"http://music.163.com/song/media/outer/url?id={id}.mp3"
        dname=idToname(id)
        r1 = requests.get(url=url, headers=headers).content
        with open(f'./Download/{dname}.mp3', 'wb') as f:
            f.write(r1)


# 歌词下载模块
def lyricDownload(name=None,id=None,switch=True):
    if switch !=True:
        pass
    else:
        if name == None and id ==None:
            return 'error'
        elif name == None:
            return 'error'
        elif id ==None:
            id = nameToOneid(name)
        else:
            pass
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/84.0.4147.89 "
                          "Safari/537.36",
            "Accept-Encoding": "gzip, deflate",
        }

        url = "https://music.163.com/api/song/media?id=" + str(id)
        r3 = requests.get(url=url, headers=headers).text
        r = json.loads(r3)
        Yric = str(r["lyric"])
        with open(f'./Download/{name}.lrc', 'w') as f:
            f.write(Yric)
