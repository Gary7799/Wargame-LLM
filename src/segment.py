
import os
from openai import OpenAI

def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return len(lines)

def split_file(file_path, num_segments):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    total_lines = len(lines)
    segment_size = total_lines // num_segments

    segments = []
    for i in range(num_segments):
        start = i * segment_size
        end = (i + 1) * segment_size if i < num_segments - 1 else total_lines
        segments.append(''.join(lines[start:end]))

    return segments

def generate_summary(text):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a professional StarCraft 2 player, skilled in analysing game strategies and match turning points."},
            {"role": "user", "content": f"This is part of the events data of a game, based on this data summarise the game during this period and give the strategy choices and turing point of the players in this game.\n\n{text}"}
        ]
    )

    return response.choices[0].message.content

def process_file(file_path):
    # 计算文件行数
    total_lines = count_lines(file_path)
    print(f"Total lines in the file '{file_path}': {total_lines}")

    # 将文件分成5段
    if total_lines >= 1400:
        segments = split_file(file_path, 5)
    elif total_lines >= 1100:
        segments = split_file(file_path, 4)
    elif total_lines >= 800:
        segments = split_file(file_path, 3)
    elif total_lines >= 500:
        segments = split_file(file_path, 2)
    else:
        segments = split_file(file_path, 1)

    # 调用GPT API生成每段的摘要
    summaries = []
    for i, segment in enumerate(segments):
        summary = generate_summary(segment)
        summaries.append(summary)
        # print(f"Summary for segment {i + 1} of '{file_path}':\n{summary}\n")

    # 合并所有摘要生成最终的总结
    final_summary = '\n'.join(summaries)

    # 保存最终的总结到同名_summary.txt文件中
    summary_file_path = file_path.replace('.txt', '_summary.txt')
    with open(summary_file_path, 'w', encoding='utf-8') as summary_file:
        summary_file.write(final_summary)
    print(f"Final summary saved to '{summary_file_path}'")

def main(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            process_file(file_path)

if __name__ == "__main__":
    main("D:\\Replays\\TVT - Cyclone Opening")