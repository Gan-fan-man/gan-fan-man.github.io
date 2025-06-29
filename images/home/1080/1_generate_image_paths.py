import os

def generate_image_paths_in_current_directory(output_filename="1_image_paths.txt"):
    """
    遍历脚本所在目录下的所有图片，并生成特定格式的图片路径字符串，然后保存到TXT文件。
    """
    # 获取当前脚本文件所在的目录
    folder_path = os.path.dirname(os.path.abspath(__file__))
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp') # 可以根据需要添加或删除图片扩展名
    image_paths = []

    print(f"正在遍历当前目录：{folder_path}")
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(image_extensions):
            # 拼接目标格式的字符串
            path_string = f"  - /images/home/1080/{filename}"
            image_paths.append(path_string)
            print(f"找到图片：{filename} -> {path_string}")

    if not image_paths:
        print("未在当前目录找到任何图片文件。")
        return

    # 将生成的路径写入TXT文件
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            for path in image_paths:
                f.write(path + '\n')
        print(f"\n图片路径已成功保存到文件：{output_filename}")
    except IOError as e:
        print(f"写入文件时发生错误：{e}")

if __name__ == "__main__":
    generate_image_paths_in_current_directory()