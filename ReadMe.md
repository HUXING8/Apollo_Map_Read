### 转换proto文件
* 摘取Apollo工程下的/modules/common_msgs/map_msgs的地图proto文件，使用python的`protobuf`库进行序列化。
### 读取地图文件
* 地图文件为`.txt`格式，另有其他格式`.xml`,`.bin`文件，需要额外的读取方式。
* "apollo_map.txt"为apollo工程下的demo地图文件，"lane_segment.txt"为摘取自前者的一条lane的数据。
### 绘图
* 将序列化后的数据格式进行import导入，按照地图层级进行地图可视化绘制。

![map](./map_img.png)
