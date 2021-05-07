import random


class PhoneNum:
    def dianXin(self):
        # 随机生成电信号码
        header = [133, 149, 153, 173, 177, 180, 181, 189, 191, 199]
        phone = str(random.choice(header)) + "".join(random.choices("0123456789",k=8))
        return phone

    def lianTong(self):
        # 随机生成联通号码
        header = [130, 131, 132, 145, 155, 156, 166, 171, 175, 176, 185, 186]
        phone = str(random.choice(header)) + "".join(random.choices("0123456789",k=8))
        return phone

    def yiDong(self):
        # 随机生成移动号码
        header = [135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158, 159, 172,
                  178, 182, 183, 184, 187, 188, 198]
        phone = str(random.choice(header)) + "".join(random.choices("0123456789",k=8))
        return phone
    def dataId(self):
        count = 0
        dataId = str()
        for count in range(3):
            count += 1
            dataId += random.choice("".join(chr(i) for i in range(65, 91))) + random.choice("0123456789")
        return  dataId
    def address(self):
        addressHeard = "".join(random.choices("".join(chr(i) for i in range(65, 91)), k=2))
        addressbody="".join(random.choices("0123456789",k=3))
        address=addressHeard+addressbody
        return address