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
    meeting_link = "https://meet.google.com/sqn-tved-zxb"

    main(
        # title="AA Workshop(II):\nPaymaster + ERC-4337 Bundler",
        title=[
            {"txt": 'Ethereum decentralization,', "size_scale": 1.0},
            {"txt": 'Censorship resistance', "size_scale": 1.0},
            {"txt": 'and Client diversity', "size_scale": 1.0},
        ],
        title_zh="以太坊去中心化、抗审查性和客户端多样性",
        title_size=90,
        title_size_cover=75,
        presenter="Ahmad Bitar",
        presenter_avatar="./input/avatar.jpg",
        twitter="@Smartprogrammer",
        language="English",
        project="Nethermind",
        project_logo="./input/Nethermind_Light_Vertical.png",
        project_logo_horizontal="./input/logo.png",
        project_twitter="@NethermindEth",
        project_log_max_size=(400, 300),
        time_str="2024.04.14 20:00 (UTC+8)",
        meeting_number="sqn-tved-zxb",
        meeting_link=meeting_link,
        meeting_type="google",
        doc_link="",
        chat_time_str="8:00pm, Apr 14th",
    )
