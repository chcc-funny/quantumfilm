#!/usr/bin/env python3
"""
量子膜网页图片批量生成脚本
使用 Replicate API (flux-schnell 模型)
生成18张品牌宣传图片
"""

import os
import replicate
import time

def batch_generate_images(image_configs, output_dir):
    """批量生成多张图片（自动处理限流）"""
    os.makedirs(output_dir, exist_ok=True)
    os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN", "")
    if not os.environ["REPLICATE_API_TOKEN"]:
        print("✗ 错误: 未设置 REPLICATE_API_TOKEN 环境变量")
        return

    total = len(image_configs)
    success = 0
    failed = 0
    failed_list = []

    print(f"开始批量生成 {total} 张图片...")
    print(f"输出目录: {output_dir}")
    print("=" * 80)

    for i, config in enumerate(image_configs, 1):
        print(f"\n[{i}/{total}] 生成: {config['name']}")
        print(f"提示词: {config['prompt'][:80]}...")
        output_path = os.path.join(output_dir, config['name'])

        try:
            output = replicate.run(
                "black-forest-labs/flux-schnell",
                input={
                    "prompt": config['prompt'],
                    "num_outputs": 1,
                    "aspect_ratio": config.get('aspect_ratio', '1:1'),
                    "output_format": "png",
                    "output_quality": 90
                }
            )

            if output and len(output) > 0:
                with open(output_path, 'wb') as f:
                    f.write(output[0].read())
                print(f"✓ 成功保存至: {output_path}")
                success += 1
            else:
                print("✗ 未能生成图片")
                failed += 1
                failed_list.append(config['name'])

        except Exception as e:
            error_msg = str(e)
            print(f"✗ 错误: {error_msg}")
            failed += 1
            failed_list.append(config['name'])

            # 如果是限流错误，额外等待
            if "429" in error_msg or "throttled" in error_msg.lower():
                print("⚠️  遇到限流，额外等待 20 秒...")
                time.sleep(20)

        # API 限流防护：每次请求间隔 12 秒
        if i < total:
            print("等待 12 秒后继续...")
            time.sleep(12)

    print("\n" + "=" * 80)
    print(f"生成完成！")
    print(f"成功: {success}/{total}")
    print(f"失败: {failed}/{total}")

    if failed_list:
        print(f"\n失败的图片:")
        for name in failed_list:
            print(f"  - {name}")

if __name__ == "__main__":
    # 检查依赖
    try:
        import replicate
    except ImportError:
        print("✗ 缺少依赖，请先安装: pip install replicate")
        exit(1)

    # 图片配置列表（共18张）
    image_configs = [
        # 【图01】Hero 主视觉横幅（16:9）
        {
            "name": "01_hero_banner.png",
            "aspect_ratio": "16:9",
            "prompt": "A sleek modern car windshield with premium window tint film being applied, glassmorphism style, cyan gradient light from light cyan #80E5F0 to deep teal #1E8A9A reflecting on the glass surface, clean white studio background, soft cyan diffused light from above, premium tech aesthetic, frosted glass texture, 3D render, 8K, minimal and modern, cinematic quality"
        },

        # 【图02】品牌背书·圣戈班历史徽章（1:1）
        {
            "name": "02_saint_gobain_badge.png",
            "aspect_ratio": "1:1",
            "prompt": "An elegant 3D badge or emblem representing 360 years of heritage, glassmorphism style, frosted cyan glass texture, light cyan to deep teal gradient, year \"1665\" engraved, floating on white background, soft cyan-teal shadow, premium luxury brand feel, 3D render, clean minimal"
        },

        # 【图03】技术图·10层磁控溅射膜层剖面（4:3）
        {
            "name": "03_10_layer_tech.png",
            "aspect_ratio": "4:3",
            "prompt": "A cross-section technical diagram of a 10-layer metallic sputtering window film, glassmorphism visualization, each layer shown as a translucent cyan-teal gradient glass sheet, floating layered structure, clean white background, cyan gradient labels, scientific precision aesthetic, 3D render, premium tech infographic style, light cyan to deep teal color scheme"
        },

        # 【图04】卖点图·SPF285+ 防晒护肤（1:1）
        {
            "name": "04_spf_protection.png",
            "aspect_ratio": "1:1",
            "prompt": "A 3D icon of UV rays being blocked by a translucent cyan glassmorphism shield, SPF protection visualization, sun rays hitting the glass barrier and dissipating, frosted cyan glass shield floating on white background, light cyan to deep teal gradient fill, soft cyan-teal shadow, clean minimal render, 8K"
        },

        # 【图05】卖点图·5G信号零干扰（1:1）
        {
            "name": "05_5g_signal.png",
            "aspect_ratio": "1:1",
            "prompt": "A 3D visualization of 5G signal waves passing freely through a thin glassmorphism window film panel, signal waves shown as flowing translucent lines in cyan teal color, frosted glass panel in center with light cyan to deep teal gradient, white clean background, cyan teal glow, tech-forward minimal style, 3D render"
        },

        # 【图06】卖点图·10年双重质保盾牌（1:1）
        {
            "name": "06_10year_warranty.png",
            "aspect_ratio": "1:1",
            "prompt": "A 3D premium shield icon with \"10\" text, glassmorphism style, frosted glass texture with cyan gradient from light cyan #80E5F0 to deep teal #1E8A9A, floating on white background, inner light edge highlight, certification badge aesthetic, soft cyan-teal drop shadow, 3D render, 8K"
        },

        # 【图07】卖点图·防爆安全厚度对比（1:1）
        {
            "name": "07_safety_thickness.png",
            "aspect_ratio": "1:1",
            "prompt": "A 3D comparison of two glass film layers side by side, one thick slab (3.0mil, premium) with deep teal glassmorphism glow, one thin slab (1.5mil) with light grey tone, clean white background, floating glass panels, safety and protection aesthetic, minimal tech style, cyan teal color accent, 3D render"
        },

        # 【图08】施工流程01·到店接待（4:3）
        {
            "name": "08_reception.png",
            "aspect_ratio": "4:3",
            "prompt": "A modern premium car window tinting shop interior, glassmorphism design elements on walls in cyan teal tones, clean minimalist white and teal decor, reception desk, professional ambiance, no people, photorealistic, soft studio lighting, premium service aesthetic"
        },

        # 【图09】施工流程02·玻璃检测（4:3）
        {
            "name": "09_inspection.png",
            "aspect_ratio": "4:3",
            "prompt": "Close-up of a gloved professional technician carefully inspecting an automotive windshield glass surface with a bright inspection light, clean workshop environment, cyan teal accent lighting, no text, photorealistic style, premium automotive service aesthetic"
        },

        # 【图10】施工流程03·无尘施工间（4:3）
        {
            "name": "10_clean_workshop.png",
            "aspect_ratio": "4:3",
            "prompt": "A clean professional automotive window tinting workshop room, dust-free environment, bright clean white walls, cyan teal LED accent lighting strips, empty car parking space in center, high-end garage aesthetic, glassmorphism elements on walls in teal tones, photorealistic, no people"
        },

        # 【图11】施工流程04·专业施工（4:3）
        {
            "name": "11_installation.png",
            "aspect_ratio": "4:3",
            "prompt": "Professional automotive technician in dark uniform carefully applying window tint film to a car side window, close-up detailed shot, clean workshop background, cyan teal premium lighting glow, gloved hands with squeegee tool, photorealistic, high-end service center aesthetic"
        },

        # 【图12】施工流程05·质检验收（4:3）
        {
            "name": "12_quality_check.png",
            "aspect_ratio": "4:3",
            "prompt": "Close-up of a professional quality inspection of newly applied window tint film, technician holding a bright inspection lamp against car window, checking for bubbles and edges, clean background, premium automotive service, photorealistic, cyan teal studio side lighting"
        },

        # 【图13】施工流程06·质保凭证（4:3）
        {
            "name": "13_warranty_card.png",
            "aspect_ratio": "4:3",
            "prompt": "A premium warranty card and invoice laid on a clean white surface, glassmorphism card design with cyan to deep teal gradient, elegant minimal flat lay, the card shows warranty information, soft drop shadows, top-down photography style, premium stationary aesthetic"
        },

        # 【图14】竞品对比概念图（16:9）
        {
            "name": "14_comparison.png",
            "aspect_ratio": "16:9",
            "prompt": "A sleek comparison visualization of two automotive window film samples, left film glowing with deep teal glassmorphism aura (10 layers, premium, thick), right film with light grey-blue tone (7 layers, standard, thin), clean white background, floating glass panels, scientific tech aesthetic, cyan teal accent glow on premium side, 3D render, no text"
        },

        # 【图15】产品展示·钻石系列膜样（1:1）
        {
            "name": "15_diamond_series.png",
            "aspect_ratio": "1:1",
            "prompt": "Close-up macro shot of premium automotive window tint film sample, diamond series, very light translucent cyan teal color, smooth surface with subtle metallic shimmer and depth reflection, glassmorphism inner glow, white background, studio lighting, premium product photography, high detail, 8K"
        },

        # 【图16】产品展示·水晶系列膜样（1:1）
        {
            "name": "16_crystal_series.png",
            "aspect_ratio": "1:1",
            "prompt": "Close-up macro shot of automotive window tint film sample, crystal series, highly transparent with a faint cyan tint, smooth glass-like surface with minimal haze, soft glassmorphism shimmer in teal tones, white background, clean studio lighting, premium product photography, 8K"
        },

        # 【图17】产品展示·炫影系列膜样（1:1）
        {
            "name": "17_fashion_series.png",
            "aspect_ratio": "1:1",
            "prompt": "Close-up macro shot of automotive window tint film sample, fashion series, medium dark teal translucent color, subtle metallic shimmer finish, stylish and modern aesthetic, glassmorphism surface glow in deep teal, white background, clean studio lighting, premium product photography, 8K"
        },

        # 【图18】选膜场景·家用车（16:9）
        {
            "name": "18_family_car.png",
            "aspect_ratio": "16:9",
            "prompt": "A modern family sedan car in bright outdoor setting with natural sunlight, front windshield and side windows showing premium window tint film with a subtle teal-cyan reflection, clean minimal background, no text, photorealistic CGI render, premium automotive aesthetic, soft teal light reflection on glass"
        }
    ]

    # 设置输出目录
    output_directory = "/Users/funnyliu/Documents/量子膜/量子膜-CHCC资料/量子膜-客户-介绍网页/generated_images"

    # 执行批量生成
    batch_generate_images(image_configs, output_directory)

    print("\n✓ 所有任务完成！")
    print(f"✓ 图片保存位置: {output_directory}")
