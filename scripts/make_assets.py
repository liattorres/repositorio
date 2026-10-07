import os
import subprocess
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow', '--quiet'])
    from PIL import Image, ImageDraw, ImageFont

root = r"C:\Users\liatt\repositorio.worktrees\evoluc-a-o-e-responsividade-com-bootstrap-da\img"
os.makedirs(root, exist_ok=True)

# Desktop preview
w, h = 1400, 900
img = Image.new('RGB', (w, h), '#f3f6fb')
draw = ImageDraw.Draw(img)

draw.rounded_rectangle((0, 0, w, 110), radius=20, fill='#16213d')
draw.text((70, 38), 'DashBoard Pro', fill='white', font=ImageFont.truetype('arial.ttf', 40))
for x, label in [(890,'Início'),(980,'Sobre'),(1070,'Benefícios'),(1215,'Contato')]:
    draw.text((x, 42), label, fill=(220,230,255), font=ImageFont.truetype('arial.ttf', 20))
draw.rounded_rectangle((70, 150, 980, 680), radius=28, fill='white')
draw.rounded_rectangle((980, 150, 1330, 680), radius=28, fill='#eef5ff')
draw.rounded_rectangle((110, 210, 560, 360), radius=18, fill='#dfeaff')
draw.text((145, 245), 'Atividade', fill='#1d4ed8', font=ImageFont.truetype('arial.ttf', 26))
for i, val in enumerate([95,120,160,135,200,185,220]):
    x = 130 + i*60
    y = 430 - val
    draw.rectangle((x, y, x+32, 430), fill='#5a8bff')
draw.rounded_rectangle((610, 220, 930, 320), radius=16, fill='#f8fafc')
draw.text((650, 245), 'Métricas', fill='#1e293b', font=ImageFont.truetype('arial.ttf', 22))
for i, txt in enumerate(['+42%', '+18%', '+9%']):
    draw.rounded_rectangle((650 + i*120, 310, 730 + i*120, 360), radius=12, fill='#e0ecff')
    draw.text((670 + i*120, 323), txt, fill='#1d4ed8', font=ImageFont.truetype('arial.ttf', 18))
draw.text((112, 520), 'Acompanhe seu negócio com clareza e rapidez.', fill='#0f172a', font=ImageFont.truetype('arial.ttf', 38))
draw.text((112, 630), 'Dashboard para monitorar vendas, produtividade e decisões em tempo real.', fill='#475569', font=ImageFont.truetype('arial.ttf', 22))
stat_y = 200
for idx, (txt, val) in enumerate([('Usuários', '24k'), ('Satisfação', '89%'), ('Vendas', '1.8M'), ('Notas', '4.9/5')]):
    draw.rounded_rectangle((1010, stat_y + idx*110, 1290, stat_y + idx*110 + 82), radius=20, fill='white')
    draw.text((1045, stat_y + idx*110 + 22), val, fill='#16213d', font=ImageFont.truetype('arial.ttf', 30))
    draw.text((1045, stat_y + idx*110 + 56), txt, fill='#475569', font=ImageFont.truetype('arial.ttf', 19))
for i, (title, text) in enumerate([('Relatórios claros', 'Dados claros'), ('Estratégia em tempo real', 'Ações rápidas'), ('Ações mais rápidas', 'Projetos em foco')]):
    x = 70 + i*430
    draw.rounded_rectangle((x, 730, x+380, 880), radius=20, fill='white')
    draw.rounded_rectangle((x+22, 748, x+358, 810), radius=14, fill='#dfeaff')
    draw.text((x+38, 828), title, fill='#16213d', font=ImageFont.truetype('arial.ttf', 24))
    draw.text((x+38, 860), text, fill='#475569', font=ImageFont.truetype('arial.ttf', 18))
img.save(os.path.join(root, 'desktop.png'))

# Mobile preview
w, h = 430, 930
img = Image.new('RGB', (w, h), '#eef5ff')
draw = ImageDraw.Draw(img)
draw.rounded_rectangle((0, 0, w, 120), radius=18, fill='#16213d')
draw.text((20, 40), 'DashBoard Pro', fill='white', font=ImageFont.truetype('arial.ttf', 24))
draw.rounded_rectangle((20, 150, 390, 500), radius=24, fill='white')
draw.rounded_rectangle((40, 180, 370, 430), radius=16, fill='#dfeaff')
draw.text((55, 220), 'Acompanhe seu negócio', fill='#0f172a', font=ImageFont.truetype('arial.ttf', 24))
draw.text((55, 350), 'Produtividade +42%', fill='#1d4ed8', font=ImageFont.truetype('arial.ttf', 20))
draw.text((55, 385), 'Vendas +18%', fill='#1d4ed8', font=ImageFont.truetype('arial.ttf', 20))
for i, (label, val) in enumerate([('Usuários','24k'),('Satisfação','89%'),('Vendas','1.8M')]):
    y = 530 + i*110
    draw.rounded_rectangle((20, y, 390, y+90), radius=18, fill='white')
    draw.text((45, y+23), val, fill='#16213d', font=ImageFont.truetype('arial.ttf', 28))
    draw.text((45, y+58), label, fill='#475569', font=ImageFont.truetype('arial.ttf', 18))
draw.rounded_rectangle((0, 840, w, h), radius=18, fill='#0f172a')
draw.text((30, 870), 'Instagram', fill='white', font=ImageFont.truetype('arial.ttf', 18))
draw.text((150, 870), 'LinkedIn', fill='white', font=ImageFont.truetype('arial.ttf', 18))
draw.text((285, 870), 'Facebook', fill='white', font=ImageFont.truetype('arial.ttf', 18))
img.save(os.path.join(root, 'mobile.png'))
print('ok')
