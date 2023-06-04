import streamlit as st
import pandas as pd
import numpy as np
import json
import requests

def openDoor():

    url = 'https://www.91hilife.com/erp//front/interface/door/openDoor/three'
    payload = {"isScan":"2","cardNo":"13632370507","distance":"0","userId":"3728644193967033128","doorName":"合生骏景花园逸A大堂门","communityId":260,"doorId":90011715,"doorCommunityId":260}
    headers = {'Host':'www.91hilife.com','Content-Type': 'application/json', 'is_guest': 'false','Cookie':'JSESSIONID=FE7F76803EF814F25C5CC58279E4DE7A; appmanage_web_APPLET_SESSION_ID=195644300834589900; erp_APPLET_SESSION_ID=1358205862092686388; accesscontrol_web_APPLET_SESSION_ID=948378855403572631; acw_tc=2760824d16807601491845044e0863facf8239dc23430619d28ad6d36c577f; advert_APPLET_SESSION_ID=8179368745998829535; protalmanage_APPLET_SESSION_ID=282384236711134068; CNZZDATA1278274866=163299725-1678240117-%7C1678427303; UM_distinctid=186bf147298498-0405e1b6adb63b-727a1d3c-5a900-186bf14729941c'}

    print("123433")
    response = requests.post(url, json=payload, headers=headers)
    result = response.text
    json_obj=json.loads(result)
    print(result)
 

    # print(resp)
    return json_obj

st.title('Open Door APP')

if st.button('Open Door'):
    result=openDoor()
    # data=json.dumps(result)
    status=result['status']
    if status==1:
        st.write("Open Success")
    else:
        st.write('Open Fail')
else:
    st.write('Goodbye')