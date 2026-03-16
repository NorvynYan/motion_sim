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
