#!/bin/bash

# 固定檔案大小（預設：1MB）
FILE_SIZE="1M"

# 目標資料夾
TARGET_DIR="target"

# 新的副檔名清單
# EXTENSIONS=("csr" "p12" "suo" "ppsm" "pfx" "odg" "sldx" "otg" "onetoc2" "brd")
EXTENSIONS=("csr" "sldx" "otg" "onetoc2" "brd")

# 建立資料夾
mkdir -p "$TARGET_DIR"

# 建立檔案
for i in "${!EXTENSIONS[@]}"; do
    filename="$TARGET_DIR/$((i + 1)).${EXTENSIONS[$i]}"
    
    if command -v fallocate >/dev/null 2>&1; then
        fallocate -l "$FILE_SIZE" "$filename"
    else
        dd if=/dev/zero of="$filename" bs=$FILE_SIZE count=1 2>/dev/null
    fi

    echo "Created: $filename"
done
