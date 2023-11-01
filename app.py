import streamlit as st
import requests
import re
import json
# import pyperclip

def get_channel_id(url):
    response = requests.get(url).text
    reCompYtInfo = re.compile("ytInitialData" + ' = ({.*?});', re.DOTALL)
    searchCompYtInfo = reCompYtInfo.search(response)
    data = json.loads(searchCompYtInfo.group(1))
    channel_id = data.get("contents").get("twoColumnBrowseResultsRenderer").get("tabs")[0].get("tabRenderer").get("endpoint").get("browseEndpoint").get("browseId")

    return channel_id

st.title("유튜브 채널 ID 조회기")
value = st.text_input(label="URL을 입력하세요")

if st.button("조회"):
    get_channel_id(value)
    channel_id = get_channel_id(value)
    st.code(channel_id, language="python")
    # pyperclip.copy(channel_id)
    st.success('조회를 성공하였습니다. 마우스를 오버하여 클립보드에 복사하세요.')