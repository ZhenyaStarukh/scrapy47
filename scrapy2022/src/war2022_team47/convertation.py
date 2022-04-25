import json
import codecs
import os.path

file_name = "womanrudisc.json"
json_path = os.path.dirname(os.path.realpath(__file__))+"\\war2022_team47\\"
print(json_path)
json_data = []
os.mkdir(json_path+"\\sas_ready_txt")
with open(json_path+"\\spiders\\"+file_name) as json_fileopen:
    json_data = json.load(json_fileopen)
for discussion in json_data:
    discussion_body = "".join(discussion['discussion_theme'])+"\n\n"\
                      + discussion['discussion_text'].replace("\xa0", " ")
    for comment in discussion['discussion_comments']:
        discussion_body += " ".join(comment['comment_text']).replace("\xa0", " ") + "\n\n"
    discussion_id = "".join(discussion['discussion_id'])
    with codecs.open(json_path+"\\sas_ready_txt\\" + discussion_id + ".txt", "w", "utf-8-sig") as temp:
        temp.write(discussion_body)
