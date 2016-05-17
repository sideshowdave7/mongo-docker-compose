import uuid
import json
import pymongo
import random


def get_entry(month=0):
    v = json.loads('{"description": "Thanks! Turhan is flying in from CA to interview with the team onsite in Austin. \\n\\n-----------\\n\\nPlease enter feedback in smartrecruiters:\\nhttps://www.smartrecruiters.com/app/people/a6d2e51f-a2ac-4b4a-a062-834cec0bab66/messages\\n\\n----------\\n\\nInterview Schedule:\\n11:30am - 12:30pm CDT      Craig Drummond & Jonathon Kennemer - ATX Beerland\\n12:30pm - 1:15pm CDT        Lunch w/ Billy Mock - ATX Beerland (or Eatlassian)\\n1:15pm - 2pm CDT               Chuck Talk - ATX Beerland\\n2pm - 2:45pm CDT        ...", "visibility": "default", "private": false, "organizer": {"status": "", "role": "", "name": "", "updated_at": "2016-05-16T20:37:31.854753+00:00", "created_at": "2016-05-16T20:37:31.849128+00:00", "type": "", "id": 17490652, "email": "kminoza@atlassian.com"}, "id": 105072971, "end": 1463425200.0, "tentative": false, "title": "[ATX] F2F Interview: Turhan Herder - Premiere Support Engineer (SF)", "all_day": false, "start": 1463422500.0, "participants": [{"status": "", "is_organizer": false, "role": "", "name": "ATX - 16.18 - Beerland - 10p - VC", "updated_at": "2016-05-16T20:37:31.878235+00:00", "created_at": "2016-05-13T17:34:29.861116+00:00", "type": "", "email": "atlassian.com_33363432303231352d313934@resource.calendar.google.com", "id": 18494859995}, {"status": "", "is_organizer": false, "role": "", "name": "Chuck Talk", "updated_at": "2016-05-16T20:37:31.890962+00:00", "created_at": "2016-05-13T17:34:29.841500+00:00", "type": "", "email": "ctalk@atlassian.com", "id": 18494859992}, {"status": "", "is_organizer": false, "role": "", "name": "kmalone@atlassian.com", "updated_at": "2016-05-16T20:37:31.884638+00:00", "created_at": "2016-05-13T17:34:29.852210+00:00", "type": "", "email": "kmalone@atlassian.com", "id": 18494859994}], "location": "ATX - 16.18 - Beerland - 10p - VC", "identifier": "e7ok6v83i4jn7u0hpg2kseli04", "recurring": false}')

    r = random.randrange(0,50000)
    # 20 % company
    if r > 30000 and r < 40000:
        r = 30000
    # 10 % company
    elif r > 40000 and r < 45000:
        r = 40000
    # 10 % company
    elif r >= 45000:
        r = 45000

    v['company_id'] = r

    v['month'] = month

    return v


client = pymongo.MongoClient('ebdev.io')
db = client.test
cal = db.calendars

for i in xrange(100000):
    cal.insert(get_entry(6))
    cal.insert(get_entry(7))
    cal.insert(get_entry(8))
    cal.insert(get_entry(9))
    cal.insert(get_entry(10))
    cal.insert(get_entry(11))
