---
title: "A Holistic Design and Simulation of Advanced UTM Services for Urban Air Mobility"
source: "https://ieeexplore.ieee.org/document/11340640"
author:
published:
created: 2026-07-01
description: "This article presents a modular suite of collaborative uncrewed aircraft system traffic management (UTM) services designed to enhance urban airspace operations."
tags:
  - "clippings"
---
## Abstract:

This article presents a modular suite of collaborative uncrewed aircraft system traffic management (UTM) services designed to enhance urban airspace operations. The frame...

---

The rise of urban air mobility (UAM) is key to the multimodal development of smart cities, promoting a connected, safer, and greener airspace. Global trends are transforming air transportation by integrating uncrewed aircraft systems (UAS) with current aviation. Initiatives, such as the Next Generation Air Transportation System (NextGen) in the United States and the Digital Single European Sky (SES) in Europe, propose a competitive framework aimed at modernizing the National Airspace System (NAS) and the SES \[1\], \[2\]. This shift includes the creation of UAS traffic management (UTM), which complements traditional air traffic management (ATM) by focusing on low-altitude airspace.

The current development phase of UTM extended by the UAM concept of operations (ConOps), aims to challenge innovative operational scenarios to assess potential demand, available resources, and existing capabilities for establishing a functional management ecosystem. These ConOps facilitate UTM service provisions that ensure safe and efficient airspace usage while complying with operational and regulatory requirements \[3\]. In the USA, the Federal Aviation Administration (FAA) collaborates with National Aeronautics and Space Administration (NASA) to develop ConOps and integrate UTM services into the National Airspace System \[4\]. According to the ConOps \[4\], the evolution of UAM operations can be divided into initial, midterm, and mature phases, with each phase providing services tailored to operational needs. FAA has also proposed Beyond Visual Line of Sight (BVLOS) rules (Part 108 and Part 146) explicitly recognize strategic conflict resolution (ScR) and conformance monitoring as regulated UTM services \[5\]. In Europe, Single European Sky ATM Research Joint Undertaking (SESAR JU) partnerships initiate projects to promote research and development of UTM services, proposing a Blueprint categorizing services into four deployment levels: foundation, initial, advanced, and full (U1–U4) \[6\], \[7\]. The U.K. Civil Aviation Authority drives UTM technology development through a 10-year roadmap and future flight challenges \[8\].

As a key element of future UAM operations, UAM services are being developed through both academic research and projects led by government or industry stakeholders. Academic studies typically focus on advanced approaches, such as heuristic algorithms, optimization techniques, and machine learning (ML). Research on critical UAM services, include ScR and tactical conflict resolution (TcR) \[9\], \[10\], \[11\], \[12\], risk assessment \[13\], \[14\], and demand capacity management \[15\], \[16\], have already been widely discussed in the literature. In contrast, research projects are usually motivated by practical application. For example, NASA has presented the results of an analysis of strategic conflict management strategies applied to UAM and AAM operations \[17\], \[18\], and has also proposed a set of demand capacity balancing algorithms specifically designed for UAM operations \[19\], aiming to reduce predeparture delays. The European U-Space programme encompasses a series of influential research projects that proposes and develops UAM ConOps, regularly updating UTM service recommendations. While many foundational UTM development projects exist, BUBBLES, Metropolis 2, and DACUS have reshaped tactical conflict detection and TcR, ScR, and dynamic capacity management (DCM) services \[20\], \[21\], \[22\].

To accelerate the integration of UAM operations into the airspace and to evaluate the effectiveness of the proposed ConOps and framework, a series of demonstrations has been conducted. In the USA, NASA, in partnership with the FAA and industry partners, developed and validated a UTM ecosystem for small UAS through a series of progressively complex field tests \[23\], \[24\]. These were structured into four technical capability levels (TCL), each addressing increasing operational complexity—from rural, low-risk operations up to dense urban airspace integration at TCL4. Building on this, NASA launched the National Campaign project to assess and accelerate the technologies required for UAM through a series of systems-level flight demonstrations \[17\], \[25\]. In Europe, projects, such as Proving Operations of Drones with Initial UTM (PODIUM), U-Space Initial Services (USIS), Safe and Flexible Integration of Advanced U-space Services for medical Air Mobility (SAFIR-Med), and Air Mobility Urban-Large Experimental Demonstration (AMU-LED), have tested and validated service integration across various scenarios, involving stakeholders, such as common information Service Providers (CISPs) and UTM Service Providers (USSPs) \[26\], \[27\], \[28\], \[29\]. The current focus on deploying U2 services aims to democratize the management of beyond visual line of sight operations in controlled, low-density airspace where crewed aviation is restricted \[30\]. U-Space European Common Deployment (U-ELCOME) implemented UTM services across multiple locations through a new series of trials, testing, and demonstrating U1 and U2 solutions \[31\]. SPATIO focuses on separation management between UAS, emphasizing both strategic and TcR to maintain safe distances in crowded airspace \[32\]. Enhanced Automation for U-Space/ATM integration (EALU-AER) project is establishing Ireland's first digital sky demonstrator to integrate UTM technology for enhanced automation through advanced services (U3/U4) \[33\].

The development of UTM services necessitates extensive testing in synthetic operational environments using simulations. Recent research has highlighted the effectiveness of a comprehensive simulation framework for supporting ATM and UTM services. The Traffic Manager (TMX), created by the Netherlands Aerospace Centre (NLR), has evolved into a medium-fidelity application for exploring innovative ATM concepts \[34\]. Advances in agent-based techniques have improved the simulation of UTM operational scenarios, ensuring continuous coordination among stakeholders. TU Delft has developed BlueSky \[35\], an open-source air traffic control (ATC) simulator designed to complement projects, such as Complex Adaptive Systems for Optimization of Performance in ATM (CASSIOPEIA) and empirically grounded agentbased models for the future ATM scenario (ELSA), facilitating academic ATM research \[36\], \[37\]. NASA's UTM Laboratory developed Fe3 \[38\], a versatile simulation component that supports near-term live flight testing and studies high-density, low-altitude air traffic systems, featuring a fast-time simulation option akin to BlueSky. A survey of prominent agent-based frameworks, such as Gazebo, AirSim and Janus, identified essential components for deploying synthetic operations \[39\]. Cranfield University created a mixed-reality digital twin (DT) that accommodates diverse users, including USSPs and ATC Officers (ATCOs), and assesses operations from various real or virtual platforms \[40\]. Airbus developed USim that integrates a simulation environment with an ScR prototype \[41\].

The current UTM state-of-the-art reveals several limitations that hinder the transition from concept to operational deployment. Academic research often address individual functions in isolation, with limited exploration of how services can operate together within an integrated, digitally enabled framework, and with little alignment to governance or industrial practices. This fragmented approach results in overlapping concepts built on differing assumptions, data dependencies, and no clear path to interoperability. On the industrial side, while notable progress has been made toward deployable UTM systems and their ongoing certifications, these solutions are often proprietary and opaque, offering little awareness into service interactions, performance benchmarking, or operational dependencies. There is a pressing need for integration-oriented research that defines the role of service digitalization and AI/ML, discusses their place through concrete applications, and clarifies how core UTM services can be jointly implemented, benchmarked under consistent criteria, and designed with transparent interservice dependencies.

Building on the large-scale AMU-LED project \[42\], \[43\], which has applied our research in real-world scenarios, this article presents additional contributions that further advance the state of the art in UTM service design and simulation.

1. A unified UTM service framework is presented that combines an automated preflight service toolset with an in-flight service toolset. While the platform supports advanced DT capabilities (e.g., live–virtual–constructive integration), in this study both toolsets were integrated into a synthetic operational environment that relied exclusively on high-fidelity simulation.
2. A modular testbed is developed that facilitates the integration and replacement of specific services, such as alternative models and algorithms. This supports comprehensive simulations that examine interdependencies between services, improving the understanding of how changes in one service impact overall system performance.
3. Using the testbed, over 1600 flight hours of simulation have been conducted to thoroughly evaluate the effects of various UTM services and their parameters, which offers valuable insights into key performance areas (KPAs), including safety, cost-efficiency, and operational workload.
4. EUROCONTROL's complexity Air Navigation Service (ANS) metrics are adapted to the UTM context, presenting a method for quantifying and managing the complexity of urban airspace operations, which provides benchmarks for assessing how UTM services can alleviate the heightened complexity in dense environments.

The rest of this article is organized as follows. First, a high-level description of the ecosystem embedding the UTM services and their interacting components is provided in the “High-Level UTM Simulation Framework” section. The services are grouped into two categories: the preflight services, described in the “Preflight UTM Services” section, and the in-flight services, presented in the “In-Flight UTM Services” section. This is followed by the experimental evaluation in the “Experiments” section. The discussion is done in the “Discussion” section. Finally, the “Conclusion” section concludes this article.

This section presents a high-level overview of the ecosystem developed in this study. The “Architecture Overview” section begins by presenting the overall architecture of the UTM simulation framework. It is followed by how services are orchestrated within this framework in the “UTM Service Provision Flow Summary” section.

### Architecture Overview

This research focuses on a set of advanced UTM services designed to be modular toolsets, that is, they can be complemented with additional services or selectively removed in specific cases. This modularity enables the ecosystem to scale on a service-on-demand basis and constitutes the core interest of this study.

In addition to the UTM services, two additional elements complete the ecosystem. The first is the simulator, which emulates the operational environment in which flight activities are tracked and managed by the UTM services. The simulator can operate in a fully back-end mode or be enhanced with visual components to support situational awareness. In principle, any simulation engine may be used, provided it delivers the required traffic information. Its importance lies in the quality of the generated data, which directly influence the fidelity of the simulated operational dynamics.

Finally, the system accounts for two categories of users: the operator or pilot, who conducts point-to-point flight missions at very low level, and the controller or USSP, who supervises the operation and oversees the execution of UTM services.

Figure 1 illustrates the components described above: the user's mission timeline appears on the left, the simulator is located in the bottom-left corner, and the modular UTM services, which are the main focus of this study, occupy the remainder of the framework. In this research, all operations and services are executed autonomously, without human intervention. The description of the different blocks of the framework is introduced in the following section.

[![Figure 1. - 
            Overview of the UTM services framework and its interactions. The framework is divided into two stages: preflight services, which ensure mission planning before flight authorization, and in-flight services, which oversee execution and respond to operational events in real time.
          ](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/62/11554465/11340640/xu1-3652153-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/62/11554465/11340640/xu1-3652153-large.gif)

**Figure 1.**

Overview of the UTM services framework and its interactions. The framework is divided into two stages: preflight services, which ensure mission planning before flight authorization, and in-flight services, which oversee execution and respond to operational events in real time.

### UTM Service Provision Flow Summary

As illustrated in Figure 1, the set of advanced UTM services is organized into two main blocks: preflight services and in-flight services, which are detailed in the “Preflight UTM Services” section and the “In-Flight UTM Services” section, respectively. In this article, we refer to the strategic, preflight phase services that perform the flight authorization process collectively as preflight services, and to the in-flight phase services, often referred to as tactical services, as in-flight services.

In a given piece of airspace managed by UTM services, operations must adhere to a defined protocol, beginning with a flight approval. Preflight services process such requests based on existing demand, current operational plans, and the constraints imposed by airspace capacity and risk. At the end of this preflight process, the operator typically receives authorization to fly within the airspace along a defined route, during a specified time window. The granted authorization may differ from the original request, and the operation is subsequently registered to enable monitoring throughout its activation.

Once the registered and approved operation enters its authorized time window, it is considered active, and the in-flight services take over the monitoring process. Based on the flight plan and operation tracking, these services assess whether the behavior of the aircraft aligns with the expected trajectory. If the operation proceeds nominally, then no visible intervention is made. However, in the event of an off-nominal situation, the in-flight services are designed to detect the anomaly and respond appropriately to ensure safety.

An intermediate module, referred to as the compiler in Figure 1, acts as a unidirectional bridge between the preflight and in-flight services. In the current design, this unidirectional flow implies that in-flight services do not provide feedback to preflight components. The compiler processes, organizes, and transmits authorized flight data from the preflight services to both the simulator and the in-flight services. While the compiler is also capable of communicating information to third parties (e.g., USSPs and CISP), this functionality falls outside the scope of the present study. Readers interested in large-scale demonstrations of such UTM capabilities are referred to relevant literature \[44\], \[45\], which discusses findings from the SESAR JU AMU-LED project.

### Algorithm 1. Pre-Flight Services Workflow.

1:

**if** operation $request$ (i.e., flight plan = $\emptyset$) **then** “Operation Plan Preparation & Optimisation” section

2:

flight plan $\gets$ $A^{*}$ (initial constraints)

3:

**else**

4:

flight plan $\gets$ $A^{*}(g_{RAA}$, $g_{DCM}$, $g_{ScR}$)

5:

**end if**

6:

**for** $segment$ **in** flight plan **do** “Risk Analysis Assistance” section

7:

**if** $R_{segment} \geq \text{Risk}_{\text{threshold}}$ **then** Eq. [(1)](#deqn1)

8:

$$
g_{RAA} \longleftarrow \text{geofence}(segment)
$$

9:

**end if**

10:

**end for**

11:

**if** $g_{RAA} \ne \emptyset$ **then**

12:

**return to** line 4

13:

**end if**

14:

**for** $cell$ **in** airspace crossed by flight plan **do** “Dynamic Capacity Management” section

15:

**if** $cell$ in congested area **then**

16:

$g_{DCM} \longleftarrow min(C_{r}|cell)$ Eq. [(2)](#deqn2)

17:

**end if**

18:

**end for**

19:

**if** $g_{DCM} \ne \emptyset$ **then**

20:

**return to** line 4

21:

**end if**

22:

**for** $cell$ **in** airspace crossed by flight plan **do** “Strategic Conflict Resolution” section

23:

**if** $cell$ **is** occupied **then**

24:

$g_{ScR} \longleftarrow C_{delay}|cell$ Eq. [(3)](#deqn3)

25:

**end if**

26:

**end for**

27:

**if** $g_{ScR} \ne \emptyset$ **then**

28:

**return to** line 4

29:

**else**

30:

flight plan **is** approved

31:

**end if**

This section focuses on the preflight services involved in the flight authorization process. The “Preflight Toolset Integration” section provides a high-level overview of their interactions, followed by detailed descriptions of each service: operation plan preparation and optimization in the “Operation Plan Preparation and Optimization” section, risk analysis assistance (RAA) in the “Risk Analysis Assistance” section, DCM in the “Dynamic Capacity Management” section, and ScR in the “Strategic Conflict Resolution” section.

### Preflight Toolset Integration

The preflight service toolset includes the following services: Operation plan preparation and optimization, RAA, DCM, and ScR. While these services are presented as opaque systems here, they are explained in detail in the rest of this section. The provided references offer additional resources for readers interested in exploring the replicability of each service.

As shown in Figure 2 and in the pseudocode for the preflight phase module through Algorithm 1, preflight services are executed sequentially with retroactive effects on the operation plan optimization service. If an upstream provision encounters a constraint or fails during the flight plan authorization, then these constraints are considered to refine the proposal for a safer and more efficient option. This iterative process continues until all preflight services have validated the flight plan for their specific purposes.

[![Figure 2. - 
            Preflight services workflow.
          ](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/62/11554465/11340640/xu2-3652153-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/62/11554465/11340640/xu2-3652153-large.gif)

**Figure 2.**

Preflight services workflow.

The operator submits a flight request with the departure time, origin, and destination, which is processed by the operation plan preparation service (Algorithm 1, line 1). During flight plan construction, static data, including terrain features, ground obstacles, major road networks, and restricted airspace, are considered (line 2). These data represent environmental information that is unlikely to change. The initial flight plan is then sent to the RAA service to evaluate its risk level (line 7). Once the flight plan is deemed to exceed the airspace capacity, it is forwarded to the DCM service (line 14), which may suggest alternative flight trajectories to avoid congested airspace and balance demand with capacity (line 16). Finally, the flight plan is handled by the ScR service (line 22), which identifies potential conflicts with other flight plans and resolves them by allocating delays (line 24).

### Operation Plan Preparation and Optimization

This service includes strategies that optimize the creation and modification of flight plans, ensuring compliance with safety and efficiency requirements for UTM operations.

This service generates initial flight plans based on a discretized 3-D airspace divided into equally sized volumes. Each cell connects to its adjacent cells in 10 directions, eight horizontally, and two vertically, except where airspace constraints or boundaries exist. Altitude layers are added to these volumes to represent vertical operations, as shown in Figure 2. Horizontally adjacent cells are dimensioned to maintain the minimum lateral separation required between vehicles, preventing loss of separation events (refer to the “Tactical Conflict Resolution” section), whereas vertical cell spacing is set in accordance with nominal flight levels (FLs) and altitude stratification rules defined for the operational concept later in the “Setup” section.

After receiving the original and destination points from flight requests, A\* algorithm is used to identify the preferred path through a series of sequential airspace volumes. As detailed in the “Preflight Toolset Integration” section, static data, such as terrain and constraints, are considered, including airspace restrictions, significant buildings, power lines, obstacles, and high population density areas. The planning includes three parts: vertical takeoff, vertical landing, and the cruise phase. An example of the generated trajectories is illustrated in Figure 3, where the curved segments represent paths that avoid high-risk or restricted areas.

**Figure 3.**

Operation trajectories generated in the 3D designated airspace with constraints applied \[9\].

This service not only generates initial flight plans but also collaborates with other services to optimize trajectories. Through its interface with the RAA service (see the “Risk Analysis Assistance” section), it establishes a feedback loop for risk assessment and trajectory adjustments. If a flight segment's risk level exceeds the safety threshold, then geofences based on obstacle circles will indicate high-risk areas. The operation plan optimization service will then adjust the trajectory accordingly and send the revised routes back to the risk analysis module for reevaluation. This iterative process continues until all flight segments meet acceptable risk levels.

Figure 3 depicts an optimization scenario created by the operation plan optimization service, considering constraints, such as static obstacles, airspace restrictions, high-risk areas, and hotspot regions, represented by green, blue, and red shapes, respectively. While temporal aspects are not shown, the flight plans in blue are deconflicted, eliminating the need for TcR, as will be discussed later.

### Risk Analysis Assistance

The RAA service conducts both qualitative and quantitative assessments of flight plans to ensure mission area safety. After receiving the flight plan from the previous operation plan preparation and optimization service, it segments the route by waypoints and associates each segment with a risk value derived from aircraft performance parameters (e.g., size, weight, and cruising speed), environmental factors (e.g., wind speed and direction), and ground context (e.g., population density and road traffic statistics). The module's operational workflow is depicted in Figure 4, the parameters are collected from operational datasets and live or near-live data feeds.

**Figure 4.**

RAA parameterization and process \[46\].

The risk for each segment is defined as the probability of a fatal event, calculated in [(1)](#deqn1), where $P_{CR}$ is the probability of a catastrophic failure during the segment, $P_{\text{IM}|CR}$ is the conditional probability of impacting an object given such a failure, and $P_{\text{FA}|\text{IM}}$ is the probability of a fatality given the impact. These probabilities are evaluated in accordance with Specific Operations Risk Assessment (SORA)-based safety targets for urban operations

$$
\begin{equation*}R = P_{CR}*P_{\text{IM}|CR}*P_{\text{FA}|\text{IM}}. \tag{1}
\end{equation*}
$$
 View Source

Once calculated, each segment's risk value is compared to a predefined acceptable threshold. If any segment exceeds the threshold, then the system issues a rerouting request to the operation plan optimization service.

Segments passing over dense urban areas or major roads typically register higher risk values, as shown in the example in Figure 5. Risk severity in the flight plan is visually represented by a color gradient from green to red, as shown in Figure 5. Each segment is color-coded based on its calculated risk, allowing for easy comparison against safety limits. The analysis indicates that segments over highways or densely populated areas show significantly high risks, marked in red. The top figure illustrates risk along the original flight plan. In the same example, the RAA identifies a segment with a yellow geofence, leading to an optimized flight plan that includes rerouting constraints for enhanced safety.

**Figure 5.**

Risk-based geofencing and local rerouting.

This service is also responsible for identifying safe landing zones and emergency landing zones (SLZ & ELZ) using the risk map, selecting clear areas with minimal population exposure where contingent operations can land without compromising surrounding safety. However, it does not perform airspace capacity checks as part of its assessment, as these are the responsibility of the subsequent DCM service.

### Dynamic Capacity Management

The DCM service \[15\] monitors airspace demand based on active flight plans and regulates access when capacity limits are approached. It comprises three threads: capacity, demand, and demand–capacity balancing.

The capacity thread estimates the maximum operations an airspace can support. The airspace is divided into grid cells, where the demand thread assesses traffic demand for each cell using existing flight plans. By integrating the airspace configuration (capacity thread) with the trajectories (demand thread), we can identify intersections between trajectories and airspace. When any airspace portion becomes full and turns into a hotspot, routing is adjusted to avoid it. Alternative trajectories are generated to bypass the affected grid cells, excluding the first and last cells for take-off and landing, by applying these constraints to the operation plan optimization service (recall the “Operation Plan Preparation Optimization” section).

Using input from both capacity and demand, a DCM model calculates and identifies the optimal trajectory to balance demand and capacity. As shown in [(2)](#deqn2), the costs of rerouting operations are quantified

$$
\begin{equation*}C_{r} = \sum \limits _{f \in \mathcal {F}} \sum \limits _{k \in \mathcal {K}_{f}} v_{f} d_{f}^{k} z_{f}^{k} \tag{2}
\end{equation*}
$$
 View Source

where $d_{f}^{k}$ represents the additional flight duration for alternative trajectory $k$ compared to the originally scheduled duration, $v_{f}$ indicates the operation's priority based on submission timing, and $z_{f}^{k}$ is a Boolean variable that is 1 if trajectory $k$ is selected. Consequently, an optimal rerouting path is identified through the objective function min ($C_{r}$), which mitigates congestion in airspace while minimizing the costs.

### Strategic Conflict Resolution

The ScR service aims to identify and address conflicts based on flight plans during the preflight phase and after prior service completions. It is designed to greatly prevent the use of the TcR service and the use of airborne collision avoidance systems.

By sharing with relevant parties, flight plans will be compared to the activated ones to check for conflicts. If a conflict arises, then a tentative plan change will be proposed, either by delaying the takeoff time for specific operations based on a first-come, first-served (FCFS) principle or using a batch optimization approach, as illustrated in Figure 6(a) and (b), respectively. The batch optimization approach aims to resolve all conflicts while minimizing total delay, as shown in the following:

$$
\begin{equation*}C_{\text{delay}} = \sum \limits _{l \in L} \sum \limits _{j \in J_{l}^{(1)}} \sum \limits _{t \in T_{l}^{J_{l}^{(1)}}} (t - r_{l}^{J_{l}^{(1)}})(x^{j}_{l,t} - x^{j}_{l,t-1}). \tag{3}
\end{equation*}
$$
 View Source

**Figure 6.**

ScR approaches for decentralized USSPs architecture. In Figure 6(a), each flight plan is processed individually that prioritizes early submissions. In Figure 6(b), USSPs process multiple flight plans simultaneously using batch optimization considering spatial efficiency and submission fairness. (a) FCFS. (b) Batch optimization.

The total delay cost is determined by [(3)](#deqn3), where $r_{l}^{J_{l}^{(1)}}$ represents the initially scheduled takeoff times, and $t$ denotes the controlled time of arrival. Only one operation can occupy a cell within a default sliding time window, corresponding to the separation minima. Once the appropriate delay allocation is identified, an iterative negotiation and resubmission process may ensue until all predicted conflicts are resolved. The service provider then assesses airspace occupancy and determines if delays are necessary for any conflicting flights. The FCFS method is illustrated in Algorithm 2.

### Algorithm 2. FCFS Process.

1:

**for** $f \in F$ **do**

2:

**for** $(e, t), (b_{e}, t) \in f_{l}$ **do**

3:

**if** $(e, t)$ or $(b_{e}, t)$ is blocked **then**

4:

delay $f$ for 1 time unit

5:

**go to line 2**

6:

**else**

7:

insert $(e, t)$ and $(b_{e}, t)$ to $list_{l}$

8:

**end if**

9:

**end for**

10:

**for** $(e, t)$ and $(b_{e}, t) \in list_{l}$ **do**

11:

occupancy $(e, t), (e, t \pm sep)$

12:

occupancy $(b_{e}, t), (b_{e}, t \pm sep)$

13:

**move to the next operation**

14:

**end for**

15:

**end for**

If a flight plan is conflict-free, then it can be activated to update the common airspace representation. This process can occur in parallel, enabling multiple service providers to manage their flight plans simultaneously. Once a set of grid cells linked to an activated flight is occupied for a specified duration, they will be unavailable for subsequent flight plans until the current operation concludes.

Delay is used as the sole conflict resolution manoeuvre not only because it is the preferred strategy in both academic research \[18\] and practical applications \[47\], but also because rerouting has already been applied in the preceding services in the framework, (through both the RAA and DCM services). Introducing additional geometric modifications during the ScR phase could result in excessive trajectory deviations, potentially altering the operator's original intent for the submitted flight plan.

The “Preflight UTM Services” section introduced the preflight services to deliver flight authorization to the operations. This section is focused on the in-flight services toolset taking over the management of the operations once activated. The “In-flight Toolset Integration” section provides a high-level overview of the interactions and workflow of these services, followed by detailed descriptions for each of them: conformance monitoring in the “Conformance Monitoring” section, contingency management (CM) in the “Contingency Management” section, and TcR in the “Tactical Conflict Resolution” section.

### In-Flight Toolset Integration

The in-flight service toolset includes conformance monitoring, CM, and TcR. Each service is detailed in the following sections, with references for those interested in exploring their replicability. Figure 7 summarizes the high-level workflow linking flight status notifications to the activation conditions of in-flight services, which are detailed deeper for each service in the following sections.

**Figure 7.**

In-flight services workflow. The activation of the services are driven by the real-time flight status of ongoing operations.

At the activation of an operation, conformance monitoring defines its 4D operation volume (OV), specifying both altitude and lateral limits between waypoints. Meanwhile, the contingency manager designates safe and emergency landing zones based on a risk map generated by the RAA service. In-flight services actively exchange with the operational environment by interpreting traffic information, supplying real-time flight status (see Figure 7), and issuing instructions, advisories, and resolution commands during off-nominal situations with each function described for its respective service, as shown in Algorithm 3.

### Algorithm 3. In-Flight Services Workflow.

1:

Extract $operation$ information from environment

2:

**for** $operation$ **in** $active$ $operations$ **do**

3:

Conformance Monitoring is active

4:

Update $operation$ $status$

5:

Conformance Monitoring ends

6:

Contingency Manager is active

7:

**if** new $operation$ status **is** $contingent$ **then**

8:

$operation$ $\gets$ Safe Emergency Landing zone

9:

Update Safe Emergency Landing zones capacity

10:

**else if** contingent $operation$ new status **is** $Ended$ **then**

11:

Update Safe Emergency Landing zones capacity

12:

**end if**

13:

Contingency Manager ends

14:

Tactical Conflict Resolution is active

15:

**if** $operation$ **is** $conflicted$ **then**

16:

$operation$ $\gets$ resolution manoeuvre

17:

**end if**

18:

Tactical Conflict Resolution ends

19:

**end for**

At each simulation time step, the in-flight services toolset gathers traffic information from the environment, which the conformance monitoring uses to update the current operational status. This involves classifying the operations’ statuses continuously. As illustrated in Figure 7, an active operation can be either nominal or off-nominal. Off-nominal operations may be categorized as nonconformant, contingent, or conflicted. Conformance monitoring plays a determining role in the collaborative management of operations by delegating tasks to other in-flight services.

### Conformance Monitoring

The conformance monitoring service \[48\] ensures continuous verification of an operation's adherence to its designated OV, enabling early detection of deviations and proactive safety management.

The OV, illustrated in Figure 8, defines the permissible 3D space around the nominal flight plan. It consists of two vertical cylinders of radius $R_{\text{toffl}}$ extending from ground level to cruise altitude at the origin and destination, accommodating manoeuvre tolerances during takeoff and landing.

[$Figure 8. - 
            Illustration of OV geometry and dynamic intent transitions. (a) OV structural components, including takeoff/landing cylinders and lateral/vertical buffers, defining the permissible cruise corridor—OV geometry. (b) Example of intent-based OV progression at two time snapshots, showing how the active segment transitions from $ov_{\text{wpt}}$ to $ov_{\text{wpt}+1}$ along the planned route—Intent OV and segment transition shown at two time snapshots.$](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/62/11554465/11340640/xu8-3652153-large.gif)

**Figure 8.**

Illustration of OV geometry and dynamic intent transitions. (a) OV structural components, including takeoff/landing cylinders and lateral/vertical buffers, defining the permissible cruise corridor—OV geometry. (b) Example of intent-based OV progression at two time snapshots, showing how the active segment transitions from $ov_{\text{wpt}}$ to $ov_{\text{wpt}+1}$ along the planned route—Intent OV and segment transition shown at two time snapshots.

As illustrated in Figure 8(a), these cylinders are connected by a polygonal corridor representing the cruise phase, bounded laterally by a buffer $L_{\text{buff}}$ and vertically by a buffer $A_{\text{buff}}$ that determines the tolerance between two nominal flight levels (FLs). The value of $L_{\text{buff}}$ reflects the vehicle's manoeuvrability, speed, and traffic priority: a smaller volume increases sensitivity to off-nominal conditions but raises false-alert rates, while a larger volume reduces false alerts but may delay anomaly detection (later explored in the “Operation Volume Buffer Sizing” section).

As presented in Figure 8(b), the OV is divided into segments based on the nominal waypoints of the flight plan, with each segment representing an intended OV. Let $\mathcal {P}$ be a permutation-symmetric function that takes the coordinates $(\varphi, \lambda, h)$ of the OV's corner points, as defined by projecting laterally $L_{\text{buff}}$ to the left and right of the two waypoints delimiting the segment, as per [(4)](#deqn4) for a plan with $n$ waypoints. Circular OVs at takeoff and landing are defined solely by $R_{\text{toffl}}$

$$
\begin{equation*}{\left\lbrace \begin{array}{lc}(\varphi _{i,-L_{\text{buff}}},\lambda _{i,-L_{\text{buff}}}), (\varphi _{i,L_{\text{buff}}},\lambda _{i,L_{\text{buff}}}), \\ 
(\varphi _{i+1,-L_{\text{buff}}},\lambda _{i+1,-L_{\text{buff}}}), (\varphi _{i+1,L_{\text{buff}}},\lambda _{i+1,L_{\text{buff}}}) \end{array}\right\rbrace}. \tag{4}
\end{equation*}
$$
 View Source

Horizontal conformance within ov is given by the Boolean $\mathcal {L}_{\text{ov}}$, while vertical conformance is given by $\mathcal {A}_{\text{ov}}$. The combined 3D conformance check $\mathcal {C}_{\text{ov}}$ is defined in in the following:

$$
\begin{equation*}\mathcal {C}_{\text{ov}}(\varphi _{\text{UAS}}, \lambda _{\text{UAS}}, h_{\text{UAS}}) = \mathcal {L}_{\text{ov}}(\varphi _{\text{UAS}}, \lambda _{\text{UAS}}) \cap \mathcal {A}_{\text{ov}}(h_{\text{UAS}}). \tag{5}
\end{equation*}
$$
 View Source

An operation is considered conformant if at least one OV segment, from a flight plan $\mathcal {F}$, satisfies $\mathcal {C}_{\text{ov}}$, as per [(6)](#deqn6). This definition reflects the fact that once a flight plan is activated, the OV is valid over its entire active time window, without enforcing intermediate time checkpoints between waypoints. Consequently, the operation may be located in any authorized segment at a given time, allowing for temporary deviations (e.g., due to conflict avoidance) that exit one segment and re-enter another (either the preceding or subsequent segment) without triggering an irreversible contingency, provided the aircraft remains within at least one permitted OV

$$
\begin{equation*}\exists {\text{ov}} \in \mathcal {F}_{\text{UAS}}, \; \mathcal {C}_{\text{ov}}(\varphi _{\text{UAS}}, \lambda _{\text{UAS}}, h_{\text{UAS}}) \Leftrightarrow \text{Conformance}. \tag{6}
\end{equation*}
$$
 View Source

The service supports both reactive (current-time) and predictive conformance checks. Prediction extrapolates the trajectory forward in time, accounting for uncertainties, such as GNSS noise, weather effects, and manoeuvre delays. If an operation exceeds its OV, then its status changes from *activated* to *nonconformant*. As described in Figure 9, nonconformance can be detected reactively or predicted in advance. In the latter case, a contingency procedure can be triggered before the actual breach occurs.

[$Figure 9. - 
            Reactive versus predictive conformance monitoring and corresponding flight status updates. Both cases start from identical initial conditions and run over equivalent time intervals, but differ in monitoring configuration: reactive monitoring uses timeline $t$ in (a) and (b), while predictive monitoring uses timeline $t^{\prime }$ in (c) and (d). (a) Nominal at $t_{0}$. (b) Nonconformance at $t_{1}$. (c) Predict nonconformance at $t^{\prime }_{0}$. (d) Contingency triggered at $t^{\prime }_{1}$$](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/62/11554465/11340640/xu9-3652153-large.gif)

**Figure 9.**

Reactive versus predictive conformance monitoring and corresponding flight status updates. Both cases start from identical initial conditions and run over equivalent time intervals, but differ in monitoring configuration: reactive monitoring uses timeline $t$ in (a) and (b), while predictive monitoring uses timeline $t^{\prime }$ in (c) and (d). (a) Nominal at $t_{0}$. (b) Nonconformance at $t_{1}$. (c) Predict nonconformance at $t^{\prime }_{0}$. (d) Contingency triggered at $t^{\prime }_{1}$

### Contingency Management

CM ensures high safety, security, and efficiency in operations. A contingent situation arises from a persistent nonconformance status, as shown in Figure 9(d), or through alerts from the operator or the USSP.

Contingency actions are implemented to ensure safety for the contingent vehicle and surrounding traffic. The CM protocol is illustrated in Figure 10 and is initiated by the risk map from the RAA service (recall the “Risk Analysis Assistance” section), which identifies SLZ & ELZ.

**Figure 10.**

Contingency manager workflow.

Once the contingency manager receives operation-specific information, it short-lists feasible SLZ & ELZ based on the contingency level. The nearest unoccupied option is then selected as the new destination and marked as occupied in the database.

The contingent vehicle is considered as a moving obstacle for the rest of the traffic. It is also assumed that the contingent vehicles were semi or fully controllable and operates a conventional landing due to the diverse source of contingency that may restrict vertical landing. Contingency events, their corresponding operational behaviors, and their arbitrarily selected frequencies, chosen to provoke some contingencies while maintaining realism, are summarized in Table 1. Finally, when the contingent operation lands safely, the capacity of the selected SLZ & ELZ is updated back, and the contingency manager block terminates.

**Table 1.** Parameterization of Contingency Events to Generate Operational Perturbations

### Tactical Conflict Resolution

The TcR service prevents midair collisions by managing manoeuvres’ instructions for avoiding conflicting intruders. It addresses short-term conflict scenarios within a short time frame up to 50 s ahead and, in rare cases, responds to safety breaches caused by upstream service failures that compromise safe operations.

In many cases, in-flight conflicts arise when a contingent operation fails to maintain its OV. The affected operation must guide itself to an SLZ & ELZ, often neglecting surrounding traffic due to factors affecting manoeuvrability or situational awareness. This can lead to potential incursions into neighboring OVs, as illustrated in Figure 11. In this illustrative example, aircraft EHG9 loses altitude and encroaches upon the nominal OV of PHAN10, posing a threat. The TcR service issues instructions to the nominal operation, which is temporarily in an off-nominal state due to external factors, in this case, a contingent operation.

**Figure 11.**

Illustration of a tactical conflict scenario from two perspectives. (a) 3D view where a contingent operation (orange) crosses another OV, resulting in a conflict with the nominal operation (blue)—OV incursion with flight status. (b) similar scenario in 2D, highlighting the concentric safety layers (i.e., observation, LoWC, and NMAC) used to trigger TcR—OV incursion with safety layers.

When combined with the CM service (recall the “Contingency Management” section), TcR functions in two modes based on the presence of contingencies. If no contingencies are detected in the observation layer, then the solver remains deactivated. However, if at least one contingency is detected in the traffic, then the solver activates and follows the safety layers shown in Figure 11(b), which include the following.

- *Observation:* Positions of contingent operations are compared with those of surrounding traffic. An operation is considered under observation if it falls within this layer, and the solver acts even if there is no imminent threat.
- *Loss of well-clear (LoWC):* This layer signifies a loss of separation but with relative severity. The solver acts to resolve conflicts at this level.
- *Near midair collision (NMAC)*: This represents the highest severity level, where there is a significant risk of collision. The solver is trained to minimize intrusion within this layer to prevent potential midair collisions.

When the Conformance Monitoring or CM services are not provided (as we do in the “Intervention of Tactical Services” section), the TcR service stays alert. It considers any operation within the activation range (i.e., observation) to be an intruder, which triggers the service's mode to switch from dormant to active.

The service centralizes traffic information into an observation vector containing details about the threatened operation and encoded encounter data from both threatened and contingent operations, including parameters, such as separation distance, crossing angle, and relative speed. As illustrated in Figure 12, this information is processed using a long short-term memory network, enabling sequential handling of multiple contingent operations threatening a single aircraft. The resulting observation vector is fed into a shared policy that generates deconfliction instructions, combining altitude manoeuvres in {-50, 0, 50} ft with speed adjustments in {-5, 0, 5} kts. This shared policy forms the core of the TcR decision-making process, implemented via a multiagent reinforcement learning (MARL) system that treats threatened operations as agents requiring deconfliction \[11\]. While MARL is often recognized for its ability to resolve multithreat scenarios, it is equally valuable, and often more practical for solving multiple isolated conflicts within seconds through a single centralized entity.

**Figure 12.**

Conceptual centralized TcR.

This section presents the experimental studies conducted to demonstrate the proposed advanced UTM services. It begins with the evaluation metrics in the “Evaluation Metrics” section, followed by the experimental setup in the “Setup” section. The subsequent sections report the results: the “Results—Combination of UTM Services” section presents the progressive combination of UTM services and their full capabilities, while the “Results—Sensitivity Analysis” section focuses on a sensitivity analysis assessing the influence of different control variables across services. The complete dataset for these experiments is available in an online repository \[49\].

### Evaluation Metrics

This section presents the key metrics for evaluating the efficiency of UTM services, categorized into four KPAs: Safety, path efficiency, and workload. Safety is the top priority in research deployment. While this is time-based, the TcR service emphasizes in-flight separation and its distribution. Following the American Society for Testing and Materials (ASTM) guidelines for UAS detect and avoid systems, the LoWC and near midair tolerances are established at 2000 and 500 ft, respectively.

Preflight services also focus on path efficiency in flight plan design. Delay measurements in minutes are evaluated through rerouting and rescheduling, guided by the operation plan preparation and optimization, ScR, and DCM services. In addition, RAA affects cost efficiency with geofence restrictions that necessitate rerouting.

This study also introduces conceptual metrics to evaluate the potential workload associated with operations, which are categorized by flight status that reflects the frequency of vigilance required by the USSP. The process of changing status and in-flight interactions contribute to this workload, primarily described in the conformance monitoring service, in conjunction with the CM service.

Drawing inspiration from EUROCONTROL's complexity metrics for ANS Providers (ANSPs) \[50\], this research attempts to adapt them to UTM as follows.

- *Interactions:* The accumulated number of simultaneous operation in the airspace is defined through unidirectional comparisons at each timestep.
- *Horizontal different interacting flow (HDIF):* The interactions per flight hour for operations at the same FL within a 5 NM range.
- *Vertical Different Interacting Flows (VDIF):* The interactions per flight hour during operations transitioning to or from the same FL with a vertical separation of under 160 ft ($A_{\text{buff}}$) and within 5 NM horizontally.
- *Speed different interacting flows (SDIF):* The interactions per flight hour for operations with a speed difference greater than 15 kts within a 5 NM range.
- *Adjusted sensity:* The traffic over a specific period, indicating the ratio of interaction hours to flight hours.
- *Concentration:* The distribution of traffic within the airspace using the ratio of adjusted to raw densities.
- *Structural index:* The traffic flow structure as the sum of the relative HDIF, VDIF, and SDIF indicators.
- *Complexity score:* The complexity of operational environment by means of multiplying the adjusted density with the structural index.

### Setup

All the case studies in this experiment are based on a synthetic, large-scale scenario representing a portion of the airspace managed by a USSP, which we refer to as our research deployment.

This airspace, as shown in Figure 13, covers 115 NM <sup>2</sup> with dimention of 12.5 by 9.2 NM, and incorporates four discrete FLs at 657, 821, 985, and 1150 ft, which are the nominal altitudes of each level. Each operation is preassigned one FL by the preflight services, with HPVs allocated to the highest level and SPVs distributed across the remaining three to balance demand. The planned cruise altitude corresponds to the nominal altitude of the assigned level, with a control tolerance of $\pm 80$ ft for tracking. This defines a vertical band of $[z_{i}-80,\,z_{i}+80]$, giving $A_{\text{buff}}=160$ ft. Vehicles do not cruise between levels, except short climb/descend segments occur only to change from $z_{i}$ to $z_{j}$ when commanded by takeoff, landing, rerouting, and TcR.

**Figure 13.**

Airspace configuration.

Upon receiving flight plans from preflight services, a random vehicle model is assigned to each operation based on the vehicle performance (HPV or SPV) outlined in Table 2. To assess the CM service, synthetic failure events have been created, as detailed in Table 1. The DCM service employs a grid-based partition to calculate the cost of each airspace cell shown in Figure 13. ScR sets the separation minima to 15 min. The TcR service uses a shared policy trained through an MARL system based on Model 7.0 from previous work \[11\].

**Table 2.** Vehicle Performance and OV Size

### Results—Combination of UTM Services

This section presents the experimental evaluation of different combinations of UTM services, as summarized in Table 3. Three categories of preflight service combinations are introduced, corresponding to three sets of flight plans: Initial, intermediate, and optimal (noted “ini,” “Inter,” and “OPT,” in the table).

**Table 3.** Combination of Advanced UTM Services in the Experiments

First, the initial set considers only OPP, then the intermediate set adds RAA and DCM to the flight authorization. Finally, the optimal set completes the authorization process with ScR.

We index scenarios as P.I, where P encodes the preflight service bundle and I encodes the in-flight bundle. A value of 0 indicates that the corresponding bundle is disabled. For example, 0.0 is our benchmark (no services).

In this set of experiments, each configuration detailed in Table 3 is evaluated under three traffic densities: low (50 operations), moderate (100 operations), and high (150 operations). One-fifth of the operations are HPVs, which operate at the highest FL (i.e., 1150 ft), while the remaining operations consist of SPVs distributed across the three lower FLs.

The structure of this section is summarized as follows. First, the “Initial versus Optimal Flight Planning” section focuses on comparing the quality of flight authorizations involving different preflight services, considering both safety and flight efficiency aspects. Then, the “Flight Planning Impacts at the Tactical Level” section examines the safety implications of these flight authorizations at the tactical level. The “Intervention of Tactical Services” section investigates the performances of in-flight services in the absence of most of preflight services. Finally, the “Unified UTM Services” section presents the results when all UTM services are jointly activated.

#### Initial Versus Optimal Flight Planning

In this section, we compare the initial (“ini”) and optimized (“OPT”) flight plans, as detailed in Table 3. Key performance metrics for these operations, across low, moderate, and high traffic densities, are then summarized in Table 4.

**Table 4.** Comparison of Flight Planning Performances With (“OPT”) and Without (“ini”) Provision of Preflight Services

We begin by evaluating the effectiveness of the RAA service based on the order of services applied. In three traffic scenarios, 26, 56, and 83 operations from the initial flight plans were identified as passing through high-risk areas, comprising over half of the operations in each scenario. The total high-risk feedback suggests that some operations have only one segment with unacceptable risk, while others have multiple high-risk segments. Compared to the optimized results, all high-risk operation segments have been successfully cleared through rerouting.

Rerouting issued by the DCM service reflects how many operations have been affected with alternative routes to bypass hotspot areas. As mentioned earlier, the optimization model calculates the new route in identifying the lowest cost solution. Table 4 shows that in a low traffic density scenario, a unique operation was rerouted, while in a high traffic density scenario, seven operations were rerouted. Furthermore, the average route distance may be affected by the RAA and DCM services, as operations can be rerouted after evaluation by these services.

Analyzing all submitted flight plans, we found 21, 61, and 101 conflicting operations in the initial experiments without the ScR service. All conflicts can be effectively resolved using this service, as indicated in the optimized result columns.

#### Flight Planning Impacts at the Tactical Level

Based on the preflight service configurations that generated the initial (“ini”) and optimized (“OPT”) flight plans, this section examines their effects during real-time, simulated operations. Figure 14 shows how the number of simultaneous operations evolves under our traffic scenarios. “ini” corresponds to benchmark Scenario 0.0, while “OPT” is Scenario 3.0. The intermediate configurations (“Inter”) are Scenarios 1.0 and 2.0 (refer to Table 3).

**Figure 14.**

Preflight services effects on airspace occupancy. (a) Low traffic density. (b) Moderate traffic density. (c) High traffic density.

Consistent with the delay statistics in Table 4, the addition of ScR (in Scenarios 2.0 and 3.0) produces larger, but more evenly distributed delays in the moderate and high-density cases. In contrast, DCM's effect alone on flight efficiency is minimal, evidenced by the near overlap of the cyan and magenta curves in Figure 15. DCM stands out only under low-density traffic: while ScR also introduces some delay in this case, the effect is modest. DCM yields the lowest sustained number of simultaneous operations but exhibits the highest peak (13 aircraft around 90 min).

As expected, the absence of ScR results in intense traffic in shorter scenarios, as visible for the “ini” configuration and Scenario 1.0 in blue. Figure 14 illustrates the distribution of in-flight separations between pairwise operations across various traffic: “Low,” “Med,” and “High” for the respective densities. These separations are determined for pairs operating simultaneously at the same altitude. Since all conflicts are resolved by preflight services in the optimized flight plan, the minimum separations in all optimized groups exceed those in the initial group, thereby meeting the safety separation threshold. In addition, the average separation in all three scenarios has increased after processing by the preflight services, with the high traffic density scenario showing a more significant improvement. Although the overall comparison shows high similarity, the “ini” configuration shows the most hazardous separations, visible with its first quartile that lies closest to zero.

**Figure 15.**

Separation distributions over various traffic densities.

#### Intervention of Tactical Services

The previous section presented simulated operations under the three preflight configurations, which are “ini,” “Inter,” and “OPT,” assuming nominal conditions without any real-time monitoring. In this section, we explore how tactical (in-flight) services can enhance and adapt operational performance relative to those preflight plans through three experiments.

In the first experiment, we evaluate the safety benefits of TcR on flight plans that have not been deconflicted (i.e., no ScR). Figure 16 compares our benchmark Scenario 0.0 (no in-flight services) with Scenario 0.1, in which TcR engages whenever horizontal separation drops below 6000 ft or vertical separation below 100 ft.

**Figure 16.**

Pairwise separation clusters for the “ini” flight plan under three traffic densities (Scenario 0.1), illustrating the safety impact of TcR. Red markers show separations without TcR, whereas green markers show separations with TcR fully active. Points in the lower left region indicate the most hazardous (closest) encounters. (a) Low traffic density. (b) Moderate traffic density. (c) High traffic density.

In the low-density case illustrated in Figure 16(a), both curves show some loss of separation, but TcR notably increases the minimum horizontal spacing between the closest aircraft. Under moderate density \[see Figure 16(b)\], TcR “pushes back” operations even further apart horizontally, reducing collision risk. At high density \[see Figure 16(c)\], TcR alone cannot fully prevent NMAC events (horizontal separation <500 ft), although its vertical separation adjustments still avert some overlaps that occur when TcR is inactive.

The second experiment examines the synergy between conformance monitoring and CM services through Scenario 0.2. Its goal is to demonstrate how conformance monitoring can spot off-nominal operations and how CM can respond to these situations. We primarily focus on the workload aspects of the operations as a service provider point of view. Contingency events are based on the failure rates and protocols listed in Table 5. An interaction is considered to involve a pair of operations if at least one is under off-nominal conditions. This indicates that arbitrary failure rates yield a contingency occurrence rate of up to 3% in the busiest scenario. While this does not reflect real-world UAM expectations, it likely overestimates for testing purposes.

**Table 5.** Operation Flight Status Distribution and Interactions Based on “ini” Flight Planning (Scenario 0.2)

Table 5 quantifies this workload across different traffic densities, highlighting how potential workload escalates with higher density due to increased interactions and risk of separation loss. Conformance monitoring manages flight status to reduce workload and enhance safety through a set of control variables related to OV, including size and sensitivity of nonconformance activation. In Scenario 0.0, without any service, the USSP must closely monitor operations of 243, 972, and 2345 thousand flight interactions for the respective densities. According to the same table, conformance monitoring reduces this by 679, 259, and 260 times, respectively. These results are sensitively influenced by the frequency of off-nominal situations.

The framework in the “High-Level UTM Simulation Framework” section reminds that the activation of the in-flight services is relying on the monitored flight status of the operation considered by the service. For the third experiment, Table 6 summarizes the distribution of the different flight status met for the different densities of traffic and the most critical situation for each: the minimum separation observed between a pair of operations and their respective flight status.

**Table 6.** Operation Flight Status Distribution and Highest Safety Critical Situation With In-Flight Monitoring Based on “ini” Flight Planning (Scenario 0.3)

Off-nominal operations (i.e., nonconformance or contingency events) remain anecdotal compared to nominal operations, which account for nearly 99% of the operational lifecycle. While off-nominal cases exhibit relatively safe separations, with no NMACs and only a few LoWCs, nominal operations reveal hazardous separation minima, reaching as low as 647, 325, and even 7 ft, as shown in Figure 16.

#### Unified UTM Services

We evaluate the integrated system, with all in-flight services running concurrently alongside OPT-based flight planning. Experiments are restricted to moderate traffic density to focus on safety outcomes. Figure 17 compares separation distributions for the baseline with no services (i.e., Scenario 0.0) versus all services enabled (i.e. “All”). Figure 18 further stratifies separations by flight operation-pair flight status and clusters them.

**Figure 17.**

Horizontal and vertical separation distributions for all flight operation pairs with no services (i.e., blue distribution) and with all in-flight services enabled (i.e., purple distribution). Top and right histograms show marginal separation distributions; the main scatter plot depicts pairwise separation values, with lines indicating clustered vertical levels.

**Figure 18.**

Clustered horizontal separations by encounter flight-status pairings. Percentages on the horizontal axis indicate each pairing's share of total encounter time, while colors show separation bins, with a green-to-black gradient indicating increasing severity.

First, we observe a clear reduction in simultaneous operations when all services are enabled relative to the baseline with no services. Across all horizontal separations the purple distribution is markedly lower, while both conditions retain a similar peak at 2–4 NM, encounters below 0.3 NM become nearly absent. Vertically, separations concentrate at 200 and 300 ft with no material change in proportions, suggesting that flight planning was not significantly altered in the FL assignments by preflight services or, at least, was fairly distributed.

In this experiment, nominal operations account for approximately 85% of total flight time, while off-nominal conditions exceed 15%. Contingent flights remain well separated from surrounding traffic, with the minimum horizontal separation is above 0.5 NM. As a result, no TcR activations were required, even across repeated runs. Nonconformance occurs only occasionally (less than 2 min over tens of flight hours) and maintains safe separations. Consistent with Table 6, encounters between contingent flights are the most critical, as trajectory changes may be infeasible. By contrast, OPT-based planning shows substantially larger safety margins.

Using the ATM-derived complexity metrics adapted to UTM, enabling all UTM services reduces overall complexity by 4.4 times (see Table 7). Hours of interactions, adjusted density, and concentration are each roughly halved. HDIF drops by 63%, while speed and vertical differentials decrease more modestly. The structural index falls by 56%.

**Table 7.** Complexity Metrics for a Moderate Density Airspace, Comparing No Services (I.e., Benchmark Scenario 0.0) Versus All UTM Services Enabled (I.e., Scenario “all”)

### Results—Sensitivity Analysis

We conducted sensitivity experiments to quantify how key control variables affect service performance: Geofence (obstacle) radius in the “Geofence Sizing” section, separation minima in the “Operation Separation Minima” section, buffer sizing and conformance look-ahead time in the “Operation Volume Buffer Sizing” section, and TcR activation range together with progressive operational failure rate in the “Dependence Against Contingencies” section.

#### Geofence Sizing

The size and location of the geofence around potential obstacles provide feedback for the RAA service to direct flights away from high-risk areas. The radius is determined by the risk level of the flight segment. For operational efficiency, the geofence is modeled as a cylinder, with the obstacle radius sometimes restricted to prevent major deviations from the flight plan. By keeping the radius within a certain range, risks are mitigated while minimizing unnecessary detours.

The cost-efficiency of the geofence radius on the RAA service is shown in Figure 19. It uses the average flight distance in a moderate density configuration to demonstrate the effects of geofence sizing. The impact of the radius on flight distance is expected to follow a similar trend in the other two traffic density scenarios, which is why this article focuses on moderate traffic density. As mentioned in the “Operation Plan Preparation and Optimization” section, the initial flight plan produced by the operation plan preparation and optimization service results in the shortest trajectory distance.

**Figure 19.**

Impact of geofence radius on SPV (i.e., black) & HPV (i.e., blue) routing and operational endurance.

The average distance for both SPVs and HPVs without RAA is the smallest among all radius values. Changes in average flight distances are minor when the maximum allowed radius ranges from 300 to 500 m. Without a radius limit, SPVs and HPVs can operate at maximum distances of 1390 and 994 m, respectively, leading to a significant increase in average distances. However, the overall impact of the geofence radius on distance remains relatively minor.

#### Operation Separation Minima

As discussed in the “Strategic Conflict Resolution” section, time-based separation is used to identify conflicts between operation pairs in the same airspace volume. Therefore, the separation minima significantly affect the strategic conflict management service regarding delay allocation and conflict resolution. In addition, safety separation may influence subsequent TcR services. To explore the relationship between these two services, we conducted sensitivity experiments varying safety separation minima while keeping other factors constant.

We first examine how separation minima affect ScR services under various traffic scenarios. As shown in Figure 20(a), increasing the safety separation minima leads to longer delays, particularly at higher traffic densities. Typically, a 5-min increase in separation minima results in a delay increase of 1.5–2 times. Transitioning from a 5-min to a 10-min safety interval causes a more pronounced delay increase, as a 5-min interval allows most flights to operate conflict-free, minimizing delays.

**Figure 20.**

Impact of ScR separation minima on operations. (a) Average flight delay for three traffic densities—Effects on flight delay. (b) Minimum observed in-flight separation, with and without TcR—Effects on minimum in-flight separation..

We operate various flight plans based on four separation minima: 5, 10, 15, and 20 min, to evaluate the behavior of the TcR service. Figure 21 compares the four scenarios with (TCR) and without (No TCR) the service, displaying separation distribution. The TcR service enhances in-flight separation similarly to Figure 14, even when flight plans are already deconflicted. It eliminates separation below 2000 ft when employing a 10-min minimum or greater. The impact of a 5-min separation minimum is more contentious, as it slightly increases vertical separation beyond 1500 ft, while the initial scenario indicates horizontal separation just below 1500 ft. This analysis is illustrated in Figure 20(b), which compares in-flight separation with the minima set by the ScR service.

**Figure 21.**

Safety impact of separation minima, issued by the ScR, on in-flight separations. Pairwise separations for all active aircraft encounters in a moderate density scenario under varying strategic separation intervals (5, 10, 15, and 20 min). Left-side figures \[see Figure 21(a), (c), (e), and (g)\] present the results without TcR, while the corresponding right-side figures \[see Figure 21(b), (e), (f), and (h)\] show the results with active TcR. (a) Without TcR—5 min. (b) With TcR—5 min. (c) Without TcR—10 min. (d) With TcR—10 min. (e) Without TcR—15 min. (f) With TcR—15 min. (g) Without TcR—20 min. (h) With TcR—20 min.

#### OV Buffer Sizing

This analysis emphasizes the safety implications of the OV's buffer size, particularly in managing nonconformance sensitivity. A smaller OV improves situational awareness by being more responsive to deviations, allowing for timely decision-making during off-nominal conditions. However, while a smaller volume with a larger separation minima enhances responsiveness and safety, it may lead to undesirable nonconformance statuses if the buffer size does not align with the flight envelope. Figure 22 illustrates the proportion of undesirable nonconformance statuses as prediction time varies from 5 s to 2 min.

**Figure 22.**

Effects of buffer size on conformance prediction.

Prediction time for conformance significantly influences the frequency of false nonconformance alerts. All three buffer size configurations identify nonconformance in about 73% of operations. The remaining 27% occur during stable in-cruise phases, where the trajectory remains unchanged. While predicting nonconformance based solely on time-ahead calculations with current navigational data is straightforward and safe, it results in a high rate of false alarms, making it less effective. Even with a doubled buffer size, nearly 1% of operations still face these alerts.

#### Dependence Against Contingencies

This analysis examines the resilience of CM and TcR services in chaotic environments. It builds on the findings in the “Results—Combination of UTM Services” section, highlighting limitations in interpreting the benefits of TcR for mitigating contingent encounters. According to the standard failure rates, the failure rate has increased by up to four times. Figure 23 depicts the separation distribution between pairs of off-nominal operations. Specifically, Figure 23(a) focuses on interactions between contingent aircraft, while Figure 23(b) examines conflicts involving operations that observe surrounding contingency scenarios. These are analyzed based on activation ranges set between 0.3 and 1 NM.

**Figure 23.**

Pairwise in-flight separations under escalating contingency events and varying tactical conflict detection sensitivity. (a) Contingent–Contingent. (b) Conflicted–Contingent.

No evident correlation is observed between the number of simultaneous contingent operations (i.e., interactions) and failure rates. This sensitivity analysis is constrained by the randomness of failure events, which can be rapidly mitigated when operations are near SLZ & ELZ, even as the number of contingencies may increase. This is evident in Figure 23(a), where doubling the failure rate results in fewer interactions between pairs of contingent operations. However, a fourfold increase in the standard failure rates leads to chaotic scenarios, with a significant proportion of traffic becoming contingent. Despite these challenging circumstances, separations generally remain safe, with only a few instances of operations breaching the well-clear tolerance, which did not escalate into more severe issues.

Despite the chaotic conditions observed in high failure rate scenarios, the TcR service remains largely inactive, irrespective of the activation range settings. Specifically, across multiple high traffic density scenarios, no TcR was triggered when the activation range was set strictly below 0.8 NM. As illustrated in Figure 23(b), interactions between conflicted operations managed by the service and contingent operations occurred over brief intervals without any loss of separation. The broad separation distribution observed under a doubled failure rate highlights cases where separations exceed the activation range, with some operations maintaining distances as large as 10,000 ft.

This section is organized as follows. The “Key Outcomes” section presents the experimental outcomes along with a cross-analysis of the results. The “Limitations” section highlights the main limitations and challenges, and the “Future Work” section discusses directions for future work.

### Key Outcomes

Across all experiments, total delay and the number of affected operations grow with traffic density as depicted in Table 4. Under an FCFS regime, early delay allocations propagate to subsequent flights and amplify both average and maximum delays, especially in the moderate and high-density cases. Sensitivity to separation minima reinforces this: increasing the strategic threshold raises delay nonlinearly, as illustrated in Figure 20, where separation minima from 5 to 10 min step often causing a marked jump. These results highlight the importance of coupling strategic deconfliction with policies that minimize knock-on effects in congested periods.

Conformance monitoring and CM are central to safe operations but also drive provider workload: every status change and interaction are a potential distraction or triggers downstream action as detailed in Table 5. The effectiveness of conformance monitoring depends on timely, trustworthy inputs from both preflight authorizations and in-flight state estimates. If a nondeconflicted plan bypassed ScR, an incipient hazard could be masked and go unmitigated. Our buffer-sizing analysis in the “Operation Volume Buffer Sizing” section further shows that low time-ahead conformance prediction can lead to high false-alert rates. To mitigate alert fatigue, buffer size, and look-ahead should be tuned to the flight envelope, and ideally, trajectory-aware predictors should be employed.

As shown in Figure 17 when all UTM services are enabled, we observe a clear reduction in simultaneous operations and a healthier separation profile relative to the baseline. The distributions highlighted in the results suggest that preflight services did not materially distort FL allocations. In the same experiment, among nominal–nominal encounters the vast majority exceed 1 NM, although short-lived passes at 0.15 and up to 0.3 NM (about 35 s) appear across adjacent FLs and would be benign unless an off-nominal event arose midencounter. Encounters involving contingencies remain mostly above 0.5 NM, and repeated runs required no TcR activations at the tested settings, consistent with ScR providing adequate strategic margin (see Figure 18, Table 6).

These local separation gains translate to macrolevel simplicity: using ATM-derived metrics adapted to UTM, enabling all services reduces overall complexity as detailed in Table 7. Raw density and flight hours remain essentially unchanged, isolating the effect to service enablement rather than scenario scaling. In scenarios without ScR, TcR increases closest horizontal spacing and mitigates risk across densities but cannot fully offset congestion at high density according to Figure 16, recommending upstream strategic deconfliction.

The design levers behave as expected. Geofence sizing has a modest average impact on route distance and endurance (see Figure 19). Limiting the radius in low-risk areas helps avoid unnecessary detours, whereas allowing larger radii around high-risk obstacles is acceptable provided that endurance margins are maintained. Strategic separation minima present a classic safety–cost tradeoff: larger thresholds raise delays but, together with TcR, eliminate short-range encounters below 2000 ft at 10 min or greater (see Figures 20 and 21). The placement and capacity of SLZ & ELZ also matter in practice: while contingent–contingent separations remained safe in our runs, simultaneous nearby contingencies could exceed system capacity without further safeguards.

### Limitations

This study has several limitations. Results are derived from synthetic scenarios with a single airspace geometry and a simplified traffic mix, which may not capture city-specific constraints. The simulation stack is deliberately simple, idealized vehicle kinematics, perfect communications/sensing, no weather or GNSS degradation, and limited state-estimation error, which can understate corner cases. Failure rates and contingency behaviors are assumed rather than empirically calibrated. Fourth, preflight and in-flight services are only loosely coupled: there is no replanning loop, shared state interface, or latency/quality-of-service contracts ensuring tight coordination within the time window between flight plan approval and operation activation. Human-in-the-loop evaluation is absent, so impacts on UTM providers’ workload, trust, and acceptability are not accurately measured. The framework is not integrated with ATM/ATC systems or real aircraft operations. UTM–ATM data exchange (e.g., constraints, advisories, and tactical clearances) and operational collaboration with ATC are not represented. Detailed aircraft-performance models (energy, climb/descent envelopes) are not yet embedded in curvature or level-assignment constraints. These factors limit external validity and policy transferability. Finally, although the underlying framework includes DT capabilities, such as live–virtual–constructive integration and real-time mirroring—these features were only partially employed in this study. The current deployment relied primarily on simulation, without exploiting full DT mechanisms, which limits the extent to which DT benefits are demonstrated in the results.

### Future Work

A practical next step is to close the loop by feeding real-time insight back into some preflight services during the time window between flight plan approval and operation activation. This would allow dynamic updates to operation plan preparation and optimiation with temporary restrictions, refresh risk maps as SLZ & ELZ occupancy changes, and pass predictive conic envelopes of contingent trajectories to ScR to pre-empt conflicts.

We also plan more advanced simulations to stress services under richer interactions, such as mixed vehicle classes, interacting contingencies, stochastic failures and to run human-in-the-loop studies. These will help identify which services can be safely automated and those requiring human supervision, and quantify effects on workload, trust, and performance.

Beyond this, we aim to tighten collaboration between preflight and in-flight modules via shared APIs and latency budgets, enabling real-time capacity updates and sustainable coordination in an integrated ATM/UTM R&D testbed. We will broaden scope to include additional operational features (e.g., noise or privacy constraints) and scaling to city-wide, federated providers.

Finally, we intend to establish open, reproducible benchmarks and KPIs for UTM services, together with datasets and reference implementations in light of latest progress, to support comparative research and inform stakeholders. Parallel efforts will incorporate detailed aircraft-performance models into curvature constraints and validate findings with real geofences and operational data.

This study introduced a cosimulation environment that integrates a comprehensive suite of collaborative UTM services, enabling realistic and scalable evaluation of their performance. Across more than 1600 simulated flight hours, the framework demonstrated the ability of advanced UTM services to manage high-density urban airspace, handle complex contingencies, and maintain operational safety. The results highlight both the strengths and the boundaries of these services, showing the need for continued integration research, adaptive decision-making algorithms, and robust benchmarking methods to support the transition from conceptual designs to deployable UTM systems.

### ACKNOWLEDGMENTS

The opinions expressed herein reflect the authors view only. Under no circumstances shall the SESAR Joint Undertaking be responsible for any use that may be made of the information contained herein.