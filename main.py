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

    main(
        title=[
            {"txt": '', "size_scale": 0.8},
            {"txt": 'Dex Strategies on HummingBot', "size_scale": 1.0},
            {"txt": '', "size_scale": 0.8},
        ],
        title_zh="HummingBot 上的 Dex 策略分享",
        main_content="""
- HummingBot 的历史
- HummingBot 是什么
- HummingBot 上的Dex策略
- HummingBot 实操演示
""",
        title_size=80,
        title_size_cover=80,
        presenter="Dolm",
        presenter_avatar="./input/avatar.png",
        twitter="@dolm5415",
        language="Chinese",
        project="Hummmingbot Foundation",
        project_logo="./input/hummingbot-logo.svg",
        project_logo_horizontal="",
        project_twitter="",
        project_log_max_size=(180, 180),
        time_str="2025.07.21 20:00 (UTC+8)",
        meeting_number="448-927-766",
        meeting_link="https://meeting.tencent.com/dm/R859UQFXVg7v",
        meeting_type="tencent",
        doc_link="https://www.canva.com/design/DAGr4zip7BM/zkRxikA33cN9wMdcRLpJHQ/view",
        chat_time_str="8:00pm, July 21st",
    )
