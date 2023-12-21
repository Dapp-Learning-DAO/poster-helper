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
    meeting_link = "https://meeting.tencent.com/dm/0f6vSxjqtxFa"

    main(
        # title="AA Workshop(II):\nPaymaster + ERC-4337 Bundler",
        title=[
            {"txt": "AA Workshop(II):", "size_scale": 1},
            {"txt": "Paymaster + ERC-4337 Bundler", "size_scale": 0.8},
        ],
        title_zh="账户抽象 workshop(II)",
        title_size=120,
        presenter="Cyan & Jiahui",
        presenter_avatar="./input/Symble_Square.png",
        twitter="@imTokenOfficial",
        language="Chinese",
        project="imToken Labs",
        project_logo="./input/imtoken.png",
        time_str="2023.12.21 20:00 (UTC+8)",
        meeting_number="482-423-635",
        meeting_link=meeting_link,
        meeting_type="tencent",
        doc_link="""\n- https://docs.google.com/presentation/d/1RCZMrT_xncU7IClcLnHwmq6bABTS1OI0BIfez4g7rPQ/edit?usp=sharing
- https://docs.google.com/presentation/d/1heRbrECmAlPivmnVCeZH9s7hxs3MqGK5rWsj080-1c4/edit?usp=sharing""",
        chat_time_str="8pm, Dec 21th",
    )
