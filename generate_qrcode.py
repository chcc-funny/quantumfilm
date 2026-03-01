#!/usr/bin/env python3
import qrcode

# 创建二维码实例
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# 添加 URL 数据
url = "https://quantumfilm.aicarengine.com"
qr.add_data(url)
qr.make(fit=True)

# 生成图片
img = qr.make_image(fill_color="black", back_color="white")

# 保存图片
img.save("quantumfilm_qrcode.png")
print(f"二维码已生成并保存为: quantumfilm_qrcode.png")
print(f"URL: {url}")
