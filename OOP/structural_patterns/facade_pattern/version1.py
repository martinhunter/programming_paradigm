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

# 客户端代码
if __name__ == "__main__":
    light = Light()
    ac = AirConditioner()
    curtain = Curtain()

    # 回家模式
    light.on()
    ac.set_temperature(24)
    curtain.open()

    # 离家模式
    light.off()
    ac.set_temperature(18)
    curtain.close()
