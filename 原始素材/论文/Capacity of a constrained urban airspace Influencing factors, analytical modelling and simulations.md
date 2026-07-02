---
title: "Capacity of a constrained urban airspace: Influencing factors, analytical modelling and simulations"
source: "https://www.sciencedirect.com/science/article/pii/S0968090X23001626?pes=vor&utm_source=clarivate&getft_integrator=clarivate"
author:
  - "[[airspace]]"
  - "[[Joost Ellerbroek]]"
  - "[[Victor L. Knoop]]"
published:
created: 2026-07-01
description: "The traffic density of small aerial vehicles operating within urban environments is expected to increase significantly in the near future. This urban …"
tags:
  - "clippings"
---
## Published by: Elsevier

### Published by

[![Elsevier](https://sciencedirect.elseviercdn.cn/prod/8c5bb82080b0f791d6ca95759147bab0d0e4e18d/image/elsevier-non-solus.svg)](https://www.sciencedirect.com/journal/transportation-research-part-c-emerging-technologies "Go to Transportation Research Part C: Emerging Technologies on ScienceDirect")

## FMS BEI检索SCI升级版 工程技术1区SCI Q1IF 8.4

,,

[View **PDF**](https://www.sciencedirect.com/science/article/pii/S0968090X23001626/pdfft?md5=79685327de53e5f84c733524e439f29e&pid=1-s2.0-S0968090X23001626-main.pdf)

[10.1016/j.trc.2023.104173](https://doi.org/10.1016/j.trc.2023.104173)

## Highlights

## Keywords

Constrained urban airspace

;

Decentralised airspace

;

Speed-based conflict resolution

;

Analytical model

;

Airspace capacity

;

Airspace stability

;

Urban traffic management (UTM)

;

BlueSky ATM simulator

;

Traffic simulation

- [Previous article in this issue](https://www.sciencedirect.com/science/article/pii/S0968090X23001651)
- [Next article in this issue](https://www.sciencedirect.com/science/article/pii/S0968090X23001614)

## Nomenclature

$a$

acceleration or deceleration capability \[m/s $2$\]

$c$

cycle time of a traffic signal \[s\]

$D$

flight distance, or leg length \[m\]

$d$

delay \[s\]

$F$

set of all legs $f$ at a single intersection

$k$

comparison scaling parameter \[m\]

$L$

queue length \[m\]

$N_{i}$

number of instantaneous aircraft \[–\]

$p$

proportion of aircraft passages \[–\]

$q$

flow rate \[s $−1$\]

$r$

red time of a traffic signal \[s\]

$S$

conflict-free flight distance between two aircraft \[m\]

$S_{h}$

horizontal separation requirement \[m\]

$s$

intersection flow capacity \[s $−1$\]

$t$

time \[s\]

$V$

aircraft speed \[m/s\]

$x$

[degree of saturation](https://www.sciencedirect.com/topics/engineering/degree-of-saturation) \[–\]

$Z$

set of all network legs $z$
### Superscripts:

$¯$

mean value of
### Subscripts:

$c$

of the crossing aircraft

$d$

downstream intersection leg

$E$

eastbound through flow

$EN$

east- to northbound turning flow

$f$

intersection leg

$g$

general (delay)

$i$

inflow (rate)

$l$

look-ahead

$N$

northbound through flow

$NE$

north- to eastbound turning flow

$NR$

without (no) conflict resolution

$s$

stochastic (delay)

$u$

upstream intersection leg

$z$

network leg

$λ$

proportion of time an intersection is free to cross

$ψ$

[ground track](https://www.sciencedirect.com/topics/physics-and-astronomy/ground-track) angle \[rad\]

$+$

crossing at right angles

$∠$

crossing at an angle

$∥$

originating from the same upstream leg

$%$

relative (comparison scaling parameter) \[%\]

## 1\. Introduction

In recent years, the development of [unmanned aerial vehicles](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/pilotless-aircraft) (UAVs) and personal aerial vehicles (PAVs) have been proposed as solutions for the increasing number of road congestion problems within cities. estimated that, even for a conservative growth rate, the traffic density of parcel and food delivery UAVs in the urban [airspace](https://www.sciencedirect.com/topics/physics-and-astronomy/airspace) of Paris would reach more than 60 thousand simultaneously operating vehicles by 2035. These numbers are substantially higher than current en-route [airspace](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/airspace) densities for conventional aviation (). Furthermore, the environment of the low-altitude urban airspace is highly constrained. Flying above existing infrastructures, such as roads and waterways, is desired to reduce exposure to the urban population (, ) or even unavoidable due to the presence of high buildings in the low-altitude urban airspace. The high level of aircraft density and the increased level of constraints are not found in regular, en-route airspace, raising the question of whether and how the constrained urban airspace can sustain such densities.

In previous studies, it has been shown that imposing some structure on an airspace can have beneficial effects on capacity and safety. and conclude that non-constrained airspace capacity benefits from a limited degree of structuring, namely, adding altitude layers with a reduced heading range. This vertical segmentation was confirmed to be beneficial as well for the constrained urban airspace (). The latter study also demonstrates the advantages of enforcing [unidirectional flows](https://www.sciencedirect.com/topics/physics-and-astronomy/laminar-flows) along streets, as opposed to allowing both directions (at different altitudes). Similarly, argued that a structured airspace design is a prerequisite to enable large-scale urban airspace operations, with follow-up research showing that the airspace should not be overly constrained (). In all studies mentioned, simulations are used to compare the different concepts for airspace structure. With simulations, we refer to a computer simulation of individual aircraft interacting with each other, in which their movements are determined by computer code (no human in the loop). In different fields, this is known under various names: fast-time simulations, agent-based simulations or microscopic simulations. In this paper, we will simply use the word “simulations” for this.

Up to now, the simulations are empirical in nature (i.e., they are applied to specific conditions), which limits their use beyond the specific conditions tested (). Notably, restricted airspaces are not well studied. At the moment, it is unknown which parameters influence traffic operations or road capacity. This is addressed in the current paper. We follow the approach suggested by, to create a mathematical model using an analytical approach that can quantify the factors influencing the capacity of constrained urban airspace. The suggested approach is based on conflict count models and [domino effect](https://www.sciencedirect.com/topics/engineering/domino-effect) models as predictors of airspace capacity.

This study will hence investigate the factors that influence the capacity of constrained urban airspace. An analytical method is proposed that estimates the relationship between the mean [inflow rate](https://www.sciencedirect.com/topics/engineering/inflow-rate) and the [mean density](https://www.sciencedirect.com/topics/physics-and-astronomy/mean-matter-density), for which we use a two-dimensional, orthogonal grid network airspace. As a result, the effect of several airspace design parameters on constrained urban airspace capacity can be quantified. These insights can be used in urban airspace design applications. They can also provide a basis for the derivation of more expanded models, enabling an increased comprehension and modelling of the constrained urban airspace.

This paper continues by presenting the techniques available to model airspace capacity, followed by the definitions and technical terminology we will be using in Section. Subsequently, Section elaborates on the interactions between aircraft in a constrained urban environment, laying the groundwork for the derivation of the analytical model in Section. Next, by means of a simulation experiment, the level of accuracy of the analytical model is assessed. The experimental setup thereof is discussed in Section, and the empirical results of these simulation experiments are compared to the predictions of the analytical model in Section. In Section, we discuss the level of accuracy of the derived model, its limitations, and key findings and limitations of this study. Additionally, opportunities for future research are presented. Finally, the main conclusions are summarised in Section.

## 2\. Models for airspace capacity

For free, unconstrained [airspace](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/airspace), several analytical models of [airspace](https://www.sciencedirect.com/topics/physics-and-astronomy/airspace) capacity exist. These models relate capacity to airspace stability and conflict probability, using binomial combinatorics-based equations. They are typically referred to as ‘gas model’ equations and have been proposed in aviation research since the late 1960s (,,,,,,,, ). These also are proposed as dynamic discrete-time simulation models (e.g., ). They have various applications, including traffic control (e.g.,, ). These models rely on several assumptions, such as a uniform distribution of traffic and flight direction, which make them not suitable for constrained urban airspace.

In a constrained environment, the limited horizontal manoeuvre space prevents [lateral resolution](https://www.sciencedirect.com/topics/engineering/lateral-resolution) manoeuvres. Moreover, when traffic is distributed across altitude layers of different speed or [heading directions](https://www.sciencedirect.com/topics/engineering/heading-direction), as advocated by,,,, vertical resolution possibilities are limited. As a result, of the three available en-route conflict resolution options (), this paper will focus on speed-based algorithms. Similar to the analytical models of,, strategic conflict resolution, also called pre-departure conflict resolution, will not be considered. Therefore, importantly, in this paper we consider tactical, en-route conflict resolution to be performed using speed-based algorithms.

An emergent behaviour resulting from speed-based resolution manoeuvres in a constrained environment is that aircraft queue upstream of busy intersections. In other words, within an airway, an aircraft can be in continuous conflict with the aircraft directly in front of it. The essentially one-dimensional nature of traffic following a street will cause knock-on conflicts to be much more commonplace, which reduces the value of conflict count models and [domino effect](https://www.sciencedirect.com/topics/engineering/domino-effect) models as predictors of airspace capacity. Furthermore, as concluded by, the accuracy of their earlier proposed analytical model () degrades when creating artificial ‘hotspots’ with a higher traffic density. Constrained urban airspace is a clear example of an environment with many hotspots, as traffic can become concentrated on busy streets and intersections. Altogether, the existing analytical models are not valid for constrained urban airspace, signifying the need for a tailored analytical model.

While constrained urban airspace has different characteristics than non-constrained airspace, it has many similarities with road transportation environments. This makes road transportation research an obvious inspiration for capacity modelling of constrained urban airspace. Similar to our observation above about knock-on conflicts in streets, road transportation research also seldom considers conflicts. Instead, network efficiency and instability are extensively investigated. Recent research in urban road transportation has focused on the relationship between the mean [inflow rate](https://www.sciencedirect.com/topics/engineering/inflow-rate) and the [mean density](https://www.sciencedirect.com/topics/physics-and-astronomy/mean-matter-density) in a network (,,, ). This relationship is expressed in the so-called Macroscopic Fundamental Diagram (MFD), which has been experimentally confirmed in a study on actual road traffic in Yokohoma, [Japan](https://www.sciencedirect.com/topics/engineering/japan) () and various other cities since. See for a comparison of 41 cities. Using the MFD, the behaviour of a [road network](https://www.sciencedirect.com/topics/engineering/road-network) can be observed, such that the traffic status (free-flow or congestion), critical density, and efficiency are identified.

As aircraft behaviour shows many similarities to road traffic behaviour in constrained urban environments, the adaptation of the Macroscopic Fundamental Diagram to assess constrained urban airspace has potential and will hence be explored here. This has had some first exploration based on particular conflict avoidance using simulations (e.g.,,, ). In the current paper, we will combine simulations and analytical approaches for constraint environments. Furthermore, we will focus on the free-flow part and the critical density point of the MFD. The congestion part is assumed less relevant for air traffic operations, as the regulated inflow means congestion can be avoided.

## 3\. Conflicts, intrusions and their resolution

This section explains conflicts, intrusions, and the tactical conflict resolution methods used in this paper.

An *intrusion*, also called loss of separation, occurs when two aircraft simultaneously violate the minimum horizontal and vertical separation requirements. In this paper, an aircraft is assumed to be any small flying vehicle with hovering capabilities, e.g., [UAVs](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/pilotless-aircraft), PAVs, or helicopters. When an intrusion is predicted to occur within a predetermined look-ahead time, this is called a *conflict*. The difference between conflicts and intrusions is shown in. By definition, conflicts and intrusions are pairwise, i.e., between two aircraft only.

To prevent intrusions, most research in urban airspace either makes use of pre-departure separation (, ) or of en-route decentralised air traffic management (ATM) performed by each aircraft autonomously (,, ). The model derivations in this study assume decentralised tactical separation management, based on state-based *conflict detection* and speed-based *conflict resolution*. With state-based conflict detection, aircraft positions are linearly extrapolated along the [velocity vector](https://www.sciencedirect.com/topics/engineering/velocity-vector) to detect conflicts within a given look-ahead time. Note that, when using state-based detection, changes in state, such as turns and accelerations are not predicted. It is assumed, however, that aircraft have perfect knowledge of their own and others’ current state. In reality, the accuracy of this state information can be considered in the design choice for the horizontal and vertical separation requirements, to prevent inaccuracies from resulting in collisions.

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X23001626-gr1.jpg)

Download: Download high-res image (103KB)

Upon detection of a conflict, an aircraft will perform tactical conflict resolution to avoid the predicted intrusion. As mentioned in the introduction, speed-based conflict resolution algorithms are used. The implementation of speed-based conflict resolution means that airways can be one-way only (per altitude level), as head-on conflicts are not resolvable.

Moreover, analogous to road transportation networks, [speed limits](https://www.sciencedirect.com/topics/engineering/speed-limit) are possibly applied in specific airways or locations. It is assumed that all aircraft will fly at equal cruise speed $V_{N R}$ when no conflict resolution (NR) would be used, likely close to such a speed limit. Already, the FAA proposed a speed limit for small [UAVs](https://www.sciencedirect.com/topics/physics-and-astronomy/pilotless-aircraft) of $45m/s$ (). In addition, the International Rules of the Air () define that an overtaking aircraft has to give right-of-way to the aircraft being overtaken. Due to both reasons, the resolution of a conflict by accelerating is assumed infeasible in a two-dimensional constrained environment. Hence, the speed with conflict resolution (WR) $V_{W R}$ will always be lower than the cruise speed. By assuming hovering capabilities for all aircraft, the lower bound equals $0$, and the range of $V_{W R}$ is: (1) $V_{W R} \in \left[\right. 0 , V_{N R} 〉$

For conflicts within an airway, the speed-based algorithm used follows the International Rules of the Air (), dictating that an aircraft overtaking another aircraft needs to give way. For crossing conflicts, the aircraft which has to incur the slightest delay will perform the resolution. This aircraft is the aircraft that crosses on the rear-side of the other aircraft, i.e., the aircraft which, at the closest point of approach, has a relative bearing with the other aircraft in the range of $[−90°,90°]$.

## 4\. Aircraft interactions in a constrained environment

In a constrained airspace, the interactions between aircraft differ from the interactions encountered in a non-constrained environment. By analysing these interactions, several assumptions can be made which facilitate the derivation of an analytical model for the relationship between the mean inflow rate and the aircraft density. These assumptions relate to the maximum throughput capacity of a single intersection, which is an input for the analytical model. Additionally, the theoretical upper bounds for the aircraft density are set by the assumptions made in this section.

This section presents several aircraft interactions that can be identified in a two-dimensional (i.e., all aircraft fly at the same altitude level) constrained urban airspace environment. For demonstration purposes, an orthogonal intersection of two one-way airways will be used. At this single orthogonal intersection, two types of traffic are distinguished. *Through traffic* represents the set of aircraft that continues on a straight path, whereas *turning traffic* represents the set of aircraft that turns onto the other airway. Firstly, the effect of the interaction between through traffic of two flows crossing a single intersection is evaluated. Next, the additional effect of turning traffic interacting with through traffic at this single intersection is analysed. Finally, the resulting macroscopic interactions due to speed-based conflict resolution manoeuvres in an orthogonal grid network environment are examined. The emergent behaviour of the aircraft flow, including queuing for intersections, demonstrates the motivation for a delay model, which will be derived in Section.

### 4.1. Interaction between through traffic of two flows crossing a single intersection

Consider an intersection of two one-way airways, with through traffic only. A difference exists in the [minimum separation distance](https://www.sciencedirect.com/topics/engineering/minimum-separation-distance) between two aircraft coming from the same upstream leg and between two aircraft coming from different upstream legs. This difference has a significant impact on the maximum throughput capacity of an intersection, as an increased separation margin means that fewer aircraft can cross within the same time window. The increase in minimum separation distance is illustrated in.

In, to remain conflict-free, aircraft B must follow aircraft A at a distance of at least the horizontal separation requirement $S_{h}$. This safe distance is named the conflict-free flight distance $S_{\angle}$ and is geometrically defined as a function of the absolute difference in [ground track](https://www.sciencedirect.com/topics/engineering/ground-track) angle $|Δψ|$ at the intersection: (2) $S_{\angle} \left(\left|\Delta \psi\right|\right) = \frac{S_{h}}{cos \left(\left|\Delta \psi\right| / 2\right)}$ By using this equation, the minimum separation distance $S_{\parallel}$, shown as the orange bar in, between subsequent aircraft coming from the same leg can be determined: (3) $S_{\parallel} = S_{\angle} \left(0\right) = S_{h}$

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X23001626-gr2.jpg)

Download: Download high-res image (283KB)

In the situation where two aircraft originate from different upstream legs, the conflict-free flight distance increases. This situation is visualised in, where the orange bar represents the minimum separation distance $S_{+}$ for aircraft coming from different upstream legs. In this figure, the conflict-free flight distance is increased to the distance B $→$ I $→$ A, with I signifying the intersection midpoint. For an orthogonal intersection, by applying Eq., $S_{+}$ equals: (4) $S_{+} = S_{\angle} \left(\pi / 2\right) = S_{h} \sqrt{2}$

In summary, after a crossing aircraft of the other airway, the subsequent aircraft needs to keep a separation distance over the path of at least $S_{h} \sqrt{2}$. However, following a through aircraft of its own airway, a margin of $S_{h}$ suffices. Therefore, it is assumed that:

**Assumption 1**

When the origin leg of the crossing traffic at an intersection alternates less often between both upstream legs, intersection throughput capacity can be increased compared to an intersection with perfectly alternating upstream legs.

### 4.2. Interaction of turning traffic with through traffic on a single intersection

Continuing with the analysis of a single intersection of two one-way airways, turning traffic is added next to the through traffic. Two situations are considered that affect the maximum throughput capacity: either (1) turning aircraft A is in the airway of aircraft B and turning onto the crossing airway, or (2) turning aircraft A is on the crossing airway and merging into the airway of aircraft B. Note that the turns of turning traffic are not predicted by the state-based conflict [detection algorithm](https://www.sciencedirect.com/topics/engineering/detection-algorithm) used in this paper. Additionally, aircraft are assumed to not have to decelerate during a turn.

For the first case, aircraft B can follow aircraft A conflict-free at a distance of $S_{\parallel}$ of Eq. within the airway. As both aircraft have the same [airspeed](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/airspeed), no conflict is detected. This situation is equivalent to the situation illustrated in. However, when aircraft A, instead of continuing through, has turned, a similar situation as visualised in occurs (although aircraft A originated from the bottom leg instead of the left leg). As a result, aircraft B in fact needs to keep a margin equivalent to $S_{+}$ of Eq.. Hence, when the two aircraft are following each other more closely than $S_{+}$ within the airway, the leading aircraft A will provoke a conflict with B by turning. Therefore, each aircraft trailing a turning aircraft within a distance $S_{+}$ needs to decelerate and increase its distance to $S_{+}$ to resolve the conflict. In other words, this case of turning traffic has a decreasing effect on the intersection throughput capacity for aircraft coming from the same upstream leg.

In the second situation, the opposite occurs. Aircraft B coming from the bottom leg approaches the intersection and expects aircraft A coming from the left leg to continue straight, see. As a result, aircraft B predicts an intrusion will occur when its minimum separation distance is smaller than $S_{+}$. Yet, when aircraft A, instead of going straight, turns upwards into the airway of aircraft B, the intrusion will only occur when the minimum separation distance is smaller than $S_{\parallel}$. In other words, by turning, aircraft A moves its closest point of approach away from aircraft B and aircraft B can reduce its conflict-free distance from $S_{+}$ to $S_{\parallel}$. As such, each aircraft performing a turn has an increasing effect on the intersection throughput capacity for aircraft coming from the alternating upstream leg.

When the flow rates from both upstream legs are approximately identical, the first situation occurs equally often as the second situation. In addition, the magnitude of change in conflict-free distance is equal, with the sign reversed. Hence, both effects counterbalance each other, resulting in the following assumption:

**Assumption 2**

Through traffic and turning traffic have an equal impact on the intersection throughput capacity when both upstream flow rates are approximately equal.

In this analysis, it is assumed that aircraft do not decelerate to perform a turn. If this is not the case, an additional delay needs to be modelled per turning aircraft, and turning traffic will have a decreasing impact on maximum throughput capacity compared to through traffic. To prevent this, future airspace designs could implement solutions such as separate altitude layers dedicated to turning traffic (), similar to turning lanes in road traffic.

### 4.3. Macroscopic interactions due to conflict resolution in constrained urban airspace

In constrained urban airspace, three [macroscopic properties](https://www.sciencedirect.com/topics/engineering/macroscopic-property) due to speed-based conflict resolution need to be considered. The first property, an increase in aircraft density, demonstrates the choice for an analytical delay model as the main input in the relationship between the mean inflow rate and the aircraft density. The second property, a queuing effect, defines an upper bound to the stability of a constrained airspace. This is used as an upper bound in the analytical model as well. The third property is a structuring effect, which assesses the impact of clustered aircraft on the analytical model.

Firstly, an increase in density occurs in a speed-based conflict resolution environment, as aircraft resolve conflicts by decelerating, thereby extending their flight time. This increase can be expressed analytically, starting from the (hypothetical) mean number of instantaneous aircraft without conflict resolution $\bar{N}_{i , N R}$. $\bar{N}_{i , N R}$ and the mean inflow rate $\bar{q}_{i}$ are related through the mean flight duration (which equals the mean flight distance $\bar{D}$ divided by the cruise speed $V_{N R}$): (5) $\bar{N}_{i , N R} = \frac{\bar{D}}{V_{N R}} \bar{q}_{i}$

Aircraft routes and departure times are not impacted by the speed-based conflict resolution used in this paper. Therefore, in a stable situation, an equal number of aircraft depart, arrive or pass an intersection per unit of time, regardless of whether or not conflict resolution is used. Hence, the mean inflow rate $\bar{q}_{i}$ is unchanged.

The mean [airspeed](https://www.sciencedirect.com/topics/physics-and-astronomy/airspeed) with conflict resolution $V_{W R}$ can be extracted using the increased mean flight duration, which is the sum of the no-resolution flight duration and the mean delay $\bar{d}$: (6) $V_{W R} = \frac{\bar{D}}{\frac{\bar{D}}{V_{N R}} + \bar{d}}$

Subsequently, the actual density, expressed as the mean number of instantaneous aircraft with resolution $\bar{N}_{i , W R}$, is given by substituting $V_{N R}$ with $V_{W R}$ of Eq. into Eq.: (7) $\bar{N}_{i , W R} = \frac{\bar{D}}{V_{W R}} \bar{q}_{i} = \left(\frac{\bar{D}}{V_{N R}} + \bar{d}\right) \bar{q}_{i}$ The mean route length $\bar{D}$, the cruise speed $V_{N R}$, and the mean inflow rate $\bar{q}_{i}$ are assumed to be known input variables. Thus, the mean delay $\bar{d}$ is the only unknown variable required to obtain the mean density and, thereby, to express the entire relationship between the mean flow rate and the mean density. This will be the starting point in the model derivation in the next section.

Secondly, within airways, a queuing effect can occur. While one aircraft waits for a crossing aircraft, another aircraft coming from upstream in the same airway approaches the waiting aircraft and forms a queue, increasing the density locally. When a queue gets longer, it can start to interfere with upstream intersections. This interference is visualised in. In this figure, intersection A is operating above its capacity limit. As a result, not all aircraft can cross the intersection, blocking the aircraft in the northbound leg, with the queue overflowing to the upstream intersection B. In turn, this queue blocks all traffic in the westbound airway upstream of intersection B.

In other words, queuing has a destabilising effect on the network flows, as more and more intersections become occupied by the queuing aircraft, blocking all flows at those intersections. Finally, the entire airspace becomes ‘gridlocked’, as the speed of all aircraft equals $0m/s$ and the aircraft are unable to reach their destination. Therefore, it is assumed that once a queue reaches an upstream intersection, the airspace becomes unstable:

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X23001626-gr3.jpg)

Download: Download high-res image (233KB)

**Assumption 3**

Once the mean queue length within a leg of an intersection is longer than the distance to the upstream intersection of that leg, the airspace becomes unstable.

Due to stochastic effects, the queue length varies and is longer than the mean length at particular intervals. As a result, the network can already become unstable at a lower inflow rate than at the inflow rate needed for the mean length of. The assumption is, therefore, expected to overestimate the instability density. Nevertheless, is an effective metric to use as a theoretical maximum capacity limit for a given constrained urban airspace, similar to the stability metric defined by for general airspace.

Thirdly, a structuring effect is present. While an aircraft is waiting for a crossing aircraft, a queue forms behind this aircraft. Once the intersection becomes free to cross, the queued aircraft continue their flight bunched together. In other words, aircraft get structured into *platoons* of multiple aircraft following each other closely. These platoons can impact the mean delay incurred at downstream intersections. Namely, a platoon of multiple aircraft can either fit in a relatively tinier gap, decreasing the mean delay for the aircraft in the platoon, or be blocked entirely, increasing the mean delay for the platoon. Furthermore, in this paper, traffic at the intersection adheres to the first-come, first-serve principle because no systems are present to limit flow alternation. Therefore, delay periods are limited to a single crossing aircraft, reducing the size of platoons. Altogether, the effect is assumed negligible for all densities:

**Assumption 4**

The structuring effect has a negligible impact on the mean delay for all airspace densities.

## 5\. Analytic computations for a constrained urban airspace

We will now first derive an analytical delay model for a single intersection of a two-dimensional orthogonal grid network. This model is based on an analytical delay model for road transportation research and subsequently adjusted to constrained urban airspace. Secondly, combining this delay model and Eq., we approximate the relationship between the mean inflow rate and the mean density in constrained urban airspace. This yields an expression similar to the free-flow part of the Macroscopic Fundamental Diagram. Thirdly, we will comment on airspace stability based on queue lengths, which are used to approximate the [transition point](https://www.sciencedirect.com/topics/physics-and-astronomy/transition-point) of the MFD.

For the models in this paper, we assume that a speed-based conflict resolution algorithm is used, which resolves conflicts by decelerating for a particular period. This way, each conflict results in a delay incurred by a single aircraft.

As a known input variable, we use the mean inflow rate of aircraft in the network $\bar{q}_{i}$. Together with a known routing distribution and an average route length, this variable can be translated to a mean flow rate in an intersection leg $\bar{q}_{f}$: (8) $\bar{q}_{f} = \bar{q}_{i} \frac{\bar{D}}{D_{f}} p_{f}$

In this equation, $p_{f}$ represents the proportion of aircraft passages through this leg over the sum of all leg passages. $D_{f}$ is the length of the leg, and $\bar{D}$ the mean flight distance.

### 5.1. Analytical delay model

Consider the single, same-level, orthogonal intersection with area $A$ of a northbound and an eastbound airway as shown in. Turning onto the other airway is allowed. Therefore, across the intersection, four possible flows exist: an eastbound (E) through flow, a northbound (N) through flow, an east- to northbound (EN) turning flow, and a north- to eastbound (NE) turning flow. These are further grouped into a set of the two upstream legs $u$, with mean flow rates $\bar{q}_{E} + \bar{q}_{E N}$ and $\bar{q}_{N} + \bar{q}_{N E}$, and a set of the two downstream legs $d$, with mean flow rates $\bar{q}_{E} + \bar{q}_{N E}$ and $\bar{q}_{N} + \bar{q}_{E N}$, respectively. The set of all legs $F$ represents the union of the sets of upstream and downstream legs.

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X23001626-gr4.jpg)

Download: Download high-res image (97KB)

#### 5.1.1. Analytical delay in road transportation

Such an intersection has many similarities with signalised intersections found in road transportation. Therefore, as a starting point in the derivation of the delay model, we use Webster’s model for delays at signalised intersections (): (9) $\bar{d} = \underset{1 st \text{term}}{\underset{︸}{\frac{c \left(1 - \lambda\right)^{2}}{2 \left(1 - \lambda x\right)}}} + \underset{2 nd \text{term}}{\underset{︸}{\frac{x^{2}}{2 \bar{q} \left(1 - x\right)}}} - \text{empirical correction factor} \left(\approx 5 \%– 15 \%\right)$ In this equation, the mean delay incurred in an upstream leg $\bar{d}$ is approximated by two terms, and a correction factor. The first term models the general delay, which is incurred when traffic arrives at a red signal at a constant rate. The second term models the stochastic delay, representing the incurred delay due to the random nature of the separation between consecutive arrivals. A correction factor is included to match the experimental road traffic data found by. In this paper, the empirical correction factor is not used, since there is no experimental data to match. Therefore, the mean delay of aircraft in an upstream leg, $\bar{d}_{u}$ is given by the sum of the mean general delay $\bar{d}_{g , u}$ and the mean stochastic delay $\bar{d}_{s , u}$: (10) $\bar{d}_{u} = \bar{d}_{g , u} + \bar{d}_{s , u}$

#### 5.1.2. Analytical delay in constrained urban airspace

To compute the mean density in constrained urban airspace, first, the mean general delay in an upstream leg $\bar{d}_{g , u}$ is approximated. At the intersection of, when assuming that the two flows are perfectly balanced, the maximum number of aircraft that can cross per unit of time is called the flow capacity $s$ of the intersection. This is different per angle of the crossing flow. Therefore, we split the analysis between aircraft crossing at right angles (denoted by subscript $+$) and aircraft crossing after each other originating from the same airway (denoted by subscript $∥$). $s_{+}$ is the inverse of the time a crossing aircraft needs to clear the intersection for the alternating leg completely, denoted by $t_{+}$. Without other conflicts, $t_{+}$ is given by: (11) $t_{+} = \frac{S_{+}}{V_{N R}}$ Hence, for any two crossing flows flying at equal speed, denoted $V_{N R}$, $s_{+}$ can be expressed as: (12) $s_{+} = \frac{1}{t_{+}} = \frac{V_{N R}}{S_{h} \sqrt{2}}$ Recall that the separation distance $S_{+}$ assumes that the flows are perfectly alternating. When the flows are not perfectly alternating, the mean distance decreases. Therefore, the time to cross $t_{+}$ is predicted to be underestimated at regular intersections.

In this paper, no traffic signal is used. Instead, the red signal time $r$ used in the derivation of Webster’s model can be replaced by the time $t_{+}$ with which a crossing aircraft occupies the intersection. This ‘red time’ happens at a mean cycle time $\bar{c}_{u}$ equivalent to the mean time window between two consecutive aircraft within a crossing flow (i.e., the flow originating from the other upstream leg), in [traffic engineering](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/traffic-engineering) also known as time headway. This time window is inversely proportional to the mean crossing flow rate $\bar{q}_{c}$, meaning that: (13) $r = t_{+}$ (14) $\bar{c}_{u} = 1 / \bar{q}_{c}$ Hence, the mean proportion of time $\bar{\lambda}$ that the traffic in an upstream leg $u$ perceives the intersection to be free to cross, equals: (15) $\bar{\lambda}_{u} = 1 - \frac{r}{\bar{c}_{u}} = 1 - t_{+} \bar{q}_{c}$

When an intersection is free to cross, two aircraft coming from the same upstream leg can cross with a minimum separation time window equal to $t_{\parallel}$: (16) $t_{\parallel} = \frac{S_{\parallel}}{V_{N R}}$ Accordingly, the maximum airway flow capacity $s_{\parallel}$ is inversely proportional to $t_{\parallel}$: (17) $s_{\parallel} = \frac{1}{t_{\parallel}} = \frac{V_{N R}}{S_{h}}$

Lastly, the mean ratio of the actual flow to the maximum flow which can pass through an intersection from the upstream leg is called the [degree of saturation](https://www.sciencedirect.com/topics/engineering/degree-of-saturation) $\bar{x}_{u}$ and is given by (): (18) $\bar{x}_{u} = \frac{\bar{q}_{u}}{\lambda_{u} s_{\parallel}}$

We can now obtain an expression for the mean general delay incurred in an upstream leg $\bar{d}_{g , u}$, by substituting all variables defined above into the first part of Eq.: (19) $\bar{d}_{g , u} = \frac{\bar{c}_{u} \left(1 - \bar{\lambda}\right)^{2}}{2 \left(1 - \bar{\lambda} \bar{x}\right)} = \frac{\left(1 - t_{+} \bar{q}_{c}\right)^{2}}{2 \bar{q}_{c} \left(1 - t_{\parallel} \bar{q}_{u}\right)}$

Next, the mean stochastic delay in an upstream leg $\bar{d}_{s , u}$ is derived. It concerns the flow within an airway, as it models the delay incurred due to queuing for a waiting aircraft. By inserting Eq. into the second part of Eq., the single intersection airspace version of $\bar{d}_{s , u}$ is obtained: (20) $\bar{d}_{s , u} = \frac{\bar{x}_{u}^{2}}{2 \bar{q}_{u} \left(1 - \bar{x}_{u}\right)}$

With expressions for both the mean general delay (Eq. ) and the mean stochastic delay (Eq. ), the mean delay incurred by an aircraft in an upstream leg can be determined using Eq.. As aircraft in the downstream legs $d$ do not encounter any conflicts, no delay is incurred after crossing. Hence, the final set of delay equations is: (21) $\bar{d}_{u} = \frac{\left(1 - t_{+} \bar{q}_{c}\right)^{2}}{2 \bar{q}_{c} \left(1 - t_{\parallel} \bar{q}_{u}\right)} + \frac{\bar{x}_{u}^{2}}{2 \bar{q}_{u} \left(1 - \bar{x}_{u}\right)}$ (22) $\bar{d}_{d} = 0$

### 5.2. Analytical free-flow model

The second goal is to get to the relationship between the mean inflow rate $\bar{q}_{i}$ and the mean density $\bar{N}_{i , W R}$ for the entire airspace. This requires completing Eq.. As mentioned, the mean delay $\bar{d}$ was the only unknown variable. In the previous section, we derived an equation for the delay in a single intersection leg. Therefore, we can apply Eq. on a single leg and obtain the mean density in this leg. Recall that using Eq., we could transform the mean inflow rate $\bar{q}_{i}$ into the flow rate in a single leg $\bar{q}_{f}$.

By applying Eq. to each leg $f$ of a single intersection, the mean number of instantaneous aircraft with resolution at this intersection $\bar{N}_{i , W R , +}$ can be derived to be: (23) $\bar{N}_{i , W R , +} = \underset{f \in F}{\sum} \bar{N}_{i , W R , f} = \underset{f \in F}{\sum} \left(\frac{D_{f}}{V_{N R}} + \bar{d}_{f}\right) \bar{q}_{f}$

Under, Eqs. to are valid for intersections with and without turning traffic. Also, all interactions between intersections are either assumed negligible () or limiting for the entire airspace (). Hence, the mean number of instantaneous aircraft with resolution in the grid network can be obtained by summing $N_{i , W R}$ per leg $z$ for the set of all legs $Z$ in the network: (24) $\bar{N}_{i , W R , g r i d} = \underset{z \in Z}{\sum} \bar{N}_{i , W R , z} = \underset{z \in Z}{\sum} \left(\frac{D_{l}}{V_{N R}} + \bar{d}_{z}\right) \bar{q}_{z} = \bar{q}_{i} \bar{D} \underset{z \in Z}{\sum} \left(\frac{D_{z}}{V_{N R}} + \bar{d}_{z}\right) \frac{p_{z}}{D_{z}}$

By substituting Eqs., into Eq., the complete relationship between the mean inflow rate and the mean density in the airspace is derived. This relationship is similar to the free-flow part of the Macroscopic Fundamental Diagram used in road transportation research. As such, it can be used by future urban airspace designers to assess the capacity of a constrained urban airspace.

Additionally, following, the derived analytical delay model is assumed to act as an upper bound to the experimental mean delay, due to the overestimation of the time $t_{+}$ with which a crossing aircraft occupies an intersection. This overestimation is increased when more aircraft from the same origin leg cross without alternating with traffic from the crossing leg, i.e., for increasing density or flow ratio unbalance.

### 5.3. Airspace capacity measure

We are interested in the theoretical capacity (i.e., the maximum stable flow) and the factors influencing this. To obtain a measure of the [transition point](https://www.sciencedirect.com/topics/engineering/transition-point) between free-flow (stable) and congestion (unstable), we approximate a measure of stability based on the mean queue length (in meters) $\bar{L}$, as stated by. The mean queue length in a leg $\bar{L}_{z}$ can be calculated using Little’s law () for the number of vehicles, multiplied by the horizontal separation requirement $S_{h}$: (25) $\bar{L}_{z} = \bar{d}_{z} \bar{q}_{z} S_{h}$ By, when $\bar{L}_{z}$ is greater than the distance to the next intersection, i.e., length of the leg $D_{z}$, the airspace is predicted to become unstable.

## 6\. Simulations

To verify the assumptions and models from the previous sections, a set of simulation experiments is performed. All experiments are conducted using the BlueSky open-source ATM simulator (). This is a microscopic simulator representing the movements of individual aircraft. The remainder of this section will first discuss the tactical conflict detection and resolution algorithms used in the simulation. This is followed by a summary of the scenarios generated for the experiment. Finally, a model accuracy parameter is proposed, facilitating the comparison between the analytical model predictions and the simulation results. Results will be presented in Section.

### 6.1. Conflict detection and resolution

The state-based conflict [detection algorithm](https://www.sciencedirect.com/topics/engineering/detection-algorithm) used in this study is equal to the algorithm used by and assumes perfect knowledge of aircraft position and [ground speed](https://www.sciencedirect.com/topics/engineering/ground-speed) vector. In the algorithm, aircraft positions are linearly extrapolated along their ground speed vectors over a look-ahead time $t_{l}$ of $20$ seconds to predict intrusions.

Tactical conflict resolution is implemented, where each pairwise conflict is resolved using a speed-based resolution algorithm. This algorithm dictates that one aircraft decelerates to avoid the predicted intrusion. Recall from Eq. that the resolution speed $V_{W R}$ is in the range $\left[\right. 0 , V_{N R} 〉$. During a simulation, both the detection and resolution algorithms are executed for each simulation timestep $Δt$ of 0.05 s.

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X23001626-gr5.jpg)

Download: Download high-res image (207KB)

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X23001626-gr6.jpg)

Download: Download high-res image (344KB)

### 6.2. Scenario generation

We aim to set up a simulation in which we can capture the essence of the elements we want to study. There should hence be interactions between aircraft, and since we consider a constraint air space (e.g., between buildings), we consider a network with a road-like layout in the horizontal plane. In order to get the most insights from the resulting simulation results, we choose the simplest form of this. This way, results are not caused by network artefacts or irregularities. We hence simulate an orthogonal grid, with nodes where two one-way airways intersect, with the outer airways forming a counterclockwise flow, as depicted in,. Each aircraft is randomly assigned an origin (O) and a (different) destination (D) node from the set of OD nodes. This set includes all nodes halfway between two intersections. The grid is set up with a separation of $400$ m between two adjacent intersections, resulting in a total simulation area of almost $8$ km $2$. To prevent instantaneous intrusions between aircraft departing subsequently, the origin nodes of the three prior departures are excluded from the set of origin nodes for that aircraft. However, instantaneous intrusions with cruising aircraft can still occur.

The route is chosen based on the shortest path between the origin and [destination node](https://www.sciencedirect.com/topics/engineering/destination-node), taking into account the one-way restrictions. When multiple paths are equally short, the path with the least number of turns is chosen. As a result, only a single route is available for any OD combination.

For all conditions, scenarios are generated in which we aim for a more or less constant traffic density, by using a stochastically constant inflow. In contrast to, aircraft are introduced at intervals following a random Poisson variable, i.e., exponentially distributed with a mean inflow rate $\bar{q}_{i}$. summarises the common parameters used in the simulations.

We will be running the simulation with 3 different settings. Firstly, a base experiment with the parameters outlined in is used to evaluate the accuracy of the analytical free-flow model. Secondly, a speed experiment with a cruise speed of $5m/s$ is used as a sensitivity analysis to verify and show the impact of changing $V_{N R}$. Thirdly, a horizontal separation requirement experiment is used with an $S_{h}$ of $100$ meters to verify and show the impact of changing $S_{h}$ on the relationship between mean inflow rate and the mean density.

Table 1. Parameters used in the simulations.

| Parameter | Value | Unit | Description |
| --- | --- | --- | --- |
| $a$ | 3.5 | m/s $2$ | Acceleration or deceleration capability |
| $D$ | 200 | m | Distance OD-node to intersection |
| $S_{h}$ | 50 | m | Horizontal separation requirement |
| $t_{l}$ | 20 | s | Look-ahead time |
| $V_{N R}$ | 10 | m/s | Cruise speed of aircraft NR |
| $V_{W R}$ | $\left[\right. 0 , V_{N R} 〉$ | m/s | Possible range of speeds of aircraft WR (see Eq. ) |
| $Δt$ | 0.05 | s | Simulation timestep |
| Repetitions | 10 | – | Number of repetitions per density for each experiment |
| Size | 8x8 | – | Number of flows (H x V) |

Both the base and speed experiments are run at $10$ different traffic inflow rates $\bar{q}_{i}$ equally spaced from $22$ to $220$ aircraft per second. The maximum mean traffic density of $220$ $\bar{N}_{i , N R}$ is chosen as the upper bound, since for higher inflow rates simulation runs became unstable (i.e., the simulated airspace became gridlocked, see Section and ()). For the separation experiment, the runs were found to become unstable upward of a lower mean traffic density compared to the base and speed experiment, namely from $80$ $\bar{N}_{i , N R}$. Therefore, as a maximum mean density, $80$ is chosen, and the separation experiment uses $10$ densities equally spaced from $8$ to $80$ $\bar{N}_{i , N R}$. The inputs of the experiments are summarised in. $10$ different random realisations are generated for each traffic density, to account for random fluctuations. Hence, altogether, $300$ scenarios are simulated.

In each scenario, all aircraft are assigned a departure time, origin, destination, and route. Each run uses a warm-up period of $15$ minutes, a logging period of $45$ minutes, and a cool-down period of $15$ minutes in which aircraft keep spawning. The warm-up period is used to avoid effects at the start of the simulation, due to the generation of aircraft. The cool-down period, likewise, is used to avoid effects at the end, due to aircraft arriving. $15$ minutes is deemed sufficient, as the maximum trip duration without resolution is less than $6$ minutes in all simulation runs. Furthermore, when evaluating dependent airspace variables, such as the mean density or the mean delay, the values over the entire logging period are averaged.

Table 2. Summary of experiment inputs.

| Experiment | Changed variable | $\bar{N}_{i , N R}$ range | Total no. of aircraft $[′000]$ |
| --- | --- | --- | --- |
| Base | – | $[22,44,…,220]$ | 377 |
| $0 . 5 V_{N R}$ | $V_{N R} \rightarrow 5 m/s$ | $[22,44,…,220]$ | 188 |
| $2 S_{h}$ | $S_{h} \rightarrow 100$ m | $[8,16,…,80]$ | 137 |

### 6.3. Model accuracy assessment

A qualitative assessment can be made of the accuracy by inspecting the similarity in shape and magnitude between the analytical model predictions and the simulation results. To also facilitate a quantitative comparison, the $k$ -parameter is introduced (): (26) $q_{\text{Simulation measurement}} = q_{\text{Analytical model}} \cdot k$

This parameter is obtained by fitting the analytical model in a least-squares sense to the simulation data. In this report, we convert $k$ to express the [relative error](https://www.sciencedirect.com/topics/engineering/relative-error), $k_{\%}$, as well: (27) $k_{\%} = \left(1 - \left|\frac{k - 1}{k}\right|\right) \cdot 100 \%$

We expect that not all simulations will produce stable simulation results. For the same inflow, we repeat the simulation several times with stochastic changes. The relative frequency at which simulations for a certain inflow will become unstable is an important criterion to assess how close the inflow value is to the [transition point](https://www.sciencedirect.com/topics/physics-and-astronomy/transition-point) between free flow and congestion, and, thereby, the capacity of the network.

## 7\. Results

This section compares the predictions of the analytical free-flow model to the outcomes of the simulations. Next, the section analyses the correlation between the analytical model’s prediction of the theoretical capacity of the constrained airspace and the maximum capacities encountered in the simulation.

### 7.1. Analytical free-flow model validation

In, the comparison between the predictions of the analytical model and the results of the simulations is visualised. The analytical model predictions of Section are shown as solid lines, with the corresponding simulation runs marked by an ‘x’ in the same colour. As can be seen, the analytical model closely predicts both the shape and the magnitude of the mean density. Only for higher inflow rates the analytical model slightly overestimates the simulated mean densities.

Simulation runs with the highest densities sometimes became unstable, i.e., $8$, $2$, and $5$ out of the $10$ random realisations for the maximum density simulation runs of the base, $0 . 5 V_{N R}$, and $2 S_{h}$ experiments, respectively. In an unstable run, the airspace became gridlocked. In other words, the speed of all aircraft had reduced to $0m/s$ and they were unable to reach their destination. These unstable runs cannot be shown in the figures, as, without outflow, the number of instantaneous aircraft keeps increasing linearly with inflow.

In addition, the comparison between the analytical model and the simulation experiments is expressed quantitatively in terms of $k$ and $k_{\%}$ (as defined by Eqs., ) in. Note that the fitted model curve, i.e., the model multiplied by $k$, is not shown in the figure. The accuracies of 98% and higher show that the model can closely predict the shape and magnitude of the relationship between the mean inflow rate and the mean density in a two-dimensional grid network airspace. Inspecting the results closely, we find all three experiments show a slight overestimation of the mean density predicted for a given mean inflow rate (the line is below the points, or numerically we find values of $k$ in the order of 0.98, which is smaller than 1).

![](https://ars.els-cdn.com/content/image/1-s2.0-S0968090X23001626-gr7.jpg)

Download: Download high-res image (233KB)

This slight overestimation can be explained by noting that, as mentioned in Section, the derived model acts as an upper bound on delay and, therefore, as an upper bound on the mean density. Namely, the analytical model overestimates the time a crossing aircraft occupies an intersection when the upstream legs are not perfectly alternating. In the grid network airspace used in the simulations, the busy intersections near the centre are unbalanced, having flow ratios between both upstream legs up to approximately $1.7:1$. This imbalance explains the overestimation of the mean delay and the mean density.

Table 3. Accuracy of the analytical model for the relationship between the mean inflow rate and the mean density compared to the simulation experiments.

| Experiment | $k$ | $k_{\%}$ | $N \left(\text{unstable at} \bar{q}_{i , m a x}\right)$ |
| --- | --- | --- | --- |
| Base | 0.984 | 98.4% | $8/10$ |
| $0 . 5 V_{N R}$ | 0.981 | 98.1% | $2/10$ |
| $2 S_{h}$ | 0.979 | 97.8% | $5/10$ |

### 7.2. Comparison between theoretical and simulation airspace capacities

The analytical model allows the prediction of the theoretical maximum density and flow rate for an airspace with given parameters (e.g., cruise speed, size, separation distance), using and Eq.. The calculated values for the three experiments are shown under ‘Analytical’ in. Next to the analytical predictions, the maximum densities as encountered in the simulation runs are shown under ‘Simulated’. Due to randomness in the simulation runs, no hard upper bound for the maximum capacity can be derived. However, all three experiments produced at least a single unstable run at their maximum density (see ). Therefore, the maximum capacities encountered in the simulations are assumed to be a close approximation to the actual maximum.

The table shows that a change in cruise speed $V_{N R}$ does not impact the analytically predicted maximum density. Furthermore, the same density can be reached by scaling the network inflow rate proportionally to the cruise speed. However, for a change in the horizontal separation requirement $S_{h}$, no proportionality is found. Increasing $S_{h}$ means that both the maximum mean density and the maximum mean flow rate decrease. These analytical predictions are confirmed by the simulation data, which, although at a lower maximum capacity, shows similar behaviour.

Table 4. Analytical versus simulated capacities of the three experiments, shown as a combination of maximum stable density and stable inflow rate.

<table><thead><tr><th>Experiment</th><th colspan="2">Analytical</th><th colspan="2">Simulated</th></tr><tr><td>Empty Cell</td><th>Max. <math><msub is="true"><mrow is="true"><mover is="true"><mrow is="true"><mi is="true">N</mi></mrow> <mo is="true">¯</mo></mover></mrow> <mrow is="true"><mi is="true">i</mi><mo is="true">,</mo><mi is="true">W</mi> <mi is="true">R</mi></mrow></msub></math></th><th>Max. <math><msub is="true"><mrow is="true"><mover is="true"><mrow is="true"><mi is="true">q</mi></mrow> <mo is="true">¯</mo></mover></mrow> <mrow is="true"><mi is="true">i</mi></mrow></msub></math></th><th>Max. <math><msub is="true"><mrow is="true"><mover is="true"><mrow is="true"><mi is="true">N</mi></mrow> <mo is="true">¯</mo></mover></mrow> <mrow is="true"><mi is="true">i</mi><mo is="true">,</mo><mi is="true">W</mi> <mi is="true">R</mi></mrow></msub></math></th><th>Max. <math><msub is="true"><mrow is="true"><mover is="true"><mrow is="true"><mi is="true">q</mi></mrow> <mo is="true">¯</mo></mover></mrow> <mrow is="true"><mi is="true">i</mi></mrow></msub></math></th></tr><tr><td>Empty Cell</td><th>–</th><th>s <sup>−1</sup></th><th>–</th><th>s <sup>−1</sup></th></tr></thead><tbody><tr><th>Base</th><td>353</td><td>0.96</td><td>259</td><td>0.78</td></tr><tr><th><math><mrow is="true"><mn is="true">0</mn><mo is="true">.</mo><mn is="true">5</mn> <msub is="true"><mrow is="true"><mi is="true">V</mi></mrow> <mrow is="true"><mi is="true">N</mi> <mi is="true">R</mi></mrow></msub></mrow></math></th><td>353</td><td>0.48</td><td>249</td><td>0.39</td></tr><tr><th><math><mrow is="true"><mn is="true">2</mn> <msub is="true"><mrow is="true"><mi is="true">S</mi></mrow> <mrow is="true"><mi is="true">h</mi></mrow></msub></mrow></math></th><td>181</td><td>0.45</td><td>93</td><td>0.28</td></tr></tbody></table>

Additionally, the maximum theoretical densities as predicted by the analytical model overestimate the maximum stable densities encountered in the simulation runs by a factor of 1.35 for the Base and $0 . 5 V_{N R}$ experiments and a factor of almost $2$ for the $2 S_{h}$ experiment. Yet, this was predicted by, as stochastic effects mean that the network can already become unstable at a lower flow rate than at the mean flow rate used for the analytical prediction.

## 8\. Comparison and synthesis

In this study, a purely analytical free-flow model for the relationship between the mean inflow rate and the mean density was developed to investigate and quantify the factors influencing the capacity of constrained urban airspace. Simulations were performed to validate the accuracy of the analytical model. This section discusses the level of accuracy of the analytical model, followed by a discussion on the effects of several airspace design parameters on its capacity.

### 8.1. Analytical free-flow model validation

The comparison of the analytical model with the results of simulations showed that model accuracy is high, with accuracies higher than 97%. The analytical model closely predicts the shape of the relationship between the mean inflow rate and the mean density, as well as the values. The inaccuracies stem from an overestimation of the mean density by less than 2.5% in all three experiments.

Two limitations were identified in Section. The first limitation is the slight overestimation of the mean density. As mentioned, this is the result of the overestimation of the mean delay on unbalanced intersections. The second limitation is that the maximum theoretical densities as predicted by the analytical model overestimate the maximum stable densities encountered in the simulation runs. This can be attributed to the stochastic periods of higher inflow rates in the simulations.

Additionally, turning traffic is simulated and modelled to not decelerate in order to perform a turn. If this would be the case, the deceleration could cause spillback conflicts to occur, increasing the mean density for the same inflow rate. As proposed by, this effect can be coped with by adding altitude layers specifically for turning, in a three-dimensional airspace design.

Despite the limitations discussed above, the analytical model demonstrated the ability to estimate the relationship between the mean inflow rate and the mean density, similar to the free-flow section of a Macroscopic Fundamental Diagram, for a two-dimensional orthogonal grid network. Therefore, the derived model provides an effective tool to predict the effect of several design parameters on the capacity of constrained urban airspace. In addition, the high level of accuracy validates utilisation of the theoretical maximum density defined by to compare different constrained urban airspace designs, similar to the maximum density defined for general airspace by the CAMDA model ().

### 8.2. Effect of airspace design parameters

The analytical model’s accuracy level allows for quantifying the effect of several relevant airspace design parameters. Based on the parameters used in the equations, three design parameters are observed to affect the capacity metrics used in this paper: the cruise speed $V_{N R}$, the horizontal separation requirement $S_{h}$, and the number of flow alternations at an intersection. The look-ahead time, when sufficiently long, does not affect the relationship between the mean inflow rate and the mean density. Additionally, the effect of the airspace structure, including, for example, the distance between intersections and the airspace area, is discussed.

When increasing the cruise speed, aircraft can travel a longer distance in the same time window, lowering the resulting mean density. Moreover, the mean delay per aircraft decreases as more aircraft can cross an intersection in the same time window. The analytical model predicts that the mean inflow rate scales proportionally with the cruise speed $V_{N R}$ when keeping the mean density constant. Furthermore, the maximum stable density defined by remains unchanged. Hence, an increase in cruise speed is predicted to result in a proportional increase in the maximum inflow rate and capacity.

For the horizontal separation requirement $S_{h}$, this proportionality is not present. Instead, the analytical model predicts that enlarging $S_{h}$ reduces capacity. When $S_{h}$ is increased, the maximum number of aircraft that fit within an airway is lowered, while the crossing times of aircraft are extended. Both factors increase the mean delay per aircraft, reducing the maximum inflow rate and the maximum density.

Furthermore, capacity is predicted to be increased when the flows coming from the two upstream legs of an intersection alternate less frequently, as was stated in. Because the time window between two subsequent aircraft is increased by a factor $\sqrt{2}$ when the upstream flow is alternated (on an orthogonal intersection, see Eqs., ), capacity is decreased for each alternation. Therefore, a system limiting the number of alternations, for example, a traffic signal, may increase capacity. However, this system extends the mean queue length, increasing the chance of overflow. In this study, no exact model for an intersection with an alternation [limiter](https://www.sciencedirect.com/topics/engineering/limiters) is derived. Hence, the break-even point for the benefits of this system cannot be predicted. It is recommended to quantify this break-even point in further research.

Lastly, the structure of the airspace itself has a significant impact. When the distance between two neighbouring intersections is decreased, the probability of overflow increases, resulting in a reduced capacity. Contrarily, if this change results from an enlarged number of intersections and airways in the area, the capacity increases as the proportion of flyable airspace increases. When keeping the airspace area equal, doubling the number of airways in each direction leads to an increase by a factor of 2.1 in capacity.

Concluding, for airspace design, capacity can be optimised by lowering the separation requirement and by increasing the cruise speed, taking into account the necessary safety levels. Additionally, increasing the density of airways within an airspace increases the maximum capacity as well. However, the minimum separation requirement should be considered when increasing the airway density, as the separation requirement circle should not overlap with adjacent airways, leading to head-on conflicts between aircraft in adjacent airways.

## 9\. Conclusions and disucussion

The traffic density of small aerial vehicles within the highly constrained, low-altitude urban airspace is expected to increase significantly in the near future. An analytical approach is taken to increase understanding of the factors that influence the capacity of constrained urban airspace. The emergent behaviour of aircraft in constrained urban airspace, such as queuing and local hotspots, yields the existing analytical models for general airspace invalid. Therefore, in this paper, a new mathematical model is derived to estimate the relationship between the mean inflow rate and the mean density, similar to the free-flow section of a Macroscopic Fundamental Diagram, for a two-dimensional orthogonal grid network. By performing three simulation experiments involving more than 700,000 flights, the level of accuracy of the mathematical model is shown to be higher than 98.5%. This high level confirms the ability of the model to closely predict the shape and magnitude of the relationship between the mean inflow rate and the mean density in the two-dimensional orthogonal grid network.

In addition, the high level of accuracy of the analytical model allows quantitative prediction of the effects of several relevant airspace design parameters on capacity. Notable findings showed that an increase in cruise speed leads to a proportional increase in the maximum network inflow rate while the maximum density is unaffected. Contrarily, enlarging the [minimum separation distance](https://www.sciencedirect.com/topics/engineering/minimum-separation-distance) reduces capacity. Additionally, turning traffic on balanced intersections does not impact the capacity more than through traffic. If routing with additional turns means that a shorter route is possible, efficiency may be increased. Lastly, a metric was defined describing a theoretical maximum density, which can rank different constrained urban airspace designs on capacity.

Furthermore, in a stable environment, the model predicts that the constrained urban airspace can destabilise when the maximum capacity of a single intersection only is reached. Additionally, for intersections operating at near-maximum capacity, measures limiting flow alternation, such as traffic signals, potentially improve the efficiency of an intersection of airways.

All in all, the results demonstrate how the derived analytical model provides an effective tool to predict the effect of several design parameters on the capacity of constrained urban airspace. Therefore, the analytical method offered by this work can be one of the tools in the toolbox of the future urban airspace designer. Moreover, this model lays the foundation for the derivation of more expanded models, including the altitude dimension and non-orthogonal or non-two-way intersections, enabling an increased understanding of the constrained urban airspace.

There are some further open questions which can be addressed in future work. First, in this paper, a two-dimensional model is derived. However, in a realistic airspace design, the vertical dimension cannot be neglected. The model approach presented in this paper can form a basis for this three-dimensional analysis. By substituting the vertical equivalents of the horizontal variables, e.g., the vertical separation requirement instead of $S_{h}$ and the vertical speed equivalents of $V_{N R}$ and $V_{W R}$, the model is expected to be valid for a single vertical plane, two-dimensional airspace. It is recommended to investigate whether the three-dimensional constrained urban airspace can subsequently be modelled as the sum of intersections in either the vertical or the horizontal plane, or whether a separate model extension needs to be derived for the third dimension. Consider that model accuracy is expected to deteriorate when interactions between the vertical and horizontal manoeuvres exist.

Furthermore, the derived model is validated for orthogonal intersections with up to two upstream legs only. In general, more complicated intersections exist with, for example, more than two upstream legs or non-orthogonal legs. It is hypothesised that the model can accurately predict the relationship between the mean inflow rate and the mean density at more complicated intersections, considering a few adjustments. Specifically, the red time $r$ and the cycle time $\bar{c}_{u}$ need to be adjusted to include all crossing traffic and their respective crossing times. Further research is required to test this hypothesis.

Additionally, several limitations need to be considered for the findings in this paper. This study neglected meteorological effects, which may harm overall capacity. Nevertheless, the meteorological effects can be approximated using, e.g., an increased horizontal separation requirement $S_{h}$. Another limitation is the static demand (in terms of network inflow rate) assumed in both the analytical model and the simulations. In reality, airspace demand changes from time to time in urban networks (). Depending on the size of the airspace and rate of change of aircraft inflow rate, this may imply that during a ‘rush hour’, busy parts of the airspace can congest for a limited time without destabilising the entire airspace (in contrast to ). When demand decreases at the end of the rush hour, the congestion gradually disappears. Note that the energy storage of drones is limited, making it plausible that congestion is to be prevented at all times. Also, various other forms of [stochasticity](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/stochasticity) in demand (e.g., origin and destination variations over time) and heterogeneity in UAV type should ultimately be included.

## CRediT authorship contribution statement

**Michiel J.M. Aarts:** Conceptualization, Investigation, Formal analysis, Writing – original draft. **Joost Ellerbroek:** Conceptualization, Supervision, Reviewed and edited the draft. **Victor L. Knoop:** Conceptualization, Supervision, Reviewed and edited the draft.

## Data availability

Code can be found in the cited github repository.

## References

The source code used to perform the simulations can be found here: [https://doi.org/10.5281/zenodo.5984628](https://doi.org/10.5281/zenodo.5984628).