from src.generate_sharing_cover import generate_sharing_cover
from src.generate_sharing_post import generate_sharing_post
from src.generate_text import generate_text


def main(
    title,
    title_size,
    presenter,
    presenter_avatar,
    twitter,
    language,
    project,
    project_logo,
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
        presenter=presenter,
        presenter_avatar=presenter_avatar,
        twitter=twitter,
        language=language,
        project=project,
        project_logo=project_logo,
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
    meeting_link = "https://meeting.tencent.com/dm/EhilLAleZgc8"

    main(
        # title="AA Workshop(II):\nPaymaster + ERC-4337 Bundler",
        title=[
            {"txt": 'Pendle Finance', "size_scale": 1.4},
        ],
        title_zh="Pendle Finance协议解析",
        title_size=120,
        presenter="Sam",
        presenter_avatar="./input/avatar.jpg",
        twitter="@0xmetazen",
        language="Chinese",
        project="",
        project_logo="",
        project_twitter="",
        project_log_max_size=(400, 200),
        time_str="2024.04.07 20:00 (UTC+8)",
        meeting_number="865-600-588",
        meeting_link=meeting_link,
        meeting_type="tencent",
        doc_link="https://drive.google.com/file/d/1CafQmIZoEqrBcge_TF6d1kMJC8ATSo4Z/view?usp=sharing",
        chat_time_str="8:00pm, Apr 7th",
    )
