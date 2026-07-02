---
标题: UAM高级UTM服务整体设计与仿真
类型: 摘要
标签: [UTM, UAM, 冲突解脱, 需求容量管理, 仿真框架, 空域复杂度]
创建日期: 2026-07-01
来源: [原始素材/论文/A Holistic Design and Simulation of Advanced UTM Services for Urban Air Mobility.md]
---

# UAM高级UTM服务整体设计与仿真

> IEEE Access, 2025 | AMU-LED项目 | 1600+飞行小时仿真

## 一文总结

提出**模块化UTM服务套件**（飞行前+飞行中），集成到统一仿真框架中进行协同测试。覆盖四大核心服务：战略冲突解脱(ScR)、战术冲突解脱(TcR)、需求容量管理(DCM)、空域复杂度评估。使用EUROCONTROL复杂度指标适配UTM场景。1600+飞行小时验证服务间依赖关系和关键性能。

## 框架架构

```
飞行前服务工具集              飞行中服务工具集
├─ 战略冲突解脱(ScR)           ├─ 战术冲突解脱(TcR)
├─ 需求容量管理(DCM)           ├─ 符合性监控
└─ 飞行计划验证               └─ 空域复杂度评估
        ↓                           ↓
        仿真引擎 → 模块化可替换测试平台
```

## 核心服务

| 服务 | 阶段 | 功能 |
|------|:--:|------|
| ScR | 飞行前 | 预离场冲突消除 |
| DCM | 飞行前 | 需求与可用容量平衡 |
| TcR | 飞行中 | 实时冲突检测与解脱 |
| 复杂度评估 | 飞行中 | EUROCONTROL ANS指标适配 |

## 关键创新

- 模块化可替换：算法可插拔，测试不同方案
- 服务间依赖量化：首次系统评估服务交互影响
- 空域复杂度基准：适配EUROCONTROL复杂度指标
- 1600+飞行小时验证

## 仿真生态

支持多种仿真引擎（BlueSky/Fe3/Gazebo/AirSim），研究使用AMU-LED项目数据验证。

## 与子课题3关联

需求容量管理(DCM)和空域复杂度评估直接对应承载力评价——提供了UTM框架中的容量-需求平衡机制和复杂度量化方法。

## 来源
- `原始素材/论文/A Holistic Design and Simulation of Advanced UTM Services for Urban Air Mobility.md`
