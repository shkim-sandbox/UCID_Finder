import streamlit as st
import requests
import re
import json

def get_channel_id(url):
    response = requests.get(url).text
    reCompYtInfo = re.compile("ytInitialData" + ' = ({.*?});', re.DOTALL)
    searchCompYtInfo = reCompYtInfo.search(response)
    data = json.loads(searchCompYtInfo.group(1))
    channel_id = data.get("contents").get("twoColumnBrowseResultsRenderer").get("tabs")[0].get("tabRenderer").get("endpoint").get("browseEndpoint").get("browseId")

    return channel_id

value = st.text_input(label="URL을 입력하세요")

if st.button("조회"):
    get_channel_id(value)
    st.text(get_channel_id(value))