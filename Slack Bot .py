import urllib3
import json
import logging
import enum

http = urllib3.PoolManager()


def lambda_handler(event, context):
    url = "Slack Api"
    sns_data = json.loads(event["Records"][0]["Sns"]["Message"])
    pipeline_name = sns_data["detail"]["pipeline"]
    state = sns_data["detail"]["state"]
    stage = sns_data["detail"]["stage"]
    pipid = sns_data["detail"]["execution-id"]
    details_req = pipid + " / " + stage + " / " + state

    if state == "FAILED":
        color = "#C70039"
    elif state == "STARTED" or state == "SUCCEEDED":
        color = "#008000"
    else:
        color = "#FF9900"
        
    if stage == "Source":
        msg = {
            "channel": "#test2",
            "username": "",
            "text": " ",
            "attachments": [
                {
                    "color": color,
                    "title": "",
                    "title_link": "",
                    "fields": [
                        {
                            "title": pipeline_name,
                            "value": details_req,
                            "short": False
                        },
                        {
                            "title": "Pipeline",
                            "value": "<https://us-east-1.console.aws.amazon.com/codesuite/codepipeline/pipelines/Notifier/view?region=us-east-1|LINK>",
                        },
                    ],
                },
            ],
        }
        encoded_msg = json.dumps(msg).encode('utf-8')

    elif stage == "Build":
        msg = {
            "channel": "#test2",
            "username": " ",
            "text": " ",
            "attachments": [
                {
                    "color": color,
                    "title": " ",
                    "title_link": "",
                    "fields": [
                        {
                            "title": pipeline_name,
                            "value": details_req,
                            "short": False
                        },
                        {
                            "title": "Pipeline",
                            "value": "<https://us-east-1.console.aws.amazon.com/codesuite/codepipeline/pipelines/Notifier/view?region=us-east-1|LINK>",
                        },
                    ],
                },
            ],
            "icon_emoji": "",
        }
        encoded_msg = json.dumps(msg).encode('utf-8')
    else:
        logging.ERROR("Pipeline Failed")

    resp = http.request('POST', url, body=encoded_msg)
    print({
        "status_code": resp.status,
        "response": resp.data
    })
