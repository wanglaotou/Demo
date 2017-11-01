import itchat 

itchat.auto_login()

itchat.send('Hello,filehelper',toUserName='filehelper')

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
	return msg.txt

itchat.auto_login()
itchat.run()
