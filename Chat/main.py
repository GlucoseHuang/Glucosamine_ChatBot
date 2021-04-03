"""
本文件中的代码来源于：
    https://github.com/Dimsmary/Ossas_ChatBot
"""

import Chat.RNN_model as RNN

states = [1, 1]
reply_dict = [None, None]
input_str = ['', '']

work_dir = RNN.works_dir


def reply(str_in):
    return RNN.predict(str_in)


if __name__ == "__main__":
    while True:
        print("-----------------")
        print("1：搭建模型")
        print("2：训练模型")
        print("3：进行对话")
        print("-----------------")
        mode = input('输入选项：')
        if mode == '1':
            RNN.pre_precess()
            RNN.setup_model()
        elif mode == '2':
            epo = input('循环轮数：')
            bat = input('batch size:')
            RNN.train_model(bat, epo)
        elif mode == '3':
            print('输入数字0退出')
            while True:
                str_in = input('你说：')
                if str_in == '0':
                    break
                print(RNN.predict(str_in))
