from PIL import Image


def overlay_image(background_path, overlay_path, output_path):
    # 打开背景图像和叠加图像
    background = Image.open(background_path).convert("RGBA")
    overlay = Image.open(overlay_path).convert("RGBA")

    # 获取背景图像的尺寸
    bg_width, bg_height = background.size

    # 获取叠加图像的尺寸
    overlay_width, overlay_height = overlay.size

    # 计算叠加图像的位置
    position = (bg_width - overlay_width, bg_height - overlay_height)

    # 创建一个空白的透明图像
    transparent = Image.new('RGBA', (bg_width, bg_height), (0, 0, 0, 0))

    # 将背景图像粘贴到透明图像上
    transparent.paste(background, (0, 0))

    # 将叠加图像粘贴到透明图像的指定位置上
    transparent.paste(overlay, position, overlay)

    # 保存结果图像
    transparent = transparent.convert("RGB")  # 如果不需要透明度，可以转换为RGB
    transparent.save(output_path)


# 示例调用
overlay_image('./triggers/badnet_patch_32.png',
              './triggers/badnet_patch_8x8.png',
              './backdoor-toolbox/triggers/badnet_patch_8x8_32.png')
