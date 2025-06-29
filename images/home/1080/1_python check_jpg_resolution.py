import os
from PIL import Image

def find_non_standard_resolution_jpg_images(target_resolution=(1920, 1080), output_filename="1_non_1920x1080_jpg_images.txt"):
    """
    遍历脚本所在目录下的所有JPG图片，检测其分辨率，并筛选出非指定分辨率的图片路径。

    Args:
        target_resolution (tuple): 目标分辨率，格式为 (宽度, 高度)。
        output_filename (str): 输出的TXT文件名称。
    """
    # 获取当前脚本文件所在的目录
    folder_path = os.path.dirname(os.path.abspath(__file__))
    non_standard_images = []

    print(f"正在检测当前目录：{folder_path} 中的JPG图片分辨率...")
    print(f"目标分辨率：{target_resolution[0]}x{target_resolution[1]}")

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'): # 只检测.jpg和.jpeg文件
            file_path = os.path.join(folder_path, filename)
            try:
                with Image.open(file_path) as img:
                    width, height = img.size
                    if (width, height) != target_resolution:
                        # 记录相对路径
                        relative_path = os.path.join("./", filename)
                        non_standard_images.append(relative_path)
                        print(f"  发现非标准分辨率JPG图片：{filename} - 分辨率: {width}x{height}")
            except Exception as e:
                print(f"  无法处理JPG图片文件 '{filename}'：{e}")

    if not non_standard_images:
        print("\n太棒了！当前目录所有JPG图片都是目标分辨率。")
        return

    # 将非标准分辨率的图片路径写入TXT文件
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            for path in non_standard_images:
                f.write(path + '\n')
        print(f"\n非目标分辨率的JPG图片路径已成功保存到文件：{output_filename}")
    except IOError as e:
        print(f"写入文件时发生错误：{e}")

if __name__ == "__main__":
    find_non_standard_resolution_jpg_images()