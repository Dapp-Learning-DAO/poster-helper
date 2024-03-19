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
    meeting_link = "https://meeting.tencent.com/dm/SjZJHcpW4T9P"

    main(
        # title="AA Workshop(II):\nPaymaster + ERC-4337 Bundler",
        title=[
            {"txt": 'Dive in Layer 2 Modules', "size_scale": 1.0},
            {"txt": '', "size_scale": 1.4},
            {"txt": 'by Morph', "size_scale": 1.2},
        ],
        title_zh="Morph Layer2 深入解析",
        title_size=120,
        presenter="Luka",
        presenter_avatar="./input/avatar.jpg",
        twitter="@0xGantoL",
        language="Chinese",
        project="Morph",
        project_logo="./input/logo.png",
        project_twitter="@MorphL2",
        project_log_max_size=(400, 200),
        time_str="2024.03.19 20:00 (UTC+8)",
        meeting_number="525-656-774",
        meeting_link=meeting_link,
        meeting_type="tencent",
        doc_link="https://docs.google.com/presentation/d/1Fag5JyOqV9e0QeEC1f1sWf8kutOek2fXHzYDld76dIQ",
        chat_time_str="8:00pm, Mar 19th",
    )
