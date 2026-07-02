# Towards Transparent and Privacy-Preserving Urban Airspace Management: A Blockchain-Based Scheme Under the Airspace-Resource-Centric Concept
## Authors
Qianyu Liu∗, Wei Dai†, Lingling Ma‡, and Claudio J. Tessone∗
- ∗Blockchain and Distributed Ledger Technologies, Universerty of Zurich, Zurich, Switzerland
- †Research Institute for Science & Technology Innovation, Civil Aviation University of China, Tianjin, China
- ‡College of Air Traffic Management, Civil Aviation University of China, Tianjin, China
Corresponding Author: Wei Dai
Email: wdai@cauc.edu.cn

## Index Terms
urban air mobility, blockchain application, smart contract, airspace management

## Abstract
The rapid development of Urban Air Mobility (UAM) bring new challenges for the efficient, secure, and fair management of low-altitude airspace. However, traditional air traffic control systems struggle to meet the dynamic demands of UAM operations, especially in scenarios involving various types of aerial vehicles with differing operational requirements. This paper proposes a consortium blockchain-based airspace reservation system, utilizing a no-token blockchain architecture and an Airspace-Resource-Centric (ARC) framework, aimed at addressing critical issues such as trust, security, privacy protection, and event traceability. The system is built on Hyperledger Fabric and adopts a three-layer architecture, enabling decentralized coordination, automated governance through smart contracts, and privacy-preserving data sharing. Additionally, the paper evaluates the system’s performance under varying load conditions through agent-based modeling (ABM) simulations. The results demonstrate that, under low-to-medium loads, the system maintains stable transaction confirmation latency and throughput. Under high load conditions, while system performance may degrade, the fault recovery capability remains robust, and network latency stays stable. Finally, based on the simulation results, the paper provides deployment recommendations for local implementation of the framework, focusing on hardware resource optimization and queue management strategies to improve load balancing and reduce performance bottlenecks under high-load scenarios.

## I. INTRODUCTION
As conventional air transportation gradually matures, the emerging Low-Altitude Economy (LAE) has become a new growth point for the aviation industry. Urban Air Mobility (UAM) is a major LAE scenario [1], [2]. Metropolitan areas have concentrated populations and resources, and face increasing traffic congestion, so there is a strong motivation to develop new air transportation modes. UAM envisions a future where air taxis, drones, and other aerial vehicles seamlessly integrate into metropolitan environments, offering fast and flexible mobility [3].

UAM has very different characteristics from conventional aviation. It covers a wide range of tasks, making it a highly flexible solution for urban transportation. These tasks include transporting passengers, delivering packages, providing emergency medical services, inspecting infrastructure, and conducting surveillance. Each type of task has different needs, such as how high vehicles fly, how fast they go, how big they are, and how long they need to stay in the air. For example, air taxis for passengers require careful scheduling and route planning, while medical drones need to fly quickly and directly in emergencies. However, delivery drones might operate frequently in crowded areas over varying distances.

The diversity in UAM presents challenges to the management of air traffic [4], [5]. Current air traffic systems were not designed for the high number of low-altitude flights that UAM brings. They are also not equipped to handle a mix of manned and autonomous vehicles, each with different speeds and priorities. Adding UAM to the airspace used by regular airplanes makes it even harder to organize flight paths, avoid collisions, and ensure smooth communication.

The urban airspace is the basis of UAM operations. Effective management of urban airspace is critical to the successful implementation of UAM. Urban airspace is complex and airspace resources are limited. Precision management of urban airspace and its resources can help ensure safe, efficient, and equitable airspace usage. By adopting advanced airspace management techniques, UAM systems can minimize conflicts, optimize flight paths, and prioritize different types of missions based on urgency and necessity. Such an approach not only ensures smooth operations but also aligns with broader goals of sustainability and accessibility in urban transportation.

Efforts have been made to address the urban airspace management problem, which includes macroscopic airspace categorization, sky-lanes and corridors design, route network construction, etc [6]. Among these, ARC management has emerged as a promising solution [7], [8]. The ARC concept presents a shift from the traditional aircraft-centric approach in conventional air traffic management to an urban airspace-focused paradigm, establishing a unified framework for the integrated management of heterogeneous airspace resources. As illustrated in Fig. 1, fundamentals of the ARC concept include discretization of airspace, projection of resources to airspace cells, and four-dimensional management of resources through dynamic allocation and monitoring. The ARC concept offers a unified framework to coordinate and monitor the utilization of urban airspace and its associated resources, ensuring more efficient and streamlined operations.

The concept of ARC airspace management effectively optimizes the usage of airspace and its resources, to better facilitate large-scale UAM operations. Successful implementation of the ARC concept requires a concordance in the airspace situational awareness among stakeholders including airspace users and managers, which needs consensus-building on the occupancies and reservations of airspace cells. A reliable and efficient airspace reservation system is critical for mitigating potential conflicts between multiple operators and ensuring the orderly functioning of urban aerial traffic. In addition, the privacy of airspace users should be preserved for business reasons.

Blockchain technology has emerged as a robust tool for addressing complex data management and coordination challenges in multi-stakeholder environments [9]. By providing a decentralized, immutable, and transparent platform [10], blockchain offers unique advantages for implementing a secure and efficient airspace reservation system. Integrating blockchain into UAM airspace management can enable realtime coordination among stakeholders, resolve disputes, and enhance operations’ trustworthiness [11]. Smart contracts, a key feature of blockchain, can automate reservation protocols, reduce administrative overhead, and provide auditable records of airspace transactions [12].

This paper proposes a consortium blockchain-based airspace reservation system which is tokenless to satisfy the needs of UAM. The proposed system leverages distributed ledger technology and smart contracts to streamline the reservation process, improve coordination between airspace operators, and ensure compliance with regulatory frameworks. By addressing the limitations of traditional centralized airspace management systems, this approach aims to enhance operational efficiency, scalability, and security. The study further evaluates the feasibility of this system through agent-based model(ABM), offering insights into its potential to revolutionize urban air traffic management.

> This research is supported by the Fundamental Research Funds for the Central Universities under the Civil Aviation University of China. Qianyu Liu is supported by the China Scholarship Council (CSC).
> Authorized licensed use limited to: Zhejiang University. Downloaded on July 01,2026 at 06:51:58 UTC from IEEE Xplore. Restrictions apply.
> 2025 Integrated Communications, Navigation and Surveillance Conference (ICNS) | 979-8-3315-3473-8/25/$31.00 ©2025 IEEE | DOI: 10.1109/ICNS65417.2025.10976922

![Fig.1 ARC Concept Diagram](reference_id="14-stdin1")
Fig. 1. The concept of Airspace-Resource-Centric management
- Green Cube: Unoccupied Block
- Yellow Cube: Block Allocated to Aircraft
- Red Cube: Block Requires Additional Attention
Right panel: Discretized Airspace Resources
  - Spatial Volumn
  - Separation Minima Informed Sizing
  - CNS Resources
  - uPBN Concept
  - Risk Awareness
  - Spatial Temporal ARC Management
Bottom isometric diagram: Low/High Density Living Area, Low/High Density Industrial Area zoning matching discretized airspace blocks

## II. METHODOLOGY
### A. Statement of Problem
Under the ARC management paradigm, significant trust barriers and collaboration dilemmas exist between Urban Navigation Service Providers (UNSPs) and flight operators [13]. These challenges manifest in three primary aspects:
1. The approval of Operational Intent Volumes (OIV) relies on manual verification, typically requiring over 24 hours per process, which fails to meet the real-time scheduling demands of high-density fleets;
2. Airspace status queries may expose commercially sensitive information, causing operators to avoid sharing data for competitive reasons;
3. The lack of postevent traceability mechanisms makes it difficult to effectively penalize malicious reservation or unauthorized occupation behaviors.

These issues severely constrain the improvement of airspace resource utilization efficiency and have become critical bottlenecks hindering UAM industrialization.

To address these challenges, we propose a consortium blockchain-based trusted OIV management framework where only pre-defined participants can join. The core innovation lies in deeply coupling distributed ledger technology with privacy-preserving computing to establish a new airspace collaborative management paradigm that balances authoritative supervision with privacy protection. The system achieves three breakthrough innovations:
1. Automation of the approval process through smart contracts, reducing response latency from hours to seconds;
2. Design of multi-level data visibility rules enabling participants to verify airspace unit availability while preventing access to competitors’ operational details;
3. Utilization of blockchain’s immutability to establish a complete operation traceability chain, providing reliable evidence for regulatory enforcement.

### B. System Architecture Design
The system adopts a three-layer decoupled architecture, enabling privacy-preserving collaboration among multiple parties while preserving the regulatory authority of the UNSP. Multi-level data access control rules are implemented to meet the needs of different stakeholders: UNSP has global access to airspace data for audit and supervision, while airspace operators can only query the occupancy status of specific airspace units without accessing sensitive competitor information. This approach ensures privacy protection and allows UNSP to enforce regulatory oversight, preventing malicious reservations and unauthorized occupation. The system is built on a Hyperledger Fabric consortium network, a permissioned blockchain framework that supports modular consensus protocols and private channels [14]. By integrating blockchain technology with privacy-preserving mechanisms, this architecture effectively addresses the dynamic and security challenges of UAM.

![Fig.2 Three-layer System Architecture](reference_id="14-stdin2")
Fig. 2. Three-layer System Architecture.
1. Application Layer: Client-Operator 1~4, Client-UNSP; Smart Contract (Reservation & Query) + Audit module
2. Blockchain Layer: Operator Peer Nodes, Airspace Channel, UNSP + Operator Order Nodes
3. Data Layer: Public Data (Airspace Slots) / Private Data (Ownership) stored in CouchDB

#### 1. Application Layer
The application layer serves as the human-machine interaction interface, provides standardized airspace service APIs. Airspace operators submit 4D airspace reservation requests through encrypted APIs, while the system employs two-factor authentication to verify the legitimacy of requesters. To avoid Denial of Service (DoS) attacks, the application layer enforces request ratelimiting policies, restricting each operator to a maximum of five queries per second. Additionally, the application layer supports an auditing interface, enabling UNSP to retrieve and analyze airspace usage records without compromising operational privacy.

#### 2. Blockchain Layer
- The system is built on a Hyperledger Fabric consortium network, comprising one UNSP node and four airspace operator nodes.
- Transactions are processed within a dedicated blockchain channel named Airspace Channel, which ensures data integrity and controlled access based on predefined policies:
  - UNSP node holds global read/write privileges, enabling full audit and oversight over all transactions;
  - Airspace operators can only query specific airspace unit occupancy status, unable to access rival sensitive operation data.
- Consensus mechanism: Raft protocol, UNSP acts as initial leader node; automatic leader reallocation occurs upon node failure to maintain network stability.
- Smart contracts automate reservation and query logic, ensuring tamper-proof, transparent airspace allocation and monitoring records.

#### 3. Data Layer
1. Public Ledger: Stores spatial coordinate, timestamp, occupancy metadata; supports efficient range queries, no sensitive competitor data exposed.
2. Private Dataset: Confidential airspace ownership data linked via cryptographic hash pointers to public ledger, privacy-protected and verifiable.
3. CouchDB: Persistent state database for structured data indexing and fast reservation/audit retrieval.

### C. Smart Contract-driven Automated Governance
This work develops an on-chain automated reservation and governance mechanism based on smart contracts to meet the specialized requirements of airspace resource management. This mechanism implements programmatic rules to automate the entire resource allocation process. The automation not only improves allocation efficiency but also ensures fairness and traceability throughout the process. When an airspace operator initiates an airspace reservation request, the smart contract executes two core steps sequentially.
1. Airspace conflict detection: Based on distributed database spatiotemporal indexing, verify target airspace time-window occupancy; only consensus-confirmed reservation records are validated to avoid state inconsistency.
2. Timestamp-based priority mechanism: For concurrent reservation requests, on-chain timestamp is the sole priority judgment standard; combined with blockchain natural transaction ordering, eliminate allocation randomness under high concurrency.

### D. Privacy-preserving Data Storage
To balance airspace allocation transparency and operator commercial privacy, the system adopts hybrid private + public data storage with cryptographic hash pointers.
1. Private Data Collections
Sensitive data (operator ID, mission type, payload, flight path) stored in encrypted private datasets via Hyperledger Fabric PDC mechanism. Access permission limited to the operator itself and UNSP; competitors only view airspace occupied status without mission details.
2. Cryptographic Hash Pointers
Private ownership records generate SHA-256 hash digests embedded into public ledger. Regulators verify data consistency by recalculating hash values, third parties cannot reverse deduce confidential information.
3. End-to-End Encryption
All private dataset transmission and storage use full encryption to prevent data leakage from network interception.

### E. Raft Consensus Fault Tolerance
The system adopts Raft consensus for leader election and log replication, with adaptive timeout parameters to improve distributed network fault tolerance.
- Initial state: UNSP node as temporary leader for system startup;
- Node failure: Automatic leader election among operator nodes to sustain service;
- Recovery mechanism: Failed nodes synchronize full log data via Raft replication before rejoining the network, guarantee global state consistency.
- Adaptive block packaging: Two adjustable parameters (block size limit, packaging timeout) balance transaction latency and system throughput to adapt variable network loads.

### F. Airspace Resource Modeling
Adopting the ARC concept modeling method, airspace resource mathematical expression:
\[
\mathcal {A}=\{ R ^{x,y,z,t}\} \tag{1}
\]
Where $\mathcal{A}$ = full airspace resource set, $R^{x,y,z,t}$ = discretized four-dimensional airspace unit (3 spatial axes + time axis). Spatial-temporal discretization resolution depends on airspace complexity, navigation equipment performance and UAM traffic volume. Performance-based navigation static cell sizing is a mature practical scheme, adapting to multi-type aircraft operation.

Rule update mechanism: UNSP can submit airspace parameter adjustment proposals; modifications take effect after majority node consensus. All policy changes are recorded immutably on chain for full traceability, and new parameters auto-apply to subsequent reservation workflows.

### G. Agent-Based System Performance Evaluation
Agent-Based Modeling (ABM) simulation framework is built for quantitative system performance test before real deployment. Core agent types: organization node agents (UNSP / operator consensus simulation), transaction generator agents, performance metric collectors. Adjustable simulation variables: network latency, node failure probability, recovery time, batch processing parameters.

Key evaluation indicators: transaction confirmation latency, system throughput (TPS), hardware resource utilization (CPU/memory/bandwidth), fault recovery time. Progressive load testing is adopted by adjusting transaction generation rate to simulate light/medium/heavy operation scenarios.

## III. SIMULATION RESULTS AND ANALYSIS
### A. Simulation Environment Configuration
1. Network Topology: 5 full-connected distributed nodes (1 UNSP + 4 operators). Inter-node communication latency normal distribution (mean=0.05s, std=0.01s). Matching urban airspace 3–5 mainstream operator real scene, 5G/edge computing low-latency environment.
2. Consensus Parameters: Raft election timeout random distribution (mean=1.5s, std=0.5s), fixed heartbeat interval 0.5s. Batch size gradient group: [100, 200, 300, 400, 500] transactions. Election timeout can be extended under high network load to reduce frequent leader switching.
3. Fault Injection: Node failure probability =1% per second, recovery time uniform distribution 5–10s; network partition probability =0.1% per second, duration 5–10s, matching real infrastructure rare failure scenarios.
4. Workload Design: Transaction rate gradient 10~200 TPS (9 levels), Poisson arrival process. Total simulation duration 10000s to reach stable operation state and collect valid metrics.

### B. Performance Evaluation Results
1. System Transaction Performance
Under low-to-medium load (10–125 TPS): System stable, average confirmation latency 0.7–1.2s, throughput close to target value, average network latency fixed around 60ms.
Under high load (150–200 TPS): Resource saturation occurs, average transaction latency surges to 69s at 200TPS, throughput drops obviously, transaction queue accumulates heavily. But the system maintains basic service without data loss or full crash.

![Fig.5 Effective System Throughput](reference_id="14-stdin3")
Fig. 5. Effective System Throughput: X-axis Target TPS, Y-axis Actual TPS
Trend: Throughput rises gradually, fluctuates at 150TPS, peaks at 175TPS then declines under 200TPS heavy load.

![Fig.6 Network Performance](reference_id="14-stdin4")
Fig. 6. Network Performance: X-axis Transaction Rate, Y-axis Average Network Latency(s)
Network latency stabilizes near 0.06s across all load gradients with minor fluctuations.

2. Fault Tolerance Simulation
During 10000s simulation period, total node failure events range 7–15 across all load gradients. All failed nodes auto-recover within 5.8–9.8s, no inconsistent chain data generated during recovery. Raft leader switching and log replication guarantee continuous service.

![Fig.7 Node Failures Impact](reference_id="14-stdin5")
Fig. 7. Node Failures Impact: X-axis Transaction Rate, Y-axis Number of Failures
Node failure frequency slightly decreases under high traffic volume due to full node participation.

3. Consensus Efficiency
Leader election frequency stable across all loads, negligible impact on overall system performance. Network latency maintains 59–61ms stably, meeting UAM real-time data exchange demand.
4. Deployment Suggestions
- Expand node hardware scale or upgrade single-node computing power for load balance;
- Dynamic adjust block batch threshold and set queue length upper limit to ease heavy load congestion.

## IV. CONCLUSION AND FUTURE PROSPECTS
This study proposes a blockchain-based urban airspace resource reservation management system built on Hyperledger Fabric. The three-layer architecture realizes decentralized supervision while protecting commercial privacy, supporting full 4D airspace resource reservation via smart contracts, and adopts private data sets to isolate sensitive business information. Complete automated airspace reservation audit workflow is constructed.

ABM simulation results verify the system’s stable operation under light and medium traffic loads, and strong fault recovery capacity even at high throughput saturation. However, the current research only relies on simulation verification without real network testing. Future work plans:
1. Build multi-physical-node test network, use Hyperledger Caliper to complete benchmark real-scene testing;
2. Optimize smart contract parallel processing capacity to improve high-concurrency performance;
3. Cooperate with air traffic control authorities to collect real UAM operation data, iterate simulation model;
4. Research docking schemes with traditional air traffic management systems to build cross-system coordination mechanism.

In general, this paper provides a blockchain technical solution for urban airspace reservation management. The theoretical design and simulation results lay a foundation for subsequent engineering deployment, and the optimized framework can provide secure, privacy-preserving, efficient intelligent air traffic control support for future urban low-altitude operation.

# REFERENCES
[1] D. P. Thipphavong, R. Apaza, B. Barmore, V. Battiste, B. Burian, Q. Dao, M. Feary, S. Go, K. H. Goodrich, J. Homola et al., “Urban air mobility airspace integration concepts and considerations,” in 2018 aviation technology, integration, and operations conference, 2018, p. 3676.
[2] Z. Jin, K. K. Ng, C. Zhang, L. Wu, and A. Li, “Integrated optimisation of strategic planning and service operations for urban air mobility systems,” Transportation Research Part A: Policy and Practice, vol. 183, p. 104059, 2024.
[3] Z. Wang, D. Delahaye, J.-L. Farges, and S. Alam, “Complexity optimal air traffic assignment in multi-layer transport network for urban air mobility operations,” Transportation Research Part C: Emerging Technologies, vol. 142, p. 103776, 2022.
[4] A. P. Cohen, S. A. Shaheen, and E. M. Farrar, “Urban air mobility: History, ecosystem, market potential, and challenges,” IEEE Transactions on Intelligent Transportation Systems, vol. 22, no. 9, pp. 6074–6087, 2021.
[5] S. S. Ahmed, G. Fountas, V. Lurkin, P. C. Anastasopoulos, Y. Zhang, M. Bierlaire, and F. Mannering, “The state of urban air mobility research: An assessment of challenges and opportunities,” IEEE Transactions on Intelligent Transportation Systems, 2024.
[6] A. Bauranov and J. Rakas, “Designing airspace for urban air mobility: A review of concepts and approaches,” Progress in Aerospace Sciences, vol. 125, p. 100726, 2021.
[7] W. Dai, “Conflict-free urban air mobility planning with an airspaceresource-centric approach,” Ph.D. dissertation, Nanyang Technological University, 2024.
[8] B. Pang, W. Dai, T. Ra, and K. H. Low, “A concept of airspace configuration and operational rules for uas in current airspace,” in 2020 AIAA/IEEE 39th Digital Avionics Systems Conference (DASC). IEEE, 2020, pp. 1–9.
[9] I. Bauer-H¨ansel, Q. Liu, C. J. Tessone, and G. Schwabe, “Designing a blockchain-based data market and pricing data to optimize data trading and welfare,” International Journal of Electronic Commerce, vol. 28, no. 1, pp. 3–30, 2024.
[10] L. Zavolokina, F. Spychiger, C. J. Tessone, and G. Schwabe, “Incentivizing data quality in blockchains for inter-organizational networks– learning from the digital car dossier.” ICIS, 2018.
[11] A. Ashiru and O. K. Ariff, “Rural air mobility in developing countries: Opportunities, challenges, and requirements in the use of blockchain to enhance growth,” in AIAA AVIATION FORUM AND ASCEND 2024, 2024, p. 4254.
[12] F. Panduwinata and P. Yugopuspito, “Bpmn approach in blockchain with hyperledger composer and smart contract: Reservation-based parking system,” in 2019 5th international conference on new media studies (CONMEDIA). IEEE, 2019, pp. 89–93.
[13] E. L. Thompson, Y. Xu, and P. Wei, “A framework for operational volume generation for urban air mobility strategic deconfliction,” in 2023 International Conference on Unmanned Aircraft Systems (ICUAS). IEEE, 2023, pp. 71–78.
[14] E. Androulaki, A. Barger, V. Bortnikov, C. Cachin, K. Christidis, A. De Caro, D. Enyeart, C. Ferris, G. Laventman, Y. Manevich et al., “Hyperledger fabric: a distributed operating system for permissioned blockchains,” in Proceedings of the thirteenth EuroSys conference, 2018, pp. 1–15.
[15] D. Ongaro and J. Ousterhout, “In search of an understandable consensus algorithm,” in 2014 USENIX annual technical conference (USENIX ATC 14), 2014, pp. 305–319.
[16] W. Dai, B. Pang, and K. H. Low, “Conflict-free four-dimensional path planning for urban air mobility considering airspace occupancy,” Aerospace Science and Technology, vol. 119, p. 107154, 2021.
[17] W. Dai and C. Deng, “Urban performance-based navigation (upbn): Addressing the cns variation problem in the context of uas traffic management,” in 2023 IEEE 26th International Conference on Intelligent Transportation Systems (ITSC). IEEE, 2023, pp. 5524– 5529.
[18] C. Fan, S. Ghaemi, H. Khazaei, and P. Musilek, “Performance evaluation of blockchain systems: A systematic survey,” IEEE Access, vol. 8, pp. 126 927–126 950, 2020.

> Authorized licensed use limited to: Zhejiang University. Downloaded on July 01,2026 at 06:51:58 UTC from IEEE Xplore. Restrictions apply.当前文件内容过长，豆包只阅读了前 5%。