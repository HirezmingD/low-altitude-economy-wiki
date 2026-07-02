---
title: "Urban air mobility in the built environment: A review of aerodynamic interactions, thermal effects, and simulation challenges"
source: "https://www.sciencedirect.com/science/article/pii/S2210670725007267?pes=vor&utm_source=clarivate&getft_integrator=clarivate"
author:
  - "[[Haidong Wang]]"
published:
created: 2026-07-01
description: "Urban Air Mobility (UAM) is poised to transform urban transportation, yet its integration into dense metropolis introduces significant aerodynamic and…"
tags:
  - "clippings"
---
## Urban air mobility in the built environment: A review of aerodynamic interactions, thermal effects, and simulation challenges EI检索SCI升级版 工程技术1区SCI Q1IF 13.3

[https://doi.org/10.1016/j.scs.2025.106853](https://doi.org/10.1016/j.scs.2025.106853 "Persistent link using digital object identifier")

Full text access

## Highlights

- •
	Comprehensive review of studies on urban air mobility in the built environment.
- •
	Urban environmental factors and methodological aspects systematically analyzed.
- •
	Quantitative research on localized turbulence coupling remains insufficient.
- •
	Dynamic threshold systems needed for eVTOLs in complex urban wind environments.

- [Next article in issue](https://www.sciencedirect.com/science/article/pii/S2210670725007231)

## Keywords

Urban air mobility

Low-altitude wind field

Urban thermal environment

Turbulence coupling

Flight safety

## 1\. Introduction

### 1.1. Background and motivation

The rapid advancement of urbanization compelled urban transportation to transition from a two-dimensional to a three-dimensional framework (). Numerous regions, including China and United States, are now promoting the innovative developments in technologies such as drones and aerial vehicles (). UAM has emerged as a promising concept, utilizing Unmanned Aerial Vehicle (UAV) or electric Vertical Take-Off and Landing (eVTOL) vehicles to provide short-distance aerial transportation (;;;; ), as shown in. Such systems have the potential to alleviate congestion issues and significantly reduce reliance on ground-based traffic. Unlike traditional urban aircraft (such as helicopters), drones and eVTOLs operate at low altitudes below 1 km, maintaining closer proximity to urban buildings.

![Fig 1](https://ars.els-cdn.com/content/image/1-s2.0-S2210670725007267-gr1.jpg)

Download: Download high-res image (610KB)

With the growing prominence of UAM, eVTOL technology has become a critical enabler for connecting urban areas. As shown in, United Airlines in the U.S. plans to launch its first eVTOL passenger route in 2025, reducing travel time from 1 h to just 10 min. Similarly, Honda unveiled an eVTOL concept at the Tokyo Motor Show, promising safer and quieter urban transportation. Recently, China has deployed manned low-altitude aircraft, underscoring global efforts to initiatives to integrate aerial vehicles into urban areas. The development of UAM aims to address key urban transportation challenges, such as traffic congestion, travel delays, and environmental concerns. However, the integration of UAM systems into complex urban environments introduces challenges related to wind flow dynamics and thermal effects (). Therefore, understanding the interaction between urban environmental factors and UAM operations is essential for achieving safe, efficient, and sustainable deployment.

![Fig 2](https://ars.els-cdn.com/content/image/1-s2.0-S2210670725007267-gr2.jpg)

Download: Download high-res image (505KB)

Existing research predominantly examines UAM from the perspective of aerial vehicles and urban transportations (;; ). Bayomi et al. () offered the diverse applications of drone technologies in the built environment and their role in climate change research. critically examines various wind flow estimation and forecasting techniques utilized within the UAM domain. They provide a comparative analysis of widely adopted wind flow models in wind engineering and atmospheric sciences, alongside an overview of urban wind flow conditions. Recently, has comprehensively reviewed the latest advancements in UAM airspace design and risk assessment. They emphasize key concepts (such as airspace categorization and geofencing) and primary organizational strategies, along with their benefits, limitations, and applications.

Despite the growing interest in UAM, research on its integration and interactions with complex urban airflow structures remains limited. A comprehensive understanding of these challenging flow phenomena is essential for the safe and efficient deployment of UAM systems. This review adopts a novel perspective by systematically examining the interplay between urban environmental conditions—including wind and thermal effects—and UAM performance. By highlighting the importance of these interactions, the paper aims to point out critical research gaps and support the development of effective, safe, and scalable UAM solutions for complex urban environments.

### 1.2. Objectives of the review

The primary objective of this literature review is to systematically analyze and synthesize current research on the interaction between UAM systems and urban environmental conditions. This review is supported by a comprehensive survey of over 150 publications (see ). Specifically, this review aims to:
- 1\. Identify key urban environmental factors. This paper intends to examine how urban wind patterns, heat islands, and atmospheric dynamics impact UAM performance, particularly in terms of stability, energy efficiency, and safety.
- 2\. Highlight technological challenges. This study will assess limitations related to vehicle performance, and climate resilience across diverse urban conditions.
- 3\. Point out existing research gaps and propose future directions. This paper intends to synthesize findings to reveal gaps in the literature and suggest priorities for future investigations.

![Fig 3](https://ars.els-cdn.com/content/image/1-s2.0-S2210670725007267-gr3.jpg)

Download: Download high-res image (1MB)

By addressing these objectives, this review provides an integrated perspective on the challenges and opportunities of UAM deployment in urban environments, clarifies current research limitations, and provides insights to guide researchers, policymakers, and industries toward sustainable and safe UAM solutions.

### 1.3. Structure of the paper

This paper systematically reviews the interplay between UAM and urban environments. It first introduces the background, motivation, and objectives, then details how urban wind complexity and thermal effects—including urban heat island phenomena—impact UAM operations. The review assesses how turbulent winds and thermal variations influence the safety and stability of UAM aircraft, particularly during critical phases such as takeoff, landing, and hovering. Methodological approaches for investigating these challenges are summarized, including computational simulations, experimental techniques, and field measurements. Finally, the paper discusses advances in urban airflow prediction and concludes with key findings and recommendations for future research to enable the safe and effective integration of UAM in cities.

The term “UAV” is often broadly applied in the literature to encompass various aerial platforms. While traditional UAVs are primarily used for surveillance, mapping, and delivery, eVTOL aircraft are specifically designed for urban air mobility (UAM), with a focus on passenger transport, elevated safety requirements, and integration with urban infrastructure. This review centers on eVTOL operations but uses the term “UAV” where it aligns with cited sources.

## 2\. Urban atmospheric conditions and constraints for UAM operations

### 2.1. Wind speed and turbulence thresholds

Wind speed and turbulence thresholds are critical parameters for the safety and stability of UAM. Vertical wind shear, often resulting from abrupt changes in wind speed and turbulence intensity in urban areas, poses a substantial risk to UAM, particularly during takeoff and landing (). Evans et al. () analyzed 990 aviation accidents documented by the U.S. National Transportation Safety Board (NTSB) from 1987 to 2011 and found that 24.2 % (240 accidents) were caused by low-altitude wind shear, turbulence, or microbursts, making this the leading atmospheric hazard, especially during landing or takeoff. compiled turbulence requirements for heliports near buildings, noting limited research on this topic (; ). Existing guidelines offer recommendations for the design and siting of vertical takeoff and landing (VTOL) infrastructure (). advocated using turbulence energy as a more effective indicator than vertical velocity standard deviation. However, these standards are largely based on offshore helicopter operations and lack specific thresholds for urban VTOL facilities. As a result, turbulence criteria for VTOL airports require further investigation and definition.

In the cruising phase, showed that as UAV speed increases, the influence of gusts on the rotors diminishes due to the greater role of thrust in maintaining flight. However, found that the Volocopter multirotor (equipped with eighteen electric rotors) had an average wind speed limit of 8.6 m/s and a gust limit of 13.74 m/s, indicating that strong winds still pose significant risks at higher speeds. Su et al. () defined wind shear as a horizontal variation over 15 m/s or vertical change over 2.5 m/s. However, precise threshold values should be determined based on specific UAV wind resistance. Therefore, achieving stable flight across varying wind conditions remains a key challenge for UAM.

In urban environments, wind speed and turbulence are strongly affected by building geometry. Basawanal et al. () found that urban wind speed varies significantly with height, with fluctuations up to 5 m/s. The Venturi effect can cause wind speeds to double in narrow streets. According to the definition, severe wind shear is identified when a rapid change in wind results in an aircraft airspeed variation exceeding 15 knots (approximately 7.7 m/s) or a vertical speed variation exceeding 500 feet per minute (approximately 2.54 m/s) (). observed that wind speed increases by approximately 50 % near building edges, requiring UAVs in these areas to possess robust control capabilities to cope with rapid airflow changes. Higher wind speeds are often accompanied by increased turbulence intensity. reported that as wind speed increased from 1.9 m/s to 14.9 m/s in a high-wind generator experiment, turbulence intensity rose from 4.2 % to 6.1 %. conducted field measurements in the outdoor atmospheric environment in Gothenburg, Sweden, and also noted that turbulence intensity is related to wind speed, with both relative and absolute turbulence intensity varying with wind speed. However, they also pointed out that due to strong shear layers near the canyon top, turbulence intensity may not increase monotonically. This indicates that the monotonic increase of turbulence intensity with wind speed is highly dependent on the specific application scenario. used UAV-based observations to show that turbulence kinetic energy dissipation rates—and thus turbulence intensity—are significantly higher below 50 m altitude than at higher elevations. These variations can undermine flight stability, particularly for low-altitude operations. Therefore, for eVTOLs operating in urban environments, especially near buildings or within confined spaces, accounting for the risks posed by wind speed and turbulence is essential. Notably, although turbulence intensity generally decreases with altitude, it remains a critical consideration for safe low-altitude eVTOL flight. There remains a marked gap in research systematically assessing low-altitude turbulence risks for eVTOLs, underscoring the need for further targeted and interdisciplinary studies.

### 2.2. Non-compliant wind patterns

Modern cities, characterized by intricate street networks and irregularly shaped buildings, generate highly complex wind patterns (; ). Notably, street canyon effects and wake vortices present significant challenges to the safety and stability of low-altitude aircraft.

The morphology and layout of street canyons strongly influence the local microclimate. When the width-to-height ratio is large or the street configuration is complex, rotational turbulent vortices commonly form within the canyon (). attributed these irregular wind fields to the obstruction and guiding effects of airflow by buildings, leading to complex recirculation and vortex motions in the street canyon. further demonstrated that, with an aspect ratio of 1 and perpendicular inflow, a primary vortex forms in the canyon, accompanied by three secondary vortices at the corners. Changes in aspect ratio or increased layout irregularity, due to variations in building height or street width, significantly alter the distribution and intensity of these vortices. Such changes can induce large fluctuations in local wind speed and direction, or create strong wind zones, thereby posing substantial risks to low-altitude flight safety in urban areas.

In addition to street canyon effects, wake vortices critically impact the flight safety of low-altitude aircraft. Wake vortices—rotational airflows generated behind buildings or aircraft—can significantly enhance turbulent kinetic energy (TKE) and vertical mixing. examined wake vortices in Gothenburg street canyons and found that when wind is perpendicular to the canyon axis, a single helical vortex forms within the canyon, while pronounced wake vortices develop behind buildings. These structures greatly increase local turbulence intensity, with values near buildings far exceeding those predicted for the inertial sublayer; the ratio of the standard deviation of vertical wind speed to friction velocity can reach 2. Such vortices disrupt flight stability for following aircraft.

With the rapid development of the low-altitude economy, future urban skies may see dense UAM operations. In this context, wake vortices generated by multiple aircraft could interact, creating highly complex and potentially hazardous airflow conditions. However, research on low-altitude flight and aircraft-induced wake interactions in urban environments remains limited, highlighting the need for further investigation. Advancing interdisciplinary research in this area is crucial for optimizing flight routes and enhancing safety in urban airspace.

### 2.3. Urban thermal stability factors

The urban thermal environment has been extensively examined, with existing studies primarily addressing phenomena such as thermal stratification and the urban heat island effect, and their impacts on pollutant dispersion and pedestrian-level thermal comfort. However, aspects relevant to low—altitude flight-particularly rooftop surfaces, underlying surface conditions along flight corridors, and high-altitude thermal circulation—remain insufficiently investigated. Drawing on established knowledge of urban meteorology and the operational characteristics of low-altitude flight, we hypothesize that these factors may significantly influence the safety and stability of urban aerial vehicles. Research in aeronautics has predominantly focused on the thermal management systems of the aircraft itself (), with comparatively little attention to the additional thermal buoyancy and convective flows encountered during operations within urban environments. Notably, under the influence of the urban heat island effect, thermal buoyancy can alter the low-altitude airflow structure, thereby potentially affecting flight performance and flight stability.

The UHI effect arises from the absorption and re-radiation of solar energy by urban infrastructure, resulting in elevated surface and air temperatures compared to rural areas and leading to thermal stratification within the urban boundary layer (). Empirical studies have quantified these effects, found that a 0.1 decrease in the Sky Visibility Factor (SVF) corresponded to a 10 W/m² increase in longwave radiation and a 1.6 K rise in mean radiant temperature. observed that a 10 % increase in SVF resulted in an 8 % increase in pedestrian sidewalk wind speed, highlighting the interplay between urban morphology, thermal conditions, and airflow. This phenomenon causes higher surface and air temperatures compared to rural areas, leading to thermal stratification within the urban boundary layer (). Additionally, anthropogenic heat sources, such as industrial activities and vehicle emissions, further contribute to the urban heat load ().

Despite these findings, significant gaps remain regarding the coupling between urban thermal stability and the safe operation of eVTOLs. A more comprehensive understanding of urban thermal effects is essential to improve the safety and operational reliability of low-altitude aircraft.

### 2.4. Section summary

This section systematically examines the wind environment requirements for UAM operations, with a focus on the complex interactions between natural airflow and urban infrastructure and their implications for flight safety. Wind speed and turbulence thresholds are critical for maintaining UAM flight stability, and the influence of vertical wind shear and turbulence must be rigorously assessed during takeoff, landing, and cruising. In addition, the urban heat effects further complicate the airflow environment, imposing greater demands on the stability of low-altitude flight. Irregular wind phenomena—such as the canyon effect and wake vortices—pose significant risks to UAM operations, underscoring the need for advanced modeling techniques to predict and mitigate these uncertainties. Accordingly, comprehensive risk assessment throughout eVTOL flight phases is essential. Future research should prioritize the enhancement of flight safety and flight stability to support the reliable and efficient deployment of UAM in urban environments.

## 3\. Impact of urban environmental parameters on UAM safety

### 3.1. Key environmental factors

UAM operations require highly stable wind conditions, yet modern urban environments generate complex and irregular wind patterns, such as canyon-induced vortices and building wake turbulence, that pose substantial risks to the stability and safety of eVTOL, particularly during takeoff and landing. The interaction between natural wind flows and urban structures may pose unique aerodynamic challenges for UAM flight safety. While previous research has extensively examined urban airflow in the contexts of ventilation (;;; ), pedestrian comfort (), structural wind loads (), and pollutant dispersion (;;; ), the specific implications of these complex wind environments for UAM operations remain underexplored. This section therefore focuses on how urban morphology shapes wind complexity and discusses its consequences for the safe and scalable deployment of UAM systems in real-world cities.

#### 3.1.1. Wind complexity from built structures

Urban airflow is profoundly influenced by building layout, including height, shape, and urban configuration () (;;; ). These elements contribute to the development of complex turbulence, vortices, and wind speed gradients in high-density urban environments (; ), as shown in (c) (). Localized spatial variations directly influence the wind corridor effect and ventilation efficiency (;;; ), thereby impacting urban air circulation and exerting a considerable effect on the local microclimate, as depicted in (d) (). Such aerodynamic variability modify the aerodynamic forces acting on low-altitude eVTOLs and introduce unexpected instabilities during takeoff, landing, and hovering processes (). Therefore, systematic studies of building layout effects on urban airflow are crucial to improving the operational safety and adaptability of eVTOLs in cities.

![Fig 4](https://ars.els-cdn.com/content/image/1-s2.0-S2210670725007267-gr4.jpg)

Download: Download high-res image (1MB)

##### 3.1.1.1. Building height

Building height is a key factor shaping urban wind environments, affecting airflow patterns (), wind speed distribution, and turbulence intensity (see (a) ()) across scales from the urban canopy layer to the microscale. found that greater building height variability ($\sigma_{H}$) intensifies wind-driven airflow: as $\sigma_{H}$ increases, the air exchange rate first rises then falls, while circulation in step canyons weakens under heating. Similarly, showed that a central building twice as tall as its surroundings (2H) produces a strong blockage effect, increasing flow complexity and expanding recirculation zones, especially under stable atmospheric conditions. Building-induced airflow disruptions also affect near-wall microclimates. found vertical velocities along facades increase with height before stabilizing or decreasing near the top, while lateral surfaces exhibit greater variation—winter side winds can exceed double those at central locations. noted upstream tall buildings split airflow at roof edges, forming vortices that expand with building density. observed enhanced velocity fluctuations atop and behind high-rises, with standard deviations up to 3.8 times inflow velocity due to recirculation and wake effects. reported free-flowing air hitting first-row tall buildings generates high streamwise velocity, wakes, and low-pressure zones. These aerodynamic instabilities, especially on leeward sides, challenge low-altitude flight.

High-rise rooftops are vulnerable to vortex-induced loads (). found wind speeds peak at corners and rooflines, recommending sensitive operations be located away from corners. Furthermore, rooftop pads for eVTOLs should maximize usable area and avoid corners. Orienting city blocks at an angle to the prevailing wind, rather than perpendicular, can also promote smoother airflow and create safer operational zones.

Although roof-edge vortices induce local instability, they maintain overall flow coherence. On leeward sides, vortices tilt toward lower structures, forming recirculation zones among low-rise buildings. Local flows around low-rise buildings couple less with large-scale canyon flows (), resulting in a more stable environment. Compared to high-rise rooftops, low-rise rooftops may be more suitable for eVTOL vertical takeoff and landing due to lower exposure to strong vortices and high winds.

##### 3.1.1.2. Building shape

Urban areas feature buildings with diverse shapes and external designs, which significantly influence local airflow and pose challenges for the stability of low-altitude aircraft operations (). Keshavarzian et al. () compared airflow around isolated buildings with square, chamfered, curved, and circular cross-sections. While windward airflow remains relatively consistent, leeward flow characteristics differ markedly; recirculation zones are larger behind square and chamfered buildings, mainly due to differences in downwash intensity, bifurcation point location, and the formation of separation-reattachment bubbles near the sides. These observations echo findings regarding building height but highlight the amplifying effect of building shape, particularly corner design, on urban airflow (). Furthermore, chamfered, curved, and circular designs also diminish vortex strength along building sides (). To enhance aircraft safety near buildings, further research is needed to determine minimum safe flight distances for various building shapes (; ), especially given the current limited understanding of how vortices generated by fundamental geometries impact aircraft performance.

##### 3.1.1.3. Urban layout

Regular and irregular urban layouts markedly influence urban wind environments (). In a regular layout, airflow tends to be more stable (). In contrast, irregular layouts, characterized by diverse horizontal building arrangements, increase airflow deflection and turbulence (). highlighted that both the prevailing wind direction and building array configuration significantly affect airflow patterns in central and peripheral urban spaces. Additionally, observed that gaps or open corridors between buildings can amplify wind speeds by 2.5 to 3 times compared to open-field conditions. These findings underscore the critical role of urban layout in shaping airflow, which is particularly important for the navigation and safety of aircraft in complex cityscapes.

Irregular vertical building arrangements further complicate airflow relative to areas with uniform building heights (). Sun et al. () observed that, hilly cities exhibit sharply increased TKE on windward hilltops, and sub-canopy ventilation rates can be two to three times higher than those in flat areas. Moreover, demonstrated that vertical forests alter flow patterns and reduce mean wind speeds and turbulence within canyons, suggesting that integrating vertical greenery can improve local wind environments for UAM operations. Despite these insights, current research remains insufficient to establish a robust theoretical basis for safe eVTOL operation in diverse urban settings, highlighting the need for more comprehensive studies.

#### 3.1.2. Thermal effects on airflow

##### 3.1.2.1. Local thermal effects on urban airflow

Local thermal conditions may influence eVTOL performance during takeoff, hovering, and low-altitude navigation. Variations in surface heat flux—arising from materials such as asphalt, concrete, and vegetation—create temperature gradients, thermal plumes, and turbulence that can destabilize aircraft, especially near the ground (;; ). Simulations indicate that surface heat dissipation shapes urban microclimates in ways that vary by surface type (). Using the Richardson number, found that intensified bottom-heating in non-uniform street canyons alters vertical velocity patterns; within −15.68 < Ri < −7.84, thermal buoyancy becomes the dominant driver of airflow, potentially amplifying vertical gusts hazardous to eVTOL control.

Urban greenery mitigates these thermal disturbances and thus contributes to safer low-altitude flight operations.

Horizontal green spaces, such as parks and roadside vegetation, contribute to improved urban microclimates by lowering surface and near-ground air temperatures. This cooling effect reduces the intensity and frequency of thermal plumes and buoyancy-driven turbulence, thereby stabilizing the airflow near the ground (;; ). As a result, abrupt wind fluctuations and localized thermal instabilities—both of which can destabilize low-altitude aerial vehicles—are mitigated. These more stable aerodynamic conditions are expected to enhance the safety and control of flight operations in the vicinity of urban green areas.

The extent of these benefits depends on canopy size, leaf area density, and spatial distribution, all of which influence local airflow and temperature (; ). However, the impact of horizontal greenery diminishes with altitude and is minimal above tall buildings, limiting its protective effect for higher-altitude operations.

Vertical greening—including green walls (), vertical gardens (;; ), and rooftop vegetation (; ) —provides additional shading and surface cooling, lowering temperatures by up to 18 °C in summer (). This reduces heat-induced turbulence near rooftops and contributes to more stable airflow in critical zones such as takeoff and landing areas.

Buildings themselves also interact with thermal effects. Elevated ambient temperatures around structures can alter vortex behavior and wind direction, particularly in leeward zones (), creating unpredictable flow patterns that challenge flight control. The influence of vegetation type, density, and spatial distribution on these effects is altitude-dependent. Despite existing insights, empirical data directly linking local thermal environments to eVTOL safety remains scarce, underscoring the need for targeted studies.

##### 3.1.2.2. UHI on urban airflow

At the urban scale, the UHI effect alters airflow patterns, reduces air density, and decreases aerodynamic lift (;; ). Based on these findings, we infer that such environmental changes could increase the operational complexity of eVTOL flights. Vertical wind speed gradients can vary by up to 0.8 m/s in winter and 0.4 m/s in summer over a 90 m height range (), influencing takeoff and rooftop operations. The interaction between UHI-induced warming, urban morphology, and seasonal temperature variations intensifies turbulence, particularly in dense city centers, as illustrated in ().

![Fig 5](https://ars.els-cdn.com/content/image/1-s2.0-S2210670725007267-gr5.jpg)

Download: Download high-res image (654KB)

Urban form strongly influences UHI intensity. found that high-density, high-rise developments exacerbate UHI and require greater wind speeds for mitigation—conditions that may not always be present. Field measurements in Beijing () showed that dispersed urban sub-centers weaken UHI intensity, while monocentric layouts increase it by up to 23.5 %. These differences are critical for planning safe aerial corridors, as heat flux distribution and wind speed in high-density zones can drive thermal updrafts that alter flight stability. Higher building density consistently amplifies UHI regardless of urban form (; ), meaning eVTOL routes between sub-centers may face variable turbulence depending on spacing, density, and surface materials.

Thermally driven vertical flows are a major operational hazard. ) reported that buoyancy- and turbulence-induced circulation in UHI cores often produces vertical velocities exceeding those of background urban plumes, extending turbulent influence to the inversion layer (). Nocturnal radiative inversions can lower stability near 50–100 m rooftops (), while UHI can raise the inversion height to 100–600 m, affecting super-tall structures (). Smaller vortices from thermal stratification () can increase rooftop temperatures and turbulence—yet the influence of rooftop plumes on eVTOL safety remains largely unstudied.

For cross-city navigation, UHI-driven “heat dome” flows can horizontally extend 45–120 km from urban cores, with travel times of 1–6 h across city edges (, ). Interactions between multiple UHI circulations depend on city spacing and layout, which can either create smoother transitional flows or generate turbulence zones (). City geometry further shapes horizontal heat transport: circular cities tend to form axisymmetric flows, whereas square cities produce uneven patterns with stronger diagonal heat transfer (, ), potentially increasing instability along certain routes. While Coriolis forces can influence airflow at large scales or high latitudes (; ), they are negligible for eVTOLs in the lower urban atmosphere.

### 3.2. Stage-specific risk analysis

#### 3.2.1. Take-off and landing

The takeoff, landing, and hovering phases are critical for UAV safety, as they are highly sensitive to turbulence and disturbances in the urban microenvironment. During takeoff, ground effects and surrounding obstacles significantly alter aerodynamic characteristics by generating complex airflow patterns and turbulence (), as illustrated in (a) and (b). Small-scale airflow variations and wind shear caused by urban structures are pivotal to UAV operational safety (). CFD simulations reveal that interactions between flow dynamics and moment parameters near the ground or walls increase turbulence intensity and alter relative velocity. For example, a wind speed difference exceeding 4 m/s within 10 m of the ground can raise landing failure rates by 18 % (), and the canyon effect in narrow streets may double wind speeds (). Wind speed near building edges can abruptly rise by 50 % (), significantly increasing the risk of vertical wind shear, as illustrated in (c) and (d). These near-ground flow phenomena underscore the need for robust aerodynamic regulation strategies to ensure stability. Additionally, the urban heat island (UHI) effect and urban ventilation can induce substantial fluctuations in wind speed and turbulence during these phases (), further elevating safety risks.

![Fig 6](https://ars.els-cdn.com/content/image/1-s2.0-S2210670725007267-gr6.jpg)

Download: Download high-res image (641KB)

During hovering, UAV stability and aerodynamic performance are mainly affected by lateral airflow. The integration of attitude control and decision support systems in hexacopter UAVs has improved reliability, with flight tests showing a maximum altitude deviation of <1 m (). Nevertheless, lateral airflow continues to impact thrust and power consumption, making it a crucial factor for hovering efficiency and stability ().

Urban turbulence intensities exceeding 40 % necessitate careful mission planning to avoid high-turbulence zones, especially near architectural corners, which create steep wind shear gradients (). Crosswind conditions have been shown to breach containment boundaries at side winds of 50 km/h, indicating significant safety concerns (). Aviation safety standards designed for commercial aircraft exhibit limited applicability to UAVs due to threshold hysteresis and operational differences (). For eVTOL vertiports, operations are permitted below 17 knots (8.7 m/s), with shutdown required above 25 knots (12.9 m/s) ().

Collectively, urban turbulence profoundly affects UAV safety and stability during critical flight phases. However, the interaction between ambient wind and rotor-induced downwash remains inadequately understood, highlighting the need for further research to enhance eVTOL safety and performance in urban environments.

#### 3.2.2. Cruise phase

The urban wind field and turbulence are critical factors influencing the stability and safety of UAM operations, particularly during the cruise phase. As illustrated in, the wind environment can be categorized into atmospheric, urban, and microscale levels based on spatial scale ().

![Fig 7](https://ars.els-cdn.com/content/image/1-s2.0-S2210670725007267-gr7.jpg)

Download: Download high-res image (722KB)

At the atmospheric scale, extreme meteorological events—such as strong winds or heavy rainfall—pose significant risks to flight safety by inducing turbulence and potentially causing loss of control (). The primary mitigation strategy is to avoid these hazardous conditions. developed methods to quantify ground and aerial risks using weather forecasts to optimize flight paths and minimize exposure to dangerous areas. proposed a real-time urban wind prediction technique that combines meteorological data with CFD simulations, helping reduce the impact of extreme turbulence on flight stability. Chrit et al. () improved wind speed prediction accuracy by coupling the WRF model with OpenFOAM, thereby providing more reliable operational data. Roseman et al. () introduced a small Unmanned Aircraft Systems (UAS) to systematically quantify weather-related risks and generate risk maps (), aiding in the mitigation of adverse wind effects on sUAS operations.

![Fig 8](https://ars.els-cdn.com/content/image/1-s2.0-S2210670725007267-gr8.jpg)

Download: Download high-res image (322KB)

While extreme weather events can often be avoided, turbulence generated by dense urban morphology remains a persistent challenge. Studies indicate that wind speeds within cities can deviate by up to ±74 % compared to open terrain, leading to highly unstable conditions for UAVs (). Wind tunnel experiments with scaled urban models further demonstrate the operational risks arising from airflow variability, such as abrupt wind direction shifts and elevated turbulence intensity. employed Large Eddy Simulation (LES) to analyze urban turbulence and wind shear, highlighting the lack of standardized thresholds for UAV operations in these environments. Raza et al. () combined LES-based wind field modeling with flight simulations to test quadcopter performance, proposing a hybrid control scheme to enhance stability under turbulence. integrated aerodynamic models into the MultiUAV 2.0 platform, revealing that both small and micro UAVs experience substantial route deviations in windy conditions compared to calm scenarios. These studies highlight the urgent need for refined modeling standards and adaptive control strategies to mitigate wind-induced risks in complex urban environments.

Numerical simulations have been widely used to assess the impact of urban environments on airflow and UAV performance. found that a 20° shift in wind angle and a 50 % increase in wind speed significantly elevated flight instability, highlighting the need for advanced control systems. identified a 3 m/s threshold for wind shear, above which control loss risk rises sharply. quantified turbulence-induced efficiency losses, noting a 1.12 % increase in flight path length due to turbulence. showed that urban thermal effects can generate vertical updrafts and downdrafts of up to 20° and 26°, respectively, presenting major challenges for low-altitude UAVs. These studies collectively underscore the critical influence of turbulence and wind shear on eVTOL safety, and reveal an urgent need for more detailed and generalized risk quantification to support safe urban operations.

Understanding turbulence effects on UAVs, particularly at low altitudes, requires a micro-scale aerodynamic approach., ) used dynamic grid simulations to show that increased drag near the ground induces force and moment oscillations, threatening stability. found that updrafts can improve UAV endurance by over 50 % through reduced power demand, while Lei et al. () demonstrated optimal efficiency at a 4 m/s horizontal flow. Ware et al. () integrated wind field and energy models, showing tailwinds reduce both travel time and energy use, while headwinds increase overspeed risk. These studies emphasize the pivotal role of local airflow in optimizing UAV performance and safety in cities.

In urban environments, complex and rapidly changing airflow continuously interacts with eVTOL aerodynamics, directly impacting flight stability and safety, especially during takeoff, landing, and hovering (; ). Deeper insight into urban turbulence mechanisms is therefore essential to advance safe and efficient eVTOL operations.

### 3.3. Section summary

Urban wind and turbulence dynamics play a crucial role in low-altitude aircraft operations, with impacts differing by flight phase and urban context. During takeoff and landing, building geometry intensifies wind shear and turbulence, while during cruising, buoyancy-driven flows induced by urban heat islands destabilize airflow. Surface properties such as thermal conductivity, albedo, and roughness further modulate turbulence intensity and local heat exchange, contributing to microclimate variability. The complex coupling among urban turbulence, multi-scale wind fields, and aircraft aerodynamics presents significant operational challenges, particularly in densely built environments. Accurate assessment of these interactions is essential for the safe deployment of UAM. Nevertheless, existing research is insufficient to address practical demands, highlighting the urgent need for more comprehensive and interdisciplinary studies.

## 4\. Quantitative assessment of urban wind hazards

### 4.1. Risk metrics for operational phases

#### 4.1.1. Analysis of urban wind risk factors

Ensuring the safe operation of low-altitude aircraft necessitates developing risk indicators tailored to different flight phases. Each stage—takeoff, landing, and cruise—is influenced by specific wind conditions. To identify key environmental risks, we statistically analyzed over 150 references (), visualizing the citation frequency of influencing factors (). Parameters such as wind shear, turbulence intensity, and vorticity are most frequently linked to takeoff and landing, underscoring heightened risks in near-ground urban settings. In contrast, cruise-phase factors like gust frequency and crosswind stability receive less focus. This implies that the most severe aerodynamic risks occur during low-altitude operations, though literature on eVTOLs remains limited.

![Fig 9](https://ars.els-cdn.com/content/image/1-s2.0-S2210670725007267-gr9.jpg)

Download: Download high-res image (182KB)

summarizes recent quantitative findings. Wind speed is the most frequently cited metric, with urban features such as street canyons and building edges increasing it by up to 50 %. Local wind differences exceeding 4 m/s can raise landing risk by 18 %. Turbulence intensity during takeoff and landing can surpass 40 % in dense urban areas, significantly affecting flight stability. Vorticity and gust fluctuations peak near upstream wakes, with standard deviations up to 3.8 times higher than in open terrain. Thermal factors also elevate risk: buoyant heat flux can rise by 23.5 % in urban hotspots, while vegetation reduces surface temperatures by up to 18 °C, altering flow patterns and inducing vertical angles up to ±26°, which further challenge vehicle stability.

Table 1. Quantitative statistics of key wind and thermal environmental parameters affecting UAM operations.

<table><thead><tr><th>Scenario</th><th>Parameter</th><th>Quantitative Description</th><th>Refs.</th></tr></thead><tbody><tr><td rowspan="8"><strong>Takeoff/Landing</strong></td><td>Turbulence intensity</td><td>Turbulence intensity below 50 m is significantly higher than in the 50–100 m and 100–150 m altitude ranges.</td><td></td></tr><tr><td>Turbulence intensity, vertical wind speed</td><td>Wake vortices behind buildings significantly increase turbulence around street canyons, with <math><mrow is="true"><msub is="true"><mi is="true">σ</mi> <mi is="true">z</mi></msub> <mo is="true">/</mo> <msup is="true"><mrow is="true"><mi is="true">u</mi></mrow> <mo is="true">*</mo></msup></mrow></math> reaching up to 2-far above inertial sub-layer (ISL) theoretical values.</td><td></td></tr><tr><td>Sky view factor (SVF), mean radiant temperature (MRT)</td><td>A 0.1 decrease in SVF increases longwave radiation by 10 W/m² and MRT by 1.6 K.</td><td></td></tr><tr><td>SVF, pedestrian wind speed</td><td>A 10 % increase in SVF leads to an 8 % increase in pedestrian-level wind speed.</td><td>Yang et al. ()</td></tr><tr><td>Wind speed</td><td>In winter experiments, wind speed on building sides can be up to 2.146 times greater than in central areas.</td><td></td></tr><tr><td>Vorticity, wind speed</td><td>Due to upstream building wake and backflow interference, peak wind speed standard deviation can reach 3.8 times the incoming flow speed.</td><td></td></tr><tr><td>Temperature</td><td>Green walls can reduce surface temperature by up to 18 °C in summer and 8 °C in winter.</td><td></td></tr><tr><td>Wind speed</td><td>A wind speed difference exceeding 4 m/s within 10 m of the ground increases landing failure probability by 18 %.</td><td></td></tr><tr><td rowspan="4"><strong>Cruise</strong></td><td>Mean wind speed, gust wind speed</td><td>For Volocopter multirotor vehicles, the average wind tolerance is 8.6 m/s, with a gust limit of 13.74 m/s.</td><td></td></tr><tr><td>Buoyancy flux</td><td>Thermal plume transport from edge to center (7.5–45 km) takes 1 to 6 h between cities.</td><td>, )</td></tr><tr><td>Wind speed</td><td>Narrow street canyon effects can double wind speed, and abrupt increases near building edges significantly raise vertical shear risk.</td><td></td></tr><tr><td>Turbulence effects</td><td>Path length increased from 411.5 m to 416.1 m due to turbulence, resulting in a 1.12 % flight efficiency loss.</td><td></td></tr><tr><td rowspan="7"><strong>Full flight cycle</strong></td><td>Wind speed, turbulence intensity</td><td>Under specific conditions, when the wind speed increases from 1.9 m/s to 14.9 m/s, the turbulence intensity rises from 4.2 % to 6.1 %.</td><td></td></tr><tr><td>Richardson number (Ri, dimensionless)</td><td>When Ri ranges from −15.68 to −7.84, buoyancy becomes the dominant driver of canyon airflow.</td><td></td></tr><tr><td>Wind speed gradient</td><td>In winter, wind speed changes by 0.8 m/s per 90 m of height; in summer, by 0.4 m/s.</td><td></td></tr><tr><td>Buoyancy flux</td><td>Heat island intensity is highest in monocentric cities, with buoyancy flux increases of up to 23.5 %.</td><td></td></tr><tr><td>Turbulence intensity</td><td>In urban areas with turbulence intensity >40 %, drone operations must be carefully planned to avoid high-risk zones.</td><td>Basawanal et al. ()</td></tr><tr><td>Wind speed</td><td>eVTOL operations limit wind speed to 17 knots (8.7 m/s); operations are suspended above 25 knots (12.9 m/s).</td><td></td></tr><tr><td>Buoyancy flux</td><td>Urban thermal effects can induce vertical flow disturbances, with maximum upward angles up to 20° and downward angles up to 26°</td><td></td></tr></tbody></table>

However, current risk indicators are limited by insufficient spatial and temporal resolution and do not fully capture the localized, dynamic nature of urban airflow. As such, existing data are inadequate to establish comprehensive operational guidelines or universal safety thresholds (). Future research should integrate multi-source wind and thermal datasets to develop robust UAM risk assessment frameworks, particularly for critical phases such as takeoff and landing.

This section reviews the principal environmental factors influencing eVTOL safety during takeoff, landing, and cruise. However, research on standardized indicators for assessing wind-related hazards in low-altitude urban flights remains limited. Further studies are necessary to refine key parameters and establish a robust safety reference framework to guide future research and regulatory development.

#### 4.1.2. Wind hazard evasion in early UAM flight trials

Pilot cities in China and the United States have begun exploring strategies to mitigate urban wind hazards in early eVTOL operations. For example, AutoFlight’s 2023 Shenzhen route was deliberately designed to avoid high-rise clusters, underscoring the importance of considering wind variability and building-induced turbulence (). Elevated TKE levels observed in Shanghai’s Lujiazui district, compared to nearby riverfront areas, further justified routing through zones with lower turbulence (). However, these flight corridors are often kept away from dense urban centers, limiting their applicability to future UAM operations in more complex environments. Additionally, most current trials lack sufficient quantitative data to inform regulatory guidelines or design standards.

To mitigate wind-related risks such as corner vortices, rooftop shear, and downdrafts, operational protocols typically require lateral buffers greater than 120 m and flight altitudes between 300 and 600 m (). For instance, Archer Aviation’s planned route between Newark Airport and Manhattan avoids both dense developments and sensitive locations, minimizing wind and noise exposure (). Nonetheless, these approaches are still largely restricted to isolated demonstration corridors. As UAM networks expand, determining safe minimum distances from urban structures will require further research and more refined assessment methodologies.

These cases highlight the necessity of integrating high-resolution urban wind data into UAM planning. Future studies should closely align with practical deployments to improve low-altitude airspace risk assessment and facilitate the transition from isolated flight corridors to fully integrated UAM networks.

### 4.2. Universal assessment standard for flight safety

Existing standards for hazardous wind detection are typically tailored to specific wind types, limiting their ability to identify the diverse hazardous wind conditions encountered during low-altitude flight. This gap highlights the need for a comprehensive and generalizable assessment framework. To address this issue, developed an interpretable semi-supervised clustering method that incorporates prior knowledge and probabilistic modeling to detect and assess multiple types of aviation hazardous winds, including wind shear, turbulence, and wake vortices. The model was trained and tested using wind data from five Chinese airports, notably including Hong Kong International Airport (HKIA) from 2017 to 2020, encompassing 515,627 unlabeled and 181 labeled hazard records.

Results showed that most unlabeled samples from HKIA were classified as calm winds with low risk, indicating effective feature extraction. Moreover, the proposed method consistently outperformed conventional approaches in identifying various hazardous wind types, particularly at optimal detection thresholds. Quantitative analysis further confirmed a strong correlation between the hazard factor assigned by the model and actual hazard intensity, demonstrating its capacity for reliable intensity assessment.

While the method exhibited strong generalization and adaptability across airports, limitations remain, such as dependence on limited pilot reports and potential performance issues under extreme weather. These aspects should be addressed in future research to enhance quantitative assessment of urban wind-related hazards.

### 4.3. Section summary

As noted in,, quantitative assessment of urban wind disaster hazards remains insufficient. However, evaluating wind disaster risks in low-altitude urban areas is essential for advancing UAM safety. Future research should focus on developing scenario-specific risk assessment standards for both takeoff/landing and cruising phases. Moreover, studies should address these hazards across diverse urban settings, including high-rise clusters and urban canyons.

## 5\. Real-time wind prediction and operational strategies

Real-time prediction of low-altitude wind is crucial for ensuring the safety and operational flexibility of UAM, especially in rapidly evolving urban weather conditions. Unlike long-term planning, which focuses on airspace structure and resource allocation, real-time modeling addresses the dynamic interplay among urban morphology, surface thermal effects, and transient meteorological patterns—factors that often induce hazardous phenomena such as gusts, turbulence, and wind shear. These localized, time-sensitive events are not adequately captured by historical data or steady-state models. Instead, high-frequency observations combined with transient simulations enable timely risk detection, facilitating obstacle avoidance and flight path adjustments. This section reviews current approaches for real-time wind prediction in complex urban airspace.

### 5.1. Predictive methodologies

#### 5.1.1. Data driven

##### 5.1.1.1. Traditional methods

Real-time airflow prediction is essential for low-altitude UAM operations. Although urban morphology is relatively stable, meteorological variability, changing traffic patterns, and the presence of UAM vehicles introduce substantial turbulence and complexity. These dynamic factors challenge traditional physics-based models, which often fail to deliver accurate real-time forecasts due to unquantifiable environmental uncertainties. Recent studies have shown that such models are generally outperformed by data-driven approaches across various forecasting horizons (; ).

Reduced Order Models (ROMs) improve computational efficiency by capturing key system dynamics in a lower-dimensional space. Techniques like Proper Orthogonal Decomposition (POD), combined with machine learning, have demonstrated enhanced performance in airflow forecasting at multiple spatial scales (,; ). ROMs can be intrusive, projecting governing equations into reduced spaces for faster simulation, or non-intrusive, using data-based approximations ().

Traditional statistical models leverage historical time series data and employ methods like Kalman filtering and information criteria to enhance forecast accuracy. Hybrid models now integrate spatiotemporal features with high-resolution boundary conditions, achieving over 90 % accuracy in wind prediction tasks ().

While these approaches are promising for quantifying environmental uncertainties and delivering real-time predictions, their application to complex urban environments and UAM operations remains limited.

##### 5.1.1.2. Intelligent and machine learning-driven methods

Traditional statistical models provide real-time wind direction predictions but are limited in handling nonlinear wind dynamics. In contrast, machine learning techniques—such as artificial neural networks (ANNs)—can capture complex, nonlinear wind patterns by learning from data and adapting to changing urban conditions (; ). Recent studies highlight the advantages of deep learning: used an Long Short-Term Memory with Firefly Algorithm (LSTM-FWA) model for urban wind forecasting, and found Long Short-Term Memory (LSTM) and Gated Transformer Units (GTUs) models outperformed seasonal Autoregressive Integrated Moving Average (ARIMA) in offshore wind predictions. applied neural architecture search to improve accuracy with limited urban datasets.

Advanced models such as Generative Adversarial Neural Networks (GANs) and Graphical Neural Networks (GNNs) have further enhanced wind prediction capabilities. GANs generate high-resolution airflow fields from sparse data (), while GNNs can accelerate CFD simulations on unstructured meshes (). Hybrid approaches are also emerging; for example, proposed a two-stage CFD-GNN framework that matches LES results with lower computational cost, and used GNNs for rapid pollutant dispersion prediction.

Moreover, integrating federated learning and hybrid neural schemes has improved both accuracy and scalability. Innovations such as Convolutional Neural Network - Long Short-Term Memory (CNN-LSTM) hybrid models (), Federated Deep Reinforcement Learning (FedDRL) for ultrashort-term forecasting (), and MultiScale Feature Adaptive Extraction (MSFAE) for improved reliability (), leveraging multi-source sensor data, provide critical support for wind prediction in UAM operations.

#### 5.1.2. Hybrid models

Hybrid models leverage the complementary strengths of physical and data-driven approaches to improve the efficiency and accuracy of urban airflow prediction. Physical models provide fundamental understanding of fluid dynamics, while data-driven models effectively capture complex nonlinearities in real environments. Their integration enables more accurate and interpretable predictions. Kastneret al. () proposed a CFD proxy model using GAN to handle arbitrary building geometries. The model was trained using an automated end-to-end pipeline based on Eddy3D and implemented as an Open Neural Network Exchange (ONNX)-based CFD-GAN predictor. While Large Eddy Simulation (LES) offers highly accurate modeling of turbulent urban airflow, its substantial computational cost limits real-time application. To overcome this, data assimilation techniques are increasingly incorporated, allowing real-world observations to continuously refine model outputs. Such approaches enable timely and accurate urban airflow predictions, positioning LES combined with data assimilation as a critical tool for urban-scale applications ().

#### 5.1.3. Sensor networks and data assimilation

Sensor networks are critical for UAM, delivering real-time data on weather, air quality, and other environmental factors (). These distributed sensors across urban areas provide essential information to enhance the safety and efficiency of UAM operations. By integrating sensor data with predictive models through data assimilation techniques, the accuracy of urban airflow forecasting is significantly improved. developed a deep learning-assisted data assimilation method, the Voronoi-tessellation Inverse operator for Variational Data assimilation (VIVID), which efficiently processes sparse and spatially heterogeneous data from low-altitude aerial vehicles. This hybrid approach demonstrates strong potential for enhancing UAM performance in complex urban environments, as illustrated in ().

![Fig 10](https://ars.els-cdn.com/content/image/1-s2.0-S2210670725007267-gr10.jpg)

Download: Download high-res image (337KB)

### 5.2. Environment-aware operational strategies

Accurate forecasting of meteorological factors, particularly wind speed and direction, is fundamental for safe and efficient UAM operations. Integrating real-time wind predictions into dynamic route planning and airspace design enables the adjustment of flight paths, avoidance of hazardous zones, and effective management of complex urban airflow variations. Such strategies are crucial for enhancing operational safety and ensuring the reliable performance of UAM systems in urban environments.

#### 5.2.1. Dynamic route planning

Dynamic route planning allows UAM operations to adapt to real-time meteorological and airspace conditions, which is essential for safe low-altitude flight. proposed a CFD-based approach using the RANS model to identify no-fly zones for delivery drones in various urban wind environments. By analyzing multiple flight directions and altitudes, they generated hazard probability maps to determine safe corridors and optimize flight paths. developed an autonomous navigation system for drones using autoencoder-based aerodynamic learning, while employed mixed-integer linear programming to optimize hospital delivery routes and mitigate airspace congestion.

Weather remains a key factor: integrated simulation-based and quantitative Probabilistic Risk Assessment (PRA) to evaluate collision risks due to loss-of-control in UAM operations. further demonstrated the impact of varied weather conditions on automated UAM trajectories, emphasizing the necessity of adaptive routing.

In summary, effective dynamic route planning in UAM must comprehensively consider wind, urban geometry, and weather. Advanced tools such as CFD and machine learning are crucial for identifying no-fly zones and enhancing route safety and efficiency.

#### 5.2.2. Urban airspace design guidelines

Airspace design is a critical aspect for ensuring safe UAM operations. Yang and Wang et al. () systematically reviewed UAM airspace classification, zoning methods, and structural models, proposing three partitioning approaches (grid-based, layered, and networked) and comparing four structural models: free flight, corridors, tubes, and lanes. Their analysis of advantages, disadvantages, and application scenarios provides theoretical support for optimizing urban airspace utilization and flight safety. introduced the AirMatrix framework, which integrates airspace configuration and operational rules, partitions airspace at various resolutions, and establishes airspace corridors to balance flight flexibility with complexity. They also developed a risk assessment and emergency management system to enhance urban airspace safety. proposed Adaptive Urban Airspace Management (AdUrAM), focusing on optimizing large-scale drone operations. Through comparative analysis of route networks (AirMatrix, building-top, and road-top), they found AirMatrix superior in capacity and throughput. AdUrAM further enables dynamic airspace configuration for efficient and safe management. explored dynamic capacity management for Unmanned Traffic Management (UTM) in dense urban airspace, proposing three traffic control strategies (street-, grid-, and cluster-based), with the small-cluster approach most effective in high-density conditions.

These studies demonstrate that optimizing route networks, balancing flexibility and complexity, and employing dynamic management are key to enhancing UAM airspace safety.

### 5.3. Section summary

This section addresses real-time wind prediction and mitigation strategies across three key areas: predictive methodologies, simulation and experimental validation, and environment-aware operational strategies. Advanced approaches—including data-driven, hybrid, sensor network, and machine learning models—enhance the accuracy of urban wind field prediction for UAM applications. Multi-scale CFD simulations and wind tunnel experiments enable the precise replication of local wind conditions, supporting reliable route planning and adaptive decision-making in complex urban environments. Environment-aware operational strategies leverage real-time data on wind speed, turbulence, and airflow to optimize flight paths and airspace management. The integration of these methods is critical to advancing UAM deployment and supporting the development of the low-altitude economy. Nevertheless, current research remains limited, particularly in comprehensive real-time wind modeling and its practical application to UAM operations in dense urban settings.

## 6\. Conclusions and future perspectives

This paper systematically reviews the interactions between urban environments and UAM systems, emphasizing the effects of complex urban wind, thermal conditions, and turbulence on UAM safety and stability. It evaluates recent progress in simulation methods and future research directions to address the gaps in coupling simulations between aircraft and urban environments. The main conclusions are as follows:
- 1\. Current research on aerodynamic and thermal challenges for UAM in urban settings is insufficient to ensure safe, scalable deployment. Findings from pilot projects in open areas cannot be easily generalized to complex urban terrains.
- 2\. The interplay of building density, height, shape, and layout leads to intricate wind fields characterized by turbulence, wake vortices, and wind shear. These phenomena significantly challenge UAM safety, particularly during takeoff, landing, and hovering.
- 3\. The UHI effect and surface heterogeneity enhance local thermal circulations, increasing wind field non-uniformity and turbulence. Buoyancy-driven turbulence and urban heat dome phenomena further destabilize low-altitude flight, especially in dense city environments.
- 4\. The interaction between urban turbulence and aircraft downwash critically affects flight safety and performance. Quantitative studies on this coupling remain limited; further research will be vital for vertiport siting, wind forecasting, and operational safety.
- 5\. Achieving computational efficiency and accuracy in urban airflow simulation remains a major challenge. Hybrid modeling and real-time data assimilation offer promising directions for improving flight path planning, vertiport selection, and wind prediction.
- 6\. Distinct operational thresholds are needed for different UAM models. Existing standards are mostly adapted from helicopter or fixed-wing aircraft, which may not suit eVTOL. Dynamic, data-driven threshold evaluation systems should be developed for complex urban environments.

Advancing research on the interaction between urban environments and UAM is essential to enable safe, efficient urban air mobility. In-depth studies on turbulence coupling will bridge existing gaps and lay a robust theoretical and data foundation for future UAM technologies.

## CRediT authorship contribution statement

**Yuwei Dai:** Writing – original draft, Visualization, Supervision, Project administration, Methodology, Investigation, Formal analysis, Conceptualization. **Feiyu Zhu:** Visualization, Investigation, Formal analysis. **Wanli Tu:** Visualization, Software, Formal analysis, Data curation. **Haotian Zhu:** Software, Methodology, Formal analysis. **Dan Qin:** Formal analysis, Data curation. **Haidong Wang:** Supervision, Project administration. **Zhiqiang  (John) Zhai:** Writing – review & editing, Supervision, Project administration, Conceptualization.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

This study was financially supported by the National Natural Science Foundation of China (No.,, ), and Chen Guang project (No. 22CGA54), supported by the Shanghai Municipal Education Commission and Shanghai Education Development Foundation.

## Data availability

Data will be made available on request.

## References

- ### System-of-systems safety for low-altitude aviation transportation
	2026, Reliability Engineering and System Safety
	Show abstract
- ### A multi-stage optimization framework for creating atmospheric boundary layer in wind tunnels with a short test section
	2026, Sustainable Cities and Society
	Show abstract
- ### Ten questions concerning urban wind environments for the safe utilization of urban air mobility
	2026, Building and Environment
	Show abstract
- ### Validation practices for simulation-based research
	2026, Energy and Buildings
- ### Estimating the impacts of the wind field size, wind speed, turbulence, and no-fly zones on unmanned aerial vehicle flights in urban areas
	2026, Physics of Fluids
- ### Research on the Impact of Urban Extreme Wind Fields on UAVs’ Flight Stability in Typical Scenarios
	2026, Applied Sciences Switzerland

[View Abstract](https://www.sciencedirect.com/science/article/abs/pii/S2210670725007267)