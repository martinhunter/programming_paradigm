# 灯光类
class Light:
    def on(self):
        print("Light is on")

    def off(self):
        print("Light is off")

# 空调类
class AirConditioner:
    def set_temperature(self, temperature):
        print(f"Air conditioner set to {temperature}°C")

# 窗帘类
class Curtain:
    def open(self):
        print("Curtain is open")

    def close(self):
        print("Curtain is closed")

# 外观类
class SmartHomeFacade:
    def __init__(self):
        self.light = Light()
        self.ac = AirConditioner()
        self.curtain = Curtain()

    def coming_home_mode(self):
        self.light.on()
        self.ac.set_temperature(24)
        self.curtain.open()

    def leaving_home_mode(self):
        self.light.off()
        self.ac.set_temperature(18)
        self.curtain.close()

    def sleep_mode(self):
        self.light.off()
        self.ac.set_temperature(22)
        self.curtain.close()

    def wake_up_mode(self):
        self.light.on()
        self.ac.set_temperature(24)
        self.curtain.open()

# 客户端代码
if __name__ == "__main__":
    facade = SmartHomeFacade()

    # 回家模式
    facade.coming_home_mode()

    # 离家模式
    facade.leaving_home_mode()

    # 睡眠模式
    facade.sleep_mode()

    # 起床模式
    facade.wake_up_mode()
