import numpy as np
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt

class uav:
    def __init__(self,id,pos,vel,acc) -> None:
        self.id = id 
        self.pos = pos
        self.vel = vel
        self.acc = acc
    
    def control(self,command) -> None:
        pass
        
    def moveT(self,sampletime) -> None:
        self.vel = self.vel + self.acc*sampletime
        self.pos = self.pos + self.vel*sampletime

class multigen:
    def __init__(self):  
        self.uavs = []  
        self.num_uavs = np.random.randint(1,8) 

    def generate_uavs(self):  
        for i in range(0,self.num_uavs):  
            id = i + 1
            pos = np.array(np.random.rand(1,2)*100) #初始坐标随机化
            vel = np.array(np.random.rand(1,2)*2) #初始速度随机化
            acc = np.array(np.random.rand(1,2)*0) #初始加速度随机化
            u = uav(id,pos,vel,acc) 
            self.uavs.append(u) 
        return self.uavs     


if __name__ == '__main__':
    '''
    u1 = uav(1,np.array([0,0]),np.array([1,1]),np.array([0,0]))
    u2 = uav(2,np.array([5,5]),np.array([1,1]),np.array([-0.5,0.5]))
    for times in range(10):
        u1.moveT(1)
        u2.moveT(1)
    '''
    multi_uav = multigen()
    uavs = multi_uav.generate_uavs()
    [print(x.id,x.pos,end = '\n') for x in uavs]

    for t in range(16):
        for u in uavs:
            u.moveT(sampletime=0.5) #每个目标随采样时间运动，状态变化
        x_coords = [x.pos[0,0] for x in uavs]
        y_coords = [x.pos[0,1] for x in uavs]
        # 使用plot函数绘制点迹图  
        # 'o' 参数表示绘制的是圆形点  
        plt.plot(x_coords, y_coords, 'o',color = 'royalblue') 


    # 添加标题和坐标轴标签  
    plt.title('Point Trace Plot')  
    plt.xlabel('X Coordinates')  
    plt.ylabel('Y Coordinates')  
    # 显示图表  
    plt.grid(True)  # 可选：添加网格线  
    plt.show()