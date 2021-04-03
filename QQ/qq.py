import asyncio

from graia.application import GraiaMiraiApplication, Session
from graia.application.friend import Friend
from graia.application.group import Group, Member
from graia.application.message.chain import MessageChain
from graia.application.message.elements.internal import At
from graia.application.message.elements.internal import Plain
from graia.broadcast import Broadcast

from Chat.main import reply

loop = asyncio.get_event_loop()

bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="http://localhost:8642",  # mirai httpapi 服务运行的地址
        authKey="Glucosamine",  # mirai authKey
        account=993422335,  # 机器人 qq 号
        websocket=True
    )
)


@bcc.receiver("FriendMessage")
async def friend_message_listener(app: GraiaMiraiApplication, friend: Friend):
    text = "作者：\n\tgithub.com/GlucoseHuang\n\n技术支持：\n\tgithub.com/mamoe/mirai\n\tgithub.com/Dimsmary/Ossas_ChatBot\n\t特别鸣谢！"
    await app.sendFriendMessage(friend, MessageChain.create([Plain(text)]))


@bcc.receiver("GroupMessage")
async def groupMessage(app: GraiaMiraiApplication, group: Group, member: Member, message: MessageChain):
    if message.has(At):
        if message.get(At)[0].target == 993422335:
            str_reply = reply(message[Plain][0].text.strip())
            await app.sendGroupMessage(group, MessageChain.create([Plain(str_reply + ' '), At(member.id)]))


app.launch_blocking()
