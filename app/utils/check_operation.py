def allowed_img_format(filename):
    # 设置允许的文件格式
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
