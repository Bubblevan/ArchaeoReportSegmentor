import pdf_to_image
import paddle_ocr_process
import llm_summary

def main():
    # PDF 转图片
    pdf_path = "./source/小兜里.pdf"
    img_dir = "./picture/D/"
    pdf_to_image.pdf2img(pdf_path, img_dir)

    # 调用 PaddleOCR 获取文字
    # folder_path = './picture/'
    # result_folder = './ocr_result/'
    # paddle_ocr_process.process_images(folder_path, result_folder)

    # 调用 LLM 进行总结分类
    # llm_summary.process_ocr_results()

if __name__ == '__main__':
    main()