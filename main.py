# from flask import Flask, render_template, request
# import logging
#
# app = Flask(__name__, template_folder='templates')
# @app.route("/")
# def main_handler():
#
#     return render_template('nameform.html',page_title = "Champion Search")
#
# @app.route("/response")
# def response_handler():
#     summoner_name = request.args.get('summonername')
#     app.logger.info(summoner_name)
#     if summoner_name :
#         return render_template('nameresponse.html', len = 3, champ_name_list = ["1", "2", "3"])
#     else:
#         return render_template('nameform.html', page_title="Name Form - Error", prompt = "Wrong Summoner Name!")
#
#
# if __name__ == "__main__":
#     app.run(host="localhost", port=8080, debug = True)

