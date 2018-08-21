from os import listdir
from os.path import join, isfile, isdir
from typing import Tuple

# 导入图像转换模块
from PIL import Image
from resizeimage import resizeimage

# 导入默认路径
from dataset.shared import maybe_create_folder

class ImagenetResizer:
    '''图片大小转换的类'''
    def __init__(self, source_dir: str, dest_dir: str, verbose: int, skip: int):
        # 判断文件夹是否存在
        if not isdir(source_dir):
            raise Exception('Input folder does not exists: {}'.format(source_dir))
        self.source_dir = source_dir
        
        # 若输出文件夹不存在则创建
        # Destination folder
        maybe_create_folder(dest_dir)
        self.dest_dir = dest_dir
        
        # 是否启用啰嗦模式
        self.verbose = verbose
        
        #跳过文件
        self.skip = skip
        
    def resize_img(self, filename: str, size: Tuple[int, int] = (299, 299)):
        """
        Resizes the image using padding
        :param filename:
        :param size:
        """
        # 将图片缩放大小
        img = Image.open(join(self.source_dir, filename))
        orig_width, orig_height = img.size
        wanted_width, wanted_height = size
        ratio_w, ratio_h = wanted_width / orig_width, wanted_height / orig_height

        enlarge_factor = min(ratio_h, ratio_w)
        if enlarge_factor > 1:
            # Both sides of the image are shorter than the desired dimension,
            # so take the side that's closer in size and enlarge the image
            # in both directions to make that one fit
            enlarged_size = (int(orig_width * enlarge_factor), int(orig_height * enlarge_factor))
            img = img.resize(enlarged_size)

        # Now we have an image that's either larger than the desired shape
        # or at least one side matches the desired shape and we can resize
        # with contain
        res = resizeimage.resize_contain(img, size).convert('RGB')
        res.save(join(self.dest_dir, filename), res.format)

    def resize_all(self, size=(299, 299)):
        k = 0
        for filename in listdir(self.source_dir):
            # 如果文件存在的话
            if isfile(join(self.source_dir, filename)):
                # 如果启用啰嗦模式则打印log
                k = k + 1
                if (k < self.skip):
                    continue
                if (bool(self.verbose) == True):
                    #print(filename)
                    if (k % self.verbose == 0):
                        print(str(k) + ' pictures has been resized.')
                self.resize_img(filename, size)


# Run from the top folder as:
# python3 -m dataset.resize <args>
if __name__ == '__main__':
    import argparse # 导入参数模块
    from dataset.shared import dir_originals, dir_resized
    k = 0
    # Argparse setup
    parser = argparse.ArgumentParser(
        description='Resize images from a folder to 299x299')
    
    # 源文件夹
    parser.add_argument('-s', '--source-folder',
                        default=dir_originals,
                        type=str,
                        metavar='FOLDER',
                        dest='source',
                        help='use FOLDER as source of the images (default: {})'.format(dir_originals))
    # 目标文件夹
    parser.add_argument('-o', '--output-folder',
                        default=dir_resized,
                        type=str,
                        metavar='FOLDER',
                        dest='output',
                        help='use FOLDER as destination (default: {})'.format(dir_resized))
    # 打印log
    parser.add_argument('-v', '--verbose',
                        default=0,
                        type=int,
                        dest='verbose')
    
    # 跳过一定数量的图片(训练中故障恢复)
    parser.add_argument('-k', '--skip',
                        default=0,
                        type=int,
                        dest='skip')
    args = parser.parse_args()
    ImagenetResizer(args.source, args.output, args.verbose, args.skip).resize_all((299, 299))
