from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
import os


def generate_visit_card(data):
    template_path = os.path.join(settings.BASE_DIR, "media", "template.png")

    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Shablon topilmadi: {template_path}")

    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Shrift yo‘lini tekshiramiz
    font_path = os.path.join(settings.BASE_DIR, "media", "arial.ttf")
    if not os.path.exists(font_path):
        font = ImageFont.load_default()
    else:
        font = ImageFont.truetype(font_path, 28)

    draw.text((506, 110), f"Phone: {data.get('phone', 'Noma’lum')}", fill="red", font=font)
    draw.text((506, 166), f"Pochta: {data.get('pochta', 'Noma’lum')}", fill="red", font=font)
    draw.text((550, 285), f"Manzil: {data.get('manzil', 'Noma’lum')}", fill="red", font=font)
    draw.text((550, 332), f"Email: {data.get('email', 'Noma’lum')}", fill="red", font=font)
    draw.text((550, 381), f"Company: {data.get('name_company', 'Noma’lum')}", fill="red", font=font)

    file_name = f"vizit_card_{data.get('name_company', 'unknown')}.png"
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    img.save(file_path)

    return settings.MEDIA_URL + file_name
