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
    meeting_link = "https://meeting.tencent.com/dm/K6MhkNLAWtl2"

    main(
        # title="AA Workshop(II):\nPaymaster + ERC-4337 Bundler",
        title=[
            {"txt": 'Evolution of Ethereum Fee Mechanism', "size_scale": 0.8},
            {"txt": '', "size_scale": 0.8},
            {"txt": 'EIP1559 -> EIP4844', "size_scale": 1},
        ],
        title_zh="以太坊费用机制的演变: [→ EIP1559 → EIP4844]",
        title_size=100,
        presenter="Jason",
        presenter_avatar="./input/avatar.jpg",
        twitter="@0xbbbb_eth",
        language="Chinese",
        project="ETHconomics Research Space",
        project_logo="",
        project_log_max_size=(400, 200),
        time_str="2024.02.25 21:00 (UTC+8)",
        meeting_number="273-504-825",
        meeting_link=meeting_link,
        meeting_type="tencent",
        doc_link="https://docs.google.com/presentation/d/1timyH4y3cqeJRgrIz0hCTLdmGK_CFRMEz_XpXIuPV5E/edit#slide=id.p",
        chat_time_str="9:00pm, Feb 25th",
    )
