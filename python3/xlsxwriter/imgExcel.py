from PIL import Image
import xlsxwriter
import numpy as np
import os, sys

book = xlsxwriter.Workbook('333.xlsx')
book_sheet = book.add_worksheet('demo')

del_img = []


def main():
    i = 0
    for root, dirs, files in os.walk('111'):
        for f in files:
            file_path = '111/' + f
            img = Image.open(file_path)
            new_img = img.resize((750, 120))
            new_file_path = '111/.' + f
            new_img.save(new_file_path)
            book_sheet.set_row(i, 100)
            book_sheet.set_column(0, 0, 120)
            book_sheet.insert_image(i, 0, new_file_path)
            i += 1
            del_img.append(new_file_path)
    book.close()


if __name__ == '__main__':
    main()
    for file in del_img:
        os.chmod(file, 755)
        os.remove(file)
