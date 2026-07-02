---
标题: SGPS空间网格划分冲突检测
类型: 概念
标签: [SGPS, 网格划分, 冲突检测, 时间窗网格, 哈希表]
创建日期: 2026-07-01
来源: [原始素材/论文/A Medium-Term Conflict Detection and Resolution Method for Open Low-Altitude City Airspace Based on Temporally and Spatially Integrated Strategies.md]
---

# SGPS空间网格划分冲突检测

## 定义

Yang等(2020)提出的空间网格划分系统(SGPS)：将连续空域离散化为均匀立方网格，用哈希表+布尔占用表替代传统逐对航点比较，将冲突检测从O(n²)降至近线性复杂度。

## 四步方法

### 1. 边界特征向量BFV
```
BFV = (Lat_min, Lat_max, Lon_min, Lon_max, Alt_min, Alt_max)
```
定义运行空域的范围边界，处理180°经线跨越。

### 2. 均匀网格划分
- 等距网格替代圆柱安全包络
- 轴对齐立方体→简化包含测试
- 网格标签lpg = i + Nx·j + Nx·Ny·k

### 3. 时间窗网格TWG
每航迹经过的每个网格记录：
```
TWG_i^j = (lpg, RP_in, RP_out)
```
- RP_in: 最早进入航点
- RP_out: 最晚离开航点

### 4. 双存储结构
| 结构 | 功能 |
|------|------|
| 哈希表 | 航迹→TWG链表，O(1)索引 |
| 布尔占用表BT | 预筛选：哪条航迹经过哪个网格 |

## 冲突检测逻辑

两航迹TY_a, TY_b冲突当且仅当：
1. 同网格标签（spatial co-occupancy）
2. 时间窗重叠：
   - RP_in^b.t ≤ RP_in^a.t ≤ RP_out^b.t 或
   - RP_in^a.t ≤ RP_in^b.t ≤ RP_out^a.t

冲突时间：[max(RP_in^a.t, RP_in^b.t), min(RP_out^a.t, RP_out^b.t)]

## 性能特征

- 复杂度从O(n²)降至~O(n)（仅检测同网格航迹对）
- 哈希碰撞概率∝网格分辨率
- 连续同冲突网格自动合并→消除重复

## 与空域承载力的关系

SGPS网格化→可直接作为承载力评价的空间离散单元。网格分辨率的选取直接影响冲突检测精度和容量评估粒度。

## 来源
- Yang et al. IEEE TCST, 2020
