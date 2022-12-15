import urllib.parse, urllib.request, urllib.error, json
from flask import Flask, render_template, request
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
import datetime
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

# riot_key can be freely generated at https://developer.riotgames.com/ after signing up a Riot Developer Account
import riot_key as riot_key
def get_champ(baseurl = "https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/",
              summonerID = "F3H7VpNLNxtcvTBHL35OMSIHtUtRxVO-MSMqjin59y0ssXkGi9OHqb6Biw",
              api_key = riot_key.key):
    url = baseurl + str(summonerID) + "?api_key=" + api_key
    page = urllib.request.urlopen(url, context=ctx)
    mypage = page.read().decode("utf-8")
    jsonFile = json.loads(mypage)
    return(jsonFile)

def get_id(baseurl = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/",
           summonerName = "REDDDSH",
            api_key = riot_key.key):
    summonerName = summonerName.replace(" ", "%20")
    print(summonerName)
    url = baseurl + summonerName + "?api_key=" + api_key
    print(url)
    page = urllib.request.urlopen(url, context=ctx)
    mypage = page.read().decode("utf-8")
    jsonFile = json.loads(mypage)
    summonerID = jsonFile.get("id")
    return summonerID

def safe_get_id(summonerName = "REDDDSH"):
    try:
        return get_id(summonerName = summonerName)
    except:
        print("There was an error with this request")
        return None

def safe_get_champ(summonerID = None):
    try:
        return get_champ(summonerID = summonerID)
    except urllib.error.URLError as e:
        print("There was an error with this request", e)
        return None
    except urllib.error.HTTPError as e:
        print("There was an error with this request", e)
        return None

def print_pretty_file(jsonFile):
    print(pretty(jsonFile))
# get_champ()

# friend_id_list = ["NHLpIG3EdtyXTgyD_Tum6HEWpkX5ql1pxe8NWYb5drsfW572_3-lq9CuyQ", "F3H7VpNLNxtcvTBHL35OMSIHtUtRxVO-MSMqjin59y0ssXkGi9OHqb6Biw", "HtJB6MOOQ3XyyHfeLmrkmEzFdnA5A-VSbkaPA0yQJBgqwhhzhmXqT-e-jA", "MXgnRSWy3yRj_n-JJ0vfp667KT1cvABnj2bL2hByuS3L_GE", "mBKdILxxHg40MPNCHiadBkhC6_fTQeby4mtUm6SLFHafLAs", "foMiS-v6Fhqx_qHguRd2Ec48Ua3XYclsbb3uA_iqflk2nDl1KnUz7JcBkg"]
# friend_list = ["AidenlIi", "HandsomeZHD", "REDDDSH"]
# for id in friend_list:
#     print_pretty_file()
# print_pretty_file(safe_get_champ(safe_get_id("Necora Nyaru")))

# def get_champ_name(champ_dic):
#     champ_dic = safe_get_champ(safe_get_id("REDDDSH"))

champ_namedic = {'266': 'Aatrox','103': 'Ahri','84': 'Akali','166': 'Akshan','12': 'Alistar','32': 'Amumu','34': 'Anivia',
                '1': 'Annie','523': 'Aphelios','22': 'Ashe','136': 'AurelionSol','268': 'Azir','432': 'Bard','53': 'Blitzcrank','63': 'Brand','201': 'Braum',
                '51': 'Caitlyn','164': 'Camille','69': 'Cassiopeia','31': 'Chogath','42': 'Corki','122': 'Darius','131': 'Diana',
                '119': 'Draven','36': 'DrMundo','245': 'Ekko','60': 'Elise','28': 'Evelynn','81': 'Ezreal','9': 'Fiddlesticks',
                '114': 'Fiora','105': 'Fizz','3': 'Galio','41': 'Gangplank','86': 'Garen','150': 'Gnar','79': 'Gragas','104': 'Graves',
                '887': 'Gwen','120': 'Hecarim','74': 'Heimerdinger','420': 'Illaoi','39': 'Irelia','427': 'Ivern','40': 'Janna',
                '59': 'JarvanIV','24': 'Jax','126': 'Jayce','202': 'Jhin','222': 'Jinx','145': 'Kaisa','429': 'Kalista','43': 'Karma',
                '30': 'Karthus','38': 'Kassadin','55': 'Katarina','10': 'Kayle','141': 'Kayn','85': 'Kennen','121': 'Khazix',
                '203': 'Kindred','240': 'Kled','96': 'KogMaw','7': 'Leblanc','64': 'LeeSin','89': 'Leona','876': 'Lillia','127': 'Lissandra',
                '236': 'Lucian','117': 'Lulu','99': 'Lux','54': 'Malphite','90': 'Malzahar','57': 'Maokai','11': 'MasterYi','21': 'MissFortune',
                '62': 'MonkeyKing','82': 'Mordekaiser','25': 'Morgana','267': 'Nami','75': 'Nasus','111': 'Nautilus','518': 'Neeko','76': 'Nidalee',
                '56': 'Nocturne','20': 'Nunu','2': 'Olaf','61': 'Orianna','516': 'Ornn','80': 'Pantheon','78': 'Poppy','555': 'Pyke',
                '246': 'Qiyana','133': 'Quinn','497': 'Rakan','33': 'Rammus','421': 'RekSai','526': 'Rell','58': 'Renekton','107': 'Rengar','92': 'Riven',
                '68': 'Rumble','13': 'Ryze','360': 'Samira','113': 'Sejuani','235': 'Senna','147': 'Seraphine','875': 'Sett','35': 'Shaco',
                '98': 'Shen','102': 'Shyvana','27': 'Singed','14': 'Sion','15': 'Sivir','72': 'Skarner','37': 'Sona','16': 'Soraka',
                '50': 'Swain','517': 'Sylas','134': 'Syndra','223': 'TahmKench','163': 'Taliyah','91': 'Talon','44': 'Taric','17': 'Teemo',
                '412': 'Thresh','18': 'Tristana','48': 'Trundle','23': 'Tryndamere','4': 'TwistedFate','29': 'Twitch','77': 'Udyr',
                '6': 'Urgot','110': 'Varus','67': 'Vayne','45': 'Veigar','161': 'Velkoz','254': 'Vi','234': 'Viego','112': 'Viktor','8': 'Vladimir',
                '106': 'Volibear','19': 'Warwick','498': 'Xayah','101': 'Xerath','5': 'XinZhao','157': 'Yasuo','777': 'Yone','83': 'Yorick',
                '350': 'Yuumi','154': 'Zac','238': 'Zed','115': 'Ziggs','26': 'Zilean','142': 'Zoe','143': 'Zyra'}


def get_champ_name(summonerName):
    champ_name_list = []
    champ_dic = safe_get_champ(safe_get_id(summonerName))
    for champion in champ_dic:
        champ_name = champ_namedic.get(str(champion.get("championId")))
        champ_name_list.append(champ_name)
    return champ_name_list

print(safe_get_champ(safe_get_id("REDDDSH"))[1])

def new_champ_list(summonerName):
    old_champ_list = safe_get_champ(safe_get_id(summonerName))
    new_champ_list = old_champ_list.copy()
    for champ in new_champ_list:
        champ["championId"] = champ_namedic.get(str(champ.get("championId")))
        champ.pop("summonerId")
        champ["lastPlayTime"] = datetime.datetime.fromtimestamp(int(champ.get("lastPlayTime")) // 1000).strftime('%Y-%m-%d %H:%M:%S')
    return new_champ_list



# def headers(new_champ_list):
#     headers = []
#     example = new_champ_list[1]
#     file_key = example.keys()
#     key_num = 0
#     for keys in range(0,len(file_key)):
#         key_num += 1
#         char_num = 0
#         key_list = list(str(keys))
#         for x in key_list:
#             if x.islower():
#                 char_num += 1
#             else:
#                 key_list[char_num] = x.lower()
#                 newList = key_list[0:char_num] + [" "] + key_list[char_num:]
#         string = "".join(newList)
#         headers.append(string)
#     return headers

print(pretty(new_champ_list("REDDDSH")))
for x in new_champ_list("Necora Nyaru"):
    print(x.get("championId"))

# Flask
app = Flask(__name__, template_folder='templates')
@app.route("/")
def main_handler():

    return render_template('nameform.html',page_title = "Champion Search")

@app.route("/response")
def response_handler():
    summoner_name = request.args.get('summonername')
    app.logger.info(summoner_name)
    header_list = ["Champion Name", "Level", "Champion Points", " Champion Points Since Last Level", "Champion Points Until Next Level",
                   "Chest Granted", "Last Play Time", " Tokens Earned", "Learn more"]
    if safe_get_id(summoner_name):
        return render_template('nameresponse.html', page_title= summoner_name, file_key = header_list,
                                file = new_champ_list(summoner_name), baseurl = str("https://universe.leagueoflegends.com/en_US/champion/"),
                               keyList = ["championId", "championLevel", "championPoints", "championPointsSinceLastLevel",
                                          "championPointsUntilNextLevel", "chestGranted", "lastPlayTime", "tokensEarned"],
                               championId = "championId")
    else:
        return render_template('nameform.html', page_title="Name Form - Error", prompt = "Wrong Summoner Name!")


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug = True)

