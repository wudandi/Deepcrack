import os

def main():
    train_image()
    val_image()

def train_image():
    with open("D:\\deepL\\deepcrack\\DeepCrack\\codes\\data\\train_example.txt", 'r+') as file:
        file.truncate(0)
    
    image_filePath = 'D:\deepL\crackImage\cracktree\image'
    gt_filePath = 'D:\deepL\crackImage\cracktree\gt'
    image_list = os.listdir(image_filePath)
    gt_list = os.listdir(gt_filePath)
    for image_name,gt_name in zip(image_list,gt_list):
        # "a"表示以不覆盖的形式写入到文件中,当前文件夹如果没有"save.txt"会自动创建
        with open("D:\\deepL\\deepcrack\\DeepCrack\\codes\\data\\train_example.txt","a") as f:
            f.write(image_filePath+"\\"+image_name +" "+ gt_filePath+"\\"+gt_name +"\n")
        f.close()

def val_image():
    with open("D:\\deepL\\deepcrack\\DeepCrack\\codes\\data\\val_example.txt", 'r+') as file:
        file.truncate(0)
    
    image_filePath = 'D:\deepL\crackImage\CrackLS315\CrackLS315_image'
    gt_filePath = 'D:\deepL\crackImage\CrackLS315\CrackLS315_gt'
    image_list = os.listdir(image_filePath)
    gt_list = os.listdir(gt_filePath)
    for image_name,gt_name in zip(image_list,gt_list):
        # "a"表示以不覆盖的形式写入到文件中,当前文件夹如果没有"save.txt"会自动创建
        with open("D:\\deepL\\deepcrack\\DeepCrack\\codes\\data\\val_example.txt","a") as f:
            f.write(image_filePath+"\\"+image_name +" "+ gt_filePath+"\\"+gt_name +"\n")
        f.close()


if __name__ == '__main__':
    main()