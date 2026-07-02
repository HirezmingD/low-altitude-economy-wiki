# 面向eVTOL航空器的城市空中运输交通管理综述
**期刊**：交通运输工程学报
Vol.20 No.4 Aug.2020
文章编号:1671-1637(2020)04-0035-20
DOI:10.19818/j.cnki.1671-1637.2020.04.003
## 作者信息
李诚龙¹,屈文秋¹,李彦冬¹,黄龙杨¹,卫 鹏²
1. 中国民用航空飞行学院空中交通管理学院,四川广汉 618307;
2. 乔治·华盛顿大学机械与航空航天工程学院,华盛顿特区 20052
作者简介:李诚龙(1990-),男,四川绵阳人,中国民用航空飞行学院讲师,从事无人机空中交通管理、城市空中交通与自主驾驶研究,lcl@cafuc.edu.cn
## 基金项目
国家自然科学基金项目(U1733105);民航安全能力建设项目(0241928);中央高校基本科研业务费专业资金项目(CJ2018-02);中央高校教育教学改革专项项目(E2020083);四川省大学生创新创业训练计划项目(S201910624031)
## 引用格式
李诚龙,等.面向eVTOL航空器的城市空中运输交通管理综述[J].交通运输工程学报,2020,20(4):35-54.
## 关键词
航空运输;城市空中交通;eVTOL;空域规划;运行控制;通信导航监视
### 中图分类号
V355
### 文献标志码
A
## 摘要
### 中文摘要
回顾了城市空中运输(UAM)的起源与发展演变,定义了UAM交通管理基本概念,分析了催生UAM的社会和技术因素,提出了面向近未来时期国家层面UAM交通管理的基础架构,将基于eVTOL的UAM交通管理问题划分为3个方面进行讨论(空域规划、地面基础设施、交通规则与运行控制),并对近年来UAM交通管理相关文献所提出的代表性观点进行了梳理,总结了UAM近未来时期所需解决的关键问题,展望了UAM交通管理未来的发展趋势。研究结果表明:空域规划方面,UAM需要对现有低空非管制空域进行更精细化的规划管理,结构化的空域划设方式应该在UAM交通管理初期被应用,高度层空域结构能较好地平衡运行安全和空域容量之间的矛盾;地面基础设施方面,需通过城市OD数据预测UAM的交通需求来进行垂直起降站点选址,选址管理将直接影响空中航线网络和通信导航监视台站布设;交通规则与运行控制方面,UAM将面临有人机、无人机复杂融合运行场景,交通规则需与现有运输航空规则兼容,高带宽通信会推动运行模式向空地协同自主决策转型,人机权责界定是未来管控核心难点。总体而言,UAM交通管理体系将与现有无人机交通管理(UTM)逐步融合,我国大概率采用集中管理、试点运行、有序放开的发展路径。
### Abstract
Overview of traffic management of urban air mobility(UAM)with eVTOL aircraft
LI Cheng-long 1,QU Wen-qiu 1,LI Yan-dong 1,HUANG Long-yang 1,WEI Peng 2
(1.College of Air Traffic Management,Civil Aviation Flight University of China,Guanghan 618307, Sichuan,China;2.Department of Mechanical and Aerospace Engineering, George Washington University,Washington DC 20052)
Abstract:The emergence and development of urban air mobility(UAM)were reviewed,the basic concept of UAM traffic management was defined,and the social and technical factors promoting the UAM industry were analyzed.A nationwide framework of UAM traffic management for the near future was proposed.The UAM traffic management issues based on the electric vertical take-off and landing(eVTOL)aircraft were divided into three aspects for discussion(airspace planning,ground infrastructure,traffic rules and operation control).The representative views put forward by related literatures of UAM traffic management in the past few years were sorted out.The key issues that UAM needs to solve in the near future were summarized,and the development trend of UAM traffic management in the future was prospected.Research result shows that in terms of airspace planning,the UAM needs more refined planning and management of existing low-altitude uncontrolled airspace.The structured airspace demarcation method should be applied in the initial stage of UAM traffic management.The flight layer airspace structure can better balance the contradiction between operational safety and airspace capacity.In terms of ground infrastructure,the UAM traffic demand predicted by urban OD data can be used for the location selection of vertiports.Also,the vertiport site management will directly affect the structure of air route network and the layout of communication,navigation, and surveillance(CNS)stations.In terms of traffic rules and operation control,more complex UAVs and manned aircraft integration operation scenarios will be directly faced by the UAM. The UAM traffic rules need to be innovated and compatible with existing transportation aviation traffic rules.High-bandwidth communication technology will promote the transformation of UAM operation control to air-ground coordinated decision-making and self-pilot.How to deal with the relationship between human and air traffic control system is very important to the future air traffic management.In general,UAM traffic management will likely intersect and gradually integrate with the existing UAS traffic management system.Facing this new mode of transportation,our country will be more likely to adopt the traffic management development route of centralized management,pilot operation,and orderly deregulation.
Key words:air transportation;urban air mobility;eVTOL;airspace planning;operation control; CNS
4tabs,13figs,76refs.
## 0 引言
伴随着电力推进、自动驾驶、5G通信等多领域技术突破,城市空中运输(Urban Air Mobility, UAM)概念被Uber、NASA、Airbus、Embraer、MITRE、亿航等机构相继提出并引起全球航空运输市场广泛关注。罗兰贝格调研指出市区机场摆渡、空中出租车、城际短途航班是UAM核心落地场景。
eVTOL相比直升机具备按需调度、人力成本低、空域使用灵活、噪声更低的优势,且可多层高度运行,能大幅减少地面交通拥堵带来的航班延误。
NASA定义广义UAM包含载人、物流两类场景:
1. 物流领域:京东、亚马逊2015年前布局末端配送无人机,国内企业先乡村后城市试点;城市配送对无人机适航、智能化、公众信任要求更高。
2. 载人领域市场规模与盈利潜力更大,近5年文献研究多聚焦载人eVTOL,主流机型分为多旋翼、倾转旋翼、复合固定旋翼三类(Volocopter 2X、EHang216、Airbus Vahana、Kitty Hawk Cora为典型机型)。
本文整体框架:
第1节 UAM概念、发展阶段、驱动因素、顶层管理框架;
第2节 空域规划(空域范围、航路结构、空域容量);
第3节 地面基础设施(垂直起降站选址与场面运行、通信导航监视地面基站);
第4节 交通规则与运行控制(飞行规则、战术/战略流量管控、签派能耗优化);
第5节 结论与关键研究方向展望。
![图1 基于eVTOL载运具的UAM](https://p-flow-sign.bytedance.net/tos-cn-i-ik7evvg4ik/96f2edbf3eb74ef3aab5c457b3e7f53f#img1)
图1 基于eVTOL载运具的UAM
## 1 UAM交通管理基本概念与发展演变
### 1.1 基本概念
UAM是以eVTOL航空器为核心载体,在城市低空空域开展载人、载货短途运输的新型交通模式,短期会与直升机、轻小型无人机共用低空空域,具备航空计划性+地面共享出行即时响应双重特征。现有UTM系统仅适配120m以下小型无人机,无法覆盖载人eVTOL运行需求,亟需独立配套交通管理体系。
UAM交通管理三大核心目标:
1. 安全:事故率远期接近干线民航,近期控制为地面驾车2倍以内;
2. 效率:缩短城市通勤耗时;
3. 环保:低噪声、低碳排放运行。
### 1.2 城市空中运输三阶段发展历程
1. **直升机商用起步阶段(1947—1971)**
美洛杉矶、纽约航空公司开通城市直升机固定航线,高峰期年客运量120万人次,配套空中出租包机业务;多起坠机重大事故后企业停运,城市空中运输进入低谷。此阶段空域为目视报告空域,无专用监视通信设施,依靠飞行员目视间隔。
2. **私人飞行器理论阶段(2000年后)**
NASA提出PAV私人飞行器概念,主打城市短途家用低空出行;同期UTM无人机交通管理框架诞生,针对120m以下无人机动态空域、电子围栏管控。
3. **eVTOL规模化研发阶段(2015至今)**
Uber Elevate白皮书、NASA UML成熟度模型发布,全球企业投入载人eVTOL样机研发;圣保罗等拥堵城市启动低空转型。现有传统ATC管制体系无法支撑千架级高密度eVTOL同时运行。
![图2 UAM成熟度模型](https://p-flow-sign.bytedance.net/tos-cn-i-ik7evvg4ik/96f2edbf3eb74ef3aab5c457b3e7f53f#img2)
图2 UAM成熟度模型
UML六层级划分:UML1初始样机测试→UML2小规模商业示范→UML3中等密度常态化运行→UML4百架级集群运行→UML5千架高密度自动化运行→UML6万台级全域普及。
### 1.3 技术驱动因素
1. **载运具革新**
电力分布式推进简化机身结构、降低运营人力成本;自主远程驾驶释放载荷空间。但锂电池能量密度远低于燃油,限制续航与载重,是当前核心技术瓶颈。eVTOL分布式桨叶可降低气动噪声,适配城市居民区上空运行。
2. **通信导航监视升级**
ADS-B、北斗/GNSS、5G蜂窝网络为UAM核心支撑;城市高楼遮挡、基站布设成本约束全域监视覆盖,发展初期优先采用结构化空域降低感知压力,成熟后逐步开放自由飞行。
### 1.4 社会经济驱动因素
全球城市化率突破50%,超大城市地面通勤拥堵严重,北京六环日均通勤56分钟、洛杉矶居民年通勤耗时280小时。UAM可将通勤时长压缩至1/5,定价对标高端网约车。
同时城市碳减排、噪声治理需求推动电动低空飞行器落地,但锂电储能短板限制大规模普及。
### 1.5 UAM四层管理顶层框架
四类参与主体:
1. 政府监管部门:立法、行业宏观监察;
2. UAM交通运营服务商:空域规划、设施保障、空中管制执行;
3. 航空承运人/航空器所有者:遵守空域规则开展运营;
4. 出行用户:服务消费群体。
本文空域、地面设施、运行控制三大核心内容归属服务商与承运人交互业务范畴。
## 2 空域规划
### 2.1 空域范围划分
FAA空域分级:
- A级高空干线空域(5400m以上):仅干线民航使用,UAM不进入;
- B/C/D级机场周边管制空域:eVTOL起降阶段少量占用;
- E/G级低空过渡/非管制空域:UAM核心巡航运行空域(120m以上);
- UTM管控层:120m以下小型无人机专属空域。
载人eVTOL巡航高度突破120m,会与低空无人机、直升机产生空域重叠,NASA提出UTM系统向上拓展兼容UAM的改造方案。
![图3 空域分级示意图](https://p-flow-sign.bytedance.net/tos-cn-i-ik7evvg4ik/96f2edbf3eb74ef3aab5c457b3e7f53f#img3)
图3 空域分级
AGL为距地面高度;MSL为平均海平面高度
城市空域划定约束条件:高层建筑安全缓冲、机场禁飞缓冲区、重点保护区域禁飞管控,基于拓扑算法可实现三维可用空域自动评估。
### 2.2 空域结构与航路划设
两大空域使用模式:结构化分层走廊、全域自由混合飞行。近中期优先结构化分层方案,成熟后逐步开放自由空域。
#### (1)水平航路三类方案
表1 城市低空空域水平航路结构设置
|设置方式|适用场景|优势|弊端|
| ---- | ---- | ---- | ---- |
|点对点直达航路|试运行、城市机场通勤|路径最短,规则简单|大量交汇冲突,对头碰撞风险高|
|沿地面路网/河道走廊|中等规模试点、低空出租|冲突点可控,降低地面坠物伤害风险|空域利用率低,绕行增加耗时能耗|
|空域网格化动态分配|成熟规模化运行|门到门灵活路径,空域容量高|依赖全域中心化调度系统,技术门槛极高|
#### (2)垂直高度分层方案
Metropolis项目标准分层:每90m(300英尺)一个高度层,单高度层限定45°航向区间,减小航空器相对速度、降低平面冲突。
![图6 高度层-空域模型](https://p-flow-sign.bytedance.net/tos-cn-i-ik7evvg4ik/96f2edbf3eb74ef3aab5c457b3e7f53f#img5)
图6 高度层-空域模型
最低巡航高度双重约束:
1. 噪声阈值:距地面80m高度噪声≤67dB;
2. 建筑超障:超大城市核心区大量建筑高于50m,局部超高楼宇(25层以上)需侧向绕飞。
![图5 成都市楼宇高度分布](https://p-flow-sign.bytedance.net/tos-cn-i-ik7evvg4ik/96f2edbf3eb74ef3aab5c457b3e7f53f#img4)
图5 成都市楼宇高度分布
(a)超过15层建筑分布;(b)超过25层建筑分布
### 2.3 空域容量演进路线
![图7 UAM空域容量增长路线](https://p-flow-sign.bytedance.net/tos-cn-i-ik7evvg4ik/96f2edbf3eb74ef3aab5c457b3e7f53f#img6)
图7 UAM空域容量增长路线
1. 低密度阶段:目视飞行、传统通信监视,容量受限;
2. 中密度阶段:仪表规则、基础自动化调度,容量提升;
3. 高密度成熟阶段:自主避障、全域感知、一体化UTM服务,空域容量大幅提升。
短期依靠结构化分层扩容,长期依托机载自主避障缩小安全间隔、提升空域承载量。自由飞行模式下马尔可夫决策、蒙特卡洛树搜索等算法可实现极限容量仿真测算。
## 3 地面基础设施
分为垂直起降场站、通信导航监视地面基站两大板块。
### 3.1 垂直起降站(Vertiport)
#### (1)选址影响因子
核心约束:地面噪声影响、人口密度、城市OD出行流量、现有交通枢纽接驳(火车站、楼顶、老旧直升机坪复用),采用GIS层次分析法综合多因子筛选站点。
#### (2)场站场面运行与容量模型
![图8 垂直起降机场场面运行管理](https://p-flow-sign.bytedance.net/tos-cn-i-ik7evvg4ik/96f2edbf3eb74ef3aab5c457b3e7f53f#img7)
图8 垂直起降机场场面运行管理
场站功能分区:到达队列、进近定位点、起降区、停机位、登机口;航空器着陆后推出至登机区,完成载客后离场起飞。
![图9 垂直起降机场容量包线模型](https://p-flow-sign.bytedance.net/tos-cn-i-ik7evvg4ik/96f2edbf3eb74ef3aab5c457b3e7f53f#img8)
图9 垂直起降机场容量包线模型
容量包线以单位时间进出港航空器数量为坐标轴,划分自由起降区间、删去饱和区间,用于场站规模测算。
eVTOL垂直起降特性降低周边建筑超障要求,适配城市屋顶小型场站落地。
### 3.2 通信导航监视(CNS)地面设施
表2 运输航空与UAM所需通信导航监视设备对比
|项目|干线运输航空|城市空中交通UAM|
| ---- | ---- | ---- |
|通信服务|VHF甚高频、ACARS低速数据链|5G蜂窝通信、机载自组网Ad-Hoc|
|导航服务|VOR/DME、ILS仪表着陆、GNSS惯性组合|北斗/GNSS+3D城市高程地图、基站辅助定位、视觉辅助导航|
|监视手段|一/二次雷达、ADS-B广播|5G协同监视、机间自组网无源探测|
|管制模式|管制员语音指挥|自动化中心调度+远程人工应急监控|
|飞行情报|机场、航路气象播报|全域流量、机位、低空气象、尾流实时推送|
|告警机制|应答机告警|全域5G主动故障广播|
传统甚高频、雷达覆盖成本高,无法适配城市峡谷;5G蜂窝网络为核心方案,需定向调整基站天线辐射方向实现低空多层覆盖。
中心化平台存在单点失效风险,机载Ad-Hoc自组网作为分布式备份,故障时机载自主协同避撞。
## 4 交通规则与运行控制
### 4.1 现有飞行规则适配对比
表3 VFR/IFR/UTM规则优缺点对比
|规则|优点|缺点|
| ---- | ---- | ---- |
|VFR目视规则|管制自由度高|依赖天气,空域容量低,无法夜间运行|
|IFR仪表规则|全时段全气象运行适配|适配人控大型民航,高密度低空扩展性差|
|UTM无人机规则|低空大容量管控体系|仅覆盖120m以下,不支持载人eVTOL高空巡航|
适配UAM创新规则:增强目视规则、动态分配空中走廊、基于机载性能差异化空域准入,难点在于不同机型气动、机载设备性能差异大,统一规则制定难度高。
### 4.2 空中交通管制与流量控制
分为战术实时调度、战略流量调控两类。
#### (1)战术管制(进场排序、冲突解脱)
针对起降点拥堵,混合整数规划、深度强化学习(DQN)可优化航空器进近顺序,平衡电池续航、场站容量双重约束。
![图10 eVTOL进场运行概念](https://p-flow-sign.bytedance.net/tos-cn-i-ik7evvg4ik/96f2edbf3eb74ef3aab5c457b3e7f53f#img9)
图10 eVTOL进场运行概念
(a)进场水平面;(b)进近侧视剖面
建立Fe3仿真平台用于各类避撞、排序算法标准化对比测试。
#### (2)战略流量管理
参考民航GDP地面延误程序、CTOP协同航迹调整方案:优先地面等待(能耗更低),通过路径重分配疏导空域拥堵;适配UAM短途、随机出行特征。
### 4.3 签派运行与能耗优化
eVTOL垂直爬升/悬停能耗远高于水平巡航,不合理剖面大幅缩减续航。
![图12 eVTOL航空器进近下滑剖面优化](https://p-flow-sign.bytedance.net/tos-cn-i-ik7evvg4ik/96f2edbf3eb74ef3aab5c457b3e7f53f#img10)
图12 eVTOL航空器进近下滑剖面优化
最优策略:垂直爬升至安全高度后斜向巡航进近,减少垂直悬停耗时;针对多旋翼、倾转旋翼不同机型可建立专属能耗下滑模型。
## 5 结论与展望
### 5.1 核心研究框架对比
![图13 传统ATM与UAM管理框架对比](https://p-flow-sign.bytedance.net/tos-cn-i-ik7evvg4ik/96f2edbf3eb74ef3aab5c457b3e7f53f#img11)
图13 传统空中交通管理与UAM交通管理问题框架对比
传统ATM分为空域、交通服务、流量管理独立模块;UAM采用空地协同一体化框架,整合空域规划、地面设施、运行控制三大板块联动优化。
### 5.2 三大领域关键待解决问题
#### （1）空侧空域管理
1. 清晰界定UAM、无人机、直升机、干线民航空域使用边界与共用区域;
2. 统一结构化航路设计标准(层高、走廊宽度、安全超障、转弯半径);
3. 构建混合机型高密度空域容量量化评估体系。
#### （2）陆侧地面设施
1. 依托城市地面出行OD数据建立UAM客流预测与场站选址模型;
2. 低成本5G低空全域通信监视基站组网方案设计。
#### （3）运行管控体系
1. 多机型融合统一低空交通规则体系;
2. 中心化空管平台与分布式机载自主管控优劣平衡;
3. 自动驾驶航空器、管制人员之间安全间隔、事故责任划分标准。
### 5.3 行业发展总结展望
国内城市人口基数庞大,UAM市场需求潜力充足,但载人eVTOL适航审定标准严苛,产业落地优先采用“远郊试点、逐步进城”路径。
国内低空交通管理发展路线:集中统筹、分区域试点、循序渐进有序放开。
长期发展趋势:
1. 空地一体化协同管控成为主流模式;
2. 机载感知、分布式自组网降低中心系统依赖;
3. AI算法全面介入流量调度、冲突解脱;
4. 短期分层结构化空域为主,远期逐步开放全域自由混合飞行。
## 参考文献
[1] MENOUAR H,GUVENC I,AKKAYA K,et al.UAVenabled intelligent transportation systems for the smart city[J].IEEE Communications Magazine,2017,55(3):22-28.
[2] HOLD J,GOEL N.Fast-forwarding to a future of ondemand urban air transportation[R].San Francisco:Uber Elevate,2016.
[3] THIPPHAVONG P,APAZA R,BARMORE B,et al.Urban airspace integration concepts and considerations[C]// AIAA.2018Aviation Technology,Integration,and Operations Conference.Reston:AIAA,2018:3676-3681.
[4] BALAKRISHNAN K,POLASTRE J,MOOBERRY J,et al. Blueprint for the sky.The roadmap for the safe integration of autonomous aircraft[R].Santa Clara Valley:Airbus A3, 2018.
[5] EmbraerX.Flight plan 2030:an air traffic management concept for urban air mobility[R].Duskamp:EmbraerX,2019.
[6] LASCARA B,SPENCER T,DEGARMO M,et al.Urban air mobility landscape report[R].McLean:MITRE,2018.
[7] XU H X.The future of transportation:white paper on urban air mobility systems[R].Guangzhou:EHang,2020.
[8] BAUR S,SCHICKRAM S,HOMULENKO A,et al.Urban air mobility:the rise of a new mode of transportation[R]. Hamburg:Roland Berger,2018.
[9] ZHAO Jing,XIE Feng-jie.Cognitive and artificial intelligence system for logistics industry[J].International Journal of Innovative Computing Applications,2020,11(2/3):84-88.
[10] 吴永鑫.物流无人机在中国农村电商物流市场应用研究[D]. 深圳:深圳大学,2017.
[11] 张丹,吴陈炜,谢安桓.城市交通问题的空中解决方案——自主载人飞行器研究综述[J].无人系统技术,2018,1(2):1-13.
[12] REICHE C,MCGILLEN C,SIEGEL J,et al.Are we ready to weather urban air mobility(UAM)?[C]∥IEEE.2019 Integrated Communications,Navigation and Surveillance Conference(ICNS).New York:IEEE,2019:1-7.
[13] SALLEH M,TAN D Y,KOH C H,et al.Preliminary concept of operations(ConOps)for traffic management of unmanned aircraft systems(TM-UAS)in urban environment[C]∥ AIAA.Information Systems—AIAA Infotech@Aerospace Infotech.Reston:AIAA,2017:1-13.
[14] Joint DOT/NASA.Concepts studies for future intracity air transportation systems[R].Cambridge:Massachusetts Institute of Technology,1970.
[15] DAJANI J S,WARNER D,EPSTEIN D,et al.The role of the helicopter in transportation[R].Durham:Duke University, 1976.
[16] MOORE M D.Personal air vehicles:a rural/regional and intraurban on-demand transportation system[J].Journal of the American Institute of Aeronautics and Astronautics,2003, 2646:1-20.
[17] CHAMBERS J R.Innovation in flight:research of the NASA Langley Research Center on revolutionary advanced concepts for aeronautics[R].Hampton:National Aeronautics and Space Administration(NASA),2005.
[18] KOPARDEKAR P.Unmanned aerial system(UAS)traffic management(UTM):enabling low-altitude airspace and UAS operations[R].Hampton:National Aeronautics and Space Administration(NASA),2014.
[19] JOHNSON W C.UAM coordination and assessment team (UCAT)[R].Ames:National Aeronautics and Space Administration (NASA),2019.
[20] VASCIK P D,HANSMAN J.Scaling constraints for urban air mobility operations:air traffic control,ground infrastructure, and noise[C]∥AIAA.2018Aviation Technology,Integration,and Operations Conference.Reston:AIAA,2018:3849-3875.
[21] SHIHAB S A M,WEI Peng,SHI Jie,et al.Optimal eVTOL fleet dispatch for urban air mobility and power grid services[C]∥ AIAA.Aviation 2020Forum.Reston:AIAA,2020:1-17.
[22] GEORGE H,WEI Peng.Service-oriented separation assurance for small UAS traffic management[C]∥IEEE.2019Integrated Communications,Navigation and Surveillance Conference (ICNS).New York:IEEE,2019:1-11.
[23] National Academiesof Sciences.Advancing aerial mobility:a national blueprint[R].Washington DC:The National Academies Press,2020.
[24] POLACZYK N,TROMBINO E,WEI P,et al.A review of current technology and research in urban on-demand air mobility applications[C]∥RAM J,KENDRA B.8th Biennial Autonomous VTOL Technical Meeting and 6th Annual Electric VTOL Symposium.Washington DC:FAA, 2019:1-11.
[25] 全权,李刚,柏艺琴,等.低空无人机交通管理概览与建议[J].航空学报,2020,41(1):6-34.
[26] SHIHAB S A M,WEI P,RAMIREZ D S J,et al.By schedule or on demand?a hybrid operation concept for urban air mobility[C]∥AIAA.Aviation 2019Forum.Reston:AIAA, 2019:1-13.
[27] 联合国人居署.2016世界城市状况报告[R].内罗毕:联合国人居署,2019.
[28] 北京交通发展研究院.北京市居民公共交通出行特征分析 [R].北京:北京交通发展研究院,2019.
[29] VASCIK P D,HANSMAN J.Evaluation of key operational constraints affecting on-demand mobility for aviation in the Los Angeles basin:ground infrastructure,air traffic control and noise[C]∥AIAA.2017:1-20.
[30] VASCIK P D,HANSMAN R J.Constraint identification in on-demand mobility for aviation through an exploratory case study of los angeles[C]∥AIAA,2017:1-26.
[31] 弓永峰,陈俊斌,刘海博,等.燃料电池行业专题报告[R].北京:中信证券,2019.
[32] 王莉,戴泽华,杨善水,等.电气化飞机电力系统智能化设计研究综述[J].航空学报,2019,40(2):5-19.
[33] 中国民用航空局航空器适航审定司.基于运行风险的无人机适航审定指导意见[R].北京:民航局,2019.
[34] MUELLER E.Enabling airspace integration for high density urban air mobility[R].Ames:NASA,2017.
[35] VASCIK P D,BALAKRISHNAN H,HANSMAN J.Assessment of air traffic control for urban air mobility and unmanned systems[C]∥FAA&EUROCONTROL,2018:1-9.
[36] CHO J,YOON Y.How to assess the capacity of urban airspace: a topological approach using keep-in and keep-out geofence[J]. Transportation Research Part C:Emerging Technologies, 2018,92:137-149.
[37] VASCIK P D,CHO J,BULUSU V,et al.Geometric approach towards airspace assessment for emerging operations[C]∥ AIAA,2019:1-12.
[38] ZHU Guo-dong,WEI Peng.Pre-departure planning for urban air mobility flights with dynamic airspace reservation[C]∥ AIAA,2019:1-11.
[39] ZHU Guo-dong,WEI Peng.Low-altitude UAS traffic coordination with dynamic geofencing[C]∥AIAA,2016:1-16.
[40] SUNIL E,ELLERBROEK J,HOEKSTRA J.Metropolisurban airspace design[R].Delft:NLR,2014.
[41] VIDOSAVLJEVIC A,DELAHAYE D,SUNIL E,et al. Complexity analysis of the concepts of urban airspace design[C]∥EIWAC,2015:1-11.
[42] SUNIL E,HOEKSTRA J,ELLERBROEK J,et al.Metropolis: rel1ensities[C]∥EUROCONTROL,2015:1-11.
[43] SUNIL E,HOEKSTRA J,ELLERBROEK J,et al.The influence of traffic structure on airspace capacity[C]∥ FAA&EUROCONTROL,2016:1-9.
[44] SUNIL E,ELLERBROEK J,HOEKSTRA J.An analysis of decentralized airspace structure and capacity using fast-time simulations[J].Journal of Guidance,Control,and Dynamics,2017,40(1):38-51.
[45] BOSSON C,LAUDERDALE T A.Simulation evaluations of an autonomous urban air mobility network management and separation service[C]∥AIAA,2018:1-14.
[46] SALLEH M F B,CHI Wan-chao,WANG Zhen-kun,et al. Adaptive urban airspace management[C]∥AIAA,2018:1-12.
[47] ARNTZ M,AALMOES R,BUSSINK F.Noise computation for future urban air traffic systems[R]. Amsterdam:NLR,2015.
[48] HOEKSTRA J,MAAS J,SUNIL E.How layered airspace design parameters affect airspace capacity[C]∥ FAA&EUROCONTROL,2016:1-8.
[49] GOODRICH K H,BARMORE B.Exploratory analysis of airspace throughput[C]∥AIAA,2018:1-9.
[50] KOCHENDERFER M J,HOLLAND J E,CHRYSSANTHACOPOUL J.Next-generation airborne collision avoidance system[R].Lexington:MIT,2012.
[51] YU Xiang,ZHANG You-min.Sense and avoid technologies review[J].Progress in Aerospace Sciences,2015,74:152-166.
[52] YANG Xu-xi,WEI Peng.Autonomous on-demand free flight[C]∥ FAA&EUROCONTROL,2018:1-8.
[53] YANG Xu-xi,DENG Li-seng,WEI Peng.Multi-agent autonomous free flight[C]∥AIAA,2019:1-13.
[54] FU Meng-ying,ROTHFELD R,ANTONIO C.慕尼黑出行需求仿真[J].Transportation Research Record,2019(2673):427-442.
[55] ROTHFELD R,BALAC M,PLOETNER K.Agentbased UAM仿真[C]∥AIAA,2018:1-10.
[56] FADHIL D N.基于GIS的UAM选址分析[D].慕尼黑工业大学,2018.
[57] VASCIK P,HANSMAN J.垂直起降机场容量包线分析[C]∥AIAA,2019:1-26.
[58] 杨秀玉.5G无人机防相撞技术[D].中国民航飞行学院,2019.
[59] HOSSEINI N,JAMAL H,HAQUE J.无人机5G通信综述[C]∥IEEE,2019:1-10.
[60] GUPTA L,JAIN R.无人机通信网络综述[J]IEEE Communications Surveys and Tutorials,2015,18(2):1123-1152.
[61] PRADE P.eVTOL进场调度[D].爱荷华州立大学,2019.
[62] KLEINBEKMAN I.混合整数规划进近排序[C]∥IEEE,2018:1-7.
[63] BRITTAIN M.深度强化学习航空器排序[C]∥ FAA&EUROCONTROL,2018:1-8.
[64] XUE Min.Fe3低空仿真平台[C]∥AIAA,2018:1-13.
[65] BELOBABA P.全球航空行业模型[R].Wiley,2015.
[66] BALL M O.地面延误随机整数规划[J].Operations Research,2003,51(1):167-171.
[67] ZHU Guo-dong.协同航迹优化模型[C]∥AIAA,2019:1-16.
[68] HOFFMAN R.协同航迹多阶段随机分配[C]∥IEEE,2018:1-10.
[69] SILVA C.多旋翼eVTOL任务剖面[C]∥AIAA,2018:1-10.
[70] PRADE P.倾转旋翼能耗下滑剖面[J]. Journal of Aerospace Information Systems,2019,16(7): 263-277.
[71] 陈志杰.未来空管系统技术挑战[J].指挥信息系统与技术,2016,7(6):1-5.
[72] PATHIYIL L.城市无人机安全运行研究[C]∥德国导航学会,2016:1-10.当前文件内容过长，豆包只阅读了前 16%。