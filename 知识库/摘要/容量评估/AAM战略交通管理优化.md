---
标题: AAM战略交通管理集中式与分布式优化
类型: 摘要
标签: [AAM, 战略交通管理, 集中式优化, 分布式优化, 博弈论, 扇区划分]
创建日期: 2026-07-01
来源: [原始素材/论文/Centralized and distributed optimization of advanced air mobility strategic traffic management.md]
---

# AAM战略交通管理集中式与分布式优化

> Drone Systems and Applications, 2025

## 一文总结

首次同时建模AAM**集中式**和**分布式PSU**战略交通管理：①社区发现+Voronoi图扇区化空域，②加权Dijkstra走廊路径规划，③MIP集中式全网延迟最小化，④双层优化+合作博弈分布式协调。Monte Carlo仿真150/300架次三种机型，验证分布式方案在可扩展性上的优势。

## 三大技术贡献

### 1. 空域扇区化
- 社区发现算法 + Voronoi图 → 划分PSU管辖空域
- 考虑人口密度、vertiport容量、拓扑结构
- 避免单个PSU过载

### 2. 走廊路径规划
- 自定义加权Dijkstra算法
- 考虑走廊吞吐量容量 + vertiport起降容量
- 三种机型（多旋翼/倾转旋翼/升力巡航）+ 三级服务优先级

### 3. 集中式 vs 分布式

| 维度 | 集中式 | 分布式 |
|------|:------:|:------:|
| 模型 | MIP整数规划 | 双层博弈+MIP |
| 目标 | min全网延迟成本 | 各PSU优化+博弈协调 |
| 可扩展性 | 受限于求解规模 | 更优 |
| 公平性 | 全局统一 | 需博弈保证 |

## 仿真设置

| 参数 | 值 |
|------|-----|
| 地图 | 人工城市（随机禁飞区+人口密度图） |
| 机型 | 3种（多旋翼/倾转/升力巡航） |
| 架次 | 150 / 300 |
| 服务优先级 | 常规/快速/急救 |
| 蒙特卡洛 | 多次随机仿真 |

## 评估指标
- 优化成本（全网延迟）
- 求解运行时间（可扩展性）
- 平均离场延迟 + 空中延迟

## 与子课题3关联

走廊容量约束 + vertiport容量约束 → 直接对应承载力评价中的"通道容量"和"节点容量"双维度。混合整数规划框架可为容量优化提供数学基础。

## 来源
- `原始素材/论文/Centralized and distributed optimization of advanced air mobility strategic traffic management.md`
