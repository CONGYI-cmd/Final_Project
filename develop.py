import urllib.parse, urllib.request, urllib.error, json
import ssl
# ssl.create_default_https_context = ssl._create_unverified_context
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)
##############
# Your turn! #
##############
# Now you're ready for the next part, where you retrieve data from an API
# of your choice. Note that you may need to provide an authentication key
# for some APIs. For that, work another file, called hw5-application.py.
#
# You will need to copy a fens, too, like pretty() or
# safe_get().w of the import statements from the top of this
# # file. You may copy any helpful function
#
# See requirements in the README.
#
# Also note that when the sunrise sunset API we used is queried for a
# date that doesn't exist, it gives a 400 error. Some APIs that you may
# use will return JSON-formatted data saying that the requested item
# couldn't be found. You may have to check the contents of the data you
# get back to see whether a query was successful. You don't have to do
# that with the sunrise sunset API.
# baseurl =  "https://www.googleapis.com/youtube/v3/search"
# resource_channelType = urllib.parse.urljoin(baseurl,"?"+ "part=snippet")
# print(resource_channelType)

# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python
# region = "na1"
# summonerID = "F3H7VpNLNxtcvTBHL35OMSIHtUtRxVO-MSMqjin59y0ssXkGi9OHqb6Biw"
# APIKey = "RGAPI-f31065db-a63d-4722-929d-b0decf6bd60c"
# url = "https://" + region + ".api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summonerID + \
#       "?api_key=" + APIKey

# paramstr = urllib.parse.urlencode({"api_key": url_key})
# newUrl = urllib.parse.urljoin(baseurl, "?" + paramstr)

import riot_key as riot_key
def get_champ(baseurl = "https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/",
              summonerID = "F3H7VpNLNxtcvTBHL35OMSIHtUtRxVO-MSMqjin59y0ssXkGi9OHqb6Biw",
              api_key = riot_key.key):
    url = baseurl + summonerID + "?api_key=" + api_key
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    page = urllib.request.urlopen(url, context=ctx)
    mypage = page.read().decode("utf-8")
    jsonFile = json.loads(mypage)
    return(jsonFile)

def safe_get_champ(summonerID = None):
    try:
        return get_champ(summonerID = summonerID)
    except urllib.error.URLError as e:
        print("There was an error with this request", e)
    except urllib.error.HTTPError as e:
        print("There was an error with this request", e)

def print_pretty_file():
    print(pretty(safe_get_champ(summonerID=id)))
# get_champ()
safe_get_champ(summonerID = "F3H7VpNLNxtcvTBHL35OMSIHtUtRxVO-MSMqjin59y0ssXkGi9OHqb6Biw")

# friend_list = ["NHLpIG3EdtyXTgyD_Tum6HEWpkX5ql1pxe8NWYb5drsfW572_3-lq9CuyQ", "F3H7VpNLNxtcvTBHL35OMSIHtUtRxVO-MSMqjin59y0ssXkGi9OHqb6Biw", "HtJB6MOOQ3XyyHfeLmrkmEzFdnA5A-VSbkaPA0yQJBgqwhhzhmXqT-e-jA", "MXgnRSWy3yRj_n-JJ0vfp667KT1cvABnj2bL2hByuS3L_GE", "mBKdILxxHg40MPNCHiadBkhC6_fTQeby4mtUm6SLFHafLAs", "foMiS-v6Fhqx_qHguRd2Ec48Ua3XYclsbb3uA_iqflk2nDl1KnUz7JcBkg"]
# for id in friend_list:
#     print_pretty_file()

name = (str)(raw_input(""))