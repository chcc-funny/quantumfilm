#!/bin/bash
# 图片生成进度检查脚本

IMG_DIR="/Users/funnyliu/Documents/量子膜/量子膜-CHCC资料/量子膜-客户-介绍网页/generated_images"
TOTAL=18

echo "=========================================="
echo "量子膜图片生成进度监控"
echo "=========================================="
echo ""

# 统计已生成图片数量
GENERATED=$(ls "$IMG_DIR"/*.png 2>/dev/null | wc -l | tr -d ' ')

echo "目标数量: $TOTAL 张"
echo "已生成: $GENERATED 张"
echo "待生成: $((TOTAL - GENERATED)) 张"
echo ""

# 计算进度百分比
PERCENT=$((GENERATED * 100 / TOTAL))
echo "进度: $PERCENT%"

# 显示进度条
echo -n "["
for i in $(seq 1 20); do
    if [ $((i * 5)) -le $PERCENT ]; then
        echo -n "="
    else
        echo -n " "
    fi
done
echo "]"
echo ""

# 显示已生成的文件
if [ $GENERATED -gt 0 ]; then
    echo "已生成的图片:"
    ls -1 "$IMG_DIR"/*.png 2>/dev/null | while read -r file; do
        filename=$(basename "$file")
        filesize=$(du -h "$file" | cut -f1)
        echo "  ✓ $filename ($filesize)"
    done
fi

echo ""
echo "=========================================="
