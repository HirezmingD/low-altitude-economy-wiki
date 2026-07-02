---
title: "Digital Twin-Based SIM Communication and Flight Control for Advanced Air Mobility"
source: "https://ieeexplore.ieee.org/document/11073085"
author:
published:
created: 2026-07-01
description: "Electric Vertical Take-off and Landing vehicles (eVTOLs), as a core component of Advanced Air Mobility (AAM), are expected to revolutionize future urban transpo"
tags:
  - "clippings"
---
## Abstract:

Electric Vertical Take-off and Landing vehicles (eVTOLs), as a core component of Advanced Air Mobility (AAM), are expected to revolutionize future urban transportation by...

---

Advanced Air Mobility (AAM) is gaining significant attention and is expected to become a reality in the near future. Originally proposed by National Aeronautics and Space Administration (NASA), AAM focuses on transporting people and goods through low-altitude airspace and is anticipated to flourish by 2030, driven by advancements in Communication, Computing, and Control (3C) technologies \[1\].

The core component of Advanced Air Mobility (AAM) is Air Traffic Control (ATCo), managed by ground-based ATCo stations \[2\], which are responsible for optimal flight control schedules, including the design of electric Vertical Takeoff and Landing (eVTOL) trajectories and the allocation of communication resources. Moreover, the Federal Aviation Administration's (FAA) Innovate28 (I28) initiative emphasizes that the safe operation of eVTOLs depends on the efficient, clearly defined, and non-overlapping design of air corridors \[3\]. While these corridors enhance operational safety and efficiency, they also introduce two key challenges: ground-to-air (G2A) communications and flight control scheduling.

Existing terrestrial networks, which are primarily designed to serve ground users, face significant challenges in supporting aerial users such as eVTOL vehicles. To address this limitation, emerging technologies like 6G-oriented Holographic Multiple Input Multiple Output (HMIMO) systems have gained attention as promising solutions, and single-layer metasurfaces may restrict the performance of HMIMO systems. In contrast, Stacked Intelligent Metasurfaces (SIM), which consist of multiple metasurface layers, provide greater beamforming flexibility, enabling more effective signal tracking for highly dynamic eVTOL operations \[4\].

Regarding flight control, urban airspace introduces unique challenges for eVTOLs, particularly due to the presence of dynamic obstacles such as other aircraft and birds. Effective flight control systems must be capable of rapidly and adaptively responding to these moving hazards while maintaining safe and efficient flight operations. This study focuses on tactical scheduling within predefined air corridors, serving as a complement to pre-established strategic plans. To design the flight control algorithm, we adopt the Artificial Potential Field (APF) method, which generates attractive forces to guide eVTOLs toward their destinations and repulsive forces to avoid obstacles \[5\].

Besides, both SIM-based beam tracking and eVTOL tactical scheduling require significant computational resources for real-time optimization, which are constrained by the limited onboard processing capabilities of eVTOL platforms. Digital Twin (DT) technology offers a compelling solution \[6\], enabling the replication of physical systems within a virtual environment for efficient testing, analysis, and optimization, without posing risks to real-world operations. In the proposed framework, DTs are employed to iteratively optimize both SIM beamforming and eVTOL flight control, leveraging virtual simulations to enhance real-time performance.

### A. Contribution

This paper presents a DT-based framework for the joint optimization of SIM communication and eVTOL flight control, which tackles two fundamental challenges: ensuring robust G2A communication and enabling efficient navigation within predefined air corridors. The main contributions of this study are as follows:

- We propose a novel two-step iterative method to optimize SIM-based G2A communication between ATCo stations and eVTOLs. This approach enables dynamic beam tracking of eVTOL trajectories within predefined corridors, maximizing G2A transmission rates while adapting to varying SIM configurations. Simulation results show that SIM-based communication significantly outperforms conventional MIMO systems, primarily due to the enhanced beamforming accuracy offered by configurable multi-layer phase shift components, which better accommodate the mobility of eVTOLs.
- We develop a Deep Q-learning Network (DQN)-based Composite Potential Field (CPF) method to ensure both safe aviation and robust communication connectivity. By dynamically adjusting the hyperparameters governing target tracking, safe separation, and communication-aware potential fields, the CPF method enables eVTOLs to navigate complex-shaped corridors safely and efficiently. This adaptive flight control mechanism responds effectively to real-time environmental changes, minimizes DT synchronization overhead by transmitting only key hyperparameters, and is well-suited for deployment in dynamic urban airspaces.
- We propose a DT-based optimization framework that consists of two DT modules: the SIM DT, which emulates the physical behavior of the SIM antenna system, and the eVTOL DT, which captures the real-time dynamics of eVTOLs. By offloading optimization tasks to these virtual counterparts, the framework enables eVTOLs to autonomously maintain reliable connectivity, navigate predefined corridors, and avoid collisions based on precomputed trajectories. Leveraging the global situational awareness and computational capabilities of ground-based ATCo servers, the DT-based framework enhances airspace safety and efficiency while significantly reducing the computational burden on eVTOL onboard systems.

The remainder of the paper is organized as follows: Section II reviews related work. Section III introduces the system model. Section IV presents the proposed optimization solutions for SIM-based communication and eVTOL flight control. Section V provides performance evaluation through simulations and analysis. Finally, Section VI concludes the paper.

Literature related to this work can be categorized into: (i) AAM investigation, (ii) UAV/eVTOL-enabled network architecture design, (iii) communication and flight control joint optimization, (iv) SIM-enabled communication analysis, (v) DT-based applications in low-altitude airspace management, and (vi) Some other flight control analysis.

### A. Advanced Air Mobility

Contemporary smart city infrastructures enhance AAM systems through several critical capabilities: Coordinated SIM-5G handovers reduce eVTOL beam-tracking latency, enabling safe operations in dense urban canyons; City fog networks improve real-time digital twin (DT) synchronization \[7\]; IoT sensor grids provide live traffic/weather data for air corridor flight optimization \[8\]. Concurrently, eVTOLs serve as mobile aerial platforms delivering diverse smart city services, including: Emergency response and medical supply delivery \[9\]; Hyperlocal air quality mapping \[10\]; and 3D city model construction. The integrated manufacturing, transportation, and service ecosystems underpinning AAM and smart cities are emerging as vital economic catalysts for regional industrial integration and employment growth \[11\].

Notably, \[12\] demonstrates that segregating traffic across distinct flight corridors ensures airspace safety and efficiency. Consequently, Urban Air Mobility (UAM) flight optimization should prioritize safety, stability, and communication efficiency within designated air corridors. Nevertheless, a significant research gap persists in corridor-specific flight control methodologies addressing safety-communication tradeoffs.

### B. UAV-Enabled Network

Authors in \[13\] proposed an alternating iterative algorithm to maximize the minimum user throughput in multi-UAV-assisted wireless networks by jointly optimizing cache placement, UAV trajectory, and transmission power. Building upon this foundation, \[14\] investigated uplink-downlink decoupled user association and formulated a sum-rate maximization problem, which was solved using a multi-agent deep reinforcement learning framework. Similarly, the study in \[15\] introduced a collaborative mobile edge computing system that jointly optimized UAV trajectory planning and resource allocation to minimize latency and energy consumption. Additionally, \[16\] analyzed the interaction between UAVs and ground base stations via a stochastic Stackelberg game under incomplete information, aiming to improve service delivery in heterogeneous terrestrial-aerial networks.

While these studies underscore the effectiveness of distributed optimization techniques in UAV-enabled networks, they generally overlook the stringent operational constraints imposed by regulated air corridors, which are critical for safe and compliant eVTOL deployments in urban airspace.

### C. Communication and Flight Control Joint Optimization

Authors in \[17\] jointly optimized eVTOL flight paths and user associations to maximize throughput, while authors in \[18\] proposed an energy-efficient circular trajectory design algorithm to balance the propulsion costs and communication performance. Authors in \[19\] integrated diffusion model-enabled deep reinforcement learning with DT technologies to improve UAV-enabled secure communications and reduced the swarm flight energy consumptions. The work in \[20\] aimed to jointly optimize the UAV's trajectory and computation offloading strategy, while accounting for the UAV's energy consumption and the users' quality of service (QoS) requirements. In \[21\], the authors analyzed a joint optimization problem which simultaneously considers UAV trajectory design and channel selection. Authors in \[22\] investigated the problem of data scheduling and UAV trajectory planning in UAV-assisted communication systems. A novel approach was proposed in \[23\] to enhance the anti-jamming capability of UAV-assisted wireless data collection by jointly optimizing the data collection schedule, power control, and UAV trajectory.

However, extant studies largely neglect the dynamic obstacles in the airspace, like drones/birds that create risks of collision and signal blocking. Moreover, they also ignore the operational constraints of aviation-mandated flight corridors, a gap this paper explicitly addresses through joint communication-flight control optimization.

### D. SIM-Enabled Communication Analysis

Reconfigurable Intelligent Surfaces (RIS) have garnered significant attention for enhancing communication QoS through cost-effective signal manipulation \[33\]. Evolving from conventional RIS, active RIS architectures embed radio frequency circuits into metasurfaces, paving the way for HMIMO systems. HMIMO enables software-defined wavefront shaping via fine-grained phase control, offering precise beamforming capabilities well-suited for UAV and eVTOL networks. For example, \[34\] proposed a Lyapunov-guided reinforcement learning strategy to improve secrecy and energy efficiency in RIS-assisted UAV communications. Nevertheless, the beamforming flexibility of single-layer metasurfaces is inherently limited \[35\]. Stacked Intelligent Metasurfaces (SIM) address this limitation by incorporating multiple metasurface layers, thereby offering a higher degree of freedom for forming complex and adaptive beam patterns \[32\]. Recent studies have advanced the understanding of SIM's communication potential; for instance, \[30\] analyzed channel estimation in SIM-assisted multi-user HMIMO systems, while \[31\] introduced a fully analog wideband beamforming approach leveraging SIM, optimizing performance across a broad frequency range while maintaining the simplicity of analog hardware.

Despite these advancements, the integration of SIM into 6G-oriented air-ground communication systems for AAM, particularly within regulated flight corridors, remains underexplored.

### E. Digital Twin

In UAV systems, DT frameworks have been applied to enhance single-agent navigation \[36\] and swarm coordination \[37\]. Authors in \[38\] improved the cooperative perception through DT model migration in vehicular networks, whereas authors in \[27\] ensured secure data offloading in space-air-ground networks via blockchain-integrated DTs. Moreover, the work in \[39\] demonstrated how integrating DT with reinforcement learning can reduce resource consumption in UAV systems. Recent innovations include federated DT frameworks for real-time resource management \[39\], \[40\] and semantic-aware UAV swarm coordination in metaverse environments \[41\]. To explore the potential applications of high-precision digital modeling in the military domain, \[42\] focused on the mission requirements of an individual combat quadrotor UAV, where a comprehensive architecture for the UAV DT system is developed. A review of the applications of DT technology in the field of automated driving testing, summarizes the technical architecture was proposed in \[43\], which identifies key challenges to be addressed, providing valuable references for researchers in the field. Authors in \[44\] proposed a metamodel that enables concrete and operational descriptions of DT deployment, which covers various aspects of deployment, including the specification of hardware and software components, as well as the installation and instantiation tasks involved in deployment processes.

Despite these developments, the integration of DT with SIM and flight control for corridor-constrained eVTOL operations remains an open challenge.

### F. Some Other Related Works in Flight Control Analysis

Authors in \[29\] leveraged electronic conspicuity (EC) data provided by PilotAware Ltd to develop an enhanced collision management system-Drone Aware Collision Management (DACM). This system utilizes a reactive geometric approach to detect and resolve conflicts, enabling time-optimal evasive collision avoidance (CA) maneuvers. With the technological advancement and widespread deployment of the Automatic Dependent Surveillance–Broadcast (ADS-B) system, \[45\] proposed a remote upgrade mechanism for microcontroller unit (MCU) firmware in ADS-B receivers used by ADS-B data processing centers, facilitating maintainability and operational flexibility. Despite ADS-B's pivotal role in next-generation civil aviation traffic management, its lack of built-in encryption and authentication makes it vulnerable to malicious data attacks. To address this, \[46\] introduced a robust anomaly detection method tailored for ADS-B data, based on a hybrid VAE-GAN-LSTM model that captures the temporal and statistical characteristics of broadcasted signals. Additionally, since 2018, the OpenSky Network has expanded its scope to include FLARM messages, a popular collision avoidance technology in light aircraft. In \[47\], the authors presented the OpenSky FLARM dataset, explained the FLARM protocol, and discussed its potential for future research in flight control and situational awareness. Furthermore, Multilateration (MLAT) technology has been widely adopted in civil aviation for its high-precision positioning and ease of deployment. In \[48\], a high-resolution MLAT system was used as a ground-truth reference to analyze the accuracy and detect anomalies in ADS-B position reports, providing valuable insights into system integrity and reliability.

While existing studies have made strides in UAV/eVTOL communication and flight control, few works consider the co-optimization of communication efficiency and trajectory planning under aviation authority-mandated air corridor constraints. This paper bridges this gap by proposing a DT-driven framework that unifies SIM-enhanced beamforming and composite potential field flight control, ensuring both high-throughput connectivity and safe navigation within prescribed corridors. In addition, Table I enumerates the research areas of existing literature and our work.

**TABLE I** Comparisons of Existing Studies Where $\bm {\star }$ Represents Our Work

[$Table I- 
            Comparisons of Existing Studies Where $\bm {\star }$ Represents Our Work$](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/6488902/11264281/11073085/leng.t1-3586998-large.gif)

The primary objective of this paper is to design a novel DT-based system that enables advanced communication and flight control for efficient eVTOL navigation within a predefined corridor, as illustrated in Fig. 1. The proposed DT-based AAM system consists of two types of DTs: (i) a SIM DT, denoted as $DT^{S}$, and (ii) an eVTOL DT, denoted as $DT^{e}$. The $DT^{S}$ is responsible for optimizing the phase shift and transmission power of multiple metasurfaces, while the $DT^{e}$ focuses on refining the flight control parameters.

**Fig. 1.**

DT-based SIM communication and eVTOL flight Optimization.

We consider a scenario in which an eVTOL $m$ requests access to a corridor at time slot $n$. Upon receiving this request, the ATCo station obtains a message containing the eVTOL's current flight states, such as its position $q_{m}[n]$ and velocity $v$. Based on this information, the ATCo station generates a corresponding $DT^{e}$, on its edge server. This server has direct access to the antenna configurations of the SIM modules at the ATCo station, including phase shifts and transmission power levels. These two DTs operate in a collaborative loop: the $DT^{S}$ utilizes the flight trajectory generated by $DT^{e}$, and in turn, the $DT^{e}$ updates its control parameters based on the phase shift and transmission power optimized by the $DT^{S}$.

Once the loop optimization process is complete, the communication and flight control parameters derived from the DTs are transmitted to the corresponding physical entities, such as the SIM antenna and the eVTOL. Specifically, the SIM antenna configurations are updated via the ATCo station's wired infrastructure, while the optimized flight control parameters are delivered to the eVTOL through SIM-based ground-to-air (G2A) communication. This process underscores the critical importance of reliable communication links to ensure timely and accurate execution of control commands.

To ensure reliable and timely communication, we consider a SIM-enabled communication network, where each SIM comprises $L$ metasurface layers, and each layer contains $K$ meta-atoms. Thus, each SIM consists of $L \times K$ meta-atoms, each capable of independently adjusting its phase shift. This enables the SIM to perform precise downlink beamforming for $M$ eVTOLs \[35\], \[49\], and we characterize the SIM configuration using two key parameters: (i) the phase shift matrix $\bm {\Psi }$, which defines the phase shifts of the $L \times K$ meta-atoms, and (ii) the transmission power allocation vector $\bm {P}[n]$, which determines the optimal power distribution among the $M$ eVTOLs.

### A. Digital Twin Modeling

The DT modeling framework used into this work is based on our previous work \[50\]. Specifically, the $DT^{e}$ digitally replicates these key features of the physical eVTOL, including its flight states, $q_{m}[n]$, $v$ and acceleration $a_{cc}$, as well as its communication operations, such as connection conditions $\eta _{nec}$ and quality-of-service (QoS) requirements $\eta _{QoS}$. Accordingly, for eVTOL $m$, the $DT^{e}$ is represented by the tuple $[q_{m}[n], v, a_{cc}, \eta _{nec}, \eta _{QoS}]$. In addition, the operation of $DT^{e}$ involves dynamically adjusting the eVTOL's flight behavior using a set of potential field hyperparameters, denoted by ${k_{tar}, k_{sep}, k_{com}}$, where $k_{tar}$, $k_{sep}$, and $k_{com}$ correspond to the target field, separation field, and communication field hyperparameters, respectively. These hyperparameters enable accurate and adaptive aviation modeling within the predefined corridors.

Similarly, the $DT^{S}$ mirrors the behavior of the physical SIM antenna by replicating its phase shift matrix $\bm {\Psi }[n]$ and transmission power allocation $\bm {P}$. The primary objective of $DT^{S}$ is to optimize these parameters in order to maximize the G2A communication capacity between the eVTOLs and the ATCo station.

As illustrated in Fig. 2, the joint optimization between $DT^{S}$ and $DT^{e}$, both operating on the edge server at the ATCo station, involves three main components: (i) $DT^{S}$ optimization, (ii) $DT^{e}$ optimization, and (iii) loop feedback.

**Fig. 2.**

Flowchart for joint optimization of communication and flight in DT synchronization.

*$\mathbf {DT^{S}}$ Optimization:* The optimization of $DT^{S}$ consists of two steps: first, the transmission power allocation $P[n]$, which is updated using a fractional programming algorithm; second, the phase shift matrix $\bm {\Psi }[n]$, which is optimized via an iterative gradient ascent algorithm. Once optimized, the parameters from $DT^{S}$ are transmitted to $DT^{e}$ to support flight control adjustments.

*$\mathbf {DT^{e}}$ Optimization:* Based on the updated parameters from $DT^{S}$, the $DT^{e}$ computes the optimal potential field hyperparameters ${k_{tar}, k_{sep}, k_{com}}$, which in turn determine the eVTOL's flight trajectory $\mathcal {Q}[n]$.

*Feedback Loop*: The output trajectory $\mathcal {Q}[n]$ generated by $DT^{e}$ is fed into the next iteration of SIM optimization in $DT^{S}$. Additionally, the optimal potential field hyperparameters computed by $DT^{e}$ are transmitted to the physical eVTOL to enable real-time flight control updates. The physical eVTOL, in turn, continuously reports its current flight states back to the ATCo station, allowing the system to correct any bias in the DT-generated trajectory $\mathcal {Q}[n]$. This revised trajectory subsequently influences the next round of SIM optimization in $DT^{S}$, thereby forming a closed-loop co-optimization process.

After several iterations between $DT^{S}$ and $DT^{e}$, the ATCo station finalizes the optimized parameters, including the transmission power $P[n]$, the phase shift matrix $\bm {\Psi }[n]$, and the potential field hyperparameters ${k_{tar}, k_{sep}, k_{com}}$. These parameters are then synchronized with the physical SIM antenna and eVTOLs. On the physical side, the optimized SIM parameters enhance the beamforming performance of the SIM, while the potential field hyperparameters guide the eVTOL's flight along the predefined corridor.

### B. Communication and Trajectory Joint Optimization

In this section, we formulate the joint communication and flight trajectory optimization model for SIM-based communication and flight control system.The location of the ATCo station is denoted as $B = [x^{ATC}, y^{ATC}, 0]^{T}$, where $x^{ATC}$ and $y^{ATC}$ represent the coordinates of the ATCo station along the $x$ - and $y$ -axes, respectively. The $z$ -coordinate is set to 0, indicating that the ATCo station is deployed at ground level.

*eVTOL Trajectory Model*: The eVTOLs are assumed to operate within a predefined corridor over $N$ time slots, with each time slot of duration $\delta$. The location of the $m$ -th eVTOL at time slot $n$, where $n \in [0, N]$, is denoted as $q_{m}[n] = [x_{m}^{eVTOL}[n],\ y_{m}^{eVTOL}[n],\ z_{m}^{eVTOL}[n]]^{T}$. The spatial region of the corridor is defined as $\mathcal {R}{cor}$. Accordingly, the location $q{m}[n]$ must satisfy the following constraints:

$$
\begin{gather*}
\Vert q_{m}[n]-q_{m}[n-1]\Vert \leq V_{\max } \delta, \forall n \in [0,N],\forall m \in [1,M], \tag{1}\\
q_{m}[n] \in \mathcal {R}_{cor}, \forall n \in [0,N],\forall m \in [1,M]], \tag{2}
\end{gather*}
$$
 View Source

where $V_{\max }$ is the maximum velocity of eVTOL, and the initial and destination of the $m$ -th eVTOL are set as:

$$
\begin{equation*}
{\begin{array}{c} q_{m}[0]=f_{m}[0],q_{m}[N]=f_{m}[N],\,\forall m \in [1,M], \end{array}} \tag{3}
\end{equation*}
$$
 View Source

where $f_{m}[0]$ and $f_{m}[N]$ represent the entry and exit positions of the corridor, respectively.

*SIM Communication Model*: We consider that each antenna serves one eVTOL, which implys that the number of antennas equals $M$, and the transmission power of the SIM antenna is subject to the following constraint:

$$
\begin{equation*}
\sum _{m=1}^{M}p_{m}\bigl [n\bigr ]\leq P_{ATC},\,\forall n\in [0,N], \tag{4}
\end{equation*}
$$
 View Source

where $p_{m}[n]$ denotes the transmission power allocated to the $m$ -th eVTOL at time slot $n$, and $P_{ATC}$ represents the total available transmission power of the ATCo station.

Assume that the each SIM comprises $L$ metasurface layers, each containing $K$ meta-atoms. The phase shift of the $k$ -th meta-atom on the $l$ -th metasurface layer at time slot $n$ is expressed as $e^{j\theta _{k}^{l}[n]}$, where $l\in [1,L]$ and $k\in [1,K]$. Consequently, the phase shift matrix for layer $l$ is represented as $\Psi ^{l}[n]={\mathrm{diag}}(e^{j\theta _{1}^{l}[n]},e^{j\theta _{2}^{l}[n]},\ldots,e^{j\theta _{K}^{l}[n]})\in \mathbb {C}^{K\times K}$.

Let $W^{l}\in \mathbb {C}^{K\times K},\forall \, l\ne 1,l\in L$ be the transmission matrix which models the signal transmission between metasurface layers. That is, the transmission vector from the ATCo station's antenna to the first metasurface layer is written as $w_{m}^{1}\in \mathbb {C}^{K\times 1}$. According to the Rayleigh-Sommerfeld diffraction theory \[51\], \[52\], the $(k,k^{\prime })$ -th entry $w_{k,k^{\prime }}^{l}$ of $W^{l}$ is given by,

$$
\begin{equation*}
w_{k,k^{\prime }}^{l}=\frac{d_{x}d_{y}\cos \chi _{k,k^{\prime }}^{l}}{d_{k,k^{\prime }}^{l}}\Bigg (\frac{1}{2\pi d_{k,k^{\prime }}^{l}}-j \frac{1}{\lambda }\Bigg)e^{j2\pi d_{k,k^{\prime }}^{\prime }/\lambda }, \tag{5}
\end{equation*}
$$
 View Source

where $\lambda$ is the wavelength. $d_{k,k^{\prime }}^{l}$ is the distance between the $k$ -th meta-atom of layer $(l-1)$, the $k^{\prime }$ -th meta-atom of layer $l$, and $\chi _{k,k^{\prime }}^{l}$ is the angle between the propagation direction and the normal to layer $(l-1)$. $d_{x}\times d_{y}$ is the size of each meta-atom.

Similarly, the $k$ -th entry $w_{k,m}^{l}$ of $w_{m}^{1}$ is also derived from [(5)](#deqn5). The SIM beamforming matrix $G[n]$ is then given by,

$$
\begin{equation*}
G{[}n]=\Psi ^{L}[n]W^{L}\Psi ^{L-1}[n]\cdots \Psi ^{2}[n]W^{2}\Psi ^{1}[n]\in C^{K\times K}. \tag{6}
\end{equation*}
$$
 View Source

It is worth noting that hardware imperfections may lead to deviations from the theoretical model, but these can typically be corrected during the implementation phase \[49\].

We consider the channel fading $h_{m}^{H}[n] \in \mathbb {C}^{1 \times K}$ from the last metasurface layer of the SIM to the $m$ -th eVTOL at time slot $n$, which is modeled using a Rician fading model \[53\]. The $k$ -th entry of $h_{m}^{H}[n]$, denoted as $h_{m,k}[n]$, is given by

$$
\begin{equation*}
h_{m,k}[n]=\sqrt{\frac{\rho _{0}}{(d_{m}[n])^{\alpha ^{h}}}}\sqrt{\frac{\kappa ^{h}}{\kappa ^{h}+1}}\bar{h}_{m}[n], \tag{7}
\end{equation*}
$$
 View Source

where $\rho _{0}$ is the reference path loss at a distance of 1 m, $\kappa ^{h}$ is the Rician factor, $\alpha ^{h}$ is the path-loss exponent, $\bar{h}_{m}[n]=1$ is assumed without loss of generality \[53\], and $d_{m}[n]$ denotes the distance between the ATCo station to the $m$ -th eVTOL at time slot $n$, where $d_{m}[n] = \Vert q_{m}[n]-B\Vert$.

Let $s_{m}[n]$ denote the transmitted data for the $m$ -th eVTOL at time slot $n$, which is assumed to be independent and identically distributed (i.i.d.) with zero mean and unit variance. Consequently, the received signal $y_{m}[n]$ at the $m$ -th eVTOL is given by

$$
\begin{equation*}
y_{m}[n]=h_{m}^{H}[n]G[n]\sum _{m=1}^{M}w_{m}^{1}\sqrt{p_{m}[n]}s_{m}[n]+\tau, \tag{8}
\end{equation*}
$$
 View Source

where $\tau \sim \mathcal {CN}(0, \sigma _{m}^{2})$ denotes the i.i.d. additive white Gaussian noise (AWGN) at the receiver, with noise variance $\sigma _{m}^{2}$. Thus, the signal-to-interference-plus-noise ratio (SINR) for the $m$ -th eVTOL at time slot $n$ is given by,

$$
\begin{equation*}
{{SINR}}_{m}[n]=\frac{\left|\mathcal {H}^\mathcal {G}_{m}\right|^{2} p_{m}[n]}{\sum _{m^{\prime }=1, m^{\prime } \ne m}^{M}\left|h_{m^{\prime }}^{H}[n] G[n] w_{m^{\prime }}^{1}\right|^{2} p_{m^{\prime }}[n]+\sigma _{m}^{2}}. \tag{9}
\end{equation*}
$$
 View Source

where $\mathcal {H}^\mathcal {G}_{m}=h_{m}^{H}[n] G[n] w_{m}^{1}$. Consequently, the data rate of the $m$ -th eVTOL at time slot $n$ is,

$$
\begin{equation*}
R_{m}[n] = \log \left(1+{\mathit{SINR}}_{m}[n]\right). \tag{10}
\end{equation*}
$$
 View Source

### C. Problem Formulation

In this subsection, we formulate an optimization problem to maximize the sum rate of all eVTOLs by jointly optimizing the SIM transmission power allocation, phase shift control, and eVTOL trajectory planning.

The optimization problem is formulated as,

$$
\begin{align*}
P1: &\max _{\bm {P}, \bm {\Psi },\mathcal {Q}} \ \ g(\bm {P}, \bm {\Psi },\mathcal {Q}) = \sum _{n=1}^{N}\sum _{m=1}^{M}R_{m}[n] \\
\text{s.t.} \ \ &C1:\sum _{m=1}^{M}p_{m}[n]\leq P_{ATC}, \forall n \in N \\
&C2:p_{m}[n]\geq 0, \forall n \in N, \forall m \in M \\
&C3:\theta _{k}^{l}[n]\in [0,2\pi), \forall n\in N,\forall k\in K,\forall l\in L \\
&C4:\Vert q_{m}[n]-q_{m}[n-1]\Vert \leq V_{{\max}} \delta, \forall n \in N, \forall m \in M \\
&C5:q_{m}[n] \in \mathcal {R}_{cor}, \forall n \in N, \forall m \in M \\
&C6:q_{m}[0]=f_{m}[0],q_{m}[N]=f_{m}[N], \forall m \in M, \tag{11}
\end{align*}
$$
 View Source

where $\bm {P} \triangleq [{p_{1}, p_{2},\ldots, p_{M}}]$ denotes the power allocation matrix, with $p_{m} \triangleq [p_{m}[1], p_{m}[2],\ldots, p_{m}[N]]^{T}$ representing the transmission power allocation for the $m$ -th eVTOL over all time slots. $\bm {\Psi } \triangleq \lbrace \Psi ^{1}, \Psi ^{2},\ldots, \Psi ^{L}\rbrace$ denotes the set of phase shift matrices, where $\psi _{k}^{l} \triangleq [\theta _{k}^{l}[1], \theta _{k}^{l}[2],\ldots, \theta _{k}^{l}[N]]^{T}$ represents the phase shift of the $k$ -th meta-atom on the $l$ -th metasurface layer across all time slots. Finally, $\mathcal {Q} \triangleq [q_{0}, q_{1},\ldots, q_{M}]^{T}$ denotes the set of all eVTOL trajectories, where $q_{m} \triangleq [q_{m}[0], q_{m}[1],\ldots, q_{m}[N]]^{T}$ represents the trajectory of the $m$ -th eVTOL over time.

The constraints are defined as follows: C1: The total transmission power at any time slot must not exceed the available power budget. C2: Transmission power for each eVTOL must be non-negative. C3: The phase shift of each meta-atom must lie within the range $[0, 2\pi)$. C4: The displacement of each eVTOL must not exceed the maximum allowable velocity $V_{\max }$ times the time slot duration $\delta$. C5: Each eVTOL must remain within the designated air corridor region $\mathcal {R}{cor}$ at all times. C6: The initial and final positions of each eVTOL are fixed.

Note that $\bm {P}$, $\bm {\Psi }$, and $\mathcal {Q}$ are interdependent, making problem $P1$ a non-convex optimization problem that requires iterative methods to obtain a local optimal solution. The proposed solution algorithm is introduced in the following section.

In this section, we propose a Block Coordinate Descent (BCD)-based algorithm to iteratively obtain a solution to problem $P1$.

The proposed algorithm consists of three blocks, corresponding to $\bm {P}$, $\bm {\Psi }$, and $\mathcal {Q}$, and incorporates a dual DT design, denoted as $DT^{S}$ and $DT^{e}$. In the first block, the transmit power $\bm {P}$ is optimized within $DT^{S}$, given $\bm {\Psi }$ and $\mathcal {Q}$, using an approximate linearization method as described in \[54\]. In the second block, $\bm {\Psi }$ is updated via an iterative gradient ascent algorithm, based on the optimized $\bm {P}$ and the fixed $\mathcal {Q}$. In the third block, the trajectory $\mathcal {Q}$ is refined using a composite potential field method, given the updated $\bm {P}$ and $\bm {\Psi }$. These above three blocks are repeated iteratively until the optimized parameters ($\bm {P}$, $\bm {\Psi }$, $\mathcal {Q}$) convergence, and the final solution jointly guides SIM beamforming and eVTOL navigation. This BCD-based iterative framework enhances both communication efficiency and flight performance within the prescribed air corridors. Detailed descriptions of each block are provided in the following subsections.

### A. Block 1: Transmission Power Optimization

Recall that the original joint problem is non-convex and involves three coupled variables, making global optimization intractable. In this subsection, we optimize the transmission power as part of an alternating optimization framework, where the SIM phase shift matrix $\bm {\Psi }$ and the eVTOL trajectory $\mathcal {Q}$ are fixed. By adopting the proposed BCD approach, we iteratively solve for one variable at a time, yielding a suboptimal but tractable solution, and the reduced optimization problem $P(1a)$ is as follows,

$$
\begin{align*}
P(1a): &\max \, g_{a}(\bm {P})=\sum _{n=1}^{N}\sum _{m=1}^{M}R_{m}[n] \\
\text{s.t.} \ \ &C1:\sum _{m-1}^{M}p_{m}[n]\leq P_{ATC},\forall n\in N \\
&\qquad C2: p_{m}[n]\geq 0,\forall n\in N,\forall m\in M. \tag{12}
\end{align*}
$$
 View Source

Problem $P(1a)$ is a typical fractional programming (FP) problem, which can be tackled using the approximate linear method. By applying the Lagrangian dual transformation as proposed in \[54\], the objective function $g_{a}(\bm {P})$ is reformulated into an equivalent form $g_{a1}(\bm {P}, \mu)$.

$$
\begin{align*}
& g_{a 1}(\bm {P}, \mu)=\sum _{n=1}^{N} \sum _{m=1}^{M} \log \left(1+\mu _{m}[n]\right)-\sum _{n=1}^{N} \sum _{m=1}^{M} \mu _{m}[n]\\
&\quad + \sum _{n=1}^{N} \sum _{m=1}^{M} \frac{(1+\mu _{m}[n])|\mathcal {H}^\mathcal {G}_{m}|^{2} p_{m}[n]}{\sum _{m^{\prime }=1}^{M}\left|h_{m^{\prime }}^{H}[n] G[n] w_{m^{\prime }}^{1}\right|^{2} p_{m^{\prime }}[n]+\sigma _{m}^{2}},
\end{align*}
$$
 View Source

where $\mu = [\mu _{1}, \ldots, \mu _{m}, \ldots, \mu _{M}]^{T}$ is an auxiliary variable, and $\mu _{m}[n] \geq 0$ for all $m,n$. To address the multi-ratio FP problem, we adopt the quadratic transformation method proposed in \[54\], which converts the original problem into a biconvex optimization form,

$$
\begin{align*}
& g_{a 2}(P, \mu, y)=\sum _{n=1}^{N} \sum _{m=1}^{M}\left(\log \left(1+\mu _{m}[n]\right)-\mu _{m}[n]\right)\\
& +\sum _{n=1}^{N} \sum _{m=1}^{M} 2 y_{m}[n] \sqrt{\left(1+\mu _{m}[n]\right)\left|\mathcal {H}^\mathcal {G}_{m}\right|^{2} p_{m}[n]} \\
& -\sum _{n=1}^{N} \sum _{m=1}^{M} y_{m}^{2}[n]\left(\sum _{m^{\prime }=1}^{M}\left|h_{m^{\prime }}^{H}[n] G[n] w_{m^{\prime }}^{1}\right|^{2} p_{m^{\prime }}[n]+\sigma _{m}^{2}\right),
\end{align*}
$$
 View Source

where $y=[y_{1}, \ldots, y_{m} \ldots, y_{M}]^{T}$ are auxiliary variables. The problem $P(1a)$ can now be rewritten as:

$$
\begin{align*}
\overline{P(1a)}: &\max g_{a 2}(P, \mu, y) \\
\text{ s.t. } \ \ &C1: \sum _{m=1}^{M} p_{m}[n] \leq P_{ATC}, \forall n \in N \\
&C2: p_{m}[n] \geq 0, \forall n \in N, \forall m \in M \\
&C3: \mu _{m}[n] \geq 0, \forall n \in N, \forall m \in M \tag{13}
\end{align*}
$$
 View Source

#### Theorem 1 (Solution to Block 1):

The solution to $\overline{P(1a)}$, which is equivalent to the original problem $P(1a)$, can be obtained by solving the below equations subsequently,

$$
\begin{align*}
\mu ^{\star }_{m}[n]=&\frac{y_{m}^{2}[n]\left|\mathcal {H}^\mathcal {G}_{m}\right|^{2} p_{m}[n]}{2} \\
&+\frac{y_{m}[n] \sqrt{\left|\mathcal {H}^\mathcal {G}_{m}\right|^{2} p_{m}[n] (y_{m}^{2}[n]\left|\mathcal {H}^\mathcal {G}_{m}\right|^{2} p_{m}[n]+4)}}{2}, \tag{14}\\
y^{*}_{m}[n]=&\frac{\sqrt{\left(1+\mu _{m}^{\star }[n]\right)\left|\mathcal {H}^\mathcal {G}_{m}\right|^{2} p_{m}[n]}}{\sum _{m^{\prime }=1}^{M}\left|h_{m^{\prime }}^{H}[n] G[n] w_{m^{\prime }}^{1}\right|^{2} p_{m^{\prime }}[n]+\sigma _{m}^{2}}, \tag{15}\\
p_{m}^{*}[n]=&\left(\frac{y_{m}^{\star }[n] \sqrt{\left(1+\mu _{m}^{\star }[n]\right)\left|\mathcal {H}^\mathcal {G}_{m}\right|^{2}}}{\left|\mathcal {H}^\mathcal {G}_{m}\right|^{2} \sum _{m=1}^{M} (y_{m}^{\star }[n])^{2}-\beta [n]}\right)^{2}, \tag{16}
\end{align*}
$$
 View Source

Based on the above equations, we propose the algorithm to solve $P(1a)$ in Algorithm 1.

#### Proof:

See Appendix A.$\blacksquare$

### Algorithm 1: Prox-Linear Algorithm for P(1a).

### B. Block 2: Phase Shift Matrix Optimization

To optimize the SIM phase shift matrix $\bm {\Psi }$, we reduce the original problem $P1$ to a subproblem $P(1b)$ by fixing the SIM transmission power $\bm {P}$ and the eVTOL flight trajectory $\mathcal {Q}$. The problem $P(1b)$ is as follows,

$$
\begin{align*}
P(1b):&\max g_{b}(\bm {\Psi })=\sum _{n=1}^{N}\sum _{m=1}^{M}R_{m}[n], \\
\text{s.t.} \ \ &\theta _{k}^{l}[n]\in [0,2\pi), \\
&\forall n\in [1,N],\forall k\in [1,K],\forall l\in [1,L]. \tag{17}
\end{align*}
$$
 View Source

#### Theorem 2 (Solution to Block 2):

To solve $P(1b)$, we employ a gradient ascent-based method. The phase shifts $\theta _{k}^{l}[n]$ are initialized with random values and iteratively updated using the following update rules,

$$
\begin{align*}
\theta _{k}^{l}[n+1]\leftarrow \theta _{k}^{l}[n]+\xi \frac{\partial g_{b}(\bm {\Psi })}{\partial \theta _{k}^{l}[n]}, \tag{18}
\end{align*}
$$
 View Source

where $\xi > 0$ denotes the step size, which is determined using the Armijo backtracking line search method as described in \[55\], and $\frac{\partial g_{b}(\bm {\Psi })}{\partial \theta _{k}^{l}[n]}$ is provided in Appendix B. The corresponding algorithm towards problem $P(1b)$ is provided in Algorithm 2.

### Algorithm 2: Iterative Gradient Ascent for P(1b).

### C. Block 3: Flight Control Optimization

This subsection optimizes eVTOL trajectories by jointly considering transmission rates and aviation safety within predefined corridors. Using the proposed CPF algorithm, which combines target, separation, and communication potential fields ($\mathcal {F}^{tar}$, $\mathcal {F}^{sep}$, $\mathcal {F}^{com}$), the problem is reformulated as optimizing the field hyperparameters ${k_{tar}, k_{sep}, k_{com}}$.

Given fixed SIM transmission power allocation $\bm {P}$ and phase shift matrix $\bm {\Psi }$, the original problem $P1$ is reduced to $P(1c)$,

$$
\begin{align*}
P(1c)&: \max _{k_{tar}, k_{sep}, k_{com}} {g}_{c}(\mathcal {Q})= \sum _{m=1}^{M} \left\lbrace \mathcal {S}_{m} + \sum _{n=1}^{N} R_{m}[n] \right\rbrace \\
\text{s.t.} \ \ &C1:\Vert q_{m}[n]-q_{m}[n-1]\Vert \leq V_{{\max}} \delta, \forall n \in N, \forall m \in M \\
&C2:q_{m}[n] \in \mathcal {R}_{cor}, \forall n \in N, \forall m \in M \\
&C3:q_{m}[0]=f_{m}[0],q_{m}[N]=f_{m}[N], \forall m \in M, \tag{19}
\end{align*}
$$
 View Source

where $\mathcal {S}_{m} = \sum _{k=1,k\ne m}^{M}\frac{1-e^{c_{1}+c_{2}d_{k,m}}}{M}$, in which $c_{1}$ and $c_{2}$ are weighting constants, and $d_{k,m}$ is the distance between eVTOLs $k$ and $m$.

The optimization objective of $P(1c)$ comprises two main components: (i) Collision Risk Minimization: The term $\mathcal {S}_{m}$ represents the penalty associated with potential collisions between eVTOLs. A large penalty is applied when the distance $d{k,m}$ between two eVTOLs becomes too small, and the penalty is controlled by constants $c_{1}$ and $c_{2}$, (ii) Communication Rate Maximization: The term $\sum _{n=1}^{N} R_{m}[n]$ represents the total SIM communication rate between the ATCo station and the eVTOLs.

To solve this problem, we employ the CPF method, which tunes flight control hyperparameters to ensure both safe operation and high communication efficiency for eVTOLs.

#### 1) CPF Method

The CPF design centers on two primary objectives: aviation safety and communication connectivity, as outlined below.

(i) *Aviation Safety*: is achieved through the combination of the target field and the separation field. The target field $\mathcal {F}_{i}^{tar}[n]$ directs each eVTOL toward its destination and is defined as follows,

$$
\begin{equation*}
\mathcal {F}_{i}^{tar}[n] = \frac{1}{2} k_{tar} \Vert q_{i}[n] - q_{tar}\Vert ^{2}, \tag{20}
\end{equation*}
$$
 View Source

where $\Vert q_{i}[n] - q_{tar}\Vert$ represents the distance between eVTOL $i$ and its target $q_{tar}$ at time slot $n$. The separation field $\mathcal {F}_{i}^{sep}[n]$ maintains a safe distance between eVTOLs to prevent collisions and is defined as follows:

$$
\begin{equation*}
\mathcal {F}_{i}^{sep}[n]= \sum _{j\in N_{i}} \mathcal {F}_{i,j}^{sep}[n], \tag{21}
\end{equation*}
$$
 View Source

where $N_{i}$ is the set of neighboring eVTOLs of $i$, and

$$
\begin{equation*}
\mathcal {F}_{i,j}^{sep}[n]= {\begin{cases}\frac{1}{2}k_{sep}\left(\frac{d_{sep}}{d_{i,j}[n]}\right)^{2},& \text{if } d_{i,j}[n] \leq d_{sep} \\
0, & \text{if } d_{i,j}[n] > d_{sep}, \end{cases}} \tag{22}
\end{equation*}
$$
 View Source

in which $d_{sep}$ is the minimum safe separation between eVTOLs.

(ii) *Communication Connectivity*: The communication field $\mathcal {F}_{i}^{com}[n]$ ensures that eVTOLs maintain connectivity with the platoon and is defined as follows,

$$
\begin{equation*}
\mathcal {F}_{i}^{com}[n]= \sum _{j\in N_{i}^{c}} \mathcal {F}_{i,j}^{com}[n], \tag{23}
\end{equation*}
$$
 View Source

where

$$
\begin{equation*}
\mathcal {F}_{n,i,j}^{com} = {\begin{cases}\frac{1}{2}k_{com} d_{i,j}[n]^{2} & \text{if} \ \ d_{i,j}[n] \geq d^{eVTOL}_{max} \\
0 & \text{otherwise}, \end{cases}} \tag{24}
\end{equation*}
$$
 View Source

in which $d_{i,j}[n]$ represents the distance between eVTOLs $i$ and $j$, and $N_{i}^{c}$ is the set of communication-active neighbors. $d^{eVTOL}_{max}$ defines the maximum communication range, preventing eVTOL-to-eVTOL communication disconnection.

Consequently, the flight acceleration $\Lambda _{i}[n]$ of eVTOL $i$ is derived as a combination of the negative gradients of the potential fields,

$$
\begin{equation*}
\Lambda _{i}[n] = -\nabla {(\mathcal {F}_{i}^{com}[n] + \mathcal {F}_{i}^{sep}[n] + \mathcal {F}_{i}^{tar}[n])}, \tag{25}
\end{equation*}
$$
 View Source

which enables real-time trajectory adjustments to balance safety and communication connectivity, supporting efficient and reliable eVTOL operations.

#### 2) DQN Framework

As observed from the previous discussion, fixed values of ${k_{tar}, k_{sep}, k_{com}}$ often lead to linear or circular flight patterns, which are insufficient for navigating complex-shaped corridors. Moreover, the objective value of $P(1c)$ may fluctuate in response to dynamic environmental changes, such as moving obstacles like birds or other drones, highlighting the need for adaptive field hyperparameters to ensure safe and efficient navigation.

To address this challenge, we propose a Deep Reinforcement Learning (DRL)-based approach in which the field hyperparameters are treated as adaptive parameters and dynamically optimized through interactions with the environment. Specifically, we employ the Deep Q-Network (DQN) algorithm, which integrates Q-learning with deep neural networks and is well-suited for high-dimensional state spaces and complex input scenarios \[56\].

The DQN framework consists of three fundamental components: (i) **State**, (ii) **Action**, and (iii) **Reward**.

*State*: The state space, denoted as $\mathcal {S}$, contains the key environmental information relevant to decision-making. Each state $\mathbf {s} \in \mathcal {S}$ includes the target position $\mathbf {p}_{t}$ and the relative positions of neighboring eVTOLs with respect to the target, defined as:

$$
\begin{equation*}
\mathbf {s} = \lbrace \mathbf {p}_{t}, (\mathbf {p}_{i} - \mathbf {p}_{t}), i \in \mathcal {N}\rbrace \tag{26}
\end{equation*}
$$
 View Source

where $\mathbf {p}_{t}$ represents the target position, $\mathbf {p}_{i}$ denotes the position of eVTOL $i$, and $\mathcal {N}$ is the set of neighboring eVTOLs.

*Action*: The action space, denoted by $\mathcal {A}=\lbrace a[1], a[2],\ldots, a[n],\dots \rbrace$, defines possible adjustments to the field hyperparameters ${k_{tar}, k_{sep}, k_{com}}$. For each hyperparameter, the agent can choose from three discrete changes: ${+0.06, -0.06, 0}$ (no change). Consequently, the total number of actions is $M \times 3 \times 3$, and the action space is given by,

$$
\begin{equation*}
\begin{split} \mathcal {A} = &\lbrace \Delta k^{i}_* \mid \Delta k^{i}_* \in \lbrace \pm 0.06, 0\rbrace, \, i = 1, \ldots, M, \\
& *\in \lbrace tar,sep,com\rbrace \rbrace. \end{split} \tag{27}
\end{equation*}
$$
 View Source

*Reward*: The reward function provides feedback on the agent's actions. For a swarm consisting of $M$ eVTOLs, the reward for eVTOL $i$ is defined as:

$$
\begin{align*}
r_{i} =& \alpha _{1} v_{tar}(1 + \alpha _{2} d_{i,tar}) + \sum _{ j \ne i, \, d_{i,j} < d_{sep} }\left(\frac{\beta v_{sep}}{d_{i,j}}\right) \\
&+ \sum _{m=1}^{M}R_{m}[n], \tag{28}
\end{align*}
$$
 View Source

The reward $r_{i}$ consists of three key components: (i) $\alpha _{1} v_{tar}(1 + \alpha _{2} d_{i,tar})$ prioritizes target progression, (ii) $\sum \beta v_{sep}/d_{i,j}$ enforces safety-critical separation, (iii) The logarithmic term maximizes swarm communication efficiency.

Here, $v_{tar}$ and $v_{sep}$ represent the velocity components guiding the eVTOL toward its target and away from nearby eVTOLs, respectively. $d_{i,tar}$ denotes the distance between eVTOL $i$ and its destination, while $d_{i,j}$ is the distance between eVTOLs $i$ and $j$. The constants $\alpha _{1}$, $\alpha _{2}$, and $\beta$ are weighting factors used to balance the reward components. Specifically, $\alpha _{1}$ scales the primary incentive for target progression. $\alpha _{2}$ adjusts the sensitivity of the target-proximity reward based on distance. $\beta$ governs the penalty strength for violating minimum safe separation distances ($d_{sep}$).

*DQN Network Design*: DQN is model-free and can directly optimize the action-value function $Q^{*}(s,a)$ through interactions with the environment, and its update rule is given by,

$$
\begin{align*}
Q(s[n], a[n]) &\leftarrow (1-\alpha)Q(s[n], a[n]) \\
&+ \alpha \left(r[n+1] + \gamma \max Q(s[n+1], a) \right), \tag{29}
\end{align*}
$$
 View Source

where $\alpha$ is the learning rate, $r[n+1]$ is the reward at time step $n+1$, $\gamma$ is the discount factor for future rewards, $s[n+1]$ denotes the state at time step $n+1$, and $a^{\prime }$ is the action that maximizes the Q-value at $s[n+1]$. To balance exploration and exploitation, an $\epsilon$ -greedy policy is adopted, where $\epsilon$ determines the probability of choosing a random action versus selecting the action with the highest estimated Q-value.

The framework of the proposed DQN network is illustrated in Fig. 3, where the Q-function is approximated using a deep neural network with parameters $\Upsilon$. To stabilize training, a target network $Q_{target}$ with parameters $\Upsilon ^-$ is employed and updated less frequently. The update rule for the target Q-network is:

$$
\begin{equation*}
y[n] = r[n] + \gamma \max _{a^{\prime }} Q_{\text{target}}(s[n+1], a^{\prime }; \Upsilon ^-), \tag{30}
\end{equation*}
$$
 View Source

where $y[n]$ is the target Q-value and $a^{\prime }$ denotes the action that maximizes the Q-value at state $s[n+1]$. The primary Q-network is trained by minimizing the following loss function, which is the mean squared error between the predicted and target Q-values:

$$
\begin{align*}
&L(\theta) =\\
&\mathbb {E}_{(s[n], a[n], r[n], s[n+1]) \sim \mathcal {D}} \left[ \left(y[n] - Q_{\text{primary}}(s[n], a[n]; \Upsilon) \right)^{2} \right], \tag{31}
\end{align*}
$$
 View Source

where $\mathcal {D}$ is the experience replay buffer, which stores transitions $(s[n], a[n], r[n], s[n+1])$ to reduce the correlation between consecutive experiences and improve training stability. The network parameters $\Upsilon$ are updated using Stochastic Gradient Descent (SGD):

$$
\begin{equation*}
\Upsilon \leftarrow \Upsilon - \eta \nabla _{\Upsilon } L(\Upsilon) \tag{32}
\end{equation*}
$$
 View Source

where $\eta$ is the learning rate. The loss function for the mini-batch sampled from $\mathcal {D}$ is given by:

$$
\begin{align*}
&L(\Upsilon) = \\
&\mathbb {E}_{(s[n], a[n], r[n], s[n+1]) \sim \mathcal {D}} \left[ \left(y[n] - Q_{\text{prim}}(s[n], a[n]; \Upsilon) \right)^{2} \right] \tag{33}
\end{align*}
$$
 View Source

where,

$$
\begin{equation*}
y[n] = {\begin{cases}r[n], &\text{terminal}, \\
r[n] + \gamma Q_{\text{target}}(s[n+1], a^{\prime }; \Upsilon ^-), &\text{otherwise}. \end{cases}} \tag{34}
\end{equation*}
$$
 View Source

**Fig. 3.**

Illustration of the proposed DQN structure.

#### Algorithm 3: Deep Q-Network (DQN).

The detailed steps of the proposed DQN algorithm are illustrated in Algorithm 3. Each training episode starts by initializing the state $s[n]$ from the environment and proceeds for up to $T$ time steps. At each step, an action is chosen with probability $1 - \epsilon$ as $a[n] = \arg \max _{a} Q(s[n], a; \Upsilon)$. The action $a[n]$ is executed, yielding reward $r[n]$ and next state $s[n+1]$. The algorithm updates the network by minimizing the loss via gradient descent and sets $s[n] \leftarrow s[n+1]$. To stabilize training, the target network parameters $\Upsilon ^-$ are periodically synced with $\Upsilon$. The episode terminates upon reaching a terminal state, outputting the optimized field hyperparameters $\lbrace k_{tar}, k_{sep}, k_{com}\rbrace$ for safe and efficient eVTOL navigation.

### D. DT-Driven Joint Resource-Trajectory Optimization Algorithm

In this subsection, we propose an final optimization algorithm that integrates the three aforementioned optimization blocks. The complete process of the proposed DT-based system is presented in Algorithm 4.

### Algorithm 4: DT-based Joint Optimization.

The process begins by initializing the eVTOL trajectory $\mathcal {Q}$ along the centerline of the predefined corridor. In the first step, $DT^{S}$ iteratively applies Algorithm 1 and Algorithm 2 to optimize the transmission power $\bm {P}$ and the phase shift matrix $\bm {\Psi }$, respectively. The optimized SIM parameters $\bm {P}$ and $\bm {\Psi }$ are then passed to $DT^{e}$, which uses Algorithm 3 to determine the optimal CPF hyperparameters $\lbrace k_{tar}, k_{sep}, k_{com}\rbrace$. In the second step, the optimized SIM parameters $\bm {P}$ and $\bm {\Psi }$ are transmitted to the SIM antenna via wired fiber, and the CPF hyperparameters $\lbrace k_{tar}, k_{sep}, k_{com}\rbrace$ are sent to the corresponding eVTOL through SIM-based G2A communication link.

Moreover, the computational complexity of the proposed algorithms are listed in Table II, where $M$ denotes the number of BS antennas (or equivalently, eVTOLs), $N$ represents the number of time slots, $L$ indicates the number of metasurface layers in the SIM, $K$ signifies the number of meta-atoms per metasurface layer in the SIM. $n_{t}$ denotes the number of time steps per episode, and $n_{m}$ represents the total number of episodes.

**TABLE II** Algorithm Complexity

Specifically, SIM Optimization: 18 ms/iteration (M = 3, L = 5, K = 16, N = 30); Trajectory Update: 9 ms/decision.

Despite these optimizations, practical challenges such as unexpected dynamic obstacles (e.g., drones or birds) may cause deviations in the DT-derived parameters during real-world operations. To mitigate this, eVTOLs must continuously update their real-time dynamic data, such as velocity and position, to the ATCo station, enabling timely revisions and corrections to the DT-derived parameters.

Here, synchronized data streams are processed in the DT environment to generate dynamic environmental digital twins, enabling: (i) Real-time trajectory re-planning via CPF hyperparameter adjustment; (ii) Predictive conflict detection using historical encounter patterns. For instance, when electronic conspicuity systems detect manned aircraft (e.g., via ADS-B Message Type 3/4), the separation field automatically strengthens to enforce emergency avoidance maneuvers.

Additionally, the DT synchronization protocol minimizes overhead by transmitting only critical hyperparameters: (i) $DT^{e} \rightarrow$ Physical eVTOL: ${k_{tar},\ k_{sep},\ k_{com}}$ (only 3 parameters); (ii) Physical eVTOL $\rightarrow DT^{e}$: Deviations ${\Delta q_{m},\ \Delta v_{m}}$ exceeding safety thresholds, which achieves payload reduction vs. full-state synchronization. The above operations greatly reduce synchronized overheads on the air-ground communication. Through this iterative feedback loop, $DT^{S}$ and $DT^{e}$ work collaboratively to produce updated SIM communication and eVTOL flight parameters, effectively guiding the future operations of the physical system.

Finally, the synchronization frequency of the digital twin, denoted as $f_{re}$, plays a critical role in mitigating deviations. A higher $f_{re}$ enables more accurate and reliable DT-derived parameters by allowing the system to adapt more promptly to dynamic environmental changes, the $f_{re}$ used in this work is provided in Section V.

To evaluate the effectiveness of the proposed scheme for eVTOL-based AAM, we conduct simulations for both SIM-based beamforming and CPF-based flight control. The carrier frequency is set to 30 GHz, and the ATCo station, equipped with $M$ antennas, is positioned at the origin. Each SIM metasurface is aligned parallel to the $x$ – $y$ plane, centered along the $z$ -axis. The total SIM thickness is defined as $\text{Thick} = 5\lambda$; for an $L$ -layer SIM, the spacing between adjacent metasurfaces is $d_{\text{Layer}} = \text{Thick} / L$. Each metasurface comprises $K_{x}$ and $K_{y}$ meta-atoms along the $x$ - and $y$ -axes, respectively, with $K = K_{x} K_{y}$. For simplicity, we assume a square metasurface layout, i.e., $K_{x} = K_{y}$, and each meta-atom has dimensions $d_{x} = d_{y} = \lambda / 2$. Algorithm 1 and Algorithm 2 are implemented in MATLAB, while Algorithm 3 is developed using PyTorch. The main simulation parameters are summarized in Table III.

**TABLE III** Simulation Parameters

The simulation setup assumes an obstacle-free digital environment and an obstacle-containing physical environment, with two rounds of DT interaction. Initially, random phase values and a predefined trajectory are used to iteratively optimize power and phase, followed by digital trajectory generation. This process is repeated to refine both communication and flight control parameters. In each DT interaction, physical and digital trajectory segments are merged to form updated trajectories, which are then used to further optimize beamforming and flight control. After two such interactions, the final trajectory, phase, and power are constructed by concatenating the best segments from previous results, yielding a fully optimized solution.

Fig. 4 shows the transmission rates among three SIM optimization schemes for a given eVTOL trajectory. In the joint Power & Phase Optimization scheme, the transmission rate is calculated by iteratively applying Algorithm 1 and Algorithm 2. In the Power-Only Optimization scheme, all phase shifts are initialized to $\theta _{k}^{l}[n] = 0$, and Algorithm 1 is then used to optimize the transmission rate. Conversely, the Phase-Only Optimization scheme sets the transmission power of each antenna to $p_{m}[n] = 3.33$ dBm for every time slot and employs Algorithm 2 to optimize the transmission rate.

**Fig. 4.**

Transmission rate comparison of different SIM communication optimizations.

As shown in Fig. 4, the joint Power & Phase Optimization scheme achieves the best performance, with a transmission rate of approximately 3.0 bps. The second-best performance is seen in the Phase-Only Optimization scheme, where the transmission rate converges to 1.9 bps. On the other hand, the Power-Only Optimization scheme delivers the worst results, with rates approaching 0 bps. This significantly highlights the importance of phase shifts in beam alignment. Relying solely on power optimization is insufficient for maintaining effective beam tracking for dynamic eVTOL trajectories.

Fig. 5 illustrates the evolution of the proposed DQN-based CPF flight control algorithm over 500 iterations. The $x$ -axis represents the number of iterations, while the $y$ -axis shows the mean distance deviation, defined as the average distance of each eVTOL from the corridor centerline.

**Fig. 5.**

Mean distance deviation of the eVTOL with the proposed DQN-based flight control.

Initially, the mean distance deviation decreases rapidly, reaching approximately 10 m by iteration 50. Beyond iteration 400, the deviation stabilizes at around 4 m, indicating that the eVTOLs have achieved a steady state and remain within the air corridor boundaries. This result demonstrates the convergence and performance efficiency of the proposed DQN-based CPF algorithm. With its rapid convergence and stable plateau, the CPF algorithm is well-suited for AAM applications. Note that the converged 4 m deviation is achieved in the corridor without obstacles. When there are obstacles in the corridor, the converged deviation will increase. It will be verified in the following simulation experiments.

Fig. 6 compares the transmission rates over time for three eVTOLs, using SIM-based and MIMO-based ATCo stations. The SIM-based station includes five cases with varying configurations. For the MIMO-based ATCo station, the transmission capacity is given by:

$$
\begin{equation*}
\sum _{n=1}^{N} \sum _{m=1}^{M} \log \left(1+\frac{h_{m}[n]^{2} p_{m}[n]}{\sum _{m^{\prime }=1, m^{\prime } \ne m}^{M} h_{m}[n]^{2} p_{m^{\prime }}[n]+\sigma _{m}^{2}}\right), \tag{35}
\end{equation*}
$$
 View Source

where the eVTOL trajectory is predetermined, and the transmission power is optimized using Algorithm 1. For the SIM-based station, both transmission power and phase shifts are optimized iteratively using Algorithm 1 and Algorithm 2 with the same eVTOL trajectory. As eVTOLs move farther from the ATCo station, the transmission rate decreases for both configurations. However, the SIM transmission rate declines faster than that of the MIMO transmission. This is due to the SIM phase shift amplifying the effect of distance on channel capacity. Among SIM configurations, the transmission rate of the metasurface setups ($L=5,K=9$ or $L=5,K=16$ where $L$ is the number of layers and $K$ is the total number of the meta-atoms per layer) outperforms that of the MIMO (without SIM). In contrast, the transmission rate of the metasurface setups ($L=3, K=4$, $L=5, K=4$, and $L=7, K=4$) is even worse than that of the station without SIM.

**Fig. 6.**

Transmission rate of SIM v.s. that of without SIM.

Moreover, Fig. 7 shows the variation of the total transmission rate with respect to the number of metasurface layers $L$, the number $K$ of meta-atoms per layer, and the total SIM thickness (${\mathit{Thick}}$). For a fixed $K = 4$ and ${\mathit{Thick}} = 0.05$ m, the transmission rate increases with the number of metasurface layers $L$. Similarly, for a fixed $L$ and ${\mathit{Thick}}$, increasing the number of meta-atoms per layer can also improve the SIM transmission rate. When the spacing between adjacent metasurface layers ${\mathit{Thick/}}L$ is held constant (e.g., ${\mathit{Thick}}/L = 0.01$ m), increasing $L$ results in a thicker SIM and a corresponding decrease in transmission rate. This highlights a key limitation: SIM manufacturing constraints that impose a minimum gap between metasurface layers can reduce performance as $L$ increases. For example, when $K = 4$ and $L = 3$, the transmission rate at ${\mathit{Thick}}/L = 0.05$ is significantly lower (1.5 bps) than at ${\mathit{Thick}}/L = 0.01$ m (about 21.2 bps). These results demonstrate that the transmission rate is inversely proportional to the distance between adjacent layers. Additionally, for a fixed $textit{Thick}$, increasing the total number of meta-atoms ($L \times K$) generally results in higher transmission rates.

**Fig. 7.**

Transmission rate v.s. different SIM configurations.

For instance, the transmission rate for $K = 4$ and $L = 7$ ($K\times L=28$) is significantly lower than that for $K = 9$ and $L = 5$ ($K\times L=45$), yet higher than that for $K = 4$ and $L = 5$ ($K\times L=20$).

Fig. 8 highlights the effectiveness of the DQN-based CPF method in maintaining eVTOL trajectories within the prescribed air corridor. The DQN-based trajectory shows fewer jitters compared to the original CPF method, providing smoother and safer flight paths. This improvement is essential for ensuring airspace safety and enhancing passenger experience.

**Fig. 8.**

DQN-based CPF method can maintain the eVTOL trajectory in the corridor.

Fig. 9 compares the transmission rate and flight trajectories across three flight control schemes: the proposed DT scheme, the predetermined scheme (without DT synchronization), and the safe aviation-only scheme (without communication optimization). The simulation spans 30 time slots, illustrating the flight process through the prescribed corridor. In the proposed DT scheme, Algorithm 4 is executed with the DT synchronization procedure performed every 10 time slots. In contrast, the predetermined scheme without DT synchronization runs Algorithm 4 only once before the eVTOL platoon enters the corridor. This approach omits the DT synchronization step (lines 12–14 in Algorithm 4), effectively generating a static, pre-optimal flight trajectory. Lastly, the scheme without communication optimization eliminates the communication component from [(28)](#deqn28). This reduces the whole algorithm to a DQN procedure (Algorithm 3) where the reward function is modified as: $r_{i} = \alpha _{1} v_{tar}(1 + \alpha _{2} d_{i,tar}) + \sum _{j \ne i, \, d_{i,j} < d_{sep}} \left(\frac{\beta v_{sep}}{d_{i,j}}\right)$.

**Fig. 9.**

Transmission rate with different flight control schemes.

Fig. 9(a) shows that the proposed DT scheme achieves the highest transmission rate among the three approaches. Conversely, the scheme without communication optimization performs the worst due to its lack of communication-oriented optimization. However, the overall performance differences between the three schemes remain relatively small. This is primarily because the air corridor's constraints limit the flexibility of flight trajectories, restricting additional gains in communication through mobility. Fig. 9(b), (c), and (d) depict the eVTOL flight trajectories under the DT scheme, the scheme without DT synchronization, and the scheme without communication optimization, respectively. In these figures, the blue entity represents a spherical obstacle with a radius of 50 m. The DT scheme demonstrates a noticeably smoother trajectory compared to the other two schemes. This smoothness arises from the frequent DT synchronizations, which allow timely updates to the eVTOL flight parameters (CPF parameters), mitigating trajectory deviations caused by obstacles. In contrast, the other two schemes lack this DT synchronization mechanism, leaving the flight parameters static throughout the simulation, which cannot revise the trajectory deviation caused by obstacles.

Fig. 10 examines the performance of the flight control schemes in the air corridor containing five obstacles. All schemes successfully navigated in the corridor without colliding with obstacles, showcasing the robustness of the proposed DQN algorithm. Moreover, the proposed DT scheme achieves the highest transmission rate, outperforming the other approaches. Compared to the CPF flight control benchmark, it improves the transmission rate by 8.3%. When comparing scenarios with three obstacles versus five, the performance gap between the DT-based scheme and the predetermined scheme widens. This is because DT synchronization can revise deviations caused by obstacles. As the number of obstacles increases, the frequency of trajectory deviations and jitters also grows, amplifying the benefits of DT synchronization. Conversely, flight control schemes without DT synchronization suffer from reduced performance due to their inability to adapt to dynamic environmental changes.

**Fig. 10.**

Different flight control schemes with 5 obstacles.

Fig. 11 highlights the impact of DT synchronization frequency on transmission rates and mean distance deviations in a corridor with three obstacles. Note that the DT synchronization procedure is realized as Line 10 to 11 of Algorithm 4. Moreover, Fig. 11(a) shows that the transmission rates of four times DT synchronization (DT\_Sync\_4) is much better than synchronizing twice or not at all. This reveals the more times of DT synchronization can further improve the communication performance of the eVTOLs. However, the improvement of DT synchronization twice (DT\_Sync\_2) is modest because the only twice DT synchronizations cannot fully exploit the benefits of DT deduction due to the minimal information exchanges.

**Fig. 11.**

Impact of DT synchronization in a corridor with three obstacles.

In contrast, Fig. 11(b) demonstrates a significant reduction in mean distance deviation as the frequency of DT synchronization increases. Frequent synchronization allows eVTOLs to promptly correct flight deviations, ensuring that their trajectories remain closer to the corridor centerline. The DT\_Sync\_4 reduces flight distance deviation from the prescribed corridor by 10% compared to the predetermined optimization (without DT). This finding underscores the importance of DT synchronization for precise flight control, particularly in complex or obstacle-rich environments.

Fig. 12 illustrates the scalability of the proposed method by showing transmission rate and distance deviation versus different number of eVTOLs (3 and 5). Due to dense communication interference and competition, the transmission rate decreases with the number of eVTOLs, as demonstrated in Fig. 12(a). Concurrently, Fig. 12(b) reveals that the 5-eVTOL scenario has a better distance deviation control. The reason is that large numbers of eVTOLs intensify the interaction force of the potential field, resulting in tighter swarm formations and reduced mean distance deviation of the swarm.

**Fig. 12.**

Comparison with different number of eVTOLs.

Fig. 13 shows the performance comparison of DQN and D3QN. While D3QN marginally improved flight deviation metrics (Fig. 13(a)), its transmission rate of D3QN is slightly less than that of the DQN (Fig. 13(b)). Additionally, the higher computational overhead of D3QN outweighed benefits for our latency-sensitive application.

**Fig. 13.**

DQN vs.D3QN.

Thus, there are two design rationale for DQN: (i) Computational Efficiency: DQN's lower memory footprint ($\sim$ 28% lighter than D3QN) better aligns with ATCo edge server constraints. (ii) Training Stability: For our composite potential field optimization, DQN achieved convergence with fewer episodes than D3QN in preliminary tests.

This evidence-based clarification demonstrates that while D3QN offers theoretical advantages, DQN provides superior operational practicality for corridor-constrained eVTOL operations. Besides, future work will implement distributed D3QN for large-scale swarms ($\geq 20$ eVTOLs) where its advanced value decomposition outweighs computational costs.

This paper presents a DT-based flight control framework for eVTOLs, designed to ensure safe and communication-efficient operations within predefined air corridors. The proposed approach jointly addresses three sub-problems: transmission power optimization, SIM phase shift optimization, and flight control via CPF. Within the DT system, the SIM DT iteratively optimizes transmission power and phase shifts, which are then passed to the eVTOL DT. Using these inputs, the eVTOL DT applies a DQN-based algorithm to refine CPF hyperparameters for safe navigation. These updated parameters guide the next round of SIM optimization, forming an iterative loop between the SIM and eVTOL DTs. The final outputs, including optimized power, phase shifts, and CPF parameters, are transmitted to the physical eVTOLs and SIM antennas, while real-time updates from the physical system maintain synchronization. Simulation results confirm the proposed framework outperforms existing methods in both communication efficiency and flight safety. Future work will explore scaling the framework to support large-scale eVTOL swarms across multiple corridors.

In this reformulated problem $\overline{P(1a)}$, $\bm {P}$, $\mu$, and $y$ are updated iteratively. By fixing $\bm {P}$ and $y$ as constants, the partial derivative of $g_{a2}$ with respect to $\mu _{m}[n]$ is computed as:

$$
\begin{equation*}
\frac{\partial g_{a 2}}{\partial \mu _{m}[n]}=\frac{1}{1+\mu _{m}[n]}-1+\frac{y_{m}[n] \sqrt{\left|\mathcal {H}^\mathcal {G}_{m}\right|^{2} p_{m}[n]}}{\sqrt{1+\mu _{m}[n]}}, \tag{36}
\end{equation*}
$$
 View Source

where $\mathcal {H}^\mathcal {G}_{m} = h_{m}^{H}[n] G[n] w_{m}^{1}$. Setting ${\partial g_{A2}}/{\partial \mu _{m}[n]} = 0$ gives the optimal value:

$$
\begin{align*}
&\mu ^{*}_{m}[n]=\frac{y_{m}^{2}[n]\left|\mathcal {H}^\mathcal {G}_{m}\right|^{2} p_{m}[n]}{2}+ \\
&\frac{y_{m}[n] \sqrt{\left|\mathcal {H}^\mathcal {G}_{m}\right|^{2} p_{m}[n] (y_{m}^{2}[n]\left|\mathcal {H}^\mathcal {G}_{m}\right|^{2} p_{m}[n]+4)}}{2}. \tag{37}
\end{align*}
$$
 View Source

Similarly, setting ${\partial g_{a2}}/{\partial y_{m}[n]} = 0$ gives the optimal $y^{*}_{m}[n]$:

$$
\begin{equation*}
y^{*}_{m}[n]=\frac{\sqrt{\left(1+\mu _{m}[n]\right)\left|h_{m}^{H}[n] G[n] w_{m}^{1}\right|^{2} p_{m}[n]}}{\sum _{m^{\prime }=1}^{M}\left|h_{m^{\prime }}^{H}[n] G[n] w_{m^{\prime }}^{1}\right|^{2} p_{m^{\prime }}[n]+\sigma _{m}^{2}}. \tag{38}
\end{equation*}
$$
 View Source

Next, the dual function of $g_{a2}$ is introduced by incorporating dual variables $\beta [n]$ and $a_{m}[n]$ to account for SIM transmission power constraints:

$$
\begin{align*}
& g_{a 2}^{Dual}(P, \beta, a)=\sum _{n=1}^{N} \sum _{m=1}^{M}\left(\log \left(1+\mu _{m}[n]\right)-\mu _{m}[n]\right) \\
&+ \sum _{n=1}^{N} \sum _{m=1}^{M} 2 y_{m}[n] \sqrt{\left(1+\mu _{m}[n]\right)\left|\mathcal {H}^\mathcal {G}_{m}\right|^{2} p_{m}[n]} \\
& -\sum _{n=1}^{N} \sum _{m=1}^{M} y_{m}^{2}[n]\left(\sum _{m^{\prime }=1}^{M}\left|h_{m^{\prime }}^{H}[n] G[n] w_{m^{\prime }}^{1}\right|^{2} p_{m^{\prime }}[n]+\sigma _{m}^{2}\right) \\
& +\sum _{n=1}^{N} \beta [n]\left(\sum _{m=1}^{M} p_{m}[n]-P_{ATC}\right)+a_{m}[n]\left(-p_{m}[n]\right). \tag{39}
\end{align*}
$$
 View Source

Using the Karush-Kuhn-Tucker (KKT) conditions \[57\], the optimal transmission power $\bm {P}^{*}$ can be derived by solving the system of equations:

$$
\begin{equation*}
\left\lbrace \begin{array}{l}\frac{\partial g_{a 2}^{Dual}}{\partial p_{m}[n]}=\frac{y_{m}[n] \sqrt{\left(1+\mu _{m}[n]\right)\left|h_{m}^{H}[n] G[n] w_{m}^{1}\right|^{2}}}{\sqrt{p_{m}[n]}} \\
-\left|h_{m}^{H}[n] G[n] w_{m}^{1}\right|^{2} \sum _{m=1}^{M} y_{m}^{2}[n]+\beta [n] \\
-a_{m}[n]=0, \forall n \in N, \forall m \in M \\
\sum _{m=1}^{M} p_{m}[n] \leq P_{ATC}, \forall n \in N \\
\beta [n] \geq 0, \forall n \in N \\
\beta [n]\left(\sum _{m=1}^{M} p_{m}[n]-P_{ATC}\right)=0, \forall n \in N \\
p_{m}[n] \geq 0, \forall n \in N, \forall m \in M \\
a_{m}[n] \geq 0, \forall n \in N, \forall m \in M \\
-a_{m}[n] p_{m}[n]=0, \forall n \in N, \forall m \in M \end{array}\right. \tag{40}
\end{equation*}
$$
 View Source

The solving technique is as follows: setting $a_{m}[n]=0, \forall n \in N, \forall m \in M$ and $\frac{\partial g_{a 2}^{Dual}}{\partial p_{m}[n]}=0, \forall n \in N, \forall m \in M$, we get,

$$
\begin{equation*}
p_{m}[n]=\left(\frac{y_{m}[n] \sqrt{\left(1+\mu _{m}[n]\right)\left|h_{m}^{H}[n] G[n] w_{m}^{1}\right|^{2}}}{\left|h_{m}^{H}[n] G[n] w_{m}^{1}\right|^{2} \sum _{m=1}^{M} y_{m}^{2}[n]-\beta [n]}\right)^{2} \tag{41}
\end{equation*}
$$
 View Source

Here, $\beta [n]$ is gradually increased from 0 until the condition $0.9 P_{ATC} \leq \sum _{m=1}^{M} p_{m}[n] \leq P_{ATC}, \forall n \in N$ is satisfied. An exponential increase and linear decrease search algorithm is applied to obtain the suboptimal solution $\bm {P}^{*}$.

The phase shifts $\theta _{k}^{l}[n]$ are initialized with random values and iteratively updated using the following update rules:

$$
\begin{align*}
\theta _{k}^{l}[n+1]\leftarrow \theta _{k}^{l}[n]+\xi \frac{\partial g_{b}(\bm {\Psi })}{\partial \theta _{k}^{l}[n]}, \tag{42}
\end{align*}
$$
 View Source

where $\xi > 0$ denotes the step size, which is determined using the Armijo backtracking line search method as described in \[55\],

$$
\begin{align*}
\frac{\partial g_{b}(\boldsymbol{\Psi })}{\partial \theta _{k}^{l}[n]}=\sum _{m=1}^{M} \gamma _{m}[n]\left(\frac{\ell _{m}[n] \zeta _{m}[n]-\wp _{m}[n] \imath _{m}[n]}{\zeta _{m}[n]}\right),
\end{align*}
$$
 View Source

where $\gamma _{m}[n]$, $\ell _{m}[n]$, $\zeta _{m}[n]$, $\wp _{m}[n]$ and $\imath _{m}[n]$ are given by

$$
\begin{align*}
\gamma _{m}[n]=&\frac{1}{\sum _{m^{\prime }=1}^{M}\left|h_{m^{\prime }}^{H}[n] G[n] w_{m^{\prime }}^{1}\right|^{2} p_{m^{\prime }}[n]+\sigma _{m}^{2}}, \\
\ell _{m}[n]=&p_{m}[n] \eta _{m}[n], \\
\zeta _{m}[n]=&\sum _{m^{\prime }=1, m^{\prime } \ne m}^{M}\left|h_{m^{\prime }}^{H}[n] G[n] w_{m^{\prime }}^{1}\right|^{2} p_{m^{\prime }}[n]+\sigma _{m}^{2}, \\
\wp _{m}[n]=&\sum _{m^{\prime }=1, m^{\prime } \ne m}^{M} p_{m^{\prime }}[n] \eta _{m^{\prime }}[n], \\
\imath _{m}[n]=&\left|h_{m}^{H}[n] G[n] w_{m}^{1}\right|^{2} p_{m}[n],
\end{align*}
$$
 View Source

and $\eta _{m}[n]$ is given by

$$
\begin{align*}
\eta _{m}[n]=&2 \operatorname{Im}\left\lbrace h_{m}^{H}[n] G[n] w_{m}^{1}\right\rbrace \operatorname{Im}\left(\varsigma _{k, l, n, m}\right) \\
& +2 \operatorname{Re}\left\lbrace h_{m}^{H}[n] G[n] w_{m}^{1}\right\rbrace \operatorname{Re}\left(\varsigma _{k, l, n, m}\right),
\end{align*}
$$
 View Source

where

$$
\begin{align*}
\varsigma _{k, l, n, m}=h_{m}^{H}[n] v_{k}^{l}[n] e^{j \theta _{k}^{l}[n]} u_{k}^{l}[n] w_{m}^{1} j.
\end{align*}
$$
 View Source

in which $u_{k}^{l}[n]$ and $v_{k}^{l}[n]$ represent the $k$ -th row and $k$ -th column of the matrices $U_{l}[n] \in \mathbb {C}^{K \times K}$ and $V_{l}[n] \in \mathbb {C}^{K \times K}$, respectively, given as follows,

$$
\begin{align*}
& U^{l}[n] \triangleq \left\lbrace \begin{array}{lc} W^{l} \Psi ^{l-1}[n] \cdots \Psi ^{2}[n] W^{2} \Psi ^{1}[n], \text{i}f\ l \ne 1, \\
I_{K}, if\ l=1, \end{array}\right.\\
& V^{l}[n] \triangleq \left\lbrace \begin{array}{lc} \Psi ^{L}[n] W^{L} \Psi ^{L-1}[n] \cdots \Psi ^{l+1}[n] W^{l+1}, \text{if}\quad l \ne L, \\
I_{K}, \text{if}\quad l=L. \end{array}\right.
\end{align*}
$$
 View Source