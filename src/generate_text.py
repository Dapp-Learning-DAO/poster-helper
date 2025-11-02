from typing import Literal


def generate_text(
    title: str,
    presenter: str,
    meeting_number: str,
    time_str: str,
    meeting_link: str,
    language: str = "Chinese",
    twitter: str = "",
    project: str = "",
    project_logo: str = "",
    project_twitter: str = "",
    meeting_type: Literal["tencent", "zoom", "google"] = "tencent",  # "tencent" | "zoom" | "google"
    doc_link: str = "",
    title_zh: str = "",
    main_content: str = "",
    chat_time_str: str = "",
):
    if isinstance(title, str):
        title = title.replace("\n", " ")
    else:
        title = " ".join([line["txt"].replace("\n", "") for line in title])

    if title_zh != "":
        title_zh = f"{title_zh}"

    meeting_name = "腾讯会议"
    if meeting_type == "zoom":
        meeting_name = "ZOOM会议"
    elif meeting_type == "google":
        meeting_name = "谷歌会议"
    
    presenter_wecaht = presenter
    if project:
        presenter_wecaht += f" from {project}"

    presenter_twitter = presenter
    if twitter:
        presenter_twitter = twitter
    if project_twitter:
        presenter_twitter += f" from {project_twitter}"
    elif project:
        presenter_twitter += f" from {project}"


    chat_announcement = f"""
wechat:

🎉🎉🎉
DappLearning 分享会预告：
分享者：{presenter}
{'项目/社区：' + project if project else ''}

标题：{title_zh}({title})
主要内容：{main_content}
会议时间：{chat_time_str}
会议语言：{"英文" if language.lower() == "english" else "中文"} 
会议链接：{meeting_link}
{meeting_name}：{meeting_number}
分享材料：{doc_link if doc_link else ""}

欢迎大家来做分享, 优秀分享者将会获得 200 DAI 奖励哦！  
https://dapplearning.org/sharing
🎉🎉🎉

At {chat_time_str} (utc+8), we are excited to have {presenter_wecaht} to bring us a sharing about '{title}{"("+title_zh+")" if title_zh else ""}'. Don't miss this meeting if you are interested in![Rose][Rose][Rose]

meeting link: {meeting_link}
{"doc link: " + doc_link if doc_link else ""}

Feel free to come to share and get 200 DAI reward. Complete the form at the following link: 
https://dapplearning.org/sharing



\n\n
🎉🎉🎉
During the sharing period, you have the chance to receive ZK red packet rewards!
来听分享的小伙伴，可以获取官网口令红包哦！



twitter:
At {chat_time_str} (utc+8), we are excited to have {presenter_twitter} to bring us a sharing about '{title}{"("+title_zh+")" if title_zh else ""}'. Don't miss this meeting if you are interested in!🌹🌹🌹

meeting link: {meeting_link}
{"doc link: " + doc_link if doc_link else ""}

Feel free to come to share and get 200 DAI reward. Complete the form at the following link: 
https://dapplearning.org/sharing


\n\n
🎉🎉🎉
During the sharing period, you have the chance to receive ZK red packet rewards!
来听分享的小伙伴，可以获取官网口令红包哦！

"""

    meeting_announcement = f"""DL Open Source University
+V: DappLearning, 加入交流群

标题：{title_zh}({title})
分享者：{presenter}
{'项目/社区：' + project if project else ''}
主要内容：{main_content}
分享者推特: {twitter}
资料链接: {doc_link}

🎉🎉🎉DappLearning 官网上线啦🎉🎉🎉
小伙伴们快去注册吧，享受更多社区福利 !
也欢迎大家报名分享！

官网传送门👇
https://dapplearning.org/

欢迎关注和加入我们:
website: https://dapplearning.org
github: https://github.com/Dapp-Learning-DAO/Dapp-Learning
公众号: Dapp Learning
discord: https://discord.gg/cRYNYXqPeR
telegram: https://t.me/joinchat/48Mp2jy4Yw40MmI1
twitter: https://twitter.com/Dapp_Learning
bilibili: https://space.bilibili.com/2145417872
youtube: https://www.youtube.com/c/DappLearning

本项目适合有一定语言基础的开发者入门区块链 DAPP 开发, 由浅到深了解和开发 DeFi, NFT, DAO, CRYPTO 项目。
项目愿景是给初级开发者一个可执行且最简的区块链 Dapp 学习路线图, 给进阶开发者一个可以交流和协作的平台。

We are designed for developers with basic skills to step into blockchain DAPP development, where they can get close to DeFi, NFT, DAO, CRYPTO projects. We hope we could not only give junior developers an executable and simplest blockchain DAPP learning roadmap, but also present advanced developers with a platform for communication and cooperation.
    """

    video_intro = f"""+V: DappLearning, 加入交流群

标题：{title_zh}({title})
分享者：{presenter}
{'项目/社区：' + project if project else ''}
主要内容：{main_content}
分享者推特: {twitter}
资料链接: {doc_link}

🎉🎉🎉DappLearning 官网上线啦🎉🎉🎉
小伙伴们快去注册吧，享受更多社区福利 !
也欢迎大家报名分享！

官网传送门👇
https://dapplearning.org/

欢迎来做分享, 我们秉持开源大学理念, 创造去中心化的分享体验, 可自行填写表格安排时间和分享内容: 
https://dapplearning.org/sharing


欢迎关注和加入我们: 
Welcome to follow and join us:
website: https://dapplearning.org
github: https://github.com/Dapp-Learning-DAO/Dapp-Learning
公众号: Dapp Learning
discord: https://discord.gg/cRYNYXqPeR
telegram: https://t.me/joinchat/48Mp2jy4Yw40MmI1
twitter: https://twitter.com/Dapp_Learning
youtube: https://www.youtube.com/c/DappLearning
bilibili: https://space.bilibili.com/2145417872
bounty: https://dapplearning.org/bounty

本项目适合有一定语言基础的开发者入门区块链 DAPP 开发, 由浅到深了解和开发 DeFi, NFT, DAO, CRYPTO 项目。
项目愿景是给初级开发者一个可执行且最简的区块链 Dapp 学习路线图, 给进阶开发者一个可以交流和协作的平台。

We are designed for developers with basic skills to step into blockchain DAPP development, where they can get close to DeFi, NFT, DAO, CRYPTO projects. We hope we could not only give junior developers an executable and simplest blockchain DAPP learning roadmap, but also present advanced developers with a platform for communication and cooperation.
    """

    video_link = f"""《{title_zh}》by {presenter}
精彩分享已上传, 欢迎点赞收藏订阅转发～～

Youtube: 
Bilibili: 
    """

    with open("./output/announcement.txt", "w", encoding="utf-8") as file:
        file.write(f"\n{chat_announcement}\n\n\n\n\n{meeting_announcement}\n\n\n\n\n{video_intro}\n\n\n\n\n{video_link}\n\n\n\n\n")


    return chat_announcement, meeting_announcement, video_intro, video_link
