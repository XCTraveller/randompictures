import os

def batch_rename(folder):
    # 排除自身脚本文件
    script_name = os.path.basename(__file__)

    # 保存上次执行到的编号
    last_num_file = os.path.join(folder, "last_renamed.txt")
    if os.path.exists(last_num_file):
        with open(last_num_file, "r", encoding="utf-8") as f:
            last_num = int(f.read().strip() or 0)
    else:
        last_num = 0

    files = sorted(os.listdir(folder))

    for file in files:
        if file == script_name or file == "last_renamed.txt":
            continue  # 跳过脚本自身和记录文件

        old_path = os.path.join(folder, file)
        if not os.path.isfile(old_path):
            continue  # 跳过文件夹

        name, ext = os.path.splitext(file)
        last_num += 1
        new_name = f"{last_num}{ext}"
        new_path = os.path.join(folder, new_name)

        # 如果目标文件存在，则跳过
        if os.path.exists(new_path):
            print(f"跳过 {file} -> {new_name} (已存在)")
            last_num -= 1  # 保持编号不浪费
            continue

        os.rename(old_path, new_path)
        print(f"{file} -> {new_name}")

    # 更新记录文件
    with open(last_num_file, "w", encoding="utf-8") as f:
        f.write(str(last_num))


if __name__ == "__main__":
    folder_path = os.path.dirname(os.path.abspath(__file__))
    batch_rename(folder_path)
