#!/bin/bash

# 将此函数加入 .zshrc 方法调用，目的是一些图片缓存目录是没有后缀的，方便查看
# 定义函数 add_jpg_extension
add_jpg_extension() {
  # 目标目录
  local TARGET_DIR="$1"

  # 检查目标目录是否存在
  if [ ! -d "$TARGET_DIR" ]; then
    echo "Directory $TARGET_DIR does not exist."
    return 1
  fi

  # 遍历目录中的所有文件
  for file in "$TARGET_DIR"/*; do
    # 检查是否是文件
    if [ -f "$file" ]; then
      # 提取文件名和扩展名
      local filename=$(basename "$file")
      local extension="${filename##*.}"
      if [ "$extension" = "$filename" ]; then
        # 文件没有扩展名，添加 .jpg 后缀
        mv "$file" "$file.jpg"
        echo "Renamed: $file -> $file.jpg"
      fi
    fi
  done
}
