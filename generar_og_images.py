import os
from PIL import Image, ImageDraw, ImageFont

def get_font(name, size):
    font_path = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts', name)
    try:
        return ImageFont.truetype(font_path, size)
    except Exception:
        return ImageFont.load_default()

def create_pizzeria_angela_og(output_path, logo_path):
    W, H = 1200, 630
    img = Image.new('RGB', (W, H), color='#141110')

    # Ambient glows
    overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    ov_draw.ellipse([(-120, -120), (450, 450)], fill=(185, 28, 28, 75)) # Deep tomato red
    ov_draw.ellipse([(850, 250), (1450, 850)], fill=(217, 119, 6, 65))  # Warm pizza crust amber
    img.paste(overlay, (0, 0), overlay)

    draw = ImageDraw.Draw(img)

    # Logo Box on top left
    has_logo = os.path.exists(logo_path)
    if has_logo:
        # Rounded white container for square logo
        draw.rounded_rectangle([(80, 42), (200, 162)], radius=20, fill='#ffffff', outline='#d97706', width=2)
        try:
            logo = Image.open(logo_path).convert('RGBA')
            logo.thumbnail((106, 106), Image.Resampling.LANCZOS)
            lw, lh = logo.size
            pos_x = 80 + (120 - lw) // 2
            pos_y = 42 + (120 - lh) // 2
            img.paste(logo, (pos_x, pos_y), logo)
        except Exception as e:
            print("Pizzeria logo load error:", e)

    text_x = 225 if has_logo else 80

    # Top Italian Flag Ribbon
    draw.rectangle([(text_x, 48), (text_x + 30, 56)], fill='#15803d') # Green
    draw.rectangle([(text_x + 30, 48), (text_x + 60, 56)], fill='#f8fafc') # White
    draw.rectangle([(text_x + 60, 48), (text_x + 90, 56)], fill='#b91c1c') # Red

    font_sub_top = get_font('calibrib.ttf', 19)
    draw.text((text_x + 105, 43), "IL GUSTO DELL'ITALIA · IMAGINALIA (ALBACETE)", fill='#f59e0b', font=font_sub_top)

    # Title
    font_title = get_font('arialbd.ttf', 52)
    draw.text((text_x, 72), "PIZZERÍA ÁNGELA", fill='#ffffff', font=font_title)

    # Subtitle
    font_lead = get_font('arialbd.ttf', 25)
    draw.text((text_x, 132), "Sistema Propio de Pedidos WhatsApp & Horno KDS", fill='#fca5a5', font=font_lead)

    # Bullet points
    font_body = get_font('calibrib.ttf', 24)
    lines = [
        "• Bot interactivo de pedidos en WhatsApp con cobro Bizum / Stripe",
        "• Comandera digital KDS en cocina para horno de piedra (cero tickets perdidos)",
        "• Recepcionista de voz IA en hora punta: atiende pedidos por teléfono sin esperas"
    ]
    y = 200
    for line in lines:
        draw.text((80, y), line, fill='#f1f5f9', font=font_body)
        y += 42

    # Pill 1: Ahorro
    draw.rounded_rectangle([(80, 385), (550, 448)], radius=16, fill='#450a0a', outline='#b91c1c', width=2)
    font_pill = get_font('arialbd.ttf', 19)
    draw.ellipse([(102, 411), (114, 423)], fill='#ef4444')
    draw.text((125, 404), "SIN COMISIONES UBER EATS (Ahorro 30%)", fill='#fecaca', font=font_pill)

    # Pill 2: Subvención
    draw.rounded_rectangle([(570, 385), (1120, 448)], radius=16, fill='#064e3b', outline='#10b981', width=2)
    draw.ellipse([(592, 411), (604, 423)], fill='#10b981')
    draw.text((615, 404), "80% SUBVENCIONADO JCCM (Coste Real: 600€)", fill='#a7f3d0', font=font_pill)

    # Divider
    draw.line([(80, 492), (1120, 492)], fill='#292524', width=2)

    # Footer
    font_footer_brand = get_font('arialbd.ttf', 21)
    font_footer_url = get_font('calibrib.ttf', 22)
    draw.text((80, 528), "Altera Food · Inteligencia REAL aplicada a tu negocio", fill='#94a3b8', font=font_footer_brand)
    draw.text((650, 528), "Simulador: devai82.github.io/altera-food/", fill='#38bdf8', font=font_footer_url)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, 'PNG', optimize=True)
    print(f"Created: {output_path}")

def create_vibra_burger_og(output_path, logo_path):
    W, H = 1200, 630
    img = Image.new('RGB', (W, H), color='#080708')

    # Ambient glows
    overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    ov_draw.ellipse([(700, -120), (1450, 480)], fill=(219, 39, 119, 70)) # Neon magenta
    ov_draw.ellipse([(-120, 220), (480, 820)], fill=(245, 158, 11, 45))   # Warm amber burger
    img.paste(overlay, (0, 0), overlay)

    draw = ImageDraw.Draw(img)

    # Clean Dark Container for Vibra Logo
    draw.rounded_rectangle([(80, 42), (440, 162)], radius=20, fill='#000000', outline='#db2777', width=2)
    if os.path.exists(logo_path):
        try:
            logo = Image.open(logo_path).convert('RGBA')
            logo.thumbnail((330, 95), Image.Resampling.LANCZOS)
            lw, lh = logo.size
            pos_x = 80 + (360 - lw) // 2
            pos_y = 42 + (120 - lh) // 2
            img.paste(logo, (pos_x, pos_y), logo)
        except Exception as e:
            print("Vibra logo load error:", e)

    # Header text next to logo
    font_sub_top = get_font('calibrib.ttf', 19)
    draw.text((470, 52), "SMASH BURGERS & STREET FOOD · ALBACETE", fill='#fb7185', font=font_sub_top)

    font_title = get_font('arialbd.ttf', 44)
    draw.text((470, 78), "PEDIDOS PROPIOS & KDS", fill='#ffffff', font=font_title)

    font_lead = get_font('arialbd.ttf', 24)
    draw.text((470, 132), "Independencia Total de Last.app", fill='#f472b6', font=font_lead)

    # Bullet points
    font_body = get_font('calibrib.ttf', 24)
    lines = [
        "• Carta interactiva de smash burgers con selección de extras y salsas",
        "• Pantalla KDS en cocina: comandas en vivo clasificadas por plancha y delivery",
        "• Recepción de llamadas con Voz IA Dino (ElevenLabs HD) para dudas y pedidos"
    ]
    y = 200
    for line in lines:
        draw.text((80, y), line, fill='#f1f5f9', font=font_body)
        y += 42

    # Pill 1: Independencia Last.app
    draw.rounded_rectangle([(80, 385), (550, 448)], radius=16, fill='#500724', outline='#db2777', width=2)
    font_pill = get_font('arialbd.ttf', 19)
    draw.ellipse([(102, 411), (114, 423)], fill='#f43f5e')
    draw.text((125, 404), "SIN COMISIONES LAST.APP (Tarifa Cero)", fill='#fbcfe8', font=font_pill)

    # Pill 2: Subvención
    draw.rounded_rectangle([(570, 385), (1120, 448)], radius=16, fill='#064e3b', outline='#10b981', width=2)
    draw.ellipse([(592, 411), (604, 423)], fill='#10b981')
    draw.text((615, 404), "80% SUBVENCIONADO JCCM (Coste Real: 600€)", fill='#a7f3d0', font=font_pill)

    # Divider
    draw.line([(80, 492), (1120, 492)], fill='#292524', width=2)

    # Footer
    font_footer_brand = get_font('arialbd.ttf', 21)
    font_footer_url = get_font('calibrib.ttf', 22)
    draw.text((80, 528), "Altera Food · Inteligencia REAL aplicada a tu negocio", fill='#94a3b8', font=font_footer_brand)
    draw.text((650, 528), "Simulador: devai82.github.io/altera-food/", fill='#38bdf8', font=font_footer_url)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, 'PNG', optimize=True)
    print(f"Created: {output_path}")

def create_dental_sonrisastar_og(output_path, logo_path):
    W, H = 1200, 630
    img = Image.new('RGB', (W, H), color='#080e1d')

    # Ambient Cyan & Magenta medical glow
    overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    ov_draw.ellipse([(-120, -120), (480, 480)], fill=(2, 132, 199, 65))  # Cyan
    ov_draw.ellipse([(800, 200), (1450, 850)], fill=(226, 0, 119, 50))   # Magenta
    img.paste(overlay, (0, 0), overlay)

    draw = ImageDraw.Draw(img)

    # Clean Logo Container (white card on top left)
    draw.rounded_rectangle([(80, 42), (480, 162)], radius=20, fill='#ffffff', outline='#cbd5e1', width=2)
    if os.path.exists(logo_path):
        try:
            logo = Image.open(logo_path).convert('RGBA')
            logo.thumbnail((370, 100), Image.Resampling.LANCZOS)
            lw, lh = logo.size
            pos_x = 80 + (400 - lw) // 2
            pos_y = 42 + (120 - lh) // 2
            img.paste(logo, (pos_x, pos_y), logo)
        except Exception as e:
            print("Dental logo load error:", e)

    font_sub_top = get_font('calibrib.ttf', 19)
    draw.text((510, 52), "ODONTOLOGÍA INTEGRAL AVANZADA · ALBACETE", fill='#38bdf8', font=font_sub_top)

    font_title = get_font('arialbd.ttf', 44)
    draw.text((510, 78), "RECEPCIÓN IA 24/7", fill='#ffffff', font=font_title)

    font_lead = get_font('arialbd.ttf', 24)
    draw.text((510, 132), "Nueva Web Clínica & Citas Automatizadas", fill='#a5f3fc', font=font_lead)

    # Bullet points
    font_body = get_font('calibrib.ttf', 24)
    lines = [
        "• Asistente de voz ElevenLabs 24/7: atiende llamadas, explica tratamientos y filtra urgencias",
        "• Bot de WhatsApp y redes para agendamiento directo y recordatorio de citas",
        "• Nueva Web clínica de alta conversión integrada con CRM dental"
    ]
    y = 200
    for line in lines:
        draw.text((80, y), line, fill='#f1f5f9', font=font_body)
        y += 42

    # Pill 1: Cero llamadas perdidas
    draw.rounded_rectangle([(80, 385), (550, 448)], radius=16, fill='#082f49', outline='#0284c7', width=2)
    font_pill = get_font('arialbd.ttf', 19)
    draw.ellipse([(102, 411), (114, 423)], fill='#38bdf8')
    draw.text((125, 404), "RECEPCIÓN IA 24/7 (Cero Llamadas Perdidas)", fill='#bae6fd', font=font_pill)

    # Pill 2: Subvención
    draw.rounded_rectangle([(570, 385), (1120, 448)], radius=16, fill='#064e3b', outline='#10b981', width=2)
    draw.ellipse([(592, 411), (604, 423)], fill='#10b981')
    draw.text((615, 404), "80% SUBVENCIONADO BONO PYME (Coste Real: 600€)", fill='#a7f3d0', font=font_pill)

    # Divider
    draw.line([(80, 492), (1120, 492)], fill='#1e293b', width=2)

    # Footer
    font_footer_brand = get_font('arialbd.ttf', 21)
    font_footer_url = get_font('calibrib.ttf', 22)
    draw.text((80, 528), "Altera Dental · Inteligencia REAL aplicada a tu clínica", fill='#94a3b8', font=font_footer_brand)
    draw.text((650, 528), "Propuesta: www.altera-es.com/dental/", fill='#38bdf8', font=font_footer_url)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, 'PNG', optimize=True)
    print(f"Created: {output_path}")

if __name__ == '__main__':
    create_pizzeria_angela_og('g:/Mi unidad/Altera_food/og-pizzeria-angela.png', 'g:/Mi unidad/Altera_food/logo-angela.jpg')
    create_vibra_burger_og('g:/Mi unidad/Altera_food/og-vibra-burger.png', 'g:/Mi unidad/Altera_food/logo-vibra-clean.png')
    
    # Generate for Altera Dental in both repo locations
    create_dental_sonrisastar_og('G:/Mi unidad/Altera Dental/og-dental-sonrisastar.png', 'g:/Mi unidad/Altera_food/logo-sonrisa-clean.png')
    create_dental_sonrisastar_og('C:/Users/Usuario/altera-dental/og-dental-sonrisastar.png', 'g:/Mi unidad/Altera_food/logo-sonrisa-clean.png')
