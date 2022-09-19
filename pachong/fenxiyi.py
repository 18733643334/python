import os, sys, shutil


def dd(d=None):
    print(d)
    sys.exit()


def main():
    path = 'wx_headimg/'
    res = os.listdir(path)
    for i in res:
        new_path = path + i
        dir_list = os.listdir(new_path)
        for d in dir_list:
            man = '男' in d
            shuai = '帅' in d
            try:
                if man:
                    man_path = path + '男'
                    if not os.path.exists(man_path):
                        os.makedirs(man_path)
                    shutil.copyfile(new_path + '/' + d, man_path + '/' + d)
                if shuai:
                    shuai_path = path + '帅'
                    if not os.path.exists(shuai_path):
                        os.makedirs(shuai_path)
                    shutil.copyfile(new_path + '/' + d, shuai_path + '/' + d)
            except:
                print(d)


if __name__ == '__main__':
    main()
    print(True)
