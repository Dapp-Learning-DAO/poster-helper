from src.generate_sharing_cover import generate_sharing_cover
from src.generate_sharing_post import generate_sharing_post
from src.generate_text import generate_text


def main(
    title,
    presenter,
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
    meeting_link = "https://us06web.zoom.us/j/84222261147"

    main(
        title="Reqeust Network XXXX",
        presenter="David Hunt-Mateo",
        twitter="@RequestNetwork",
        language="English",
        project="Reqeust Network",
        project_logo="./img/ethereum_foundation_logo.svg",
        time_str="2023.12.14 22:00 (UTC+8)",
        meeting_number="842-222-61147",
        meeting_link=meeting_link,
        meeting_type="zoom",
        doc_link="https://github.com/sec-bit/learning-zkp/blob/develop/plonk-intro-cn/7-plonk-lookup.md",
        title_zh="查找表技术",
        chat_time_str="8pm, Dec 9th",
    )
