---
title: "Digital Twin Approach for Integrated Airspace Management With Applications to Advanced Air Mobility"
source: "https://ieeexplore.ieee.org/abstract/document/10239467"
author:
  - "[[Kamesh Namuduri]]"
published:
created: 2026-07-01
description: "In the very near future, Advanced Air Mobility (AAM) services including air taxis and air ambulances are moving closer to reality. The low-altitude airspace, es"
tags:
  - "clippings"
---
## EI检索SCI升级版 计算机科学2区IF 6.6

Under a [Creative Commons License](https://creativecommons.org/licenses/by/4.0/)

## Abstract:

In the very near future, Advanced Air Mobility (AAM) services including air taxis and air ambulances are moving closer to reality. The low-altitude airspace, especially i...

---

CCBY - IEEE is not the copyright holder of this material. Please follow the instructions via https://creativecommons.org/licenses/by/4.0/ to obtain full-text articles and stipulations in the API documentation.

Most people feel very conformable catching a flight to go to places because of the trust and safety record that the aviation industry built over the years. According to the International Air Transport Association (IATA), there were five fatal accidents among 32.2 million flights in 2022 \[1\]. The trust that a common person has in commercial aviation is that the stakeholders - including the aviation industry, the Federal Aviation Administration (FAA), and the civic communities - have developed the safety standards and guidelines, and that the enforcement mechanisms are in place. As we embark on the new era of Advanced Air Mobility (AAM), it is imperative that the stakeholder communities provide at the least the same level safety assurance of air travel. This is by no means an easy task. But, as one can expect, efforts are underway from all stakeholders to provide such a safe and pleasant air travel experience. The FAA in the United States suggested a crawl-walk-run approach by proposing that in the initial stages, Advanced Air Mobility vehicles include a pilot onboard \[2\]. This cautious approach underscores the importance of safety and the need for supporting guidelines and standards before AAM becomes a reality. An important statistic to note is that human error causes approximately 80% of all aviation accidents. So, automation, if tested thoroughly, and introduced progressively, adds to aviation safety \[3\].

### A. Advanced Air Mobility National Campaign

The AAM National Campaign (NC) project was initiated by the National Aeronautics and Space Administration (NASA) <sup>1</sup> to promote uncrewed aviation services such as air taxis and air ambulances. On November 1st, 2018, NASA organized an inaugural meeting on Urban Air Mobility (UAM) Grand Challenge, later renamed as AAM National Campaign (AAM-NC),<sup>2</sup> inviting the industry in which 400 people participated. Since then, the participation grew into a large ecosystem consisting of various working groups including: 1) airspace 2) aircraft 3) community integration and 4) crosscutting. The participation grew from hundreds to thousands. The airspace working group is pursuing air traffic management at scale with safety in the airspace as a major objective. These efforts are based on the wealth of the knowledge and insights gained over the decades of commercial aviation. At the same time, under the championship of NASA, the stakeholder communities are actively engaged in the AAM-NC. The AAM-NC is providing an opportunity to conceive scenarios ranging from simple to complex, test them through simulations and conducting real-world flight tests for validating the solutions developed. In a very unique position, the author of this article, in collaboration with Keven Gambold, a retired pilot form the British Royal Air Force, has been leading the North Texas Cohort, a consortium of fifteen private, public, and government organizations, which is engaged in the AAM NC since its inception in 2019. Thus, this article sums up the research and development efforts from academics as well as from the industry perspectives.

### B. Major Contributions

This article contributes primarily to the theme of digital twin model for airspace management. It also reviews the elements that constitute the digital twin model and brings them together to present a unified view of the airspace management. It explains the need for the digital twin approach and how it helps address the most challenging issues in air traffic management at scale. It reviews the state of art to create the proposed digital twin model - air corridors, digital flight rules, and UAS to UAS communications. The major contributions of this article are described below.

1. Digital Twin Model: The concept of digital twin model for airspace management is introduced and discussed in detail in Section II.
2. Integrated Airspace Management: An overview of industry efforts on integrated airspace management is discussed in Section III. A summary of autonomous airspace operations that makeup uncrewed air transportation are also discussed in this section.
3. Digital Flight Rules: The joint efforts of NASA and FAA to develop digital flight rules are discussed in Section IV.
4. Urban/Advanced Air Mobility Corridors: An overview of UAM/AAM corridors is discussed in Section V.
5. UAS to UAS Communications: The ongoing efforts by various organizations in developing standards for UAS-to-UAS communications are discussed in detail in Section VI.

### C. Organization

This article is organized as follows: Section II outlines the central concept, the necessity and the benefits of digital twin approach for airspace management. Section III presents an integrated perspective of airspace management. Section IV presents the newly emerging concepts of digital flight and digital flight rules as defined by NASA. Section V outlines the vision of urban air corridors. Section VI explains the need for UAS-to-UAS communications with relevant use cases. Section VII concludes this article with a summary abd future perspectives.

Digital twins are digital or cyber versions of physical objects. A digital twin for airspace is a digital representation of the the airspace including all objects present in the airspace. At any given instant of time, the digital twin is a snapshot of the airspace including all aircraft systems that are currently flying, potential hazards such as bad weather, and no-fly-zones among others. With the software tools such as Airsim \[6\] and Cesium \[7\] that are available today for 3D-visualization of the airspace, it is possible to build such a digital twin model for the airspace for operators and bring it close to UAS operators, remote pilots and traffic controllers. The digital twin model for integrated airspace management presented in this article is illustrated in Fig. 1 and includes the following subsystems: 1) Integrated Airspace management, 2) Digital Flight Rules, 3) Traffic Management, 4) Air Corridor System, 5) Autonomous Airspace Operations, 6) UAS-to-UAS Communications, 7) Aircraft models, and 8) Infrastructure. These subsystems are cyber representations of physical systems. The digital twin approach brings these components together as cyber-physical components and allows them to interact and interface with one another seamlessly. This articles elaborates on the first six elements in Sections III through VI as they fall within the scope of the article. Aircraft models and infrastructure are not discussed, but, mentioned here for completeness.

[![Figure 1. - Digital Twin Model for Integrated Airspace Management.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8782711/9932544/10239467/namud1-3312277-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8782711/9932544/10239467/namud1-3312277-large.gif)

**Figure 1.**

Digital Twin Model for Integrated Airspace Management.

### A. Digital Twin for Airspace Management

Air traffic is expected to scale with the introduction of UASs into the airspace. Small and large, crewed and uncrewed aircraft are expected to share the airspace. The UAS operators, flight controllers, and remote pilots are expected to find it extremely challenging to manage such a massive scale of air traffic. A typical UAS operator will be expected to monitor multiple vehicles concurrently. Given such a complex setting, it is important that routine and repetitive tasks are automated as much as possible to minimize human errors. At the same time, the automated systems must be able to identify potential scenarios that require the attention of a human operator or a remote pilot.

Recently released AAM implementation plan termed as “Innovate28”, demonstrates the need for cautiously moving towards fully automated AAM. The crawl-walk-run approach requires a human pilot to be present in the early stages of AAM implementation \[2\]. As the levels of automation increase, the need for a platform that makes it easier for a human operator to manage the air traffic efficiently becomes critical. This is exactly the gap that a digital twin approach will be able to fill. The expected benefits of the digital twin approach are listed below and require further exploration.

#### 1) Real-Time Airspace Simulation

Digital twins create virtual replicas of the airspace, incorporating real-time data from sensors, satellite feeds, and air traffic management systems. This enables operators to visualize and monitor air traffic movements and patterns in real-time, facilitating effective decision-making for autonomous airspace management in Advanced Air Mobility (AAM). By analyzing live data, digital twins offer a comprehensive view of the airspace ecosystem, allowing operators to identify potential conflicts, assess airspace utilization, and optimize traffic flow. The ability to simulate different scenarios in real-time aids in risk assessment and helps ensure the safety and efficiency of airspace operations. Real-time airspace simulation is vital for managing the increasing number of AAM vehicles in urban airspace \[8\].

### B. Dynamic Traffic Management

Digital twins serve as dynamic traffic management systems that continuously receive live data from AAM operators, weather service, and ground-based sensors. Fig. 2 illustrates how the traffic management system (referred to as PSU) interacts with other systems and services in the AAM ecosystem. By processing this diverse and continuously updated data, digital twins optimize flight paths, altitudes, and speeds to ensure smooth traffic flow and efficient airspace utilization. This real-time optimization minimizes congestion and potential conflicts, resulting in improved safety and reduced travel times. With the capability to quickly respond to changing airspace conditions, dynamic traffic management supported by digital twins is instrumental in ensuring the seamless integration of AAM vehicles into the existing airspace ecosystem.

[![Figure 2. - AAM Ecosystem.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8782711/9932544/10239467/namud2-3312277-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8782711/9932544/10239467/namud2-3312277-large.gif)

**Figure 2.**

AAM Ecosystem.

### C. Predictive Analytics for Safety in the Airspace

Leveraging historical flight data and real-time inputs, digital twins analyze patterns and trends to predict safety risks in AAM airspace. Machine learning (ML) algorithms within the digital twin identify potential hazards, such as airspace congestion, adverse weather, or proximity conflicts, allowing for the implementation of proactive safety measures. By anticipating safety risks, operators can take preventive actions, such as rerouting aircraft or adjusting flight altitudes, to avoid potential accidents or incidents. Predictive analytics in digital twins provide an additional layer of safety assurance for autonomous airspace management, complementing the capabilities of air traffic management systems and enhancing overall airspace safety.

### D. AI-Driven Traffic Optimization

Digital twins have the potential to harness the power of artificial intelligence (AI) to optimize airspace utilization for AAM vehicles. AI-driven traffic optimization algorithms consider various factors, including weather conditions such as wind patterns, traffic congestion, and vehicle performance characteristics. By analyzing this complex data, digital twins can dynamically adjust flight paths, optimize traffic flow to minimize travel time and reduce fuel consumption.

### E. Scalability and Adaptability

Digital twin approach to airspace management allows for scalability to accommodate the increasing volume of data generated by AAM vehicles. As volume of traffic increase, digital twins can seamlessly expand their infrastructure to support the growing complexity of airspace management. Additionally, the adaptability of digital twin systems allows them to handle diverse airspace scenarios and evolving operational requirements, making them suitable for managing various types of aircraft and airspace regulations.

### F. Training and Skill Development

Digital twins offer a safe and cost-effective environment for training AAM operators and UAV traffic controllers, enabling them to practice handling complex scenarios without real-world risks. This simulation-based training enhances operators' skills and decision-making abilities, preparing them for challenging situations and emergencies. Additionally, training within digital twins enables operators to gain experience in managing diverse traffic scenarios, weather conditions, and airspace congestion, ensuring they are well-prepared for real-world airspace management challenges.

### G. Enhanced Situational Awareness

Digital twins provide a clear and intuitive visualization of the entire airspace, incorporating real-time data on aircraft, weather, no-flight zones, and other airspace hazards. This enhanced situational awareness aids decision-making in AAM, UAV Traffic Management, and Digital Flight Rules. Operators can effectively monitor air traffic p\[patterns, identify potential airspace conflicts, and respond promptly to changing conditions. By offering a comprehensive and integrated view of the airspace, digital twins help operators maintain control and awareness over complex airspace environments, thereby enhancing the safety and efficiency of airspace management operations.

### H. Testing and Validation

Digital twins serve as valuable platforms for testing and validating new algorithms, protocols, and airspace management strategies in a controlled environment. Developers can simulate various scenarios, including peak traffic periods and emergency situations, to assess system responses and identify areas for improvement. This iterative testing and validation process within the digital twin help optimize airspace management algorithms, ensuring they perform effectively in real-world conditions. By validating new technologies and procedures in digital twins, developers can gain confidence in their solutions before implementing them in actual airspace operations.

### I. Seamless Integration With IoT

Digital twins seamlessly integrate with the Internet of Things (IoT) and sensor networks, enhancing the accuracy and reliability of airspace simulations and management processes. IoT-connected devices and sensors provide real-time data updates to digital twins, enabling accurate airspace representation and airspace management. This integration facilitates efficient data exchange between connected aircraft and air traffic management systems, supporting safe and optimal operations for AAM.

Airspace is a shared resource for both crewed and uncrewed aircraft flying at different altitudes. Integrated airspace management refers to managing this shared resource and handling the conflicts that arise due to planned and unexpected situations. Digitized airspace is a snapshot of the state of airspace at a given time as shown in Fig. 3. It shows all the vehicles currently flying in the airspace including small UAS (sUAS) flying at or below 400 ft., AAM traffic flying above 400 ft and below 3000 ft, commercial aircraft flying between 18,000 ft. and 40,000 ft. It also includes all airspace hazards such as rough weather. A digital twin must include all objects at all altitudes of interest in the airspace to the operator, but, in a fully digital format and with real-time and highly accurate representation of the physical airspace as possible. While there are many visualization tools are available today for operators to monitor the airspace, they are not ready for real-time interfacing with other systems and tools. A digital twin model fills this gap - airspace management tool with the ability to integrate with other services through Application Interfaces (APIs).

[![Figure 3. - Integrated Airspace Management (Adapted from [5]).](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8782711/9932544/10239467/namud3-3312277-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8782711/9932544/10239467/namud3-3312277-large.gif)

**Figure 3.**

Integrated Airspace Management (Adapted from \[5\]).

### A. Integrating UTM and AAM

At present, there are two modalities that form the core of future air mobility: 1) UAS Traffic Management (UTM), and 2) Advanced Air Mobility (AAM). The UTM traffic refers sUAS flying under 400 ft, whereas AAM traffic refer to larger UAS flying between 400 ft to 3000 ft. The architectures of UTM and AAM have some similarities as well as differences. NASA led the UTM project \[9\] consisting of four increasing levels of technology capability from 2015 to 2019. NASA started the AAM project in late 2018 and completed its first National Campaign known as AAM NC-1 in 2022. The second phase, AAM-NC2 is about to begin sometime in the very near future in 2023.

The central component of the UTM architecture \[10\] is UAS Service Supplier (USS). Similarly, the central component of AAM architecture \[5\] is Provider of Service for UAM (PSU) (see Fig. 2). A PSU is an entity that supports operators with meeting operational requirements that enable safe, efficient, and secure use of the airspace. It is the primary service and data provider for stakeholders and the interface between the UAM ecosystem and the FAA. PSU supports operations planning, deconfliction, and airspace management functions. A USS plays a similar role in the UTM architecture. In essence, both USS and PSU serve as regional traffic management systems making sure that the UASs are flying as per the traffic rules.

### B. Autonomous Airspace Operations

Autonomy is the key to uncrewed air transportation. The UASs are capable of taking off and landing autonomously. All airspace operations are also expected to be conducted autonomously in the long run. The industry is moving in this direction progressively introducing increasing levels of autonomy in airspace operations. This subsection outlines Three key airspace operations namely flight planning, telemetry sharing, and handling no-fly zones to highlight the spectrum of complexity involved in implementing autonomous operations. The concept of operations for UTM and UAM \[5\], \[10\] include these autonomous operations. The specifics of implementation are left to the industry. No-fly zones are represented using UAS Volume Restriction (UVR) defined through ASTM standard \[11\].

In order to get a glimpse of autonomous airspace operations, let us consider a scenario in which an operator gets approval for a flight plan. Such scenarios were extensively tested through a series of sprints in AAM National Campaign \[12\] by the industry. The subsystems involved in this particular scenario are: 1) PSU, 2) Discovery Synchronization Service (DSS), and 3) Flight Information Management System (FIMS). While FIMS and DSS were managed by NASA during the AAM NC, in the long run all subsystems are expected to be managed by the industry through some form of cooperation. This is a significant change for uncrewed air transportation compared to crewed air transportation which is managed by the Federal Aviation administration (FAA) or its equivalent.

- Operator plans a mission, referred to as Operational Intent (OI).
- Operator submits plan to its supporting PSU.
- PSU shares it with appropriate op data to DSS, discovering other PSUs.
- PSU checks the OI against services such as weather and vertiport management.
- PSU shares the OI with other PSUs.
- FIMS manages the authentication services.

The above sequence is just a small subset of operations before the flight takes off, shown here as a sample. After the OI is approved, the operator begins the flight operation. The flight takes off along the predefined route sharing the Telemetry data periodically with the PSU (or other designated entity). Fine details are omitted in the above sequence for the purpose of clarity. The scenario, in its simplest form, exemplifies the challenges involved in completely automating airspace operations.

Imagine that a sudden weather development takes place while the UAS is enroute its destination. Such developments can happen at anytime and any number of times during a flight. Events such as weather development are handled the same as no-fly zones. The volume of airspace that surrounds rough weather is described in the same format as UVRs. This allows the flight to be rerouted around the UVR. The new route that avoids a UVR is defined by the human operator who designed the original route. However, in the long run, generation of the new route can be automated. In either case, the new route needs to go through the sequence of steps discussed above.

NASA defines Digital Flight as an operating mode in which flight operations are conducted by reference to digital information, with the operator ensuring flight-path safety through cooperative practices and self-separation enabled by connected digital technologies and automated information exchange \[13\], \[14\].

NASA also defines Digital Fight Rules as a set of regulations authorizing sustained Digital Flight as an alternative means of separation in Visual Meteorological Conditions (VMC) and Instrumental Meteorological Conditions (IMC) in lieu of employing visual procedures (i.e., Visual Flight Rules or VFR) or receiving Air Traffic Control separation services (i.e., Instrument Flight Rules or IFR) \[13\], \[14\].

Digital flight rules will lay the foundation for autonomy as well as safety of airspace operations. NASA is working through Radio Technical Committee for Aeronautics (RTCA) to develop the digital flight rules. Airspace operations are human-centric and managed through interaction with air traffic control operators on the ground. For uncrewed air transportation at scale, this becomes a limitation. Digital flight rules driven by integrated data, machine-learning, and artificial intelligence provide a means to enhanced automation, efficiency, and safety.

Today, airspace operations are conducted with VFR and IFR. With VFR, the pilot primarily controls and navigates the aircraft using outside visual references. With IFR, the aircraft is flown using only the instruments with no visual references to the outside world. In crewed transportation both IFR and VFR flights rely on human decision-making. Digital flight rules are expected to remove this dependency on human operator and increase the level of autonomy of airspace operations. Although the need is identified, it is a long journey from where the industry is today to reach the point when a flight is fully operated using digital flight rules. In crewed aviation, the pilot is responsible even when flying with IFR, because VFR flights may be present in the vicinity of IFR flights.

An example of digital flight rules is the horizontal and vertical separation between two aircraft. Assume that two UASs are flying at the same altitude maintaining minimum safety distance as shown in Fig. 4. If the first UAS slows down for any reason, the following UAS will be forced to slow down automatically in order to maintain the minimum safety distance. Another example is negotiation for a right of way at an intersection. This use case scenario will be discussed in the context of collision avoidance in Section VI. Digital rules require automatic enforcement methods. For example, the lateral separation rule discussed above can be implemented through sensing, computing, and communication infrastructure. Section VI highlights UAS-to-UAS communications as a means of implementing airborne separation.

[![Figure 4. - Digital flight rules for enhanced autonomy and safety in the airspace.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8782711/9932544/10239467/namud4-3312277-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8782711/9932544/10239467/namud4-3312277-large.gif)

**Figure 4.**

Digital flight rules for enhanced autonomy and safety in the airspace.

Air corridors are three-dimensional (3D) volumes of airspace reserved for UASs for Advanced Air Mobility (AAM) traffic \[15\], \[16\]. They are structured airspaces for facilitating smooth flow of traffic. Air corridor designs are specific to each country and are defined by the respective federal aviation organizations. In the United States, the Federal Aviation Administration (FAA) defines air corridors in class B, C, or D airspace \[17\]. The FAA also defines the expected performance requirements of a UAS flying in an air corridor. Fig. 5 illustrates a possible design of an air corridor with three layers. Note that, this design is created for visualization purposes by the author and is not approved or standardized by any authority. In this design, the top and bottom layers contain one directional tracks or skylanes. The middle layer contains intersections (roundabouts) for the AAM aircraft to change the direction of travel. For example, if a Southbound UAS needs to turn East, it will lower down from Layer 1 to Layer 2, takes a quarter turn in the roundabout, climbs down to Layer 3, merges into the Eastbound skylane, and continues its travel. The design of such air corridors, traffic rules in the air corridors, safety requirements, and performance specifications are still evolving. Airspace design concepts, such as the geofense \[18\], are currently being considered by various research groups. Irrespective of the air corridor design, there is a need for finding a substitute for traffic lights in air corridors. The most obvious choice for this substitution is UAS-to-UAS communications.

[![Figure 5. - Illustration of an air corridor (Courtesy, Unmanned Experts).](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8782711/9932544/10239467/namud5-3312277-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8782711/9932544/10239467/namud5-3312277-large.gif)

**Figure 5.**

Illustration of an air corridor (Courtesy, Unmanned Experts).

In real-world air corridors are not as elegant as in Fig. 5. Instead, the regions are carefully designed based on the existing commercial traffic. Fig. 6 shows airspace identified for UAM flights at different altitudes around the Dallas Fort Worth area, that is separated (about 95% of the time) from legacy traffic \[19\].

[![Figure 6. - Air corridors in Dallas-Fort Worth Metroplex (Courtesy NASA [19]).](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8782711/9932544/10239467/namud6-3312277-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8782711/9932544/10239467/namud6-3312277-large.gif)

**Figure 6.**

Air corridors in Dallas-Fort Worth Metroplex (Courtesy NASA \[19\]).

This section begins with five use case scenarios to highlight the need for UAS-to-UAS communications. These scenarios are based on the suggestions that came from a meeting organized by the RTCA in September 2022. The five use cases support the airspace operations as illustrated in Fig. 7 in the AAM ecosystem. In particular, these five use cases illustrate the need for UAS-to-UAS communications. Note that these use cases are for AAM. Working group members are free to choose any use case scenarios that are not related AAM.

[![Figure 7. - UAS-to-UAS Communication needs in the AAM ecosystem (Source: NASA, RTCA).](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8782711/9932544/10239467/namud7-3312277-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8782711/9932544/10239467/namud7-3312277-large.gif)

**Figure 7.**

UAS-to-UAS Communication needs in the AAM ecosystem (Source: NASA, RTCA).

*a) Collision Avoidance:* Two or more UASs are approaching a region at the same time and they need to avoid a potential collision. There can be many variations to this scenario. For example, the vehicles can be cooperative or non-cooperative. The airspace can be structured or unstructured. Structured airspaces are defined and reserved for certain types of vehicles and typically applicable for urban areas. Unstructured airspaces are typical for rural regions.

*b) Merging and Spacing/Sequencing of Traffic:* This use case refers to traffic in structured airspaces, i.e., air corridors. An air corridor is a highway system in the airspace. Air corridors are reserved airspaces at altitudes ranging from 150 meters to 1 km Above Ground Level (AGL). Imagine an intersection such as a roundabout illustrated in Fig. 5. Merging occurs when a UAS is trying to enter the roundabout.

*c) Airborne Separation:* This scenario refers to the need for maintaining a safe distance between any pair of UASs during flight. Two situations arise depending on whether UASs are flying in structured or unstructured airspace. The former case is illustrated in in Fig. 8. Here if the UAS in front decelerates, the vehicle behind it needs to decelerate as well in order to maintain a safe distance between the two. In the later case, each UAS assumes a geofence \[18\] around it in order to maintain a safe distance from other UASs.

[![Figure 8. - Illustration of airborne separation in a skylane (Courtesy, Unmanned Experts, Inc.).](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8782711/9932544/10239467/namud8-3312277-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8782711/9932544/10239467/namud8-3312277-large.gif)

**Figure 8.**

Illustration of airborne separation in a skylane (Courtesy, Unmanned Experts, Inc.).

*d) Airborne Rerouting:* Rerouting of a UAS may be needed when the planned or current route is not navigable due to airspace space hazards such as the one shown in the Fig. 8. Typically, the new route is shared with the UAS by the remote operator (pilot) on the ground or by the Ground Control Station (GCS) if the UAS is within the communication range of the operator or GCS. If the UAS is Beyond the Radio Line-of-Sight (BRLOS), the rerouting information may be relayed by one or more UASs. Rerouting may also be required when a vertiport where a UAS planned to land becomes unavailable. In this case, the UAS needs to to change its destination to another available vertiport that is close by. These scenarios also emphasize the need for a multi-hop connections or UAS network for sharing mission critical information in real-time.

*e) Cooperative Sensing of Weather/winds:* Sudden weather development during a flight might require a UAS to reroute its planned flight path as in the previous scenario. In extreme weather conditions a UAS may need to land in a nearby location or return home immediately. In such situations, the weather information and the message indicating immediate landing needs to be delivered to the UAS.

This article presented a digital twin approach for integrated airspace management which includes six subsystems: digitized airspaces, digital flight rules, integrated airspace management, autonomous airspace operations, air corridors, and UAS to UAS communications. These six areas are emerging research and development topics. Hence, challenges will arise as these technologies evolve. Throughout the world, partnerships or cohorts are being established among academic, public, private, and government organizations are being established to address such challenges. The author is leading one such cohort in collaboration with fifteen organizations in the North Texas region. This North Texas cohort demonstrated its first flight test in an air corridor in the North Texas region that stretched about 30 miles from Fort Worth to Denton on October 11, 2022. A set of autonomous airspace operations discussed in Section III were evaluated during this demonstration. Experiences gained and lessons learned from such demonstrations will help build safer air corridors in our local and regional communities.