#coding=utf8
import requests
import itchat

#KEY = '3ce015d11d4c49619cea64004af7c51f'
#API = 'http://www.tuling123.com/openapi/api'

KEY = '64e529d8095c413ebcf80b91cf1851d8'
API = 'http://www.tuling123.com/openapi/api'

def get_response(msg):
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        result = requests.post(API, data=data).json()
        return result.get('text')
    except:
        return


@itchat.msg_register(itchat.content.TEXT)#文字
@itchat.msg_register(itchat.content.PICTURE)#图片
@itchat.msg_register(itchat.content.RECORDING)#语音
def tuling_reply(msg):
    print("%s:%s" % ( msg['User']['NickName'],msg['Text'] ))
    defaultReply = 'I received: ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
    reply = get_response(msg['Text'])
    return reply or defaultReply


itchat.auto_login(hotReload=True)
itchat.run()
