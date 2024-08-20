from PIL import Image

# 打开3x3的图像
image = Image.open('./backdoor-toolbox/triggers/badnet_patch.png')

# 调整图像大小到5x5
resized_image = image.resize((8, 8), Image.NEAREST)

# 保存调整大小后的图像
resized_image.save('./backdoor-toolbox/triggers/badnet_patch_8x8.png')

# 显示调整大小后的图像
resized_image.show()
