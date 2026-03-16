
**Mar 16 PM**

完成以下工作：

* 完成 `algorithms/pid.py`，实现横向PD控制（航向角误差+横向偏差）和纵向P控制
* 完成 `visualizer.py`，实现matplotlib实时动画，包含参考路径、历史轨迹、车辆朝向箭头
* 完成 `main.py`，组装所有模块，while循环驱动仿真
* 完成 `test/test_pid.py`，静态轨迹对比验证
* 调参过程发现：仿真环境下纯 `kp_yaw`效果最好，加 `kp_d`和 `kd_yaw`反而互相干扰，最终参数 `kp_yaw=9.0`，其余置零
* 路径增加终点检测，`get_reference`返回 `None`时仿真停止

**经验总结：**

* 增益不是越多越好，够用就行
* 仿真无噪声无扰动，D项和多误差叠加容易过调
* 实车调参和仿真调参结果不同，根本原因是真实系统有噪声、延迟和非线性

**待完成：**

* Stanley控制器
* MPC控制器
* 圆形路径
* CARLA C++项目



**Mar 16 AM**

项目初始化，完成以下工作：

* 确定项目定位：模块化运动控制仿真框架，策略模式解耦模型/算法/路径三层
* 创建GitHub公开仓库 `motion_sim`，MIT协议
* 搭建项目目录结构：`models/`、`algorithms/`、`paths/`、`test/`
* 完成三个抽象基类：`BaseModel`、`BaseAlgorithm`、`BasePath`
* 完成运动学自行车模型：`BicycleModel`，状态量 `[x, y, yaw, v]`
* 完成L形路径：`LShapePath`，含圆弧过渡，间距0.1m，路径验证通过
* 配置 `.gitignore`，忽略 `.venv/`、`__pycache__/`、`test/`

**待完成：**

* `algorithms/pid.py`
* `visualizer.py`
* `main.py`
