
import requests
from feed_pb2 import Feed
from google.protobuf.json_format import MessageToDict


def start_requests():

    headers = {
        'authority': 'xxxxxx',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookies':'自己的cookie',
        'origin': 'https://www.xxxxx.com',
        'pragma': 'no-cache',
        'referer': 'https://www.xxxxx.com/video/BV1E4411B7ef?spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=3374492988fa79cc49e37a8221ff5cd8',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    params = {
        'type': '1',
        'oid': '133823042',
        'pid': '66028664',
        'segment_index': '1',
    }
 
    response = requests.get('https://api.******.com/x/v2/dm/web/seg.so', params=params,
                            headers=headers)
    print(response)
    print('-------------------------------')
    info = Feed()
    info.ParseFromString(response.content)
    _data = MessageToDict(info, preserving_proto_field_name=True)
    messages = _data.get("message") or []
    print('messages',messages)
    print("===========================================")
    for message in messages:
        print(message.get("content"))


if __name__ == '__main__':
    start_requests()




# '{"nested":{"bilibili":{"nested":{"community":{"nested":{"service":{"nested":{"dm":{"nested":{"v1":{"nested":{"DmWebViewReply":{"fields":{"state":{"type":"int32","id":1},"text":{"type":"string","id":2},"textSide":{"type":"string","id":3},"dmSge":{"type":"DmSegConfig","id":4},"flag":{"type":"DanmakuFlagConfig","id":5},"specialDms":{"rule":"repeated","type":"string","id":6},"checkBox":{"type":"bool","id":7},"count":{"type":"int64","id":8},"commandDms":{"rule":"repeated","type":"CommandDm","id":9},"dmSetting":{"type":"DanmuWebPlayerConfig","id":10},"reportFilter":{"rule":"repeated","type":"string","id":11},"expressions":{"rule":"repeated","type":"Expressions","id":12},"postPanel":{"rule":"repeated","type":"PostPanel","id":13},"activityMetas":{"rule":"repeated","type":"string","id":14}}},"PostPanel":{"fields":{"start":{"type":"int64","id":1},"end":{"type":"int64","id":2},"priority":{"type":"int64","id":3},"bizId":{"type":"int64","id":4},"bizType":{"type":"PostPanelBizType","id":5},"clickButton":{"type":"ClickButton","id":6},"textInput":{"type":"TextInput","id":7},"checkBox":{"type":"CheckBox","id":8},"toast":{"type":"Toast","id":9}}},"ClickButton":{"fields":{"portraitText":{"rule":"repeated","type":"string","id":1},"landscapeText":{"rule":"repeated","type":"string","id":2},"portraitTextFocus":{"rule":"repeated","type":"string","id":3},"landscapeTextFocus":{"rule":"repeated","type":"string","id":4},"renderType":{"type":"RenderType","id":5},"show":{"type":"bool","id":6}}},"PostPanelBizType":{"values":{"PostPanelBizTypeNone":0,"PostPanelBizTypeEncourage":1,"PostPanelBizTypeFragClose":4}},"TextInput":{"fields":{"portraitPlaceholder":{"rule":"repeated","type":"string","id":1},"landscapePlaceholder":{"rule":"repeated","type":"string","id":2},"renderType":{"type":"RenderType","id":3},"placeholderPost":{"type":"bool","id":4},"show":{"type":"bool","id":5},"postStatus":{"type":"PostStatus","id":7}}},"PostStatus":{"values":{"PostStatusNormal":0,"PostStatusClosed":1}},"RenderType":{"values":{"RenderTypeNone":0,"RenderTypeSingle":1,"RenderTypeRotation":2}},"CheckBox":{"fields":{"text":{"type":"string","id":1},"type":{"type":"CheckboxType","id":2},"defaultValue":{"type":"bool","id":3},"show":{"type":"bool","id":4}}},"CheckboxType":{"values":{"CheckboxTypeNone":0,"CheckboxTypeEncourage":1}},"Toast":{"fields":{"text":{"type":"string","id":1},"duration":{"type":"int32","id":2},"show":{"type":"bool","id":3},"button":{"type":"Button","id":4}}},"Button":{"fields":{"text":{"type":"string","id":1},"action":{"type":"ToastFunctionType","id":2}}},"ToastFunctionType":{"values":{"ToastFunctionTypeNone":0,"ToastFunctionTypePostPanel":1}},"ToastBizType":{"values":{"ToastBizTypeNone":0,"ToastBizTypeEncourage":1}},"CommandDm":{"fields":{"id":{"type":"int64","id":1},"oid":{"type":"int64","id":2},"mid":{"type":"int64","id":3},"command":{"type":"string","id":4},"content":{"type":"string","id":5},"progress":{"type":"int32","id":6},"ctime":{"type":"string","id":7},"mtime":{"type":"string","id":8},"extra":{"type":"string","id":9},"idStr":{"type":"string","id":10}}},"DmSegConfig":{"fields":{"pageSize":{"type":"int64","id":1},"total":{"type":"int64","id":2}}},"DanmakuFlagConfig":{"fields":{"recFlag":{"type":"int32","id":1},"recText":{"type":"string","id":2},"recSwitch":{"type":"int32","id":3}}},"DmSegMobileReply":{"fields":{"elems":{"rule":"repeated","type":"DanmakuElem","id":1}}},"DanmakuElem":{"fields":{"id":{"type":"int64","id":1},"progress":{"type":"int32","id":2},"mode":{"type":"int32","id":3},"fontsize":{"type":"int32","id":4},"color":{"type":"uint32","id":5},"midHash":{"type":"string","id":6},"content":{"type":"string","id":7},"ctime":{"type":"int64","id":8},"weight":{"type":"int32","id":9},"action":{"type":"string","id":10},"pool":{"type":"int32","id":11},"idStr":{"type":"string","id":12},"attr":{"type":"int32","id":13},"effect":{"type":"string","id":22}}},"DanmuWebPlayerConfig":{"fields":{"dmSwitch":{"type":"bool","id":1},"aiSwitch":{"type":"bool","id":2},"aiLevel":{"type":"int32","id":3},"blocktop":{"type":"bool","id":4},"blockscroll":{"type":"bool","id":5},"blockbottom":{"type":"bool","id":6},"blockcolor":{"type":"bool","id":7},"blockspecial":{"type":"bool","id":8},"preventshade":{"type":"bool","id":9},"dmask":{"type":"bool","id":10},"opacity":{"type":"float","id":11},"dmarea":{"type":"int32","id":12},"speedplus":{"type":"float","id":13},"fontsize":{"type":"float","id":14},"screensync":{"type":"bool","id":15},"speedsync":{"type":"bool","id":16},"fontfamily":{"type":"string","id":17},"bold":{"type":"bool","id":18},"fontborder":{"type":"int32","id":19},"drawType":{"type":"string","id":20},"seniorModeSwitch":{"type":"int32","id":21}}},"Expressions":{"fields":{"data":{"rule":"repeated","type":"Expression","id":1}}},"Expression":{"fields":{"keyword":{"rule":"repeated","type":"string","id":1},"url":{"type":"string","id":2},"period":{"rule":"repeated","type":"Period","id":3}}},"Period":{"fields":{"start":{"type":"int64","id":1},"end":{"type":"int64","id":2}}}}}}}}}}}}}}}'

