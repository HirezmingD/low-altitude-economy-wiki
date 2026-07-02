---
title: "Centralized and distributed optimization of advanced air mobility strategic traffic management"
source: "https://cdnsciencepub.com/doi/full/10.1139/dsa-2025-0020"
author:
published:
created: 2026-07-01
description: "Effective traffic management for advanced air mobility (AAM) operations in low-altitude urban airspace is crucial for safety and scalability. Our study aims to bridge a critical gap in AAM traffic ..."
tags:
  - "clippings"
---
## Abstract

Effective traffic management for advanced air mobility (AAM) operations in low-altitude urban airspace is crucial for safety and scalability. Our study aims to bridge a critical gap in AAM traffic management by minimizing travel delays in both centralized and distributed providers of services for urban air mobility (PSU) settings. Key contributions include methods to (1) sectorize urban airspace for effective AAM management, (2) centrally plan AAM routes considering limited capacities in corridors and vertiports, and (3) manage airspace in distributed PSU settings while considering traffic flow capacities and interactions among PSUs. Specifically, the research combines community detection algorithms with Voronoi diagrams to sectorize individual PSU airspace. Corridor route planning is performed with a custom-weighted Dijkstra’s algorithm. Centralized AAM traffic flow management adopts mixed-integer programming (MIP) to minimize overall network delay costs. Distributed PSU network management is formulated as bi-level optimization using cooperative game theory and MIP, where individual PSUs update their strategies based on game theory outcomes. The simulation environment features a randomized no-fly zone, population density maps, and vertiport capacities assigned to artificial cities. Three vehicle configurations with varying ranges and adjustable speeds (i.e., minimum to cruise speeds) are simulated under three service priorities in Monte Carlo simulations. AAM flight operations are evaluated by optimization cost and runtime. This research provides a technical framework and insights into the comparison of centralized and distributed AAM network managements. The paper will facilitate informed decision-making in the development and implementation of AAM traffic management strategies.

## 1\. Introduction

The growth of advanced air mobility (AAM) as an urban and regional transportation mode raises the need for efficient air traffic management (ATM) ([^29]; [^26]; [^49]; FAA 2023 [^18]). Therefore, various concepts of operations (ConOps) and architectures have been proposed for unmanned aircraft systems (UAS)/AAM traffic management ([^44]; [^8]; [^53]; FAA 2023 [^17], 2023 [^18]). [Figure 1](#f1) illustrates FAA’s envisioned urban air mobility transportation system ([^19]) and the roles of each stakeholder. However, to our knowledge, no research has investigated a holistic approach to efficiently manage low-altitude AAM urban airspace, considering local traffic constraints in flight corridors, vertiport capacities, vehicle types, service priorities, and equity. This research aims to fill this gap by strategically optimizing AAM traffic management in both centralized and distributed providers of services for urban air mobility (PSU) settings.

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_f1.jpg)

Fig. 1. Envisioned urban air mobility (UAM) architecture with providers of services for urban air mobility (PSU) network.

It is worth noting that AAM traffic management shares some architectural principles with UAS traffic management, but differs in terms of operational complexity, safety requirements, and vehicle performance characteristics. Our proposed distributed AAM traffic management framework is particularly designed with passenger-carrying vehicles (i.e., air taxis) in mind. The system incorporates a negotiation-based distributed optimization process that reflects time-varying demands across residential and commercial regions. That said, the algorithm can be adapted to other AAM vehicles, such as delivery drones, by appropriately adjusting service priorities. The system generates optimized vehicle departure times and time-varying speeds along planned trajectories with fairness considerations.

Our research addresses three key questions to holistically answer how the PSU system can be designed in response to fundamental airspace constraints, such as finite capacity and the efficient use of spatial and temporal resources:

- *Airspace sectorization*: How should urban airspace be divided so that neighboring PSUs can handle AAM effectively? Or when a single PSU manages a large airspace with numerous vehicles, how should that airspace be structured to facilitate optimal air traffic solutions quickly?
- *AAM route planning*: How can we efficiently plan AAM routes and schedules considering limited capacities in both airspace and vertiports, along with varying vehicle types and service priorities?
- *Distributed management*: How can we minimize the time needed to generate optimized traffic management schedules for a large number of AAM vehicles managed by each/multiple PSU(s)?

It is important to understand that our research addresses fundamental questions in AAM traffic management, taking into account various constraints. In particular, both the need for airspace sectorization in AAM operations and the identification of responsible entities for managing aircraft within sectorized airspace and performing traffic optimization remain open and evolving questions. The precise role of PSU is also evolving; multiple PSUs may manage a large number of AAM vehicles in the same area, or each PSU may govern specific airspace regions. Our research offers distributed AAM traffic management solutions adaptable to both scenarios, employing a cooperative game theoretic approach to coordinate AAM traffic management. In this context, we define the PSU’s role as providing critical data (i.e., terrain and weather services), segmenting airspace, and strategically planning AAM flight routes ([^8]) with the following criteria/goals:

- Each PSU manages multiple vertiports and computes distinct air traffic flow management (ATFM) capacity limits based on factors like vertiport size and public concerns.
- PSU must ensure strategic conflict-free operations, spatially or temporally, for all AAM flights.
- To ensure safe AAM operations, especially during the early stages of low-level automation and deployment ([^13]; [^25]; [^23]), PSUs aim to allocate optimized flight corridor routes, minimizing travel time while considering its airspace, vertiport capacities, and vehicle service priorities.
- PSUs aim to ensure equitable allocation of departure time for each AAM vehicle, considering factors such as operational service priorities and vehicle characteristics (i.e., min and cruise speeds and range).

In the simulation, we categorize AAM vehicles into three configurations: multicopter, vectored thrust, and lift-and-cruise, representing the most common designs ([^12]; [^20]; [^27]). Then, each vehicle’s design-specific flight speeds and range are considered when solving AAM traffic solutions. Additionally, service priorities are classified into regular, express, and emergency services/medical (i.e., organ delivery) categories to accommodate various customer needs. For instance, medical centers and biotech companies aim to expedite organ transfers using AAM vehicles ([^1]). Simulations cover both centralized and distributed PSU systems in an artificially created map, testing scenarios with 150 and 300 vehicles in a Monte Carlo simulation. The proposed traffic management systems for both centralized and distributed environments are evaluated by their runtimes (i.e., scalability), objective costs, and average departure and airborne delays. This aims to compare different models and design safe, efficient, and scalable AAM traffic management.

## 2\. Literature review

The technical maturity of aviation technology is creating a new era of transportation. AAM services include various operations such as passenger transportation, package and medical delivery, humanitarian and rescue missions, surveillance, and ground data gathering, all within low-altitude airspace. However, ensuring the safe and efficient operation of AAM requires collaborative efforts among governments, industries, and academia to overcome many challenges ([^49]; [^33]; [^8]). In this literature review, our focus centers on the challenges of AAM traffic management, addressing the complexities of high-tempo, low-altitude, high-density AAM operations within the national airspace system (NAS) to ensure safe and efficient operations.

To start off, NASA has been conducting collaborative research to integrate AAM operations into the NAS. This involves investigating procedures and algorithmic tools to address the integration challenges of AAM air traffic operations. NASA’s high-level initial airspace integration concept, as well as its envisioned strategic and tactical management components, are outlined in [^49]. The main challenges in AAM traffic management include AAM congestion management, separation management, and vertiport take-off/landing capacity sizing ([^49]; [^52]; [^8]). Governments, research laboratories, and AAM companies released their ConOps, envisioning AAM operation through corridors ([^4]; [^21]; [^31]; [^7]; [^36]; [^45]; [^16]; [^8]). The FAA formally defines a corridor as “ *an airspace volume defining a three-dimensional route, potentially divided into multiple segments, with associated performance requirements* ” (FAA 2023) [^18]. FAA and NASA envision that AAM vehicles are cooperatively managed through a data-sharing environment within these corridors, governed by set rules, to support increasing operational tempo and new service demands (FAA 2023) [^18].

AAM traffic management comprises strategic and tactical components aimed at reducing congestion and ensuring collision-free routing, similar to traditional ATFM ([^38]; [^54]; [^2]). Recent research explores various algorithmic approaches. For example, in [^57], dynamic geofencing (i.e., trajectile geofence that moves along the trajectory) and linear programming were used to develop a pre-departure first-come, first-serve (FCFS) sequential conflict-free trajectory planning for AAM vehicles. Similarly, an FCFS vertiport scheduling algorithm was developed in [^22], considering the throughput and capacity of different vertiport configurations. In [^39], a graph reinforcement learning method for online schedule planning was introduced, addressing dynamic demand and uncertainties such as take-off delays and weather-induced route closures. In [^56], a message-based decentralized computational guidance algorithm is developed for providing tactical guidance commands, ensuring safe arrivals of AAM vehicles and avoiding line-of-sight events. The paper formulated a multi-agent Markov decision process for cooperative AAM vehicles in free-flight scenarios and solved using Monte Carlo tree search.

Previous strategic AAM traffic management research has typically focused on either local optimization aspects or very specific elements, often neglecting proposed ConOps and network architectures, as well as the ecosystem of services that will support traffic management ([^31]; [^52]; [^57]; [^12]; [^22]; [^40]; [^56]; [^20]; [^32]). Our work has developed AAM traffic management architectures aligned with ConOps proposed by government entities, research laboratories, and AAM companies. We adopt the corridor architecture for AAM flight operations and develop safe, efficient, and scalable AAM strategic traffic management. Furthermore, we formulate vehicle-type-aware and service-priority-aware traffic management systems that achieve optimal solutions while considering vertiport take-off/landing capacities, corridor throughput capacities, and equity. We explore both centralized and distributed PSU architectures (i.e., bi-level optimization incorporating cooperative game theory) to evaluate their scalability. Additionally, we compare distance-based route planning with weighted route planning in both centralized and distributed PSU settings.

## 3\. Methodologies and algorithmic approaches

### 3.1. Airspace sectorization for (distributed) PSU

The concept of airspace sectorization could play a critical role in AAM traffic management, similar to its traditional application in air traffic control. The airspace sectorization problem aims to divide airspace into manageable sectors, originally for controller workload balance and coordination reduction ([^50]). In the context of AAM traffic management, PSU takes over these tasks, yet sectorization remains vital. Effective airspace sectorization prevents overburdening individual PSUs, ensuring efficient traffic handling within each sector ([^40]).

Two PSU operational concepts illustrate the relevance of sectorization. The first involves multiple PSUs operating concurrently in the same region, akin to drivers choosing between different GPS navigation apps in the same area. In this scenario, airspace sectorization aids individual PSUs in managing large vehicle volumes by generating optimized traffic solutions through distributed systems. The second concept assigns distinct airspace regions to individual PSUs, requiring vehicles to transition between regions when traveling across multiple sectors, similar to current air traffic control systems. Proper airspace sectorization in this framework reduces coordination efforts between neighboring PSUs and sectors, ensuring seamless operations.

While some AAM companies may operate and manage their own vehicles, overall regional ATM would remain under the oversight of PSU(s). For example, vertiports shared among AAM companies must integrate capacity constraints into the broader traffic management framework. By grouping regions based on features such as vertiport capacity and population density, airspace sectorization enables PSUs to manage regional airspace effectively and provide optimal traffic management solutions. Additionally, regions with higher population densities require more detailed sectorization due to increased traffic and potential conflicts. Vertiport topology also influences sectorization, as facilities may vary in the number of touchdown and liftoff (TLOF) pads, gates, and parking spaces ([^52]; [^41]). Airspace sectorization should incorporate these parameters to prevent congestion within individual PSU jurisdictions.

In this paper, we develop a distributed AAM traffic management approach that accommodates both PSU concepts, leveraging airspace sectorization to generate optimized traffic solutions more efficiently for both scenarios. Our focus, however, is on the second concept, where individual PSUs govern their respective airspace and coordinate with neighboring PSUs to optimize overall traffic management. This scenario presents greater algorithmic complexity than the first concept, and we aim to provide a mathematical framework to address and solve this challenge.

While traditional airspace design may not directly apply to PSU airspace sectorization due to differing operational complexities and infrastructure, studying airspace sectorization methods enhances our understanding of designing sectorization for PSUs. The below [Table 1](#tab1) summarizes general airspace sectorization methods for conventional ATM ([^55]; [^30]; [^43]; [^40]) and their advantages and drawbacks.

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_tab1.gif)

Our PSU airspace sectorization is achieved by assessing similarities between pairs of vertiport areas. The airspace is then sectorized by identifying communities with shared conditions among vertiport pairs. The steps are as follows:

- Create initial connections between vertiport pairs, forming flight corridors that adhere to a minimum and maximum flight range threshold of corridor.
- Create an undirected, weighted graph. The weight is determined based on the normalized distance, connectivity (number of associated flight corridors per vertiport), likenesses in population density, and vertiport capacity.
- Utilize the Louvain method of community detection algorithm ([^11]) to identify non-overlapping communities (i.e., groups of nodes) within the spatially conflicted network.
- Implement Voronoi diagrams ([^5]) to generate the union of Voronoi cells associated with individual vertiports within the same community, constructing airspace sectors for each PSU.

The Louvain method for community detection is a heuristic algorithm that optimizes modularity score to find non-overlapping communities from large networks ([^11]). Modularity measures how well a network is divided into communities, with a higher score indicating a better division. A Voronoi diagram ([^5]) is a geometric method that divides a space into regions based on the distance to a given set of points. Each region consists of all the points closer to a particular input point than to any other point in the set.

The weight equation for the flight corridor network is shown in [eqs. 1 *a*](#eq1) – [1 *f*](#eq6). The weight factor of each parameter is represented as α <sub>1</sub>, α <sub>2</sub>, α <sub>3</sub>, and α <sub>4</sub>, respectively, where the sum of the weight factors equal 1. is the normalized distance between vertiports *u* and *v* (i.e., edge *i*). max (*d <sub>i</sub>*) is the maximum corridor length, where *d <sub>i</sub>* is the length of corridor *i*. *d* <sub><i>u</i>,<i>v</i></sub> is the distance between vertiport *u* and *v*. denotes the average connectivity between vertiport *u* and *v*, where *m <sub>i</sub>* is the vertiport *i* ’s connectivity, the number of corridors that are connected to vertiport *i*. max (*m* <sub>vertiport</sub>) denotes the maximum connectivity that occurs among the vertiports. stands for the population similarity score in edge *i*, and represents the vertiport capacity similarity score in edge *i*. *p <sub>u</sub>* and *p <sub>v</sub>* are population densities of the cities, where vertiport *u* and vertiport *v* are located. Similarly, *c <sub>u</sub>* and *c <sub>v</sub>* are vertiport *u* ’s and *v* ’s capacities. [Figure 2](#f2) visualizes PSU airspace sectorization.

(1a)

(1b)

(1c)

(1d)

(1e)

(1f)

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_f2.jpg)

Fig. 2. Illustration of providers of services for urban air mobility (PSU) airspace sectorization. Each small circle represents a vertiport. Solid gray edges represent the corridors, connecting pairs of vertiports. Black dashed lines indicate the PSU boundaries.

### 3.2. Corridor-based route planning

In our work, we adopt flight corridors for AAM route planning. This aligns with the ConOps proposed by government entities, research laboratories, and AAM companies ([^4]; [^21]; [^31]; [^7]; [^36]; [^45]; [^16]; [^46]; [^8]). The summarized ConOps are shown in [Fig. 3](#f3), noting corridors or a variation of corridors for airspace management.

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_f3.jpg)

Fig. 3. Advanced air mobility airspace design concepts of operations.

#### 3.2.1. Distance-based versus weighted path construction

Using the designed PSU and the criteria/goals outlined in [Section 1](#sec-1), AAM vehicles traverse flight corridors connecting departure and destination vertiports. Each corridor is designed to link adjacent vertiports, allowing AAM vehicles to pass through multiple intermediate corridors en route to their destination. This design provides contingency landing sites at vertiports along the route in case of an emergency. Through our optimization algorithm in later sections, we ensure that all vehicles are either spatially or temporally deconflicted, whether they pass through altitudes above the vertiports or land at the vertiport of interest.

The best corridor routes are determined using Dijkstra’s algorithm ([^42]), which finds the shortest corridor routes between departure and destination vertiports. In our work, we explore two different approaches to corridor-based route planning. The first method employs the typical distance-based Dijkstra algorithm to find the shortest route between each pair of departure and destination vertiports. The second approach utilizes corridor weights in [eqs. 1 *a*](#eq1) – [1 *f*](#eq6) to find the path that minimizes the total weights. The weighted path allows PSU to consider multiple factors to determine the optimal route while avoiding potentially congested regions in low-altitude urban airspace. By exploring an alternative route planning approach, we investigate whether distributed AAM traffic management can be further optimized, reducing overall flight delays in congested airspace. In [Section 5](#sec-5), the Monte Carlo simulation results are analyzed from the randomly generated AAM flight operations (i.e., 150 vehicles, 300 vehicles) in sectorized PSU regions. The drawbacks and advantages of using weighted path approach are also discussed.

[Figure 4](#f4) illustrates the two corridor route planning methods. Blue circles represent vertiports, each labeled with a vertiport ID. Gray lines depict corridors connecting pairs of vertiports. Gray boxes highlight potential congestion regions where vertiport connectivity (i.e., number of corridors connected at the vertiport), population density, and vertiport take-off/landing capacities are high. The distance-based (shortest distance) path and the weighted path are shown as red and black dashed lines, respectively. The weighted path finds the minimum-cost solution, avoiding potentially congested regions (i.e., high-weighted routes).

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_f4.jpg)

Fig. 4. Illustration of corridor-based route planning using distance-based and weighted methods.

#### 3.2.2. Corridor design and spatial conflict detection and resolution strategy

AAM vehicles traverse through corridors that connect vertiports. Two types of spatial conflicts can occur while AAM vehicles fly through corridors. The first type occurs within each corridor itself, which we model as a three-dimensional geofence with finite dimensions at a fixed altitude. Because corridors have finite volumes, the maximum number of vehicles that can traverse the corridor simultaneously is limited, leading to spatial conflicts if the capacity is exceeded. Our optimization model in [Section 3.3](#sec-3-3) considers each corridor’s maximum throughput capacity as a constraint and adjusts vehicle speeds to maintain safe separation distances between AAM vehicles.

The maximum throughput capacity *k <sub>i</sub>* of the directional corridor *i* is defined in [eq. 2](#eq7). *d <sub>s</sub>* is the minimum inter-vehicle separation distance (MIVSD) inside the corridor. *d <sub>i</sub>* is the length of the corridor *i*. *h <sub>i</sub>* is the number of vertical lanes that construct the directional corridor. For example, a corridor of length 50 km with MIVSD of 2 km and 3 vertical lanes has a maximum throughput capacity of 75 vehicles. In our work, we construct a three-vertical lane bi-directional corridor to connect each pair of vertiports, and MIVSD is set to 2 km. [Figure 5](#f5) illustrates the constructed corridor shape. This design offers the benefit of segregating AAM vehicles by their speeds, particularly advantageous as it facilitates a smooth transition of speed and altitude for AAM flights approaching to land at a destination vertiport or departing from a departure vertiport. However, it is important to note that our optimization method for solving AAM traffic management is not tied to a specific corridor structure. For instance, whether it is a three-vertical lane bi-directional corridor or a three-horizontal lane bi-directional corridor, the results remain the same.

(2)

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_f5.jpg)

Fig. 5. Visualization of multi-lane bi-directional corridor.

The second type of conflict arises when directional corridors spatially overlap. Such conflicts can occur in multiple scenarios. For example, when multiple corridors converge at a common vertiport or when corridors connecting different pairs of vertiports intersect, spatial conflict occurs. Note that we define a corridor to connect a pair of vertiports. If an AAM flight traverses through multiple vertiports, the flight path consists of multiple corridors in sequence. [Figure 6](#f6) illustrates seven types of spatial conflicts that can occur, with circled numbers indicating the locations of such conflicts in directional corridors. ① and ② cases denote conflicts when an AAM vehicle is taking off/landing (i.e., yellow flight path) while another AAM vehicle is passing through the corridor (i.e., green flight path) shared through a common vertiport. Case ③ occurs when AAM flights with different corridor paths cross each other at a shared vertiport (i.e., purple and green flight paths). Case ④ occurs when AAM flights with different corridor paths cross each other in mid-air (i.e., purple and yellow flight paths). ⑤ and ⑥ cases denote conflicts where AAM flights with different corridor paths share departure/destination vertiports and the connecting corridors (i.e., purple and yellow flight paths in the center figure). Lastly, case ⑦ is when an AAM corridor path is spatially conflicted with another AAM flight’s corridor path by sharing more than one vertiport inside (i.e., purple flight path in the rightmost figure).

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_f6.jpg)

Fig. 6. Visualization of corridor spatial conflict types.

Each pair of spatially conflicted AAM flight paths can be characterized by a tuple of two conflict types, one for each AAM flight path, from the seven types mentioned above. Once categorized, the next step involves deconflicting the AAM flights temporarily to ensure only one AAM flight passes through the spatially conflicted region at a time, avoiding simultaneous passage. This guarantees that AAM vehicles will not collide in the spatially shared corridor region. Three strategies are available for temporal conflict resolution: (1) delaying the departure time of the AAM flight, (2) adjusting the vehicle speed in the conflicted corridor region, and (3) implementing both options 1 and 2 sequentially. In strategic AAM traffic management, it is generally preferable to delay the departure time rather than adjust the vehicle speed, considering the energy cost. However, since each vertiport has limited take-off and landing pads, gates, and parking spaces, a system-wide AAM traffic management approach may require implementing all three options to resolve spatially conflicted flight pairs while maintaining scheduled departure and arrival times.

Next step towards temporal conflict resolution involves calculating the time at which each conflicted AAM flight enters and exits the conflicted region in corridors. This involves finding the boundary coordinates of the shared region and identifying the closest boundary coordinates to each AAM flight path. Orthogonal projection is then used to determine the point of entry and exit, and time at which each flight path enters/exits the shared region. This method is similar to the spatial conflict detection method employed in [^32]. Our method extends it by incorporating various spatial conflict types and comprehensive temporal conflict resolution strategies that adjust vehicle-specific speeds (and even based on the service priority of AAM vehicles).

[Figure 7](#f7) visualizes how spatially conflicted corridor region is detected and temporally deconflicted in each conflicted flight pair. On the left side of the figure, three flight paths with their trajectory geofences (i.e., purple, green, and yellow) are depicted. Spatially conflicted corridor regions are highlighted in red polygons. On the right side, a closer view of spatially conflicted corridors *i* and *j* for two conflicted flight paths *m* and *n* is shown. The purple plus sign indicates the location before a flight enters a conflicted region (i.e., *B* <sub><i>m</i>,<i>i</i></sub> and *B* <sub><i>n</i>,<i>j</i></sub>), The purple X sign indicates the location where a flight exits a conflicted region (i.e., *E* <sub><i>m</i>,<i>i</i></sub> and *E* <sub><i>n</i>,<i>j</i></sub>). Conflicted AAM vehicles are temporally deconflicted if one vehicle enters the conflicted region after the other vehicle exits, as follows (i.e., [eq. 3](#eq8)):

(3)

Here, *t <sub>s</sub>* is an additional safety separation time buffer, accounting for uncertainties arising from guidance, navigation, and control (GNC) errors and wind. [Section 3.3.1](#sec-3-3-1) outlines the formulation of the temporal conflict resolution as optimization constraints and explains the objective cost design for solving AAM traffic management.

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_f7.jpg)

Fig. 7. Visualization of spatial conflict regions between two flight paths ( m, n ) within corridors ( i, j ). B and E denote locations before and after a flight enters/exits a spatial conflict region.

### 3.3. AAM traffic flow management

Strategic AAM traffic flow management aims to minimize the total delay time of all flights within designated airspace using centralized/ distributed methods. Considering the criteria outlined in [Section 1](#sec-1), mixed-integer programming (MIP) ([^3]) is employed to solve the optimal solution. Our algorithm determines individual vehicle speeds along flight corridors while incorporating safety buffer times to account for uncertainties arising from GNC errors and wind. Additionally, it assigns departure times, which may differ from the originally scheduled times, to optimize overall traffic flow. The solution also resolves temporal conflicts in spatially conflicted flight paths. The key parameters and constraints for optimizing AAM traffic are outlined in [Table 2](#tab2) and [Fig. 8](#f8).

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_f8.jpg)

Fig. 8. Advanced air mobility traffic optimization constraints. Figures are adapted and modified from 51, 47, and 34.

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_tab2.gif)

#### 3.3.1. Centralized AAM traffic flow management

MIP equations and constraints are formulated to solve a large number of AAM flight operations within a centralized system. The constraints include take-off/landing vertiport capacities and AAM maximum throughput capacities in multi-lane bi-directional corridors. Additionally, our model accommodates AAM vehicle types (e.g., multicopter, vectored thrust, lift-and-cruise configurations) with their speeds and ranges. Each vehicle’s speed is bounded between minimum cruise to ideal cruise speed, which is specific to the vehicle type. Service priorities are also factored into the formulation, categorized as regular, express, and medical in order of higher priority. Decision variables and parameters for centralized AAM traffic management are given in [Table 3](#tab3).

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_tab3.gif)

The formulation of the MIP problem for centralized AAM traffic flow management is shown in [eqs. 4](#eq9) – [13](#eq20). The decision variable, , is based on the well-established ATFM model ([^9]), but modified for solving AAM traffic management in the PSU airspace environment. We define equals 1 if flight *f* arrives at corridor *k* by time *t*, and 0 otherwise. The objective function minimizes the total delay cost, which is the sum of airborne delay and departure delay of all AAM vehicles. The objective function is expressed as two times the total delay minus the departure delay, where the total delay is defined as the sum of the airborne delay and the departure delay, following the expression in [^10]. By expressing this way, we can include the ϵ term (i.e., the delay equity weight) as a super-linearity function in MIP objective cost. This ensures the optimization finds a solution that allows equitable allocation of departure time for each AAM vehicle. For our simulation, we assign ϵ to be 0.05. Lastly, the service priority *s <sub>f</sub>* and the cost ratio (γ) of airborne delay to departure delay of each AAM flight are multiplied to each delay term. The expressed objective function is formulated to fairly assign each vehicle’s departure time while considering vehicle-specific parameters and their service priorities.

(4)

subject to

(5a)

(5b)

(6)

(7a)

(7b)

(8)

(9)

(10)

(11)

(12)

(13)

Constraints are as follows: [Equations 5 *a*](#eq10) and [5 *b*](#eq11) are time-dependent take-off and landing capacity constraints at each vertiport *v*. [Equation 6](#eq12) is the corridor throughput capacity constraint, ensuring that the total number of flights traversing any flight corridor *k* does not exceed its capacity. [Equations 7 *a*](#eq13) and [7 *b*](#eq14) define the minimum and maximum traversal times for AAM vehicles through each flight corridor. This essentially adjusts the speed at which each vehicle flies through a specific corridor based on its vehicle type (i.e., multicopter, vectored thrust, lift-and-cruise). [Equations 8](#eq15) and [9](#eq16) collectively enforce the constraint that an AAM vehicle must be confined to a single flight corridor at any given time during its flight, ensuring its position remains unique. [Equation 10](#eq17) ensures that the assigned departure time for any flight must be greater than or equal to its scheduled departure time to avoid early departures.

[Equations 11](#eq18) and [12](#eq19) are temporal conflict resolution constraints that delay either one of two flights in spatially shared corridor regions. They are formulated using a big *M* term (i.e., a large positive constant) to express logical conditions in [eq. 3](#eq8). *B* <sub><i>m</i>,<i>i</i></sub> is the ratio of the conflict region’s start point within corridor *i* relative to its full length, for flight *m*. *E* <sub><i>m</i>,<i>i</i></sub> is the ratio of the conflict region’s end point within corridor *i* relative to its full length, for flight *m*. *B* <sub><i>n</i>,<i>j</i></sub> and *E* <sub><i>n</i>,<i>j</i></sub> follow the same definition, with *n* and *j* replacing *m* and *i*, respectively. Additional safety separation time (*t <sub>s</sub>*) is added to deconflict spatially conflicted flight pairs. [Equation 13](#eq20) ensures that conflicted flights exit the spatially shared corridor region in order. The binary decision variables, and *x <sub>c</sub>*, follow the definition by [^32]. and *x <sub>c</sub>* cannot be 1 simultaneously. Essentially, [eqs. 11](#eq18) – [13](#eq20) enforce the condition expressed in [eq. 3](#eq8).

In a distributed AAM traffic flow management below (i.e., [Section 3.3.2](#sec-3-3-2)), each PSU applies slightly modified optimization with additional constraints, and cooperative game theory is used to facilitate fair and coordinated negotiation of AAM traffic among conflicting PSUs. The formulation shows how PSU connectivity and PSU’s negotiable bargain power influence overall AAM traffic management.

#### 3.3.2. Distributed AAM traffic flow management

As AAM operation grows both in terms of the number of vehicles and the operational regions, the AAM traffic management system requires a distributed model. This is similar to the evolution of conventional ATM from centralized to distributed networks. The present aviation traffic management operates within a complex network, incorporating various entities such as the FAA, ICAO, flight operations centers, and traffic management units at en route centers ([^48]). The traffic management is distributed across manageable units, with redundancies to enhance safety. Whether human operators play an active role in AAM traffic management or not, distributed PSU traffic management will be crucial for efficiently handling low-altitude, densely populated local air traffic. A significant advantage of distributed PSU traffic management lies in its scalability. If multiple PSUs manage a large number of AAM vehicles within the same geographical area, the distributed architecture allows each PSU to quickly generate solutions for a large number of AAM vehicles by locally optimizing traffic solutions. Alternatively, if each PSU governs a designated airspace region, the distributed architecture enables coordinating/resolving conflicts only for vehicles transitioning through multiple PSUs. The results presented in [Section 5](#sec-5) show that the coordinated AAM traffic management solution within individual PSUs can be generated between 1.4 and 30 times faster compared to the time required for centralized management to generate a global solution. With an increase in the number of AAM flight operations, the complexity of the AAM network also rises. Therefore, significantly enhanced scalability of AAM traffic management can be obtained through the distributed system. Refer to [Fig. 1](#f1) for the FAA’s envisioned AAM architecture involving multiple stakeholders and complexity of the network.

As mentioned in [Section 1](#sec-1), we focus on the scenario where each PSU governs a designated airspace. Initially, our centralized AAM traffic management model appears to be scaled for individual PSUs. However, within this framework, each PSU independently manages local air traffic within its designated region. Without coordinated communication and agreements among neighboring PSUs, optimal AAM operation schedules of one PSU may negatively affect adjacent PSUs. This occurs because each PSU independently optimizes its airspace management, potentially leading to one PSU expediting the outflow of many AAM vehicles through other PSU regions to minimize its airspace traffic density. Consequently, adjacent PSUs may experience traffic congestion due to the large inflow of AAM vehicles into their regions. To minimize such congestion and ensure fairness across neighboring PSUs, a coordinated system is crucial with optimized corridor usage and airspace efficiency. Ultimately, PSUs will need to collaborate and coordinate their traffic management solutions to achieve a harmonized and efficient global AAM traffic management system.

To address this challenge, we introduce a collaborative decision-making model among PSUs, leveraging a bi-level optimization approach. The lower-level optimization involves each PSU independently optimizing its AAM traffic management using MIP. Then, the upper-level optimization employs cooperative Nash bargaining game theory ([^37]; [^35]) to resolve conflicts among the game players (i.e., conflicting PSUs). This cooperative bargaining phase allows negotiation and agreement among conflicted pairs of PSUs to achieve a fair and cooperative agreement on vehicles transitioning between PSU regions. This is done by comparing each PSU’s negotiable bargaining power at each operation to reach stability (i.e., Nash bargaining solution). As previously mentioned, our distributed traffic management architecture is adaptable to a scenario where multiple PSUs manage a large number of AAM vehicles in the same area. This is achieved by independently sectorizing each PSU’s AAM fleet management without dependency on others. [Table 4](#tab4) and [Fig. 9](#f9) show the key parameters, objective function, and flow diagram of bi-level optimization for distributed AAM traffic management.

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_f9.jpg)

Fig. 9. Distributed advanced air mobility (AAM) traffic management flowchart. PSU, providers of services for urban air mobility; MIP, mixed-integer programming.

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_tab4.gif)

In addition to the variables listed in [Table 3](#tab3), we define additional decision variables and parameters for distributed AAM traffic management, outlined in [Table 5](#tab5). The PSU cooperative Nash bargain equations are shown in [eqs. 14](#eq21) – [15 *b*](#eq23) below. *U* <sub>1</sub> and *U* <sub>2</sub> are transition time equity functions (i.e., utility functions) that show how much each PSU feels about individual AAM’s negotiated time of entry/exit in its airspace region. The decision variable represents the payoff of AAM flight *f* traveling through conflicted PSUs *i* and *j*, with its value ranging between 0 and 1. The decision variable is a payoff of AAM flight *f* entering/exiting PSU *i*, and its value ranges between 0 and 1. The equation below essentially determines the payoff.

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_tab5.gif)

(14)

(15a)

(15b)

Here, *n <sub>i</sub>* is the negotiable bargain power of PSU *i* during flight operation time window , expressed as [eqs. 16 *a*](#eq24) and [16 *b*](#eq25). The equation comprises three parameters, each multiplied with weight factors (i.e., β <sub>1</sub>, β <sub>2</sub>, and β <sub>3</sub>). These weight factors collectively sum up to 1. Each parameter represents AAM density in PSU *i*, the total number of transition corridors (i.e., corridors connecting to adjacent PSUs), and the total number of spatially conflicted flight paths inside the PSU *i*.

(16a)

(16b)

It is crucial to recognize that the negotiable bargaining power of PSUs varies with each operational time window . For instance, during morning hours when AAM is heavily utilized for commuting from residential to commercial PSU areas, there is significant inbound traffic from residential to commercial PSU sectors. Conversely, during the evening rush when people return home from work, there is a surge in outbound traffic from commercial to residential areas. This fluctuation in PSU bargaining power mirrors the demand dynamics within each PSU’s operational time window. This establishes a cooperative negotiation framework among PSUs, ensuring that no single PSU maintains a permanent advantage over others. Instead, bargaining power equitably reflects demand, conflict complexity, and the strength of connectivity between adjacent PSUs.

Now, the process of calculating the actual bargained entry/exit transition time *b* <sub><i>f</i>,<i>i</i></sub> for each AAM flight *f* in PSU *i* is shown in Algorithm 1. Note that represents the time difference between an AAM flight *f* ’s optimal departure from PSU *i* and its optimal arrival at adjacent PSU *j*, where PSUs *i* and *j* are in conflict.

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_ufig2.jpg)

A new constraint is introduced after cooperative negotiations among conflicting PSU pairs. This constraint pertains to each flight’s coordinated entry/exit time in shared corridors between conflicted PSU pairs. Furthermore, to make bi-level optimization feasible, the objective function is modified in distributed AAM traffic management, and the constraint from [eq. 10](#eq17) is relaxed. If a feasible solution cannot be found, the modified optimization and relaxed constraint may choose to depart the AAM flight earlier than the desired departure time to coordinate flights passing through multiple PSUs. Here, we anticipate that each AAM operator would file their desired departure times in advance (i.e., several hours or even days ahead), similar to how airlines schedule departures. This supports system-level optimization and enables proactive coordination across PSUs while respecting vehicle performance limits. This earlier departure than the AAM operator’s desired time occurs when the vehicle cannot accelerate beyond its ideal cruise speed to meet the coordinated entry/exit time. The objective function penalizes these early departures more heavily to minimize their occurrence.

We envision that strategic AAM scheduling by PSUs will require AAM operators to file their desired flight departure times in advance, based on each operator’s preferred operating hours and location. Since multiple AAM operators will share the airspace, and regular commuting by AAM will likely follow fixed schedules (similar to how buses operate), advance planning is essential. For example, each PSU may ask AAM operators to submit their desired vehicle departure times 12 h in advance. The distributed AAM traffic management algorithm will then generate an optimal solution, which may result in a departure time that is slightly earlier (1–5 min) than the operator’s preferred time. The algorithm can bound the maximum allowable early departure, with our simulation setting this maximum at 5 min. The optimization algorithm heavily penalizes early departures, even though this is part of strategic AAM traffic management, and such adjustments should not significantly disrupt the operators’ preferred schedules. Our distributed AAM traffic management’s modified objective function and new constraint are shown in [eqs. 17](#eq26) and [18](#eq27). Algorithm 2 shows bi-level optimization for distributed AAM traffic management.

(17)

subject to additional constraint:

(18)

The bi-level optimization yields sub-optimal solutions compared to the centralized MIP approach, as each conflicted PSU pair coordinates its solutions to resolve conflicts. Nonetheless, the objective cost for each PSU will be lower than that of centralized AAM traffic management, as each PSU manages fewer vehicles than the centralized system. Additionally, the computation time for finding solutions will also be reduced in each PSU. [Section 5](#sec-5) provides a more detailed examination of objective costs and runtime.

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_ufig3.jpg)

## 4\. Simulation setup

Monte Carlo simulation was used to introduce variability in operational scenarios by assigning random seeds to generate different combinations of origin–destination pairs, desired speeds, and departure/arrival times for each vehicle. Vehicle types were also randomly assigned based on predefined ratios. We tested four scenarios: (1) 150 AAM flights with distance-based corridor routing, (2) 150 AAM flights with weighted corridor routing, (3) 300 AAM flights with distance-based routing, and (4) 300 AAM flights with weighted routing. Each scenario was simulated 150 times to compute statistics (i.e., mean and standard deviation) for metrics such as delay percentage, average delay by vehicle and service priority types, runtime, and objective cost for both centralized and distributed systems. Then, the simulation is tested using an artificially created map. Population density is randomly assigned to each town/city, and vertiports are constructed to reflect AAM demand ([^24]). No-fly zone with keep-out geofence is constructed. The maximum distance of a single flight corridor is limited to 60 km, matching the minimum AAM operational range (i.e., multicopter range). The parameters for constructing the artificial map and AAM flight operations are summarized in [Table 6](#tab6). Here, vehicle types 1, 2, and 3 correspond to Volocity (i.e., multicopter), Joby Aviation (i.e., vectored thrust), and Beta Technologies (i.e., lift-and-cruise), respectively ([^6]; Electric-VTOL-News 2023 [^14], 2023 [^15]), as shown in [Table 7](#tab7). Service priority types 1, 2, and 3 refer to regular, express, and medical AAM flight operation, respectively. The geofence width of directional corridor is determined based on [^28]. Their study calculates statistically optimal trajectory geofence buffer sizes using GNC and computational fluid dynamics wind simulations in an urban environment. The operation time window is set to 4 h (i.e., from 7 am to 11 am to simulate the morning commute). During the operation time, individual AAM scheduled departure times are randomly generated. The actual simultaneous take-off and landing are constrained by the concurrent take-off and landing (TLOF) capacity at each vertiport. Otherwise, there are 5 min intervals between scheduled departure times for AAM flights. Finally, we set the number of AAM flights in each vehicle type and corresponding service priority percentage distribution the same. This allows us to analyze how optimization solutions affect each vehicle type and service priority type in both centralized and distributed settings.

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_tab6.gif)

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_tab7.gif)

[Figure 10](#f10) visualizes the simulation map environment with PSU airspace sectorization. In this figure, vertiports are indicated by numbering with blue circles. Flight corridors are shown in gray lines, forming the AAM corridor network. Corridor transition points between PSUs are indicated by numbering with orange circles. Distributed PSU airspace regions are indicated with purple, blue, yellow, and green tints. In the simulation, the weight ratio (γ) of airborne delay to departure delay is set to 2 for all vehicle types. This helps analyze how the distributed AAM traffic management algorithm generates the optimal solution incorporating different ranges and speeds of vehicles. However, in reality, the delay weight ratio will vary by vehicle type. Below are the assumptions for the Monte Carlo simulation:

- Hovering is excluded from AAM traffic management due to its energy inefficiency. Only departure delay (ground delay) and airborne delay (adjusting cruise speed) are considered.
- Each AAM flight operates as a one-way trip; multiple trips for each flight are not taken into account.
- Concurrent TLOF capacity at each vertiport and maximum throughput capacity at each corridor remain constant throughout the operation time window.
- The cruise altitude for all AAM vehicle types is set to 3280 ft (i.e., 1000 m).
- AAM flight information is shared knowledge (i.e., scheduled departure/arrival time, departure/destination vertiports), meaning that it is accessible to adjacent PSUs for distributed traffic management.

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_f10.jpg)

Fig. 10. Construction of artificial map with airspace sectorization (grid size: 5 km). PSU, providers of services for urban air mobility.

## 5\. Simulation analysis

To evaluate AAM traffic flow management, 150 and 300 AAM flight operations are generated in the artificially created map with the above assumptions and parameters. As mentioned above, a total of 150 Monte Carlo simulations are conducted for each scenario: (1) 150 AAM flight operations with distance-based corridor routes, (2) 150 AAM flight operations with weighted corridor routes, (3) 300 AAM flight operations with distance-based corridor routes, and (4) 300 AAM flight operations with weighted corridor routes. The performance of both centralized and distributed PSU environments are examined and analyzed for comparison in terms of runtime, objective costs, and departure and airborne delay.

[Figure 11](#f11) compares the percentages of delayed flights for 150 and 300 flights. Mean and standard deviation values were calculated for both centralized and distributed settings based on 150 simulations of optimized/weighted corridor routes each. In the distributed AAM traffic management scenario, there was an average increase of less than 1.05% in the number of delayed flights for both 150 and 300 flights compared to the centralized system. As anticipated, the percentages of delayed flights were higher for 300 flights compared to 150 flights in both centralized and distributed systems.

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_f11.jpg)

Fig. 11. Comparison of delayed flight percentages: 150 versus 300 flights.

[Figure 12](#f12) presents the comparison of average delays by vehicle type and service priority type for both 150 and 300 flights in both centralized and distributed PSU systems. Across all vehicle types, 300 flights experienced more delays than 150 flights in both centralized and distributed systems. In the distributed system, vectored thrust and lift-and-cruise vehicle configurations exhibited greater average delays compared to multicopter. This is attributed to their extended ranges, increasing the likelihood of flight routes traversing multiple PSUs and resulting in increased average delays in departure and airborne delay to negotiate entry/exit times at transitioning PSUs. Regarding service priority types, 150 flights in the centralized system indicated that express service (i.e., second highest priority) experienced the least average delay, followed by medical and regular, respectively. For 300 flights, medical service (i.e., highest priority) experienced the least average delay, followed by express and regular services, respectively. However, the trend was consistent in the distributed system. For both 150 and 300 flights, regular service experienced the highest average delay, followed by express and medical services. In our simulation, we assigned weights of 1, 2, and 3 to regular, express, and medical service priority types, respectively. The results suggest that the weight of medical service should be significantly increased relative to the other two types in both centralized and distributed systems. That will ensure that medical service consistently has the least departure and airborne delay.

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_f12.jpg)

Fig. 12. Comparison of average delays by vehicle type and service priority: 150 versus 300 flights.

The runtime and objective cost comparisons are shown in [Fig. 13](#f13) for both 150 and 300 flights across centralized and distributed systems. The average runtime shows that centralized system has the longest duration for both 150 and 300 flights. This is because the distributed nature of individual PSUs allows them to manage a fraction of the total AAM flights handled by the centralized system. Notably, in the case of 300 AAM flight operations, individual PSUs generated coordinated AAM traffic solutions between 1.4 and 30 times faster compared to the time required for centralized management to generate a global solution. A similar trend was observed in objective costs, with individual PSUs having significantly lower costs compared to the centralized system. Furthermore, among the distributed PSUs, PSU 3 had the highest runtime and objective cost. This outcome can be attributed to the substantial number of vehicles operated within PSU 3, along with its extensive corridor network and a higher frequency of spatial corridor conflicts. Refer to [Fig. 10](#f10) that shows the PSU 3 corridor network. These findings show the critical influence of factors such as the volume of AAM vehicle operations, corridor network size, and the occurrence of spatial corridor conflicts on both runtime and objective costs. Nonetheless, as the number of AAM vehicles increases in the region, the results show that PSU 3 remains 28.4% faster than the centralized system in generating optimal solutions. The comparison of average ground and airborne delays for 150 and 300 flights is illustrated in [Fig. 14](#f14). Across both centralized and distributed systems, increasing ground and airborne delays are observed with a higher volume of vehicles. Furthermore, the distributed system resulted sub-optimal solutions, but the total delays incurred by each PSU are not significantly higher compared to the centralized system.

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_f13.jpg)

Fig. 13. Runtime and objective cost comparisons: 150 versus 300 flights. PSU, providers of services for urban air mobility.

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_f14.jpg)

Fig. 14. Average ground and airborne delay comparisons: 150 versus 300 flights. PSU, providers of services for urban air mobility.

[Figure 15](#f15) illustrates the comparison between distance-based and weighted corridor routes for both 150 and 300 flights. The comparison is based on the average count of total delay duration for delayed AAM flights. In both scenarios, the weighted route method resulted in slightly fewer spatial conflicts in PSU 0, PSU 1, and PSU 2. However, PSU 3 showed significantly higher spatial conflicts in the weighted corridor route method for both 150 and 300 flights. This may be attributed to the fact that as more AAM flights seek to avoid congested areas due to highly connected vertiports and high TLOF vertiports, the number of spatial conflicts inadvertently increases as vehicles are routed to detour around these areas, leading to more conflicts among themselves. Consequently, our weighted corridor route did not outperform the distance-based route method. However, we found that the weighted corridor route method minimizes the number of PSU transitions, thereby reducing the amount of coordination required between PSUs compared to the distance-based method. This finding underscores the potential of the weighted corridor route method. This highlights the need to explore the selection between the two route planning methods in congested areas to further reduce flight delays beyond solely relying on the distance-based route method. Lastly, [Fig. 16](#f16) presents the runtime comparison for varying numbers of flights in the centralized system. The computation time demonstrates a cubic increase, as indicated by the curve-fitted dash line. This provides insights into the algorithm’s scalability. For instance, the equation predicts that coordinating 1000 flights in the centralized system would require approximately 11 h to compute the solution. This underscores the minimum lead time required for AAM operators to submit their scheduled AAM flights in advance, facilitating efficient coordination within each PSU.

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_f15.jpg)

Fig. 15. Route method comparisons: distance-based versus weighted paths. PSU, providers of services for urban air mobility.

![](https://cdnsciencepub.com/cms/10.1139/dsa-2025-0020/asset/images/dsa-2025-0020_f16.jpg)

Fig. 16. Runtime versus number of flights.

## 6\. Conclusions and future work

Our research offers solutions for both centralized and distributed AAM traffic management, taking into account the diverse stakeholders involved in AAM architecture. The contributions of this paper are as follows: (1) A method to effectively sectorize low-altitude urban airspace is developed. (2) Centrally planning AAM routes is modeled considering the limited capacities of corridors and vertiports. We compare two different corridor route planning methods, and discuss how those methods can be combined for rerouting method. (3) A bi-level optimization architecture is formulated, solving distributed AAM traffic management. This involves MIP and cooperative game theoretic approach. We use an artificially created map to conduct Monte Carlo simulations, evaluating 150 and 300 AAM flight operations across three vehicle configurations and three service priority types.

Our research provides valuable insights into the performance of centralized versus distributed AAM network management strategies. We found that the centralized system consistently exhibits longer runtime for both 150 and 300 flights compared to individual PSUs within the distributed system (i.e. 1.4–30 times longer). Our analysis indicates that the distributed system may lead to sub-optimal solutions, but the total delays incurred by each PSU are not significantly higher compared to the centralized system. These findings underscore the importance and potential of scalable distributed AAM traffic management strategies in addressing the evolving demands of urban airspace. By providing a comprehensive technical framework, our research informs decision-making processes in the development and implementation of AAM traffic management strategies. Particularly, our findings highlight important implications for the practical deployment of AAM traffic management systems. The observed trade-off between solution optimality and computational efficiency suggests that a hybrid architecture may be highly beneficial. Centralized planning can provide a globally optimized strategic framework, and a distributed solution can perform real-time operational management more efficiently as traffic volumes increase. This integration will enable scalable and resilient urban airspace operations, supporting the safe and equitable expansion of AAM operations in complex urban environments. Our work thus informs regulators and service providers about the benefits of combining centralized and distributed approaches to address the evolving demands of AAM operations and management.

In future work, the stochastic optimization approach will be explored to address uncertainties in estimated times of arrivals, as well as robust optimization concerning the worst-case scenarios. Additionally, we plan to incorporate real map data with demand forecasts based on geography, population, and general aviation traffic to enhance the accuracy of AAM traffic management systems. There are numerous hyperparameters involved in the optimization, sectorization, and game-theoretic components of the bi-level distributed AAM traffic management framework. Future work will include sensitivity analyses of these hyperparameters to identify realistic and operationally meaningful values, which may provide valuable guidance for regulators. For example, simulation analysis can be further expanded to investigate the impact of different weight ratios (γ) for airborne and departure delays across various AAM vehicle types, as well as the impact of time-dependent TLOF vertiport capacities. Furthermore, by introducing auction mechanisms, we plan to incorporate the payment systems of each AAM vehicle operator within each PSU. Lastly, we will explore rerouting strategies and implement dynamic airspace sectorization for PSUs to further optimize AAM traffic management.

[^1]: Aerospace-America. 2023. Electric drones and air taxis target the logistical frustration of transporting organs for transplants. Available from [https://aerospaceamerica.aiaa.org/electric-drones-and-air-taxis-target-the-logistical-frustration-of-transporting-organs-for-transplants/?utm\_campaign=AerospaceAmericaAMB&utm\_medium=email&\_hsmi=294472799&\_hsenc=p2ANqtz--0lJ0ysk-\_CBUuwJSRI-GgoRMowEQit2CZnMpGirz0FWdJJK11eIEYEJNkQGjFI5ioXbnr9bn5nS3nKj-Pms-JdtT08A&utm\_content=294472799&utm\_source=hs\_email](https://aerospaceamerica.aiaa.org/electric-drones-and-air-taxis-target-the-logistical-frustration-of-transporting-organs-for-transplants/?utm_campaign=AerospaceAmericaAMB&utm_medium=email&_hsmi=294472799&_hsenc=p2ANqtz--0lJ0ysk-_CBUuwJSRI-GgoRMowEQit2CZnMpGirz0FWdJJK11eIEYEJNkQGjFI5ioXbnr9bn5nS3nKj-Pms-JdtT08A&utm_content=294472799&utm_source=hs_email)   \[accessed Jan 2025\].

[^2]: Agustín A., Alonso-Ayuso A., Escudero L.F., Pizarro C., et al. 2010. Mathematical optimization models for air traffic flow management: a review.

[^3]: Alves M.J., Clímaco J. 2007. A review of interactive methods for multiobjective integer and mixed-integer programming. Eur. J. Oper. Res. **180** (1): 99–115.

[^4]: Amazon. 2015. Revising the airspace model for the safe integration of small unmanned aircraft systems. Amazon Prime Air.

[^5]: Aurenhammer F., Klein R. 2000. Voronoi diagrams. *In* Handbook of computational geometry. Vol. 5. No. 10. pp. 201–290.

[^6]: Aviation-Week. 2023. Joby Aviation S4. Available from [https://aerospaceamerica.aiaa.org/features/building-vertiport-cities/](https://aerospaceamerica.aiaa.org/features/building-vertiport-cities/) \[accessed Jan 2025\].

[^7]: Balakrishnan K., Polastre J., Mooberry J., Golding R., Sachs P. 2018. Blueprint for the sky: the roadmap for the safe integration of autonomous aircraft. Airbus UTM, San Francisco, CA.

[^8]: Bauranov A., Rakas J. 2021. Designing airspace for urban air mobility: a review of concepts and approaches. Prog. Aerosp. Sci. **125**: 100726.

[^9]: Bertsimas D., Patterson S.S. 1998. The air traffic flow management problem with enroute capacities. Oper. Res. **46** (3): 406–422.

[^10]: Bertsimas D., Lulli G., Odoni A. 2008. The air traffic flow management problem: an integer optimization approach. *In* Integer Programming and Combinatorial Optimization: 13th International Conference, IPCO 2008 Bertinoro, Italy, 26–28 May 2008 Proceedings 13. Springer. pp. 34–46.

[^11]: Blondel V.D., Guillaume J.L., Lambiotte R., Lefebvre E. 2008. Fast unfolding of communities in large networks. J. Stat. Mech. Theory Exp. **2008** (10): P10008.

[^12]: Brown A., Harris W.L. 2020. Vehicle design and optimization model for urban air mobility. J. Aircr. **57** (6): 1003–1013.

[^13]: Clough B.T. 2002. Metrics, schmetrics! How the heck do you determine a UAV’s autonomy anyway? NIST Spec. Publ. **990**: 313–319.

[^14]: Electric-VTOL-News. 2023a. Beta Technologies ALIA-250. Available from [https://evtol.news/beta-technologies-alia/](https://evtol.news/beta-technologies-alia/) \[accessed Jan 2025\].

[^15]: Electric-VTOL-News. 2023b. Volocopter VoloCity (prototype). Available from [https://evtol.news/volocopter-volocity/](https://evtol.news/volocopter-volocity/) \[accessed Jan 2025\].

[^16]: EmbraerX. 2019. Flight plan 2030: an air traffic management concept for urban air mobility. Available from [https://daflwcl3bnxyt.cloudfront.net/m/f58fb8ea648aeb9/original/EmbraerX-White-Paper-Flight-Plan2030.pdf](https://daflwcl3bnxyt.cloudfront.net/m/f58fb8ea648aeb9/original/EmbraerX-White-Paper-Flight-Plan2030.pdf) \[accessed Jan 2025\].

[^17]: FAA. 2023a. Advanced air mobility implementation plan. Available from [https://www.faa.gov/sites/faa.gov/files/AAM-I28-Implementation-Plan.pdf](https://www.faa.gov/sites/faa.gov/files/AAM-I28-Implementation-Plan.pdf) \[accessed Jan 2025\].

[^18]: FAA. 2023b. Urban Air Mobility (UAM), Concept of Operations. v2.0, US Department of Transportation. Office of Nextgen, 2023. Available from [https://www.faa.gov/sites/faa.gov/files/Urban%20Air%20Mobility%20%28UAM%29%20Concept%20of%20Operations%202.0\_0.pdf](https://www.faa.gov/sites/faa.gov/files/Urban%20Air%20Mobility%20%28UAM%29%20Concept%20of%20Operations%202.0_0.pdf) \[accessed Jan 2025\].

[^19]: FAA-NextGen. 2023. A New U.S. DOT Volpe Center-FAA Thought Leadership Series. Transformation: urban air mobility concept of operations. Available from [https://www.volpe.dot.gov/events/transformation-urban-air-mobility-concept-operations](https://www.volpe.dot.gov/events/transformation-urban-air-mobility-concept-operations) \[accessed Jan 2025\].

[^20]: Garrow L.A., German B.J., Leonard C.E. 2021. Urban air mobility: a comprehensive review and comparative analysis with autonomous and electric ground transportation for informing future research. Transp. Res. C: Emerg. Technol. **132**: 103377.

[^21]: Geister D., Korn B. 2017. Concept for urban airspace integration DLR U-space blueprint. German Aerospace Center-Institut of Flight Guidance.

[^22]: Guerreiro N.M., Hagen G.E., Maddalon J.M., Butler R.W. 2020. Capacity and throughput of urban air mobility vertiports with a first-come, first-served vertiport scheduling algorithm. *In* AIAA Aviation 2020 Forum. p. 2903.

[^23]: Hill B.P., DeCarme D., Metcalfe M., Griffin C., Wiggins S., Metts C., Bastedo B., Patterson M.D., Mendonca N.L. 2020. UAM vision concept of operations (ConOps) UAM maturity level (UML) 4.

[^24]: Hofacker C., Tomlinson A. 2021. Building vertiport cities. Available from [https://aerospaceamerica.aiaa.org/features/building-vertiport-cities/](https://aerospaceamerica.aiaa.org/features/building-vertiport-cities/) \[accessed Jan 2025\].

[^25]: Huang H.M., Pavek K., Novak B., Albus J., Messin E. 2005. A framework for autonomy levels for unmanned systems (ALFUS). *In* Proceedings of the AUVSI’s Unmanned Systems North America. pp. 849–863.

[^26]: Jiang T., Geller J., Ni D., Collura J. 2016. Unmanned aircraft system traffic management: concept of operation and system architecture. Int. J. Transp. Sci. Technol. **5** (3): 123–135.

[^27]: Johnson W., Silva C. 2022. NASA concept vehicles and the engineering of advanced air mobility aircraft. Aeronaut. J. **126** (1295): 59–91.

[^28]: Kim J., Liberko N., Atkins E. 2022. Airspace geofencing volume sizing with an advanced air mobility vehicle performance model. *In* 2022 IEEE/AIAA 41st Digital Avionics Systems Conference (DASC). IEEE. pp. 1–8.

[^29]: Kopardekar P., Rios J., Prevot T., Johnson M., Jung J., Robinson J.E. 2016. Unmanned aircraft system traffic management (UTM) concept of operations. *In* AIAA Aviation and Aeronautics Forum (Aviation 2016). ARC-E-DAA-TN32838.

[^30]: Kulkarni S., Ganesan R., Sherry L. 2011. Static sectorization approach to dynamic airspace configuration using approximate dynamic programming. *In* 2011 Integrated Communications, Navigation, and Surveillance Conference Proceedings. IEEE. pp.J2–1.

[^31]: Le Tallec C., Le Blaye P., Kasbari M. 2017. Low level RPAS traffic management (LLRTM) concept of operation. *In* 17th AIAA Aviation Technology, Integration, and Operations Conference. p. 3938.

[^32]: Li A., Hansen M., Zou B. 2022. Traffic management and resource allocation for UAV-based parcel delivery in low-altitude urban space. Transport. Res. C: Emerg. Technol. **143**: 103808.

[^33]: Mathur A., Panesar K., Kim J., Atkins E.M., Sarter N. 2019. Paths to autonomous vehicle operations for urban air mobility. *In* AIAA Aviation 2019 Forum. p. 3255.

[^34]: Mckinsey. 2022. Perspectives on advanced air mobility. Navigating the emerging passenger urban and regional air-mobility industry. Available from [https://www.mckinsey.com/ /media/mckinsey/industries/aerospace%20and%20defense/our%20insights/perspectives%20on%20advanced%20air%20mobility/airmobilitypdf.pdf](https://www.mckinsey.com/%20/media/mckinsey/industries/aerospace%20and%20defense/our%20insights/perspectives%20on%20advanced%20air%20mobility/airmobilitypdf.pdf) \[accessed Jan 2025\].

[^35]: Myerson R.B. 2013. Game theory. Harvard University Press.

[^36]: NASA. 2018. Air traffic management for low-altitude drones. NASA, Washington, DC, USA.

[^37]: Nash J. 1953. Two-person cooperative games. Econom. J. Econom. Soc. 128–140.

[^38]: Odoni A.R. 1987. The flow management problem in air traffic control. *In* Flow control of congested networks, Springer. pp. 269–288.

[^39]: Paul S., Witter J., Chowdhury S. 2024. Graph learning-based fleet scheduling for urban air mobility under operational constraints, varying demand & uncertainties. arXiv preprint \[accessed Jan 2025\].

[^40]: Pongsakornsathien N., Bijjahalli S., Gardi A., Symons A., Xi Y., Sabatini R., Kistan T. 2020. A performance-based airspace model for unmanned aircraft systems traffic management. Aerospace, **7** (11): 154.

[^41]: Preis L., Hornung M. 2022. Vertiport operations modeling, agent-based simulation and parameter value specification. Electronics, **11** (7): 1071.

[^42]: Prim R.C. 1957. Shortest connection networks and some generalizations. Bell Syst. Tech. J. **36** (6): 1389–1401.

[^43]: Sergeeva M., Delahaye D., Mancel C. 2015. 3D airspace sector design by genetic algorithm. *In* 2015 International Conference on Models and Technologies for Intelligent Transportation Systems (MT-ITS). IEEE. pp. 499–506.

[^44]: SESAR. 2019. U-space concept of operations. Available from [https://www.sesarju.eu/sites/default/files/documents/u-space/CORUS%20ConOps%20vol2.pdf](https://www.sesarju.eu/sites/default/files/documents/u-space/CORUS%20ConOps%20vol2.pdf) \[accessed Jan 2025\].

[^45]: SESAR-Joint-Undertaking. 2018. European ATM master plan: roadmap for the safe integration of drones into all classes of airspace. SESAR Joint Undertaking: Brussels, Belgium.

[^46]: SkyGrid. 2019. SkyGrid concept of operations. Available from [https://www.skygrid.com/wp-content/uploads/2024/12/SkyGrid-Concept-of-Operations-v1.0-2.pdf](https://www.skygrid.com/wp-content/uploads/2024/12/SkyGrid-Concept-of-Operations-v1.0-2.pdf) \[accessed Jan 2025\].

[^47]: SMG-Consulting. 2023. AAM reality index: vehicle types. Available from [https://aamrealityindex.com/aam-reality-index](https://aamrealityindex.com/aam-reality-index) \[accessed Jan 2025\].

[^48]: Smith P.J., Spencer A.L., Billings C.E. 2007. Strategies for designing distributed systems: case studies in the design of an air traffic management system. Cogn. Technol. Work, **9**: 39–49.

[^49]: Thipphavong D.P., Apaza R., Barmore B., Battiste V., Burian B., Dao Q., et al. 2018. Urban air mobility airspace integration concepts and considerations. *In* 2018 Aviation Technology, Integration, and Operations Conference. p. 3676.

[^50]: Trandac H., Baptiste P., Duong V. 2005. Airspace sectorization with constraints. RAIRO Oper. Res. **39** (2): 105–122.

[^51]: Varon. 2023. Varon vehicles: UAM concept. Available from [https://varon.aero/concept/](https://varon.aero/concept/) \[accessed Jan 2025\].

[^52]: Vascik P.D., Hansman R.J. 2019. Development of vertiport capacity envelopes and analysis of their sensitivity to topological and operational factors. *In* AIAA Scitech 2019 Forum. p. 0526.

[^53]: Wisk. 2022. Concept of operations for uncrewed urban air mobility. Available from [https://wisk.aero/wp-content/uploads/2022/09/Concept-of-Operations-for-Uncrewed-Urban-Air-Mobility.pdf](https://wisk.aero/wp-content/uploads/2022/09/Concept-of-Operations-for-Uncrewed-Urban-Air-Mobility.pdf) \[accessed Jan 2025\].

[^54]: Wu C.L., Caves R.E. 2002. Research review of air traffic management. Transp. Rev. **22** (1): 115–132.

[^55]: Xue M. 2009. Airspace sector redesign based on voronoi diagrams. J. Aerosp. Comput. Inf. Commun. **6** (12): 624–634.

[^56]: Yang X., Wei P. 2020. Scalable multi-agent computational guidance with separation assurance for autonomous urban air mobility. J. Guid. Control Dyn. **43** (8): 1473–1486.

[^57]: Zhu G., Wei P. 2019. Pre-departure planning for urban air mobility flights with dynamic airspace reservation. *In* AIAA Aviation 2019 Forum. p. 3519.