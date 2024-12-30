from src.generate_sharing_cover import generate_sharing_cover
from src.generate_sharing_post import generate_sharing_post
from src.generate_text import generate_text


def main(
    title,
    title_size,
    title_size_cover,
    presenter,
    presenter_avatar,
    twitter,
    language,
    project,
    project_logo,
    project_logo_horizontal,
    project_twitter,
    project_log_max_size,
    time_str,
    meeting_number,
    meeting_link,
    meeting_type,
    doc_link,
    title_zh,
    main_content,
    chat_time_str,
):
    generate_sharing_post(
        title=title,
        title_size=title_size,
        presenter=presenter,
        twitter=twitter,
        language=language,
        project=project,
        project_logo=project_logo,
        project_log_max_size=project_log_max_size,
        time_str=time_str,
        meeting_number=meeting_number,
        meeting_link=meeting_link,
        meeting_type=meeting_type,
    )

    generate_sharing_cover(
        title=title,
        title_size=title_size_cover if title_size_cover else title_size,
        presenter=presenter,
        presenter_avatar=presenter_avatar,
        twitter=twitter,
        language=language,
        project=project,
        project_logo=project_logo_horizontal if project_logo_horizontal else project_logo,
        project_log_max_size=project_log_max_size,
        time_str=time_str,
        meeting_number=meeting_number,
        meeting_link=meeting_link,
        meeting_type=meeting_type,
    )

    chat_announcement, meeting_announcement, video_intro, video_link = generate_text(
        title=title,
        presenter=presenter,
        twitter=twitter,
        language=language,
        project=project,
        project_logo=project_logo,
        project_twitter=project_twitter,
        time_str=time_str,
        meeting_number=meeting_number,
        meeting_link=meeting_link,
        meeting_type=meeting_type,
        doc_link=doc_link,
        title_zh=title_zh,
        main_content=main_content,
        chat_time_str=chat_time_str,
    )
    
    # print()
    # print(chat_announcement)
    # print()
    # print(meeting_announcement)
    # print()
    # print(video_intro)
    # print()
    # print(video_link)


if __name__ == "__main__":
    meeting_link = "https://meeting.tencent.com/dm/scBibuvXjEIx"

    main(
        # title="AA Workshop(II):\nPaymaster + ERC-4337 Bundler",
        title=[
            {"txt": '', "size_scale": 1.0},
            {"txt": 'Web2⇔Web3 through Email', "size_scale": 1.1},
        ],
        title_zh="通过 Email 实现 Web2 和 Web3 互通",
        main_content="""
1. 在区块链上适配 DKIM
2. 使用 ZK（零知识）技术保护身份和消息隐私
3. 相关风险
""",
        title_size=90,
        title_size_cover=80,
        presenter="Jason",
        presenter_avatar="./input/avatar.jpg",
        twitter="0xbbbb_eth",
        language="Chinese",
        project="Panta Rhei",
        project_logo="./input/logo.png",
        project_logo_horizontal="./input/logo.png",
        project_twitter="0xpantarhei",
        project_log_max_size=(480, 480),
        time_str="2024.12.30 20:00 (UTC+8)",
        meeting_number="528-768-393",
        meeting_link=meeting_link,
        meeting_type="tencent",
        doc_link="https://docs.google.com/presentation/d/15KLwPefsIrmC2OUeE_WDhqPCEcC7FOSFzUoRtYjT4fw/edit?usp=sharing",
        chat_time_str="8:00pm, Dec 30th",
    )
