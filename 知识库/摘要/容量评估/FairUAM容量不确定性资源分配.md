---
标题: 需求与容量不确定性下的公平风险规避UAM资源分配
类型: 摘要
标签: [UAM, 容量不确定性, 资源分配, CVaR风险规避, 公平性, 两阶段随机规划]
创建日期: 2026-07-01
来源: [原始素材/论文/On a fair and risk‐averse urban air mobility resource allocation problem under demand and capacity uncertainties.md]
---

# 需求与容量不确定性下的公平风险规避UAM资源分配

> Sun L (VT), Deng H (GT), Peng Wei (GWU), Xie W (GT), Naval Research Logistics, 2024
> DOI: 10.1002/nav.22217 | 基金: NSF 2246414/2246417/2047390

## 一文总结

提出**FairUAM**两阶段随机规划模型：第一阶段分配飞行器资源，第二阶段在**空域容量**和**乘客需求**双重不确定性下公平分配地面与空中延误。NP-hard→MILP重构+有效不等式+Benders/L-shaped分解算法。CVaR风险规避确保最坏情况可控。真实网络数值验证：定制算法远超商用求解器。

## FairUAM模型架构

```
第一阶段：飞行器资源配置
    ↓
随机场景实现（容量+需求）
    ↓
第二阶段：公平延误分配
  - 地面延误（离场等待）
  - 空中延误（航路等待）
    ↓ CVaR风险规避
最小化最坏情况成本 + 公平性约束
```

## 关键技术特征

| 特征 | 实现 |
|------|------|
| 不确定性建模 | 容量=瓶颈点/时间单元随机变量 {low, high} |
| 风险度量 | CVaR (Conditional Value-at-Risk), ε=0.1 |
| 算法 | MILP+多族有效不等式+Benders/L-shaped分解 |
| 公平性 | 跨服务商的公平延误分配 |

## 容量不确定性设置

瓶颈点容量随机取值：
- 低容量场景：{1, 2} 架/时间单元
- 高容量场景：{2, 3} 架/时间单元

需求分为低/中/高三档，场景数5/10/20。

## 算法性能

| 指标 | 商业求解器 | FairUAM算法 |
|------|:--------:|:---------:|
| 小网络(20场景) | 3600s+ gap 6.8% | **0.2% gap** |
| 大网络(20场景) | gap 57.3% | **gap 10.2%** |

定制分解算法在所有实例上显著优于Gurobi直接求解。

## 与子课题3关联 ⭐⭐⭐

直接建模**空域容量不确定性**——将容量从"确定性瓶颈"升级为"随机变量"，为承载力评价提供不确定性量化框架。CVaR风险规避可对接到项目中的鲁棒承载力评估。

## 来源
- `原始素材/论文/On a fair and risk‐averse urban air mobility resource allocation problem under demand and capacity uncertainties.md`
