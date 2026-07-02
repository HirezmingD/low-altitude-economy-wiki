---
title: "HTML阅读-基于CNN-ConvLSTM的城市低空空域复杂度建模与预测"
source: "https://kns.cnki.net/reader/xml?invoice=Cr64%2F2k%2BF4%2FQEocKENGdXu392xoJ15gczYs96NTZOWMCzrDBWjLSJ56%2B7bONwkcFqrUS8Wfl8OnRbz%2Bk2oTIJd1sK1JH%2F9n2OZBaXZ0P%2FK6bGy7Xb0K91lDVVduny78VQKnTqhXWxFuuUWpoxeagZiv%2B9D0gp7ubkXrcILh129U%3D&platform=NZKPT&sourcetype=nxgp&product=CAPJ&filename=XTFZ20260424006&tablename=capjlast&type=JOURNAL&scope=readonline&cflag=html&dflag=xml&pages=&language=CHS&trial=&nonce=7D03FA4D6F3C4D108D622ED4E404509E&loginType=trialRead"
author:
  - "[[解决无障碍阅读Errors]]"
published:
created: 2026-06-29
description:
tags:
  - "clippings"
---
## 基于CNN-ConvLSTM的城市低空空域复杂度建模与预测

(期刊) [系统仿真学报](https://navi.cnki.net/knavi/detail?p=UlMsFNOcQSn0X5Bbzt0O2OV4IiaXSZez4BoTfChUpDTyG1Ql7nbGnZ_IHkoxtezOF8CDLVtVfejhdCn3LwCWvbpDv57ef0g5Fx31K1FmA9s=&uniplatform=NZKPT&language=CHS "系统仿真学报")

欢迎浙江大学图书馆

目录图表

0引言

1 低空异构空域复杂度建模

1.1 问题描述与假设

1.1.1 问题描述

1.1.2 模型假设

1.1.3 符号说明

1.2 分层空域状态表征

1.2.1 复杂度定义

1.2.2 八通道空域特征

1.3 预测任务与技术路线

1.3.1 任务定义

1.3.2 技术路线图

2 基于CNN-ConvLSTM的复杂度预测仿真模型

2.1 模型整体架构

2.1.1 架构设计

2.1.2 模块功能

2.1.3 预测策略

2.2 网络结构设计

2.2.1 空间编码器

2.2.2 ConvLSTM时序建模器

2.2.3 未来预测器与解码器

2.3 训练设置

2.3.1 损失函数

2.3.2 评估指标

3 仿真实验验证与分析

3.1 实验设置

3.1.1 数据集配置

3.1.2 实验环境与参数配置

3.1.3 对比方法

3.2 性能对比与分析

3.2.1 整体性能对比

3.2.2 时域退化分析

3.3 模型分析与讨论

3.3.1 消融实验

3.3.2 分层异构复杂度预测性能

3.3.3 空间预测误差分布

3.3.4 实时性与鲁棒性评估

4 结论

参考文献

![CNKI](https://kns.cnki.net/reader/img/CNKILogo.39d0187b.png)

(期刊) [系统仿真学报](https://navi.cnki.net/knavi/detail?p=UlMsFNOcQSn0X5Bbzt0O2OV4IiaXSZez4BoTfChUpDTyG1Ql7nbGnZ_IHkoxtezOF8CDLVtVfejhdCn3LwCWvbpDv57ef0g5Fx31K1FmA9s=&uniplatform=NZKPT&language=CHS "系统仿真学报")

## 基于CNN-ConvLSTM的城市低空空域复杂度建模与预测

- [郑州航空工业管理学院民航学院](https://kns.cnki.net/kcms2/organ/detail?v=myyot3CgzEoZgWsS0-9-FF0BWQ--eKq4PnFz7OSWzfmquHBmVcMYLxliL-VmXyjN5ZuuYwWrAdkILBD9uFHb2r8N7zXTyfRM9wyLuI6znxx0xDwriJLHD4H_qmPHVr4zMQ4OxH1kj-7GgkLKsbLgR83eEfupNTTkv952UCK7xOjJSdbhpxzuvdC-kwCS7bWad_m5sOJtKbhNNYTGQu7Kmvy8M_DPg5UMeqmmEBn4EqJgV7xeHlpm6rzaYV1-MBwY&uniplatform=NZKPT&language=CHS)

摘要:

针对城市低空空域中标准性能飞行器（Standard-Performance Vehicle, SPV）与高性能飞行器（High-Performance Vehicle, HPV）并发运行场景下的复杂度预测问题， *提出一种分层异构复杂度（* *Stratified* *Heterogeneous Complexity,* *SHC* *）预测框架* 。 *以八通道网格状态特征为输入（由分层密度、速度、航向等统计量构成* *），* *采用卷积神经网络（* *Convolutional* *Neural Network,* *CNN* *）进行空间编码，并利用卷积长短期记忆网络（* *Convolutional* *Long Short* - *Term Memory, ConvLSTM* *）进行时序建模，直接预测未来* *180 s* *预测时域内的* *SPV* *层复杂度、* *HPV* *层复杂度及跨层交互复杂度三个分量场* 。在BlueSky仿真的典型城市场景数据集上，模型的MAE和R²分别为0.0045和0.870，端到端推理延迟为26.1 ms，满足5 s采样间隔下的实时性要求。消融实验表明，ConvLSTM时序建模与分层多输出预测是性能提升的主要来源。

基金:[河南省哲学社会科学规划年度项目(2023BJJ091);](https://kns.cnki.net/kcms2/fund/detail?v=myyot3CgzEoZgWsS0-9-FM0wm5hH6k4eccbMiQ6CniKM8HCl-n9DnvvbhzFpRqIlPg4Ib88Z8NTjVNKoM6kcv2VOYKfD1i-YGL7XFiNIRH1cR7DoJ1-HJX4bHp5Dj4nZejv3vfDvXRA1_08gRVF3YDajs7SIhaGWjvjzAgC5UQrIHVqcVSsSOsTjUW51UBik9dKBLf7_salCihHyOhxI7hsNE4WX8VUhmFAykUr5fLCBG-Afm3_79f0Ens5MjFURO8nxPuvmakrGbqsE3WoWsTvBQFnoxpSp&uniplatform=NZKPT&language=CHS)[河南省高等学校重点科研项目（26B580011）](https://kns.cnki.net/kcms2/fund/detail?v=myyot3CgzEoZgWsS0-9-FLUGYR2jJRy7kc02ZFCoida8plclYdbMp4anZ2nNw2heDJtD-qJgIqyJ-82abhKHfX3xrMF8QNVpJ6uqsbQwaIACVDS9gvNHayOU7ckijGlb9lhSdYlBY2YXLk56GiEiEqyYv9P8fA8YVjxxGonYbzq4DYuwPV6DZGasMR7dRYk6GLwVMnvyKyHkp8ga0ZSZ5Z2fSo7oZIbC61-1FVCM321M2qFfNQMQPOLF-Kl4kg4uw9Z8ZIsML0mUihFevN_Qyw==&uniplatform=NZKPT&language=CHS)

作者简介:张云景(1983-)，男，讲师，博士，研究方向为交通运输;

收稿日期:2026-01-22

## Urban Low-altitude Airspace Complexity Modeling and Prediction Based on CNN-ConvLSTM

- Zhang Yunjng
- Wang Hao
- Yang Minghui
- Zhengzhou University of Aeronautics, Civil Aviation College

Abstract:

To address the complexity prediction problem in the layered scenario of concurrent operations between Standard-Performance Vehicles (SPV) and High-Performance Vehicles (HPV) in urban low-altitude airspace, *a Stratified Heterogeneous Complexity (SHC) prediction framework is proposed*. *The model takes eight* - *channel gridded state features (derived from layer* - *wise density, speed, and headi* *ng statistics) as input, uses Convolutional Neural Network (CNN) for spatial encoding and Convolutional Long Short* - *Term Memory (**ConvLSTM**) for temporal modeling, and directly predicts three complexity component fields over a 180 s prediction horizon: SPV* - *la* *yer complexity, HPV* - *layer complexity, and cross* - *layer interaction complexity*. On a typical urban dataset simulated in BlueSky, the model achieves an MAE of 0.0045 and an R² of 0.870, with an end-to-end inference latency of 26.1 ms, satisfying the real-time requirement of a 5 s sampling interval. Ablation studies show that ConvLSTM-based temporal modeling and hierarchical multi-output prediction are the main sources of performance gains.

Received:2026-01-22

## 0引言

近年来，低空经济已成为我国战略性新兴产业。2024年，“低空经济”首次写入全国政府工作报告，被纳入新质生产力范畴；2026年全国两会进一步将低空经济站位提升至新兴支柱产业，并与集成电路、航空航天、生物医药并列。此外，31个省份也将低空经济相关内容写入了地方政府的工作报告。蒲钒等人将数字低空融合运行需要构建的从信息基础设施到交通协同调控的完整体系进行了研究，其核心观点指出现在空域态势感知与复杂度评估是支撑低空安全运行的关键环节 <sup><a type="reference">[1]</a></sup> 。在此背景下，物流无人机（Unmanned Aerial Vehicle, UAV）与电动垂直起降飞行器（electric Vertical Take-Off and Landing, e-VTOL）等多类型飞行器在城市低空的并发运行密度快速攀升，对空域运行态势的实时感知与预测提出了迫切需求。

伴随产业规模扩张，城市低空空域管理面临的压力日趋严峻。根据Garrow等人的预测，到2030年全球无人机市场规模将达到28.3亿美元，空域容量将达到1420万架 <sup><a type="reference">[2]</a></sup> 。在城市低空建筑物密集、禁飞区动态变化与多类型飞行器高密度并发的环境下，不同类型飞行器在功能定位、飞行性能与运行高度上差异显着。按照《国家空域基础分类方法》 <sup><a type="reference">[3]</a></sup> ，真高120m以下为W类非管制空域，主要供微型、轻型无人机适飞使用；120～300m属于G类非管制空域，可供行业级无人机报备飞行。《无人驾驶航空器飞行管理暂行条例》 <sup><a type="reference">[4]</a></sup> 进一步以真高120m为管制边界，对无人机飞行活动实施分类管理。结合亿欧智库对低空经济空域的研究 <sup><a type="reference">[5]</a></sup> ，120～300m高度层以快递物流等行业级无人机任务为主，飞行速度较低（约15m/s）；300～1000m高度层主要服务于城市出行、低空旅游等场景的载客类eVTOL，飞行速度较高（约28m/s）。两类飞行器任务模式与性能特征不同，在高度边界处存在跨层交互的冲突风险。基于此，本文将前者定义为标准性能飞行器（Standard-Performance Vehicle，SPV）层，后者定义为高性能飞行器（High-Performance Vehicle，HPV）层。

然而，现有空域管理缺少量化这一多层异构运行压力的有效指标。空域复杂度（Airspace Complexity）作为表征拥挤程度、冲突风险与管制难度的综合指标，为解决上述问题提供了可行路径。美国联邦航空管理局（Federal Aviation Administration, FAA）在发布的无人机交通管理（UAS Traffic Management, UTM）ConOps文件中强调，空域管理系统必须具备对复杂运行环境的评估与响应能力 <sup><a type="reference">[6]</a></sup> 。因此，建立面向城市低空分层空域的复杂度预测方法，对保障低空融合运行安全、支撑空域精细化管理决策具有重要的现实意义和工程价值。

国内外学者对空域复杂度评价与预测进行了大量研究，现有成果可从传统建模方法、深度学习方法和融合运行场景三个方面加以梳理。

在传统建模方法方面，Laudeman等人最早提出了动态密度的概念，用线性加权的交通密度加上8个复杂的因子来衡量空域负荷 <sup><a type="reference">[7]</a></sup> 。随后，Delahaye和Puechmorel提出基于线性动力系统（Linear Dynamical System，LDS）的复杂度建模方法 <sup><a type="reference">[8]</a></sup> ，Delahaye等进一步开发了LDS复杂度地图可视化技术 <sup><a type="reference">[9]</a></sup> 。温瑞英等提出融合接近程度与汇聚程度的多元栅格化复杂度计算方法，将交互复杂度与背景复杂度映射到空域栅格以支持航迹优化，但该方法面向传统管制空域且仅计算当前时刻复杂度 <sup><a type="reference">[10]</a></sup> 。张博为等构建了基于区间层次分析法与熔权法的空域复杂度评估指标体系，实现了主客观融合的综合量化评估 <sup><a type="reference">[11]</a></sup> 。对于城市空中交通（Urban Air Mobility, UAM）场景，Sunil等人研究了空域结构对极端交通密度的适应性 <sup><a type="reference">[12]</a></sup> ，Wang等提出了基于LDS的复杂度优化方法 <sup><a type="reference">[13]</a></sup> 。

在深度学习方法方面，Li等人提出一种用深度无监督学习实现交通量自适应控制的方法 <sup><a type="reference">[14]</a></sup> ，Alharbi等人设计了专门针对UAM场景的深度学习结构，去解决复杂度的非线性映射问题 <sup><a type="reference">[15]</a></sup> 。付翌蕊等将空域交通数据映射为多尺度时空图像，采用深度度量学习模型进行复杂度五级分类评估，在实际空域数据上取得了较高的分类准确率 <sup><a type="reference">[16]</a></sup> 。在复杂度预测方面，Li Boyuan等提出多模态自适应时空图神经网络（Multimodal Adaptive Spatio-Temporal Graph Neural Network, MAST-GNN），通过物理邻接图、语义图和自适应图联合建模扇区间的多维空间依赖，在多步复杂度预测任务中显着优于LSTM、STGCN等基线方法 <sup><a type="reference">[17]</a></sup> ；Moreno等构建了融合冲突潜势、高度分层和速度差异的动态复杂度指标，系统对比了多种机器学习模型在不同预测时域下的精度，验证了动态特征对预测性能的提升作用 <sup><a type="reference">[18]</a></sup> 。

在有人与无人融合运行场景方面，李谋等针对有人机与无人机并发运行场景，采用柯尼希系数量化航迹复杂度并通过模拟退火算法使空域总复杂度降低56%，但该方法面向高空管制空域，未涉及城市低空SPV与HPV分层运行特征 <sup><a type="reference">[19]</a></sup> 。国内张进等对空中交通管理复杂性建模进行了系统研究 <sup><a type="reference">[20]</a></sup> 。Shi等提出的卷积长短期记忆网络（Convolutional Long Short-Term Memory, ConvLSTM）采用卷积的方式来解决时空序列的特征提取问题 <sup><a type="reference">[21]</a></sup> ；Zhang等提出的时空残差网络（Spatio-Temporal Residual Network, ST-ResNet）使用了残差学习的框架，在城市人流预测方面表现较好 <sup><a type="reference">[22]</a></sup> 。

纵观已有研究成果，存在以下不足：第一，传统复杂度建模方法 <sup><a type="reference">[7]</a> <a type="reference">[8]</a> <a type="reference">[9]</a> <a type="reference">[10]</a> <a type="reference">[11]</a> <a type="reference">[12]</a> <a type="reference">[13]</a></sup> 及近期栅格化方法 <sup><a type="reference">[10]</a></sup> 主要面向有人飞行场景或管制空域，未能体现城市低空SPV与HPV两类飞行器并发运行下的分层异构冲突特征；第二，深度学习方法 <sup><a type="reference">[14]</a> <a type="reference">[15]</a> <a type="reference">[16]</a> <a type="reference">[17]</a> <a type="reference">[18]</a></sup> 多面向扇区级建模，忽略网格级空间特征与垂直密度差异，且侧重评估而非时序预测；第三，融合运行下的复杂度研究 <sup><a type="reference">[19]</a></sup> 已关注异构飞行器场景，但尚未涉及跨层交互复杂度量化与多步预测问题。

针对以上问题，本文的主要贡献包括：（1）提出融合占用密度、冲突意图与航向熵的分层异构复杂度（Stratified Heterogeneous Complexity，SHC）指标体系，建立八通道分层特征表征，覆盖SPV层、HPV层及跨层交互三个复杂度分量的量化建模；（2）构建基于卷积神经网络（Convolutional Neural Network, CNN）与卷积长短期记忆网络（ConvLSTM）的端到端多任务预测框架，以三信道复杂度联合预测方式直接输出未来180s的分层复杂度场，实现对空域复杂度演化趋势的多步预示；（3）针对跨层交互复杂度，提出基于两层密度几何均值与层间速度差的量化方法，并借助仿真平台构造多密度、多场景的SPV与HPV并发运行工况，通过消融实验、时域退化分析与鲁棒性测试对跨层交互复杂度的建模与预示效果进行了总体验证。本文的结构为第一部分低空异构空域复杂度建模、第二部分基于CNN-ConvLSTM的复杂度预测模型、第三部分仿真实验与分析、第四部分结论。

## 1 低空异构空域复杂度建模

## 1.1 问题描述与假设

### 1.1.1 问题描述

城市低空异构空域的复杂度随运行态势动态演化，对其进行量化建模与预示是保障低空安全运行的关键。本文将空域分为SPV层与HPV层，两者独立运行并在层间边界有跨层交互风险。问题是如何根据过去60s的轨迹状态来预测180s内每个网格的分层复杂度分布。正式任务定义见1.3.1节。

### 1.1.2 模型假设

为了简化模型，做出如下假设：（1）假定无人机飞行路径、高度均在规定范围内，不考虑禁飞区外的飞行安全风险。若实际中出现违规飞行导致飞行器超出规定高度层，分层特征提取将产生归层偏差，使局部密度和跨层交互复杂度估计失准，因此本文方法的适用前提是飞行器在各自规定层内合规运行。（2）无人机匀速飞行，飞行速度与载重无关，SPV层最大巡航速度设定为15m/s，HPV层设定为28m/s。实际运行中飞行器存在加减速行为，速度波动会对特征通道引入噪声并影响冲突意图分量的计算精度，该假设不满足时的具体影响有待后续研究。（3）预测时域为3分钟，短期内气象条件变化缓慢，空域环境基本稳定。若遭遇强风切变等极端气象突变，飞行器航迹与速度分布将偏离训练数据模式导致预测精度下降，本文模型未纳入气象特征通道，仅适用于常规气象条件。

### 1.1.3 符号说明

$t$ ：时刻索引；

$\Delta t$ ：时间步长， $\Delta t$ =5s；

$g = \left(i , j\right)$ ：网格单元索引， $i , j \in \left\{1 , 2 , . . . , 5 0\right\}$ ；

$$ ， $$ ：时刻 $t$ 空域内SPV层、HPV层飞行器集合；

$$ ， $$ ：时刻 $t$ 网格 $g$ 内SPV层、HPV层飞行器数量；

$$ ：总飞行器数量；

$$ ， $$ ， $$ ： $l$ 层密度、交互、航向混乱度指标， $l \in \left\{s p v , h p v\right\}$ ；

$$ ， $$ ：SPV层、HPV层内部复杂度， $$ ；

$$ ：跨层交互复杂度， $$ ；

$\mathbf{S} \left(t\right)$ ：空域状态张量， $$ ；

$\mathbf{C} \left(t\right)$ ：三通道复杂度场， $$ ；

$T                                                                                                    i                      n$ ：输入时间步数（12步，60秒）；

$T                                                                                                    o                      u                      t$ ：输出时间步数（36步，180秒）。

## 1.2 分层空域状态表征

### 1.2.1 复杂度定义

本文根据分层异构空域提出三个复杂度分量。SPV层内部复杂度和HPV层内部复杂度用统一的单层加权公式表示为：

$C                                                                                                                                  l                                                                                                    (                                                      g                            ,                            t                                                    )                                                =                        w                                                                                                                                  D                                                                          ⋅                        D                                                                                                                                  l                                                                                                    (                                                      g                            ,                            t                                                    )                                                +                        w                                                                                                                                  I                                                                          ⋅                        I                                                                                                                                  l                                                                                                    (                                                      g                            ,                            t                                                    )                                                                                                                                    +                        w                                                                                                                                  H                                                                          ⋅                        H                                                                                                                                  l                                                                                                    (                                                      g                            ,                            t                                                    )                                                ,                        l                        ∈                                                  {                                                      s                            p                            v                            ,                            h                            p                            v                                                    }$

式中： $wD,wI,wH$ 为权重系数，取值参考NASA动态密度理论和相关文献，本文取值为 $wD=0.4、wI=0.3、wH=0.3$ 。

密度指标反映局部拥挤程度：

$D                                                                                                    l                                                                            (                                          g                      ,                      t                                        )                                    =                                                            N                                                                                                                        l                                                                                            (                                                  g                          ,                          t                                                )                                                                                    N                                                                                                                        m                          a                          x                                                                          l$

其中 $Nl(g,t)$ 为网格 $g$ 在时刻 $t$ 内 $l$ 层的飞行器的瞬时数量， $Nmaxl$ 为历史最大值，用于归一化。密度指标随采样时刻t更新，时间演化关系通过ConvLSTM对连续帧序列的循环处理来捕捉。

冲突意图分量反映网格内飞行器速度向量的对向程度，速度夹角越大，潜在冲突意图越强：

$I                                                                                                    l                                                                            (                                          g                      ,                      t                                        )                                    =                                                                                                                                          ∑                                                                                                    i                          ≠                          j                          ,                                                     i                          ,                          j                          ∈                          U                                                                                                                                            l                                                                                                            (                                                          g                              ,                              t                                                        )                                                                                              s                      i                      n                                                                                                                        2                                                                                            (                                                  θ                                                                                                                                            i                              j                                                                                /                          2                                                )                                                                                    C                                              (                                                  N                                                                                                                                            l                                                                                                            (                                                          g                              ,                              t                                                        )                                                    ,                          2                                                )$

式中： $θijl$ 为第L层网格内飞行器i与j速度向量的夹角； $C(Nl(g,t),2)$ 为从 $Nl(g,t)$ 架飞器中取2架的组合数，即

$C                                      (                                          N                                                                                                                        l                                                                                            (                                                  g                          ,                          t                                                )                                            ,                      2                                        )                                    =                                                            N                                                                                                                        l                                                                                            (                                                  g                          ,                          t                                                )                                                                    [                                                  N                                                                                                                                            l                                                                                                            (                                                          g                              ,                              t                                                        )                                                    −                          1                                                ]                                                                                    2$

航向熵分量体现的是网格内飞行器航向分布的散乱程度，熵值越高说明航向越分散、冲突态势就越复杂：

$H                                                                                                    l                                                                            (                                          g                      ,                      t                                        )                                    =                  −                                                            1                                                              l                      o                      g                      K                                                                                                                          ∑                                                                                    k                      =                      1                                                              K                                                        p                                                                                                    k                                                        l                  o                  g                  p                                                                                                    k$

其中 $pk$ = $pk$ (g，t)为采样时刻t网格g内第k个航向区间（将360°等分为 $K=8$ 个区间）的飞行器比例，归一化至 $[0,1]$ 。航向熵在每个采样时刻独立计算，其时间演化同样通过ConvLSTM的时序建模来捕捉。

跨层交互复杂度刻画同一网格内SPV层和HPV层飞行器在垂直方向上可能存在的交互风险，由两层密度的几何均值以及层间速度差共同决定：

$C                                                                                                                                  c                            r                            o                            s                            s                                                                                                    (                                                      g                            ,                            t                                                    )                                                =                        α                        ⋅                                                                              D                                                                                                                                                      s                                p                                v                                                                                                                    (                                                              g                                ,                                t                                                            )                                                        ⋅                            D                                                                                                                                                      h                                p                                v                                                                                                                    (                                                              g                                ,                                t                                                            )                                                                                                                                                                                          +                        β                        ⋅                                                                                                            |                                                                                                v                                  ¯                                                                                                                                                                                                          s                                    p                                    v                                                                                                                                    (                                                                      g                                    ,                                    t                                                                    )                                                                −                                                                  v                                  ¯                                                                                                                                                                                                          h                                    p                                    v                                                                                                                                    (                                                                      g                                    ,                                    t                                                                    )                                                                                            |                                                                                                            v                                                                                                                                                      m                                a                                x$

其中 $α=β=0.5$ ， $v¯spv$ 和 $v¯hpv$ 分别为两层飞行器的平均速度， $vmax=28$ m/s为归一化基准。由于D <sup>l</sup> ∈\[0,1\]，速度差归一化项|v <sub>spv</sub> -v <sub>hpv</sub> |/28∈\[0,1\]，且权重α+β=1，故C <sub>cross</sub> ∈\[0,1\]，与C <sub>spv</sub> 、C <sub>hpv</sub> 保持相同值域。

### 1.2.2 八通道空域特征

综合上述复杂度指标的计算需求，每个时刻的空域状态可表示为 $S(t)∈ℝ50×50×8$ 的张量，各通道定义如表1所示：

| 信道索引 | 变量名 | 含义 | 归一化方式 |
| --- | --- | --- | --- |
| 0 | $d                                                                                                                                  s                            p                            v$ | SPV层归一化飞行器密度 | 除以历史最大值 |
| 1 | $s                        p                        d                                                                                                                                  s                            p                            v$ | SPV层平均速度 | 除以15m/s |
| 2 | $h                        d                        g                                                                                                                                  s                            p                            v$ | SPV层平均航向 | 除以360° |
| 3 | $d                                                                                                                                  h                            p                            v$ | HPV层归一化飞行器密度 | 除以历史最大值 |
| 4 | $s                        p                        d                                                                                                                                  h                            p                            v$ | HPV层平均速度 | 除以28m/s |
| 5 | $h                        d                        g                                                                                                                                  h                            p                            v$ | HPV层平均航向 | 除以360° |
| 6 | $t                        o                        t                        a                        l                        _                        d$ | 总飞行器密度（SPV+HPV） | 除以历史最大值 |
| 7 | $r                        a                        t                        i                        o                                                                                                                                  s                            p                            v$ | SPV层飞行器占总数比例 | 自然归一化至 $[0,1]$ |

## 1.3 预测任务与技术路线

### 1.3.1 任务定义

任务本质上是一个时空序列到序列（Seq2Seq）映射问题，难点在于输入状态张量高维（12×50×50×8=240，000维），有复杂的时空依赖；长时预测（180秒）需要模型有长期记忆的能力；输出是三个通道，要同时表现层内以及跨层的复杂度的协同变化。

具体定义为给定历史 $Tin=12$ 帧（60秒）的轨迹状态序列 ${S(t−11),…,S(t)}$ ，预测未来 $Tout=36$ 帧（180秒）的复杂度序列 ${C(t+1),…,C(t+36)}$ ，其中 $C(t)∈ℝ50×50×3$ 用来表示三通道复杂度场。形式化表示为：

$f                  :                                      {                                          S                                              (                                                  t                          −                          1                          1                                                )                                            ,                      …                      ,                      S                                              (                                                  t                                                )                                                              }                                    →                  {                  C                                      (                                          t                      +                      1                                        )                                    ,                  …                  ,                  C                                      (                                          t                      +                      3                      6                                        )$

### 1.3.2 技术路线图

本文采用深度学习方法，构建CNN-ConvLSTM架构直接从轨迹特征预测复杂度场。技术路线具体如图1所示：

![图片](https://kns.cnki.net/ossapi/kreader-api/v1/xml/attachment?platform=NZKPT&product=CAPJ&filename=XTFZ20260424006&tablename=capjlast&type=JOURNAL&scope=readonline&cflag=7D03FA4D6F3C4D108D622ED4E404509E&dflag=Cr64/2k%2bF4/QEocKENGdXu392xoJ15gczYs96NTZOWMCzrDBWjLSJ56%2b7bONwkcFqrUS8Wfl8OnRbz%2bk2oTIJd1sK1JH/9n2OZBaXZ0P/K6bGy7Xb0K91lDVVduny78VQKnTqhXWxFuuUWpoxeagZiv%2b9D0gp7ubkXrcILh129U=&nonce=7D03FA4D6F3C4D108D622ED4E404509E&invoice=Cr64/2k%2bF4/QEocKENGdXu392xoJ15gczYs96NTZOWMCzrDBWjLSJ56%2b7bONwkcFqrUS8Wfl8OnRbz%2bk2oTIJd1sK1JH/9n2OZBaXZ0P/K6bGy7Xb0K91lDVVduny78VQKnTqhXWxFuuUWpoxeagZiv%2b9D0gp7ubkXrcILh129U=&idenid=WEEvREcwSlJHSldSdmVpZ0doelJ3VkMyUlorcVo1V3NjdkdzMmo3cHBBOD0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&annexid=XTFZ20260424006_185.jpg)

#### 图1 技术路线图

#### Fig. 1 Technology roadmap

## 2 基于CNN-ConvLSTM的复杂度预测仿真模型

## 2.1 模型整体架构

### 2.1.1 架构设计

为满足任务50×50×8高维时空序列的三通道复杂度预测要求，本文提出SHC预测网络。该预测架构由空间编码器、时序建模器、未来预测器和空间解码器四部分组成，模型输入维度：12帧历史，8通道，50×50网格；模型输出维度：36帧预测，3通道复杂度（ $Cspv$ 、 $Chpv$ 、 $Ccross$ ）。如图2所示：

![图片](https://kns.cnki.net/ossapi/kreader-api/v1/xml/attachment?platform=NZKPT&product=CAPJ&filename=XTFZ20260424006&tablename=capjlast&type=JOURNAL&scope=readonline&cflag=7D03FA4D6F3C4D108D622ED4E404509E&dflag=Cr64/2k%2bF4/QEocKENGdXu392xoJ15gczYs96NTZOWMCzrDBWjLSJ56%2b7bONwkcFqrUS8Wfl8OnRbz%2bk2oTIJd1sK1JH/9n2OZBaXZ0P/K6bGy7Xb0K91lDVVduny78VQKnTqhXWxFuuUWpoxeagZiv%2b9D0gp7ubkXrcILh129U=&nonce=7D03FA4D6F3C4D108D622ED4E404509E&invoice=Cr64/2k%2bF4/QEocKENGdXu392xoJ15gczYs96NTZOWMCzrDBWjLSJ56%2b7bONwkcFqrUS8Wfl8OnRbz%2bk2oTIJd1sK1JH/9n2OZBaXZ0P/K6bGy7Xb0K91lDVVduny78VQKnTqhXWxFuuUWpoxeagZiv%2b9D0gp7ubkXrcILh129U=&idenid=WEEvREcwSlJHSldSdmVpZ0doelJ3VkMyUlorcVo1V3NjdkdzMmo3cHBBOD0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&annexid=XTFZ20260424006_194.jpg)

#### 图2 CNN-ConvLSTM模型架构图

#### Fig. 2 CNN-ConvLSTM model architecture diagram

### 2.1.2 模块功能

空间编码器用CNN提取每一帧的空间特征，把50×50压缩到25×25，并且把通道数从8增加到64。时序建模器使用ConvLSTM，对12帧输入进行循环处理，用门控机制选择性地记住或者遗忘历史信息，最终得到隐藏状态 $H12$ ，编码60s的历史轨迹状态变化信息。未来预测器用卷积投影把 $H12$ 映射为36帧未来特征。空间解码器通过上采样和卷积，将特征还原至50×50分辨率，输出三通道复杂度预测。

### 2.1.3 预测策略

因为，大规模异构并发场景下局部复杂度会发生剧烈变化（突发拥挤），残差连接假设未来状态和当前状态很接近（只预测增量），很难捕捉到这种突变。基于此，本文采用直接预测策略，即模型直接输出未来三通道复杂度即 $Cspv(t+1:t+36)$ 、 $Chpv(t+1:t+36)$ 、 $Ccross(t+1:t+36)$ 。

## 2.2 网络结构设计

### 2.2.1 空间编码器

空间编码器采用卷积神经网络来提取每帧的空间特征。首先通过两层卷积（8→32→64通道），卷积核大小3×3，padding为1，激活函数为ReLU。随后通过最大池化（kernelsize2×2，stride2），将特征从50×50压缩至25×25。其中卷积层通过共享权重的滤波器捕捉局部空间模式，池化层通过下采样降低特征维度并增强特征不变性，从而实现从原始8通道异构特征到高级语义特征的转换。

### 2.2.2 ConvLSTM时序建模器

ConvLSTM是对LSTM的空间扩展版本，把全连接操作替换为卷积操作，使得隐藏状态和细胞状态均是二维张量，从而有效捕捉时空序列数据中的长期依赖关系。设ConvLSTM的输入为空间编码器的输出序列{X1，…，X12}，其状态更新过程为：

$H                                                                                                    t                                                        ,                  C                                                                                                    t                                                        =                  C                  o                  n                  v                  L                  S                  T                  M                                      (                                          X                                                                                                                        t                                                                    ,                      H                                                                                                                        t                          −                          1                                                                    ,                      C                                                                                                                        t                          −                          1                                                                                      )$

式中： $Ht∈ℝ64×25×25$ 为时刻t的隐藏状态； $Ct∈ℝ64×25×25$ 为细胞状态。ConvLSTM利用门控机制，在每个时间步选择性地遗忘或接收。本文采用单层ConvLSTM（input <sub>dim</sub> =64，hidden <sub>dim</sub> =64，kernel <sub>size</sub> =3），循环处理12个时间步的输入，仅保留最终隐藏状态 $H12$ ，该状态编码了历史60秒轨迹状态的时空演化信息。

### 2.2.3 未来预测器与解码器

未来预测器对 $H12$ 进行卷积投影，输出通道数扩展为 $36×64$ ，再经kernelsize3×3、padding1的卷积层reshape为36帧特征图，从而其维度为36×64×25×25。

空间解码器依次通过双线性上采样（scale\_factor=2）、Conv2d（64→32，kernelsize3×3，ReLU激活）和Conv2d（32→3，kernelsize1×1，无激活函数）三个模块，将特征还原至50×50×3的三通道复杂度输出。最后一层采用线性输出，模型训练阶段输出值无界；推理阶段对输出结果进行截断处理（clamp to\[0,1\]），以与复杂度指标的物理定义保持一致。

## 2.3 训练设置

### 2.3.1 损失函数

使用Smooth L1损失函数来衡量预测复杂度与真实复杂度之间的差距：

$L                                                                                                    c                                                        =                                                            1                                                              N                                                                                                                          ∑                                                                                    i                      =                      1                                                              N                                                        S                  m                  o                  o                  t                  h                  L                  1                  ​                                      (                                          y                                                                                                                        i                                                                                                      (                                                          c                                                        )                                                                                              ,                                              y                        ^                                                                                                                                              i                                                                                                      (                                                          c                                                        )                                                                                                                )$

$SmoothL1(x,y)={0.5(x−y)2if|x−y|<1|x−y|−0.5otherwise$

其中 $N$ 为批次内样本总数，c∈{spv，hpv，cross}为信道索引， $yi(c)$ 与 $y^i(c)$ 分别为第 $c$ 通道的真实值与预测值。为防止某个通道主导梯度的方向。设置总损失函数为三个通道损失的等权加和：

$L                                                                                                    t                      o                      t                      a                      l                                                        =                  L                                                                                                    s                      p                      v                                                        +                  L                                                                                                    h                      p                      v                                                        +                  L                                                                                                    c                      r                      o                      s                      s$

### 2.3.2 评估指标

实验采用平均绝对误差（MAE）、均方根误差（RMSE）和决定系数（ $R2$ ）评估全局预测性能：

$M                  A                  E                  =                                                            1                                                              M                                                                                                                          ∑                                                                                    i                      =                      1                                                              M                                                                            |                                                                  y                        ^                                                                                                                                              i                                                                    −                      y                                                                                                                        i                                                                                      |$

$R                  M                  S                  E                  =                                                                                                              1                                                                          M                                                                                                                                                  ∑                                                                                                    i                          =                          1                                                                          M                                                                    (                                              y                        ^                                                                                                                                              i                                                                    −                      y                                                                                                                        i                                                                    )                                                                                                                        2$

$R                                                                                                    2                                                        =                  1                  −                                                                                                                                          ∑                                                                                                    i                          =                          1                                                                          M                                                                    (                                              y                        ^                                                                                                                                              i                                                                    −                      y                                                                                                                        i                                                                    )                                                                                                                        2                                                                                                                                                                                          ∑                                                                                                    i                          =                          1                                                                          M                                                                    (                      y                                                                                                                        i                                                                    −                                              y                        ¯                                            )                                                                                                                        2$

其中 $M$ 为样本总数， $y^$ 为真实值均值。MAE和RMSE用来衡量预测的绝对误差， $R2$ 衡量模型对复杂度空间分布的整体拟合程度。

## 3 仿真实验验证与分析

## 3.1 实验设置

### 3.1.1 数据集配置

本文使用BlueSky ATM仿真平台构建典型城市场景下双层异构空域数据集。仿真场景大小为50km×50km，划分为1km×1km的网格。数据采样间隔Δt为5s，依据来自于ASTM F3411-22a <sup><a type="reference">[23]</a></sup> 要求无人机位置消息的广播间隔不小于1Hz，因此5s为工程折中的评估粒度。输入序列12帧（60s历史），预测序列36帧（180s）。

基于仿真场景对数据集进行分类，其中训练集75个场景（645个样本），验证集20场景（172个样本），无场景重复。仿真中SPV层机型参照DJI Matrice 600 Pro物流无人机，最大巡航速度设定为15m/s；HPV层机型参照EHang 216载客类e-VTOL"，最大巡航速度设定为28m/s。上述参数均来自对应机型的公开技术规格。不同的场景下飞行器的数量配置分别为SPV层50-500架、HPV层20-200架，每个场景下使用独立的随机种子，轨迹序列不跨场景复用，进而科学评价模型对于没见过的交通流量组合的泛化能力。但是，由于数据量的限制，没有独立测试集。验证集既做Early Stopping又做最终评价。

### 3.1.2 实验环境与参数配置

所有实验在NVIDIA GeForce RTX 4060 GPU（8GB显存）上进行，环境为PyTorch 2.3.0与CUDA 12.1。采用AdamW <sup><a type="reference">[24]</a></sup> 优化器（lr=1×10⁻³，权重衰减1×10⁻⁴），Cosine Annealing LR调度，批大小8，最大训练50epochs，采用patience=10的早停策略。以验证集Smooth L1 Loss最小的检查点为最终模型。单个epoch训练耗时约9秒，50个epoch总训练时长约7～8分钟。

### 3.1.3 对比方法

评价指标分为两种口径统计：全局指标包括MAE、RMSE和R²；非零格指标（MAE <sub>nz</sub> 、R² <sub>nz</sub> ）仅统计有飞行器的网格时刻，更能反映模型对高风险区域的实际预测能力。

为了检验本文所用的方法是否有效，选取以下基线方法进行比较：

（1）Persistence（持久性模型）：假设未来复杂度与最后一帧相同，即 $C^(t+j)=C(t)$ 。这是时间序列预测中最经典的基线，也就是假定变化率是零。

（2）HA（Historical Average）：即历史均值基线，用训练集中每个预测步长的平均复杂度图来代替预测。

（3）ST-ResNet：Zhang等 <sup><a type="reference">[22]</a></sup> 提出的时空残差网络，通过残差连接融合历史、近期和周期性三个时间尺度的信息。本文仅使用近期分支（12帧输入），输出36帧预测。

（4）Pure-ConvLSTM：去除CNN空间编码器，直接用ConvLSTM处理原始8通道输入。用于验证CNN空间编码模块的贡献。

## 3.2 性能对比与分析

在进行定量性能对比之前，首先从方法定位层面回顾引言中梳理的代表性研究。表2从复杂度指标构成、输出形式、时间维度和目标场景四个维度对代表性方法与本文方法进行定性对比。

| 对比维度 | 动态密度 <sup>[7]</sup> | LDS复杂度 <sup>[8-9]</sup> | 栅格化方法 <sup>[10]</sup> | MAST-GNN <sup>[17]</sup> | Moreno <sup>[18]</sup> | 本文SHC |
| --- | --- | --- | --- | --- | --- | --- |
| 复杂度指标构成 | 交通密度+8个管制负荷因子 | Lyapunov指数（流场混沌度） | 接近程度+汇聚程度 | 基于管制员标定的综合等级 | 冲突潜势+高度分层+速度差异 | 密度+冲突意图+航向熵 |
| 输出形式 | 扇区级单一标量 | 区域级连续值地图 | 网格级复杂度分布 | 扇区级离散等级 | 扇区级离散等级 | 网格级三通道连续值场 |
| 时间维度 | 当前时刻评估 | 当前时刻评估 | 当前时刻评估 | 多步预测 | 多步预测 | 多步预测（180s） |
| 目标场景 | 传统管制空域 | 传统管制空域 | 传统管制空域 | 传统管制空域 | 传统管制空域 | 城市低空异构空域 |

由表2可见，传统方法在复杂度指标构成上各有侧重，但均面向传统管制空域且多数仅支持当前时刻评估；MAST-GNN和Moreno等近期工作引入了机器学习实现多步预测，但空间粒度为扇区级、输出为离散等级。本文SHC在网格级空间粒度上输出三通道连续值复杂度场，并将目标场景拓展至城市低空异构空域，以下通过定量实验进一步验证其预测性能。

### 3.2.1 整体性能对比

表3给出了各个方法在验证集上的整体预测性能。图3（a）用棒棒糖图显示各个方法的全局MAE差异，（b）用柱状图展示消融实验各变体的R²对比（A1~A5），（c）用双色柱状图比较SHC各通道全格和非零格R²，（d）用条形图比较SHC推理流水线各个阶段延迟和参数量分布。

| 模型 | MAE（全格） | R²（全格） | MAE（非零格） | R²（非零格） |
| --- | --- | --- | --- | --- |
| Persistence | 0.0204 | \-2.032 | 0.0548 | \-0.504 |
| 历史均值（HA） | 0.0117 | 0.124 | 0.0423 | 0.034 |
| ST-ResNet | 0.0091 | 0.482 | 0.0364 | 0.365 |
| Pure-ConvLSTM | 0.0053 | 0.820 | 0.0231 | 0.775 |
| Ours（SHC） | 0.0045 | 0.870 | 0.0196 | 0.838 |

通过数据发现Persistence全格R²=-2.032，这证明纯持久性假设在动态场景下完全失效。Ours（SHC）相比ST-ResNet非零格R²从0.365提升至0.838，说明残差学习在高动态稀疏场景下的局限性较大，详见3.3.1部分的详细分析。Pure-ConvLSTM与Ours（SHC）的非零格R²差距（0.775 vs 0.838）这进一步证明了8通道异构分层特征的有效性。

![图片](https://kns.cnki.net/ossapi/kreader-api/v1/xml/attachment?platform=NZKPT&product=CAPJ&filename=XTFZ20260424006&tablename=capjlast&type=JOURNAL&scope=readonline&cflag=7D03FA4D6F3C4D108D622ED4E404509E&dflag=Cr64/2k%2bF4/QEocKENGdXu392xoJ15gczYs96NTZOWMCzrDBWjLSJ56%2b7bONwkcFqrUS8Wfl8OnRbz%2bk2oTIJd1sK1JH/9n2OZBaXZ0P/K6bGy7Xb0K91lDVVduny78VQKnTqhXWxFuuUWpoxeagZiv%2b9D0gp7ubkXrcILh129U=&nonce=7D03FA4D6F3C4D108D622ED4E404509E&invoice=Cr64/2k%2bF4/QEocKENGdXu392xoJ15gczYs96NTZOWMCzrDBWjLSJ56%2b7bONwkcFqrUS8Wfl8OnRbz%2bk2oTIJd1sK1JH/9n2OZBaXZ0P/K6bGy7Xb0K91lDVVduny78VQKnTqhXWxFuuUWpoxeagZiv%2b9D0gp7ubkXrcILh129U=&idenid=WEEvREcwSlJHSldSdmVpZ0doelJ3VkMyUlorcVo1V3NjdkdzMmo3cHBBOD0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&annexid=XTFZ20260424006_274.jpg)

#### 图3 各方法性能综合对比

#### Fig. 3 Comprehensive performance comparison

### 3.2.2 时域退化分析

图4展示了三个复杂度分量上各方法MAE随预测时域（5s至180s）的变化，纵向三列分别对应C <sub>spv</sub> （SPV层）、C <sub>hpv</sub> （HPV层）、C <sub>cross</sub> （跨层交互），T+120虚线对应图5热力图可视化时刻。

![图片](https://kns.cnki.net/ossapi/kreader-api/v1/xml/attachment?platform=NZKPT&product=CAPJ&filename=XTFZ20260424006&tablename=capjlast&type=JOURNAL&scope=readonline&cflag=7D03FA4D6F3C4D108D622ED4E404509E&dflag=Cr64/2k%2bF4/QEocKENGdXu392xoJ15gczYs96NTZOWMCzrDBWjLSJ56%2b7bONwkcFqrUS8Wfl8OnRbz%2bk2oTIJd1sK1JH/9n2OZBaXZ0P/K6bGy7Xb0K91lDVVduny78VQKnTqhXWxFuuUWpoxeagZiv%2b9D0gp7ubkXrcILh129U=&nonce=7D03FA4D6F3C4D108D622ED4E404509E&invoice=Cr64/2k%2bF4/QEocKENGdXu392xoJ15gczYs96NTZOWMCzrDBWjLSJ56%2b7bONwkcFqrUS8Wfl8OnRbz%2bk2oTIJd1sK1JH/9n2OZBaXZ0P/K6bGy7Xb0K91lDVVduny78VQKnTqhXWxFuuUWpoxeagZiv%2b9D0gp7ubkXrcILh129U=&idenid=WEEvREcwSlJHSldSdmVpZ0doelJ3VkMyUlorcVo1V3NjdkdzMmo3cHBBOD0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&annexid=XTFZ20260424006_278.jpg)

#### 图4 分层复杂度预测误差随预测时域变化（均值，验证集）

#### Fig. 4 Temporal degradation of layered complexity prediction error (mean MAE vs. forecast horizon, validation set).

具体来看，C <sub>spv</sub> 子图中各个方法的误差随着时间的推移逐渐减小，这是因为仿真场景末期SPV层的配送任务基本完成，复杂度自然归零，长时预测的绝对误差也逐渐变小。C <sub>hpv</sub> 子图中Persistence误差从T+5s的约0.016迅速上升到T≈10-15s的约0.041，而其它两层没有出现这样的尖峰。这是因为Persistence将初始帧冻结复制，无法跟随HPV层复杂度的快速变化，导致预测窗口初期误差骤增。而本文模型在同一时段误差平稳，则说明ConvLSTM捕捉到了HPV层复杂度的短期演化趋势。C <sub>cross</sub> 子图中本文模型在三列里一直保持着最小的误差，和其它方法的差别在中长时域（T+60s到T+180s）比较稳定。

## 3.3 模型分析与讨论

### 3.3.1 消融实验

如表4所示列出了结构消融的实验结果，而图3（b）则展示了各变体模型的R²对比。A1加载50epochs正式检查点作为参考基线；A2至A5训练20epochs，早停patience=7，调度器T <sub>max</sub> =20，评估协议统一，保证消融对比的公平性。

| 变体 | 说明 | 参数量 | MAE（全格） | R²（全格） | R²（非零格） |
| --- | --- | --- | --- | --- | --- |
| A1：SHC完整 | 8通道+CNN+ConvLSTM+3输出 | 1,663,971 | 0.0060 | 0.809 | 0.735 |
| A2：无CNN编码器 | 去掉CNN空间编码模块 | 1,643,715 | 0.0088 | 0.647 | 0.508 |
| A3：无ConvLSTM | 去掉ConvLSTM，仅保留CNN | 1,418,019 | 0.0100 | 0.570 | 0.416 |
| A4：5通道输入 | 去掉HPV层3个特征通道 | 1,663,107 | 0.0077 | 0.707 | 0.592 |
| A5：单通道输出 | 仅预测总复杂度C <sub>eff</sub> | 1,663,905 | 0.0054 | 0.622 | 0.474 |

注：A1为消融基线，采用逐批次评估协议（per-batch evaluation，逐批累加）；表4中Ours采用全量评估协议（full-set evaluation，全量拼接后统一计算），两者使用同一50-epoch最优检查点，数值差异（R²:0.809vs0.870）源于评估口径不同，A2–A5均在统一的逐批次协议下训练20轮，与A1保持可比性。

从R²的差值结果看，去掉ConvLSTM后，R²从0.809降至0.570，说明其对模型性能影响最大。三信道变为单信道输出之后R²降低0.187，说明分层联合预测效果更好。CNN编码器影响排名第三。HPV层特征对于整体R²的贡献较小，但是去掉之后非零格R²下降了19.5%，这说明全局指标不能很好地反映它在高风险区段预测的作用。

然而，模型加上残差之后效果变差，R²为负。进一步通过残差分布的统计结果（偏度-8.29，峰度138.01），可以发现残差目标分布在很大程度上是尾大不掉的重尾特征。该结果与ST-ResNet在非零格上表现不佳相互印证，再次证明高动态、稀疏性强的环境里，直接预测比残差预测更合适。

进一步针对输入特征与标签同源的问题，对特征通道做了推理期置零实验。结果详见表5：

| 变体 | 置零通道 | MAE（全格） | R²（全格） | R²（非零格） |
| --- | --- | --- | --- | --- |
| F0：完整8通道（基线） | — | 0.00446 | 0.870 | 0.838 |
| F1：去航向通道 | hdg <sub>spv</sub> ，hdg <sub>hpv</sub> | 0.00816 | 0.421 | 0.338 |
| F2：去冗余密度信道 | total <sub>d</sub> ，ratio <sub>spv</sub> | 0.00658 | 0.509 | 0.340 |
| F3：去航向+冗余密度 | ch2,5,6,7全部 | 0.00793 | 0.260 | 0.027 |

通过具体数据可知，去掉航向通道后，R²降至0.421；去掉冗余密度信道后，R²降至0.509；两类通道同时去掉后，非零格R²仅剩0.027。这表明模型学习的是未来演化规律，而不是对当前复杂度指标的直接“复现”。

### 3.3.2 分层异构复杂度预测性能

如表6所示展示了SHC模型在各复杂度分量上的分信道性能，图3（c）则同步对比各通道全格与非零格R²。

| 通道 | 含义 | MAE（全格） | R²（全格） | MAE（非零格） | R²（非零格） |
| --- | --- | --- | --- | --- | --- |
| C <sub>spv</sub> | SPV层综合复杂度 | 0.0049 | 0.745 | 0.0223 | 0.736 |
| C <sub>hpv</sub> | HPV层综合复杂度 | 0.0097 | 0.863 | 0.0432 | 0.829 |
| C <sub>cross</sub> | 跨层交互复杂度 | 0.0034 | 0.645 | 0.0197 | 0.627 |
| C <sub>eff</sub> | 总有效复杂度 | 0.0045 | 0.870 | 0.0196 | 0.838 |

通过分析发现，预测的难度与运动规律性成正比，其中C <sub>hpv</sub> 预测精度最高，这是因为HPV飞行器航路固定、时序规律强、稀疏度低（87.6%），非零格样本相对充足。C <sub>cross</sub> 最难预测，是因为跨层交互依赖于两层飞行器随机时空重合，是后续研究改进的重点。而合成之后C <sub>eff</sub> 略大于各个分量则是因为误差方向的部分抵消。

### 3.3.3 空间预测误差分布

如图5所展示了T+120s时刻三个分量的空间预测结果，行分别是C <sub>spv</sub> 、C <sub>hpv</sub> 、C <sub>cross</sub> ，列分别是真实值、SHC预测、误差绝对值。C <sub>spv</sub> 真实值为条带状高复杂度区域（对应物流无人机主干配送走廊），SHC预测基本上还原了这条结构，而其误差则主要出现在条带的边缘部分，这说明模型对于热点的位置定位比较准确，但是边界精度还有待提升。C <sub>hpv</sub> 的预测精度最好，误差图绝大部分为0，只有少数走廊汇聚节点有残差。C <sub>cross</sub> 的误差比较分散，则是因为两层飞行器随机时空相遇事件的捕捉能力差。高误差区主要集中在主要航路交汇处，也就是复杂度时空波动最剧烈的地方，说明模型残差是由于场景本身的不确定性造成的，并不是系统性的偏差。

![图片](https://kns.cnki.net/ossapi/kreader-api/v1/xml/attachment?platform=NZKPT&product=CAPJ&filename=XTFZ20260424006&tablename=capjlast&type=JOURNAL&scope=readonline&cflag=7D03FA4D6F3C4D108D622ED4E404509E&dflag=Cr64/2k%2bF4/QEocKENGdXu392xoJ15gczYs96NTZOWMCzrDBWjLSJ56%2b7bONwkcFqrUS8Wfl8OnRbz%2bk2oTIJd1sK1JH/9n2OZBaXZ0P/K6bGy7Xb0K91lDVVduny78VQKnTqhXWxFuuUWpoxeagZiv%2b9D0gp7ubkXrcILh129U=&nonce=7D03FA4D6F3C4D108D622ED4E404509E&invoice=Cr64/2k%2bF4/QEocKENGdXu392xoJ15gczYs96NTZOWMCzrDBWjLSJ56%2b7bONwkcFqrUS8Wfl8OnRbz%2bk2oTIJd1sK1JH/9n2OZBaXZ0P/K6bGy7Xb0K91lDVVduny78VQKnTqhXWxFuuUWpoxeagZiv%2b9D0gp7ubkXrcILh129U=&idenid=WEEvREcwSlJHSldSdmVpZ0doelJ3VkMyUlorcVo1V3NjdkdzMmo3cHBBOD0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&annexid=XTFZ20260424006_296.jpg)

#### 图5 分层复杂度预测热力图（T+120s）

#### Fig. 5 Layered complexity prediction heatmaps at T+120s.

### 3.3.4 实时性与鲁棒性评估

（1）实时性，SHC端到端推理流水线由网格化、缓冲区管理、模型推理、滚动聚合、后处理五个阶段组成，各阶段延迟测试结果如表7和图3(d)所示。其中模型推理用时20.3ms为最久。端到端延迟中位数26.1ms（P95：51.2ms），占5s采样间隔的0.52%，满足实时性要求。

| 处理阶段 | 延迟（ms） | 占比 |
| --- | --- | --- |
| 网格化（Gridder） | 1.93 | 7.4% |
| 环形缓冲区（Ring Buffer） | 0.23 | 0.9% |
| 模型推理（Inference） | 20.30 | 77.8% |
| 滚动聚合（Aggregator） | 1.04 | 4.0% |
| 后处理（Postproc） | 0.07 | 0.3% |
| 端到端合计 | 26.10 | 100% |

（2）鲁棒性实验分随机缺失和空间遮蔽两组，结果见表8。随机缺失实验中，缺失率10%-20%时R²仍大于0.78，性能退化比较平缓说明CNN卷积核对邻格信息的空间聚合可弥补单格缺失，同时ConvLSTM门控机制对局部帧缺失也有时间平滑作用。当缺失率≥30%时退化情况加重，此时则需要依赖多源传感器融合补偿。空间遮蔽实验模拟高层建筑对广播式自动相关监视（Automatic Dependent Surveillance-Broadcast, ADS-B）信号的连续遮挡：5×5矩形（覆盖1%网格）R²下降较少仅0.008；15×15矩形（覆盖9%，约7.5km×7.5km）此时R²=0.783，但仍优于ST-ResNet基线。相比同覆盖率的随机缺失，空间聚集性缺失对模型的干扰更大——连续大面积空洞超出卷积核感受野范围，又受限于邻格插值的能力，这说明在高楼密集区域同样需要多源传感器互补。

（3）针对数据集85.16%网格复杂度为零的稀疏特性，进一步对模型在零格与非零格上的预测偏差分别进行了分析。零格上模型平均预测值为0.0012，接近零，并无系统性高估；非零格上相对偏差为-13.9%，存在轻微低估，假阴性率（非零格被预测为零）仅2.48%，高风险区域漏报率低，因此满足安全预警的基本要求。分通道来看的话，C <sub>cross</sub> 偏差最大，这与其最低R²=0.645一致，是后续改进的重点。分析得出，上述轻微低估倾向源于等权Smooth L1损失对稀疏目标的隐式偏好，因此后续可通过对非零格加权来缓解。

| 缺失模式 | 覆盖率 | MAE | R²（全格） | R²（非零格） | R²相对下降 |
| --- | --- | --- | --- | --- | --- |
| 基线（无缺失） | 0% | 0.0045 | 0.870 | 0.837 | — |
| 随机缺失 | 10% | 0.0047 | 0.832 | — | \-4.4% |
| 随机缺失 | 20% | 0.0049 | 0.778 | — | \-10.6% |
| 随机缺失 | 30% | 0.0053 | 0.706 | — | \-18.9% |
| 随机缺失 | 50% | 0.0059 | 0.530 | — | \-39.1% |
| 矩形遮蔽5×5 | 1% | 0.0047 | 0.863 | 0.826 | \-0.8% |
| 矩形遮蔽10×10 | 4% | 0.0048 | 0.842 | 0.798 | \-3.2% |
| 矩形遮蔽15×15 | 9% | 0.0052 | 0.783 | 0.718 | \-10.0% |

## 4 结论

本文针对城市低空异构空域复杂度的建模与预示问题，提出了SHC预测框架，用8个通道时空特征作为输入，分别预测SPV层、HPV层和跨层交互这三个复杂度分量，在BlueSky仿真数据集上总R²达到0.870，端到端延迟为26.1ms。鲁棒性实验表示20%信号缺失的时候R²仍然大于等于0.778。消融实验结果表明，用ConvLSTM时序建模、分层输出得到最好的性能。

本文的主要不足在于数据来源于仿真环境，没有办法对真实ADS-B场景下的泛化能力进行检验，C <sub>cross</sub> 预测精度偏低，现有的特征不能很好地覆盖两层飞行器随机时空重合事件；验证集兼作Early Stopping和最终评价，缺少独立测试集，因此可能会出现泛化性能被高估的现象。后续将从这几个方向继续进行优化。

### 参考文献

- \[1\]蒲钒, 陈志杰, 刘杨, 等. 数字低空融合运行空中交通管理技术\[J\]. 航空学报, 2025, 46(11): 531331.
- \[2\]Pu Fan, Chen Zhijie, Liu Yang, et al. Air Traffic Management Technology for Digital Low-altitude Integrated Operations\[J\]. Acta Aeronautica et Astronautica Sinica, 2025, 46(11): 531331.
- \[3\]Garrow L A, German B J, Leonard C E. Urban Air Mobility: A Comprehensive Review and Comparative Analysis with Autonomous and Electric Ground Transportation for Informing Future Research\[J\]. Transportation Research Part C, 2021, 132: 103377.
- \[4\]国家空管委. 国家空域基础分类方法\[S\]. 2023.
- \[5\]National Airspace Management Committee. National Airspace Basic Classification Method\[S\]. 2023.
- \[6\]国务院. 无人驾驶航空器飞行管理暂行条例\[S\]. 国务院令第761号, 2023.
- \[7\]The State Council. Interim Regulations on the Flight Management of Unmanned Aircraft\[S\]. State Council Decree No. 761, 2023.
- \[8\]亿欧智库. 2024中国低空经济行业研究报告\[R\]. 北京: 亿欧智库, 2024.
- \[9\]EqualOcean Intelligence. 2024 China Low-altitude Economy Industry Research Report\[R\]. Beijing: EqualOcean Intelligence, 2024.
- \[10\]Federal Aviation Administration. Unmanned Aircraft System (UAS) Traffic Management (UTM) Concept of Operations\[R\]. Washington DC: FAA, 2020.
- \[11\]Laudeman I V, Shelden S G, Branstrom R, et al. Dynamic Density: An Air Traffic Management Metric\[R\]. Moffett Field: NASA Ames Research Center, 1998.
- \[12\]Delahaye D, Puechmorel S. Air Traffic Complexity: Towards Intrinsic Metrics\[C\]//3rd USA/Europe ATM R&D Seminar. Napoli: Eurocontrol, 2000: 1-11.
- \[13\]Delahaye D, García A, Lavandier J, et al. Air Traffic Complexity Map Based on Linear Dynamical Systems\[J\]. Aerospace, 2022, 9(5): 230.
- \[14\]温瑞英, 何家兴, 王红勇. 支持稳定航迹优化的空中交通多元复杂度计算方法\[J\]. 交通运输系统工程与信息, 2025, 25(1): 258-269.
- \[15\]Wen Ruiying, He Jiaxing, Wang Hongyong. A Multi-element Complexity Calculation Method for Air Traffic Supporting Stable Trajectory Optimization\[J\]. Journal of Transportation Systems Engineering and Information Technology, 2025, 25(1): 258-269.
- \[16\]张博为, 田文. 基于IAHP-熔权法的空域复杂度评估方法\[J\]. 航空计算技术, 2025, 55(5): 74-78, 86.
- \[17\]Zhang Bowei, Tian Wen. Airspace Complexity Evaluation Method Based on IAHP and Fusion Weighting\[J\]. Aeronautical Computing Technique, 2025, 55(5): 74-78, 86.
- \[18\]Sunil E, Hoekstra J, Ellerbroek J, et al. Metropolis: Relating Airspace Structure and Capacity for Extreme Traffic Densities\[C\]//11th USA/Europe ATM R&D Seminar. Lisbon: Eurocontrol/FAA, 2015: 1-10.
- \[19\]Wang Z, Delahaye D, Farges J L, et al. Complexity Optimal Air Traffic Assignment in Multi-layer Transport Network for Urban Air Mobility Operations\[J\]. Transportation Research Part C, 2022, 142: 103776.
- \[20\]Li Z, Peng J, Xu Z. A Deep Unsupervised Learning Approach for Airspace Complexity Evaluation\[J\]. IEEE Transactions on Intelligent Transportation Systems, 2022, 23(8): 11739-11750.
- \[21\]Alharbi A, Petrunin I, Panagiotakopoulos D. Deep Learning Architecture for UAV Traffic-density Prediction\[J\]. Drones, 2023, 7(2): 78.
- \[22\]付翌蕊, 陈海燕, 周智慧, 等. 基于多尺度时空图像和深度度量的空域交通复杂度评估\[J\]. 计算机工程, 2025. DOI: 10.19678/j.issn.1000-3428.0070484.
- \[23\]Fu Yirui, Chen Haiyan, Zhou Zhihui, et al. Airspace Traffic Complexity Evaluation Based on Multi-scale Spatio-temporal Images and Deep Metric Learning\[J\]. Computer Engineering, 2025. DOI: 10.19678/j.issn.1000-3428.0070484.
- \[24\]Li B Y, Li Z H, Chen J, et al. MAST-GNN: A Multimodal Adaptive Spatio-Temporal Graph Neural Network for Airspace Complexity Prediction\[J\]. Transportation Research Part C, 2024, 160: 104521.
- \[25\]Pérez Moreno F, Ibáñez Rodríguez F, Gómez Comendador V F, et al. Prediction of Air Traffic Complexity Through a Dynamic Complexity Indicator and Machine Learning Models\[J\]. Journal of Air Transport Management, 2024, 119: 102632.
- \[26\]李谋, 胡明华, 张颖, 等. 有人与无人融合运行空域航迹复杂度优化研究\[C\]//第八届中国航空科学技术大会论文集. 2025: 1094-1102.
- \[27\]Li Mou, Hu Minghua, Zhang Ying, et al. Research on Trajectory Complexity Optimization in Manned and Unmanned Integrated Airspace Operations\[C\]//Proceedings of the 8th China Aeronautical Science and Technology Conference. 2025: 1094-1102.
- \[28\]张进, 胡明华, 张晨. 空中交通管理中的复杂性研究\[J\]. 航空学报, 2009, 30(11): 2132-2142.
- \[29\]Zhang Jin, Hu Minghua, Zhang Chen. Research on Complexity in Air Traffic Management\[J\]. Acta Aeronautica et Astronautica Sinica, 2009, 30(11): 2132-2142.
- \[30\]Shi X, Chen Z, Wang H, et al. Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting\[C\]//Advances in Neural Information Processing Systems 28. Montreal: Curran Associates, 2015: 802-810.
- \[31\]Zhang J, Zheng Y, Qi D. Deep Spatio-temporal Residual Networks for Citywide Crowd Flows Prediction\[C\]//Proceedings of the 31st AAAI Conference on Artificial Intelligence. San Francisco: AAAI Press, 2017: 1655-1661.
- \[32\]ASTM International. ASTM F3411-22a: Standard Specification for Remote ID and Tracking\[S\]. 2022.
- \[33\]Loshchilov I, Hutter F. Decoupled Weight Decay Regularization\[C\]//7th International Conference on Learning Representations. New Orleans: OpenReview.net, 2019.

顶部

返回顶部