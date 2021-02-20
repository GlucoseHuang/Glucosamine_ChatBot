import Chat.Seq2Seq as RNN

states = [1, 1]
reply_dict = [None, None]
input_str = ['', '']

work_dir = RNN.works_dir


def reply(str_in):
    return RNN.predict(str_in)


if __name__ == "__main__":
    while True:
        print("-----------------")
        print("模式1：搭建模型")
        print("模式2：训练模型")
        print("模式3：进行对话")
        print("-----------------")
        mode = input('输入工作模式：')
        if mode == '1':
            RNN.pre_precess()
            RNN.setup_model()
        elif mode == '2':
            epo = input('输入循环轮数：')
            bat = input('输入batch size:')
            RNN.train_model(bat, epo)
        elif mode == '3':
            print('输入数字0退出')
            while True:
                str_in = input('你说：')
                if str_in == '0':
                    break
                print(RNN.predict(str_in))
