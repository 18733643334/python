import xlsxwriter
from PIL import Image

img = Image.open('20200818/1596616898432.jpg')
newSizeImg = img.resize((218, 75))
newSizeImg.save('111.jpg', 'JPEG')

book = xlsxwriter.Workbook('333.xlsx')
book_sheet = book.add_worksheet('demo')
book_format = book.add_format()
book_format.set_align('center')
book_sheet.set_row(0, 70)
book_sheet.set_column(0, 0, 30)
book_sheet.insert_image(0, 0, '111.jpg')
book_sheet.set_row(1, 70)
book_sheet.insert_image(1, 0, '111.jpg')
book.close()
