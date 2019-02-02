import datetime
import json
import logging
import sys
import os
from stackapi import StackAPI
from flask import Flask, jsonify
from flask import request
from flask import render_template
app = Flask(__name__, template_folder="templates")
app.root_path = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(stream=sys.stderr, level=logging.INFO)
LOG = logging.getLogger()
SITE_TYPE = "stackoverflow"
PAGE_SIZE = 100
MAX_PAGES = 1
TOP_N = 10
N_DAYS = 7

site = StackAPI(SITE_TYPE)
site.page_size = PAGE_SIZE
site.max_pages = MAX_PAGES


@app.route("/most_recent_questions", methods=['GET'])
def get_most_recent_questions():
    """
    This function is used to get the top 10 most recent asked questions for a particular tag from stackoverflow
    :return:
    """
    try:
        LOG.info("The request is: {} ".format(request))
        post_type = request.args.get('post_type', 'questions')
        tagged = request.args.get('tagged', 'android')
        sort = request.args.get('sort', 'creation')
        response_items = []
        final_response = {}
        stackoverflow_response = site.fetch(post_type, tagged=tagged, sort=sort)
        for item in stackoverflow_response["items"]:
            temp_dict = dict(title=item.get("title", "Empty_Title"), link=item.get("link", "Empty_URL"),
                             creation_date=item.get("creation_date", "Empty_Date"))
            response_items.append(temp_dict)
        final_response["output"] = response_items[:TOP_N]
    except Exception as e:
        LOG.error("Error fetching the latest questions from : {} {}".format(tagged, str(e)))
        return jsonify({"output": []})
    LOG.info("The final response to be returned is: {}".format(str(final_response)))
    #return render_template('<html><h1>HI</hi></html>')
    return render_template("index.html", result=final_response)


@app.route("/most_scored_questions", methods=['GET'])
def get_most_scored_questions():
    """
    This function is used to get the top 10 scored or relevant questions (depends on the score) from stackoverflow
    :return:
    """
    try:
        LOG.info("The request is: {} ".format(request))
        post_type = request.args.get('post_type', 'questions')
        tagged = request.args.get('tagged', 'android')
        sort = request.args.get('sort', 'votes')
        response_items = []
        final_response = {}
        fromdate = datetime.datetime.today() - datetime.timedelta(days=N_DAYS)
        todate = datetime.datetime.today()
        stackoverflow_response = site.fetch(post_type, tagged=tagged, sort=sort, fromdate=fromdate, todate=todate)
        for item in stackoverflow_response["items"]:
            temp_dict = dict(title=item.get("title", "Empty_Title"), link=item.get("link", "Empty_URL"),
                             creation_date=item.get("creation_date", "Empty_Date"))
            response_items.append(temp_dict)
        final_response["output"] = response_items[:TOP_N]
    except Exception as e:
        LOG.error("Error fetching the latest questions from : {} {}".format(tagged, str(e)))
        return jsonify({"output": []})
    LOG.info("The final response to be returned is: {}".format(str(final_response)))
    #return render_template('<html><h1>HI</hi></html>')
    return render_template("index.html", result=final_response)  #jsonify(final_response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
