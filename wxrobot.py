import requests
from wxpy import *
bot = Bot(cache_path=True)
my_friend = bot.friends().search('奇超')[0] #定位好友
my_friend.send('Hello！') #发送“Hello！”测试一下对接是否成功。
#group = bot.groups().search('浪啊浪')[0] #定位群

#接入图灵api：需要去网址申请：在http://www.tuling123.com/申请
tuling = Tuling(api_key='6f31ca4eb9fc4979a4a46e4e42eb9ae4')

# 使用图灵机器人自动与指定好友聊天
@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)


if __name__ == '__main__':
    bot.start()
    embed()
