---
title: "Sky highway: An air traffic structure for low-altitude heterogeneous VTOL aircraft"
source: "https://www.sciencedirect.com/science/article/pii/S0968090X26000197?pes=vor&utm_source=clarivate&getft_integrator=clarivate"
author:
  - "[[Quan Quan]]"
  - "[[Jack Haddad]]"
published:
created: 2026-07-01
description: "The development of a new mode of air transport, i.e., low alti tude aircraft, rises with the advancement of aviation and communication technologies. T…"
tags:
  - "clippings"
---
## Published by: Elsevier

### Published by

[![Elsevier](https://sciencedirect.elseviercdn.cn/prod/8c5bb82080b0f791d6ca95759147bab0d0e4e18d/image/elsevier-non-solus.svg)](https://www.sciencedirect.com/journal/transportation-research-part-c-emerging-technologies "Go to Transportation Research Part C: Emerging Technologies on ScienceDirect")

## FMS BEI检索SCI升级版 工程技术1区SCI Q1IF 8.4

,,,

[View **PDF**](https://www.sciencedirect.com/science/article/pii/S0968090X26000197/pdfft?md5=3b60868d84510cca8fead0254ff58274&pid=1-s2.0-S0968090X26000197-main.pdf)

[10.1016/j.trc.2026.105531](https://doi.org/10.1016/j.trc.2026.105531)

## Keywords

Low-altitude aircraft

;

Urban air mobility

;

Air traffic management

;

Swarm

;

Airspace structure design,

- [Previous article in this issue](https://www.sciencedirect.com/science/article/pii/S0968090X26000410)
- [Next article in this issue](https://www.sciencedirect.com/science/article/pii/S0968090X26000604)

## Nomenclature

$\mathcal{G}_{i} , \mathcal{N}_{i} , \mathcal{E}_{i} , \mathcal{W}_{i}$

Undirected graph, node set, edge set and weighted adjacency matrix of the ith layer

*n* <sub><em>i,j</em></sub>

Element of the node set $\mathcal{N}_{i}$ with the index j

$\left(n_{i , j_{1}} , n_{i , j_{2}}\right)$

Element of the node set $\mathcal{E}_{i}$

**p** <sub><em>i,j</em></sub>

Position of the node *n* <sub><em>i,j</em></sub>

$\mathcal{N}_{i , \text{e}} , \mathcal{N}_{i , \text{c}} , \mathcal{N}_{i , \text{h}}$

Boundary intersection set, connected intersection set, and hub intersection set

*R <sub>k</sub>*

Route of the kth aircraft

$\mathcal{S}_{i} , \mathcal{A}_{i} , r_{\text{s} , i} , r_{\text{a} , i}$

Safety area, avoidance area, safety radius and avoidance radius of the ith aircraft

$\mathcal{A}_{i , j_{1} j_{2}}$

Airway derived from the edge $\left(n_{i , j_{1}} , n_{i , j_{2}}\right)$

$\mathcal{I}_{i , j , \text{az}} , \mathcal{I}_{i , j , \text{al}}$

Azimuth/altitude connected intersection derived from the node *n* <sub><em>i,j</em></sub>

$\mathcal{I}_{i , j_{1} j_{2} j_{3}}$

Arc airway connecting the two airways $\mathcal{I}_{i , j_{1} j_{2}}$ and $\mathcal{I}_{i , j_{2} j_{3}}$

$\mathcal{H}_{i , j}$

Central island set of the 3-D roundabout at the hub intersection *n* <sub><em>i,j</em></sub>

$\mathcal{R}_{i , j_{\text{1}} j} \left(\mathcal{R}_{i , j j_{\text{2}}}\right)$

On-ramp (off-ramp) set connecting $\mathcal{H}_{i , j}$ and the airway $\mathcal{A}_{i , j_{\text{1}} j} \left(\mathcal{A}_{i , j j_{\text{2}}}\right)$

$\overset{\overline}{\mathbf{p}_{1} , \mathbf{p}_{2}}$

Straight line passing through **p** <sub>1</sub> and **p** <sub>2</sub>

\[**p** <sub>1</sub>, **p** <sub>2</sub>\]

Line segment bounded by **p** <sub>1</sub> and **p** <sub>2</sub>

$\overset{\rightarrow}{\mathbf{p}_{1} \mathbf{p}_{2}}$

Vector from **p** <sub>1</sub> to **p** <sub>2</sub>

## 1\. Introduction

In the current decade, Unmanned Aerial Vehicles (UAVs) have assumed an increasingly prominent role across a wide range of applications, including on-demand package delivery, traffic and wildlife surveillance, inspection of infrastructure, search and rescue, agriculture, and cinematography (). The number of small UAVs has continued to grow in recent years, particularly in low-altitude airspace. Personal Aerial Vehicles (PAVs) and Urban Air Mobility (UAM), referring to flight operations to carry people within the geographical limits of an urban metropolis, are also on the way (, ).

With a specific focus on UAM operations, the emergence of electric Vertical Take-Off and Landing (VTOL) aircraft, designed to facilitate precise landings and hovering, is becoming increasingly evident on a large scale. The surge in demand for low-altitude urban air transportation (LAAT) presents formidable challenges in designing an efficient low-altitude air traffic system. It is worth noting that the conventional high-altitude human-centric air traffic management (ATM) system, which has been successfully employed for decades, faces significant scalability limitations when applied to the unique demands of low-altitude airspace. As such, the motivation behind our research is to address these pressing challenges and develop a tailored solution for efficient and scalable low-altitude ATM.

The research landscape in the field of LAAT systems has seen a growing interest in recent years. The relevant research can be divided into two aspects: (i) Optimization and design are conducted from the perspective of airspace structure, aiming to reduce conflicts among vehicles as much as possible by designing different airspace structures, thereby enhancing the safety and efficiency of LAAT systems; (ii) Control strategies for vehicles, particularly UAVs, are designed, which include decision-making, scheduling, trajectory planning, collision avoidance, etc., to ensure that vehicles can operate efficiently within the relevant airspace structure and corresponding constraint rules. It should be noted that these two aspects are not completely decoupled. In particular, well-designed airspace structures and traffic rules will inevitably lead to a certain degree of simplification in LAAT system control strategies and vice versa.

To enable safe and efficient UAM operations, the Federal Aviation Administration (FAA) and the National Aeronautics and Space Administration (NASA) are developing and refining a concept of operations for UAS Traffic Management (UTM) (). The ConOps focuses on UTM operations below 400 feet above ground level, which should fluctuate up and down with the topography. Motivated by this, the *controlled airspace* for low-altitude aircraft is designed as the layer-based concept described in;,. Specifically, the controlled airspace can be segmented into several vertical layers subject to the fluctuated topography; further, heterogeneous aircraft should fly in different altitude layers according to pre-defined principles, as illustrated in. This design does not only reduce potential conflicts among heterogeneous aircraft (), but also improves fuel burn by reducing climbing/descending maneuvers of the aircraft. Furthermore, future airspace structure is investigated in several works. In;;;;;;, the airspace is structured consisting of airways and/or intersections, while in;;; unstructured airspace is considered.

![Fig. 1 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr1.jpg)

Download: Download high-res image (382KB)

A concept called the Internet of Drones (IoD) is proposed in, where a conceptual model of its architecture is outlined, and the features of an IoD system are described. In, a preliminary concept of adaptive urban airspace management is proposed, emphasizing the importance of studying route network performance to effectively balance demand and capacity in urban airspace. In, based on a proposed pre-established route network, an open-loop UAV operation paradigm is proposed to enable a large number of relatively low-cost UAVs to fly beyond line-of-sight. In, a network design concept for a UTM system is proposed, where feasible low-level urban airspace regions, candidate network nodes, and unmanned traffic network structure were introduced. Inspired by a swarm in nature, dense traffic for aircraft is also attracting some research. In, some different dense multirotor UAV traffic simulation scenarios in open 2D and 3D spaces were studied under realistic environments with the presence of sensor noise, communication delay, limited communication range, limited sensor update rate, and finite inertia. Similarly, the feasibility of the designed 3D routes for fulfilling cargo UAVs named “3D aerial highway” is investigated in, where several practical concerns are considered, such as public safety, social acceptability, network requirements, and risk management.

The airway network design problem mainly focuses on optimizing the structure of a predefined network subject to given origins and destinations under geographical and artificial (or virtual) constraints. In, a modified path planning algorithm for UAV is proposed based on a risk assessment model, demonstrating superiority in generating safer flight paths compared to traditional shortest-distance methods. In, an airway network design method is proposed to eliminate the risk and to improve flight efficiency for aircraft. Similarly, an airport network model and a flow control method for urban logistics UAVs based on graph theory are investigated in, which can ensure safe and orderly flight. Furthermore, an algorithm is proposed in to generate a traffic network automatically by input images, where the safety and efficiency of aircraft are both considered. Based on these designed traffic networks, the risk to the people on the ground will be reduced greatly. Furthermore, a concept on low-altitude air traffic flow control with various airspace structural designs is proposed in, where the microscopic traffic model of aircraft is developed. However, these works often focus on the concepts of airspace design rather than the specific geometrical structure design, considering the safety constraints of aircraft.

In both structured and unstructured airspace, one of the primary concerns in UTM operations revolves around collision avoidance behaviors among aircraft. Various collision avoidance methods that provide conflict resolution have been extensively explored in the existing literature. For instance, noteworthy references include;, and the extensive body of work cited therein. A common underlying assumption in many works is that the aircraft are UAVs and can be fully controlled. Swarm control is a well-known method to ensure larger volumes of aircraft flying in the same airspace. The current architectures are mainly categorized into centralized architecture and decentralized architecture. In the centralized architecture, the ground-based ATM system can get the state of aircraft by air-to-ground communications or surveillance systems and then provide flight strategies to individual aircraft or flows of air traffic (, ). On the other hand, free flight is an air traffic control method that uses decentralized control (, ). By Automatic Dependent Surveillance-Broadcast (), Vehicle-to-Vehicle communication or on-board sensors, the individual aircraft can get the state of neighboring aircraft and determine its maneuvers according to the corresponding communication protocols. In, a decentralized air traffic control solution using autonomous drones is proposed, where some congested traffic situations were challenged for the distributed multi-robot control protocol. Based on simulation results, a conclusion given in indicates that the centralized architecture has better performance in terms of safety and efficiency but lacks robustness and scalability compared to the decentralized architecture. Furthermore, while the evolution of 5G/6G cellular networks shows significant potential for application in centralized LAAT systems (, ), there is still a challenge to ensure a dependable and high-bandwidth air-to-ground communication infrastructure for the expected multitude of aircraft in the future.

It is noteworthy that there is a limited body of work dedicated to the investigation of traffic flow models for LAAT systems, particularly in estimating macroscopic traffic flow variables (,,,,,,,,,, ). These studies have adopted various approaches to investigate different traffic characteristics, such as speed, separation, frequency of conflicts, density (accumulation), outflow, and capacity. Compared to collision avoidance methodologies, these works represent a higher-level endeavor aimed at optimizing LAAT systems and deserve significant attention in the future. Recent research efforts have increasingly focused on studying Macroscopic Fundamental Diagrams (MFDs) and leveraging them for control-oriented strategies in LAAT systems. While this line of research builds on a substantial body of prior work in urban road networks, recent examples include perimeter control and route guidance, speed regulation strategies (), and resilience under cyber-attacks (). These studies demonstrate how concepts originally developed for urban traffic are now being adapted to support advanced control and management strategies for UAM systems, such as perimeter control (), integrated departure and boundary (perimeter) control (), and dynamic routing strategies (). From the perspective of airspace structure design, it is crucial that future airspace designs facilitate the measurement of traffic characteristics to provide valuable feedback on LAAT system optimization strategies. It is worth pointing out that the dynamic routing based on grid-based or hexagon-based airspace partitioning methods remains best suited to unstructured operations (), and may face inherent limitations in dense traffic scenarios. These approaches still require extensive real-time computation to resolve conflicts between aircraft that retain full directional freedom within each cell. As traffic density increases, the computational complexity of pairwise conflict detection and resolution grows substantially, creating scalability challenges. Additionally, the conflict resolution in these systems may lead to last-minute maneuvers that reduce overall traffic efficiency.

Motivated by these works, in this paper, a “sky highway” structure is proposed first for low-altitude heterogeneous VTOL aircraft, where air traffic network, route, flow, and swarm control design are all considered. The sky highway structure integrates layer- and tube-based concepts, i.e., the low-altitude airspace is divided into multiple layers by altitude, and each layer has its own air traffic network similar to the tube topology, according to practical requirements and constraints. Heterogeneous aircraft, such as cargo UAVs and PAVs in UAM, can fly in different layers to reduce risks. By this, aircraft in the same layer have similar tasks, speeds, and kinematic models, which can also reduce conflicts among aircraft. While drawing inspiration from ground transportation networks, the proposed sky highway fundamentally differs in both design principles and operational mechanisms. Unlike ground vehicles, which are constrained by physical infrastructure, aircraft in low-altitude airspace possess greater mobility in three dimensions, allowing for more flexible route configurations. However, this flexibility also introduces unique challenges in conflict management and spatial coordination. The sky highway architecture addresses these challenges by incorporating aircraft’s distributed collision avoidance algorithms and centralized routing strategies that leverage aircraft’s autonomous capabilities, significantly surpassing traditional ground-based traffic management approaches. Furthermore, similar to the road network, the air traffic network at each layer consists of the following elements: i) airways, ii) connected intersections, iii) hub intersections, and iv) boundary intersections. Multi-lane is allowed to classify aircraft into different predefined speeds. Aircraft are controlled in a swarm control manner with a hybrid centralized-distributed control protocol; specifically, the conflict resolution maneuver for each aircraft is provided by a distributed control protocol, while the traffic scheduling is realized by a centralized control system. By this control scheme, the flow performance of aircraft in low-altitude airspace is improved as far as possible. The process of UAV flight in the sky highway can be regarded as a fusion of the free flight concept and the structural constraints of the airway network. Compared to the free flight concept in unstructured airspace, the sky highway offers distinct advantages for urban air mobility applications. While free flight operations may achieve theoretical efficiency in low-density scenarios, they face significant scalability limitations under higher traffic demands due to unpredictable conflict patterns and computational complexity in conflict resolution. The structured sky highway design introduces necessary constraints that streamline traffic flow, reduce coordination uncertainty, and provide deterministic safety guarantees through carefully designed topological features. This structured approach represents an essential intermediate solution between completely free flight and overly rigid route-based flight, striking a balance between operational flexibility and safety assurance for large-scale UAM operations. Therefore, as shown in, the concept of the sky highway combines some of the characteristics of the free flight concept and the traditional trajectory planning approach in civil aviation, thus achieving a compromise between safety and efficiency.

![Fig. 2 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr2.jpg)

Download: Download high-res image (216KB)

In, the sky highway concept with a structure design was introduced for homogeneous aircraft motion in 2D space. This paper enhances the preliminary study in in the following issues: (i) a *sky highway design* is developed, entailing the introduction of an improved geometrical structure and the design of flight modes for airways and intersections to accommodate *heterogeneous* aircraft, including multi-lanes within airways, arc roads at connected intersections, three-dimensional (3-D) roundabouts at hub intersections, and a First In First Out (FIFO) flight rule at boundary intersections; (ii) a hybrid centralized-distributed control protocol is proposed for the sky highway structure; and (iii) different case studies are analyzed to evaluate the proposed structure, where the macroscopic traffic flow variables are estimated to determine the airspace performance and traffic characteristics.

In this paper, we introduce a designed layer-based structured airspace for a sky highway. Subsequently, we delve into the geometrical structure of airways and different types of intersections within the network, along with their corresponding flight modes tailored to support congested traffic. The contributions can be summarized as follows:
- •
	The layer-based multi-lane geometrical structure of the air traffic network is designed to maintain a certain separation of different elements, which can maintain separation among heterogeneous aircraft flying in different elements.
- •
	Different flight modes are proposed for the airways and intersections, which can allow aircraft to fly safely and efficiently while avoiding potential congestion.
- •
	The hybrid centralized-distributed control protocol for low-altitude ATM is designed under the sky highway structure, where the traffic flows and separation between aircraft can be managed simultaneously.

The following section outlines the structure of the paper. In, the problem is formulated, including the proposed airspace structure, traffic network model, VTOL aircraft model, and several basic requirements. outlines the design of the sky highway structure for low-altitude heterogeneous VTOL aircraft, which incorporates various elements, including bidirectional airways, connected intersections, hub intersections, and boundary intersections. presents the flight modes corresponding to different elements within the sky highway structure. showcases the primary simulation results, which demonstrate the efficacy of the designed sky highway structure. concludes the paper with a summary of the key findings.

## 2\. Sky highway model development

This section introduces the developed sky highway model, which includes three key elements: (i) a general traffic network model for a layer-based airspace structure, (ii) a specified VTOL aircraft model featuring two surrounding areas, and (iii) various fundamental requirements pertinent to sky highway design.

### 2.1. General traffic network model

In this work, the layer-based concept, as previously outlined in references (,, ), is considered in relation to the controlled airspace. Similarly to the Skyways project developed by AIRBUS, each layer is further structured with a tube topology comparable to the road networks observed in urban areas. As discussed in,, in comparison to alternative concepts such as layers or zones, the tube topology can facilitate the provision of fixed routes for aircraft within the airspace. This is achieved through the use of bidirectional tubes that do not intersect except at designated nodes. This approach not only enhances the predictability of traffic flows but also improves safety.

Furthermore, using graph theory, the tube topology in each layer is formulated into a general traffic network model for this study. More specifically, the traffic network is modeled as an undirected graph with nodes and edges. For the proposed airspace structure, each layer has its own traffic network to accommodate specific types of aircraft. Suppose that the controlled airspace for low-altitude aircraft is divided into *M* layers. To ensure safety, different layers’ traffic networks are unconnected, i.e., aircraft cannot travel from one layer to another, as shown in (a). Without loss of generality, an undirected graph $\mathcal{G}_{i} = \left(\mathcal{N}_{i} , \mathcal{E}_{i} , \mathcal{W}_{i}\right)$ is used to describe the *i* th layer’s traffic network, which consists of a node set $\mathcal{N}_{i} = \left\{n_{i , 1} , n_{i , 2} , \hdots , n_{i , N_{i}}\right\}$, an edge set $\mathcal{E}_{i} \subseteq \left\{\left(n_{i , j_{1}} , n_{i , j_{2}}\right) : n_{i , j_{1}} , n_{i , j_{2}} \in \mathcal{N}_{i} , j_{1} \neq j_{2}\right\}$, and a symmetric weighted adjacency matrix $\mathcal{W}_{i} = \left[d_{i , j_{1} j_{2}}\right] \in \mathbb{R}^{N_{i} \times N_{i}}$ with its elements defined as(1) $d_{i , j_{1} j_{2}} = \begin{cases} \left\|\mathbf{p}_{i , j_{1}} - \mathbf{p}_{i , j_{2}}\right\| & \text{if} \left(n_{i , j_{1}} , n_{i , j_{2}}\right) \in \mathcal{E}_{i} \\ 0 & \text{else} \end{cases} ,$where $\mathbf{p}_{i , j_{1}} , \mathbf{p}_{i , j_{2}} \in \mathbb{R}^{3}$ denote the positions of the nodes $n_{i , j_{1}}$, $n_{i , j_{2}}$, respectively. In the *i* th layer’s traffic network, the nodes and edges are further characterized as *intersections* and *airways*, respectively. The *airways* act like multi-lane bidirectional highways in a road network. The *intersections* are classified as follows: (i) *boundary intersections* directly link to a vertiport (an infrastructure that allows aircraft to fly in and out of the traffic network) or free flight airspace (an airspace where aircraft can select their speed and trajectory freely and flexibly without constraints), (ii) *connected intersections* connecting two edges, and (iii) *hub intersections* connecting at least three edges, as shown in (a). Then, we can express $\mathcal{N}_{i}$ as $\mathcal{N}_{i} = \mathcal{N}_{i , \text{e}} \cup \mathcal{N}_{i , \text{c}} \cup \mathcal{N}_{i , \text{h}}$, where $\mathcal{N}_{i , \text{e}} , \mathcal{N}_{i , \text{c}} , \mathcal{N}_{i , \text{h}}$ denote the boundary intersection set, connected intersection set, and hub intersection set, respectively. In the *i* th layer, the *k* th aircraft’s *route* is a path on the graph $\mathcal{G}_{i}$, i.e., a sequence of distinct vertices, namely $R_{k} = \left\{n_{i , k_{1}} , n_{i , k_{2}} \hdots , n_{i , k_{r}}\right\}$, where *r* is the number of vertices in route *R <sub>k</sub>*, $\left(n_{i , k_{m}} , n_{i , k_{m + 1}}\right) \in \mathcal{E}_{i}$ for $m = 1 , \hdots , r - 1$, and $n_{i , k_{1}} , n_{i , k_{r}} \in \mathcal{N}_{i , \text{e}}$. For better clarification of the above definitions, the network model for the two layers in (a) is shown in (b). By the definitions above, the sets $\mathcal{N}_{i , \text{e}} , \mathcal{N}_{i , \text{c}} , \mathcal{N}_{i , \text{h}}$ for $i = 1 , 2$ can be written as $\mathcal{N}_{1 , \text{e}} = \left\{n_{1 , 1} , n_{1 , 12}\right\}$, $\mathcal{N}_{1 , \text{c}} = \left\{n_{1 , 2} , n_{1 , 3} , n_{1 , 4} , n_{1 , 6} , n_{1 , 7} , n_{1 , 10}\right\}$, $\mathcal{N}_{1 , \text{h}} = \left\{n_{1 , 5} , n_{1 , 8} , n_{1 , 9} , n_{1 , 11}\right\} ,$ and $\mathcal{N}_{2 , \text{e}} = \left\{n_{2 , 1} , n_{2 , 11}\right\}$, $\mathcal{N}_{2 , \text{c}} = \left\{\right. n_{2 , 2} , n_{2 , 3} , n_{2 , 4} , n_{2 , 9} ,$.*n* <sub>2,10</sub> }, $\mathcal{N}_{2 , \text{h}} = \left\{n_{2 , 5} , n_{2 , 6} , n_{2 , 7} , n_{2 , 8}\right\}$.

![Fig. 3 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr3.jpg)

Download: Download high-res image (858KB)

### 2.2. VTOL aircraft model

To describe the sense-and-avoid behavior for VTOL aircraft at a microscopic level, two areas named *safety area* and *avoidance area* for each VTOL aircraft are modeled, as shown in. Specifically, a VTOL aircraft’s *safety area* $\mathcal{S}$ is defined as a sphere(2) $\mathcal{S} = \left\{\mathbf{x} \in \mathbb{R}^{3} \left|\right. \left\|\mathbf{x} - \mathbf{p}_{i}\right\| < r_{\text{s} , i}\right\} ,$where $\mathbf{p}_{i} \in \mathbb{R}^{3}$ is the center position of the *i* th aircraft, and *r* <sub>s,<em>i</em></sub> is called the *safety radius* of the *i* th aircraft. In accordance with the aforementioned definition, each aircraft is equipped with a distinct predefined safety radius. Furthermore, the risk of collision between two aircraft is mitigated to the extent that their safety areas do not overlap. When designing the safety radius of an aircraft, a multitude of factors must be taken into account, including its physical dimensions, maneuverability, operational environment, and communication uncertainties (). In addition to the safety area, an *avoidance area* is utilized for initiating avoidance control, which is defined as another sphere(3) $\mathcal{A} = \left\{\mathbf{x} \in \mathbb{R}^{3} \left|\right. \left\|\mathbf{x} - \mathbf{p}_{i}\right\| < r_{\text{a} , i}\right\} ,$where *r* <sub>a,<em>i</em></sub> is called the *avoidance radius* of the *i* th aircraft. The *i* th aircraft needs to avoid the *j* th aircraft if and only if the *i* th aircraft’s safety area enters the *j* th aircraft’s avoidance area (we called that the *i* th aircraft conflicts with the *j* th aircraft). On the other hand, no conflict between the *i* th and the *j* th aircraft implies that(4) $\left\|\mathbf{p}_{i} - \mathbf{p}_{j}\right\| > max \left(r_{\text{a} , i} + r_{\text{s} , j} , r_{\text{a} , j} + r_{\text{s} , i}\right) .$

![Fig. 4 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr4.jpg)

Download: Download high-res image (145KB)

It is obvious that each aircraft’s avoidance radius is larger than its safety radius. For the convenience of description, we suppose that all aircraft have the same safety radius *r* <sub>s</sub> and avoidance radius *r* <sub>a</sub>. The more general condition that each aircraft has its own safety radius and avoidance radius can be easily extended. In addition, it is imperative to consider the turning radius of each aircraft, a critical parameter for evaluating its maneuverability and flight dynamics. The turning radius refers to the minimum radius of curvature necessary for the aircraft during a turning maneuver. This metric is intricately linked to the aircraft’s design, agility, and flight control system. A smaller turning radius indicates improved agility, enabling the aircraft to navigate through confined spaces and execute precise maneuvers. In this paper, we assume that the maximum turning radius of all aircraft, denoted as *r* <sub>turn</sub>, is known a priori.

### 2.3. Sky highway design requirements

In this work, some *basic requirements* are proposed to guide the geometric design of the traffic network, which is formulated as the *sky highway design problem*.

**Basic Requirement 1**. Each aircraft has its own route from one boundary intersection to another boundary intersection corresponding to its task.

**Basic Requirement 2**. Aircraft should not change the altitude and azimuth simultaneously as far as possible.

**Basic Requirement 3**. Aircraft should be separated by a safety distance of at least 2 *r* <sub>s</sub> to avoid collision with each other.

**Basic Requirement 4**. Each aircraft cannot fly outside of the located airways or intersections, i.e., the aircraft maintains a distance from the boundary of airways or intersections larger than their safety radius.

**Basic Requirement 5**. Each aircraft can have different velocities and different priorities.

The work presented in explores an automatic approach for generating air traffic networks based on low-altitude geographical information. Thus, it is reasonable for us to assume a priori knowledge of the general traffic network model, represented as an undirected graph $\mathcal{G}_{i} = \left(\mathcal{N}_{i} , \mathcal{E}_{i} , \mathcal{W}_{i}\right)$, as indicated in. Based on these basic requirements, an air traffic network, named *sky highway*, is designed for *low-altitude heterogeneous VTOL aircraft*. Compared with current civil aviation transportation, numerous heterogeneous VTOL aircraft will be allowed to share the same airspace during congested air traffic. The design of the sky highway structure aims to (i) ensure the safety distance among aircraft, and (ii) improve traffic efficiency as much as possible. Therefore, the abstract traffic network model is further designed, which includes the geometrical design of the elements (intersections and airways) and the corresponding flight modes.

**Remark 1**

The origin and destination for each aircraft are specified by *Basic Requirement 1* to connect the vertiport and the general traffic network in each layered airspace. *Basic Requirement 2* is reasonable because most aircraft are controlled according to longitudinal channel (changing altitude) and lateral channel (changing azimuth). The safety separation is ensured by *Basic Requirement 3*, where the safety distance *r* <sub>s</sub>  > 0 among aircraft can take the uncertainties into consideration (). Similar to the urban traffic network, *Basic Requirement 4* indicates that the airways and nodes both have borders to restrict aircraft, and *Basic Requirement 5* is to make improvement of the traffic efficiency.

## 3\. Sky highway structure design for low-Altitude heterogeneous VTOL aircraft

In this section, the structure of airways and intersections with corresponding flight modes for supporting congested traffic are studied one by one.

### 3.1. Airway design

A multi-lane bidirectional *airway structure* is designed in the sky highway structure, as shown in.

![Fig. 5 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr5.jpg)

Download: Download high-res image (489KB)

The airway $\mathcal{A}_{i , j_{1} j_{2}}$ in the *i* th layer derived from the edge $\left(n_{i , j_{1}} , n_{i , j_{2}}\right) \in \mathcal{E}_{i}$, $i = 1 , 2 , \hdots , M$, $j_{1} , j_{2} = 1 , 2 , \hdots , N_{i}$ is a cuboid set on the right-hand side of $\overset{\rightarrow}{\mathbf{p}_{i , j_{1}} \mathbf{p}_{i , j_{2}}}$ with the width *r* <sub><em>i</em>,aw</sub>, the height *h* <sub><em>i</em>,aw</sub>, the center line segment $\left[\mathbf{p}_{i , j_{1} j_{2} , \text{o}} , \mathbf{p}_{i , j_{1} j_{2} , \text{d}}\right]$ on the middle height, and the flight direction consistent with $\overset{\rightarrow}{\mathbf{p}_{i , j_{1}} \mathbf{p}_{i , j_{2}}}$, as indicated by the red rectangle area in (b). The length of the airway $\mathcal{A}_{i , j_{1} j_{2}}$ is related to the distance $d_{i , j_{1} j_{2}} ,$ and the structure of nodes $n_{i , j_{1}} , n_{i , j_{2}}$ Furthermore, as illustrated in (b), the two opposing airways $\mathcal{A}_{i , j_{1} j_{2}}$ and $\mathcal{A}_{i , j_{2} j_{1}}$ are denoted by the red area and blue area, respectively. The two airways are separated by an *airway isolation belt* area $\mathcal{A}_{i , j_{1} j_{2} , \text{aib}}$ with the width *r* <sub><em>i</em>,aib</sub> and the center line segment $\left[\mathbf{p}_{i , j_{1} j_{2} , \text{aio}} , \mathbf{p}_{i , j_{1} j_{2} , \text{aid}}\right]$ on the middle height, where(5) $\begin{aligned}\mathbf{p}_{i , j_{1} j_{2} , \text{aio}} & = \mathbf{p}_{i , j_{2} j_{1} , \text{aid}} = \frac{1}{2} \left(\mathbf{p}_{i , j_{1} j_{2} , \text{o}} + \mathbf{p}_{i , j_{2} j_{1} , \text{d}}\right) ,\end{aligned}$(6) $\begin{aligned}\mathbf{p}_{i , j_{1} j_{2} , \text{aid}} & = \mathbf{p}_{i , j_{2} j_{1} , \text{aio}} = \frac{1}{2} \left(\mathbf{p}_{i , j_{1} j_{2} , \text{d}} + \mathbf{p}_{i , j_{2} j_{1} , \text{o}}\right) .\end{aligned}$To further refine the airway structure, each airway is divided into *N* <sub><em>i</em>,lane</sub> *lanes* with the same width *r* <sub><em>i</em>,lane</sub> which allow aircraft to fly inside, and $N_{i , \text{lane}} - 1$ *lane isolation belts* with the same width *r* <sub><em>i</em>,lib</sub> to separate the lanes. For example, an airway structure with $N_{i , \text{lane}} = 3$ is shown in. Then, the following relationship holds(7) $r_{i , \text{aw}} = N_{i , \text{lane}} r_{i , \text{lane}} + \left(N_{i , \text{lane}} - 1\right) r_{i , \text{lib}} .$

Except for the length $d_{i , j_{1} j_{2}} ,$ the defined parameters above are unified for all airways at the same layer. Without loss of generality, more specifically, the cuboid set $\mathcal{A}_{i , j_{1} j_{2} , \text{lane} , k}$ denotes the *k* th lane in the airway $\mathcal{A}_{i , j_{1} j_{2}}$, where $k = 1 , 2 , \hdots ,$ *N* <sub><em>i</em>,lane</sub>. The minimum distance between two sets $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$ is defined as(8) $d \left(\mathcal{S}_{1} , \mathcal{S}_{2}\right) \triangleq \underset{\mathbf{x} \in \mathcal{S}_{1} , \mathbf{y} \in \mathcal{S}_{2}}{min} \left\|\mathbf{x} - \mathbf{y}\right\| .$Then, according to *Basic Requirements 3 and 4*, the following *Airway Design Requirements* are proposed:

**Airway Design Requirement 1**. In the same airway, the aircraft flying in different lanes should maintain their distance larger than $r_{\text{a}} + r_{\text{s}}$.

**Airway Design Requirement 2**. The aircraft flying in different airways should maintain their distance larger than $r_{\text{a}} + r_{\text{s}}$.

Note that if the distance between two aircraft is larger than $r_{\text{a}} + r_{\text{s}}$, then they do not need to make avoidance with each other. *Airway Design Requirements 1 and 2* imply that there is no conflict between two aircraft if they are at different lanes or airways.

**Proposition 1**

*Suppose that the airway structure matches the one depicted in* *. For the two opposite airways* $\mathcal{A}_{i , j_{1} j_{2}}$ *and* $\mathcal{A}_{i , j_{2} j_{1}}$ *, if* (9) $min \left(r_{i , \text{aib}} , r_{i , \text{lib}}\right) > r_{\text{s}}$ *then Airway Design Requirement 1 holds, where* $\left(n_{i , j_{1}} , n_{i , j_{2}}\right) \in \mathcal{E}_{i}$ *.*

**Proof**

The proof is obvious.

Furthermore, provides a result relevant to *Airway Design Requirement 2.*

**Proposition 2**

*Suppose that the airway structure matches the one depicted in* *. For the ith and the jth airways, if* (10) $\begin{matrix}d \left(\left[\mathbf{p}_{i_{1} , j_{1}} , \mathbf{p}_{i_{1} , j_{2}}\right] , \left[\mathbf{p}_{i_{2} , j_{3}} , \mathbf{p}_{i_{2} , j_{4}}\right]\right) > r_{\text{s}} + \frac{1}{2} \sqrt{d_{1}^{2} + d_{2}^{2}}\end{matrix}$ *then the minimum distance among the sets* $\mathcal{A}_{i_{1} , j_{1} j_{2}}$ *,* $\mathcal{A}_{i_{1} , j_{2} j_{1}}$ *,* $\mathcal{A}_{i_{2} , j_{3} j_{4}}$ *,* $\mathcal{A}_{i_{2} , j_{4} j_{3}}$ *is larger than r* <sub>s</sub>*, where* $d_{1} = r_{i_{1} , \text{aw}} + r_{i_{2} , \text{aw}}$ *,* $d_{2} = h_{i_{1} , \text{aw}} + h_{i_{2} , \text{aw}}$ *,* $i_{1} , i_{2} = 1 , 2 , \hdots , M$ *,* $\left(n_{i_{1} , j_{1}} , n_{i_{1} , j_{2}}\right) \in \mathcal{E}_{i_{1}} , \left(n_{i_{2} , j_{3}} , n_{i_{2} , j_{4}}\right) \in \mathcal{E}_{i_{2}}$ *.*

**Proof**

This follows directly from the proof of the in().

### 3.2. Connected intersection design

A *connected intersection* is the connection of two edges in the traffic network. By *Basic Requirement 2*, the aircraft cannot change the altitude and azimuth simultaneously, which implies that connected intersections can be classified into two types: (i) *azimuth connected intersection*, where aircraft change azimuth, and (ii) *altitude connected intersection*, where aircraft change altitude, as respectively shown in (a) and (b). In the following, we describe the design of each type.

#### 3.2.1. Azimuth connected intersection design

Suppose the two edges $\left(n_{i , j_{1}} , n_{i , j_{2}}\right) , \left(n_{i , j_{2}} , n_{i , j_{3}}\right) \in \mathcal{E}_{i}$ are at the same altitude with the azimuth connected intersection $n_{i , j_{2}} \in \mathcal{N}_{i , \text{c}}$. Note that each edge contains two opposite airways, that is to say, two pairs of airways $\left(\mathcal{A}_{i , j_{1} j_{2}} , \mathcal{A}_{i , j_{2} j_{3}}\right)$, $\left(\mathcal{A}_{i , j_{3} j_{2}} , \mathcal{A}_{i , j_{2} j_{1}}\right)$ are connected at the same intersection $\mathcal{I}_{i , j_{2} , \text{az}}$, as shown in. Specifically, the azimuth connected intersection $\mathcal{I}_{i , j_{2} , \text{az}}$ is modeled as a cylinder set with the center $\mathbf{p}_{i , j_{2}}$, radius $r_{i , j_{2}}$, height *h* <sub><em>i</em>,aw</sub>, and radial direction perpendicular to the horizontal plane. Motivated by the arc roads in ground traffic, the two airways $\mathcal{A}_{i , j_{1} j_{2}} , \mathcal{A}_{i , j_{2} j_{3}}$ are connected with an arc airway denoted as $\mathcal{I}_{i , j_{1} j_{2} j_{3}}$ inside the intersection. By the definitions above, the only design parameter is the radius $r_{i , j_{2}}$, which should satisfy *Basic Requirements 3 and 4*. Furthermore, the following two *Connected Intersection Design Requirements* are obtained.

![Fig. 6 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr6.jpg)

Download: Download high-res image (248KB)

**Connected Intersection Design Requirement 1**. Except for the space within the connected intersection, the minimum distance between any two airways connected to the connected intersection should be larger than $r_{\text{a}} + r_{\text{s}}$. Note that the conditions $\mathcal{A}_{i , j_{1} j_{2}} \cap \mathcal{A}_{i , j_{2} j_{1}} = \emptyset$ and $\mathcal{A}_{i , j_{2} j_{3}} \cap \mathcal{A}_{i , j_{3} j_{2}} = \emptyset$ always hold due to the design of the airway isolation belt introduced in. Therefore, *Connected Intersection Design Requirement 1* here can be formulated as(11) $d \left(\left(\mathcal{A}_{i , j_{1} j_{2}} \cup \mathcal{A}_{i , j_{2} j_{1}}\right) \cap \left(\bar{\mathcal{I}}\right)_{i , j_{2} , \text{az}} , \left(\mathcal{A}_{i , j_{2} j_{3}} \cup \mathcal{A}_{i , j_{3} j_{2}}\right) \cap \left(\bar{\mathcal{I}}\right)_{i , j_{2} , \text{az}}\right) > r_{\text{a}} + r_{\text{s}} ,$where $$ denotes the complementary set of $\mathcal{I}_{i , j_{2} , \text{az}} .$

**Connected Intersection Design Requirement 2**. Each arc airway’s inner radius should be larger than the maximum turn radius of aircraft *r* <sub>turn</sub> for safety considerations.

For *Connected Intersection Design Requirements 1 and 2*, we have the result shown in.

**Proposition 3**

*For the azimuth connected intersection* $\mathcal{A}_{i , j_{2} , \text{az}}$ *, if the intersection radius* $r_{i , j_{2}}$ *satisfies* (12) $r_{i , j_{2}} > max \left(d_{3} , d_{4}\right) ,$ *then Connected Intersection Design Requirements 1 and 2 hold, where* (13) $\begin{matrix}d_{3} = \frac{1}{2 cos \theta_{i , \text{aw}} sin \frac{\theta_{i , j_{2}}}{2}} \left(r_{\text{a}} + r_{\text{s}} + \sqrt{r_{i , \text{aw}}^{2} + h_{i , \text{aw}}^{2}}\right) ,\end{matrix}$(14) $\begin{matrix}d_{4} = \frac{1}{2} \sqrt{\left(\frac{r_{i_{1} , \text{aw}} + 2 r_{\text{turn}}}{tan \frac{\theta_{i , j_{2}}}{2}}\right)^{2} + r_{i , \text{aw}}^{2}} ,\end{matrix}$(15) $\begin{matrix}\theta_{i , j_{2}} = arccos \frac{\left(\mathbf{p}_{i , j_{2}} - \mathbf{p}_{i , j_{1}}\right)^{\text{T}} \left(\mathbf{p}_{i , j_{2}} - \mathbf{p}_{i , j_{3}}\right)}{\left\|\mathbf{p}_{i , j_{2}} - \mathbf{p}_{i , j_{1}}\right\| \left\|\mathbf{p}_{i , j_{2}} - \mathbf{p}_{i , j_{3}}\right\|} ,\end{matrix}$(16) $\begin{matrix}\theta_{i , \text{aw}} = arcsin \frac{r_{i , \text{aw}}}{2 r_{i , j_{2}}} .\end{matrix}$

**Proof**

See Appendix.

#### 3.2.2. Altitude connected intersection design

We similarly define the altitude connected intersection $n_{i , j_{5}} \in \mathcal{N}_{i , \text{c}}$ as the connection of the two edges $\left(n_{i , j_{4}} , n_{i , j_{5}}\right)$, $\left(n_{i , j_{5}} , n_{i , j_{6}}\right) \in \mathcal{E}_{i}$ at the same azimuth, as shown in (b). The altitude connected intersection $\mathcal{A}_{i , j_{5} , \text{al}}$ is modeled as a cylinder set with the center $\mathbf{p}_{i , j_{5}}$, radius $r_{i , j_{5}}$, height *r* <sub><em>i</em>,aw</sub>, and radial direction perpendicular to the plane which contains the three points $\mathbf{p}_{i , j_{4}}$, $\mathbf{p}_{i , j_{5}}$, and $\mathbf{p}_{i , j_{6}}$. By the definitions above, the similar result is shown in.

**Proposition 4**

*For the altitude connected intersection* $\mathcal{A}_{i , j_{5} , \text{al}}$ *, if the intersection radius* $r_{i , j_{5}}$ *satisfies* (17) $r_{i , j_{5}} > max \left(d_{5} , d_{6}\right) ,$ *then Connected Intersection Design Requirements 1 and 2 hold, where* (18) $\begin{matrix}d_{3} = \frac{1}{2 cos \theta_{i , \text{aw}} sin \frac{\theta_{i , j_{5}}}{2}} \left(r_{\text{s}} + \sqrt{r_{i , \text{aw}}^{2} + h_{i , \text{aw}}^{2}}\right) ,\end{matrix}$(19) $\begin{matrix}d_{4} = \frac{1}{2} \sqrt{\left(\frac{h_{i , \text{aw}} + 2 \left\|\mathbf{o}_{i , j_{5}} - \mathbf{p}_{i , j_{4} j_{5} , \text{r}}\right\|}{\sqrt{4 r_{i , j_{5}}^{2} - h_{i , \text{aw}}^{2}}}\right)^{2} + h_{i , \text{aw}}^{2}} ,\end{matrix}$(20) $\begin{matrix}\theta_{i , j_{5}} = arccos \frac{\left(\mathbf{p}_{i , j_{5}} - \mathbf{p}_{i , j_{4}}\right)^{\text{T}} \left(\mathbf{p}_{i , j_{5}} - \mathbf{p}_{i , j_{6}}\right)}{\left\|\mathbf{p}_{i , j_{5}} - \mathbf{p}_{i , j_{4}}\right\| \left\|\mathbf{p}_{i , j_{5}} - \mathbf{p}_{i , j_{6}}\right\|} ,\end{matrix}$(21) $\begin{matrix}\theta_{i , j_{5} , \text{aw}} = arcsin \frac{h_{i , \text{aw}}}{2 r_{i , j_{5}}} .\end{matrix}$

**Proof**

The proof is similar to the proof of.

**Remark 2**

From condition, $\theta_{i , j_{2}} , \theta_{i , j_{5}} , r_{\text{s}} , h_{i , \text{aw}} , r_{i , \text{aw}}$ are constant, and $cos \theta_{i , j_{2} , \text{aw}} \rightarrow 1 , cos \theta_{i , j_{5} , \text{aw}} \rightarrow 1$ as $r_{i , j_{2}} , r_{i , j_{5}}$ increase, respectively.

It is, therefore, possible to ensure that the radius of each interconnected intersection is of sufficient size to consistently meet the *Connected Intersection Design Requirements 1 and 2*. It should be noted, however, that the angle between airways should not be too small, otherwise the radius of the connected intersection will be too large. This represents a hard constraint during the network generation process.

### 3.3. Hub intersection design

A roundabout is a type of intersection structure that is designed to accommodate high traffic volumes while simultaneously ensuring the safety and efficiency of the transportation system. In particular, a roundabout is composed of a central island and a number of ramps. Each aircraft entering the hub intersection from an airway via the corresponding on-ramp will perform a counterclockwise rotation in the central island until it proceeds via an off-ramp to another airway, as illustrated in (a). The central island and ramps are subdivided into a number of lanes, with each lane corresponding to a specific airway. Each aircraft entering the roundabout will be in the fixed lane corresponding to the lane it enters, and no lane changes will occur until it leaves the roundabout. However, in the context of ground traffic with two-dimensional (2-D) case, conflicts among vehicles may occur at the intersection of each ramp’s lanes and the central island’s lanes (referred to as *conflict points*) (), as illustrated in (a). These conflict points can be systematically classified into two distinct categories: intra-lane and inter-lane conflict points.
- •
	Intra-lane conflict points: These occur within the same traffic lane and are typically rear-end conflicts arising from the deceleration of vehicles preparing to enter the roundabout (as the conflict points 1 and 2 shown in (b)). The primary cause is the variance in vehicular speed and the subsequent need for trailing vehicles to adjust speed accordingly to avoid collisions. Such conflict points are characterized by longitudinal interactions, where the primary relative motion is in the direction of traffic flow.
- •
	Inter-lane conflict points: These conflicts manifest between vehicles traveling in adjacent lanes and arise at the junctures where the on-ramp and off-ramp’s inner lane intersect with the central island’s outer lane (as the conflict points 3 and 4 shown in (b)). Inter-lane conflicts are induced by the lateral movement of vehicles crossing over the delineation of adjacent traffic lanes.

![Fig. 7 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr7.jpg)

Download: Download high-res image (486KB)

In ground traffic, the two types of conflict points are typically avoided by the implementation of yield controls at the junction of the ramps and the central island. However, in the proposed sky highway structure, the objective is to avoid these conflict points as much as possible through the design of the airspace structure itself rather than through the implementation of traffic control strategies. In order to circumvent the aforementioned inter-lane conflict points, a 3-D multi-lane roundabout has been designed for hub intersections in the proposed sky highway structure. As illustrated in, the ramps and central island have been constructed at varying altitudes and are connected by buffer zones (highlighted in red in (a)). Specifically, the occurrence of inter-lane conflict points is due to the intersection between different lanes on the ramp and the central island, which is unavoidable in a 2-D roundabout. However, these conflict points will no longer exist in the proposed 3-D roundabout, as the design with different altitudes for the ramps and central island ensures that they no longer intersect (see (b)). Compared to unstructured airspace, the circular design within the 3-D roundabout intrinsically reduces conflict points and simplifies traffic flow, but necessarily creates a geometrically unused central area. The apparent underutilization of the central area is an inherent characteristic of the 3-D roundabout structure, which trades spatial efficiency for enhanced safety. Furthermore, this reserved space provides crucial flexibility for urban integration, allowing the central zone to accommodate terrain obstacles, restricted areas, or ground infrastructure. Such infrastructure can provide precise state information to aircraft, including the relative distance, velocity, and azimuth angles to the roundabout’s center. The information effectively supports distributed control algorithms for aircraft while maintaining the roundabout’s operational integrity ().

![Fig. 8 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr8.jpg)

Download: Download high-res image (270KB)

Without loss of generality, let us consider $2 \bar{M}$ airways corresponding to the edges $\left(j_{k} , j_{1}\right) , \left(j_{k} , j_{2}\right) , \hdots , \left(j_{k} , j_{\bar{M}}\right)$ at the same altitude connected at the hub intersection $\mathbf{n}_{i , j_{k}}$, where (*j <sub>k</sub>, j* <sub>1</sub>) denotes the edge $\left(n_{i , j_{k}} , n_{i , j_{1}}\right) \in \mathcal{E}_{i}$ for simplicity, and $n_{i , j_{k}} \in \mathcal{N}_{i , \text{h}}$. The hub intersection $\mathbf{n}_{i , j_{k}}$ is modeled as a 3-D multi-lane roundabout, which consists of a central island, $\bar{M}$ on-ramps and $\bar{M}$ off-ramps. For the sake of convenience and without loss of generality, we take a single-lane roundabout as an example, as shown in. Specifically, the central island is an annular cylinder set $\mathcal{H}_{i , j_{k}}$ with the center $\mathbf{p}_{i , j_{k}} + h_{\text{r}} \mathbf{e}_{3}$ ($\mathbf{e}_{3} \triangleq \begin{bmatrix} 0 & 0 & 1 \end{bmatrix}^{\text{T}}$ is an unit vector), inner radius $r_{i , j_{k} , \text{in}}$, outer radius $r_{i , j_{k} , \text{in}} + r_{i , \text{aw}}$, height *h* <sub><em>i</em>,aw</sub>, and radial direction perpendicular to the horizontal plane; the on-ramp $\mathcal{R}_{i , j_{\text{in}} j_{k}}$ connects the central island $\mathcal{H}_{i , j_{k}}$ and the airway $\mathcal{A}_{i , j_{\text{in}} j_{k}}$, and the off-ramp $\mathcal{R}_{i , j_{k} j_{\text{out}}}$ connects the central island $\mathcal{H}_{i , j_{k}}$ and the airway $\mathcal{A}_{i , j_{k} j_{\text{out}}}$, where $j_{\text{in}} , j_{\text{out}} \in \left\{j_{1} , j_{2} , \hdots , j_{\bar{M}}\right\}$. Furthermore, each ramp consists of a ramp zone and a buffer zone (for example, the on-ramp $\mathcal{R}_{i , j_{\text{in}} j_{k}}$ consists of a ramp zone denoted by $\mathcal{R}_{i , j_{\text{in}} j_{k} , \text{ram}}$ and a buffer zone denoted by $\mathcal{R}_{i , j_{\text{in}} j_{k} , \text{buf}}$); specifically, the ramp zone $\mathcal{R}_{i , j_{\text{in}} j_{k} , \text{ram}}$ is modeled as an annular sector set whose middle horizontal plane and height are the same with the airway $\mathcal{A}_{i , j_{\text{in}} j_{k}}$, and the buffer zone $\mathcal{R}_{i , j_{\text{in}} j_{k} , \text{buf}}$ is modeled as a *sloped* annular sector set whose center, inner radius and outer radius are the same with $\mathcal{H}_{i , j_{k}}$. By the definitions above, we propose the following *Roundabout Design Requirements* for the design of the 3-D roundabout structure.

![Fig. 9 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr9.jpg)

Download: Download high-res image (444KB)

**Roundabout Design Requirement 1.** All ramps in the same roundabout are geometrically identical.

**Roundabout Design Requirement 2.** There is no intersection between each ramp zone and the central island.

**Roundabout Design Requirement 3.** The central island’s and each ramp’s inner radius should be both larger than a maximum turn radius of aircraft *r* <sub>turn</sub> for safety consideration.

**Roundabout Design Requirement 4.** For the projection of the roundabout on the middle horizontal plane, there is no intersection between each ramp zone and buffer zone.

**Roundabout Design Requirement 5.** For the projection of the roundabout on the middle horizontal plane, each ramp zone’s inner and outer circles are tangent to the boundary of their corresponding airway and the central island, respectively.

To simplify the analysis, a single-lane roundabout model is shown in, where only two airways $\mathcal{A}_{i , j_{\text{1}} j_{k}}$ and $\mathcal{A}_{i , j_{k} j_{\text{1}}}$ are reserved, and only the airway $\mathcal{A}_{i , j_{\text{1}} j_{k}}$ and the on-ramp $\mathcal{R}_{i , j_{\text{1}} j_{k}}$ need to be considered because of *Roundabout Design Requirement 1*. Then, *Roundabout Design Requirement 2* is written as(22) $\begin{matrix}h_{\text{r}} \geq h_{i , \text{aw}} ,\end{matrix}$where *h* <sub>r</sub> is the altitude difference between the central island and each airway or ramp. Furthermore, for simplicity, the point **o** denotes the center of $\mathcal{R}_{i , j_{\text{1}} j_{k}}$, **p** <sub>1</sub> denotes the perpendicular foot point from $\mathbf{p}_{i , j_{k}}$ to the intersecting plane of $\mathcal{A}_{i , j_{\text{1}} j_{k}}$ and $\mathcal{R}_{i , j_{\text{1}} j_{k}}$, **p** <sub>2</sub> and **p** <sub>3</sub> denote the tangent points of the ramp $\mathcal{R}_{i , j_{\text{1}} j_{k}}$ and the central island $\mathcal{H}_{i , j_{k}}$, *r* <sub>1</sub> and *r* <sub>2</sub> denote the inner radius and outer radius of $\mathcal{R}_{i , j_{\text{1}} j_{k}}$, respectively. The angles *θ* <sub>1</sub> and *θ* <sub>2</sub> denote the angle $\angle \mathbf{p}_{1} \mathbf{p}_{i , j_{k}} \mathbf{p}_{3}$ and ∠ **p** <sub>1</sub> **op** <sub>2</sub>, respectively, and *θ* <sub>3</sub> denotes the arc angle of each buffer zone. Obviously, *Roundabout Design Requirements 3 and 4* imply that(23) $\begin{aligned}r_{i , j_{k} , \text{in}} & > r_{\text{turn}} ,\end{aligned}$(24) $\begin{aligned}r_{1} & > r_{\text{turn}} ,\end{aligned}$(25) $\begin{aligned}\theta_{1} + \theta_{3} & < \frac{\pi}{\bar{M}} .\end{aligned}$By geometrical relationships, *Roundabout Design Requirement 5* indicates that the points **o, p** <sub>2</sub>, **p** <sub>3</sub>, and $\mathbf{p}_{i , j_{k}}$ are collinear, that is,(26) $\begin{aligned}sin \theta_{1} & = \frac{2 r_{2} + r_{i , \text{asb}}}{2 \left(r_{i , j_{k} , \text{in}} + r_{i , \text{aw}} + r_{1}\right)} ,\end{aligned}$(27) $\begin{aligned}\theta_{2} & = \frac{\pi}{2} - \theta_{1} ,\end{aligned}$(28) $\begin{aligned}r_{2} & = r_{1} + r_{i , \text{aw}} .\end{aligned}$According to *Roundabout Design Requirements 1–5* above, the design parameters are *r* <sub>1</sub>, *r* <sub>2</sub>, $r_{i , j_{k} , \text{in}}$, *θ* <sub>1</sub>, *θ* <sub>2</sub>, and *θ* <sub>3</sub>. First, the design parameters are reduced to *r* <sub>1</sub>, $r_{i , j_{k} , \text{in}}$, *θ* <sub>1</sub>, *θ* <sub>3</sub> by the relationships and. These parameters can be designed by the inequality and equality constraints –. The result here is shown in.

**Proposition 5**

*For the hub intersection* $\mathbf{n}_{i , j_{k}}$ *, if the constraints* *–* *are satisfied, then Roundabout Design Requirements 1–5 for the proposed three dimensional roundabout hold.*

**Proof**

The proof is *easily derived from the analysis above.*

### 3.4. Boundary intersection design

The boundary intersection can be regarded as the inlet/outlet node of the sky highway structure, as shown in. The *boundary intersections* are classified into two types according to the vertiport or free flight airspace they connect. The former is called *vertiport termination*, and the latter is called *free flight airspace termination.* It is required that each airway connected to boundary intersections must maintain a consistent altitude, wherein its center line aligns parallel to the ground.

![Fig. 10 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr10.jpg)

Download: Download high-res image (166KB)

The fundamental configuration of the vertiport model comprises a basic vertiport termination and a virtual vertical airway extending down to the ground, as illustrated in (a). Subsequently, the fundamental vertiport termination is regarded as an intersection that links a *tangible airway* and a *virtual vertical airway*, as illustrated in (a). In order for an aircraft to commence its take-off sequence, it must first be armed. This indicates that the aircraft is permitted to enter the vertiport termination from the virtual vertical airway. Subsequently, the aircraft will ascend to the entrance of the actual airway and subsequently maintain a level flight path within. In the case of landing, the aircraft will first enter the vertiport termination and descend to the ground. Subsequently, the aircraft may be disarmed and considered to have departed the vertiport. In this instance, the vertiport termination is regarded as an altitude-connected intersection, which is required similarly to. This basic vertiport model can be further extended to a general vertiport model with multiple tarmacs, where the boundary intersection is transformed into a hub intersection that connects several basic vertiport terminations, as illustrated in (b).

![Fig. 11 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr11.jpg)

Download: Download high-res image (264KB)

A free flight airspace termination is also regarded as a connected intersection, which serves to link a tangible airway with a number of *temporal airways*. For each aircraft operating within the free airspace, a temporal carriageway will be connected to the termination point as a preliminary measure. Once an aircraft has entered the termination, the temporal airway may be removed. In the event that an aircraft departs the network from a free flight airspace termination, a temporal airway connected to the aforementioned intersection will be generated for the UAV in question. Once the aircraft has left the termination and entered the temporal airway, the temporal airway can be deleted from the network. It should be noted that, in contrast to the virtual airways associated with vertiport terminations, the temporal airways exist in practice. Consequently, the resulting intersection should satisfy the requirements set forth in and, with due consideration given to temporal airways.

## 4\. Flight modes design for sky highway structure

Motivated by our previous work (, ), a *virtual tube flight mode* is designed for the proposed airway structure. This flight mode combines the characteristics of three skyline structures proposed in; specifically, the virtual tube is bidirectional and divided into several lanes with no center line restriction. Moreover, the proposed virtual tube can be straight or arc corresponding to different sky highway elements.

### 4.1. Straight tube flight mode for airways

We first define the origin plane $\mathcal{P}_{i , j_{1} j_{2} , \text{o}}$ and the destination plane $\mathcal{P}_{i , j_{1} j_{2} , \text{d}}$ of an airway $\mathcal{A}_{i , j_{1} j_{2}}$ as the following sets $\begin{matrix}\mathcal{P}_{i , j_{1} j_{2} , o} = \left\{\mathbf{n} \in \mathbb{R}^{3} \left|\right. \left(\mathbf{n} - \mathbf{p}_{i , j_{1} j_{2} , \text{aio}}\right)^{T} \left(\mathbf{p}_{i , j_{1} j_{2} , \text{aio}} - \mathbf{p}_{i , j_{1} j_{2} , \text{aid}}\right) = 0\right\} , \\ \mathcal{P}_{i , j_{1} j_{2} , d} = \left\{\mathbf{n} \in \mathbb{R}^{3} \left|\right. \left(\mathbf{n} - \mathbf{p}_{i , j_{1} j_{2} , \text{aid}}\right)^{T} \left(\mathbf{p}_{i , j_{1} j_{2} , \text{aio}} - \mathbf{p}_{i , j_{1} j_{2} , \text{aid}}\right) = 0\right\} .\end{matrix}$The aircraft in each airway have a unique distributed control protocol with three *airway control requirements* correspond to *Basic Requirements 1, 3, 4*. Taking the airway $\mathcal{A}_{i , j_{1} j_{2}}$ as an example, the following *Airway Flight Requirements* are proposed:

**Airway Flight Requirement 1.** Each aircraft should approach the finish plane $\mathcal{P}_{i , j_{1} j_{2}}$ in a finite time.

**Airway Flight Requirement 2.** In the airway, the minimum distance between aircraft should be always larger than a predefined safety distance 2 *r* <sub>s</sub>.

**Airway Flight Requirement 3.** Each aircraft should always keep a distance from the boundary of the airway $\mathcal{A}_{i , j_{1} j_{2}}$ larger than its safety radius *r* <sub>s</sub>.

It should be noted that the distributed control protocol implies that each aircraft is only able to engage in avoidance maneuvers with its neighboring aircraft within a certain distance corresponding to its controller. This is consistent with the definition presented in. It should be noted that conflicts are not necessarily mutual due to the differing priorities of aircraft. In the event that an aircraft has a higher priority, it is not required to actively avoid other aircraft with lower priorities. In accordance with *Basic Requirement 5*, overtaking is permitted in the virtual tube flight mode. This entails the faster aircraft overtaking the slower one, which consequently gives rise to a conflict between the two aircraft.

Moreover, in order to ensure the safety of all parties involved, it is imperative that as few conflicts as possible arise among aircraft operating within the same airway. As with the fast and slow lanes on the ground, different speed ranges are predefined for different lanes in the same airway, as illustrated in. In order to reduce conflicts, aircraft should select different lanes in accordance with their respective flight speeds. This approach represents a significant departure from our previous work (), as evidenced by the introduction of the multi-lane design. It is similarly recommended that aircraft avoid changing lanes unless absolutely necessary. In other words, each aircraft should remain in the lane that corresponds to its flight speed (maintaining the distance from the boundary of the lane). In accordance with the right-hand traffic convention proposed for the airway structure, the speed range for different lanes decreases from left to right. The rightmost lane may be designed as an emergency lane connected with temporary on/off ramps In the event of an emergency, such as rotor failure or low battery, aircraft may enter or exit the sky highway via these ramps. This has the potential to enhance the safety and resilience of low-altitude air traffic management systems.

![Fig. 12 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr12.jpg)

Download: Download high-res image (510KB)

The proposed virtual tube flight mode is suitable for low-altitude air traffic management for the following reasons. (i) In comparison to a predefined path for all aircraft, which is analogous to a railway for trains, the airspace is utilized to a sufficient extent, which has the potential to enhance the capacity of the airspace. (ii) The design of isolation belts ensures the safety of all parties involved. (iii) The multi-lane structure has the capacity to reduce the likelihood of potential conflicts and improve traffic efficiency by distinguishing the speed range of aircraft. (iv) The emergency case is taken into consideration by the designed emergency lane and exit ramp.

### 4.2. Arc road flight mode for connected intersections

Furthermore, an *arc road flight mode* is designed for the proposed arc airway structure and roundabout structure. The aircraft in each connected intersection have the unique distributed control protocol with the following *arc road control requirements*. Take the azimuth connected intersection $\mathcal{I}_{i , j_{2} , \text{az}}$ as an example, which connects two pairs of airways $\left(\mathcal{A}_{i , j_{1} j_{2}} , \mathcal{A}_{i , j_{2} j_{3}}\right) , \left(\mathcal{A}_{i , j_{3} j_{2}} , \mathcal{A}_{i , j_{2} j_{1}}\right)$ with the corresponding arc airways $\mathcal{I}_{i , j_{1} j_{2} j_{3}}$, $\mathcal{I}_{i , j_{3} j_{2} j_{1}}$ inside it, the *Arc Road Flight Requirements* are in the following:

**Arc Road Flight Requirement 1.** Each aircraft at the arc airways $\mathcal{I}_{i , j_{1} j_{2} j_{3}}$, $\mathcal{I}_{i , j_{3} j_{2} j_{1}}$ should approach the planes $\mathcal{P}_{i , j_{2} j_{3} , \text{o}} , \mathcal{P}_{i , j_{2} j_{1} , \text{o}}$ in a finite time, respectively.

**Arc Road Flight Requirement 2.** In the connected intersection, the minimum distance between aircraft should be always larger than a predefined safety distance 2 *r* <sub>s</sub>.

**Arc Road Flight Requirement 3.** Each aircraft should always keep a distance from the boundary of the arc airway $\mathcal{I}_{i , j_{1} j_{2} j_{3}}$ larger than its safety radius *r* <sub>s</sub>.

It is obvious that *Basic Requirements 3 and 4* are satisfied by *Arc Road Flight Requirements 2 and 3. Arc Road Flight Requirement 1* implies that the arc road mode can be regarded as the virtual tube flight mode with arc boundaries. The only difference from the virtual tube flight mode is that lane changing is not allowed for safety reasons. When an aircraft enters the arc airway, its flight mode should be switched to the proposed arc road flight mode until it leaves the arc airway.

Obviously, by the proposed arc road flight mode, each aircraft flying in the connected intersection can achieve the transition from one airway to another while satisfying *Basic Requirements 1–5*. Similarly, the proposed 3-D roundabout can be regarded as a combination of multiple arc roads. By switching arc road flight modes, aircraft can enter and leave the hub intersection while satisfying *Basic Requirements 1–5*.

### 4.3. FIFO flight mode for boundary intersections

As for the flight mode in the boundary intersection, an easy mode is proposed here, i.e., only one aircraft is permitted in each boundary intersection so that no conflicts will happen among aircraft. The boundary intersection will serve the first aircraft in a queue, with others waiting (hovering) on their airways outside of the boundary intersection if they have reached the entrance/exit. If the aircraft has entered into a virtual or temporal airway, the aircraft can be considered to have left the termination or, that is to say, the sky highway. Then, the second aircraft will shift to the first one, and so on. All aircraft will leave or enter in the order according to their requests. An aircraft with the highest priority can move to the first of the queue. This flight mode is called First In First Out (FIFO) flight mode. Since a termination can only have one aircraft at most, *Basic Requirements 1–5* are satisfied.

## 5\. Simulation of sky highway

Motivated by the current fast-time simulation schemes for air traffic management (), a simulation platform is developed to show the effectiveness of the proposed sky highway structure, as shown in. A video is available on [https://youtu.be/URRFmUB8JJA](https://youtu.be/URRFmUB8JJA) to show the proposed simulation platform and the simulation results.

![Fig. 13 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr13.jpg)

Download: Download high-res image (1MB)

### 5.1. Sky highway simulation platform architecture

In this section, the sky highway simulation platform architecture is proposed, as shown in. The details of the modules are introduced in the following.

![Fig. 14 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr14.jpg)

Download: Download high-res image (241KB)

#### 5.1.1. Preset settings

Prior to the takeoff and ascent of each aircraft, a series of global data points must be preloaded, collectively referred to as *preset settings*. Specifically, the preset settings for each aircraft consist of three elements: (i) the sky highway structure, which contains the general traffic network model and the design parameters of all elements (airways and intersections), (ii) the origin and destination of the aircraft, which are represented as the boundary intersections, and (iii) the safety radius and the avoidance radius of the aircraft. These settings will remain unchanged throughout the flight process.

### 5.2. Simulation setup

Without loss of generality, the following conditions are considered in the simulation:
- (i)
	The traffic network is one layer with an altitude range from 100m to 140m.
- (ii)
	All nodes are at the same altitude, i.e., there is no altitude connected intersection in this network.
- (iii)
	All aircraft have the same priority to simplify the simulation, i.e., the collision avoidance maneuvers are cooperative for each pair of aircraft.

In the following definitions of the traffic network, the index of the layer is omitted for simplicity because of condition (i) (e.g., the notation of airway $\mathcal{A}_{i , j_{1} j_{2}}$ is simplified as $\mathcal{A}_{j_{1} j_{2}}$). Furthermore, the specific design for the sky highway structure corresponds to the designed simulation scenario, which will be introduced in the following.

#### 5.2.1. Aircraft kinematic model

The kinematic model of the *k* th VTOL aircraft is described as follows, refer to, for further information,(29) $\begin{aligned}\left(\overset{\cdot}{\mathbf{p}}\right)_{k , \text{v}} & = \mathbf{v}_{k , \text{v}} ,\end{aligned}$(30) $\begin{aligned}\left(\overset{\cdot}{\mathbf{v}}\right)_{k , \text{v}} & = - l_{k , \text{v}} \left(\mathbf{v}_{k , \text{v}} - \mathbf{v}_{k , \text{c}}\right) ,\end{aligned}$(31) $\begin{aligned}\left\|\mathbf{v}_{k , \text{c}}\right\| & \leq v_{k , \text{max}} ,\end{aligned}$where $\mathbf{p}_{k , \text{v}} , \mathbf{v}_{k , \text{v}} , \mathbf{v}_{k , \text{c}} \in \mathbb{R}^{3}$ and *l* <sub><em>k</em>,v</sub>, *v* <sub><em>k</em>,max</sub>  > 0 are the position, velocity, velocity command, control gain and maximum velocity of the *k* th aircraft, respectively. All aircraft are set with the same safety radius $r_{\text{s}} = 2 \text{m}$, avoidance radius $r_{\text{a}} = 3 \text{m}$, maximum turn radius $r_{\text{turn}} = 2 \text{m}$, and maximum velocity corresponding to different scenarios. Furthermore, to simplify the controller design and analysis, a filtered position model is defined as(32) $\begin{matrix}\mathbf{\mathit{\xi}}_{k , \text{v}} \triangleq \mathbf{p}_{k , \text{v}} + \frac{1}{l_{k , \text{v}}} \mathbf{v}_{k , \text{v}} .\end{matrix}$By the definition of the filtered position, the motion of each aircraft can be transformed into a single integrator form as(33) $\begin{aligned}\overset{\cdot}{\mathbf{\mathit{\xi}}}_{k , \text{v}} & = \left(\overset{\cdot}{\mathbf{p}}\right)_{k , \text{v}} + \frac{1}{l_{k , \text{v}}} \left(\overset{\cdot}{\mathbf{v}}\right)_{k , \text{v}} = \mathbf{v}_{k , \text{c}} .\end{aligned}$The relationship between filtered position and position is given in (), which indicates that the position error of any pair of aircraft is large enough as long as the filtered position error is also large enough. Therefore, the filtered position is used as the feedback in the designed distributed collision-free controller described in the following subsection.

#### 5.2.2. Distributed collision-free control model

The distributed collision-free controller for aircraft is designed based on recent works (,,,, ). For the airway $\mathcal{A}_{j_{1} j_{2}}$ with the corresponding origin $\mathbf{p}_{j_{1} j_{2} , \text{o}}$ and destination $\mathbf{p}_{j_{1} j_{2} , \text{d}}$, the following filtered position errors are defined as(34) $$(35) $$(36) $$where $\mathbf{A}_{j_{1} j_{2} , \text{1}}$, $\mathbf{A}_{j_{1} j_{2} , \text{2}}$ are the projection operators defined as(37) $$(38) $$where **I** <sub>3</sub> denotes the third-order unit matrix. Specifically, the controller that allows an aircraft to fly within the airway $\mathcal{A}_{j_{1} j_{2}}$ is described as the following velocity command(39) $$where $k_{1} = 1$, $\mathcal{N}_{m , k}$ is the collection of all mark numbers of other aircraft whose safety areas enter into the avoidance area of the *k* th aircraft, i.e. $\mathcal{N}_{m , k} = \left\{\right. j \left|\right. \mathcal{S}_{j} \cap \mathcal{A}_{k} \neq \emptyset , k \neq j \left.\right\}$, *V* <sub>m,<em>kj</em></sub> and *V* <sub>t,<em>k</em></sub> are called the Lyapunov-like functions for avoiding conflict with other aircraft and the edge of the airway given in. Note that the proposed controller is distributed because only the neighboring aircraft’s states are used for feedback. The stability of the proposed controller is proved (), which includes (i) each aircraft will keep a defined safety separation with the neighboring aircraft described as the neighboring set $\mathcal{N}_{m , k}$, and (ii) each aircraft will reach the airway’s destination plane $\mathcal{P}_{j_{1} j_{2} , \text{d}}$. Furthermore, the proposed controller should be revised under other flight modes corresponding to other elements; specifically, (i) for the arc roads flight mode, the first and the third terms of should be revised (), and (ii) for the free flight mode, the third term of should be removed ().

#### 5.2.3. Centralized scheduling model

In the centralized scheduling model, real-time traffic characteristics for each element of the sky highway can be utilized for feedback centralized control. Specifically, the performance metrics for each element including the two aspects: (i) the aircraft level, including the average speed *U* (*t*), and (ii) the element level, including the accumulation *N* (*t*), generalized density *K* (*t*), average absolute average flow *Q* (*t*), and outflow *G* (*t*) (trip completion rate) modeled in at each time. For each element (airway, connected intersection, or hub intersection), let the parameters *A, S* denote the volume of the element, the volume of each multicopter’s safety area, respectively. For a predefined scheduling time period $\Delta t_{\text{TFC}}$, define the displacement vector of the *k* th aircraft as(40) $\begin{matrix}\mathbf{d}_{k} \left(t\right) = \mathbf{p}_{k , \text{v}} \left(t\right) - \mathbf{p}_{k , \text{v}} \left(t - \Delta t_{\text{TFC}}\right) .\end{matrix}$

Furthermore, during the time interval $\left(t - \Delta t_{\text{TFC}} , t\right]$, define *τ <sub>k</sub>* (*t*) as the time spent of the *k* th aircraft in the element, the set *I* (*t*) as the index set of all aircraft flying into the element, and the set *D* (*t*) as the index set of all aircraft leave the element. Then, the performance metrics above are further defined as (41) $\begin{aligned}N \left(t\right) & = \text{card} \left(I \left(t\right)\right) ,\end{aligned}$(42) $\begin{aligned}K \left(t\right) & = \frac{\underset{k \in I \left(t\right)}{\sum} \tau_{k} \left(t\right)}{A \Delta t_{\text{TFC}}} ,\end{aligned}$(43) $\begin{aligned}U \left(t\right) & = \frac{\underset{k \in I \left(t\right)}{\sum} \left\|\mathbf{d}_{k} \left(t\right)\right\|}{\underset{k \in I \left(t\right)}{\sum} \tau_{k} \left(t\right)} ,\end{aligned}$(44) $\begin{aligned}Q \left(t\right) & = \frac{\underset{k \in I \left(t\right)}{\sum} \left\|\mathbf{d}_{k} \left(t\right)\right\|}{A \Delta t_{\text{TFC}}} ,\end{aligned}$(45) $\begin{aligned}G \left(t\right) & = \frac{\text{card} \left(D \left(t\right)\right)}{\Delta t_{\text{TFC}}} ,\end{aligned}$which can further be the feedback to guide the design of centralized scheduling/routing policies.

### 5.3. Simulation scenarios and results

In this work, four simulation scenarios are designed, which include (i) a single airway with various widths, (ii) a comparison of different structures at the hub intersection, (iii) a completed grid network designed with the proposed sky highway structure, and (iv) different routing policies. In all designed scenarios, the time period for updating the traffic characteristics is $\Delta t_{\text{TFC}} = 0.5 \text{s}$, while the time period for routing control command is $\Delta t_{\text{ro}} = 30 \text{s}$. In scenarios (i), (iii), and (iv), each airway only contains one lane, while the varying numbers of lanes is considered in scenario (ii).

#### 5.3.1. A single airway with various widths

In the first simulation scenario, the influence of the designed airway’s width is investigated. Intuitively, a wider airway implies (i) a greater allowable traffic inflow, (ii) fewer conflicts among aircraft compared to narrower airways when the flow is fixed, and (iii) a larger airspace utilization area of the airspace. This suggests that there are irreconcilable internal contradictions among safety, efficiency, and airspace occupancy. For these reasons, it is necessary to find the optimal airway width design to achieve a tradeoff among such contradictions. Without loss of generality, a single horizontal airway with a fixed length of 200m, a fixed height of 20m, and a maximum allowed inflow $Q_{i n} = 1 \text{aircraft}/\text{s}$ is considered. This implies that the minimum airway width is 2 *r* <sub>a</sub>. Each aircraft’s maximum velocity is uniformly distributed within the range \[6, 10\]m/s. Another obvious conclusion is that overtaking is only allowed when the airway’s width is larger than $3 r_{\text{a}} + r_{\text{s}}$. In this scenario, the case where the airway’s width progressively increases at intervals of $2 r_{\text{a}} = 6 \text{m}$ is considered, while each aircraft with a fixed altitude will enter the airway at a random position, which is conflict-free with the airway’s boundary located at the origin plane of the airway. To investigate the effect of inflow on results, two cases are simulated: (i) $Q_{i n} = 0.5 \text{aircraft}/\text{s}$ and (ii) $Q_{i n} = 1 \text{aircraft}/\text{s}$. The simulation results include (i) the average outflow *G* (*t*) of the airway, (ii) the average speed *U* (*t*) of the aircraft, and (iii) the number of conflicts among aircraft, which are shown in and [^2]. The simulation results provide the following insights:
- •
	The average speed of aircraft increases and the number of conflicts decreases with the greater airway width, which is consistent with intuition. Conversely, the outflow does not show significant changes corresponding to the varying widths when overtaking is allowed (i.e., the width is greater than $3 r_{\text{a}} + r_{\text{s}} = 11 \text{m}$).
- •
	With the inflow 0.5 aircraft/s, the average speed increases uniformly when the width grows from 2 *r* <sub>a</sub> to 10 *r* <sub>a</sub> and becomes steadily when the airway width is greater than 10 *r* <sub>a</sub>. When the inflow increases to 1 aircraft/s, the width that stabilizes the average speed becomes greater at 14 *r* <sub>a</sub>. This implies the best-designed airway width from the perspective of traffic efficiency.
- •
	The number of conflicts keeps decreasing uniformly with the greater airway width. Therefore, from the perspective of safety, the traffic manager should determine the allowable level of conflicts per unit time first, and then design the minimum airway width to save airspace as much as possible.

Table 1. Traffic characteristics for a single airway with a simulation time step 0.1s, an inflow 0.5 aircraft/s, various widths ranging from $2 r_{\text{a}} = 6 \text{m}$ to $12 r_{\text{a}} = 36 \text{m}$, including outflow, average speed, and the number of conflicts. Note that the number of conflicts is not meaningful when the airway’s width is 2 *r* <sub>a</sub>, as overtaking is not allowed.

| Traffic characteristics Airway’s width (m) | 2 *r* <sub>a</sub> | 4 *r* <sub>a</sub> | 6 *r* <sub>a</sub> | 8 *r* <sub>a</sub> | 10 *r* <sub>a</sub> | 12 *r* <sub>a</sub> |
| --- | --- | --- | --- | --- | --- | --- |
| Outflow (aircraft/s) | 0.39 | 0.41 | 0.42 | 0.41 | 0.42 | 0.42 |
| Average speed (m/s) | 6 | 7.29 | 7.65 | 7.69 | 7.98 | 7.96 |
| Number of conflicts | 0 | 121 | 107 | 101 | 99 | 87 |

Table 2. Traffic characteristics for a single airway with a simulation time step 0.1s, an inflow 1 aircraft/s, various widths ranging from $2 r_{\text{a}} = 6 \text{m}$ to $14 r_{\text{a}} = 42 \text{m}$, including outflow, average speed, and the number of conflicts.

| Traffic characteristics Airway’s width (m) | 2 *r* <sub>a</sub> | 4 *r* <sub>a</sub> | 6 *r* <sub>a</sub> | 8 *r* <sub>a</sub> | 10 *r* <sub>a</sub> | 12 *r* <sub>a</sub> | 14 *r* <sub>a</sub> | 16 *r* <sub>a</sub> |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Outflow (aircraft/s) | 0.77 | 0.80 | 0.83 | 0.83 | 0.82 | 0.82 | 0.83 | 0.84 |
| Average speed (m/s) | 6 | 7.28 | 7.48 | 7.56 | 7.66 | 7.73 | 7.83 | 7.79 |
| Number of conflicts | 0 | 469 | 464 | 443 | 439 | 429 | 408 | 353 |

#### 5.3.2. Comparison of different structures at the hub intersection

*Balanced Traffic Demand with Two-Lane Case*

In the second simulation scenario, to better illustrate the advantages of the 3-D roundabout design at the hub intersection, we consider the number of conflicts among VTOL aircraft for three different structures: (i) the proposed 3-D roundabout, (ii) the traditional 2-D roundabout, and (iii) the unstructured airspace. To simplify the simulation scenario, the network only consists of one hub intersection connecting three pairs of airways. Each airway contains two lanes with the same width $r_{i , \text{lane}} = 19 \text{m}$ and one lane isolation belt with the width $r_{i , \text{lsb}} = 2 \text{m}$. The node set $\mathcal{N}$ of the traffic network is denoted as $\mathcal{N} = \left\{n_{1} , n_{2} , n_{3} , n_{4}\right\}$ with the positions of the nodes $\mathbf{p}_{1} = \left[- 100 173 120\right]^{\text{T}} \text{m}$, $\mathbf{p}_{2} = \left[- 100 - 173 120\right]^{\text{T}} \text{m}$, $\mathbf{p}_{3} =$ \[200 0 120\] <sup>T</sup> m, $\mathbf{p}_{4} = \left[0 0 120\right]^{\text{T}} \text{m}$. The edge set $\mathcal{E}$ is denoted as $\begin{aligned}\mathcal{E} = & \left\{\right. \left(n_{1} , n_{4}\right) , \left(n_{2} , n_{4}\right) , \left(n_{3} , n_{4}\right) , \left(n_{4} , n_{1}\right) , \left(n_{4} , n_{2}\right) , \left(n_{4} , n_{3}\right) \left.\right\} .\end{aligned}$Then, the node sets $\mathcal{N}_{\text{e}} , \mathcal{N}_{\text{c}} , \mathcal{N}_{\text{h}}$ can be written as $\mathcal{N}_{\text{e}} =$ { *n* <sub>1</sub>, *n* <sub>2</sub>, *n* <sub>3</sub> }, $\mathcal{N}_{\text{c}} = \emptyset$, $\mathcal{N}_{\text{h}} = \left\{n_{4}\right\}$. The aircraft model is set the same as the first simulation scenario (see ). The traffic demand is balanced across all boundary intersections { *n* <sub>1</sub>, *n* <sub>2</sub>, *n* <sub>3</sub> }, meaning that aircraft departing from any single boundary intersection are evenly distributed to all other boundary intersections. The design parameters of the 3-D roundabout $\mathcal{H}_{i , j_{k}}$ are set as follows: $h_{\text{r}} = 20 \text{m}$, $r_{1} = 88.64 \text{m}$, $r_{3 , \text{in}} = 95 \text{m}$, $\theta_{1} = 0.655 \text{rad}$, $\theta_{3} = \pi / 8$, which satisfy the constraints –. For the traditional 2-D roundabout, the buffer zones are removed. In the unstructured free flight airspace, each aircraft entering the airspace will fly directly to the origin plane of the next airway while avoiding collisions with other aircraft, as shown in (a). Over a duration of 10 minutes, the fixed lane inflow for each boundary intersection is set between 0.2 aircraft/s and 1.6 aircraft/s during the first 5 minutes, while the inflow is set as zero during the last 5 minutes. The relationships among the average speed *U* (*t*), accumulation *N* (*t*), and outflow *G* (*t*) of the hub intersection are extracted, and the results are shown in. Furthermore, we compare the number of conflicts with intervals of 0.2s from 0.2 aircraft/s to 1.2 aircraft/s under different structures at the hub intersection, as shown in, where the definition of the conflicts is consistent with. In other words, a conflict occurs when the separation between two aircraft falls below the predefined threshold that activates the collision avoidance algorithm, indicating that one aircraft has entered the avoidance area of another. This event triggers the collision avoidance maneuvers executed by the distributed control algorithm. The simulation results provide the following insights:
- •
	In comparison to the traditional 2-D roundabout, the unstructured airspace exhibits a reduced incidence of conflicts among aircraft. The primary reason is that the roundabout structure reduces the area of airspace utilized, and 1.2 aircraft per second represents the maximum lane inflow for a 2-D roundabout in this scenario. This phenomenon occurs because some aircraft begin to violate *Arc Road Flight Requirement 3*, i.e., they fly out of the roundabout’s boundary due to inter-agent safety constraints, as illustrated in (a). In contrast, the 3-D roundabout has the potential to mitigate conflicts among aircraft with the same inflow to a greater extent than the 2-D roundabout and unstructured airspace. This is particularly evident when the inflow is higher. This indicates that the proposed 3-D roundabout structure not only reduces the airspace utilization area but also enhances safety and circumvents congestion.
	![Fig. 19 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr19.jpg)
	Download: Download high-res image (498KB)
- •
	At low demand levels (e.g., up to 0.6 aircraft/s per lane), all structures exhibit similar performance. Although there is some scatter in the results, the average values remain comparable. As the inflow increases, notable differences in performance emerge. In moderate inflow conditions (e.g., 0.6-1.2 aircraft/s), the unstructured setup outperforms the 2-D roundabout structure, achieving higher speeds and avoiding highly congested states (characterized by very high accumulation and low speed), as shown in and (a). However, it is outperformed by the 3D structure, which maintains similar high speeds to the unstructured case but supports larger accumulations more effectively. At higher inflow levels (e.g., above 1.4 aircraft/s), congestion becomes a significant issue. As illustrated in and (b), the unstructured configuration starts to break down, with points appearing in the congested regime (e.g., at 1.6 aircraft/s). In contrast, the proposed 3-D roundabout structure continues to sustain high speeds while maintaining lower accumulation levels, demonstrating superior performance under heavy demand. Furthermore, the space occupancy of the 3-D roundabout is superior to that of the unstructured airspace, which enhances the potential for applications (e.g., the roundabout design remains effective when the airspace within the central island is invalid). These findings also demonstrate the efficacy of the proposed 3-D roundabout design in scenarios with higher traffic inflow.

![Fig. 17 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr17.jpg)

Download: Download high-res image (243KB)

![Fig. 18 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr18.jpg)

Download: Download high-res image (871KB)

Table 3. The number of conflicts under three different structures at the hub intersection during 10 minutes, while the fixed lane inflow from 0.2 aircraft/s to 1.2 aircraft/s is only within the first 5 minutes.

| Structure Number of conflicts Lane inflow | 0.2 | 0.4 | 0.6 | 0.8 | 1.0 | 1.2 |
| --- | --- | --- | --- | --- | --- | --- |
| 3-D roundabout | 2 | 131 | 835 | 928 | 1411 | 4302 |
| 2-D roundabout | 98 | 979 | 2719 | 2.67 × 10 <sup>4</sup> | 1.04 × 10 <sup>5</sup> | 2.87 × 10 <sup>5</sup> |
| Unstructured free flight airspace | 75 | 478 | 1211 | 3494 | 5330 | 1.44 × 10 <sup>4</sup> |

*Unbalanced Traffic Demand with Two-Lane Case*

In this comparative scenario, the performance of the 3-D roundabout and unstructured airspace under unbalanced demand scenarios is evaluated. The node set of the traffic network and the design parameters of the 3-D and 2-D roundabout are set same as Section 5.3.2.1, where each airway contains two lanes. We first considered two extreme cases of unbalanced demand: (i) concentrated demand on fixed aircraft’s routes { *n* <sub>1</sub>, *n* <sub>3</sub> }, { *n* <sub>3</sub>, *n* <sub>2</sub> }, and{ *n* <sub>2</sub>, *n* <sub>1</sub> } (called short routes), as shown in (a), and (ii) concentrated demand on fixed aircraft’s routes { *n* <sub>1</sub>, *n* <sub>2</sub> }, { *n* <sub>2</sub>, *n* <sub>3</sub> }, and{ *n* <sub>3</sub>, *n* <sub>1</sub> } (called long routes), as shown in (b).

![Fig. 20 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr20.jpg)

Download: Download high-res image (650KB)

Intuitively, aircraft in the 3-D roundabout structure afollowing short routes traverse significantly shorter distances, while those on long routes must navigate longer distances due to the circular geometry. On the other hand, for the aircraft in unstructured airspace, long routes and short routes types exhibit nearly identical path lengths due to the absence of structural constraints and the ability to follow direct trajectories between nodes, but different long routes inherently generate head-on conflicts for aircraft. To investigate the unbalanced demand cases, the unbalanced traffic demand is characterized by the proportion of short routes ({ *n* <sub>1</sub>, *n* <sub>2</sub> }, { *n* <sub>2</sub>, *n* <sub>3</sub> }, { *n* <sub>3</sub>, *n* <sub>1</sub> }) distributed to each boundary intersection’s aircraft, which ranges from 0% to 100%. For the proportion of long routes from 0% to 60%, the inflow rate at each boundary intersection varies from 0.2 aircraft/s to 1.6 aircraft/s, while for the proportion of long routes from 80% to 100%, the lane inflow rate is from 0.2 aircraft/s to 1.2 aircraft/s. The relationships among the average speed *U* (*t*), accumulation *N* (*t*), and outflow *G* (*t*) of the hub intersection are extracted, and the relationships among the average speed *U* (*t*), accumulation *N* (*t*), and outflow *G* (*t*) are shown in and. The simulation results provide the following insights:
- •
	When the proportion of long routes remains at or below 40%, both the 3-D roundabout and the unstructured airspace exhibit comparable performance metrics. Notably, the unstructured airspace consumes less airspace capacity for the same level of outflow, as evidenced by its lower accumulation under equivalent outflow conditions. This efficiency stems from the ability of aircraft to follow direct trajectories, minimizing travel distance and enhancing traffic efficiency when short routes dominate the hub intersection’s traffic demand.
- •
	As the proportion of long routes increases to 60% or beyond, the 3-D roundabout sustains a higher critical flow. Aircraft in the 3-D roundabout maintains high speeds under the lane inflow ranging from 0.2 aircraft/s to 1.6 aircraft/s while maintaining lower accumulation levels. In contrast, the unstructured airspace experiences severe congestion under high inflow rates, characterized by a rapid decline in the average speed *U* (*t*) and the outflow *G* (*t*). This highlights the traffic efficiency of the 3-D roundabout in some extreme imbalance scenarios, particularly those dominated by long routes at the hub intersection. These findings also demonstrate the robustness of the proposed 3-D roundabout design in scenarios with some extreme unbalanced traffic demand.

![Fig. 21 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr21.jpg)

Download: Download high-res image (1MB)

![Fig. 22 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr22.jpg)

Download: Download high-res image (1MB)

*Varying Numbers of Lanes*

In this comparative scenario, the influence of varying numbers of airway lanes is investigated under the proposed 3-D roundabout and the traditional 2-D roundabout. The node set of the traffic network and the design parameters of the 3-D and 2-D roundabout are set same as Section 5.3.2.1. Over a duration of 10 minutes, the fixed airway inflow for each boundary intersection is set as a range from 0.4 aircraft/s to 2.0 aircraft/s during the first 5 minutes, while the inflow is set as zero during the last 5 minutes, which is similar to the settings in Section 5.3.2.1. We consider three different cases where each airway contains one, two, and three lanes, respectively. For each fixed airway inflow, the aircraft is distributed equally among all lanes of the airway; in other words, the lane inflow is calculated as the airway inflow divided by the number of lanes. The number of conflicts among aircraft under the 3-D roundabout and the 2-D roundabout is shown in.

Table 4. The number of conflicts under the 3-D roundabout and the 2-D roundabout with varying number of airways during 10 minutes, while the fixed airway inflow from 0.4 aircraft/s to 2.0 aircraft/s is only within the first 5 minutes.

| Structure Number of conflicts Airway inflow | 0.4 | 0.8 | 1.2 | 1.6 | 2.0 |
| --- | --- | --- | --- | --- | --- |
| 3-D roundabout with one lane | 8 | 58 | 453 | 739 | 1058 |
| 3-D roundabout with two lanes | 2 | 131 | 835 | 928 | 1411 |
| 3-D roundabout with three lanes | 15 | 370 | 1142 | 1540 | 3661 |
| 2-D roundabout with one lane | 64 | 743 | 2666 | 2.09 × 10 <sup>4</sup> | 7.97 × 10 <sup>4</sup> |
| 2-D roundabout with two lanes | 98 | 979 | 2719 | 2.67 × 10 <sup>4</sup> | 1.04 × 10 <sup>5</sup> |
| 2-D roundabout with three lanes | 236 | 1153 | 8754 | 5.31 × 10 <sup>4</sup> | 1.94 × 10 <sup>5</sup> |

The results presented in clearly demonstrate the structural superiority of the 3-D roundabout in conflict mitigation across all tested scenarios. Notably, the 3-D roundabout exhibits a significantly lower number of conflicts compared to the 2-D roundabout, particularly under higher inflow rates and increased lanes. For instance, at an airway inflow of 2.0 aircraft/s with three lanes, the 3-D roundabout generates 3661 conflicts-nearly two orders of magnitude lower than the 1.94 × 10 <sup>5</sup> conflicts observed in the 2-D roundabout. This substantial reduction can be attributed to the vertical segregation of traffic flows in the 3-D design, which eliminates cross-directional inter-lane conflicts that are inherent in 2-D roundabouts. Furthermore, while the conflict count in the 3-D roundabout increases modestly with additional lanes due to higher traffic volume, the 2-D roundabout experiences exponential growth in conflicts as lane count rises, highlighting the scalability and congestion avoidance of the 3-D roundabout structure under dense traffic conditions. These findings underscore the critical role of 3-D design of the roundabout structure in enhancing safety and throughput in multi-lane cases.

#### 5.3.3. Grid network scenario

In the third simulation, a grid traffic network is considered to simulate parts of the practical urban air traffic scenario. Firstly, the node set $\mathcal{N} = \left\{n_{1} , n_{2} , \hdots , n_{12}\right\}$ is initialized with positions of the nodes $\mathbf{p}_{1} = \left[400 200 120\right]^{\text{T}} \text{m}$, $\mathbf{p}_{2} = \left[400 - 200 120\right]^{\text{T}} \text{m}$, $\mathbf{p}_{3} = \left[200 400 120\right]^{\text{T}} \text{m}$, $\mathbf{p}_{4} = \left[200 - 400 120\right]^{\text{T}} \text{m}$, $\mathbf{p}_{5} = \left[- 400 - 200 120\right]^{\text{T}} \text{m}$, $\mathbf{p}_{6} =$ $\left[- 400 200 120\right]^{\text{T}} \text{m}$, $\mathbf{p}_{7} = \left[- 200 400 120\right]^{\text{T}} \text{m}$, $\mathbf{p}_{8} = \left[200 400 120\right]^{\text{T}} \text{m}$, $\mathbf{p}_{9} = \left[200 200 120\right]^{\text{T}} \text{m}$, $\mathbf{p}_{10} = \left[200 - 200 120\right]^{\text{T}} \text{m}$, $\mathbf{p}_{11} = \left[- 200 - 200 120\right]^{\text{T}} \text{m}$, $\mathbf{p}_{12} = \left[- 200 200 120\right]^{\text{T}} \text{m}$. The edge set $\mathcal{E}$ is denoted as $\begin{aligned}\mathcal{E} = \left\{\right. & \left(n_{1} , n_{9}\right) , \left(n_{2} , n_{10}\right) , \left(n_{3} , n_{10}\right) , \left(n_{4} , n_{11}\right) , \left(n_{5} , n_{11}\right) , \left(n_{6} , n_{12}\right) , \left(n_{7} , n_{12}\right) , \left(n_{8} , n_{9}\right) , \left(n_{9} , n_{1}\right) , \left(n_{9} , n_{10}\right) , \\ \left(n_{9} , n_{12}\right) , \left(n_{9} , n_{8}\right) , \left(n_{10} , n_{2}\right) , \left(n_{10} , n_{3}\right) , \left(n_{10} , n_{11}\right) , \left(n_{10} , n_{9}\right) , \left(n_{11} , n_{4}\right) , \left(n_{11} , n_{5}\right) , \left(n_{11} , n_{12}\right) , \left(n_{11} , n_{10}\right) , \\ \left(n_{12} , n_{6}\right) , \left(n_{12} , n_{7}\right) , \left(n_{12} , n_{11}\right) , \left(n_{12} , n_{9}\right) \left.\right\} ,\end{aligned}$and the node sets $\mathcal{N}_{\text{e}} , \mathcal{N}_{\text{c}} , \mathcal{N}_{\text{h}}$ can be written as $\mathcal{N}_{\text{e}} = \left\{n_{1} , n_{2} , n_{3} , n_{4} , n_{5} , n_{6} , n_{7} , n_{8}\right\}$, $\mathcal{N}_{\text{c}} = \emptyset$, $\mathcal{N}_{\text{h}} = \left\{n_{9} , n_{10} , n_{11} , n_{12}\right\}$, as shown in.

![Fig. 23 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr23.jpg)

Download: Download high-res image (789KB)

According to the proposed geometrical structure design for the sky highway: (i) the airways and airway isolation belts have a width of $r_{\text{aw}} = 40 \text{m}$, $r_{\text{aib}} = 15 \text{m}$, with a height of $h_{i , \text{aw}} = 20 \text{m}$, and (ii) the design parameters of the four hub intersections are all set as $h_{\text{r}} = 20 \text{m}$, $r_{1} = 6.7425 \text{m}$, $r_{3 , \text{in}} = 95 \text{m}$, $\theta_{1} = 0.3927 \text{rad}$, $\theta_{3} = \frac{\pi}{8}$, which satisfy *Roundabout Intersection Design Requirements 1–5* by the constraints –.

All aircraft enter the sky highway from the eight boundary intersections with random destinations and the same inflow shown in (a). In this scenario, to compare performance, the proposed 3-D roundabout structure and unstructured airspace are utilized separately at the hub intersection. The relationships among the average speed *U* (*t*), accumulation *N* (*t*), and outflow *G* (*t*) of the entire traffic network are extracted with different maximum inflows $Q_{\text{in}} = 1 , 2 \text{aircraft}/\text{s}$ during 30 minutes, as shown in. The results indicate the following aspects:
- •
	With the increasing inflow before *t* =7.5min, the accumulation and outflow increase at the sky highway structure with the growing inflow, while the average speed remains stable in both structures. This implies that no congestion happens in the airspace.
- •
	With the fixed highest inflow from *t* = 7.5min to *t* = 22.5min, congestion still does not occur when $Q_{\text{in}} = 1$ aircraft/s in both the roundabout structure and unstructured airspace. However, when a greater maximum inflow $Q_{\text{in}} = 2$ aircraft/s is set, congestion occurs in the unstructured airspace rather than the 3-D roundabout structure, as evidenced by the increasing accumulation and decreasing average speed and outflow. This indicates that the designed three-roundabout can better handle larger traffic inflows in practice. Finally, from *t* = 22.5min to *t* = 30min, the inflow gradually decreases to 0, and the congestion is eventually resolved, consistent with expectations and further indicating the effectiveness of the distributed controller. Therefore, the effectiveness of the proposed sky highway structure is shown from another perspective.

**Remark 4**

The reason we set the maximum inflow of each boundary intersection as $Q_{\text{in}} = 2 \text{aircraft}/\text{s}$ is that safety constraints should be considered (), i.e., aircraft should not initially conflict with each other. On the other hand, in the simulation scenario, aircraft will continuously appear at its predefined origin and try to enter the traffic network according to the defined inflow, even if the congestion occurs near the origin. This indicates that the maximum inflow in the simulation is related to the affordability of the airspace structure design; otherwise, safety constraints for aircraft are violated initially when congestion happens at the origins, which leads to unreasonable results.

![Fig. 24 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr24.jpg)

Download: Download high-res image (199KB)

![Fig. 25 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr25.jpg)

Download: Download high-res image (410KB)

#### 5.3.4. Routing policies comparison with two-route scenario

In the last simulation scenario, the comparison of various routing policies is investigated in the sky highway structure. For simplicity, a two-route scenario is considered; specifically, the node set $\mathcal{N} = \left\{n_{1} , n_{2} , \hdots , n_{6}\right\}$ is initialized with positions of the nodes $\mathbf{p}_{1} = \left[- 600 0 120\right]^{\text{T}} \text{m}$, $\mathbf{p}_{2} = \left[- 300 0 120\right]^{\text{T}} \text{m}$, $\mathbf{p}_{3} = \left[0 500 120\right]^{\text{T}} \text{m}$, $\mathbf{p}_{4} = \left[300 0 120\right]^{\text{T}} \text{m}$, $\mathbf{p}_{5} = \left[600 0 120\right]^{\text{T}} \text{m}$, $\mathbf{p}_{6} =$ \[0 495 120\] <sup>T</sup> m. The edge set $\mathcal{E}$ is denoted as $\begin{aligned}\mathcal{E} = \left\{\right. & \left(n_{1} , n_{2}\right) , \left(n_{2} , n_{1}\right) , \left(n_{2} , n_{3}\right) , \left(n_{2} , n_{6}\right) , \left(n_{3} , n_{2}\right) , \left(n_{3} , n_{4}\right) , \left(n_{4} , n_{3}\right) , \left(n_{4} , n_{5}\right) , \left(n_{4} , n_{6}\right) , \left(n_{5} , n_{4}\right) , \\ \left(n_{6} , n_{2}\right) , \left(n_{6} , n_{4}\right) \left.\right\} ,\end{aligned}$and the node sets $\mathcal{N}_{\text{e}} , \mathcal{N}_{\text{c}} , \mathcal{N}_{\text{h}}$ can be written as $\mathcal{N}_{\text{e}} = \left\{n_{1} , n_{5}\right\}$, $\mathcal{N}_{\text{c}} = \left\{n_{3} , n_{6}\right\}$, $\mathcal{N}_{\text{h}} = \left\{n_{2} , n_{4}\right\}$, as shown in. The preset settings for the geometrical structure design for the sky highway include: (i) the width and height of the airway $r_{\text{aw}} = 40 \text{m}$, $r_{\text{aib}} = 15 \text{m}$, $h_{i , \text{aw}} = 20 \text{m}$, (ii) the design parameters of the two connected intersections { *n* <sub>3</sub>, *n* <sub>6</sub> } are the intersection radii 82.5m and 81.67m, respectively, which satisfy *connected intersection Design Requirements 1 and 2* by the constraint, and (iii) the design parameters of the two hub intersections are all set as $h_{\text{r}} = 20 \text{m}$, $r_{1} = 80.2756 \text{m}$, $r_{3 , \text{in}} = 95 \text{m}$, $\theta_{1} = 0.6354 \text{rad}$, $\theta_{3} = \frac{\pi}{8}$ while satisfying *Roundabout Intersection Design Requirements 1-5* by the constraints –. The aircraft’s trips are generated from the origin *n* <sub>1</sub> to the destination *n* <sub>5</sub> with the inflow shown in (b) during 20 minutes, where warm-up and cool-down processes are considered. According to the defined scenario, each aircraft can choose one of the following two routes: $R_{\text{a}} = \left\{n_{1} , n_{2} , n_{3} , n_{4} , n_{5}\right\}$ and $R_{\text{b}} = \left\{n_{1} , n_{2} , n_{6} , n_{4} , n_{5}\right\}$, while *R* <sub>b</sub> is shorter than *R* <sub>a</sub>.

![Fig. 26 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr26.jpg)

Download: Download high-res image (455KB)

From the perspective of a centralized system, the objective here is to minimize the total travel time defined as the sum of the time spent for all aircraft. Three simple different routing policies are applied separately for comparison, as shown in the following:
- 1.
	*Policy 1 (no routing)*: Each aircraft chooses the shorter route *R* <sub>b</sub> without feedback from real-time traffic characteristics.
- 2.
	*Policy 2 (random routing)*: Each aircraft randomly chooses one route without feedback from real-time traffic characteristics.
- 3.
	*Policy 3 (bang-bang routing)*: Each aircraft predicts the expected time spent for both routes using the real-time average speed for each element, then chooses the route with the shorter expected time spent.

The total time spent (TTS), total traveling distance (TTD) and their reduction rate relative to *Policy 1* are shown in, demonstrating that bang-bang routing achieves superior efficiency among the three evaluated policies. It can be intuitively observed from the results that the optimization of TTS and TTD may be contradictory in routing policies. For instance, while Policy 3 achieves the highest reduction in TTS, it also leads to a significant increase in TTD. This indicates a potential trade-off between time efficiency and energy efficiency in route planning. Therefore, in practical applications, routing policies should be carefully designed and parameterized to achieve a desired balance between these competing objectives based on specific operational requirements. Furthermore, if physical parameters of the aircraft (e.g., wingspan, weight, parasite area, propulsion efficiency) are determined, the total energy consumption could be directly modeled and optimized (), providing a more comprehensive basis for routing policy evaluation and selection. While this result aligns with intuitive expectations, we deliberately present this comparison to underscore the criticality of our methodological framework: (i) it enables precise quantification of performance differentials through traffic characteristics, and (ii) it can be used for more advanced enhanced routing policies in future work. This finding further substantiates that the proposed sky highway structure exhibits notable extensible utility for centralized routing policies. More advanced routing policies, such as the recent approach proposed in, could be further investigated and adapted for future sky highway structure research.

Table 5. Total time spent (TTS) and total traveling distance (TTD) on different routing policies and the reduction relative to Policy 1 (no routing).

| Routing policy | TTS (s) | TTD (m) | TTS reduction | TTD reduction |
| --- | --- | --- | --- | --- |
| Policy 1 (no routing) | 1.7409 × 10 <sup>5</sup> | 2.4162 × 10 <sup>6</sup> | 0 | 0% |
| Policy 2 (random routing) | 1.7077 × 10 <sup>5</sup> | 2.6998 × 10 <sup>6</sup> | 1.91% | \-11.7% |
| Policy 3 (bang-bang routing) | 1.7018 × 10 <sup>5</sup> | 2.8849 × 10 <sup>6</sup> | 2.25% | \-19.4% |

## 6\. Conclusion

This paper proposes a sky highway structure– a designed, layer-based structured airspace– to accommodate a large volume of low-altitude aircraft. The geometrical structure of the sky highway includes the layout of airways and intersections, designed to meet relevant safety requirements. Additionally, specific flight modes, such as virtual tube mode, arc road mode, 3-D roundabout mode, and FIFO mode, are proposed for the airways, connected intersections, hub intersections, and boundary intersections, respectively. Finally, a hybrid centralized and distributed control protocol is proposed for the sky highway, addressing collision avoidance at the microscopic level and traffic scheduling at the macroscopic level, aiming to balance safety and efficiency. The effectiveness of the proposed sky highway is demonstrated.

## Acknowledgments

This work was supported in part by the National Key Research and Development Program of China under Grant, and the National Natural Science Foundation of China under Grant, Grant.

## CRediT authorship contribution statement

**Rao Fu:** Writing – review & editing, Writing – original draft, Visualization, Validation, Methodology, Investigation, Conceptualization. **Yazan Safadi:** Writing – review & editing, Writing – original draft, Visualization, Validation, Methodology, Investigation, Conceptualization. **Quan Quan:** Writing – review & editing, Writing – original draft, Visualization, Validation, Methodology, Investigation, Conceptualization. **Jack Haddad:** Writing – review & editing, Writing – original draft, Visualization, Validation, Methodology, Investigation, Conceptualization.

## Appendix A. Appendix

### A1. Proof of

![Fig. A1 dummy alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X26000197-gr27.jpg)

Download: Download high-res image (239KB)

First, $r_{i , j_{2}} > d_{3}$ is the sufficient condition of, and the proof can be derived directly from; in other words, if $r_{i , j_{2}} > d_{3}$, then *Connected Intersection Design Requirement 1* holds. Furthermore, as shown in, on the middle horizontal plane containing the three points $\mathbf{p}_{i , j_{1}}$, $\mathbf{p}_{i , j_{2}}$ and $\mathbf{p}_{i , j_{3}}$, we have the following relationships $\begin{aligned}\left(\mathcal{A}_{i , j_{1} j_{2}} \cup \mathcal{A}_{i , j_{2} j_{1}}\right) \cap \mathcal{I}_{i , j_{2} , \text{az}} & = \left\{\mathbf{p}_{i , j_{1} j_{2} , \text{l}} , \mathbf{p}_{i , j_{1} j_{2} , \text{r}}\right\}\end{aligned}$ where the points $\mathbf{p}_{i , j_{1} j_{2} , \text{l}} , \mathbf{p}_{i , j_{1} j_{2} , \text{r}}$ are located at the left side and right side of $\overset{\rightarrow}{\mathbf{p}_{i , j_{1}} \mathbf{p}_{i , j_{2}}}$, respectively. Similarly, we have $\left(\mathcal{A}_{i , j_{2} j_{3}} \cup \mathcal{A}_{i , j_{3} j_{2}}\right) \cap \mathcal{I}_{i , j_{2} , \text{az}} = \left\{\mathbf{p}_{i , j_{2} j_{3} , \text{l}} , \mathbf{p}_{i , j_{2} j_{3} , \text{r}}\right\} .$Obviously, the center of concentric arc airways $\mathbf{o}_{i , j_{2}}$ is the intersection of two lines $\overset{\overline}{\mathbf{p}_{i , j_{1} j_{2} , \text{l}} \mathbf{p}_{i , j_{1} j_{2} , \text{r}}}$ and $\overset{\overline}{\mathbf{p}_{i , j_{2} j_{3} , \text{l}} \mathbf{p}_{i , j_{2} j_{3} , \text{r}}}$. Then *connected intersection Design Requirements 2* can be written as(A.1) $min \left(\left\|\mathbf{o}_{i , j_{2}} - \mathbf{p}_{i , j_{1} j_{2} , \text{l}}\right\| , \left\|\mathbf{o}_{i , j_{2}} - \mathbf{p}_{i , j_{1} j_{2} , \text{r}}\right\|\right) > r_{\text{turn}} .$Without loss of generality, we suppose that $\left\|\mathbf{o}_{i , j_{2}} - \mathbf{p}_{i , j_{1} j_{2} , \text{r}}\right\| < \left\|\mathbf{o}_{i , j_{2}} - \mathbf{p}_{i , j_{1} j_{2} , \text{l}}\right\|$, which is consistent with the condition in. Through geometrical relations, we have(A.2) $tan \frac{\theta_{i , j_{2}}}{2} = \frac{r_{i , \text{aw}} + 2 \left\|\mathbf{o}_{i , j_{2}} - \mathbf{p}_{i , j_{1} j_{2} , \text{r}}\right\|}{\sqrt{4 r_{i , j_{2}}^{2} - r_{i , \text{aw}}^{2}}} .$By, can be written as $r_{i , j_{2}} > \frac{1}{2} \sqrt{\left(\frac{r_{i , \text{aw}} + 2 r_{\text{turn}}}{tan \frac{\theta_{i , j_{2}}}{2}}\right)^{2} + r_{i , \text{aw}}^{2}} = d_{4}$ which indicates that is the sufficient condition of *Connected Intersection Design Requirement 2*. This completes the proof.

## Data availability

No data was used for the research described in the article.

## References

The classification of heterogeneous aircraft can be determined by different attributes, such as speeds, maneuverabilities, or applications.

The terms ‘safety area’ and ‘safety radius’ both denote a spatial zone where aircraft proximity poses potential safety risks, rather than representing an area of guaranteed safety. Similar to the aviation concept of ’safe separation,’ which mandates intervention when aircraft enter this area, it signifies that separation thresholds have been breached, and an emergency maneuver should be activated to restore safe separation. More details can be found in reference ().

This restriction is imposed to align with fundamental aerodynamic constraints and operational safety principles of both multicopter and fixed-wing aircraft. By decoupling azimuth and altitude maneuvers, aircraft can significantly reduce the risk of unintended altitude loss, stall, or loss of control caused by dynamic coupling and control interference in low-altitude environments. While it may marginally reduce the theoretical throughput of the airspace, it substantially increases operational safety and robustness, which is critical for UAM.

The structure of different nodes will be introduced in the following.

In both 2-D and 3-D roundabout configurations, aircraft navigate the along predefined route without right-of-way management. Coordination is achieved in a fully decentralized manner where each aircraft uses local sensing and distributed control algorithms to maintain safe separation, with no explicit or implicit priority assigned to any aircraft (). This approach eliminates the need for right-of-way management or rule-based yielding, ensuring autonomous distributed conflict resolution for all aircraft within the roundabout.

The word “tangible airway” means that this airway is a designed airway in sky highway structure, which is to distinguish from the following “virtual vertical airway.”

The three different structures for skylines, named sky-lanes, sky-tubes, and sky-corridors, are investigated in. Specifically, aircraft in sky-lanes should obey the restrictions (i) by following a fixed direction and (ii) by tracking a fixed center line. By comparison, aircraft in the sky-tubes should only obey the restriction (i), and aircraft flying in sky-corridors have no restriction.

The temporary ramp is temporarily constructed for emergency purposes. The location of the temporary ramp is not fixed and is determined based on the current position where the UAV needs to enter or exit the airway. It can be created or canceled at any time.

[^1]

The airspace utilization area means the 3-D space occupied by aircraft movements.

This indicates that only the cruising conflicts among aircraft will happen; in other words, the scenario is simplified as the 2-D case.

The initially conflict-free with airway’s boundary implies that the initial position of each aircraft is limited to a segment whose boundary intersections are more than *r* <sub>a</sub> from the airway’s boundary. Under the most extreme case that the airway’s width is 2 *r* <sub>a</sub>, this segment will degenerate into a fixed point.

The conflict between each pair of aircraft will not be calculated repeatedly, no matter how long the conflict resolution process takes.

It is worth pointing out that this conflict count model is less valuable under the proposed airway structure, because one aircraft can be in continuous conflict with another aircraft directly in front. Nevertheless, the result is still valid in indicating the possibility of conflicts under different structures at the hub intersection; in other words, the extra conflicts count in the airways are approximately the same.

[View Abstract](https://www.sciencedirect.com/science/article/abs/pii/S0968090X26000197)

[^1]: In the first simulation scenario, the influence of the designed airway’s width is investigated. Intuitively, a wider airway implies (i) a greater allowable traffic inflow, (ii) fewer conflicts among aircraft compared to narrower airways when the flow is fixed, and (iii) a larger airspace utilization area of the airspace. This suggests that there are irreconcilable internal contradictions among safety, efficiency, and airspace occupancy. For these reasons, it is necessary to find the optimal airway width design to achieve a tradeoff among such contradictions. Without loss of generality, a single horizontal airway with a fixed length of 200m, a fixed height of 20m, and a maximum allowed inflow $Q_{i n} = 1 \text{aircraft}/\text{s}$ is considered. This implies that the minimum airway width is 2 *r* <sub>a</sub>. Each aircraft’s maximum velocity is uniformly distributed within the range \[6, 10\]m/s. Another obvious conclusion is that overtaking is only allowed when the airway’s width is larger than $3 r_{\text{a}} + r_{\text{s}}$. In this scenario, the case where the airway’s width progressively increases at intervals of $2 r_{\text{a}} = 6 \text{m}$ is considered, while each aircraft with a fixed altitude will enter the airway at a random position, which is conflict-free with the airway’s boundary located at the origin plane of the airway. To investigate the effect of inflow on results, two cases are simulated: (i) $Q_{i n} = 0.5 \text{aircraft}/\text{s}$ and (ii) $Q_{i n} = 1 \text{aircraft}/\text{s}$. The simulation results include (i) the average outflow *G* (*t*) of the airway, (ii) the average speed *U* (*t*) of the aircraft, and (iii) the number of conflicts among aircraft, which are shown in and. The simulation results provide the following insights:
- •
	The average speed of aircraft increases and the number of conflicts decreases with the greater airway width, which is consistent with intuition. Conversely, the outflow does not show significant changes corresponding to the varying widths when overtaking is allowed (i.e., the width is greater than $3 r_{\text{a}} + r_{\text{s}} = 11 \text{m}$).
- •
	With the inflow 0.5 aircraft/s, the average speed increases uniformly when the width grows from 2 *r* <sub>a</sub> to 10 *r* <sub>a</sub> and becomes steadily when the airway width is greater than 10 *r* <sub>a</sub>. When the inflow increases to 1 aircraft/s, the width that stabilizes the average speed becomes greater at 14 *r* <sub>a</sub>. This implies the best-designed airway width from the perspective of traffic efficiency.
- •
	The number of conflicts keeps decreasing uniformly with the greater airway width. Therefore, from the perspective of safety, the traffic manager should determine the allowable level of conflicts per unit time first, and then design the minimum airway width to save airspace as much as possible.

Table 1. Traffic characteristics for a single airway with a simulation time step 0.1s, an inflow 0.5 aircraft/s, various widths ranging from $2 r_{\text{a}} = 6 \text{m}$ to $12 r_{\text{a}} = 36 \text{m}$, including outflow, average speed, and the number of conflicts. Note that the number of conflicts is not meaningful when the airway’s width is 2 *r* <sub>a</sub>, as overtaking is not allowed.

| Traffic characteristics Airway’s width (m) | 2 *r* <sub>a</sub> | 4 *r* <sub>a</sub> | 6 *r* <sub>a</sub> | 8 *r* <sub>a</sub> | 10 *r* <sub>a</sub> | 12 *r* <sub>a</sub> |
| --- | --- | --- | --- | --- | --- | --- |
| Outflow (aircraft/s) | 0.39 | 0.41 | 0.42 | 0.41 | 0.42 | 0.42 |
| Average speed (m/s) | 6 | 7.29 | 7.65 | 7.69 | 7.98 | 7.96 |
| Number of conflicts | 0 | 121 | 107 | 101 | 99 | 87 |

Table 2. Traffic characteristics for a single airway with a simulation time step 0.1s, an inflow 1 aircraft/s, various widths ranging from $2 r_{\text{a}} = 6 \text{m}$ to $14 r_{\text{a}} = 42 \text{m}$, including outflow, average speed, and the number of conflicts.

| Traffic characteristics Airway’s width (m) | 2 *r* <sub>a</sub> | 4 *r* <sub>a</sub> | 6 *r* <sub>a</sub> | 8 *r* <sub>a</sub> | 10 *r* <sub>a</sub> | 12 *r* <sub>a</sub> | 14 *r* <sub>a</sub> | 16 *r* <sub>a</sub> |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Outflow (aircraft/s) | 0.77 | 0.80 | 0.83 | 0.83 | 0.82 | 0.82 | 0.83 | 0.84 |
| Average speed (m/s) | 6 | 7.28 | 7.48 | 7.56 | 7.66 | 7.73 | 7.83 | 7.79 |
| Number of conflicts | 0 | 469 | 464 | 443 | 439 | 429 | 408 | 353 |

[^2]: Table 2. Traffic characteristics for a single airway with a simulation time step 0.1s, an inflow 1 aircraft/s, various widths ranging from $2 r_{\text{a}} = 6 \text{m}$ to $14 r_{\text{a}} = 42 \text{m}$, including outflow, average speed, and the number of conflicts.

| Traffic characteristics Airway’s width (m) | 2 *r* <sub>a</sub> | 4 *r* <sub>a</sub> | 6 *r* <sub>a</sub> | 8 *r* <sub>a</sub> | 10 *r* <sub>a</sub> | 12 *r* <sub>a</sub> | 14 *r* <sub>a</sub> | 16 *r* <sub>a</sub> |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Outflow (aircraft/s) | 0.77 | 0.80 | 0.83 | 0.83 | 0.82 | 0.82 | 0.83 | 0.84 |
| Average speed (m/s) | 6 | 7.28 | 7.48 | 7.56 | 7.66 | 7.73 | 7.83 | 7.79 |
| Number of conflicts | 0 | 469 | 464 | 443 | 439 | 429 | 408 | 353 |