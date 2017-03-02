from PIL import ImageFont, Image, ImageDraw

# Text for months - CY and EN
months = [
  'Ionawr - January',
  'Chwefror - February',
  'Mawrth - March',
  'Ebrill - April',
  'Mai - May',
  'Mehefin - June',
  'Gorffennaf - July',
  'Awst - August',
  'Medi - September',
  'Hydref - October',
  'Tachwedd - November',
  'Rhagfyr - December'
]

# Loop through months
for month in months:
  font = ImageFont.truetype("../font/Veracity SSi Italic.ttf",30)
  img=Image.new("RGBA", (367,100),(255,255,255))
  draw = ImageDraw.Draw(img)
  draw.text((20, 35), month ,(0,0,0),font=font)
  draw = ImageDraw.Draw(img)
  img.save('../images/' + month + ".jpg")


# Loop through years 
# start at 1804 and loop until we reach 1920
year = 1804  
for i in range(116):
  year_text = str(year + i)
  font = ImageFont.truetype("../font/Veracity SSi Italic.ttf",30)
  img=Image.new("RGBA", (367,100),(255,255,255))
  draw = ImageDraw.Draw(img)
  draw.text((20, 35), year_text ,(0,0,0),font=font)
  draw = ImageDraw.Draw(img)
  img.save('../images/' + year_text + ".jpg")