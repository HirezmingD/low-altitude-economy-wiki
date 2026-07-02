---
标题: ARROW 地面传感器无人机监视网络（英国Skyway）
类型: 实体
标签: [ARROW, Skyway, 英国, 地面传感器, 无人机走廊, 蜂窝网络, BT, Altitude Angel]
创建日期: 2026-07-01
更新日期: 2026-07-01
来源:
  - 原始素材/文章/Skyway低空高速公路  英国Skyway项目的总体介绍.md
国家/地区: 英国
部署区域: 英国南部/东南部，265km/6+2城市
---

# ARROW 地面传感器无人机监视网络（英国Skyway）

> **ARROW**（Automated Remote Recognition of Wildlife）——Altitude Angel开发的地面传感器网络，是英国Skyway低空高速公路的核心技术底座。★全球首个**地面传感器驱动**的无人机监视走廊——区别于日本（机载CNS驱动）、NASA（UTM管道协调）、GCC（分层飞行规则），开创第四种低空走廊范式。BT/EE 4G+5G公用蜂窝网络提供通信支撑，ARROW地面传感器+Skyports垂直起降场+集中UTM构成完整技术栈。

## 基本属性

| 属性 | 内容 |
|:---|:---|
| **名称** | ARROW（Automated Remote Recognition of Wildlife） |
| **开发商** | Altitude Angel |
| **所属项目** | 英国Skyway低空高速公路 |
| **走廊长度** | 265km |
| **覆盖城市** | 6+2（牛津/剑桥/雷丁/考文垂/米尔顿凯恩斯/克兰菲尔德 + 伯明翰/伦敦） |
| **通信方案** | ★BT/EE 4G+5G公用蜂窝网络 |
| **监视方案** | ★ARROW地面传感器网络（全球首个地面感知无人机走廊） |
| **集中UTM** | Altitude Angel集中UTM平台 |

## 核心能力

| 能力 | 功能描述 |
|:---|:---|
| **地面传感器监视** | ★全球首创——地面传感器网络替代机载/星基监视，实现低成本全覆盖 |
| **公用蜂窝通信** | BT/EE 4G+5G公用网络——无需专用航空通信基础设施 |
| **集中UTM协调** | Altitude Angel集中UTM——统一管理走廊内所有BVLOS飞行 |
| **线性走廊管理** | 265km线性空域→可预测容量+简化协调 |
| **Skyports集成** | 垂直起降场+地面传感器+蜂窝网络——三位一体 |

## 技术架构

```
            Skyway ARROW 技术栈
                    │
        ┌───────────┼───────────┐
        │           │           │
    地面感知层   通信层      UTM层
        │           │           │
   ARROW传感器  BT/EE 4G+5G  Altitude Angel
   （地面监视）  （公用蜂窝）   （集中UTM）
        │           │           │
   实时目标检测  数据回传      BVLOS管理
   低成本部署    现成网络      Skyports集成
```

## 四种走廊范式中的定位

| 范式 | 代表 | 感知方式 | 通信依赖 | 容量公式 |
|:---|:---|:---|:---|:---|
| ★ **地面感知** | ARROW/Skyway | ★地面传感器 | ★公用蜂窝 | $C_{linear}=v/s_{min}\times n_{lanes}\times\eta_{network}$ |
| **机载CNS** | 日本ConOps | 机载传感器 | 机载C2链路 | $C=f(L,s_{min},v,CNS_{threshold})$ |
| **UTM管道** | NASA/FAA | UTM协调 | UTM数据链 | $C_{pipe}=f(n_{pipes},s_{pipe})$ |
| **分层规则** | GCC | 分层隔离 | 飞行规则预定义 | $C_{layer}=f(n_{layers},s_{layer})$ |

## 与子课题3关联

| 维度 | 关联 |
|:---|:---|
| **f_network_reliability** | ★公用蜂窝可靠性→容量波动：$\eta_{network}=P(connectivity)\times(1-P(congestion))$——新增折减因子 |
| **线性容量公式** | $C_{linear}=v/s_{min}\times n_{lanes}\times\eta_{network}$——独立容量计算单元 |
| **低成本→快速部署** | 地面传感器+公用蜂窝→$t_{deploy}$短→$C(t)$增长起点早 |

## 相关页面

- [英国Skyway低空高速公路（实体）](知识库/摘要/应用案例/英国Skyway低空高速公路.md)
- [英国低空治理体系（实体）](/知识库/实体/国家地区/英国.md)
- [低空高速公路走廊（概念）](/知识库/概念/容量评估/低空高速公路走廊.md)

## 引用来源

- `原始素材/文章/Skyway低空高速公路  英国Skyway项目的总体介绍.md`
