import matplotlib.pyplot as plt

def create_empty_3d_grid(x_range=(0, 10), y_range=(0, 10), z_range=(0, 10)):
    # 创建一个图形窗口
    fig = plt.figure(figsize=(8, 6))
    
    # 添加一个 3D 类型的子图
    ax = fig.add_subplot(111, projection='3d')
    
    # 设置三个轴的范围
    ax.set_xlim(x_range)
    ax.set_ylim(y_range)
    ax.set_zlim(z_range)
    
    # 设置轴标签
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # 开启网格（默认通常是开启的，这里显式调用）
    ax.grid(True)
    
    plt.title("Empty 3D Coordinate Grid")
    plt.show()

# 调用函数生成网格
create_empty_3d_grid()