#!/usr/bin/env python3
# encoding: utf-8

import matplotlib.pyplot as plt

class Plot:
    image_size_x = 8
    image_size_y = 6
    title_size = 14
    label_size_x = 14
    label_size_y = 14

    def __init__(self):
        '''
        function: 初始化一个绘图实例
        '''
        plt.figure(num=1, figsize=(Plot.image_size_x, Plot.image_size_y))
        plt.cla()
        pass

    def reset(self):
        '''
        function: 清空绘图实例的待绘制内容
        '''
        plt.cla()
        return

    def add_line(self, x_data, y_data, label, line_style='--', marker='.', color='b'):
        '''
        function: 为绘图实例添加一个待绘制曲线
        x_data: x轴数据列表
        y_data: y轴数据列表(x_data与y_data需要等长)
        label: 单挑曲线的名称
        line_style: 曲线的形状
        marker: 采样点的形状
        color: 曲线颜色
        '''
        plt.plot(x_data, y_data, color=color, linestyle=line_style, marker=marker, label=label)
        return

    def multi_plot(self, file_path='./multi_plot.png', file_format='png', title='result', x_name='x-axis', y_name='y-axis'):
        '''
        function: 绘图实例将待绘制曲线全部绘制到图片文件
        file_path: 保存的图片文件路径
        file_format: 图片格式
        title: 图片内部的名称
        x_name: x轴名称
        y_name: y轴名称
        '''
        plt.title(title, size=Plot.title_size)
        plt.xlabel(x_name, size=Plot.label_size_x)
        plt.ylabel(y_name, size=Plot.label_size_y)
        plt.legend(loc='upper left')
        plt.savefig(file_path, format=file_format)
        return

    @staticmethod
    def single_plot(x_data, y_data, file_path='./single_plot.png', file_format='png', title='result', x_name='x-axis', y_name='y-axis', line_style='--', marker='.', color='b'):
        '''
        function: 绘制单一曲线到一张图片
        x_data: x轴数据列表
        y_data: y轴数据列表(x_data与y_data需要等长)
        file_path: 保存的图片文件路径
        file_format: 图片格式
        title: 图片内部的名称
        x_name: x轴名称
        y_name: y轴名称
        line_style: 曲线的形状
        marker: 采样点的形状
        color: 曲线颜色
        '''
        plt.figure(num=1, figsize=(Plot.image_size_x, Plot.image_size_y))
        plt.title(title, size=Plot.title_size)
        plt.xlabel(x_name, size=Plot.label_size_x)
        plt.ylabel(y_name, size=Plot.label_size_y)

        plt.plot(x_data, y_data, color=color, linestyle=line_style, marker=marker, label=title)

        plt.legend(loc='upper left')
        plt.savefig(file_path, format=file_format)
        return


if __name__ == '__main__':
    # 数据生成
    #xData = np.arange(0, 10, 1)
    #yData1 = xData.__pow__(2.0)
    #yData2 = np.arange(15, 61, 5)
    xData = [0, 1, 2, 3, 4, 5]
    yData1 = [0, 2, 4, 6, 8, 10]
    yData2 = [0, 3, 6, 9, 12, 15]

    # 单个函数静态打印
    Plot.single_plot(xData, yData1, file_path="./example/single_plot.png", file_format="png", title='result', x_name='x-axis', y_name='y-axis', line_style='--', marker='.', color='b')

    # 多函数打印
    pt = Plot()
    pt.reset()
    pt.add_line(xData, yData1, 'func1', line_style='-', marker='.', color='b')
    pt.add_line(xData, yData2, 'func2', line_style='--', marker='o', color='r')
    pt.multi_plot(file_path='./example/multi_plot.png', file_format='png', title='result', x_name='x-axis', y_name='y-axis')

