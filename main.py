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
    meeting_link = "https://meeting.tencent.com/dm/lozHZ6sgZC96"

    main(
        # title="AA Workshop(II):\nPaymaster + ERC-4337 Bundler",
        title=[
            {"txt": 'Devcon7 Insights:', "size_scale": 1.0},
            {"txt": 'the Latest Advancements in', "size_scale": 1.0},
            {"txt": 'Ethereum Technology', "size_scale": 1.0},
        ],
        title_zh="Devcon7见闻--以太坊最新技术进展分享",
        title_size=90,
        title_size_cover=80,
        presenter="Yan",
        presenter_avatar="./input/avatar.png",
        twitter="yanyanho",
        language="Chinese",
        project="DappLearning",
        project_logo="",
        project_logo_horizontal="",
        project_twitter="",
        project_log_max_size=(460, 460),
        time_str="2024.12.15 20:00 (UTC+8)",
        meeting_number="607-771-690",
        meeting_link=meeting_link,
        meeting_type="tencent",
        doc_link="https://dldao.notion.site/6-Devcon-159c40c2577f80f38862cc76563feb35",
        chat_time_str="8:00pm, Dec 15th",
    )
