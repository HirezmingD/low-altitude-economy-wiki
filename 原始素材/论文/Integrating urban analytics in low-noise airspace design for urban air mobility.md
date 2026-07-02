---
title: "Integrating urban analytics in low-noise airspace design for urban air mobility"
source: "https://www.sciencedirect.com/science/article/pii/S1270963826000313?pes=vor&utm_source=clarivate&getft_integrator=clarivate"
author:
published:
created: 2026-07-01
description: "Aircraft noise is a significant constraint in the urban integration of urban air mobility (UAM) system. Recent research has explored various approache…"
tags:
  - "clippings"
---
## Original article EI检索SCI升级版 工程技术1区SCI Q1IF 6.4

[https://doi.org/10.1016/j.ast.2026.111650](https://doi.org/10.1016/j.ast.2026.111650 "Persistent link using digital object identifier")

Full text access

## Highlights

- •
	Proposes a framework that integrates a rigorous urban analytics component in the design of urban airspace for UAM noise mitigation.
- •
	Utilizes geographic information system techniques, modern smart city data, and aircraft noise model to create 3D city-scale noise no-fly zones.
- •
	Develops a tailored UAM optimal path planning algorithm that considers both no-fly zones and flight performance constraints.
- •
	Generates prototypes of the proposed concept in a comprehensive case study in Hong Kong.

- [Next article in issue](https://www.sciencedirect.com/science/article/pii/S127096382600012X)

## Keywords

Urban air mobility

Airspace design

Aircraft noise

Urban analytics

Trajectory planning

## 1\. Introduction

The emergence of urban air mobility (UAM) is anticipated by many to transform urban transportation and services. Enabled by advancements in aircraft design, battery technologies, air traffic management systems, and innovative business models, UAM will utilize small aerial vehicles like electric vertical take-off and landing (eVTOL) aircraft and unmanned aerial vehicles (UAVs) to operate at lower altitudes within or across metropolitan areas. Networked UAM operations will support various urban services, including air taxi services, medical supply transport, environmental monitoring, public safety, and emergency response. This new system offers distinct advantages in time-sensitive services and promoting public welfare in underserved regional communities.

Despite all these features and advantages, integrating UAM into current urban environments is a significant challenge. Urban integration of UAM faces several substantial constraints, including community acceptance of aircraft noise, safety concerns, supporting infrastructure, and air traffic control (ATC),,. Among these constraints, aircraft noise has been identified as a particularly significant factor, exhibiting the highest severity level across all UAM development stages,. Urban noise is already a growing problem with significant social and economic consequences,, and whether UAM noise can be effectively managed will determine if the system can be implemented and sustained in cities around the world. Mitigating UAM’s noise emissions has thus become a top research priority within the aerospace community in recent years,,.

Operations planning, including noise-aware flight trajectory planning, has been a crucial method in aviation for mitigating aircraft noise emissions, as it is necessary regardless of the noise magnitude at the source or the availability of advanced noise reduction aircraft technologies,. Apart from the complex noise-centric flight trajectory optimization, researchers have recently been exploring UAM noise control within the context of proper airspace design for two main reasons. First, noise-aware airspace design can simplify flight trajectory planning by converting noise constraints in urban environments into no-fly zones, allowing flights to achieve satisfactory noise control by simply operating outside these zones. Second, urban airspace management itself is an important problem, as several UAM safety,, and societal considerations (e.g., noise, privacy, perceived risk ) for UAM system planning can be framed as airspace management problems. The current noise-aware urban airspace design problems primarily focus on integrating acoustic and urban terrain models to define airspace sectors that are sufficiently distant from buildings and other objects on the ground.

A significant research gap lies in the fact that noise-aware urban airspace design should be informed by urban analytics techniques, given that UAM operates in a complex urban space and community noise impact is determined by urban residents’ responses to UAM noise emissions. This is made possible by modern smart city initiatives that are focused on developing intelligent functions to synthesize data for enhancing efficiency, equity, sustainability, and quality of life in urban areas,. In this study, we begin to address this gap by contributing to the integration of urban analytics elements for designing city-scale, noise-aware urban airspace that facilitates low-noise planning for UAM operations. Specifically, our urban analytics component integrates:
- •
	High-quality urban geospatial datasets (e.g., ground traffic noise, land use, population density, building heights, and noise-sensitive locations).
- •
	A spatio-temporal model of urban ambient noise, which accounts for hourly variations based on data from rigorous peer-reviewed studies.
- •
	A model of community noise response based on U.S. Environmental Protection Agency (EPA) guidelines, which defines acceptable noise levels as a function of the difference between UAM noise and the local ambient noise level.

With a background review presented in, the proposed model described in and combines geographic information system (GIS) techniques, high-quality urban geospatial and spatio-temporal datasets, along with an aircraft noise model to produce combined physical and noise no-fly zones. In, we introduce a flight profile-informed 3D path planning algorithm, HFPI-A\*, designed to efficiently plan a flight path that takes into account no-fly zones and flight performance constraints. In and, we implement the modeling and planning approach in a case study in Hong Kong. The representative computational results illustrate how key factors, such as noise requirements and time of day, can affect the configuration of the airspace and the resulting optimal flight trajectory.

## 2\. Background

### 2.1. UAM operational constraints

Although UAM offers numerous benefits to urban life and development, its integration into complex urban settings poses significant challenges. An important lesson from the past is that urban helicopter services in places like New York City led to unsustainable operations due to critical challenges in community acceptance, safety, and financial viability. Recently, researchers from North America and Europe conducted thorough analyses and pinpointed key operational challenges to implementing and scaling up a UAM system,,. In summary, the five key operational constraints of UAM are: (1) community acceptance of aircraft noise, (2) safety concerns, (3) availability of takeoff and landing areas (TOLAs), (4) scalability of ATC, and (5) ground and communication infrastructure. These operational constraints can become more prominent at various stages of UAM development. For instance, the availability of TOLAs and the scalability of ATC will pose significant challenges when the UAM system operates at a very high scale.

Among the key operational constraints of UAM, community acceptance of aircraft noise stands out as a particularly significant factor, with most careful studies repeatedly placing it among the top obstacles. Study identified aircraft noise as the only UAM operational constraint that consistently has the highest severity level across all UAM development stages. Study identified aircraft noise reduction as a challenge for UAM that requires the longest period to resolve. Even before UAM emerges, urban noise pollution is already a growing problem with considerable social and economic consequences. Because UAM operates in close proximity to urban residents, the range of noises generated by UAM aircraft poses significant health risks, including psychological discomfort, sleep disruption, and an increased risk of cardiovascular diseases. Consequently, addressing UAM’s noise impact has become a top priority for the community.

### 2.2. UAM noise and mitigation

Mitigating UAM aircraft noise has become a leading focus of research within the aerospace community. In general, we can achieve noise reduction by: (i) developing advanced quiet aircraft components to lessen noise at the source, and (ii) utilizing noise-aware operations planning to decrease the noise footprint during flight. Since breakthroughs in low-noise aircraft design technologies may take time to develop and mature, noise-aware flight operations planning is an indispensable approach for noise mitigation in UAM. In commercial aviation, noise abatement trajectories, such as the continuous descent approach (CDA) and the noise abatement departure procedures (NADP) have been widely studied. Within the UAM domain, the majority of related efforts have concentrated on low-noise flight trajectory planning and air traffic flow management for both eVTOL aircraft and small drones,. Noise-aware flight trajectory planning aims to create 2D or 3D flight paths that avoid populated areas and buildings on the ground,. These planning methods often rely on aircraft noise models from advanced numerical simulations to predict the noise patterns of UAM aircraft in complex urban environments,.

Noise-aware flight trajectory planning can be computationally demanding, as it involves an iterative process that uses both aircraft noise models and numerical optimization algorithms to determine the optimal aircraft trajectory. Another key challenge is that the trajectory planning process must eventually also take into account other considerations, such as safety and privacy, which further increases the complexity of the problem. To tackle these challenges, a newly proposed paradigm addresses low-noise flight trajectory planning through urban airspace design,. The core idea is to transform noise constraints in a complex urban environment into no-fly zones, making the trajectory planning process essentially a barrier avoidance problem, similar to avoiding the urban physical terrain. This airspace-based approach not only improves the computational efficiency of noise-aware trajectory planning but also simplifies the multi-objective trajectory planning problem, as other constraints can also be converted into no-fly zones. The vital role of airspace design in ensuring sustainable and safe operations makes it a crucial problem in UAM development.

### 2.3. Research gap

UAM’s operation in complex urban environments necessitates airspace design and operations planning processes that incorporate urban analytics to promote the system’s community acceptance. For instance, an effective solution for mitigating UAM’s community noise annoyance must integrate geospatial and urban data with models that describe how urban residents react to UAM noise. However, despite the abundance of powerful urban data generated by smart data initiatives worldwide, the integration of urban analytical components into community-friendly UAM airspace design is still insufficiently addressed in the current literature. In this work, we aim to advance data-driven, community-friendly UAM airspace design, focusing on low-noise UAM operations.

## 3\. Data and models

### 3.1. The overall approach

We present a data-driven approach to constructing 3D airspace that facilitates low-noise UAM path planning and promotes community-friendly urban airspace management. illustrates the core components of the proposed approach. Overall, the approach employs urban geospatial data analytics, aircraft noise model, policy requirements, and constrained optimization to achieve the following two outcomes:
- •
	**Noise-aware 3D airspace design:** this part will determine the 3D sectors in urban airspace where UAM operations are prohibited, known as no-fly zones. The noise-aware 3D airspace design involves constructing two types of no-fly zones: physical and acoustic. The physical no-fly zone is straightforward and universal, requiring aircraft to maintain a certain clearance distance from obstacles like mountains and buildings. The green box in shows that we form the physical no-fly zone using urban terrain data, building height data, and minimum clearance information.
	The acoustic no-fly zone is a central focus of this study. Unlike the physical no-fly zone, the acoustic no-fly zone is a virtual concept that aircraft must also avoid to limit community noise impact. The purple box in illustrates that ambient noise estimation and aircraft noise model are the two major components in computing the acoustic no-fly zone. We leverage ambient noise level information and its distribution to better plan noise-aware UAM operations because: (1) as will be discussed in, UAM community noise annoyance is a function of noise difference above the local ambient noise level, and (2) ambient noise masking–concentrating flights over less noise-sensitive areas–is a well-recognized strategy for mitigating UAM’s noise impact. Modeling the acoustic no-fly zone involves using multiple urban geospatial and spatio-temporal datasets, in addition to noise requirements. The combined no-fly zone, depicted in the blue box in, results from the union of physical and acoustic no-fly zones.
- •
	**Airspace- and performance-constrained path optimization:** this part essentially addresses how to plan an optimal flight path by incorporating no-fly zone information. Common practices involve finding the shortest path outside the no-fly zone that connects an origin to a destination. Nevertheless, a UAM aircraft path planning problem is further constrained by aircraft performance and flight profile. A typical flight profile for eVTOL aircraft includes five segments: vertical takeoff, climb, cruise, descent, and vertical landing. In addition, each segment has some performance constraints, such as the rate of climb and descent. A realistic UAM flight path must consider not only restricted airspace but also aircraft flight profile and performance limitations. We will present a modified optimal path planning algorithm that can account for both important considerations.

![Fig. 1](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr1.jpg)

Download: Download high-res image (690KB)

### 3.2. Datasets and data integration

The urban datasets used in the proposed approach must comprehensively cover the key aspects of low-noise urban airspace design. provides a summary of nine identified datasets, using Hong Kong as a case study. These datasets come from government databases, like the Hong Kong government database, or open geospatial data sources, such as Esri.

Table 1. Summary of relevant datasets identified in this study.

| Dataset Number | Dataset Name | Source(s) | Used in This Study |
| --- | --- | --- | --- |
| 1 | Ground Traffic Noise Data | Hong Kong Environmental Protection Department (EPD) | Y |
| 2 | Land Use Zonings Data | Esri China Hong Kong | Y |
| 3 | Digital Terrain Model (DTM) Data | Hong Kong Common Spatial Data Infrastructure (CSDI) | Y |
| 4 | Building Height Data | Esri China Hong Kong | Y |
| 5 | Population Density Data | Esri China Hong Kong | Y |
| 6 | Noise Sensitive Locations Data | Esri China Hong Kong | Y |
| 7 | Building Height Control Areas Data | Esri China Hong Kong | N |
| 8 | Aviation Noise Data | Noise Map Global Noise Dashboard | N |
| 9 | Temporal Noise Data | Journal Papers, | Y |

Of the nine datasets identified in, seven are used in this study. Six of these (datasets 1–6) are urban geospatial datasets that cover ground traffic noise, land use zoning, digital terrain model (DTM), building height, population density, and noise-sensitive locations. visualizes the six geospatial datasets within the selected area of Hong Kong. The building height control areas data (dataset 7) is not used because the building height data (dataset 4) provides more precise information. The aviation noise data (dataset 8) is not used because it is less direct for evaluating ground ambient noise. The final dataset, temporal noise data, describes how ground noise changes throughout the day and is sourced from two journal papers. In the following, we outline the details of each dataset and the data processing method.

![Fig. 2](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr2.jpg)

Download: Download high-res image (2MB)

#### 3.2.1. Ground traffic noise data

The ground transportation noise data shown in (a) is provided by the Hong Kong Environmental Protection Department (EPD). It describes the calculated L <sub>10</sub>, the noise level exceeded for 10% of the time during a 1 h measurement period, at 4 PM during the traffic peak hour, measured at a height of 4 m. The use of L <sub>10</sub> to describe traffic noise stems from extensive research that found L <sub>10</sub> correlates well with community response. It was adopted in developed countries like the UK as the eligibility criterion for acoustic insulation. The data format is GeoTIFF, which includes geo-referencing capabilities within the traditional tagged image file format (TIFF). This format is supported by various GIS software, including the tool used for data integration in our study. Similar datasets exist globally, such as the National Transportation Noise Exposure Map in the United States,. Ground transportation noise is the major contributor to urban ambient noise and will be used in this study as the main source for estimating the ambient noise distribution in the city.

#### 3.2.2. Land use zoning data

The land use zoning data shown in (b) shows the broad land use zoning within the Planning Scheme Area of Outline Zoning Plans in Hong Kong. The source data in Shapefile format is a subset of the Digital Planning Data made available by the Town Planning Board under the Hong Kong Government. This original dataset includes a relatively large number of land use types. For example, under ‘residential area,’ there are five subcategories with even more detailed groups. Based on the Land Utilization in Hong Kong (LUHK) released by the Planning Department of Hong Kong, we consolidated a group of 12 land use types as the definitive list for this project: Water Bodies, Transportation, Residential, Recreation, Industrial, Conservation, Comprehensive Development Area, Commercial, Agriculture, Open Space, Other Specified Uses, and Government or Institution.

Land use zoning data plays a key role in UAM noise management, as different land use zones have varying daily noise levels and standards. For example, the Hong Kong EPD has established the categorization of noise Area Sensitive Rating (ASR) and the corresponding Acceptable Noise Levels (ANLs) for different areas. In addition, existing research in the literature contains typical noise levels for these standard land use zones. We utilize noise data from major cities, including Manchester, Wuhan, and Tainan,, to establish typical noise levels for the 12 zones, with emphasis on the noise levels observed during the afternoon period, which corresponds to the time of peak activity within the city. presents the 12 consolidated land use types and their minimum, maximum, and average noise levels in decibels (dBA).

Table 2. Consolidated land use types and their noise levels in dBA.

| Zone Number | Category | *L* <sub>min</sub> | *L* <sub>max</sub> | *L* <sub>avg</sub> |
| --- | --- | --- | --- | --- |
| 1 | Water Bodies | 47.5 | 82.5 | 65.5 |
| 2 | Transportation | 46.0 | 84.0 | 71.6 |
| 3 | Residential | 41.5 | 79.0 | 62.2 |
| 4 | Recreation | 40.0 | 82.0 | 61.9 |
| 5 | Other Specified Uses | 41.5 | 81.5 | 60.0 |
| 6 | Open Space | 46.0 | 84.0 | 71.6 |
| 7 | Industrial | 41.5 | 79.8 | 62.5 |
| 8 | Government or Institution | 48.0 | 79.5 | 66.5 |
| 9 | Conservation | 47.5 | 82.5 | 65.5 |
| 10 | Comprehensive Development Area | 41.5 | 81.5 | 60.0 |
| 11 | Commercial | 68.0 | 78.0 | 74.0 |
| 12 | Agriculture | 37.5 | 82.5 | 60.5 |

#### 3.2.3. Digital terrain model data

The Digital Terrain Model (DTM) data shown in (c) is a digital terrain model of Hong Kong from the 2020 LiDAR Survey. It shows the topography of the Hong Kong terrain (including non-ground features like elevated roads and bridges) in a 5-meter raster grid with an accuracy of plus-minus 5 m. DTM data is the primary source for modeling the natural physical terrain and the physical no-fly zones.

#### 3.2.4. Building height data

The building Height Data shown in (d) shows the building locations of buildings in Hong Kong. It is a dataset provided by the Lands Department under the Hong Kong Government. The source data is in Shapefile format, with top height information linked to each building’s shape data. This dataset is crucial for establishing physical no-fly zones, ensuring UAM operations maintain adequate clearance distances from buildings in the city.

#### 3.2.5. Population density data

The population density data is derived from the 2021 Hong Kong Population Census Statistics by District Council Constituency Area, as shown in (e). This dataset contains the boundaries of the 452 District Council Constituency Areas and provides statistics on demographic, household, educational, economic, housing, and internal migration characteristics of the Hong Kong population, offering benchmark data on the population’s socio-economic traits. To compute the population density of each Constituency Area, one divides its total population by its area.

#### 3.2.6. Noise sensitive locations data

Noise-sensitive locations include hospitals, schools, nursing homes, etc. In this study, we include the locations of hospitals in Hong Kong, as shown in (f). It is a subset of the geo-referenced public facility data provided by the Hospital Authority under the Hong Kong government. The design approach will apply the strictest noise criteria to hospitals.

#### 3.2.7. Temporal noise data

One limitation of the ground transportation noise data in (a) and the land use zone noise levels in is that they only represent noise levels during the afternoon peak hour at 4 PM. It is widely recognized that urban ambient noise fluctuates throughout the day. Consequently, there is a necessity for an additional data source to model the general temporal patterns of urban ambient noise.

We identified two studies in the literature that collected data to model the temporal patterns of urban noise in East Asia. The first study provides comprehensive hourly measurements of A-weighted decibel noise levels at 14 different roads in Foshan, China, which were used as one of their multiple data sources for mapping the spatiotemporal distribution of traffic noise. The second study provides comprehensive hourly noise monitoring data collected by the Taipei City Government from 24 noise measurement points. Using 4 PM as the reference point, displays the main hourly noise variation patterns reported in and. There is a good overall agreement between the mean trends from the two studies, as shown by the blue and red curves in. In this study, we use the mean results from the two studies, represented by the purple curve in, to model the hourly ambient noise variation in Hong Kong. Given the limitations for more precise spatiotemporal ambient noise modeling, we assume that this temporal pattern applies uniformly across all locations within our area of investigation.

![Fig. 3](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr3.jpg)

Download: Download high-res image (247KB)

#### 3.2.8. Data integration and processing

This step integrates the six main urban geospatial datasets shown in into a single environment and converts them into formats suitable for computations. The collected datasets exhibit format inconsistencies, with some datasets in shapefile format containing both geometric and attribute data, as shown in (a), while others were in raster image format, as illustrated in (b), or point data formats. This necessitated standardization processing to achieve format uniformity. Furthermore, the datasets utilize different coordinate reference systems, necessitating extensive processing to transform their geometric references to a standardized system. We carried out this geospatial standardization using ArcGIS software tools together with Python programming language.

![Fig. 4](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr4.jpg)

Download: Download high-res image (732KB)

After determining the definitive study region (mainly Kowloon Bay and Hong Kong Island), we implemented a standardized grid system in ArcGIS to facilitate consistent spatial analysis, using the WGS 1984 Web Mercator (auxiliary sphere) as the coordinate reference system. Within this spatial framework, we established a 200  ×  200 cell fishnet, as illustrated in, for data aggregation. We customize data aggregation methods to suit the characteristics of each dataset, typically adopting a more conservative analytical approach. For building height and DTM data, we use the maximum height value to represent physical terrain constraint for each cell; the predominant land use category to denote the zoning classification of a cell; and the minimum recorded value to represent transportation noise within the cell.

![Fig. 5](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr5.jpg)

Download: Download high-res image (1MB)

The standardization process converts all geospatial datasets into 200  ×  200 matrices, ensuring that all entries are prepared for subsequent computations. visualizes these post-processed geospatial datasets in a uniform numeric format. We will utilize these geospatial data matrices, along with an aircraft noise model and policy requirements regarding noise and clearance distance, to construct a noise-aware 3D airspace for the Hong Kong region.

![Fig. 6](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr6.jpg)

Download: Download high-res image (1014KB)

The richness and reliability of the integrated geospatial data are critical to the framework’s robustness. The seven core datasets provide a diverse representation of urban physical, acoustic, and social dimensions. Data reliability is upheld through the use of authoritative sources and a conservative aggregation strategy within a standardized 200x200 grid, employing maximum values for physical features and minimum values for noise to ensure prudent no-fly zones.

### 3.3. Aircraft noise model

The aircraft noise model is an indispensable part of this noise-aware airspace design approach. In the aviation community, practitioners model the community noise impact of aircraft in urban and suburban areas using a standard known as noise-power-distance (NPD) data, which describes the relationship between an aircraft’s noise level and its slant distance to an object. For a specific aircraft type, the NPD data is obtained from either noise certification tests or controlled tests conducted in accordance with rigorous international standards. Currently, NPD data is available for the majority of fixed-wing aircraft and helicopter types operated around the world.

Since UAM operations will involve eVTOL aircraft, a new aircraft configuration, there is currently no existing data or test results available for developing NPD data. Consequently, researchers develop NPD data through a combination of acoustic modeling and flight simulation. illustrates some core concepts in this process. Researchers begin with an eVTOL aircraft configuration (shown in (a)), conduct acoustic modeling to generate its noise hemisphere (shown in (b)), which captures the 3D directivity of noise near the aircraft configuration, and ‘fly’ the aircraft in a simulation environment (shown in (c)) to generate the sound exposure level (SEL) NPD data for three operational modes: level flyover (L), departure (D), and approach (A).

![Fig. 7](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr7.jpg)

Download: Download high-res image (600KB)

In this study, we fit a logarithmic regression model to a set of NPD data published by NASA researchers for their Revolutionary Vertical Lift Technology (RVLT) vehicle concept,, as shown in (a). For each combination of operational mode (L, D, A) and measurement position (centerline, side), the regression model takes the following functional form:(1) $N \left(d\right) = a_{0} + a_{1} log_{10} d + a_{2} \left(log_{10} d\right)^{2}$ where *N* represents noise in A-weighted SEL and *d*  ∈ \[200, 20000\] denotes distance in ft. displays the goodness-of-fit for the six NPD regression models, plotted alongside the original data points. presents the coefficients for the six NPD regression models.

![Fig. 8](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr8.jpg)

Download: Download high-res image (291KB)

Table 3. Coefficients for the NPD regression models.

| Operational Mode + Measurement Position | *a* <sub>0</sub> | *a* <sub>1</sub> | *a* <sub>2</sub> |
| --- | --- | --- | --- |
| Mode L (Level Flyover) - Centerline | 88.09 | 3.21 | −2.62 |
| Mode L (Level Flyover) - Side | 78.01 | 7.26 | −3.39 |
| Mode D (Departure) - Centerline | 84.05 | 8.76 | −4.18 |
| Mode D (Departure) - Side | 77.34 | 11.34 | −4.72 |
| Mode A (Approach) - Centerline | 93.35 | 5.17 | −2.86 |
| Mode A (Approach) - Side | 85.55 | 6.83 | −3.14 |

### 3.4. Community noise response

The management of noise pollution in urban communities is a complex problem that requires a systematic approach. Any rigorous treatment of this issue should acknowledge that different communities within the city have varying degrees of noise sensitivity. Urban communities display varying levels of noise acceptance due to two factors: (1) land use, and (2) the different ambient noise levels. Ambient noise in urban spaces encompasses the background sounds generated by a variety of sources, including transportation, construction, human activities, and natural phenomena. In fact, ambient noise plays a crucial role in predicting community responses to UAM noise.

The U.S. Environmental Protection Agency (EPA) conducted a comprehensive study to evaluate community reactions to noise exposure. presents the findings of a related study that models expected community reactions based on noise emission levels exceeding the ambient noise, specifically the ‘additional’ noise generated by an activity. The result indicates that community annoyance increases as the noise difference above the local ambient level rises. When the noise emission from UAM operations reaches 10 dB above the ambient level, widespread complaints are likely to occur. When the difference increases to 20 dB, the community’s response may escalate to threats of legal action. Therefore, our proposed approach incorporates ambient noise as a key factor in assessing spatio-temporal noise sensitivity throughout the city.

Table 4. Expected community annoyance as a function of the difference between noise emission and ambient noise levels (source: ).

<table><thead><tr><th>Expected Community Reaction</th><th colspan="2">Difference Between Noise Emission Level and Ambient Noise Level in dB</th><th>Approx. % Very Much Annoyed</th><th>Approx. % Little or Not Annoyed</th></tr><tr><td>Empty Cell</td><th>Mean</th><th>Range</th><td>Empty Cell</td><td>Empty Cell</td></tr></thead><tbody><tr><td>No reaction</td><td>2</td><td>0 to 8</td><td>20</td><td>45</td></tr><tr><td>Sporadic complaints</td><td>6</td><td>3 to 8</td><td>26</td><td>37</td></tr><tr><td>Widespread complaints</td><td>11</td><td>7 to 19</td><td>37</td><td>26</td></tr><tr><td>Threats of legal action</td><td>21</td><td>18 to 24</td><td>60</td><td>14</td></tr><tr><td>Vigorous action</td><td>28</td><td>23 to 34</td><td>87</td><td>7</td></tr></tbody></table>

## 4\. Airspace design results

### 4.1. Key concepts

In this section, we introduce the 3D airspace construction process and present prototypes of noise-aware airspace designs under various conditions. The overarching objective is to create 3D noise-informed no-fly zones that UAM flyover operations must avoid in order to limit noise exposure on the ground. There are two critical points here. First, our current objective is to control the ground noise impact of UAM operations. Ground noise is not only the most critical noise issue in urban spaces, but it also represents a scenario where urban residents are directly exposed to noise emissions without any sheltering effect. Second, we aim to control flyover noise, as it is the dominant segment of the flight profile and can simplify this new airspace concept at this stage.

In, we distinguish the four 3D airspace model concepts through data visualizations. Each ‘box’ in contains the full range of investigation on the x-y plane and an altitude range from 0 to 3,000 ft (or 1,000 m) mean sea level (MSL), corresponds to the altitude range in which UAM is expected to operate.
- 1.
	**Digital terrain model (DTM):** shown in (a), this is a digital model of the bare earth surface in the Hong Kong area, excluding most buildings and other man-made structures.
- 2.
	**The building no-fly zone:** shown in (b), adding on the DTM, the light green region incorporates all buildings and other man-made structures in the Hong Kong area, as well as the no-fly zones centered around these buildings. Here, we set the minimum clearance distance as 250 ft above any building. Result in (b) is the ’physical’ no-fly zone.
- 3.
	**The noise no-fly zone:** shown in (c), adding on the DTM, the yellow 3D sectors are the noise no-fly zones, which is a virtual concept for noise control. We will compute the noise no-fly zones by integrating all geospatial data matrices, the temporal noise model, the aircraft noise model, and policy analyses. The interpretation of this concept is straightforward: UAM flyovers must operate outside the noise no-fly zones.
- 4.
	**The combined no-fly zone:** shown in (d), represents the union of the two no-fly zone sets: physical and noise. This represents the overall no-fly zone for both objective avoidance and noise control purposes. This also serves as the basis for noise-aware flight path planning.

![Fig. 9](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr9.jpg)

Download: Download high-res image (1MB)

### 4.2. Modeling procedure

Since all geospatial datasets are in the same matrix format, we denote the representation of the noise no-fly zone as $N \left(t\right) = \left[N_{i j} \left(t\right)\right]_{i = 1 , \ldots , n , j = 1 , \ldots , m}$, where *N <sub>ij</sub>* (*t*) refers to the minimum flyover altitude at the ground region in the *i* th row and *j* th column of the matrix *N* at time *t*.

We start by estimating the urban ambient noise level. We let matrix *G* denote the ground transportation noise at 4 PM and matrix *L* denote the average land use noise at 4 PM. We combine these two aspects as estimate the spatial distribution of ambient noise in the city as:(2) $\mathbf{\mathit{A}} = max \left\{\mathbf{\mathit{G}} , \mathbf{\mathit{L}}\right\}$

Subsequently, we incorporate the temporal dimension into the ambient noise estimation. We convert the mean temporal model displayed in as a normalized factor *T* (*t*) such that $T \left(t = 16\right) = 1$, i.e., the ambient noise matrix *A* is original at 4 PM (1600). Then, the spatio-temporal model of urban ambient noise is:(3) $\mathbf{\mathit{A}} \left(t\right) = \mathbf{\mathit{A}} \cdot T \left(t\right)$

We next incorporate noise-sensitive locations. In this study, we primarily consider hospitals as noise-sensitive areas where more stringent noise regulations must be applied. For each hospital, we consider its exact location along with the eight adjacent entries surrounding it as noise-sensitive locations in the matrix. This results in a binary matrix *S*, where 0 indicates noise-sensitive locations and 1 indicates all other locations. Since we are using the difference between UAM noise emissions and the local ambient noise level as the primary method to quantify community noise annoyance, we denote the allowable noise increase as Δ *N*. For noise-sensitive locations, we ensure that UAM noise emissions do not exceed the local ambient noise level. Therefore, the matrix representing the permitted noise levels is:(4) $\mathbf{\mathit{P}} \left(t\right) = \mathbf{\mathit{A}} \left(t\right) + \Delta N \cdot \mathbf{\mathit{S}}$

Now, we consider the impact of population density on community noise response. We let matrix *D* denote the population density in the city and the median population density $\overset{\sim}{D}$ as a reference value. In, we see that as the noise difference increases, a larger percentage of the population becomes annoyed. Population density further enables the calculation of the number of people who become annoyed, which is proportional to the product of Δ *N* and *D*. When using the total annoyed population as the standard, the density-corrected permitted noise levels are:(5) $\mathbf{\mathit{P}}_{D} \left(t\right) = \mathbf{\mathit{A}} \left(t\right) + \left(\Delta N \cdot \overset{\sim}{D}\right) \cdot \mathbf{\mathit{S}} \oslash \mathbf{\mathit{D}}$ where *S* ⊘ ***D*** denotes the Hadamard division between *S* and *D*. indicates that the noise increase should be smaller for communities with higher population density.

Finally, we integrate the aircraft noise model. The NPD model *N* (*d*) described in represents noise as a function of distance. We choose the Mode L, the more conservative centerline coefficients for modeling the flyover noise, $N_{L - c} \left(d\right)$. In our airspace design problem, we require a noise model that describes ground clearance distance as a function of permitted noise, specifically $d = N_{L - c}^{- 1} \left(P\right)$. We calculate the noise-centric minimum flyover distance above the ground as:(6) $\mathbf{\mathit{N}} \left(t\right) = N_{L - c}^{- 1} \left(\mathbf{\mathit{P}}_{D} \left(t\right)\right)$

We further apply a max pooling operator, used in convolutional neural networks (CNNs), to the *N* (*t*) above. Specifically, we apply a 2  ×  2 max pool filter which selects the maximum value within each 2  ×  2 region. This aims to: (1) consider and mitigate flyover noise in adjacent cells, and (2) incorporate local feature invariance into the noise no-fly zone. With max pooling, we have:(7) $\mathbf{\mathit{N}}^{'} \left(t\right) = \text{MaxPool} \left(\mathbf{\mathit{N}} \left(t\right)\right)$

Similarly, we also construct a representation for the physical no-fly zone by combining the DTM and building height data. Let matrices *E* and *B* denote the heights of the Earth’s surface and man-made structures, respectively. Since matrix *B* is measured in above ground level (AGL) altitude, the heights of the man-made structures are given by $max \left(\mathbf{\mathit{B}} - \mathbf{\mathit{E}} , \mathbf{\mathit{O}}\right)$, where *O* is the *m* -by- *n* matrix of zeros. With the requirement of minimum vertical clearance distance Δ *h*, the physical no-fly zone representation above the ground is:(8) $\mathbf{\mathit{H}} = max \left(\mathbf{\mathit{B}} - \mathbf{\mathit{E}} , \mathbf{\mathit{O}}\right) + \Delta h \cdot \mathbf{\mathit{J}}$ where *J* is a *m* -by- *n* matrix of ones. The representation of the physical and noise combined no-fly zone, adding on the DTM, is:(9) $\mathbf{\mathit{C}} \left(t\right) = \mathbf{\mathit{E}} + max \left(\mathbf{\mathit{N}}^{'} \left(t\right) , \mathbf{\mathit{H}}\right)$

In the next two subsections, we will carry out the data-driven modeling procedure and generate noise no-fly zone results under various conditions.

### 4.3. Under different noise requirements

We first examine the impact of noise requirements (an element in the purple box in, and Δ *N* in ) on the height and volume of no-fly zones. Regarding a reasonable range for noise increase above the local ambient level, Study () investigated from zero to $\Delta N = \text{approx}. 30$ dB; Study set $\Delta N = 30$ dB as the absolute maximum noise impact within a relevant context. In this study, we vary Δ *N* from 5 dB to 25 dB. shows the noise no-fly zone results under varying noise requirements, with the time of day fixed at 4 PM, the afternoon peak hour. We observe that under the most permissive noise requirement, 25 dB above the ambient noise level, as shown in (a), the upper boundaries of the noise no-fly zones are very close to the ground. This indicates that with relaxed noise requirements, UAM can operate within a wider airspace and fly closer to the ground surface. As the noise requirements become more stringent, from 25 dB to 5 dB above the ambient level, the no-fly zones expand, reducing the space available for UAM operations. Consequently, above the same location UAM flights must maintain a greater distance from the ground to mitigate noise impact.

![Fig. 10](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr10.jpg)

Download: Download high-res image (1MB)

### 4.4. Under different times of a day

We then examine the temporal effects of the noise no-fly zone. Because urban ambient noise exhibits temporal patterns and varies throughout the day, the space within the noise no-fly zone changes even with the same noise requirements. presents the noise no-fly zone results at six representative times of the day: 12 AM, 3 AM, 9 AM, 12 PM, 4 PM, and 9 PM, with the noise requirement fixed at 15 dB above the ambient level, which is a median level. (c) shows that at $t = 9$ AM, during the morning rush hour, there is more space available for UAM operations due to the high ground ambient noise. During late night and early morning hours, such as midnight and 3 AM, the heights of the noise no-fly zones are elevated, resulting in less space for UAM operations. Overall, the results presented in and align with the general expectations of the concept.

![Fig. 11](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr11.jpg)

Download: Download high-res image (1MB)

## 5\. The airspace-enabled low-noise path planning

This noise-aware airspace design concept is intended to enhance the more efficient low-noise UAM flight path planning and promote a more integrated urban ATM framework via airspace management. In this section, we present a preliminary solution for utilizing the noise-aware airspace concept in practical UAM path planning.

### 5.1. The flight profile-informed path planning algorithm

This path planning problem is an optimal pathfinding problem that is subject to two distinct types of constraints. First, the flight path must avoid all no-fly zones to ensure sufficient clearance from urban terrain and maintain limited ground noise emission. To navigate outside the no-fly zones, the flight path can either fly above or bypass a specific prohibited 3D sector in the airspace. When flight distance or time are the primary measures of operational efficiency, finding the shortest path from A (the origin) to B (the destination) while avoiding no-fly zones can be effectively addressed using existing methods like the A\* algorithm,.

Second, constraints also arise from the aircraft’s flight profile and performance limits, requiring the fusion of flight profile information into the path planning process. A flight profile consists of distinct segments, each with specific performance characteristics that a mission must adhere to. illustrates the five segments of a standard eVTOL aircraft flight profile ‘from vertiport to vertiport,’ which include vertical takeoff, climb, cruise, descent, and vertical landing. Among the performance limits in a flight profile, the most prominent ones affecting path planning are the rate of climb (RoC) and rate of descent (RoD). For example, when considering the RoC, the flight path angle *γ* during climb may not exceed a certain threshold. Study suggested this limit to be $tan \left(\gamma\right) = 1 / 5$.

![Fig. 12](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr12.jpg)

Download: Download high-res image (128KB)

We propose a Hybrid Flight Profile-Informed A\* algorithm (HFPI-A\*) to efficiently plan a flight path that incorporates no-fly zone and flight profile information. The HFPI-A\* has the following core ideas for integrating flight profile information:
- •
	Plan by segments: instead of planning the entire path from vertiport to vertiport in one go, the algorithm plans each segment separately. For the two vertical segments, eVTOL aircraft ascend and descend vertically between the ground and 250 ft AGL. The main algorithm focuses on the climb, cruise, and descent segments, as shown in.
	![Fig. 13](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr13.jpg)
	Download: Download high-res image (333KB)
- •
	Performance constrained space discretization: For planning purposes, the entire airspace is discretized into 3D cells. The discretization on the x-y plane is established during the geospatial data processing step and is illustrated in. illustrates the options for directional movement in a vertical plane. When the aircraft is in the central cell, it can move to the eight surrounding cells in the same vertical plane, which include two vertical movements, two diagonal ascent movements, two diagonal descent movements, and two horizontal movements. In Discretization(*γ <sub>c</sub>*, *γ <sub>d</sub>*), the airspace is vertically divided into 3D cells with a height of Δ *h <sub>c</sub>*, resulting in a diagonal movement angle $\gamma = min \left\{\gamma_{c} , \gamma_{d}\right\}$. This ensures that every diagonal ascent/descent movement is achievable in relation to the rate of climb/descent.
	![Fig. 14](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr14.jpg)
	Download: Download high-res image (124KB)
- •
	A\* functions with distinct movement options: Options for directional movement are crucial in pathfinding algorithms like A\*. In 3D space, each cell has 26 adjacent cells to move to, similar to the center of a 3-by-3 cube. In our path planning problem, we must further customize the directional movement options based on the nature of each segment. For climb and descent, vertical movements violate the performance definitions and are not permitted. A customized A\* function, AStarClimbDescent(s, e), incorporates the remaining 24 directional movements and is designed for both climb and descent segments, where s and e denote the start and end points of the path, respectively.For cruise segments, the aircraft should maintain its current altitude. A specialized A\* function, AStarCruise(s, e), restricts movement to only the 8 horizontal directions.
- •
	Cone search for climb and descent paths: Both climb and descent segments link the vertical operations ceiling with the cruising altitude *h*, as illustrated in. Because we use plan by segments, identification of the two key connecting points is essential to the approach. We let *p <sub>cr</sub>* denote the connecting point between climb and cruise, and *p <sub>rd</sub>* the connecting point between cruise and descent. Due to the no-fly zones, *p <sub>cr</sub>* and *p <sub>rd</sub>* may not align along the straight line connecting the origin and destination. Therefore, to identify a connecting point, we start from the vertical operations ceiling and conduct a 360-degree search along the circumference where the cone, constrained by RoC/RoD, intersects with the cruising altitude plane. In the ConeSearch(s, *h*), we evaluate a set of 8 points (with angles of 0 <sup>∘</sup>, 45 <sup>∘</sup>, 90 <sup>∘</sup>, etc.) on the circumference and select the feasible connecting point that is nearest to the destination. also illustrates the cone search process.

details the complete HFPI-A\* algorithm for path planning under no-fly zones and flight profile information. The final output *P* is the shortest flight path that satisfies all the conditions mentioned above.

![Algorithm 1](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-fx1.jpg)

Download: Download high-res image (536KB)

### 5.2. Low-noise path planning results

In the end, we apply the HFPI-A\* plath planning algorithm to the noise-aware airspace designs and investigate the landscape of 3D low-noise flight trajectories in complex urban environments. We select two UAM routes in Hong Kong for illustrative purposes. As shown in, route 1 connects Lamma Island to Sai Kung, and route 2 connects Tung Tau Wan to Tsuen Wan.

![Fig. 15](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr15.jpg)

Download: Download high-res image (409KB)

and display the path planning results for route 1 and route 2, respectively. Note that the blue no-fly zones represent the combined no-fly zones that account for both noise and urban physical terrains. For each route, we conduct path planning at three cruising altitudes: 1,000 ft, 1,500 ft, and 2,000 ft MSL, as well as three noise increase levels: +5 dB, +10 dB, and +20 dB. On each optimal route, the red, blue, and green segments represent climb, cruise, and descent, respectively.

![Fig. 16](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr16.jpg)

Download: Download high-res image (2MB)

![Fig. 17](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr17.jpg)

Download: Download high-res image (2MB)

We can make some general observations from the results shown in and. First, when UAM aircraft cruise at a higher altitude, the cruise segment is less affected by the no-fly zones. At 2,000 ft MSL, the cruise path (blue line) can have a longer straight portion and detour less around the no-fly zones. This is because cruising at a high altitude is generally an effective way to mitigate UAM noise emissions. In contrast, at a lower cruising altitude, such as 1,000 ft MSL, the cruise path typically covers a longer distance. From the perspective of energy consumption, there is a trade-off because both climbing to a higher altitude and traveling a longer distance lead to increased energy consumption. Second, when the noise requirement is more stringent, such as +5 dB above the local ambient level, there will be less airspace available for UAM to operate at the same altitude, leading to longer travel distances. This observation allows planners to consider a trade-off between the system’s efficiency and its environmental impact.

## 6\. Conclusions

In this paper, we presented a data-driven approach to designing noise-aware UAM airspace, facilitating more efficient low-noise flight path planning in complex urban environments and promoting unified urban airspace management schemes. The model outputs an overall no-fly zone that combines the physical no-fly zones for urban terrain avoidance with the noise no-fly zones for noise emission mitigation. The proposed approach integrates an aircraft noise model with GIS technology and several high-quality urban geospatial and spatio-temporal datasets, reflecting various significant aspects of how urban residents respond to UAM noise emissions. We also developed a tailored path planning algorithm, informed by flight profile information, that can be used on the proposed airspace concept. The representative computation results demonstrated how important factors, such as noise requirements and time of day, could influence the configuration of the airspace and the resulting optimal flight trajectory.

This study is one of the first to rigorously integrate an urban analytics component into UAM airspace design and create noise no-fly zones on a citywide scale. In its current shape, the framework still has some limitations that open up future avenues to make the model more complete. First, the current study primarily focused on controlling ground noise. Moving forward, the framework can also incorporate building facades as target locations to manage UAM noise emissions. This could be important for cities with numerous high-rises and would require additional models, such as the sound transmission loss model across building facades, building materials information, and advanced acoustic models. Second, the noise-aware airspace design can also be informed by UAM network information. With the network data, one can apply similar approaches to create noise-aware 3D flight corridors for UAM operations, resulting in a more structured airspace.

## CRediT authorship contribution statement

**Jun Young Park:** Writing – review & editing, Writing – original draft, Visualization, Validation, Software, Methodology, Investigation, Formal analysis, Data curation. **Subin Kim:** Writing – review & editing, Writing – original draft, Visualization, Validation, Investigation, Formal analysis, Data curation. **Samiksha Khemka:** Writing – original draft, Visualization, Validation, Investigation, Formal analysis. **Cheuk Yan Lee:** Writing – review & editing, Writing – original draft, Visualization, Validation, Software, Methodology, Investigation, Formal analysis, Data curation. **Zhenyu Gao:** Writing – review & editing, Writing – original draft, Visualization, Supervision, Software, Resources, Project administration, Methodology, Data curation, Conceptualization.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgement

This work was jointly supported by the Department of Mechanical and Aerospace Engineering at The Hong Kong University of Science and Technology (HKUST) and the Research Grants Council (RGC) of Hong Kong through the Early Career Scheme (ECS) under project number 26219325. The opinions, findings, conclusions, or recommendations expressed in this material are solely those of the authors and do not necessarily reflect the views or policies of the project sponsor. The authors thank the Hong Kong Environmental Protection Department (EPD) for providing high-quality ground traffic noise data to support this study. Additionally, the authors thank Dr. Nawar Halabi, the developer of Noise Map, for providing the Hong Kong aviation noise data, although this dataset was not ultimately used in the study.

## Data availability

Data will be made available on request.

## References

- ### Towards Sustainable Urban Mobility: An ESG-Based Decision Framework for Urban Air Integration
	2026, Sustainability Switzerland

Common Spatial Data Infrastructure (CSDI), [https://portal.csdi.gov.hk/csdi-webpage/](https://portal.csdi.gov.hk/csdi-webpage/)

Open Geospatial Data in HK, [https://opendata.esrichina.hk/](https://opendata.esrichina.hk/)

Environmental Protection Department. The Government of the Hong Kong SAR.

DATA.GOV.HK, [https://data.gov.hk/en/](https://data.gov.hk/en/)

Land Utilization in Hong Kong, [https://www.pland.gov.hk/pland\_en/info\_serv/open\_data/landu/](https://www.pland.gov.hk/pland_en/info_serv/open_data/landu/)

[^3]

Hong Kong EPD, Noise Criteria, [https://www.epd.gov.hk/epd/noise\_education/web/ENG\_EPD\_HTML/m2](https://www.epd.gov.hk/epd/noise_education/web/ENG_EPD_HTML/m2)

[View Abstract](https://www.sciencedirect.com/science/article/abs/pii/S1270963826000313)

[^1]: ## 1\. Introduction

The emergence of urban air mobility (UAM) is anticipated by many to transform urban transportation and services. Enabled by advancements in aircraft design, battery technologies, air traffic management systems, and innovative business models, UAM will utilize small aerial vehicles like electric vertical take-off and landing (eVTOL) aircraft and unmanned aerial vehicles (UAVs) to operate at lower altitudes within or across metropolitan areas. Networked UAM operations will support various urban services, including air taxi services, medical supply transport, environmental monitoring, public safety, and emergency response. This new system offers distinct advantages in time-sensitive services and promoting public welfare in underserved regional communities.

Despite all these features and advantages, integrating UAM into current urban environments is a significant challenge. Urban integration of UAM faces several substantial constraints, including community acceptance of aircraft noise, safety concerns, supporting infrastructure, and air traffic control (ATC),,. Among these constraints, aircraft noise has been identified as a particularly significant factor, exhibiting the highest severity level across all UAM development stages,. Urban noise is already a growing problem with significant social and economic consequences,, and whether UAM noise can be effectively managed will determine if the system can be implemented and sustained in cities around the world. Mitigating UAM’s noise emissions has thus become a top research priority within the aerospace community in recent years,,.

Operations planning, including noise-aware flight trajectory planning, has been a crucial method in aviation for mitigating aircraft noise emissions, as it is necessary regardless of the noise magnitude at the source or the availability of advanced noise reduction aircraft technologies,. Apart from the complex noise-centric flight trajectory optimization, researchers have recently been exploring UAM noise control within the context of proper airspace design for two main reasons. First, noise-aware airspace design can simplify flight trajectory planning by converting noise constraints in urban environments into no-fly zones, allowing flights to achieve satisfactory noise control by simply operating outside these zones. Second, urban airspace management itself is an important problem, as several UAM safety,, and societal considerations (e.g., noise, privacy, perceived risk ) for UAM system planning can be framed as airspace management problems. The current noise-aware urban airspace design problems primarily focus on integrating acoustic and urban terrain models to define airspace sectors that are sufficiently distant from buildings and other objects on the ground.

A significant research gap lies in the fact that noise-aware urban airspace design should be informed by urban analytics techniques, given that UAM operates in a complex urban space and community noise impact is determined by urban residents’ responses to UAM noise emissions. This is made possible by modern smart city initiatives that are focused on developing intelligent functions to synthesize data for enhancing efficiency, equity, sustainability, and quality of life in urban areas,. In this study, we begin to address this gap by contributing to the integration of urban analytics elements for designing city-scale, noise-aware urban airspace that facilitates low-noise planning for UAM operations. Specifically, our urban analytics component integrates:
- •
	High-quality urban geospatial datasets (e.g., ground traffic noise, land use, population density, building heights, and noise-sensitive locations).
- •
	A spatio-temporal model of urban ambient noise, which accounts for hourly variations based on data from rigorous peer-reviewed studies.
- •
	A model of community noise response based on U.S. Environmental Protection Agency (EPA) guidelines, which defines acceptable noise levels as a function of the difference between UAM noise and the local ambient noise level.

With a background review presented in, the proposed model described in and combines geographic information system (GIS) techniques, high-quality urban geospatial and spatio-temporal datasets, along with an aircraft noise model to produce combined physical and noise no-fly zones. In, we introduce a flight profile-informed 3D path planning algorithm, HFPI-A\*, designed to efficiently plan a flight path that takes into account no-fly zones and flight performance constraints. In and, we implement the modeling and planning approach in a case study in Hong Kong. The representative computational results illustrate how key factors, such as noise requirements and time of day, can affect the configuration of the airspace and the resulting optimal flight trajectory.

## 2\. Background

### 2.1. UAM operational constraints

Although UAM offers numerous benefits to urban life and development, its integration into complex urban settings poses significant challenges. An important lesson from the past is that urban helicopter services in places like New York City led to unsustainable operations due to critical challenges in community acceptance, safety, and financial viability. Recently, researchers from North America and Europe conducted thorough analyses and pinpointed key operational challenges to implementing and scaling up a UAM system,,. In summary, the five key operational constraints of UAM are: (1) community acceptance of aircraft noise, (2) safety concerns, (3) availability of takeoff and landing areas (TOLAs), (4) scalability of ATC, and (5) ground and communication infrastructure. These operational constraints can become more prominent at various stages of UAM development. For instance, the availability of TOLAs and the scalability of ATC will pose significant challenges when the UAM system operates at a very high scale.

Among the key operational constraints of UAM, community acceptance of aircraft noise stands out as a particularly significant factor, with most careful studies repeatedly placing it among the top obstacles. Study identified aircraft noise as the only UAM operational constraint that consistently has the highest severity level across all UAM development stages. Study identified aircraft noise reduction as a challenge for UAM that requires the longest period to resolve. Even before UAM emerges, urban noise pollution is already a growing problem with considerable social and economic consequences. Because UAM operates in close proximity to urban residents, the range of noises generated by UAM aircraft poses significant health risks, including psychological discomfort, sleep disruption, and an increased risk of cardiovascular diseases. Consequently, addressing UAM’s noise impact has become a top priority for the community.

### 2.2. UAM noise and mitigation

Mitigating UAM aircraft noise has become a leading focus of research within the aerospace community. In general, we can achieve noise reduction by: (i) developing advanced quiet aircraft components to lessen noise at the source, and (ii) utilizing noise-aware operations planning to decrease the noise footprint during flight. Since breakthroughs in low-noise aircraft design technologies may take time to develop and mature, noise-aware flight operations planning is an indispensable approach for noise mitigation in UAM. In commercial aviation, noise abatement trajectories, such as the continuous descent approach (CDA) and the noise abatement departure procedures (NADP) have been widely studied. Within the UAM domain, the majority of related efforts have concentrated on low-noise flight trajectory planning and air traffic flow management for both eVTOL aircraft and small drones,. Noise-aware flight trajectory planning aims to create 2D or 3D flight paths that avoid populated areas and buildings on the ground,. These planning methods often rely on aircraft noise models from advanced numerical simulations to predict the noise patterns of UAM aircraft in complex urban environments,.

Noise-aware flight trajectory planning can be computationally demanding, as it involves an iterative process that uses both aircraft noise models and numerical optimization algorithms to determine the optimal aircraft trajectory. Another key challenge is that the trajectory planning process must eventually also take into account other considerations, such as safety and privacy, which further increases the complexity of the problem. To tackle these challenges, a newly proposed paradigm addresses low-noise flight trajectory planning through urban airspace design,. The core idea is to transform noise constraints in a complex urban environment into no-fly zones, making the trajectory planning process essentially a barrier avoidance problem, similar to avoiding the urban physical terrain. This airspace-based approach not only improves the computational efficiency of noise-aware trajectory planning but also simplifies the multi-objective trajectory planning problem, as other constraints can also be converted into no-fly zones. The vital role of airspace design in ensuring sustainable and safe operations makes it a crucial problem in UAM development.

### 2.3. Research gap

UAM’s operation in complex urban environments necessitates airspace design and operations planning processes that incorporate urban analytics to promote the system’s community acceptance. For instance, an effective solution for mitigating UAM’s community noise annoyance must integrate geospatial and urban data with models that describe how urban residents react to UAM noise. However, despite the abundance of powerful urban data generated by smart data initiatives worldwide, the integration of urban analytical components into community-friendly UAM airspace design is still insufficiently addressed in the current literature. In this work, we aim to advance data-driven, community-friendly UAM airspace design, focusing on low-noise UAM operations.

## 3\. Data and models

### 3.1. The overall approach

We present a data-driven approach to constructing 3D airspace that facilitates low-noise UAM path planning and promotes community-friendly urban airspace management. illustrates the core components of the proposed approach. Overall, the approach employs urban geospatial data analytics, aircraft noise model, policy requirements, and constrained optimization to achieve the following two outcomes:
- •
	**Noise-aware 3D airspace design:** this part will determine the 3D sectors in urban airspace where UAM operations are prohibited, known as no-fly zones. The noise-aware 3D airspace design involves constructing two types of no-fly zones: physical and acoustic. The physical no-fly zone is straightforward and universal, requiring aircraft to maintain a certain clearance distance from obstacles like mountains and buildings. The green box in shows that we form the physical no-fly zone using urban terrain data, building height data, and minimum clearance information.
	The acoustic no-fly zone is a central focus of this study. Unlike the physical no-fly zone, the acoustic no-fly zone is a virtual concept that aircraft must also avoid to limit community noise impact. The purple box in illustrates that ambient noise estimation and aircraft noise model are the two major components in computing the acoustic no-fly zone. We leverage ambient noise level information and its distribution to better plan noise-aware UAM operations because: (1) as will be discussed in, UAM community noise annoyance is a function of noise difference above the local ambient noise level, and (2) ambient noise masking–concentrating flights over less noise-sensitive areas–is a well-recognized strategy for mitigating UAM’s noise impact. Modeling the acoustic no-fly zone involves using multiple urban geospatial and spatio-temporal datasets, in addition to noise requirements. The combined no-fly zone, depicted in the blue box in, results from the union of physical and acoustic no-fly zones.
- •
	**Airspace- and performance-constrained path optimization:** this part essentially addresses how to plan an optimal flight path by incorporating no-fly zone information. Common practices involve finding the shortest path outside the no-fly zone that connects an origin to a destination. Nevertheless, a UAM aircraft path planning problem is further constrained by aircraft performance and flight profile. A typical flight profile for eVTOL aircraft includes five segments: vertical takeoff, climb, cruise, descent, and vertical landing. In addition, each segment has some performance constraints, such as the rate of climb and descent. A realistic UAM flight path must consider not only restricted airspace but also aircraft flight profile and performance limitations. We will present a modified optimal path planning algorithm that can account for both important considerations.

![Fig. 1](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr1.jpg)

Download: Download high-res image (690KB)

### 3.2. Datasets and data integration

The urban datasets used in the proposed approach must comprehensively cover the key aspects of low-noise urban airspace design. provides a summary of nine identified datasets, using Hong Kong as a case study. These datasets come from government databases, like the Hong Kong government database, or open geospatial data sources, such as Esri.

Table 1. Summary of relevant datasets identified in this study.

| Dataset Number | Dataset Name | Source(s) | Used in This Study |
| --- | --- | --- | --- |
| 1 | Ground Traffic Noise Data | Hong Kong Environmental Protection Department (EPD) | Y |
| 2 | Land Use Zonings Data | Esri China Hong Kong | Y |
| 3 | Digital Terrain Model (DTM) Data | Hong Kong Common Spatial Data Infrastructure (CSDI) | Y |
| 4 | Building Height Data | Esri China Hong Kong | Y |
| 5 | Population Density Data | Esri China Hong Kong | Y |
| 6 | Noise Sensitive Locations Data | Esri China Hong Kong | Y |
| 7 | Building Height Control Areas Data | Esri China Hong Kong | N |
| 8 | Aviation Noise Data | Noise Map Global Noise Dashboard | N |
| 9 | Temporal Noise Data | Journal Papers, | Y |

Of the nine datasets identified in, seven are used in this study. Six of these (datasets 1–6) are urban geospatial datasets that cover ground traffic noise, land use zoning, digital terrain model (DTM), building height, population density, and noise-sensitive locations. visualizes the six geospatial datasets within the selected area of Hong Kong. The building height control areas data (dataset 7) is not used because the building height data (dataset 4) provides more precise information. The aviation noise data (dataset 8) is not used because it is less direct for evaluating ground ambient noise. The final dataset, temporal noise data, describes how ground noise changes throughout the day and is sourced from two journal papers. In the following, we outline the details of each dataset and the data processing method.

![Fig. 2](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr2.jpg)

Download: Download high-res image (2MB)

#### 3.2.1. Ground traffic noise data

The ground transportation noise data shown in (a) is provided by the Hong Kong Environmental Protection Department (EPD). It describes the calculated L <sub>10</sub>, the noise level exceeded for 10% of the time during a 1 h measurement period, at 4 PM during the traffic peak hour, measured at a height of 4 m. The use of L <sub>10</sub> to describe traffic noise stems from extensive research that found L <sub>10</sub> correlates well with community response. It was adopted in developed countries like the UK as the eligibility criterion for acoustic insulation. The data format is GeoTIFF, which includes geo-referencing capabilities within the traditional tagged image file format (TIFF). This format is supported by various GIS software, including the tool used for data integration in our study. Similar datasets exist globally, such as the National Transportation Noise Exposure Map in the United States,. Ground transportation noise is the major contributor to urban ambient noise and will be used in this study as the main source for estimating the ambient noise distribution in the city.

#### 3.2.2. Land use zoning data

The land use zoning data shown in (b) shows the broad land use zoning within the Planning Scheme Area of Outline Zoning Plans in Hong Kong. The source data in Shapefile format is a subset of the Digital Planning Data made available by the Town Planning Board under the Hong Kong Government. This original dataset includes a relatively large number of land use types. For example, under ‘residential area,’ there are five subcategories with even more detailed groups. Based on the Land Utilization in Hong Kong (LUHK) released by the Planning Department of Hong Kong, we consolidated a group of 12 land use types as the definitive list for this project: Water Bodies, Transportation, Residential, Recreation, Industrial, Conservation, Comprehensive Development Area, Commercial, Agriculture, Open Space, Other Specified Uses, and Government or Institution.

Land use zoning data plays a key role in UAM noise management, as different land use zones have varying daily noise levels and standards. For example, the Hong Kong EPD has established the categorization of noise Area Sensitive Rating (ASR) and the corresponding Acceptable Noise Levels (ANLs) for different areas. In addition, existing research in the literature contains typical noise levels for these standard land use zones. We utilize noise data from major cities, including Manchester, Wuhan, and Tainan,, to establish typical noise levels for the 12 zones, with emphasis on the noise levels observed during the afternoon period, which corresponds to the time of peak activity within the city. presents the 12 consolidated land use types and their minimum, maximum, and average noise levels in decibels (dBA).

Table 2. Consolidated land use types and their noise levels in dBA.

| Zone Number | Category | *L* <sub>min</sub> | *L* <sub>max</sub> | *L* <sub>avg</sub> |
| --- | --- | --- | --- | --- |
| 1 | Water Bodies | 47.5 | 82.5 | 65.5 |
| 2 | Transportation | 46.0 | 84.0 | 71.6 |
| 3 | Residential | 41.5 | 79.0 | 62.2 |
| 4 | Recreation | 40.0 | 82.0 | 61.9 |
| 5 | Other Specified Uses | 41.5 | 81.5 | 60.0 |
| 6 | Open Space | 46.0 | 84.0 | 71.6 |
| 7 | Industrial | 41.5 | 79.8 | 62.5 |
| 8 | Government or Institution | 48.0 | 79.5 | 66.5 |
| 9 | Conservation | 47.5 | 82.5 | 65.5 |
| 10 | Comprehensive Development Area | 41.5 | 81.5 | 60.0 |
| 11 | Commercial | 68.0 | 78.0 | 74.0 |
| 12 | Agriculture | 37.5 | 82.5 | 60.5 |

#### 3.2.3. Digital terrain model data

The Digital Terrain Model (DTM) data shown in (c) is a digital terrain model of Hong Kong from the 2020 LiDAR Survey. It shows the topography of the Hong Kong terrain (including non-ground features like elevated roads and bridges) in a 5-meter raster grid with an accuracy of plus-minus 5 m. DTM data is the primary source for modeling the natural physical terrain and the physical no-fly zones.

#### 3.2.4. Building height data

The building Height Data shown in (d) shows the building locations of buildings in Hong Kong. It is a dataset provided by the Lands Department under the Hong Kong Government. The source data is in Shapefile format, with top height information linked to each building’s shape data. This dataset is crucial for establishing physical no-fly zones, ensuring UAM operations maintain adequate clearance distances from buildings in the city.

#### 3.2.5. Population density data

The population density data is derived from the 2021 Hong Kong Population Census Statistics by District Council Constituency Area, as shown in (e). This dataset contains the boundaries of the 452 District Council Constituency Areas and provides statistics on demographic, household, educational, economic, housing, and internal migration characteristics of the Hong Kong population, offering benchmark data on the population’s socio-economic traits. To compute the population density of each Constituency Area, one divides its total population by its area.

#### 3.2.6. Noise sensitive locations data

Noise-sensitive locations include hospitals, schools, nursing homes, etc. In this study, we include the locations of hospitals in Hong Kong, as shown in (f). It is a subset of the geo-referenced public facility data provided by the Hospital Authority under the Hong Kong government. The design approach will apply the strictest noise criteria to hospitals.

#### 3.2.7. Temporal noise data

One limitation of the ground transportation noise data in (a) and the land use zone noise levels in is that they only represent noise levels during the afternoon peak hour at 4 PM. It is widely recognized that urban ambient noise fluctuates throughout the day. Consequently, there is a necessity for an additional data source to model the general temporal patterns of urban ambient noise.

We identified two studies in the literature that collected data to model the temporal patterns of urban noise in East Asia. The first study provides comprehensive hourly measurements of A-weighted decibel noise levels at 14 different roads in Foshan, China, which were used as one of their multiple data sources for mapping the spatiotemporal distribution of traffic noise. The second study provides comprehensive hourly noise monitoring data collected by the Taipei City Government from 24 noise measurement points. Using 4 PM as the reference point, displays the main hourly noise variation patterns reported in and. There is a good overall agreement between the mean trends from the two studies, as shown by the blue and red curves in. In this study, we use the mean results from the two studies, represented by the purple curve in, to model the hourly ambient noise variation in Hong Kong. Given the limitations for more precise spatiotemporal ambient noise modeling, we assume that this temporal pattern applies uniformly across all locations within our area of investigation.

![Fig. 3](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr3.jpg)

Download: Download high-res image (247KB)

#### 3.2.8. Data integration and processing

This step integrates the six main urban geospatial datasets shown in into a single environment and converts them into formats suitable for computations. The collected datasets exhibit format inconsistencies, with some datasets in shapefile format containing both geometric and attribute data, as shown in (a), while others were in raster image format, as illustrated in (b), or point data formats. This necessitated standardization processing to achieve format uniformity. Furthermore, the datasets utilize different coordinate reference systems, necessitating extensive processing to transform their geometric references to a standardized system. We carried out this geospatial standardization using ArcGIS software tools together with Python programming language.

![Fig. 4](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr4.jpg)

Download: Download high-res image (732KB)

After determining the definitive study region (mainly Kowloon Bay and Hong Kong Island), we implemented a standardized grid system in ArcGIS to facilitate consistent spatial analysis, using the WGS 1984 Web Mercator (auxiliary sphere) as the coordinate reference system. Within this spatial framework, we established a 200  ×  200 cell fishnet, as illustrated in, for data aggregation. We customize data aggregation methods to suit the characteristics of each dataset, typically adopting a more conservative analytical approach. For building height and DTM data, we use the maximum height value to represent physical terrain constraint for each cell; the predominant land use category to denote the zoning classification of a cell; and the minimum recorded value to represent transportation noise within the cell.

![Fig. 5](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr5.jpg)

Download: Download high-res image (1MB)

The standardization process converts all geospatial datasets into 200  ×  200 matrices, ensuring that all entries are prepared for subsequent computations. visualizes these post-processed geospatial datasets in a uniform numeric format. We will utilize these geospatial data matrices, along with an aircraft noise model and policy requirements regarding noise and clearance distance, to construct a noise-aware 3D airspace for the Hong Kong region.

![Fig. 6](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr6.jpg)

Download: Download high-res image (1014KB)

The richness and reliability of the integrated geospatial data are critical to the framework’s robustness. The seven core datasets provide a diverse representation of urban physical, acoustic, and social dimensions. Data reliability is upheld through the use of authoritative sources and a conservative aggregation strategy within a standardized 200x200 grid, employing maximum values for physical features and minimum values for noise to ensure prudent no-fly zones.

### 3.3. Aircraft noise model

The aircraft noise model is an indispensable part of this noise-aware airspace design approach. In the aviation community, practitioners model the community noise impact of aircraft in urban and suburban areas using a standard known as noise-power-distance (NPD) data, which describes the relationship between an aircraft’s noise level and its slant distance to an object. For a specific aircraft type, the NPD data is obtained from either noise certification tests or controlled tests conducted in accordance with rigorous international standards. Currently, NPD data is available for the majority of fixed-wing aircraft and helicopter types operated around the world.

Since UAM operations will involve eVTOL aircraft, a new aircraft configuration, there is currently no existing data or test results available for developing NPD data. Consequently, researchers develop NPD data through a combination of acoustic modeling and flight simulation. illustrates some core concepts in this process. Researchers begin with an eVTOL aircraft configuration (shown in (a)), conduct acoustic modeling to generate its noise hemisphere (shown in (b)), which captures the 3D directivity of noise near the aircraft configuration, and ‘fly’ the aircraft in a simulation environment (shown in (c)) to generate the sound exposure level (SEL) NPD data for three operational modes: level flyover (L), departure (D), and approach (A).

![Fig. 7](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr7.jpg)

Download: Download high-res image (600KB)

In this study, we fit a logarithmic regression model to a set of NPD data published by NASA researchers for their Revolutionary Vertical Lift Technology (RVLT) vehicle concept,, as shown in (a). For each combination of operational mode (L, D, A) and measurement position (centerline, side), the regression model takes the following functional form:(1) $N \left(d\right) = a_{0} + a_{1} log_{10} d + a_{2} \left(log_{10} d\right)^{2}$ where *N* represents noise in A-weighted SEL and *d*  ∈ \[200, 20000\] denotes distance in ft. displays the goodness-of-fit for the six NPD regression models, plotted alongside the original data points. presents the coefficients for the six NPD regression models.

![Fig. 8](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr8.jpg)

Download: Download high-res image (291KB)

Table 3. Coefficients for the NPD regression models.

| Operational Mode + Measurement Position | *a* <sub>0</sub> | *a* <sub>1</sub> | *a* <sub>2</sub> |
| --- | --- | --- | --- |
| Mode L (Level Flyover) - Centerline | 88.09 | 3.21 | −2.62 |
| Mode L (Level Flyover) - Side | 78.01 | 7.26 | −3.39 |
| Mode D (Departure) - Centerline | 84.05 | 8.76 | −4.18 |
| Mode D (Departure) - Side | 77.34 | 11.34 | −4.72 |
| Mode A (Approach) - Centerline | 93.35 | 5.17 | −2.86 |
| Mode A (Approach) - Side | 85.55 | 6.83 | −3.14 |

### 3.4. Community noise response

The management of noise pollution in urban communities is a complex problem that requires a systematic approach. Any rigorous treatment of this issue should acknowledge that different communities within the city have varying degrees of noise sensitivity. Urban communities display varying levels of noise acceptance due to two factors: (1) land use, and (2) the different ambient noise levels. Ambient noise in urban spaces encompasses the background sounds generated by a variety of sources, including transportation, construction, human activities, and natural phenomena. In fact, ambient noise plays a crucial role in predicting community responses to UAM noise.

The U.S. Environmental Protection Agency (EPA) conducted a comprehensive study to evaluate community reactions to noise exposure. presents the findings of a related study that models expected community reactions based on noise emission levels exceeding the ambient noise, specifically the ‘additional’ noise generated by an activity. The result indicates that community annoyance increases as the noise difference above the local ambient level rises. When the noise emission from UAM operations reaches 10 dB above the ambient level, widespread complaints are likely to occur. When the difference increases to 20 dB, the community’s response may escalate to threats of legal action. Therefore, our proposed approach incorporates ambient noise as a key factor in assessing spatio-temporal noise sensitivity throughout the city.

Table 4. Expected community annoyance as a function of the difference between noise emission and ambient noise levels (source: ).

<table><thead><tr><th>Expected Community Reaction</th><th colspan="2">Difference Between Noise Emission Level and Ambient Noise Level in dB</th><th>Approx. % Very Much Annoyed</th><th>Approx. % Little or Not Annoyed</th></tr><tr><td>Empty Cell</td><th>Mean</th><th>Range</th><td>Empty Cell</td><td>Empty Cell</td></tr></thead><tbody><tr><td>No reaction</td><td>2</td><td>0 to 8</td><td>20</td><td>45</td></tr><tr><td>Sporadic complaints</td><td>6</td><td>3 to 8</td><td>26</td><td>37</td></tr><tr><td>Widespread complaints</td><td>11</td><td>7 to 19</td><td>37</td><td>26</td></tr><tr><td>Threats of legal action</td><td>21</td><td>18 to 24</td><td>60</td><td>14</td></tr><tr><td>Vigorous action</td><td>28</td><td>23 to 34</td><td>87</td><td>7</td></tr></tbody></table>

## 4\. Airspace design results

### 4.1. Key concepts

In this section, we introduce the 3D airspace construction process and present prototypes of noise-aware airspace designs under various conditions. The overarching objective is to create 3D noise-informed no-fly zones that UAM flyover operations must avoid in order to limit noise exposure on the ground. There are two critical points here. First, our current objective is to control the ground noise impact of UAM operations. Ground noise is not only the most critical noise issue in urban spaces, but it also represents a scenario where urban residents are directly exposed to noise emissions without any sheltering effect. Second, we aim to control flyover noise, as it is the dominant segment of the flight profile and can simplify this new airspace concept at this stage.

In, we distinguish the four 3D airspace model concepts through data visualizations. Each ‘box’ in contains the full range of investigation on the x-y plane and an altitude range from 0 to 3,000 ft (or 1,000 m) mean sea level (MSL), corresponds to the altitude range in which UAM is expected to operate.
- 1.
	**Digital terrain model (DTM):** shown in (a), this is a digital model of the bare earth surface in the Hong Kong area, excluding most buildings and other man-made structures.
- 2.
	**The building no-fly zone:** shown in (b), adding on the DTM, the light green region incorporates all buildings and other man-made structures in the Hong Kong area, as well as the no-fly zones centered around these buildings. Here, we set the minimum clearance distance as 250 ft above any building. Result in (b) is the ’physical’ no-fly zone.
- 3.
	**The noise no-fly zone:** shown in (c), adding on the DTM, the yellow 3D sectors are the noise no-fly zones, which is a virtual concept for noise control. We will compute the noise no-fly zones by integrating all geospatial data matrices, the temporal noise model, the aircraft noise model, and policy analyses. The interpretation of this concept is straightforward: UAM flyovers must operate outside the noise no-fly zones.
- 4.
	**The combined no-fly zone:** shown in (d), represents the union of the two no-fly zone sets: physical and noise. This represents the overall no-fly zone for both objective avoidance and noise control purposes. This also serves as the basis for noise-aware flight path planning.

![Fig. 9](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr9.jpg)

Download: Download high-res image (1MB)

### 4.2. Modeling procedure

Since all geospatial datasets are in the same matrix format, we denote the representation of the noise no-fly zone as $N \left(t\right) = \left[N_{i j} \left(t\right)\right]_{i = 1 , \ldots , n , j = 1 , \ldots , m}$, where *N <sub>ij</sub>* (*t*) refers to the minimum flyover altitude at the ground region in the *i* th row and *j* th column of the matrix *N* at time *t*.

We start by estimating the urban ambient noise level. We let matrix *G* denote the ground transportation noise at 4 PM and matrix *L* denote the average land use noise at 4 PM. We combine these two aspects as estimate the spatial distribution of ambient noise in the city as:(2) $\mathbf{\mathit{A}} = max \left\{\mathbf{\mathit{G}} , \mathbf{\mathit{L}}\right\}$

Subsequently, we incorporate the temporal dimension into the ambient noise estimation. We convert the mean temporal model displayed in as a normalized factor *T* (*t*) such that $T \left(t = 16\right) = 1$, i.e., the ambient noise matrix *A* is original at 4 PM (1600). Then, the spatio-temporal model of urban ambient noise is:(3) $\mathbf{\mathit{A}} \left(t\right) = \mathbf{\mathit{A}} \cdot T \left(t\right)$

We next incorporate noise-sensitive locations. In this study, we primarily consider hospitals as noise-sensitive areas where more stringent noise regulations must be applied. For each hospital, we consider its exact location along with the eight adjacent entries surrounding it as noise-sensitive locations in the matrix. This results in a binary matrix *S*, where 0 indicates noise-sensitive locations and 1 indicates all other locations. Since we are using the difference between UAM noise emissions and the local ambient noise level as the primary method to quantify community noise annoyance, we denote the allowable noise increase as Δ *N*. For noise-sensitive locations, we ensure that UAM noise emissions do not exceed the local ambient noise level. Therefore, the matrix representing the permitted noise levels is:(4) $\mathbf{\mathit{P}} \left(t\right) = \mathbf{\mathit{A}} \left(t\right) + \Delta N \cdot \mathbf{\mathit{S}}$

Now, we consider the impact of population density on community noise response. We let matrix *D* denote the population density in the city and the median population density $\overset{\sim}{D}$ as a reference value. In, we see that as the noise difference increases, a larger percentage of the population becomes annoyed. Population density further enables the calculation of the number of people who become annoyed, which is proportional to the product of Δ *N* and *D*. When using the total annoyed population as the standard, the density-corrected permitted noise levels are:(5) $\mathbf{\mathit{P}}_{D} \left(t\right) = \mathbf{\mathit{A}} \left(t\right) + \left(\Delta N \cdot \overset{\sim}{D}\right) \cdot \mathbf{\mathit{S}} \oslash \mathbf{\mathit{D}}$ where *S* ⊘ ***D*** denotes the Hadamard division between *S* and *D*. indicates that the noise increase should be smaller for communities with higher population density.

Finally, we integrate the aircraft noise model. The NPD model *N* (*d*) described in represents noise as a function of distance. We choose the Mode L, the more conservative centerline coefficients for modeling the flyover noise, $N_{L - c} \left(d\right)$. In our airspace design problem, we require a noise model that describes ground clearance distance as a function of permitted noise, specifically $d = N_{L - c}^{- 1} \left(P\right)$. We calculate the noise-centric minimum flyover distance above the ground as:(6) $\mathbf{\mathit{N}} \left(t\right) = N_{L - c}^{- 1} \left(\mathbf{\mathit{P}}_{D} \left(t\right)\right)$

We further apply a max pooling operator, used in convolutional neural networks (CNNs), to the *N* (*t*) above. Specifically, we apply a 2  ×  2 max pool filter which selects the maximum value within each 2  ×  2 region. This aims to: (1) consider and mitigate flyover noise in adjacent cells, and (2) incorporate local feature invariance into the noise no-fly zone. With max pooling, we have:(7) $\mathbf{\mathit{N}}^{'} \left(t\right) = \text{MaxPool} \left(\mathbf{\mathit{N}} \left(t\right)\right)$

Similarly, we also construct a representation for the physical no-fly zone by combining the DTM and building height data. Let matrices *E* and *B* denote the heights of the Earth’s surface and man-made structures, respectively. Since matrix *B* is measured in above ground level (AGL) altitude, the heights of the man-made structures are given by $max \left(\mathbf{\mathit{B}} - \mathbf{\mathit{E}} , \mathbf{\mathit{O}}\right)$, where *O* is the *m* -by- *n* matrix of zeros. With the requirement of minimum vertical clearance distance Δ *h*, the physical no-fly zone representation above the ground is:(8) $\mathbf{\mathit{H}} = max \left(\mathbf{\mathit{B}} - \mathbf{\mathit{E}} , \mathbf{\mathit{O}}\right) + \Delta h \cdot \mathbf{\mathit{J}}$ where *J* is a *m* -by- *n* matrix of ones. The representation of the physical and noise combined no-fly zone, adding on the DTM, is:(9) $\mathbf{\mathit{C}} \left(t\right) = \mathbf{\mathit{E}} + max \left(\mathbf{\mathit{N}}^{'} \left(t\right) , \mathbf{\mathit{H}}\right)$

In the next two subsections, we will carry out the data-driven modeling procedure and generate noise no-fly zone results under various conditions.

### 4.3. Under different noise requirements

We first examine the impact of noise requirements (an element in the purple box in, and Δ *N* in ) on the height and volume of no-fly zones. Regarding a reasonable range for noise increase above the local ambient level, Study () investigated from zero to $\Delta N = \text{approx}. 30$ dB; Study set $\Delta N = 30$ dB as the absolute maximum noise impact within a relevant context. In this study, we vary Δ *N* from 5 dB to 25 dB. shows the noise no-fly zone results under varying noise requirements, with the time of day fixed at 4 PM, the afternoon peak hour. We observe that under the most permissive noise requirement, 25 dB above the ambient noise level, as shown in (a), the upper boundaries of the noise no-fly zones are very close to the ground. This indicates that with relaxed noise requirements, UAM can operate within a wider airspace and fly closer to the ground surface. As the noise requirements become more stringent, from 25 dB to 5 dB above the ambient level, the no-fly zones expand, reducing the space available for UAM operations. Consequently, above the same location UAM flights must maintain a greater distance from the ground to mitigate noise impact.

![Fig. 10](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr10.jpg)

Download: Download high-res image (1MB)

### 4.4. Under different times of a day

We then examine the temporal effects of the noise no-fly zone. Because urban ambient noise exhibits temporal patterns and varies throughout the day, the space within the noise no-fly zone changes even with the same noise requirements. presents the noise no-fly zone results at six representative times of the day: 12 AM, 3 AM, 9 AM, 12 PM, 4 PM, and 9 PM, with the noise requirement fixed at 15 dB above the ambient level, which is a median level. (c) shows that at $t = 9$ AM, during the morning rush hour, there is more space available for UAM operations due to the high ground ambient noise. During late night and early morning hours, such as midnight and 3 AM, the heights of the noise no-fly zones are elevated, resulting in less space for UAM operations. Overall, the results presented in and align with the general expectations of the concept.

![Fig. 11](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr11.jpg)

Download: Download high-res image (1MB)

## 5\. The airspace-enabled low-noise path planning

This noise-aware airspace design concept is intended to enhance the more efficient low-noise UAM flight path planning and promote a more integrated urban ATM framework via airspace management. In this section, we present a preliminary solution for utilizing the noise-aware airspace concept in practical UAM path planning.

### 5.1. The flight profile-informed path planning algorithm

This path planning problem is an optimal pathfinding problem that is subject to two distinct types of constraints. First, the flight path must avoid all no-fly zones to ensure sufficient clearance from urban terrain and maintain limited ground noise emission. To navigate outside the no-fly zones, the flight path can either fly above or bypass a specific prohibited 3D sector in the airspace. When flight distance or time are the primary measures of operational efficiency, finding the shortest path from A (the origin) to B (the destination) while avoiding no-fly zones can be effectively addressed using existing methods like the A\* algorithm,.

Second, constraints also arise from the aircraft’s flight profile and performance limits, requiring the fusion of flight profile information into the path planning process. A flight profile consists of distinct segments, each with specific performance characteristics that a mission must adhere to. illustrates the five segments of a standard eVTOL aircraft flight profile ‘from vertiport to vertiport,’ which include vertical takeoff, climb, cruise, descent, and vertical landing. Among the performance limits in a flight profile, the most prominent ones affecting path planning are the rate of climb (RoC) and rate of descent (RoD). For example, when considering the RoC, the flight path angle *γ* during climb may not exceed a certain threshold. Study suggested this limit to be $tan \left(\gamma\right) = 1 / 5$.

![Fig. 12](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr12.jpg)

Download: Download high-res image (128KB)

We propose a Hybrid Flight Profile-Informed A\* algorithm (HFPI-A\*) to efficiently plan a flight path that incorporates no-fly zone and flight profile information. The HFPI-A\* has the following core ideas for integrating flight profile information:
- •
	Plan by segments: instead of planning the entire path from vertiport to vertiport in one go, the algorithm plans each segment separately. For the two vertical segments, eVTOL aircraft ascend and descend vertically between the ground and 250 ft AGL. The main algorithm focuses on the climb, cruise, and descent segments, as shown in.
	![Fig. 13](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr13.jpg)
	Download: Download high-res image (333KB)
- •
	Performance constrained space discretization: For planning purposes, the entire airspace is discretized into 3D cells. The discretization on the x-y plane is established during the geospatial data processing step and is illustrated in. illustrates the options for directional movement in a vertical plane. When the aircraft is in the central cell, it can move to the eight surrounding cells in the same vertical plane, which include two vertical movements, two diagonal ascent movements, two diagonal descent movements, and two horizontal movements. In Discretization(*γ <sub>c</sub>*, *γ <sub>d</sub>*), the airspace is vertically divided into 3D cells with a height of Δ *h <sub>c</sub>*, resulting in a diagonal movement angle $\gamma = min \left\{\gamma_{c} , \gamma_{d}\right\}$. This ensures that every diagonal ascent/descent movement is achievable in relation to the rate of climb/descent.
	![Fig. 14](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr14.jpg)
	Download: Download high-res image (124KB)
- •
	A\* functions with distinct movement options: Options for directional movement are crucial in pathfinding algorithms like A\*. In 3D space, each cell has 26 adjacent cells to move to, similar to the center of a 3-by-3 cube. In our path planning problem, we must further customize the directional movement options based on the nature of each segment. For climb and descent, vertical movements violate the performance definitions and are not permitted. A customized A\* function, AStarClimbDescent(s, e), incorporates the remaining 24 directional movements and is designed for both climb and descent segments, where s and e denote the start and end points of the path, respectively.For cruise segments, the aircraft should maintain its current altitude. A specialized A\* function, AStarCruise(s, e), restricts movement to only the 8 horizontal directions.
- •
	Cone search for climb and descent paths: Both climb and descent segments link the vertical operations ceiling with the cruising altitude *h*, as illustrated in. Because we use plan by segments, identification of the two key connecting points is essential to the approach. We let *p <sub>cr</sub>* denote the connecting point between climb and cruise, and *p <sub>rd</sub>* the connecting point between cruise and descent. Due to the no-fly zones, *p <sub>cr</sub>* and *p <sub>rd</sub>* may not align along the straight line connecting the origin and destination. Therefore, to identify a connecting point, we start from the vertical operations ceiling and conduct a 360-degree search along the circumference where the cone, constrained by RoC/RoD, intersects with the cruising altitude plane. In the ConeSearch(s, *h*), we evaluate a set of 8 points (with angles of 0 <sup>∘</sup>, 45 <sup>∘</sup>, 90 <sup>∘</sup>, etc.) on the circumference and select the feasible connecting point that is nearest to the destination. also illustrates the cone search process.

details the complete HFPI-A\* algorithm for path planning under no-fly zones and flight profile information. The final output *P* is the shortest flight path that satisfies all the conditions mentioned above.

![Algorithm 1](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-fx1.jpg)

Download: Download high-res image (536KB)

### 5.2. Low-noise path planning results

In the end, we apply the HFPI-A\* plath planning algorithm to the noise-aware airspace designs and investigate the landscape of 3D low-noise flight trajectories in complex urban environments. We select two UAM routes in Hong Kong for illustrative purposes. As shown in, route 1 connects Lamma Island to Sai Kung, and route 2 connects Tung Tau Wan to Tsuen Wan.

![Fig. 15](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr15.jpg)

Download: Download high-res image (409KB)

and display the path planning results for route 1 and route 2, respectively. Note that the blue no-fly zones represent the combined no-fly zones that account for both noise and urban physical terrains. For each route, we conduct path planning at three cruising altitudes: 1,000 ft, 1,500 ft, and 2,000 ft MSL, as well as three noise increase levels: +5 dB, +10 dB, and +20 dB. On each optimal route, the red, blue, and green segments represent climb, cruise, and descent, respectively.

![Fig. 16](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr16.jpg)

Download: Download high-res image (2MB)

![Fig. 17](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr17.jpg)

Download: Download high-res image (2MB)

We can make some general observations from the results shown in and. First, when UAM aircraft cruise at a higher altitude, the cruise segment is less affected by the no-fly zones. At 2,000 ft MSL, the cruise path (blue line) can have a longer straight portion and detour less around the no-fly zones. This is because cruising at a high altitude is generally an effective way to mitigate UAM noise emissions. In contrast, at a lower cruising altitude, such as 1,000 ft MSL, the cruise path typically covers a longer distance. From the perspective of energy consumption, there is a trade-off because both climbing to a higher altitude and traveling a longer distance lead to increased energy consumption. Second, when the noise requirement is more stringent, such as +5 dB above the local ambient level, there will be less airspace available for UAM to operate at the same altitude, leading to longer travel distances. This observation allows planners to consider a trade-off between the system’s efficiency and its environmental impact.

## 6\. Conclusions

In this paper, we presented a data-driven approach to designing noise-aware UAM airspace, facilitating more efficient low-noise flight path planning in complex urban environments and promoting unified urban airspace management schemes. The model outputs an overall no-fly zone that combines the physical no-fly zones for urban terrain avoidance with the noise no-fly zones for noise emission mitigation. The proposed approach integrates an aircraft noise model with GIS technology and several high-quality urban geospatial and spatio-temporal datasets, reflecting various significant aspects of how urban residents respond to UAM noise emissions. We also developed a tailored path planning algorithm, informed by flight profile information, that can be used on the proposed airspace concept. The representative computation results demonstrated how important factors, such as noise requirements and time of day, could influence the configuration of the airspace and the resulting optimal flight trajectory.

This study is one of the first to rigorously integrate an urban analytics component into UAM airspace design and create noise no-fly zones on a citywide scale. In its current shape, the framework still has some limitations that open up future avenues to make the model more complete. First, the current study primarily focused on controlling ground noise. Moving forward, the framework can also incorporate building facades as target locations to manage UAM noise emissions. This could be important for cities with numerous high-rises and would require additional models, such as the sound transmission loss model across building facades, building materials information, and advanced acoustic models. Second, the noise-aware airspace design can also be informed by UAM network information. With the network data, one can apply similar approaches to create noise-aware 3D flight corridors for UAM operations, resulting in a more structured airspace.

## CRediT authorship contribution statement

**Jun Young Park:** Writing – review & editing, Writing – original draft, Visualization, Validation, Software, Methodology, Investigation, Formal analysis, Data curation. **Subin Kim:** Writing – review & editing, Writing – original draft, Visualization, Validation, Investigation, Formal analysis, Data curation. **Samiksha Khemka:** Writing – original draft, Visualization, Validation, Investigation, Formal analysis. **Cheuk Yan Lee:** Writing – review & editing, Writing – original draft, Visualization, Validation, Software, Methodology, Investigation, Formal analysis, Data curation. **Zhenyu Gao:** Writing – review & editing, Writing – original draft, Visualization, Supervision, Software, Resources, Project administration, Methodology, Data curation, Conceptualization.

[^2]: | Dataset Number | Dataset Name | Source(s) | Used in This Study |
| --- | --- | --- | --- |
| 1 | Ground Traffic Noise Data | Hong Kong Environmental Protection Department (EPD) | Y |
| 2 | Land Use Zonings Data | Esri China Hong Kong | Y |
| 3 | Digital Terrain Model (DTM) Data | Hong Kong Common Spatial Data Infrastructure (CSDI) | Y |
| 4 | Building Height Data | Esri China Hong Kong | Y |
| 5 | Population Density Data | Esri China Hong Kong | Y |
| 6 | Noise Sensitive Locations Data | Esri China Hong Kong | Y |
| 7 | Building Height Control Areas Data | Esri China Hong Kong | N |
| 8 | Aviation Noise Data | Noise Map Global Noise Dashboard | N |
| 9 | Temporal Noise Data | Journal Papers, | Y |

[^3]: Land use zoning data plays a key role in UAM noise management, as different land use zones have varying daily noise levels and standards. For example, the Hong Kong EPD has established the categorization of noise Area Sensitive Rating (ASR) and the corresponding Acceptable Noise Levels (ANLs) for different areas. In addition, existing research in the literature contains typical noise levels for these standard land use zones. We utilize noise data from major cities, including Manchester, Wuhan, and Tainan,, to establish typical noise levels for the 12 zones, with emphasis on the noise levels observed during the afternoon period, which corresponds to the time of peak activity within the city. presents the 12 consolidated land use types and their minimum, maximum, and average noise levels in decibels (dBA).

Table 2. Consolidated land use types and their noise levels in dBA.

| Zone Number | Category | *L* <sub>min</sub> | *L* <sub>max</sub> | *L* <sub>avg</sub> |
| --- | --- | --- | --- | --- |
| 1 | Water Bodies | 47.5 | 82.5 | 65.5 |
| 2 | Transportation | 46.0 | 84.0 | 71.6 |
| 3 | Residential | 41.5 | 79.0 | 62.2 |
| 4 | Recreation | 40.0 | 82.0 | 61.9 |
| 5 | Other Specified Uses | 41.5 | 81.5 | 60.0 |
| 6 | Open Space | 46.0 | 84.0 | 71.6 |
| 7 | Industrial | 41.5 | 79.8 | 62.5 |
| 8 | Government or Institution | 48.0 | 79.5 | 66.5 |
| 9 | Conservation | 47.5 | 82.5 | 65.5 |
| 10 | Comprehensive Development Area | 41.5 | 81.5 | 60.0 |
| 11 | Commercial | 68.0 | 78.0 | 74.0 |
| 12 | Agriculture | 37.5 | 82.5 | 60.5 |

[^4]: We identified two studies in the literature that collected data to model the temporal patterns of urban noise in East Asia. The first study provides comprehensive hourly measurements of A-weighted decibel noise levels at 14 different roads in Foshan, China, which were used as one of their multiple data sources for mapping the spatiotemporal distribution of traffic noise. The second study provides comprehensive hourly noise monitoring data collected by the Taipei City Government from 24 noise measurement points. Using 4 PM as the reference point, displays the main hourly noise variation patterns reported in and. There is a good overall agreement between the mean trends from the two studies, as shown by the blue and red curves in. In this study, we use the mean results from the two studies, represented by the purple curve in, to model the hourly ambient noise variation in Hong Kong. Given the limitations for more precise spatiotemporal ambient noise modeling, we assume that this temporal pattern applies uniformly across all locations within our area of investigation.

![Fig. 3](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr3.jpg)

Download: Download high-res image (247KB)

[^5]: In this study, we fit a logarithmic regression model to a set of NPD data published by NASA researchers for their Revolutionary Vertical Lift Technology (RVLT) vehicle concept,, as shown in (a). For each combination of operational mode (L, D, A) and measurement position (centerline, side), the regression model takes the following functional form:(1) $N \left(d\right) = a_{0} + a_{1} log_{10} d + a_{2} \left(log_{10} d\right)^{2}$ where *N* represents noise in A-weighted SEL and *d*  ∈ \[200, 20000\] denotes distance in ft. displays the goodness-of-fit for the six NPD regression models, plotted alongside the original data points. presents the coefficients for the six NPD regression models.

![Fig. 8](https://ars.els-cdn.com/content/image/1-s2.0-S1270963826000313-gr8.jpg)

Download: Download high-res image (291KB)

Table 3. Coefficients for the NPD regression models.

| Operational Mode + Measurement Position | *a* <sub>0</sub> | *a* <sub>1</sub> | *a* <sub>2</sub> |
| --- | --- | --- | --- |
| Mode L (Level Flyover) - Centerline | 88.09 | 3.21 | −2.62 |
| Mode L (Level Flyover) - Side | 78.01 | 7.26 | −3.39 |
| Mode D (Departure) - Centerline | 84.05 | 8.76 | −4.18 |
| Mode D (Departure) - Side | 77.34 | 11.34 | −4.72 |
| Mode A (Approach) - Centerline | 93.35 | 5.17 | −2.86 |
| Mode A (Approach) - Side | 85.55 | 6.83 | −3.14 |