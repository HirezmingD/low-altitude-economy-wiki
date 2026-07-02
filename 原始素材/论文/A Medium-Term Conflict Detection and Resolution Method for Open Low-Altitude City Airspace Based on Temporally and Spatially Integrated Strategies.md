# A Medium-Term Conflict Detection and Resolution Method for Open Low-Altitude City Airspace Based on Temporally and Spatially Integrated Strategies
IEEE TRANSACTIONS ON CONTROL SYSTEMS TECHNOLOGY, VOL. 28, NO. 5, SEPTEMBER 2020
## Authors
Wenyuan Yang , Jun Tang , Renjie He, and Yingguo Chen
## Abstract
The balancing of civil airspace capacities with customer demands is achieved through air traffic management (ATM), which uses decision support tools in ATM systems that are ensured by advanced communications and contemporary navigation technologies. However, uncertainties and perturbations can emerge during low-altitude airspace traffic management when considering plans to gradually open up low-altitude airspace in China. Domino effects of time and space deviations to one trajectory may lead to the generation of other 4-D trajectories (4-D trajectories defined based on a series of sequential waypoints recording three dimensions of spatial information and their relevant time information) due to strong levels of spatiotemporal connectivity between trajectories, rendering management challenging. This paper introduces background information and a literature review about conflict detection and resolution (CD&R) for open low-altitude airspace. From our analysis, a CD algorithm for a spatial grid partition system (SGPS) is presented. A conflict resolution (CR) framework of temporally and spatially integrated strategies including the time scheduling-based technique and vertical change-based technique (VCBT) was applied to the CR process. The CD&R algorithm was tested based on a practical maneuver scenario to check its validity, and an analysis of computational performance levels was conducted through several experiments. Airspace capacities can be enhanced to alleviate local airspace network perturbations through the use of the proposed CD&R algorithm.
### Index Terms
4-D trajectories, conflict detection (CD), conflict resolution (CR), low-altitude airspace, temporally and spatially integrated strategy

## I. INTRODUCTION
IN THE aviation industry, companies and control centers of airspace are consistently confronted with the challenge of maximizing the use of confined airspace resources while taking into account the issues of safety, stabilization, sustainability, and environmental protection to meet continuously increasing passenger flows and logistics volumes and other airspace use requirements. Current and future trends render issues of air traffic management (ATM) a highly relevant research subject. Numerous papers have been published on issues of ATM. Critical issues related to complexity assessments, safety criticality analyses, frameworks and methodologies, and future patterns of ATM have been explored in recent years [1]–[7]. Safety is the most important concern related to ATM, and naturally, conflicts have been highlighted in regard to the varieties of aircraft trajectories available. Over 60 conflict detection and resolution (CD&R) models and methods have been developed [8], and new problems are appearing over time and as new techniques emerge.

Aircraft used to open up low-altitude airspace has attracted considerable attention. While they may have several economic benefits, they may also introduce uncertainty and threaten safety levels in homologous airspace. As a developed country in terms of aviation technologies, the United States exhibits representative pilot industry trends. All rules and regulations of the Federal Aviation Administration (FAA) govern general aviation, with low-altitude airspace as a core regulatory focus. Evidently, the opening of low-altitude airspace has raised widespread concerns. The State Council and Central Military Commission of China issued the *Advice on reforming the management of low-altitude airspace*; under the policy of gradual low-altitude airspace liberalization, more airspace has been opened, bringing transformative changes to China’s aviation industry [9]. Multiple studies have investigated policies and operational strategies for open low-altitude airspace [10]–[13].

This paper centers on CD&R algorithms for urban open low-altitude airspace, focusing on the Guangzhou Free Flight project for Open Low-Altitude Traffic Management (OLATM), operated under centralized aviation control. The 4-D trajectory of low-altitude aircraft may violate predefined safe separation envelopes, requiring realignment of existing and newly submitted flight paths. This paper proposes a practical, efficient CD&R methodology tailored to this project.

To mitigate air traffic network congestion, traffic assignment methods distributing demand across time and space are detailed in [14]. Conflicts and congestion arise when two or more aircraft simultaneously occupy overlapping spatial volumes. Extensive research addresses CD&R problems; Table I summarizes existing literature across four dimensions. Supplementary relevant research is outlined below:
- Hwang and Tomlin proposed a CR algorithm later extended by Stanley [17];
- Ruiz et al. [20] built a CD&R platform based on Spatial Data Structures (SDS) for simplified 4-D nominal trajectory models, using Airspace Partitioning Methods (APM) to identify conflicts and Path Stretching (PS) for resolution; SDS applications are further elaborated in [28]–[32];
- Airspace segmentation for CR algorithms is studied in [33], [34];
- Alternative CR frameworks include dynamic integer programming [35], Coloured Petri Net (CPN) causal collision models [36]–[39].

Existing literature spans centralized/distributed control modes for traditional civil airspace and open low-altitude airspace (OLA), yet many methods suffer from excessive computational complexity or poor adaptability to China’s low-altitude operational context. This paper presents a temporally-spatially integrated CD&R algorithm with three core advantages:
1. **Comprehensive conflict resolution capability**: Time-based and spatial adjustment strategies serve as backups for one another, reducing secondary conflict generation during deconfliction.
2. **High computational efficiency**: Near-linear runtime scaling with problem size, enabling deployment for large-scale traffic scenarios.
3. **Strong robustness**: Fast re-deconfliction for newly submitted or modified flight trajectories.

### Table I SUMMARY OF PUBLICATIONS ON CD&R
| No. | Publication          | Optimization Tools       | CD Strategy          | CR Strategy               | Transportation Domain |
|-----|----------------------|--------------------------|----------------------|---------------------------|-----------------------|
|     |                      | CPN / CPLEX / Simulation | APM / GC / RTD      | CP / PS / IOM / CRCS      | TCA / OLA             |
| 1   | Goss et al.[15]      |                          |                      |                           |                       |
| 2   | Wollkind et al.[16]  |                          |                      |                           |                       |
| 3   | Stanley [17]         |                          |                      |                           |                       |
| 4   | Peng and Lin [18]    |                          |                      |                           |                       |
| 5   | Zuniga et al.[19]    |                          |                      |                           |                       |
| 6   | Ruiz et al. [20]     |                          |                      |                           |                       |
| 7   | Nosedal et al.[21]   |                          |                      |                           |                       |
| 8   | Velasco et al.[22]   |                          |                      |                           |                       |
| 9   | Alonso-Ayuso et al.[23,24] |                    |                      |                           |                       |
| 10  | Alejo et al.[25]     |                          |                      |                           |                       |
| 11  | Yang et al.[26]      |                          |                      |                           |                       |

> Abbreviation Glossary:
> RTD=Real-time Detection, CP=Constraint Program, PS=Path Stretching, IOM=Intelligent Optimization Method, CRCS=Combined Strategy Conflict Resolution, TCA=Traditional Civil Airspace, OLA=Open Low-altitude Airspace, CPN=Coloured Petri-Nets, APM=Airspace Partitioning Method, GC=Geometric Construction, √=Supported

### Paper Organization
- Section I: Research background and literature review of ATM CD&R
- Section II: Problem formulation and classical Medium-Term Conflict Detection & Resolution (MTCD&R) systems
- Sections III–IV: Proposed CD algorithm and integrated CR framework
- Section V: Simulation case study and computational performance analysis
- Section VI: Conclusions and future research directions

> Manuscript Metadata:
> Received July 2, 2018; revised Jan 26, 2019 / Jun 13, 2019; accepted Jun 17, 2019; published Jul 19, 2019; current version Aug 6, 2020
> Funding: National Natural Science Foundation of China (71601181); Hunan Provincial Natural Science Foundation (2019JJ20021); Huxiang Youth Talent Project (2018RS3079); Hunan Graduate Innovation Project (CX2018B020)
> Corresponding Author: Jun Tang
> Affiliation: College of Systems Engineering, National University of Defense Technology, Changsha 410073, China
> Digital Object Identifier: 10.1109/TCST.2019.2925579
> Copyright © 2019 IEEE

## II. PROBLEM DESCRIPTION
### A. Practical Application Background
Driven by aviation growth and AI-enabled low-altitude vehicles (UAVs, light sport aircraft), China’s national low-altitude reform policies have spurred demand for orderly low-altitude traffic management. This work originates from the Guangzhou Low-Altitude Free Flight project, which targets latent trajectory conflicts under Centralized Control Mode (CCM) for dense urban low-altitude airspace.

#### Centralized Control Mode Operational Scenario
1. Pre-assigned flight tasks generate planned 4-D trajectories for Low-Altitude Aircraft (LAA);
2. LAAs execute missions under real-time communication with a ground/vehicle-mounted central controller;
3. Mobile vehicle nodes can serve as distributed sub-control centers for logistics, search-and-rescue and other mission types.

The core challenge addressed: resolving conflicts generated by intersecting, dynamically updated flight trajectories, including newly inserted task paths.

### B. Conflict Definition
A fixed minimum safe separation buffer (horizontal + vertical + temporal) must be maintained between all LAAs to mitigate collision risks from wake turbulence, navigation/communication error, and data processing latency. Separation thresholds scale with aircraft mass; this paper focuses on small-to-medium low-altitude vehicles.

#### Safe Separation Criterion
Let $V_m$ = minimum vertical safe distance, $H_m$ = minimum horizontal safe distance; $dV$, $dH$ = instantaneous vertical/horizontal separation between two aircraft. A conflict occurs at any time satisfying:
$$d V<V_{m} \tag{1}$$
$$d H<H_{m} \tag{2}$$

![Fig. 2. Conflict between aircraft in proximity](reference_id="1-0")
*Figure 2: Cylindrical safety separation envelope for aircraft, illustrating horizontal separation $dH$ and vertical separation $dV$ thresholds*

#### Conflict Data Structure
Conflicts are continuous time intervals, formalized as a six-element vector:
$$CF_{i}=\left(i d c, i d t, t_{s}, t_{e}, P_{s}, P_{e}\right) \tag{3}$$
- $idc$: Unique conflict ID
- $idt$: Associated trajectory ID
- $t_s, t_e$: Conflict start / end timestamp
- $P_s, P_e$: WGS84 3D coordinates of conflict start/end positions, defined as:
$$P= (lat, lon, alt ) \tag{4}$$

Conflicts exist in paired matched sets; two conflict records $CF$, $CF'$ describe the same encounter if:
$$i d c=i d c' \tag{5}$$
$$t_{s}=t_{s}' \tag{6}$$
$$t_{e}=t_{e}' \tag{7}$$

### C. Classical MTCD&R System Overview
Conventional medium-term CD&R systems split into independent CD and CR subsystems:
1. CD Subsystem: Detects pairwise trajectory conflicts and generates deconflict advisories for manned/autonomous aircraft;
2. CR Subsystem: Revises 4-D trajectories to eliminate detected separation violations.

Limitations of classical pairwise CD&R:
- Pairwise CD algorithms scale poorly with large trajectory volumes;
- Most CR methods rely on single adjustment tactics, frequently unable to fully resolve complex multi-aircraft conflicts.

This paper proposes a Spatial Grid Partition System (SGPS) CD algorithm for high-throughput conflict screening, paired with a heuristic CR framework optimized for LAA flight characteristics.

## III. CONFLICT DETECTION ALGORITHM
### A. CD Module Input/Output Data Flow
The CD module discretizes continuous aircraft trajectories into timestamped 4-D waypoints and partitions the operational airspace into uniform 3-D spatial grids to identify overlapping spatiotemporal occupancy.
#### Input Parameters
1. Safety thresholds: $V_m$, $H_m$
2. Discretization time step $\Delta T$: Balances detection precision and computational overhead (smaller $\Delta T$ = higher accuracy, larger memory/runtime cost)
3. Trajectory list, each trajectory structured as:
$$TY_{i}=\left(i d t, t_{s}, t_{e}, PList \right) \tag{8}$$
- $idt$: Trajectory unique ID
- $t_s, t_e$: Trajectory active time window
- $PList$: Sequence of 4-D route points, each defined:
$$RP_{i}=(idp,t,P) \tag{9}$$
    - $idp$: Waypoint ID, $t$: Timestamp, $P$: WGS84 geospatial coordinate

#### Output
List of paired matched conflict records for downstream CR processing.

### B. Spatial Grid Partition System (SGPS)
SGPS discretizes continuous airspace into bounded cubic grids, replacing direct pairwise waypoint comparison with grid occupancy + time window matching to accelerate conflict detection.
1. **Airspace Boundary Feature Vector (BFV)**
Defines the full operational airspace extents via WGS84 bounds:
$$BFV=\left( Lat _{min }, Lat _{max }, Lon _{min }, Lon _{max }, Alt_{min }, Alt_{max }\right)$$
Longitude wrapping at the 180° meridian is handled by adding 360° to negative longitude values.

2. **Partitioned Grid Definition**
Uniform equidistant grid segmentation replaces cylindrical safety envelopes with axis-aligned bounding cubes for simpler geometric tests. Each grid cube $PG_j$ is defined by three maximum coordinate vertices:
$$PG_{i}=\left(P_{ma}, P_{mo}, P_{m h}\right) \tag{11}$$

3. **Waypoint-Grid Inclusion Test**
A discrete route point $RP_i$ lies inside partition grid $PG_j$ if all coordinate constraints hold:
$$
\begin{cases}
PG_{j}.P_{mo}.lat < RP_{i}.P.lat < PG_{j}.P_{ma}.lat \\
PG_{j}.P_{mh}.lon < RP_{i}.P.lon < PG_{j}.P_{mo}.lon \\
PG_{j}.P_{ma}.alt < RP_{i}.P.alt < PG_{j}.P_{mh}.alt
\end{cases}
$$

4. **Time-Windowed Grid (TWG) Construction**
For every grid intersected by a trajectory, extract the earliest entry waypoint $RP_{in}$ and latest exit waypoint $RP_{out}$ to form a time window $[RP_{in}.t, RP_{out}.t]$ for the grid:
$$TWG_{i}^{j}=\left(l p g, RP_{in }, RP_{out }\right)$$
- $TWG_i^j$: $j$-th time-windowed grid belonging to trajectory $i$
- $lpg$: Unique 3-D grid index label, calculated as $lpg=i+N_{x} j+N_{x} N_{y} k$ ($N_x, N_y$ = grid count along latitude/longitude axes)

### C. Trajectory Data Storage Architecture
Two complementary storage structures optimize CD lookup speed and memory efficiency:
1. **Hash Table for TWG Storage**
Each trajectory maps to a linked list of TWG entries. Hash table size is computed per trajectory segment:
$$N_{hash }=\sum_{m \in M}\left(\left|i_{s}^{m}-i_{e}^{m}\right|+\left|j_{s}^{m}-j_{e}^{m}\right|+\left|k_{s}^{m}-k_{e}^{m}\right|\right)+1$$
$M$ = total trajectory segments; $(i_s^m,j_s^m,k_s^m)/(i_e^m,j_e^m,k_e^m)$ = start/end grid indices of segment $m$.

![Fig. 4. Hash table for trajectory storage](reference_id="1-1")
*Figure 4: Hash table structure mapping each trajectory to its sequence of time-windowed grid objects*

2. **Boolean Occupancy Table (BT)**
Binary lookup table tracking which trajectories pass through each grid cell:
$$BT(i, j).Pass =\begin{cases}1, & \text{Trajectory }i \text{ occupies grid }j \\ 0, & \text{Otherwise}\end{cases}$$
Stores grid offset position alongside binary occupancy flag to avoid full hash table traversal during conflict screening.

### D. Conflict Detection Logic & Flowchart
Two trajectories $TY_a$, $TY_b$ conflict if they share identical grid labels $lpg$ and their grid time windows overlap:
$$RP_{in }^{b} \cdot t \leq RP_{in }^{a} \cdot t \leq RP_{out }^{b} \cdot t \tag{16}$$
$$RP_{in }^{a} \cdot t \leq RP_{in }^{b} \cdot t \leq RP_{out }^{a} \cdot t \tag{17}$$

Overlapping conflict time interval bounds:
$$
\begin{cases}
t_{s}=max \left(RP_{in}^{a} \cdot t, RP_{in}^{b} \cdot t\right) \\
t_{e}=min \left(RP_{out }^{a} \cdot t, RP_{out }^{b} \cdot t\right)
\end{cases}
$$

![Fig. 6. Conflict space-time overlap conditions](reference_id="1-2")
*Figure 6: (a) Spatial co-occupancy of two aircraft within a single grid cube; (b) Overlapping time windows defining conflict duration $[t_s,t_e]$*

Contiguous grids generating the same pairwise conflict are merged to eliminate duplicate conflict records.

![Fig. 7. Flowchart of the CD algorithm](reference_id="1-3")
*Figure 7: End-to-end conflict detection algorithm flow logic*

## IV. CONFLICT RESOLUTION ALGORITHM
The proposed CR framework integrates two complementary deconflict tactics:
1. Time Scheduling-Based Technique (TSBT): Adjust flight speed to shift trajectory timestamps, preserving original spatial path;
2. Vertical Change-Based Technique (VCBT): Modify altitude coordinates to maintain vertical separation when temporal adjustment fails.

### A. Model Assumptions & Flyability Validation
#### Core Simplifying Hypotheses
1. Aircraft maintain constant straight-line velocity between consecutive waypoints;
2. Maneuver execution time is negligible relative to conflict duration;
3. All revised trajectories must respect predefined minimum/maximum airspeed bounds.

#### Flyability Check
Segment average speed between adjacent waypoints $RP_i$, $RP_{i+1}$:
$$V_{i, i+1}=d_{i, i+1} /\left(R P_{i+1} . t-R P_{i} . t\right) \tag{19}$$
A trajectory segment is flyable if:
$$V_{min } \leq V_{i, i+1} \leq V_{max } \tag{20}$$
Full trajectory feasibility requires all segments to satisfy speed constraints.

### B. Three Fundamental Heuristic Principles
1. **FCFS (First-Come-First-Served)**: Trajectories sorted by submission priority / earliest start time for sequential deconfliction;
2. **Temporal-Spatial Integration**: Prioritize timeline adjustment (TSBT) before vertical altitude offset (VCBT);
3. **TSBT Priority Rule**: TSBT preserves original horizontal flight path with minimal mission disruption; vertical adjustments are a fallback only when speed constraints block temporal deconfliction.

#### Global CR Workflow Optimization
Instead of all-to-all pairwise conflict checks between candidate and resolved trajectories, only test candidate $TY_i$ against the pre-conflict-free trajectory list NTYList, reducing CD module call complexity from $O(n^2)$ to $O(n)$.

![Fig. 8. Flowchart of the integrated CR algorithm](reference_id="1-4")
*Figure 8: Main deconfliction loop: conflict grouping → TSBT trial → VCBT fallback → feasible trajectory storage*

### C. Matched Conflict Grouping
All conflicts for a candidate trajectory bounded by the same left/right segment waypoints $P_L$, $P_R$ form a single conflict group:
$$P_{L}=\left\{RP_{i} | RP_{i} \in T Y_{i} . PList, RP_{i} . t<CF_{j} . t_{s}, max(i)\right\} \tag{21}$$
$$P_{R}=\left\{RP_{i} | RP_{i} \in T Y_{i}.PList, RP_{i} . t>CF_{j} . t_{e}, min(i)\right\} \tag{22}$$
Only the leading conflict within each group requires resolution; cross-waypoint conflicts merge adjacent groups to avoid redundant computation.

![Fig. 9. Matched conflict grouping schematic](reference_id="1-5")
*Figure 9: Multiple separated conflict groups bounded by unique $P_L$/$P_R$ waypoint pairs on candidate trajectory $TY_i$*

### D. Time Scheduling-Based Technique (TSBT)
TSBT inserts new waypoints to accelerate/decelerate the candidate aircraft and eliminate temporal overlap with conflict-free reference trajectories, without altering horizontal geospatial coordinates.
1. **Deceleration Mode**: Delay arrival at conflict zone to wait for conflicting aircraft to exit
2. **Acceleration Mode**: Speed up to clear conflict zone before conflicting aircraft arrives

Inserted waypoint definition with safety time buffer $\delta$:
$$RP_{insert }=\begin{cases} \left(i d p, C F . t_{e}+\delta, C F . P_{s}\right), & \text{Deceleration} \\ \left(i d p, C F . t_{s}-\delta, C F . P_{e}\right), & \text{Acceleration} \end{cases} \tag{23}$$

![Fig. 10. TSBT acceleration/deceleration scenarios](reference_id="1-6")
*Figure 10: (a) Decelerate candidate to avoid overlap; (b) Accelerate candidate to clear conflict window early*

![Fig. 11. Flowchart of TSBT deconfliction process](reference_id="1-7")
*Figure 11: TSBT execution flow: deceleration attempt first, acceleration fallback if speed limits violated, feasibility validation post-modification*

### E. Vertical Change-Based Technique (VCBT)
When TSBT fails due to airspeed hard limits, VCBT adjusts conflict segment altitudes to satisfy vertical separation $V_m$. Vertical offset incurs lower operational cost than horizontal rerouting and leverages the smaller vertical safety buffer relative to horizontal separation.
#### Relative Altitude Change Velocity (RACV)
Determines whether candidate aircraft climbs or descends relative to conflicting traffic:
$$RACV=dA_{candidate }-d A_{matched } \tag{24}$$
$$d A_{candidate }=\frac{C F \cdot P_{e} \cdot alt -C F \cdot P_{s} \cdot alt }{C F . t_{e}-C F . t_{s}} \tag{25}$$
$$d A_{matched }=\frac{ MCF. P_{e} . alt - MCF . P_{s} .alt }{ MCF . t_{e}- MCF . t_{s}} \tag{26}$$
- $RACV>0$: Candidate maintains altitude above conflicting aircraft
- $RACV≤0$: Candidate maintains altitude below conflicting aircraft

#### Inserted Vertical Adjustment Waypoints
$$RP_{s}^{insert }=
\begin{cases}
\left(i d p, C F . t_{s},\left(C F . P_{s} .lat, C F . P_{s} .lon, MCF . P_{s} .alt +V_{m}\right)\right), & RACV >0 \\
\left(i d p, C F . t_{s},\left(C F . P_{s} .lat, C F . P_{s} .lon, MCF. P_{s} .alt -V_{m}\right)\right), & \text{Otherwise}
\end{cases}$$
$$RP_{e}^{insert}=
\begin{cases}
\left( idp, CF.t_{e},\left(C F . P_{e} .lat, C F . P_{e} .lon, MCF. P_{e} .alt +V_{m}\right)\right), & RACV>0 \\
\left( idp, CF.t _{e},\left( CF.P_{e} .lat, CF.P_{e} .lon, MCF. P_{e} .alt -V_{m}\right)\right), & \text{Otherwise}
\end{cases}$$

![Fig. 12. VCBT vertical adjustment schematic](reference_id="1-8")
*Figure 12: (a) Baseline vertical conflict; (b) Altitude offset at conflict start; (c) Altitude offset at conflict end; (d) Full dual-waypoint vertical adjustment maintaining $V_m$ separation*

![Fig. 13. Flowchart of VCBT vertical adjustment process](reference_id="1-9")
*Figure 13: VCBT algorithm flow: calculate insertion altitudes, interpolate waypoint elevations, validate flight speed constraints*

## V. SIMULATION AND RESULTS
Simulation hardware: Intel Core i7 3.10 GHz laptop with 4GB RAM; two test suites:
1. Realistic Guangzhou urban low-altitude flight case (5 trajectories, 4 pairwise conflicts);
2. Random cross-traffic large-scale scenarios (50–500 trajectories) for computational performance benchmarking.

### A. Guangzhou Practical Scenario Test
#### Simulation Parameters
- Horizontal safe separation $H_m=500\mathrm{m}$, vertical safe separation $V_m=100\mathrm{m}$
- Trajectory discretization timestep $TimeStep=1\mathrm{s}$
- 4 pre-planned conflict-free LAA trajectories; LAA-05 introduces four separation violations.

![Fig. 15. 3D visualization of initial unresolvable conflicts](reference_id="1-10")
*Figure 15: Four pairwise trajectory conflicts between LAA-05 and existing traffic*

#### Stepwise Deconfliction Process
1. Steps 1–2: TSBT speed adjustment resolves conflicts LAA05-LAA01, LAA05-LAA02, LAA05-LAA03;
2. Step 3: TSBT fails for LAA04-LAA05 due to airspeed constraints; VCBT vertical offset applied to eliminate final conflict.

![Fig. 16. Post-deconfliction 3D visualization](reference_id="1-11")
*Figure 16: Trajectories after integrated TSBT/VCBT adjustment with full safety separation maintained*

Tables IV/V record raw conflict detection logs and revised LAA-05 trajectory waypoints across deconflict iterations.

### B. Large-Scale Random Scenario Benchmark
#### Scenario Generation Logic
Chessboard crisscross trajectory generator with two flight directions: FNTS (North-to-South), FWTE (West-to-East). Airspace bounds:
$Lat_{min}=22^\circ, Lat_{max}=23^\circ, Lon_{min}=114^\circ, Lon_{max}=115^\circ, Alt_{min}=500\mathrm{m}, Alt_{max}=800\mathrm{m}$

![Fig. 17. Random crisscross trajectory generation schematic](reference_id="1-12")
*Figure 17: Mixed FNTS/FWTE random trajectory layout within bounded low-altitude airspace*

#### Computational Performance Results
1. **Runtime Variability**: Small trajectory sets ($n≤150$) exhibit large relative runtime variance (~25–42%) from random traffic density fluctuations; at $n=500$, relative runtime range reduces to only 5.4%, demonstrating strong large-scale robustness.
2. **Time Complexity Linear Fit**: Average execution time vs trajectory count produces linear regression $y=-91.04761 + 1.71948x$, Pearson correlation coefficient $r=0.9973$, confirming near-linear scaling.

![Fig. 18. Box plots of execution time across trajectory volumes](reference_id="1-13")
*Figure 18: Box-and-whisker runtime distributions for 10 randomized scenarios per trajectory count (50–500 flights)*

![Fig. 19: Linear fit of average CD&R execution time](reference_id="1-14")
*Figure 19: Linear regression of mean runtime against total trajectories, near-perfect linear correlation*

#### CD&R Performance Indicator $I_{cdr}$
Standardized benchmark metric for cross-algorithm comparison:
$$I_{cdr}=\frac{t_{c}}{N_{avg} \cdot F_{cpu}} \tag{29}$$
- $t_c$: Total CD&R wall-clock time
- $N_{avg}$: Average detected conflict count
- $F_{cpu}$: CPU clock frequency (GHz)
Smaller $I_{cdr}$ = superior computational efficiency.

Baseline reference value from Ruiz et al. (2.16GHz dual-core CPU, 63 conflicts resolved in 2s): $I_{ref}≈0.01470$.
Algorithm comparison shows proposed method outperforms reference benchmarks for trajectory counts ≥300, with efficiency gains growing at higher traffic density.

## VI. CONCLUSION
### A. Core Conclusions
This paper proposes a medium-term integrated temporal-spatial CD&R algorithm for urban open low-altitude airspace with verified real-scenario validity and scalable computational performance:
1. Automatically and efficiently detects latent 4-D trajectory separation violations via spatial grid partitioning;
2. Sequential TSBT+VCBT deconfliction minimizes horizontal flight path disruption for LAA mission continuity;
3. Near-linear runtime scaling supports centralized online low-altitude traffic control for dense urban airspace;
4. Reduces local airspace network turbulence and congestion by eliminating cascading trajectory deviation domino effects.

### B. Future Research Directions
1. Quantify and mitigate random factors (traffic density, trajectory spatial distribution) impacting algorithm runtime robustness;
2. Integrate machine learning conflict prediction to reduce secondary conflict generation and further accelerate large-scale CD&R;
3. Extend model to incorporate complex low-altitude operational constraints: no-fly zones, terrain obstacles, heterogeneous multi-type low-altitude aircraft performance limits.

## REFERENCES
[1] D. Chiappe, K.-P. Vu, and T. Strybel, “Situation awareness in the NextGen air traffic management system,” Int. J. Hum.-Comput. Interact., vol. 28, no. 2, pp. 140–151, Feb. 2012.
[2] K. Margellos and J. Lygeros, “Toward 4-D trajectory management in air traffic control: A study based on Monte Carlo simulation and reachability analysis,” IEEE Trans. Control Syst. Technol., vol. 21, no. 5, pp. 1820–1833, Sep. 2013.
[3] A. Gardi, R. Sabatini, and T. Kistan, “Multiobjective 4D trajectory optimization for integrated avionics and air traffic management systems,” IEEE Trans. Aerosp. Electron. Syst., vol. 55, no. 1, pp. 170–181, 2018.
[4] M. Prandini, L. Piroddi, S. Puechmorel, and S. L. Brazdilova, “Toward air traffic complexity assessment in new generation air traffic management systems,” IEEE Trans. Intell. Transp. Syst., vol. 12, no. 3, pp. 809–818, Sep. 2011.
[5] E. De De Santis, M. D. Di Benedetto, M. Everdij, D. Pezzuti, G. Pola, and L. Scarciolla, “Safety criticality analysis of air traffic management systems: A compositional bisimulation approach,” in Proc. 3rd SESAR Innov. Days, Stockholm, Sweden, Nov. 2013, pp. 1–8.
[6] M. Soler, A. Olivares, E. Staffetti, and D. Zapata, “Framework for aircraft trajectory planning toward an efficient air traffic management,” J. Aircraft, vol. 49, no. 1, pp. 341–348, Jan./Feb. 2012.
[7] M. Strohmeier, M. Schafer, V. Lenders, and I. Martinovic, “Realities and challenges of NextGen air traffic management: The case of ADS-B,” IEEE Commun. Mag., vol. 52, no. 5, pp. 111–118, May 2014.
[8] J. Kuchar and L. C. Yang, “A review of conflict detection and resolution modeling methods,” IEEE Trans. Intell. Transp. Syst., vol. 1, no. 4, pp. 179–189, Dec. 2000.
[9] W. Yonggang and F. Mengmeng, “Airworthiness management of light sport aircraft (LSA) in the situation of opening low-altitude airspace,” Procedia Eng., vol. 17, pp. 369–374, Jan. 2011.
[10] T. Che, “Research on safety management of China’s private flight— Against the background of low-altitude airspace management reform,” J. Southwest Petroleum Univ., vol. 14, no. 4, pp. 53–56, 2012.
[11] B. Feng, “On reform of China’s low-altitude airspace management and aviation safety,” J. Civil Aviation Flight Univ. China, 2012.
[12] Q.-R. Sun, D.-K. Yao, and Y.-Y. Zhou, “Preliminary study on China’s low-altitude airspace operation safety evaluation method,” in Proc. Nat. Conf. Electr., Electron. Comput. Eng., Dec. 2015, pp. 2352–5401.
[13] X. Chen and S. O. Law, “On rights to use low altitude airspace in the content of low-altitude open-up policy,” J. Beijing China Univ. Aeronaut. Astronaut., vol. 29, no. 1, pp. 47–57, 2016.
[14] D. Daniel, S. Oussedik, and P. Stephane, “Airspace congestion smoothing by multi-objective genetic algorithm,” in Proc. ACM Symp. Appl. Comput., Mar. 2005, pp. 907–912.
[15] J. Goss, R. Rajvanshi, and K. Subbarao, “Aircraft conflict detection and resolution using mixed geometric and collision cone approaches,” in Proc. AIAA Guid., Navigat., Control Conf. Exhibit., Aug. 2004, pp. 1–20.
[16] S. Wollkind, J. Valasek, and T. Ioerger, “Automated conflict resolution for air traffic management using cooperative multiagent negotiation,” in Proc. AIAA Guid., Navigat., Control Conf., Aug. 2004, p. 4992.
[17] A. Stanley, “Flight path deconfliction of autonomous UAVs,” in Proc. AIAA Infotech Aerosp., Sep. 2005, p. 6978.
[18] L. Peng and Y. Lin, “Study on the model for horizontal escape maneuvers in TCAS,” IEEE Trans. Intell. Transp. Syst., vol. 11, no. 3, pp. 392–398, Jun. 2010.
[19] C. A. Zúñiga, M. A. Piera, S. Ruiz, and I. Del Pozo, “A CD&CR causal model based on path shortening/path stretching techniques,” Transp. Res. C, vol. 33, pp. 238–256, Aug. 2013.
[20] S. Ruiz, M. A. Piera, and I. Del Pozo, “A medium term conflict detection and resolution system for terminal maneuvering area based on spatial data structures and 4D trajectories,” Transp. Res. C, Emerg. Technol., vol. 26, pp. 396–417, Jan. 2013.
[21] J. Nosedal, M. A. Piera, S. Ruiz, and A. Nosedal, “An efficient algorithm for smoothing airspace congestion by fine-tuning take-off times,” Technologies, vol. 44, pp. 171–184, Jul. 2014.
[22] G. A. M. Velasco, C. Borst, J. Ellerbroek, M. M. van Paassen, and M. Mulder, “The use of intent information in conflict detection and resolution models based on dynamic velocity obstacles,” IEEE Trans. Intell. Transp. Syst., vol. 16, no. 4, pp. 2297–2302, Aug. 2015.
[23] A. Alonso-Ayuso, L. F. Escudero, and F. J. Martín-Campo, “On modeling the air traffic control coordination in the collision avoidance problem by mixed integer linear optimization,” Ann. Oper. Res., vol. 222, no. 1, pp. 89–105, Nov. 2014.
[24] A. Alonso-Ayuso, L. F. Escudero, F. J. Martín-Campo, and N. Mladenovi´c, “A VNS metaheuristic for solving the aircraft conflict detection and resolution problem by performing turn changes,” J. Global Optim., vol. 63, no. 3, pp. 583–596, Nov. 2015.
[25] D. Alejo, J. A. Cobano, G. Heredia, and A. Ollero, “An efficient method for multi-UAV conflict detection and resolution under uncertainties,” in Proc. Robot 2nd Iberian Robot. Conf. Cham, Switzerland: Springer, 2016, pp. 635–647.
[26] Y. Yang, J. Zhang, K.-Q. Cai, and M. Prandini, “Multi-aircraft conflict detection and resolution based on probabilistic reach sets,” IEEE Trans. Control Syst. Technol., vol. 25, no. 1, pp. 309–316, Jan. 2017.
[27] I. Hwang, J. Kim, and C. Tomlin, “Protocol-based conflict resolution for air traffic control,” Air Traffic Control Quart., vol. 15, no. 1, pp. 1–34, 2007.
[28] S. Ruiz, M. Piera, and C. Zúñiga, “Relational time-space data structure to speed up conflict detection under heavy traffic conditions,” SESAR Innov. Days (SID), 2011.
[29] S. Ruiz, M. Piera, A. Ranieri, and R. Martinez, “Computational efficient conflict detection and resolution through spatial data structures,” in Proc. Int. Conf. Res. Air Transp., 2012.
[30] S. Ruiz and M. A. Piera, “Relational time-space data structure to enable strategic de-confliction with a global scope in the presence of a large number of 4D trajectories,” J. Aerosp. Oper., vol. 2, nos. 1–2, pp. 53–78, Jan. 2013.
[31] S. Ruiz, M. A. Piera, J. Nosedal, and A. Ranieri, “Strategic deconfliction in the presence of a large number of 4D trajectories using a causal modeling approach,” Transp. Res. C, Emerg. Technol., vol. 39, pp. 129–147, Feb. 2014.
[32] J. Nosedal-Sánchez, “Aircraft departure synchronization to reduce ATC en route interventions,” Ph.D. dissertation, Dept. de Telecommun. i Enginyeria de Sistemes, Univ. Autònoma de Barcelona, Bellaterra, Spain, 2016.
[33] P. Kopardekar, K. Bilimoria, and B. Sridhar, “Initial concepts for dynamic airspace configuration,” in Proc. 7th AIAA Aviation Technol., Integr. Oper. Conf. (ATIO), Belfast, Northern Ireland, Sep. 2007, pp. 18–20.
[34] J. Tang, S. Alam, C. Lokan, and H. A. Abbass, “A multi-objective approach for dynamic airspace sectorization using agent based and geometric models,” Transp. Res. C, Emerg. Technol., vol. 21, no. 1, pp. 89–121, 2012.
[35] C. N. Glover and M. O. Ball, “Stochastic optimization models for ground delay program planning with equity–efficiency tradeoffs,” Transp. Res. C, Emerg. Technol., vol. 33, pp. 196–202, Aug. 2013.
[36] T. Jun, M. A. Piera, and S. Ruiz, “A causal model to explore the ACAS induced collisions,” Proc. Inst. Mech. Eng., G, J. Aerosp. Eng., vol. 228, no. 10, pp. 1735–1748, 2014.
[37] J. Tang, M. A. Piera, and T. Guasch, “Coloured Petri net-based traffic collision avoidance system encounter model for the analysis of potential induced collisions,” Transp. Res. C, Emerg. Technol., vol. 67, pp. 357–377, Jun. 2016.
[38] J. Tang, “Review: Analysis and improvement of traffic alert and collision avoidance system,” IEEE Access, vol. 5, pp. 21419–21429, 2017.
[39] J. Tang, F. Zhu, and M. A. Piera, “A causal encounter model of traffic collision avoidance system operations for safety assessment and advisory optimization in high-density airspace,” Transp. Res. C, Emerg. Technol., vol. 96, pp. 347–365, Nov. 2018.
[40] S. Ruiz and M. A. Piera, “A TMA simulation model for efficient conflict detection and resolution based on spatial data structures,” in Proc. WAMS, May 2010, pp. 239–244.

## Author Biographies
### Jun Tang
Assistant Professor, College of Systems Engineering, National University of Defense Technology. Former PhD researcher at Universitat Autònoma de Barcelona aeronautical innovation cluster. Research interests: UAV air traffic management, Coloured Petri Nets, logistics aviation, state-space modeling.

### Renjie He
Professor, College of Systems Engineering, National University of Defense Technology. Multidisciplinary research covering system planning, intelligent management, OR/AI cross theory, applied decision-making systems.

### Wenyuan Yang
PhD candidate, College of Systems Engineering, National University of Defense Technology. Research directions: UAV scheduling, air traffic conflict resolution, earth observation satellite multi-objective optimization, logistics system planning.

### Yingguo Chen
Assistant Professor, College of Systems Engineering, National University of Defense Technology. Research fields: combinatorial optimization, satellite scheduling, machine learning, aviation logistics planning.