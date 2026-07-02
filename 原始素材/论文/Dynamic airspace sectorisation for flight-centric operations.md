---
title: "Dynamic airspace sectorisation for flight-centric operations"
source: "https://www.sciencedirect.com/science/article/pii/S0968090X18310520?pes=vor&utm_source=clarivate&getft_integrator=clarivate"
author:
  - "[[Michael]]"
published:
created: 2026-07-01
description: "Today’s air traffic operations follow the paradigm of ‘flow follows structure’, which already limits the operational efficiency and punctuality of cur…"
tags:
  - "clippings"
---
## Part of special issue

[Artificial Intelligence and Data Analytics for Air Transportation](https://www.sciencedirect.com/science/journal/0968090X/vsi/101DT63HBBC)

[View special issue](https://www.sciencedirect.com/science/journal/0968090X/vsi/101DT63HBBC)

## Published by: Elsevier

### Published by

[![Elsevier](https://sciencedirect.elseviercdn.cn/prod/8c5bb82080b0f791d6ca95759147bab0d0e4e18d/image/elsevier-non-solus.svg)](https://www.sciencedirect.com/journal/transportation-research-part-c-emerging-technologies "Go to Transportation Research Part C: Emerging Technologies on ScienceDirect")

## FMS BEI检索SCI升级版 工程技术1区SCI Q1IF 8.4

,,

[View **PDF**](https://www.sciencedirect.com/science/article/pii/S0968090X18310520/pdfft?md5=607e7a6dce2eec27c73fcdc9618fad55&pid=1-s2.0-S0968090X18310520-main.pdf)

[10.1016/j.trc.2018.07.032](https://doi.org/10.1016/j.trc.2018.07.032)

## Highlights

## Keywords

Airspace

;

Dynamic sectorisation

;

Controller task load

;

Evolutionary algorithm

;

Clustering

- [Previous article in this issue](https://www.sciencedirect.com/science/article/pii/S0968090X18307113)
- [Next article in this issue](https://www.sciencedirect.com/science/article/pii/S0968090X18306016)

## 1\. Introduction

The sectorisation of airspace considers requirements of air traffic management (safety, capacity and efficiency), users (unhindered access) and environment (restricted areas over cities, residential areas, etc.). Particularly, air traffic control requires the airspace to be structured in order to accommodate an appropriate operational infrastructure for airspace users and operators. The airspace sectorisation is primarily triggered by operational demands (such as handling of mixed traffic, balanced controller work load, procedure design or capacity management), territorial aspects (air sovereignty) and operational performance (). In order to respond to the needs and future challenges of the air traffic (seamless European airspace), the initiated the Functional Airspace Block (FAB) design to implement multinational management and increase the airspace efficiency.

The dynamic airspace sectorisation presented in this paper deals with highly variable traffic patterns, which demand mid/short-term airspace adaptations. Our target is to create an appropriate, continuous airspace sectorisation in a fast and efficient way, which is able to react on current air traffic flows and efficiently support the airspace controller, even in uncommon traffic situations. Key drivers for dynamic traffic situations are characteristic air traffic flow patterns in Europe and the intercontinental connections (eastbound, westbound), as well as military actions (), disruptive events such as volcanic ash eruptions (), zones of convective weather (), prevention of contrails (), consideration of commercial space operations () and integration of new entrants (, ), which demand an efficient operational solution.

Furthermore, our approach bridges the gap between structured and unstructured airspace designs and will also be a fundamental key element for an efficient management of the future urban airspaces. If, in the future, the urban area consists of a significant amount of movements of personal air vehicles, the frequency of traffic will follow the daily time-dependent demand for transportation. Similar to today, there is a clear indication of a highly used infrastructure, which changes over the day (e.g. morning and evening peaks in and out of the city). However, the urban airspace will also be limited and fragmented due to immanent safety aspects (e.g. minimum distance requirements) or restricted areas (e.g. critical infrastructure). The dynamic sectorisation provides a scalable approach to balancing the air traffic demands and operational requirements by clustering traffic patterns, identifying areas of high-density traffic and providing an efficient planning and control structure to support airspace operators and users. Air traffic management in urban areas is expected to be one of the most challenging tasks in the coming years. Instead of deriving future flow control methods from today’s operations, we propose a fundamental change and provide an appropriate solution for handling dynamic traffic demands efficiently.

To ensure a more efficient allocation and a harmonised task load distribution, we consequently changed the current paradigm of traffic flow, which is determined by airspace structure (‘flow follows structure’), to a dynamic approach of a structure that is adjusted to the traffic flow sequentially (‘structure follows flow’). We contribute to the future flight-centric air traffic management with our specific approach of dynamically optimising the airspace focusing on the sector structure and resource allocation, considering both operational and economic efficiency targets (e.g. task load, fragmentation of flights by sectors). The approach of a dynamic reorganisation of airspace during the day of operation has several advantages, such as improved capacity utilisation through flexible use of airspace or appropriate distribution of task load for air traffic controllers and fast adaptation to changed operational boundaries. Dynamic Airspace Sectorisation (DAS) is a flexible method encompassing the idea of unstructured and (rigid) structured airspace, but differs from Dynamic Airspace Configuration (DAC), where predefined airspace blocks are combined to form new structures (merging and splitting). We are assuming a continuous airspace that will be separated without a specific demand for underlying structures but which considers both the current/future air traffic flows and the controller’s ability to manage all assigned aircraft. DAS enables a continuous restructuring of airspace sectors that depends on current requirements, and will be an important element for efficient air traffic operations, taking into account both regular and disruptive events. In particular, DAS covers today’s regular airspace structure and regional, trajectory-based, flight-/flow-centric operations challenged by. As emphasized, we also see the DAS approach as a sustainable solution for future air traffic management in the context of urban flight operations. Our DAS solution can be adapted to different airspace management concepts and already covers all operational aspects needed for balanced handling of dynamic air traffic flow. It is scalable and therefore able to cope with a city’s lower airspace () as well as a huge part of the upper airspace ().

### 1.1. Status quo

Over the years, several authors have developed ideas for an automatic creation of airspace sectorisation or the adaptation of airspace sectors. provide a brief overview on metaheuristics used in airspace management. One of the first approaches using evolutionary algorithms was developed by. Other approaches applied the principles of graph theory, Voronoi diagrams, linear integer programming or clustering of flight tracks. A detailed overview of recent work is given by and. A comparison of eight different methods is provided by. Furthermore, a survey on the work carried out in the area of dynamic airspace sectorisation is given by, listing relevant approaches of recent years in a systematic manner. Many of these ideas are of a more theoretical nature and not all are directly applicable to an authentic non-convex airspace problem.

### 1.2. Objectives and document structure

The objective of our research is to automatically provide an appropriate airspace sectorisation, comparable to today’s sector structure, without incorporating explicit expertise of air traffic controllers. This is necessary for a more flight-centred approach to sectorisation where the structure of the sectorisation depends highly on the predicted traffic. Especially for new approaches, such as the idea of ecologically sensitive flight operations, where airspace shall be closed due to contrail management, it will be necessary to adapt the airspace to the changed requirements of the environment. Therefore, it is not possible to rely on controller knowledge due to variable and dynamically changing constraints. In our case, the controller behaviour is implicitly covered by a task load model. Furthermore, the aim of our approach is to efficiently consider varying air traffic flows in different time intervals and react on specific events which influence the air traffic system, such as zones of convective weather.

When developing the idea of automatic sectorisation (AutoSec), we had in mind both flight-centric operations and multi-criteria optimisation. AutoSec allows the creation of an appropriate airspace structure in a three-step approach: (1) fuzzy clustering of traffic flows on the day of operations, (2) generation of new sector structure based on Voronoi diagrams and (3) application of evolutionary algorithm in order to adjust and optimise the new sector structure depending on dynamic demands over the day of operations. Within this paper, we compare the actual sectorisation of a specific airspace with evolutionary optimised solutions, which are based in a first step on real airspace and in a second step on newly created airspace structure. The optimisation in both cases is carried out with the same evolutionary algorithm and evaluation function ().

The paper is structured as follows: In we provide the general background information referring to the different reorganisation types DAC and DAS, present the task load system used for the simulation and explain the structure of the simulation framework. Within, the concepts of fuzzy clustering, Voronoi diagrams and evolutionary algorithms as well as the used data structure are explained in general. The theoretical background and the necessary adaptations of the methods used to meet the problem of reorganising airspace are introduced in. In particular, we provide a solution for handling non-convex sector shapes efficiently and demonstrate the concept of interim diagrams allowing a smooth transition between different sectorisations, which are caused by changing traffic flow patterns. The experimental setup is given in. The results for the optimisation of the real sector structure of EDYYDUTA and our DAS approach, together with a comparison of these results, are presented in. Furthermore, a first attempt at analysing the creation of building blocks is given. Finally, the conclusion provides an overview of the achieved results and an outlook on future research activities.

## 2\. Background – Optimisation approach and data structure

### 2.1. Approaches to airspace reorganisation

Approaches to reorganising airspace can generally be divided into two sub-groups depending on type and target of partition: Dynamic Airspace Sectorisation and Dynamic Airspace Configuration. The latter includes all methods that rearrange predefined parts of the airspace in dependence on changing traffic patterns. For this, a basic set of airspace blocks is created and combined in changing combinations to meet the actual requirements. The target is to minimise the effort for the controllers when changing from one sectorisation to another and to increase the stability of the airspace sectorisation (). Furthermore, this approach increases the familiarity of controllers with possible sectorisations because the airspace blocks are reused. e.g. used Voronoi diagrams to partition the French airspace, depending on the traffic density as constraint for the design of a route network. Tree search methods have been applied by for airspace configuration from fixed airspace modules based on controller workload forecast. adopted dynamic programming techniques in their DAC approach. In, constraint-based local search techniques with geometric and workload constraints built the basis for an approach generating a static airspace sectorisation from a regular mesh of cells.

In comparison, DAS approaches create a complete new sectorisation without considering actual airspace structure or using predefined elements, as is presented in, ),,,. This reorganisation approach therefore creates a less familiar setting for controllers but can be used for situations where no basic knowledge concerning the best airspace structure is available. This is especially the case when the airspace sectorisation has to be adapted to uncommon or unfamiliar events, as is the case for special meteorological effects such as volcanic ash or airspace closed to prevent contrails (). Examples for DAC are given by,,. introduced a level system for DAC based on so-called building blocks, which are stable in form and size. Here, the level determines the possibilities for rearrangement: for level one this is severely restricted, whilst for level four it is highly flexible. Thus, this level system is a kind of transition from DAC to DAS.

### 2.2. Calculation of task load

Suitable task load models provide a fundamental background, which offers the opportunity to equally distribute the expected work load among air traffic controllers in adjacent sectors. As basis for the calculation of task load times, a comprehensive study was carried out at the DLR (). Hence, a system of tasks and subtasks was defined and time values for the duration of each task and the frequency (if necessary) were advised. Further investigations could also include air traffic complexity, as driver for controller workload ().

The definitions, subdivision of controller tasks and times used by several companies, such as the German air navigation service provider DFS or EUROCONTROL, were taken into account. As a result, a system of 55 tasks for radar, planning, arrival, airport, tower, and apron controllers were defined with a set $T_{\mathit{ST}}$ of 129 subtasks, grouped by Monitoring (MO), Radio Telephony (RT), Coordination (CO), Clearances (CL), Conflict Search (CS) and Conflict Resolution (CR). For every subtask $t$ a task load time $t_{\mathit{tlt}}$ was defined. Subsequently, all task load values for all aircraft inside the sector borders were summarised to a sector task load value $\mathit{TL}_{S}$.

Let $A_{S}$ be the set of all aircraft moving within sector $S$, $T_{a}$ the set of all task load subtasks from set $T_{\mathit{ST}}$ applicable for aircraft $a \in A_{S}$, $n_{t}$ the number of events of subtask $t \in T_{\mathit{ST}}$ and $t_{\mathit{tlt}}$ the time needed to fulfil this subtask, then the task load $\mathit{TL}_{S}$ for a sector $S$ is defined as follows:(1) $\mathit{TL}_{S} = \sum_{a \in A_{s}} \sum_{t \in T_{a}} n_{t} \cdot t_{\mathit{tlt}}$

exemplarily shows some tasks for a radar controller.

Table 1. Example of some classification types and task load times for controller actions within a radar sector.

<table><thead><tr><th>Main Type</th><th>Sub Type</th><th>Task-Name</th><th>Time (s)</th><th>per × Sec.</th><th>Group</th></tr></thead><tbody><tr><td rowspan="6">Sector Entry</td><td rowspan="3">CHANGE_SECTOR_IN_CRUISE_FROM_SAME_ACC</td><td>Initial Call</td><td>11</td><td>–</td><td>RT</td></tr><tr><td>Initial Monitoring</td><td>14</td><td>–</td><td>MO</td></tr><tr><td>Receipt Flight Strip</td><td>3</td><td>–</td><td>CO</td></tr><tr><td rowspan="3">CHANGE_SECTOR_IN _CRUISE_FROM_DIFF_ACC</td><td>Initial Call</td><td>15</td><td>–</td><td>RT</td></tr><tr><td>Initial Monitoring</td><td>14</td><td>–</td><td>MO</td></tr><tr><td>Receipt Flight Strip</td><td>3</td><td>–</td><td>CO</td></tr><tr><td colspan="6"></td></tr><tr><td rowspan="2">Conflict</td><td>CONFLICT_TYPE_1</td><td>Conflict Detection</td><td>17</td><td>–</td><td>CS</td></tr><tr><td>(Consecutive flights, cruise)</td><td>Conflict Resolution</td><td>60</td><td>–</td><td>CR</td></tr><tr><td colspan="6"></td></tr><tr><td>Recurring Monitoring</td><td>RECURRING_MONITORING</td><td>Monitoring</td><td>5</td><td>120</td><td>MO</td></tr></tbody></table>

### 2.3. Simulation framework

To provide a dynamic sectorisation, the calculation consists of three steps: (1) aggregation of traffic data, (2) initial sector structure and (3) optimisation. This section provides a general introduction of the fundamental principles and introduces the tool chain used to conduct the experiments described in this paper.

For this, a simulation framework with three tools has been established (). The framework consists of the tools PrePro (pre-processor), RouGe (route generator), and AutoSec (optimisation framework), see.

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr1.jpg)

Download: Download high-res image (88KB)

RouGe and PrePro are developed and used to generate the necessary airspace data based on e.g. Eurocontrol’s DDR2 data sets. Furthermore, the boundary of the airspace area of interest is defined and created using PrePro. This could be any connected area of airspace with one continuous boundary independent of national borders, fulfilling the connectivity constraint mentioned by several authors (cf. ). PrePro extracts data of the real sectorisation e.g. from DDR-2 data and feeds them into the optimisation tool AutoSec. RouGe uses the boundary created with PrePro to filter aircraft position data in dependence on parameters such as the given boundary, flight level and time. The resulting flight track data are then used to compute cluster centres using fuzzy clustering methods. These cluster centres are further used in AutoSec to construct a Voronoi diagram. Subsequently, the selected flights are sent to PrePro, which decreases the number of trajectory points for each flight.

The next step is carried out by AutoSec and depends on the type of experiment. AutoSec is able to create a Voronoi diagram based on a group of sector centres (e.g. cluster centres of RouGe) as the start sectorisation or to import a real sectorisation exported from PrePro. The start sectorisation is handed over to an evolutionary algorithm (, ), which then optimises the selected sectorisation in dependence on a given evaluation function.

The evolutionary algorithm shifts the sector boundaries in order to create an appropriate solution with respect to evaluation criteria such as task load and task load standard deviation (cf. ).

For the optimisation process, a time component is included by defining time intervals and using different start sectorisations/cluster sets for each time interval. Thus, changing demands within a day’s traffic flow, e.g. caused by changed weather conditions, are considered. The separate optimisation for successive time intervals can lead to considerable differences in sector structure, so the concept of interim diagrams was developed to smooth the transitions between consecutive sectorisations ().

The sequence of steps for the creation of an optimised sectorisation is:
- 1.
	Creation of a boundary for a predefined airspace area (PrePro).
- 2.
	Creation of flight data sets for each predefined time interval of a day (RouGe).
- 3.
	Calculation of cluster centres for each flight data set using fuzzy clustering methods (RouGe).
- 4.
	Calculation of a convex Voronoi diagram as initial sectorisation based on the cluster centres for each time interval created in step 3 as initial solution for step 6 (AutoSec).
- 5.
	Application of a non-convex boundary form to the resulting Voronoi diagram of step 4 (AutoSec).
- 6.
	Optimisation of the resulting diagram by an evolutionary algorithm with respect to a certain optimisation task (e.g. uniform task load distribution, AutoSec).

Optional:
- 7.
	Subdivision of each time interval into an even number of sub-intervals and creation of interim diagrams for each sub-interval based on the surrounding optimised Voronoi diagrams (AutoSec).
- 8.
	Adaptation of the interim diagrams by an evolutionary algorithm with respect to a certain optimisation task and the structure of the underlying optimised Voronoi diagrams (AutoSec).

## 3\. Methodological foundations

### 3.1. Fuzzy clustering

In general, the aim of clustering techniques is to find a partition of a given dataset. In a fuzzy partition, a point is not necessarily assigned to a unique class or cluster (see and ). Instead, membership degrees are associated with each point and each cluster. These membership degrees provide information about the ambiguity of the classification. Fuzzy clustering techniques are able to adapt to noisy data and to classes which are not well-separated. Here, we consider aircraft position data (trajectories) as data points and a clear separation of clusters might be difficult. The clustering solution consists of cluster centres, i.e. the centre of gravity of a cluster w.r.t. a distance function, and membership degrees. For an overview on fuzzy clustering and its applications, see or. For our approach, we use a variant of the fuzzy-c-means clustering called probabilistic clustering () that is based on the great circle distance. In probabilistic clustering, the sum of membership degrees of a data point has to be equal to one and each membership degree has to be greater than zero.

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr2.jpg)

Download: Download high-res image (133KB)

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr3.jpg)

Download: Download high-res image (72KB)

Knowing the favoured number of sectors in advance leads to a fixed number of clusters that have to be determined. If the number of clusters is unknown, unsupervised clustering methods applying global validity measures can be used; cf.. The basic idea of unsupervised clustering is to define an upper (and eventually lower) bound of clusters and carry out the clustering for each number of clusters. A global validity measure is used to rate the partition as a whole. The ratings of different partitions are compared. Examining the curve of the validity measure over the number of clusters might show not only a best solution but also local extrema where a great gradient to neighbouring cluster numbers indicates reliable solutions. Suited of our problem are e.g. validity measures like partition coefficient or partition entropy that rate the crispness of the partition, see.

demonstrates the clustering result for an example area for one time interval. The data points are associated to the cluster centre to which they have the highest membership degree, i.e. represented by the black lines.

### 3.2. Voronoi diagrams

A Voronoi diagram (cf., ) is a possibility for structuring a plane in dependence on a certain number of so-called centre points into sections where every point belongs to the section with the nearest centre point. Edges are created of all points which belong to two centre points, i.e. the points of an edge have the same distance to the two centre points, and vertices are those points which are associated with three different centre points (see ). An area containing all points with the same nearest point is called “face”. A convex hull is added once the faces have been determined. Often this convex hull simply has the form of a rectangle. With this definition, vertices are the backbone of a Voronoi diagram, because a shift in the vertex positions will rearrange the whole Voronoi diagram. Therefore, the vertices are the elements to be optimised by the evolutionary algorithm of AutoSec.

### 3.3. Evolutionary algorithms

The principles of evolutionary algorithms follow the evolutionary theory from biology (cf., ) and are used in several aviation-related research fields, such as network planning (), airline crew pairing () and aircraft boarding (, ). An approach to apply genetic algorithms to dynamic airspace configuration is presented in. In nature, a group of individuals mix their genetic material, especially the information coded in chromosomes, to obtain a better chance of survival in a hostile environment through a higher degree of adaptation. For an evolutionary algorithm, a population with a predefined number of solutions for an artificial problem is created, where each solution is coded as sequence (chromosome) of parameters (genes) describing a possible problem solution. Typically, the chromosomes are of constant length. As in nature, solutions can be mixed between two chromosomes (so-called crossover), or some genes of a single chromosome can be mutated. To guarantee the “survival of the fittest”, an evaluation function $evalF$ is created which rates each solution and supervises the selection of the fittest chromosomes for the next generation. These will undergo the evolutionary operator’s crossover and mutation again until an appropriate solution is found. This process is normally performed for a fixed number of generations or a prescribed distance of the evaluation value to a known solution.

### 3.4. Data structure

To store data of a Voronoi diagram, an appropriate data structure called Doubly Connected Edge List (DCEL, ) is used. A DCEL consists of three lists for vertices, half-edges and faces, where the elements of every list are connected in several ways. For the edge list, each (undirected) edge of the Voronoi diagram is divided into a pair of two half-edges (directed) with opposite directions called twins (see ), e.g. e11/e11 <sup>*</sup>. Furthermore, the information about the previous and the next half edge when moving counter-clockwise though the half-edges of the corresponding face, the origin vertex, and a pointer to the corresponding face are stored with every half-edge additionally. Faces are finally defined by the centre point and a pointer to a single half-edge belonging to this face. So, every half-edge is linked to the corresponding face and each face is defined by only one corresponding half-edge. With this smart and appropriate structure, AutoSec is able to manage the framework of airspace within its software in an easy way, allowing the complete structure to be attained with a minimum of knowledge, e.g. moving through a complete sector when knowing only one edge and identifying all related sectors when knowing only one vertex. In particular with this data structure it is possible to introduce the authentic, non-convex boundary forms presented in the next section.

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr4.jpg)

Download: Download high-res image (120KB)

## 4\. Theoretical background and adaptations to the sectorisation problem

### 4.1. Non-convex boundaries

Another problem to be solved is the integration of a non-convex boundary line for an airspace region. Voronoi diagrams are limited by a convex hull. In the case of airspace areas which are taken into account to build the sectors, this cannot be guaranteed. Therefore, the calculation – carried out with a Fortune algorithm () – has been extended in such a way that a Voronoi diagram can be adapted to arbitrary boundaries (). To start with, the Fortune algorithm is applied to the closest rectangle including the selected boundary (see ) which is clearly convex.

The workflow of a sectorisation considering an authentic, non-convex boundary polygon is based on a “line-segment-intersection” method (): The necessary steps are listed in the following.
- 1.
	Transform the boundary polygon into another DCEL.
- 2.
	Calculate coordinates for all breakpoints between the half edges of both DCELs and sort the breakpoint list with increasing y-coordinate values.
- 3.
	Copy both DCEL’s into a common DCEL (overlay).
- 4.
	Move through the breakpoint list and reconstruct the affected half edges and vertices (create new half edges and vertices, assign new previous, next and twin pointers) and create a new face list for the overlay DCEL (see ).
	![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr5.jpg)
	Download: Download high-res image (109KB)
- 5.
	Remove all vertices, half edges, and faces which are outside the boundary polygon.

The resulting structure after step five is not necessarily a Voronoi diagram (see ). It will be addressed as an initially adapted Voronoi diagram instead. In the case of a sector being divided and no centre point being included in a new sector, the centre of gravity is calculated as new centre point for each newly created sector.

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr6.jpg)

Download: Download high-res image (54KB)

### 4.2. Integration of a dynamic time-component

Due to different time zones in the world and the traffic between them, the structure of the air traffic does not remain constant throughout the day. This results in the necessity to define different airspace structures for the course of the day where each sectorisation is adapted to the current amount and distribution of air traffic. To increase DAS acceptance of airspace controllers, we aim at a smooth transition between successive sectorisations. Furthermore, smooth transitions between different sectorisations are operationally mandatory in order to prevent flights from leaving one sector, entering the next and then jumping back to the first because new sectorisation demands it. For this transition, interim diagrams are introduced which are inserted between the sectorisations. The general course of action for the creation of interim diagrams is therefore as follows:
- 1.
	Calculation of Voronoi diagrams for each set of centre points.
- 2.
	Mapping of vertices between successive Voronoi diagrams as far as possible.
- 3.
	Splitting of the time intervals into smaller sub-intervals.
- 4.
	Application of evolutionary algorithm with normal evaluation function to each Voronoi diagram to generate a so-called optimised Voronoi diagram (i.e. not necessarily a Voronoi diagram).
- 5.
	Calculation of the corresponding number of interim diagrams (not necessarily Voronoi diagrams) taking the mapped vertices of the optimised Voronoi diagrams into account.
- 6.
	Application of the evolutionary algorithm.

The structure of Voronoi diagrams depends on the number and position of the centre points. When using time-dependent sets of centre points, the resulting Voronoi diagrams can be very different in the number of faces as well as in position and number of vertices. The target is to insert interim diagrams between successive pairs of Voronoi diagrams which should reflect the structure of both involved Voronoi diagrams. Therefore, it is necessary to identify those faces and vertices, which exist in both diagrams, because they can be used to calculate interim vertices between the original vertices. This is done by using information about the position of the centre points, the position of the vertices and the location of the sector itself (inner/outer sector).

The mapping algorithm starts by identifying all faces next to the boundary for both Voronoi diagrams. Subsequently, for every face of the Voronoi diagram with the lower number of faces, a mapping face from the other Voronoi diagram is searched by calculating the distances between the centre points and selecting the nearest centre point with the same face type (inner / outer). In the next step, all vertices are mapped which are (nearly) the same (e.g. boundary vertices) or start at the boundary. For the latter, the adjacent faces have to be known (). For the last step, all faces are ordered in a sequence depending on the relation of the number of already mapped to all vertices of this face. Then, the last unmapped vertices for all faces are subsequently mapped in the same way as the faces before by using distance and type of vertex (inner / outer / starting at boundary).

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr7.jpg)

Download: Download high-res image (56KB)

This method works from outside to inside by identifying the outer sectors first and then using the information to identify mappings for the adjacent sectors. This procedure has been tested for parts of upper airspace divided into a maximum number of eight sectors so far and worked well. Nevertheless, with an increasing number of sectors, this procedure will be subject to further investigations and improvements.

The connected vertex in a successive Voronoi diagram is called Map, in a preceding diagram preMap. If successive Voronoi diagrams have different vertex numbers, as many connected vertices as possible are identified. The remaining vertices stay unchanged for the interim diagrams.

As previously mentioned, the most difficult challenge for the creation of interim diagrams arises from the fact that surrounding optimised Voronoi diagrams possess significantly different structures. To cope with this, the number (*nr*) of interim diagrams inserted between two optimised Voronoi diagrams should be even-numbered, so that it can be divided into two equally numbered groups. The first group, consisting of $\left(V_{1} , \hdots , V_{\mathit{nr} / 2}\right)$, then receives structure and data from the first optimised Voronoi diagram $V_{0}$, whilst the second group, consisting of $\left(V_{\mathit{nr} / 2 + 1} , \hdots , V_{\mathit{nr}}\right)$, receives structure and data from the second optimised Voronoi diagram $V_{\mathit{nr} + 1}$. In the next step, the coordinates of all mapped vertices are recalculated for the interim diagrams proportionate to the distance between the vertex of the first optimised Voronoi diagram and its mapping.

For a given sequence of diagrams $V_{0} , V_{1} , \hdots , V_{n} , V_{n + 1}$, where $V_{0}$ and $V_{n + 1}$ are optimised Voronoi diagrams and $V_{1} , \hdots , V_{n}$ the interim diagrams between them, the positions for those vertices of the interim diagrams where a mapping exists are calculated with (2): let $V_{i} \left(j\right)$ be the vertex *j* of diagram $V_{i} , i \in \left(1 , . . , n r\right)$ and $V_{0}^{\mathit{map}} \left(j\right) = V_{\mathit{nr} + 1} \left[k\right]$ the vertex *k* of the second optimised Voronoi diagram (to which vertex *j* of the first optimised Voronoi diagram is mapped).(2) $\begin{matrix}V_{i} \left(j\right) \left(x\right) = V_{0} \left(j\right) \left(x\right) + \left(\frac{i}{\mathit{nr} + 1}\right) * \left(V_{\mathit{nr} + 1} \left(k\right) \left(x\right) - V_{0} \left(j\right) \left(x\right)\right) \\ V_{i} \left(j\right) \left(y\right) = V_{0} \left(j\right) \left(y\right) + \left(\frac{i}{\mathit{nr} + 1}\right) * \left(V_{\mathit{nr} + 1} \left(k\right) \left(y\right) - V_{0} \left(j\right) \left(y\right)\right)\end{matrix} , i \in \left(1 , . . , \frac{\mathit{nr}}{2}\right)$

A similar formula based on the data of the second Voronoi diagram is used for the calculation of the coordinates of the second group of interim diagrams $Vi,i∈{nr/2+1,⋯,nr}$. Vertices without a mapped vertex remain unchanged. shows a graphical interpretation of this procedure. Here, parts of a DCEL for the first (blue) and the second (yellow) optimised Voronoi diagrams are shown. In the next step, two new diagrams are calculated, where the structure of the first one relies on the first optimised Voronoi diagram and the second one on the structure of the second. Then the coordinates are adapted in such a way that they consist of 2/3 (bigger arrow) of the first and 1/3 (smaller arrow) of the second diagram for the first interim diagram and vice versa for the second. So, I4 moves upwards and I4 <sup>*</sup> downwards in comparison to the original vertex positions, and V5 <sup>*</sup> remains unchanged.

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr8.jpg)

Download: Download high-res image (90KB)

### 4.3. Evolutionary algorithm of AutoSec

Within this section, the used evolutionary algorithm with the problem specific adaptation is described, consisting of the formal description of the search space, description of the evolutionary operator’s mutation and crossover, the evaluation function and selection process.

For the evolutionary algorithm, a rectangular portion $AS$ of airspace was selected with $\mathit{AS} = \left(\left(x , y\right) \left|\right. x_{u} \leq x \leq x_{l} , y_{l} \leq y \leq y_{u}\right)$, where $u = \left(x_{u} , y_{u}\right) \in \mathbb{R}^{2}$ denotes the upper left and $l = \left(x_{l} , y_{l}\right) \in \mathbb{R}^{2}$ the lower right corner. Let B be the boundary described as polygon $B = \left(b_{1} , \hdots , b_{m}\right)$ of length $m$ with $bi∈AS,i∈{1,⋯,m}$, $n$ the proposed number of sectors and $k$ the number of vertices of the resulting Voronoi diagram. Then(3) $\mathit{AS}_{B} = \left(\left(x , y\right) \left|\right. \left(x , y\right) \in A S \land \left(x , y\right) l a y s o n b o u n d a r y B\right)$ is the set of all points on the boundary B and(4) $\mathit{AS}_{\mathit{IB}} = \left(\left(x , y\right) \left|\right. \left(x , y\right) \in A S \land \left(x , y\right) i n s i d e b o u n d a r y B\right)$ the set of all points inside B.

The vertices $vi∈AS,i∈{1,⋯,k}$ of the original Voronoi diagram () are used directly as genes and a sequence of these vertices with a predefined order forms a chromosome $c = \left(\right. v_{1} , \hdots , v_{k}$) (). Therefore, each chromosome represents a complete sectorisation determined by the structure of the Voronoi diagram calculated beforehand. The population contains in each chromosome a valid list of vertices.

The general structure of the selected evolutionary algorithm is based on the modGA introduced by. It is especially designed to prevent so-called super-individuals from overtaking the population. For this, three groups of chromosomes are created for each generation, where the chromosomes of the first group are all different and remain unchanged. They are selected using a stochastic sampling selection (cf. ), but without replacement. The elements for the other two groups are selected using stochastic sampling with replacement. The chromosomes of the second group undergo the crossover operator, whilst the chromosomes of the third group are mutated. So, crossover is responsible for composing new solutions from existing ones and the mutation operator carries out small steps to improve the solution.

As crossover operator for a selected pair of parent chromosomes the well-known uniform crossover was used (c.f. ), where every gene of the first chromosome has the same prescribed chance of being exchanged with the corresponding vertex of the other parent chromosome. Within the chromosomes, the position of a vertex is not important; it is therefore not necessary to exchange parts of the chromosomes as is done when using one or two-point crossover.

When applying the mutation operator, it has to be guaranteed that a vertex $v \in \mathit{AS}_{B}$ stays at the boundary after mutation and a mutated inner vertex $v \in \mathit{AS}_{\mathit{IB}}$ stays inside the boundary. This problem was solved by introducing two adaptations to the algorithm structure and especially to the mutation operator. The first adaptation is the replacement of the part of the boundary polygon of the associated face/sector by the two boundary breakpoints (see ). These breakpoints are added as additional artificial vertices to the adapted Voronoi diagram and are mutated only by moving them on the boundary. Now, the number of vertices for each face always stays the same and a mutation operator is defined for every type of vertex (inner / boundary).

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr9.jpg)

Download: Download high-res image (107KB)

For the second adaptation, the boundary is considered as a straight line and a percent value is allocated to the relative position of each outer vertex on this line (breakpoint between faces and boundary polygon). With this adaptation, the mutation of a boundary vertex is handled as the random selection of a percentage between the percentage values of the surrounding boundary vertices. shows the mutation area (green line between 40 and 70%) for the outer vertex at 45%.

For the use of interim diagrams, a special equation to limit the mutation of vertex coordinates was created. In the case of equal Map and preMap, the difference between the new and the original vertex is calculated and set in relation to a predefined threshold value, where values above the threshold are penalised by doubling the distance. In the case of different Map and preMap, an ellipsoid between Map and preMap is used to define an allowed area for the location of a new vertex point (see ). The border of this area is defined by all points where the sum of the distances of the point to the focus points F <sub>1</sub> and F <sub>2</sub> is the same. Each point outside this ellipsoid is penalised. The difference to the original vertex is calculated for each vertex and called *vertexCloseness* of an interim vertex. In the case of unmapped vertices, a predefined mutation limit is used.

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr10.jpg)

Download: Download high-res image (99KB)

We have tested several variations of factors for the evaluation function of the evolutionary algorithm (see ). From these, the following five elements were selected for the simulations presented here:
- 1.
	Sum of task load over all sectors (TL).
- 2.
	Standard deviation of task load between sectors (TLSD).
- 3.
	Standard deviation of interior angles (A).
- 4.
	Number of flight intervals (partition of flights by sectors) over all sectors (FI).
- 5.
	Closeness of vertices (VC, optional, in case interim diagrams are in use).

With this selection of evaluation parameters, the problem can be seen as a multi-objective optimisation problem, as stated by. Whilst the first two elements are directly connected to the task load distribution problem (balanced work flow for airspace controllers), the third and fourth are used to ensure an operationally relevant (more “usable”) sector layout. The calculation of task load was described in. and the interior angles of a structure are the angles between successive edges. So, the standard deviation of interior angles measures the difference to a polygon with uniform angles., have stated that a convexity constraint should be applied to created sectors to ensure that an aircraft visits every sector only once (). They also demanded a constraint limiting the inter-sector flow. These constraints are included indirectly by the evaluation factors “standard deviation of interior angle” and “number of flight intervals” but not as mandatory restriction. Including the number of flights per sector indirectly results in avoidance of short dwell times of flights in sectors and represents segmentation of flights over different sectors. As far as the convexity constraint is concerned, today’s sectors are not necessarily convex. Due to the form of the evaluation function, Pareto optimal results with respect to task load and task load standard deviation can be expected, where the shape may look completely different. The optimisation is based on a fixed flight plan, which remains unchanged for the optimisation process. Since no traffic movement simulation takes place, delay is not evaluated.

To avoid the influence of incomparable value ranges for the different factors of the evaluation function, we developed a combined function using a ranking approach where the influence factors are weighted (). These weights are not necessarily constant during the simulation run, but are adapted to some extent during optimisation. This is the case for $w_{\mathit{TLSD}}$ because $TL$ and $TLSD$ act in opposite directions and have to be optimised consecutively (),(5) $\begin{matrix}\mathit{evalF} = w_{\mathit{TL}} \cdot E_{\mathit{TL}} + w_{\mathit{TLSD}} \cdot E_{\mathit{TLSD}} + w_{A} \cdot E_{A} + w_{\mathit{FI}} \cdot E_{\mathit{FI}} + w_{\mathit{vc}} \cdot E_{\mathit{vc}} \\ \text{with} w_{\mathit{TL}} = 1 , w_{A} = 0.5 , w_{F} = 0.5 , \\ w_{\mathit{TLSD}} = \left(1 + w_{\mathit{TL}} + w_{A} + w_{\mathit{FI}}\right) - \left(\mathit{gen}_{\mathit{nr}} \cdot 1.5 / \mathit{gen}_{\mathit{max}}\right)\end{matrix}$

In, $\mathit{gen}_{\mathit{nr}}$ is the number of the actual generation, $\mathit{gen}_{\mathit{max}}$ is the maximum number of generations to be calculated and *w <sub>i</sub>* are the weights for the corresponding evaluation factors *E <sub>i</sub>*, $i∈TL,TLSD,A,FI,VC$. With an evaluation function consisting of several - partly contrary - elements, it is possible to create sectorisations which differ widely in shape but show a very similar evaluation value. Furthermore, when an optimisation is carried out where interim diagrams are created, an additional part $w_{\mathit{vc}} \cdot E_{\mathit{vc}}$ is added to the evaluation function representing the vertex closeness.

## 5\. Experimental setup

As airspace region, EDYYDUTA (EDYY Deco Sectors, Maastricht) was selected as demonstrative example because of its clear structure with only four sectors. Furthermore, this airspace region was also used by for several simulations for their DAC approach and allows a comparison between DAC and our DAS approach. To take a sufficient number of flights as basis, the flight level range was set to the region from flight level 300 to unbounded (standard level for higher altitude is 345 for this airspace region). The number of cluster centres is equal to the number of real airspace sectors.

For the experiments presented in this paper, the air traffic movements are extracted from Eurocontrol DDR-2 data set for 12.07.2012 by RouGe and are divided into four time intervals given in hours of a day: \[0, 4\], \[4, 12\], \[12, 20\] and \[20, 24\] with centres at 0, 8, 16 and 24. The first and the last intervals are smaller because with 0, resp. 24, as centre they are extended to the time before and after the selected day (see, above), but only the traffic of the selected day is taken into account. When using interim diagrams, these time intervals are shortened for the main Voronoi diagrams and the selected number of interim diagrams is inserted (see, below).

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr11.jpg)

Download: Download high-res image (71KB)

As simulation setup for the evolutionary algorithm, a population size of 80 chromosomes was used and the number of generations to be simulated was set to 1000. Ten simulations were carried out for each sectorisation. The flights selected by RouGe are defined as a sequence of connected points $p \in \mathit{AS}_{B} \cup \mathit{AS}_{\mathit{IB}}$ (see and ). Tests for an appropriate set of simulation parameters (e.g. crossover and mutation rates) were presented by and result in a mutation probability of 5% and a crossover probability of 20%. The crossover probability can be much higher than for the mutation, because the exchanged section of a chromosome often has mainly the same genes (vertices) and therefore a substantial change of the solution takes place less often.

The evaluation value for the closeness of a chromosome consists of the sum of the *vertexCloseness* for all vertices. In addition, the weight factor $w_{\mathit{vc}}$ for the new part $E_{\mathit{vc}}$ of the evaluation function was investigated and set to three, when interim diagrams are in use (). Because the *vertexCloseness* is calculated as a penalty and not as criterion for exclusion, it is possible that the interim diagrams differ recognisably from the surrounding main diagrams if this is justified by better values for task load and task load standard deviation.

## 6\. Results

For a better understanding of the abilities and possibilities given by our tool chain (cf. ), we have selected four scenarios for comparison: the real sectorisation and its optimisation as well as an artificial Voronoi structure and its optimisation. The results are presented and compared in this section. Furthermore, the Voronoi sectorisation and its optimised version are used for the creation of interim diagrams with two inserted diagrams for each of the four main intervals. The results are analysed in regard to the overlapping airspace areas, respectively building blocks.

To obtain an impression of the differences between the calculated cluster centres for the Voronoi-based sectorisations, the mean cluster centres over all time intervals were calculated and compared to the cluster centres for each time interval (). For this comparison, the centres were associated to the closest centre mean. The highest difference was found for time interval 0. Nevertheless, for the historical flight data set, the traffic for the different time intervals was very similar, especially for time intervals one and two. They have the highest amount of traffic and therefore the centres are more stable than for intervals with lower traffic numbers.

Table 2. Position difference (distance) between centres for the selected time intervals (NM).

<table><thead><tr><th rowspan="2">Centre</th><th colspan="2">Mean</th><th colspan="4">Distances in time interval</th></tr><tr><th><em>x</em></th><th><em>y</em></th><th><em>0</em></th><th><em>1</em></th><th><em>2</em></th><th><em>3</em></th></tr></thead><tbody><tr><td>1</td><td>284.3</td><td>55.2</td><td>9.2</td><td>4.7</td><td>4.1</td><td>8.4</td></tr><tr><td>2</td><td>114.6</td><td>172.3</td><td>2.6</td><td>4.7</td><td>3.3</td><td>2.6</td></tr><tr><td>3</td><td>45.8</td><td>160.6</td><td>13.4</td><td>2.5</td><td>4.2</td><td>8.7</td></tr><tr><td>4</td><td>180.8</td><td>87.8</td><td>5.3</td><td>5.2</td><td>5.6</td><td>5.3</td></tr></tbody></table>

### 6.1. Optimisation of real sectorisation of EDYYDUTA

For this part of the experiment, a real sectorisation (baseline real sectorisation: **bRS**) of the upper airspace is used. Because optimising a real structure leads to a new configuration, this approach belongs to the DAC approaches. The selected airspace area EDYYDUTA consists of four sectors (airspace blocks) with a resulting number of 12 vertices for the inner structure (, black lines). Only these vertices undergo the optimisation process using the developed evolutionary algorithm (see ), which always starts with the same set of vertices for the different time intervals. Because one focus is set on the sequence of sectorisations for successive time intervals, the positions of these vertices are major parameters for similarity in the geometric shape of the sectors.

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr12.jpg)

Download: Download high-res image (221KB)

Since the optimisation of airspace sectors could result in different geometric shapes, but with same values for the evaluation function, the average position for each vertex was exemplarily calculated in ten simulation runs for the optimised real sectorisation (**oRS**). A typical result for one simulation run is shown in. The vertices are numbered and marked by red dots; the vertices 1, 4, 5, 9 and 12 are located at the boundary.

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr13.jpg)

Download: Download high-res image (58KB)

provides a more detailed analysis of the vertex positions. Here, the mean values for the vertices are shown as green circles, whilst the average values for the four time intervals are marked by rhombi. The comparison of (baseline layout) with (variation of optimised layouts) shows that the border between centre and right sector, formed by vertices one to four, is much straighter for **oRS** than for the baseline version **bRS** of EDYYDUTA (except time interval 0) when considering the mean values.

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr14.jpg)

Download: Download high-res image (111KB)

Nevertheless, the ellipsoids around each group of vertices showing the variability of solutions include possible vertex positions similar to the vertex positions of **oRS**. The same can be recognised for vertices eleven and twelve. Contrary to this, the positions of the vertices five to ten are very limited in their position variability and have a completely different position in comparison to the **bRS**. All of them moved to the southern part of EDYYDUTA, resulting in smaller sectors and automatically in a reduction of task load. The task load values for the different task load types (excluding clearances, which are not given in this sector type) are presented in and [^1] for **bRS** and **oRS** ().

Table 3. Task load average values **bRS** (s).

| Time Interval | Monitoring | Radio Telephony | Coordination | Conflict Search | Conflict Resolution |
| --- | --- | --- | --- | --- | --- |
| 0 | 22,727 | 7585 | 5669 | 1349 | 2920 |
| 1 | 44,020 | 14,767 | 11,428 | 1642 | 2287 |
| 2 | 48,200 | 15,768 | 12,081 | 1252 | 1095 |
| 3 | 22,068 | 7222 | 5593 | 1293 | 2878 |

Table 4. Task load average values **oRS** (s).

| Time Interval | Monitoring | Radio Telephony | Coordination | Conflict Search | Conflict Resolution |
| --- | --- | --- | --- | --- | --- |
| 0 | 22,904 | 7575 | 5638 | 1325 | 2927 |
| 1 | 44,057 | 14,478 | 11,220 | 1648 | 2340 |
| 2 | 47,376 | 15,445 | 11,831 | 1186 | 1023 |
| 3 | 21,741 | 7012 | 5422 | 1223 | 2757 |

The comparison of these values shows that they are very close together, but the **oRS** results are slightly better for most factors. The highest difference exists for monitoring for time interval two. Monitoring is carried out for sector entries on the one hand and as recurring monitoring every two minutes on the other. Therefore, a considerable reduction in these values is based on a reduced dissection of flights. A comparison of the factors of the evaluation function is presented in. This shows indeed that the number of flight intervals is lower for the **oRS** version and here especially for time interval two. A closer look at the main factor task load standard deviation reveals furthermore that there is a very high difference between both versions and that the optimisation has mainly reduced this value whilst stabilising the task load on a comparable value. The task load standard deviation was reduced to values between 0.5% for time interval three and 6.9% for time interval two. Only the result for the factor task load in time interval zero is better for **bRS** than for **oRS**. It is obvious that the baseline structure with twelve vertices has given AutoSec the possibility of an easier adaptation of the distribution of task load to the different sectors than for reducing the task load as well. This is not at least due to the expert knowledge already included in the baseline structure of EDYYDUTA. The values for the interior angle are only slightly better than the baseline results. This proves the similarity of sector forms for both versions, even if the sectors themselves have different sizes.

Table 5. Comparison of **bRS** and **oRS** for the factors of the evaluation function.

<table><thead><tr><th>Time Interval</th><th colspan="2">Task Load Sum [s]</th><th colspan="2">Task Load Std. Deviation [s]</th><th colspan="2">Interior Angle Std. Deviation [°]</th><th colspan="2">Flight Intervals [#]</th><th colspan="2">Std. Deviation Area [NM]</th></tr><tr><td>Empty Cell</td><th><em>bRS</em></th><th><em>oRS</em></th><th><em>bRS</em></th><th><em>oRS</em></th><th><em>bRSe</em></th><th><em>oRS</em></th><th><em>bRS</em></th><th><em>oRS</em></th><th><em>bRS</em></th><th><em>oRS</em></th></tr></thead><tbody><tr><td>0</td><td>40,251</td><td>40,370</td><td>3171</td><td>43.2</td><td>45.8</td><td>45.2</td><td>389.0</td><td>386.2</td><td>5621</td><td>6074</td></tr><tr><td>1</td><td>74,145</td><td>73,745</td><td>4841</td><td>111.0</td><td>45.8</td><td>44.5</td><td>762.0</td><td>749.1</td><td>5621</td><td>6178</td></tr><tr><td>2</td><td>78,397</td><td>76,863</td><td>3755</td><td>260.5</td><td>45.8</td><td>44.6</td><td>802.0</td><td>785.0</td><td>5621</td><td>5833</td></tr><tr><td>3</td><td>39,055</td><td>38,156</td><td>2865</td><td>13.8</td><td>45.8</td><td>45.0</td><td>384.0</td><td>373.0</td><td>5621</td><td>6453</td></tr></tbody></table>

The factor “Std. Deviation Area” was not part of the evaluation function but is included in for a better impression of the re-arrangement of sector sizes. The reduction in task load standard deviation is accompanied by an increase in the difference of sector sizes. Altogether, the results prove that AutoSec is able to improve a sectorisation whilst staying close to the original sectorisation, which is a satisfactory initial result. Thus, it would be possible to re-use existing sectorisations, e.g. from a set of typical sectorisations calculated before, as start solution for a new traffic situation without changing the structure too much. The additional workload for controllers for the transition period can be kept low. In a future air traffic scenario, such as avoidance of contrails, this means that it is possible to create a set of typical sectorisations, select the most suitable and apply AutoSec to provide an appropriate airspace structure. This would reduce the effort for the creation of sectorisations and ensure some similarities among successive sectorisations.

### 6.2. Optimisation of EDYYDUTA using dynamic airspace sectorisation

In contrast to **oRS**, where the optimisation for each time interval started with the same baseline structure, the structure for optimisation based on traffic cluster sectorisation (**oCS**) differs depending on the set of cluster points calculated by RouGe for each time interval. Therefore, this approach belongs to the DAS group. Nevertheless, for this example, the number of vertices for each time interval was the same. shows an example for an optimised sector structure for time interval two with six vertices.

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr15.jpg)

Download: Download high-res image (53KB)

The reduced number of vertices in comparison to **oRS** leads to a lower number of possibilities for sector forms. Therefore, it is much more difficult to justify the vertex positions in order to obtain good results for all parts of the evaluation function. In, the average vertex positions for each time interval and the mean overall time intervals are presented in the same way as for DAC in. Many of the vertices are very close together, but the results for vertices one, two and six show variations.

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr16.jpg)

Download: Download high-res image (90KB)

A closer look at the simulation result has shown that there are two equivalent solution types. Only the angle of the line between vertices one and two is different. The position of this line influences these three points and results in a very different distribution of task load and task load standard deviation for different optimisations. Nevertheless, the resulting sectorisations for the different time intervals are very similar in structure (see related ellipsoids in ). Therefore, no problems for controllers responsible for EDYYDUTA should occur when switching from one sectorisation to the next.

A closer look at the task load results presented in and [^2] reveals a considerable difference between baseline of traffic cluster based sectorisation (**bCS**) and optimised sectorisation (**oCS)**. Only the value of conflict resolution for time interval 1 is higher in **oCS** than the baseline result.

Table 6. Task load average values **bCS**.

| Time Interval | Monitoring | Radio Telephony | Coordination | Conflict Search | Conflict Resolution |
| --- | --- | --- | --- | --- | --- |
| 0 | 23,530 | 8114 | 5987 | 1464 | 3186 |
| 1 | 45,261 | 16,366 | 12,467 | 1686 | 2082 |
| 2 | 49,497 | 17,495 | 13,216 | 1345 | 1030 |
| 3 | 23,326 | 8457 | 6412 | 1332 | 2813 |

Table 7. Task load average values **oCS**.

| Time Interval | Monitoring | Radio Telephony | Coordination | Conflict Search | Conflict Resolution |
| --- | --- | --- | --- | --- | --- |
| 0 | 22,434 | 7289 | 5376 | 1291 | 2842 |
| 1 | 43,798 | 14,395 | 11,023 | 1630 | 2313 |
| 2 | 47,457 | 15,459 | 11,662 | 1163 | 963 |
| 3 | 21,915 | 7155 | 5472 | 1253 | 2804 |

This suggests that the evolutionary algorithm uses conflicts to balance the task load between sectors by placing a borderline close to a conflict and counting this conflict for each adjacent sector. To avoid this, the introduction of an additional parameter evaluating the number of conflicts for each sector or measuring the distance to the closest border will be part of further investigations.

The results for the factors of the evaluation function can be found in. The optimised results of the DAS approach for these factors are always better than the baseline results. For task load, they differ between approximately 3000 and 6000 s, and the task load standard deviation is reduced by more than 85% for each time interval. The optimisation functionality was able to reduce the main factors of the evaluation function significantly in spite of the low number of vertices and therefore borderlines. The dissection of flights was considerably reduced as well. This is another reason for the task load reduction, because the number of sector entries with its connected task load decreased. The highest value for the task load standard deviation for DAS can be found in time interval 2, together with the lowermost value for the area standard deviation, which is lower than the baseline value.

Table 8. Comparison of **bCS** and **o** **CS** for the factors of the evaluation function.

<table><thead><tr><th>Time Interval</th><th colspan="2">Task Load [s]</th><th colspan="2">Task Load Std. Deviation [s]</th><th colspan="2">Interior Angle Std. Deviation [°]</th><th colspan="2">Flight Intervals [#]</th><th colspan="2">Std. Deviation Area [NM]</th></tr><tr><td>Empty Cell</td><th><em>bCS</em></th><th><em>oCS</em></th><th><em>bCS</em></th><th><em>oCS</em></th><th><em>bCS</em></th><th><em>oCS</em></th><th><em>bCS</em></th><th><em>oCS</em></th><th><em>bCS</em></th><th><em>oCS</em></th></tr></thead><tbody><tr><td>0</td><td>42,282</td><td>39,235</td><td>3293</td><td>284</td><td>46.6</td><td>44.2</td><td>410.0</td><td>368.5</td><td>4014</td><td>4846</td></tr><tr><td>1</td><td>77,862</td><td>73,161</td><td>5629</td><td>344</td><td>46.9</td><td>44.4</td><td>829.0</td><td>736.4</td><td>4594</td><td>5170</td></tr><tr><td>2</td><td>82,583</td><td>76,706</td><td>5193</td><td>690</td><td>47.7</td><td>43.9</td><td>875.0</td><td>774.0</td><td>4457</td><td>4254</td></tr><tr><td>3</td><td>42,340</td><td>38,600</td><td>2923</td><td>438</td><td>46.6</td><td>44.9</td><td>437.0</td><td>376.5</td><td>4792</td><td>5443</td></tr></tbody></table>

### 6.3. Comparison and evaluation of simulation results

Within this section, a comparison of the results of optimised real and cluster-based sectorisation (**oRS**, **oCS**) is presented against corresponding baseline (**bRS**, **bCS**). The main difference between **bRS** and **bCS** lies in the higher number of vertices for DAC and the resulting lower flexibility for **bCS**. Whilst this leads to increased possibilities for creating different solutions with similar evaluation values for **oRS**, a higher number of vertices can, however, increase the search time and space. Since the **bRS** was created using expert knowledge, the larger search space can be compensated through a better start sectorisation and the results are much better than for **bCS**. Comparing the results for **bCS** in with the results for the **bRS** in shows immediately that **bRS** outperforms the DAS baseline for each factor and time interval, with the exception of the non-optimised standard deviation of the area. However, the results are close together, and this shows that even the optimised Voronoi diagram created for our DAS approach (which is **bCS**) can be used as a substitute for situations where no sectorisation created by experts exists or there is no time to create one by hand.

Because of the reduced number of vertices, the **oCS** sectorisation has a simpler structure than **oRS**. This is an advantage for situations where the sectorisation changes over time and controllers have to adapt their work procedures accordingly. Nevertheless, when comparing both elements of, it is easy to see that the rough structure is similar to but less sophisticated than **oRS**.

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr17.jpg)

Download: Download high-res image (68KB)

When comparing and, it is obvious that **oCS** tends towards a more stable distribution of vertex positions over the time intervals than **oRS**, caused by the higher number of vertices. For the task load types, the results are mixed and very close together for **oRS** and **oCS**, whilst both are better than **bCS**. For time interval three, task load values (monitoring, radio telephony, etc.) are higher for **oCS** than for **oRS**, resulting in a higher general task load value for time interval three. All other task load values are lower than the results for **oRS** ( and [^3]), but all values for the task load standard deviation are much higher than for **oRS**. So, the decrease of the task load is paid for with an increase in task load deviation as could be expected from the evaluation function (see Eq. ), where both factors are in conflict.

The optimisation process for **oRS** has used the better starting condition to focus on task load standard deviation instead of task load as is performed by **oCS**. Because the task load is strongly influenced by the form of the sectors and consequentially by the number of flight intervals, these results are also mostly better than the related oRS values.

### 6.4. Creation of building blocks

An important point for the applicability of a new concept is the amount of workload additionally created for the users of the system, e.g. the airspace controllers. Especially in the case of dynamic sectorisation, the extent of workload caused by the change in shape and position of the artificial sectors will influence the acceptance rate of this concept by airspace controllers. How the application of interim diagrams can help to cope with this problem is presented in this section.

Therefore, it is necessary to analyse the dissimilarity of subsequent sectorisations for a selected part of the airspace. Very important for such an analysis is the part of a sector which is the same for all subsequent time intervals. This main part can be seen as Sector Building Blocks (SBB), as described by. They describe the remaining airspace areas as Sharable Airspace Modules (SAM), because these parts of the airspace are shared amongst different sectors over the time. The idea of SBBs and SAMs will be applied to our DAS approach. Again, the EDYYDUTA airspace area is used with an **oCS** approach and the same parameters as for the preceding optimisation runs. To calculate these SBBs for EDYYDUTA, overlays for the sector shapes for each sector for all time intervals were created and the parts of the airspace shared by all time intervals were calculated. The result is used as SBB for each sector.

illustrates the results of an example optimisation for all sectors. The areas coloured with brighter shades of blue indicate that they are not occupied within all time intervals. The darker a colour is, the more sectors share this part of the airspace. The darkest areas are shared by all time intervals and can be seen as the SBBs mentioned before. Sectors zero and one have small overlapping areas, especially because both adjoin each other on the right, respectively left side. The overlapping areas to the south with sector three are obviously smaller than between zero and one. The SBBs for sectors two and three include more than 75% each of the area covered by all time intervals, which is a very good value. The percent values for the SBBs for all sectors are given in.

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr18.jpg)

Download: Download high-res image (150KB)

Table 9. Example of size of sector building blocks in percent.

| Empty Cell | Sector 0 | Sector 1 | Sector 2 | Sector 3 |
| --- | --- | --- | --- | --- |
| SBB (%) | 44.4 | 48.2 | 75.3 | 78.8 |

The area of sector zero coloured with the lightest blue is undesirably large for the transition from one time step to the next, whilst all other SAMs are of a sufficient size to be switched on or off in dependence on the time interval. The transition from SBB to a combination with this large SAM could provoke situations where an aircraft has just left a sector shortly before a sectorisation change and is sent back to the same controller after it. To avoid these situations, interim diagrams can be used. The transition to the addition of a large type of SAM is divided into more steps of smaller size. So, an aircraft moving through this large SAM would hopefully stay inside the subsequently added smaller SAMs. To demonstrate the application of interim diagrams, additional simulations were carried out. For these, the same sector (EDYYDUTA) was used together with the same flight schedule and simulation parameters, but each time interval was divided into three additional time intervals by adding two more interim diagrams (see ).

An example for the usage of interim diagrams is shown in for sector zero. On the left, the main time intervals \[0:00–1:20\], \[6:40–9:20\], \[14:40–17:20\] and \[22:40–24:00\] are shown (Main SBB). All diagrams including the newly created interim diagrams are on the right side (All SBB). It can be seen that there is a large increase in sector area between time intervals zero and one for the main intervals, which is successfully divided into smaller parts when using the interim diagrams.

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr19.jpg)

Download: Download high-res image (160KB)

The percent values of the SBBs’ sizes when overlapping all intervals are listed in (All SBB) as well as the percent values for overlapping of all main intervals (Main SBB). Furthermore, the values for each main interval with its adjacent interim diagrams, which are influenced by this main diagram (see ), are presented in this table. An example for such a combination of main and surrounding interim diagrams is the interval sequence \[4:00, 6:40\], \[6:40, 9:20\], \[9:20, 12:00\] with main interval \[6:40,9:20\], (cf. ).

Table 10. Example of size of sector building blocks in percent using interim diagrams.

| Sector | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| All SBB (%) | 41.5 | 21.1 | 55.7 | 78.1 |
| Main SBB (%) | 41.5 | 21.2 | 66.7 | 79.4 |
| \[0:00–4:00\] | 48.1 | 44.2 | 69.2 | 82.4 |
| \[4:00–12:00\] | 85.8 | 45.7 | 66.7 | 81.3 |
| \[12:00–20:00\] | 81.1 | 45.3 | 55.8 | 87.7 |
| \[20:00–24:00\] | 41.5 | 42.9 | 88.7 | 95.6 |

Some of the values for the Main SBB are higher than for the version using all SBBs, because the interim diagrams did not fully overlap the original shape of the main sectorisation. This is caused by optimising the interim diagrams as well instead of using the calculated intermediate vertices related to the surrounding main diagrams without adaptation. Without the optimisation, the interim diagrams would have been much more like intermediate steps and easier to handle and to understand by airspace controllers. However, it was shown in () that the optimisation was able to improve the sectorisation in relation to task load and task load standard deviation substantially. Therefore, a balance has to be found between a sector shape easily applicable by controllers and a sectorisation with good values for the parameters of the evaluation function. The results for each main interval plus the surrounding interim diagrams are always better than those for the average main intervals themselves. This demonstrates that the interim diagrams are able to include the SBB of the belonging main interval and to change only smoothly in the direction of the next main interval, which is the desired result.

shows the course of the size of the building blocks for each sector with increasing number of included time intervals in relation to the size of the overlay of all time intervals. It can be seen that this value is stable over many time intervals and the reduction between time steps (size of new SAM) is around ten percent at most. This proves that the introduction of interim diagrams leads to a set of stable building blocks and to sharable airspace modules of reasonable size which can be handled by controllers. Nevertheless, the degree of free optimisation for the interim diagrams steered by the parameter group $w_{\mathit{vc}} \cdot E_{\mathit{vc}}$ of the evaluation function representing the vertex closeness (see ) has to be tested in simulation trials in the future, as it is already scheduled in current and upcoming research projects.

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X18310520-gr20.jpg)

Download: Download high-res image (112KB)

## 7\. Conclusions and outlook

With our AutoSec approach, in particular the concepts of fuzzy clustering, Voronoi diagrams and evolutionary algorithms we developed an efficient approach to handle dynamic air traffic movements over the day of operations. Thus, we provide an appropriate airspace structure, which is generated automatically and considers the task load of airspace controllers (level and variation). AutoSec can be seen as an enabling technology for future flight-centric operations and multi-criteria optimisation.

We introduced our three-step approach of fuzzy clustering of traffic flows on the day of operations, generation of new sector structure based on Voronoi diagrams and application of evolutionary algorithm in order to adjust and optimise the new sector structure on dynamic air traffic demands. Therefore, we sufficiently solved the problem of non-convex boundaries and a smooth transition between two sectorisations for different air traffic demand. Within our developed simulation framework, we analysed a traffic sample of EDYYDUTA (EDYY Deco Sectors, Maastricht) area to allow a future comparison of our results with results conducted by. In particular, we addressed the optimisation of EDYYDUTA area based on the real sector structure and on our DAS approach.

The results are achieved by the simulation of real and optimised sectorisations (based on real sectors) as well as a completely new sectorisation approach (based on dynamic traffic demand), which allowed a comparison of the actual situation against the opportunities arising from dynamic, automated and optimised re-structuring. In the first case of optimising real sector structures, the application of the evolutionary algorithm improved the sectorisation (in particular task load variation) whilst staying close to the original shape of sectors. From an operational perspective, optimisation of existing sectorisations with regard to dynamic air traffic situations keeps additional workload for controllers low during transition between changing sectorisations. Using our AutoSec approach for initial sectorisation and optimisation, we found similar airspace structures for a four-sector environment with less-complex shapes (reduced number of vertices) and task load values on the same order of magnitude. Since the simplified shapes resulted in reduced design flexibility, the variance of task load increased. At this point, we have to mention that dependencies between real traffic samples and real sector shapes have not been taken into account. Furthermore, we demonstrated that AutoSec could be used as a substitute to provide (near-real) operational airspace structures for situations where no prior sectorisation exists. In addition, the detailed analysis of interim diagrams indicates that building blocks can be established which can be re-used to hold the work load for controllers at a reasonable level when changing from one sectorisation to the next.

Current research uses AutoSec to provide an operational platform for ecologically efficient operations (e.g. contrail avoidance) and urban airspace management. In the future, we will use AutoSec as a demonstration environment for a real controller environment, focussing on both operational requirements of controllers and future airspace/air traffic.

## References

## Glossary

Abbreviation

Description

A

Standard deviation of interior angles

*AS*

Rectangular portion of airspace

*AS <sub>B</sub>*

Point of airspace $AS$ on boundary $B$

*AS <sub>IB</sub>*

Point of airspace $AS$ inside boundary $B$

AutoSec

Automatic Sectorisation of airspace

*B*

Boundary of selected airspace region described as polygon

bCS

Baseline cluster based optimization

bRS

Baseline real sectorization

DAC

Dynamic Airspace Configuration

DAS

Dynamic Airspace Sectorisation

DCEL

Doubly Connected Edge List

*E <sub>i</sub>*, *i* ∈{ *TL*, *TLSD*, *A*, *FI*, *VC* }

Evaluation value for corresponding part of the evaluation function

*evalF*

Evaluation function for evaluating the quality of solutions

FI

Number of flight intervals over all sectors

FAA

Federal Aviation Authority

FAB

Functional Airspace Blocks

*gen <sub>max</sub>*

Maximum number of generations for the evolutionary algorithm

oCS

Optimised cluster based sectorisaton

oRS

Optimised real sectorisation

PrePro

Pre-Processor for AutoSec

RouGe

Route Generator

SAM

Sharable Airspace Modules

SBB

Sector Building Blocks

TL

Task load over all sectors

TLSD

Standard deviation of task load between sectors

*V <sub>i</sub>*

Voronoi diagram i

*V <sub>i</sub>* \[*j*\]

Vertex j of Voronoi diagram i

VC

Closeness of vertices

*w <sub>i</sub>*, *i* ∈{ *TL*, *TLSD*, *A*, *FI*, *VC* }

Weight for corresponding part of the evaluation function

[View Abstract](https://www.sciencedirect.com/science/article/abs/pii/S0968090X18310520)

[^1]: Table 4. Task load average values **oRS** (s).

| Time Interval | Monitoring | Radio Telephony | Coordination | Conflict Search | Conflict Resolution |
| --- | --- | --- | --- | --- | --- |
| 0 | 22,904 | 7575 | 5638 | 1325 | 2927 |
| 1 | 44,057 | 14,478 | 11,220 | 1648 | 2340 |
| 2 | 47,376 | 15,445 | 11,831 | 1186 | 1023 |
| 3 | 21,741 | 7012 | 5422 | 1223 | 2757 |

[^2]: Table 7. Task load average values **oCS**.

| Time Interval | Monitoring | Radio Telephony | Coordination | Conflict Search | Conflict Resolution |
| --- | --- | --- | --- | --- | --- |
| 0 | 22,434 | 7289 | 5376 | 1291 | 2842 |
| 1 | 43,798 | 14,395 | 11,023 | 1630 | 2313 |
| 2 | 47,457 | 15,459 | 11,662 | 1163 | 963 |
| 3 | 21,915 | 7155 | 5472 | 1253 | 2804 |

[^3]: Table 8. Comparison of **bCS** and **o** **CS** for the factors of the evaluation function.

<table><thead><tr><th>Time Interval</th><th colspan="2">Task Load [s]</th><th colspan="2">Task Load Std. Deviation [s]</th><th colspan="2">Interior Angle Std. Deviation [°]</th><th colspan="2">Flight Intervals [#]</th><th colspan="2">Std. Deviation Area [NM]</th></tr><tr><td>Empty Cell</td><th><em>bCS</em></th><th><em>oCS</em></th><th><em>bCS</em></th><th><em>oCS</em></th><th><em>bCS</em></th><th><em>oCS</em></th><th><em>bCS</em></th><th><em>oCS</em></th><th><em>bCS</em></th><th><em>oCS</em></th></tr></thead><tbody><tr><td>0</td><td>42,282</td><td>39,235</td><td>3293</td><td>284</td><td>46.6</td><td>44.2</td><td>410.0</td><td>368.5</td><td>4014</td><td>4846</td></tr><tr><td>1</td><td>77,862</td><td>73,161</td><td>5629</td><td>344</td><td>46.9</td><td>44.4</td><td>829.0</td><td>736.4</td><td>4594</td><td>5170</td></tr><tr><td>2</td><td>82,583</td><td>76,706</td><td>5193</td><td>690</td><td>47.7</td><td>43.9</td><td>875.0</td><td>774.0</td><td>4457</td><td>4254</td></tr><tr><td>3</td><td>42,340</td><td>38,600</td><td>2923</td><td>438</td><td>46.6</td><td>44.9</td><td>437.0</td><td>376.5</td><td>4792</td><td>5443</td></tr></tbody></table>