import fitz

def pdf2img(pdf_path, img_dir):
    doc = fitz.open(pdf_path)  # 打开PDF
    for page in doc:  # 遍历PDF的每一页
        zoom_x = 2.0  # 设置每页的水平缩放因子
        zoom_y = 2.0  # 设置每页的垂直缩放因子
        mat = fitz.Matrix(zoom_x, zoom_y)
        pix = page.get_pixmap(matrix=mat)
        pix.save(r"{}page-{}.jpg".format(img_dir, page.number))  # 保存

if __name__ == '__main__':
    pdf_path = "./source/bg1/龙虬庄——江淮东部新石器时代遗址发掘报告.pdf"
    img_dir = "./picture/LY/"
    pdf2img(pdf_path, img_dir)