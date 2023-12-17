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
    meeting_link = "https://meeting.tencent.com/dm/CZSIBEjKMZb0"

    main(
        title="AA Workshop(I):\nAA Intro + Account",
        title_zh="账户抽象 workshop(I)",
        title_size=120,
        presenter="imToken Labs",
        presenter_avatar="./input/Symble_Square.png",
        twitter="@imTokenOfficial",
        language="Chinese",
        project="imToken Labs",
        project_logo="./input/imtoken.png",
        time_str="2023.12.19 20:00 (UTC+8)",
        meeting_number="430-278-937",
        meeting_link=meeting_link,
        meeting_type="tencent",
        doc_link="",
        chat_time_str="8pm, Dec 19th",
    )
