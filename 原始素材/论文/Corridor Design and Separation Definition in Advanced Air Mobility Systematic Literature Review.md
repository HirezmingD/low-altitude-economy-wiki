---
title: "Corridor Design and Separation Definition in Advanced Air Mobility: Systematic Literature Review"
source: "https://ieeexplore.ieee.org/document/11493558"
author:
published:
created: 2026-07-01
description: "Advanced Air Mobility (AAM) uses electric vertical take-off and landing (eVTOL) vehicles to address urban congestion and emissions. However, corridor design, op"
tags:
  - "clippings"
---
## Abstract:

Advanced Air Mobility (AAM) uses electric vertical take-off and landing (eVTOL) vehicles to address urban congestion and emissions. However, corridor design, operation ma...

---

CCBY - IEEE is not the copyright holder of this material. Please follow the instructions via https://creativecommons.org/licenses/by/4.0/ to obtain full-text articles and stipulations in the API documentation.

Urbanization is increasing pressure on existing transportation infrastructure. As cities continue to expand, traditional transportation systems struggle to keep up with increasing demand. Advanced Air Mobility (AAM) is the next-generation passenger and cargo air transportation (e.g., flying taxi) paradigm incorporating such advancements as remotely piloted, autonomous, or vertical take-off and landing (VTOL) aircraft. This includes those powered by electric (i.e., eVTOLs) or hybrid-electric propulsion. The AAM “corridor” is defined as an air route within the airspace linking two vertiports and designed for safe and efficient movement of eVTOLs. The corridor can be geometrically represented as three dimensional airspace regions with defined horizontal and vertical limits within which the movement of eVTOLs are permitted. Among the most compelling advantages, AAM can reduce congestion, lower emissions, and enhance sustainability in urban environments, offering a cleaner and more effective alternative to traditional surface-based transport. The government and commercial sectors are investing in AAM to enhance the overall mobility of urban environments that are becoming increasingly congested and to shift the development towards smart, sustainable cities.

The recent research focus on AAM resulted in several survey papers exploring various dimensions of its implementation and integration into existing transportation systems. Based on an extensive analysis of papers, we have categorized these studies into following themes: Air Mobility Overview and Evolution, Market Demand and Economic Analysis, Airspace and Corridor Organization, Ground Infrastructure and Vertiports, and Safety&Security Concerns.

Several contributions provide comprehensive overviews of AAM. Straubinger et al. \[1\] offer a broad overview of Urban Air Mobility (UAM - a subset of AAM), discussing vehicle-related aspects, operational concepts, market structures, and public acceptance. Similarly, Cohen et al. \[2\] describe the evolution of AAM, emphasizing phased development and potential barriers such as regulatory environments and public acceptance. The integration of UAM into multimodal transportation systems is discussed through research initiatives like the German Aerospace Center’s HorizonUAM project \[3\].

Understanding market demand and economic viability is essential for assessing the potential success of AAM services as evidenced by demand analyses \[4\], \[5\], meta-analyses comparing AAM with Electric and Autonomous Vehicles \[6\], and comprehensive reviews of AAM ecosystems \[7\]. Moreover, the authors of \[8\] provide an evaluation of AAM policies from four different countries highlighting that, while AAM policy development happening globally is in its infancy, the United Arab Emirates has the most developed regulatory framework.

Airspace design studies examine the structural aspects necessary for efficient and safe AAM operations. A multi-layered air corridor structure and traffic flow rules (intersections, engagement rules) are explored in \[9\]. Bauranov and Rakas \[10\] analyze urban airspace design concepts. Additionally, Nithya et al. \[11\] address operational complexities in urban airspace related to wind flow influencing the corridor design.

Ground infrastructure, particularly vertiports, is critical for the successful implementation of AAM systems. Several works review literature on UAM ground infrastructure, focusing on the guidelines for vertiport design \[12\], \[13\]. Marvraj et al. \[14\] offer an overview of AAM ground-based infrastructure, highlighting take-off and landing sites, maintenance facilities, energy supply, and regulatory frameworks, highlighting the need for a holistic perspective on infrastructure challenges.

The systematic literature review in \[15\] focuses on air taxi safety and security, and reviews advances in techniques and architectures to ensure safe and autonomous operations. Bauranov \[10\] also touches upon safety factors within airspace design, though not as comprehensively as in \[15\].

**Limitations of the State of the Art:** Despite the extensive coverage provided by the surveys, only two systematic literature reviews \[14\], \[15\] have been conducted using the recognized Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) framework. The majority of other papers, while insightful, use methodologies that i) do not permit the reproduction of results and ii) have a higher risk of bias, limiting their utility for systematic analysis of AAM and consequent regulatory advice.

Beyond these methodological concerns, several gaps exist in the current research literature:

1. **Lack of an Integrated Framework:** Existing studies often focus on individual aspects of AAM, such as vehicle-related factors, airspace design, or ground infrastructure, without offering a unified framework that integrates vertiport network design, corridor formulation, operation management, and separation definitions. This fragmentation hinders a holistic understanding of the interactions between these components.
2. **Insufficient Taxonomies and Structured Approaches:** While some literature provides overviews, there is a lack of comprehensive taxonomies that cover all essential factors for AAM corridor design. This limitation restricts the ability to systematically address the challenges involved in deploying AAM systems.
3. **Inadequate Exploration of Operational Management Strategies:** Existing studies often overlook advanced strategies for dynamically aligning flight demand with available capacity, such as corridor and vertiport management techniques, which are crucial for maintaining operational efficiency and reliability.
4. **Underdeveloped Separation Definition Factors:** Current research frequently considers existing separation standards defined for commercial and general aviation. This oversight can lead to conservative safety standards hindering higher-density AAM operations.

**Beyond the State of the Art:** We focus on AAM corridor design and separation definition as the core research dimensions because they connect ground infrastructure to daily flight operations. While vertiports act as the isolated nodes, the corridors form the physical links (requiring complex spatial and environmental considerations), and separation definitions define the operational capacity within those links. Without a systematic understanding of how to structure these routes and safely distance the vehicles within them, the holistic integration of vertiports and flight operations remains impossible. Given these interconnected challenges, this Systematic Literature Review (SLR) is both timely and essential. To address the identified research gaps, we employed a PRISMA-based methodology, drawing on the Context, Intervention, Mechanism, and Outcome (CIMO) framework to formulate research questions that target the key technological, environmental, and societal factors shaping these airspace structures. This approach aims to minimize bias, ensure reproducibility, and synthesize a broad range of recent studies. Our review seeks to establish comprehensive taxonomies for AAM design factors and propose an integrated framework that unifies vertiport network design, corridor formulation, operation management, and separation standards. The complete methodology, including search strategies, selection criteria, and quality assessment protocols, is detailed in Section II. The review results are presented in Section III while Section IV provides insights on missing factors and under-investigated areas.

This study presents a Systematic Literature Review conducted in accordance with the PRISMA 2020 guidelines \[16\] to ensure transparency, replicability, and comprehensive reporting. The objective of this SLR is to systematically identify, evaluate, and synthesize research findings related to the design and separation methodologies of AAM corridors for passenger and freight eVTOLs (flying cars) in urban environments. In the following text, we (i) provide a high-level overview of the methodology and (ii) detail the PRISMA-based selection procedure.

### A. Methodology Overview

#### 1) Overview of the Systematic Review Process

The SLR process (Fig. 1) comprises three main phases: (i) Identification, (ii) Screening, and (iii) Eligibility. Upon the formulation of research questions, the identification phase defines the search strategy, including the choice of data sources and extraction methods for collecting relevant papers. The screening and eligibility phases outline the inclusion and exclusion criteria aligned with the specific requirements and scope of the review, where papers are filtered based on titles and abstracts (screening) and full-text (eligibility). The answers to the research questions are then synthesized, while the challenges, opportunities, and limitations are highlighted.

[![FIGURE 1. - Flow Diagram for the selection of the literature reviewed.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog1-3686509-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog1-3686509-large.gif)

**FIGURE 1.**

Flow Diagram for the selection of the literature reviewed.

The search process represented by the flowchart in Fig. 1 resulted in a total of *2039* articles from IEEE Xplore and Web of Science databases. After the removal of *90* duplicate records, *1949* unique papers remained. Out of these, *1774* studies were excluded during the title and abstract screening phase as they did not fulfill the inclusion criteria, primarily due to irrelevance to the research questions, focus on non-urban areas, or not addressing passenger or heavy freight eVTOL-related topics.1 This screening process retained *175* studies for full-text review. Subsequently, *113* of these were excluded after inspecting full texts. Thus, finally, only *62* studies (see the full list in Appendix A) have been selected for inclusion in the current review and are summarized in the following sections. The selection process took approximately three months to complete.

#### 2) Geographical Distribution of Author Affiliations

Fig. 2 presents statistics of the selected papers. In total, researchers from 16 countries contributed to 62 selected papers (Fig. 2a). Thirty papers were authored by researchers based in the USA, while 11 papers were written by South Korean researchers. Germany, the UK, China, and France each contributed between 4 to 6 papers. South America is represented by Brazil (3) and Colombia (1), the Middle East by the UAE (1), ASEAN by Singapore (2) and Australia (1).

[![FIGURE 2. - Distribution of included papers.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog2-3686509-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog2-3686509-large.gif)

**FIGURE 2.**

Distribution of included papers.

Approximately one half of the papers (37) presented a realistic case study of an AAM deployment in a city. As observed in Fig. 2b, most of the case studies considered the USA (18) followed by countries like South Korea (7), Germany (3), and China (3), underlining the extensive geographical coverage of AAM research.

The relevant papers have been published from 2018 onwards, as illustrated in Fig. 2c. The USA, South Korea, and Germany have consistently published studies since 2018, reflecting sustained interest and investment in AAM technologies. In contrast, China only began contributing actively starting in 2023, indicating a recent surge in research activity within the country. The highest number of papers was published in 2023, while a relatively large number of related publications have been recorded for 2024. The trend of increasing interest is evident, despite only one paper being published in 2020, which can be attributed to the COVID-19 pandemic’s impact on research activities.

#### 3) Research Themes

Thematic analysis of the selected papers reveals that the majority focus on various aspects of AAM operation design, divided into three primary phases: vertiport location definition, corridor formulation, and operational design (including scheduling and dynamic conflict management). These themes account for approximately three fourths of the studies reviewed. Conversely, the investigation of separation distances between eVTOLs is less prevalent, constituting about one fourth of the papers. This indicates a potential area for future research to ensure the safety and efficiency of advanced air mobility systems.

#### 4) Publication Venues

Of the 62 selected studies, 24 were published in peer-reviewed journals, while 38 were presented at conferences. The most prominent journal is *Transportation Research Part C: Emerging Technologies* by Elsevier, which accounts for 4 papers. Among the conferences, the *IEEE/AIAA Digital Avionics Systems Conference (DASC)* is the leading venue with 19 papers, followed by the *Integrated Communications, Navigation and Surveillance Conference* with 8 papers.

### B. Review Steps

Fig. 3 shows the systematic review steps: specifying research questions, designing the search strategy, screening studies, assessing quality, extracting data, and analyzing findings. Each of these blocks is detailed in the text below where we discuss the procedures and decisions made at every stage.

[![FIGURE 3. - Methodology of the systematic review process.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog3-3686509-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog3-3686509-large.gif)

**FIGURE 3.**

Methodology of the systematic review process.

#### 1) Research Questions (RQs)

The SLR methodology requires well-formulated research questions. In this work, we rely on the CIMO framework (Context, Intervention, Mechanism, and Output) to define the research questions for our methodological study. Therefore, the research questions devised for this systematic review are:

- **RQ1:** In urban areas (Context), what technical, environmental, and societal factors (Mechanism) influence the design (Intervention) of AAM corridors (Outcome) for eVTOLs (flying cars)?
- **RQ2:** In urban areas (Context), what technical, environmental, and societal factors (Mechanism) influence the definition (Intervention) of separation distances (Outcome) for eVTOLs (flying cars)?
- **RQ3:** In urban areas with eVTOL operations (Context), what quantitative methodologies (Mechanism) are used to define (Intervention) safe separation distances (Outcome) for eVTOLs (flying cars)?

These key questions have been formulated to guide the systematic review to understand the factors influencing design and operational parameters of AAM corridors for passenger or freight transportation in urban settings. Moreover, this paper seeks to present a comprehensive taxonomy of the factors, highlighting gaps and opportunities for future research.

#### 2) Search Strategy

To address the research questions, we conducted a comprehensive search using two scientific databases: IEEE Xplore and Web of Science (WoS). These databases were selected due to their extensive coverage of peer-reviewed journals and conference proceedings in the fields of engineering, technology, and applied sciences, which are important to the study of AAM.

The search for relevant publications was initiated on $26{^{\text {th}}}$ of May 2024, with updates for any additional papers finalized on $19{^{\text {th}}}$ of June 2024. Using the research questions, a set of keywords and queries were formulated tailored to the search syntax and requirements of each database. A combination of keywords ’ *VTOL* ’, ’ *Vertical Take-Off and Landing* ’, ’ *air mobility* ’, ’ *UAM* ’, ’ *U-SPACE* ’, ’ *UTM* ’, ’ *AAM* ’, ’ *urban airspace* ’, ’ *air taxi* ’, ’ *flying car* ’, ’ *corridor* ’, ’ *separation distance* ’, ’ *separation* ’, ’ *airspace design* ’, ’ *traffic management* ’, ’ *flight path* ’, ’ *route* ’, ’ *trajectory* ’, ’ *flight corridor* ’, ’ *air traffic management* ’, ’ *conflict* ’, ’ *collision* ’, and ’ *navigation* ’ was employed.

All searches were limited to the “journal” and “conference” document types. After completing the first draft of the search strings, pilot searches were conducted in each database to evaluate their effectiveness in retrieving relevant studies. Effectiveness was assessed based on the relevance and number of retrieved papers. Given that WoS and IEEE Xplore support different wildcard characters (’\*’ for WoS and ’?’ for IEEE), the search strings were slightly adjusted to conform to each database’s syntax. Through iterative testing and refinement, the placement and combination of wildcards were optimized to increase the number of papers, ensuring a comprehensive collection of relevant literature. The final search time frame covered publications from January 2010 to June 2024.

The resulting search string used in WoS:

TS=((”\*VTOL\*” OR “Vertical Take-Off and Landing” OR “air mobility” OR “UAM” OR “U-SPACE” OR “UTM” OR “AAM” OR “urban airspace” OR “air taxi” OR “flying car\*”) AND (“corridor\*” OR “separation distance\*” OR “separation\*” OR “airspace design” OR “traffic management” OR “flight path\*” OR “route\*” OR “trajectory\*” OR “flight corridor” OR “air traffic management” OR “conflict” OR “collision\*” OR “navigation”)) AND (PY=(2010-2024))

The search string in IEEE Xplore:

(“All Metadata”:”?VTOL?” OR “All Metadata”:”Vertical Take-Off and Landing” OR “All Metadata”:”air mobility” OR “All Metadata”:”UAM” OR “All Metadata”:”U-SPACE” OR “All Metadata”:”UTM” OR “All Metadata”:”AAM” OR “All Metadata”:”urban airspace” OR “All Metadata”:”air taxi” OR “All Metadata”:”flying car?”) AND (“All Metadata”:”corridor?” OR “All Metadata”:”separation distance” OR “All Metadata”:”separation” OR “All Metadata”:”airspace design” OR “All Metadata”:”traffic management” OR “All Metadata”:”flight path” OR “All Metadata”:”route” OR “All Metadata”:”trajectory” OR “All Metadata”:”flight corridor” OR “All Metadata”:”air traffic management” OR “All Metadata”:”conflict” OR “All Metadata”:”collision?” OR “All Metadata”:”navigation”)

The initial search (Table 1) identified 2039 papers, 1116 of which were listed in the IEEE Xplore library and 923 in Web of Science.

**TABLE 1** Number of papers collected from each database.

[![Table 1- Number of papers collected from each database.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog.t1-3686509-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog.t1-3686509-large.gif)

#### 3) Study Selection

The collected papers from the initial search were screened according to the preset inclusion and exclusion criteria (Table 2). The paper selection process consisted of two phases. First, based on the inclusion and exclusion criteria, the papers were independently screened by two researchers through title and abstract screening. The publications selected during this phase were then independently assessed by two authors through full-text screening. The authors cross-checked the selection results and resolved any disagreements on the selection decisions. All disagreements in either phase were resolved by consensus.

**TABLE 2** Inclusion and exclusion criteria for paper selection.

[![Table 2- Inclusion and exclusion criteria for paper selection.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog.t2-3686509-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog.t2-3686509-large.gif)

The inclusion and exclusion criteria were formulated by the authors to effectively select relevant papers as summarized in Table 2.

#### 4) Risk of Bias and Quality Assessment

This systematic literature review adhered to the PRISMA 2020 guidelines to ensure a rigorous and unbiased selection of relevant literature. Recognizing that the selection of keywords and eligibility criteria can introduce bias, the authors implemented several strategies to minimize these risks:

1. **Independent Screening**: Two reviewers independently screened the titles and abstracts of all retrieved studies against the inclusion and exclusion criteria. This process was followed by an independent full-text review.
2. **Discrepancy Resolution**: Any disagreements between reviewers during the screening and selection phases were resolved through discussion or by involving a third reviewer to reach consensus.
3. **Comprehensive Quality Assessment**: To evaluate the quality and risk of bias in the included studies, the authors employed a quality assessment checklist inspired by the Critical Appraisal Skills Programme (CASP). The checklist included the following criteria:
	- **Clarity of Objectives**: Are the study objectives clearly stated?
		- **Methodological Rigor**: Are the research methods appropriately designed and executed?
		- **Data Reporting**: Are the results clearly reported, including measures of accuracy and confidence?
		- **Contribution to the Field**: Do the study’s findings offer significant insights, and do they adequately address the research questions?
		- **Limitations Acknowledgment**: Are the limitations of the study transparently discussed?
4. **Quality Categorization**: Each study was independently assessed by two reviewers, and scores were assigned based on the checklist.

Additionally, the review considered the potential for publication bias by including both journal and conference papers and by conducting a comprehensive search across multiple databases. A complete list of 62 selected studies with their bibliographic data is provided in Table 4 in Appendix A along with the CASP scores for each study..

**TABLE 3** Notional separation values \[77\].

[![Table 3- Notional separation values [77].](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog.t3-3686509-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog.t3-3686509-large.gif)

**TABLE 4** Comprehensive summary and quality assessment of selected papers.

[![Table 4- Comprehensive summary and quality assessment of selected papers.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog.t4-3686509-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog.t4-3686509-large.gif)

#### 5) Data Extraction

Relevant data were systematically extracted from the selected publications to facilitate comprehensive analysis and synthesis. The data extraction process was conducted using the *Rayyan* platform independently by two reviewers to minimize bias and ensure accuracy. The following data items were retrieved from each study:

- **Bibliographic Information**: Title, authors, year of publication, journal or conference name.
- **Study Characteristics**: Research objectives, methodology, data sources, type (case-study or theoretical).
- **Technical Aspects**: Specific technical factors addressed, technologies or frameworks used.
- **Environmental and Societal Factors**: Environmental considerations, societal impacts discussed.
- **Findings and Contributions**: Key results, conclusions, and contributions to the field.
- **Limitations**: Identified limitations or gaps in each study.

Data extraction was facilitated using a standardized extraction form developed in Excel, ensuring consistency across all studies.

#### 6) Data Synthesis and Analysis

The data extracted from the included studies were synthesized using a thematic analysis approach. This involved identifying and categorizing recurring themes, patterns, and relationships related to the research questions. The synthesis process included:

- **Thematic Coding**: Assigning codes to key concepts (e.g., distinct corridor design phases) and findings (factors) within each study.
- **Theme Development**: Grouping related codes into broader themes that address the research questions.
- **Integration of Findings**: Combining insights from multiple studies to provide a comprehensive understanding of the factors influencing AAM corridor design and separation distances.

#### 7) Limitations of the Methodology

While this SLR was conducted with rigorous methodological standards, several limitations should be acknowledged:

- **Language Restriction**: Only English-language studies were included, potentially excluding relevant research published in other languages.
- **Database Selection**: Although IEEE Xplore and Web of Science are comprehensive, relevant studies indexed in other databases may have been missed.
- **Publication Bias**: Despite efforts to include grey literature, the review primarily captures peer-reviewed publications, which may overrepresent positive or significant findings.
- **Temporal Limitation**: The search was conducted up to June 2024, and recent publications beyond this date were not included.
- **Subjectivity in Quality Assessment**: Although multiple reviewers were involved, some level of subjectivity in assessing study quality is inherent.

This section presents the findings of our systematic review, organized around the three research questions. Section III-A covers **RQ1**, detailing the technical, environmental, and societal factors that guide AAM corridor design. Section III-B addresses **RQ2**, examining which factors influence the definition of separation distances. Finally, Section III-C responds to **RQ3**, discussing the quantitative methodologies used to determine safe separation distances in urban eVTOL operations.

### A. RQ1: Corridor Design Factors

Corridor design for AAM operations involves multiple considerations spanning technical, environmental, and societal domains. The thematic grouping of the AAM corridor design papers revealed three distinct clusters related to the following three phases of AAM corridor design. Phase 1 addresses vertiport network design; Phase 2 focuses on corridor formulation, emphasizing feasibility, safety, and sustainability; and Phase 3 deals with operational management. This structure aligns with **RQ1** by revealing the core factors that guide effective corridor design in urban AAM.

To provide a quantitative overview of this specific landscape, Fig. 4 illustrates the distribution of the literature across these three phases. As shown, the majority of the reviewed literature focuses heavily on the Corridor formulation (28 papers), with a specific emphasis on Safety (23 papers), reflecting the immediate perceived bottlenecks for AAM integration.

[![FIGURE 4. - Distribution of literature focusing on various AAM design factors, reflecting current research priorities and perceived bottlenecks.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog4-3686509-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog4-3686509-large.gif)

**FIGURE 4.**

Distribution of literature focusing on various AAM design factors, reflecting current research priorities and perceived bottlenecks.

#### 1) Phase 1-Vertiport Network Design

Fig. 5 presents a taxonomy of design factors for selecting optimal vertiport locations. The location selection process is divided into four tasks:

1. **Assessing Demand for AAM** aims to define potential coarse vertiport locations (e.g., at the neighborhood level) by analyzing origin-destination patterns, transportation flows, and comparing AAM with existing transportation modes. This foundational assessment ensures that vertiport locations are strategically aligned with areas of high AAM demand.
2. **Evaluating Feasibility** focuses on fine-tuning potential vertiport positions by examining land availability, absence of physical obstacles, and the technical capabilities of the AAM aircraft. This evaluation guarantees that selected sites are practically viable and can support the operational requirements of AAM services.
3. **Considering Regulations** ensures that chosen locations comply with relevant airspace and aircraft regulations, noise restrictions, and other legal requirements, thereby facilitating smooth integration into existing frameworks.
4. **Analyzing Economic Viability** seeks to select the most suitable vertiport options by assessing both capital and operational expenses, ensuring the economic sustainability of the chosen locations.

[![FIGURE 5. - Taxonomy of design factors for selecting a candidate vertiport location.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog5-3686509-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog5-3686509-large.gif)

**FIGURE 5.**

Taxonomy of design factors for selecting a candidate vertiport location.

Collectively, these tasks provide a structured approach to identifying and validating vertiport sites that meet diverse criteria essential for successful AAM integration. Since the modifications in one task may change the output of other phases, several iterations may be required to find a stable solution.

##### a) Guidelines for Interpreting the Forest Plot:

To effectively interpret Fig. 5, it is essential to understand its hierarchical structure and the relationships between the nodes at different levels. Each parent node represents a broader category or concept identified in the literature, while the child nodes provide more detailed sub-factors derived from specific studies. For instance, under **Assessing Demand for AAM**, the parent node *“Zones \[30\]”* encompasses the general concept of zoning without detailed distinctions. This indicates that the cited paper \[30\] recognizes and utilizes the concept of zones in vertiport location selection without specifying the underlying criteria. However, when examining the child nodes such as *“Administrative districts \[27\], \[31\], \[32\]”* and *“Population density \[28\], \[33\]”*, it becomes evident that certain studies provide more granular definitions of the term “zone” based on specific factors. For example, the works \[27\], \[31\], \[32\] define zones based on administrative districts, while \[27\], \[30\] use population density as a defining criterion. This hierarchical representation highlights both general and specific applications within the vertiport location selection process, allowing readers to trace the origin of each factor and understand the varying levels of detail provided by different studies.

##### b) Explanation of Factors for Vertiport Location Definition:

Each of the four tasks in the vertiport location selection taxonomy encompasses a range of specific factors that collectively guide the decision-making process.

**Assessing Demand for AAM:** In this task, the primary focus is on understanding the demand for AAM services. First, transportation *Origin-Destination* (OD) pairs must be defined. Transport flow data derived from commute surveys \[22\], \[23\], \[24\], \[25\] and transportation datasets \[26\], \[27\], \[28\], \[29\] provide insights into existing movement patterns. These OD pairs can be grouped into Zones \[30\] to identify the most demanded areas. Zoning can be based on various factors, with the most common approaches utilizing administrative boundaries \[27\], \[31\], \[32\], population density \[28\], \[33\], household income \[22\], \[33\], and land category \[28\], \[31\].

Next, AAM is compared with *Other Transportation Modes* in terms of trip cost and trip time. Most studies focus on private cars \[23\], \[24\], \[30\], though taxi \[30\] and public transport \[31\] are also considered. The final trip cost includes price per mile and various fares \[31\]. Trip time is influenced by factors such as time-varying road congestion \[26\], \[31\], \[33\] and time spent on inter-modal transfers \[22\], \[28\], \[31\] (e.g., walking, cycling, car, taxi, shuttle, bus). Based on the projected passenger value of time, willingness to pay \[31\], \[33\] for AAM services can be assessed. It was concluded that willingness to pay in a zone is highly correlated with the density of wealthy populations \[33\].

**Evaluating Feasibility:** The primary objective of this task is to ensure that potential vertiport locations are not only situated in areas with high demand, but also in areas that are practical, physically and technically suitable to support AAM operations.

To evaluate *Available Locations*, the required vertiport size \[22\], \[29\], \[34\] must be defined based on the projected AAM demand. A detailed analysis of neighborhood categories and land use types should be performed \[22\], \[24\] to exclude areas where it is not possible to construct transportation infrastructure. Next, one should identify land available for sale \[22\] and exclude the areas where topography \[22\] does not allow for vertiport construction.

*No Obstacles* \[29\] are essential to ensure unobstructed flight paths and safe vertiport operations. As indicated by Rakas et al. \[35\], the AAM flight envelope depends on the *AAM Aircraft Capabilities*. Moreover, the selected aircraft must be able to travel the distance between vertiports and transport the required number of people. Additionally, aircraft dimensions and power requirements directly influence the design and layout of vertiport infrastructure.

**Considering Regulations:** This task aims at ensuring that chosen vertiport locations comply with all relevant regulatory frameworks.

*Airspace* regulations aim to maintain the safety and efficiency of existing aviation systems following the integration of AAM operations. One critical factor is the *Load on Air Traffic Control (ATC)* \[36\], which assesses the capacity of ATC systems to manage coordination between commercial aviation and AAM traffic around airports. Additionally, the presence of *No-fly Zones (NFZ)* \[24\], \[33\], \[34\], \[36\] must be considered to avoid restricted areas that could impede vertiport operations or conflict with existing airspace uses. Furthermore, maintaining *Separation from Other Aircraft* \[25\], \[36\] is essential to prevent mid-air collisions and ensure safe distances between AAM flights and other aviation traffic.

*Aircraft* regulations involve ensuring that AAM aircraft meet all required safety and operational standards set by aviation authorities \[35\]. Currently, there is no specified procedure for AAM aircraft certification; therefore, most studies rely on existing frameworks such as Title 14 of the Code of Federal Regulations (14 CFR) part 135 to assess compliance and operational readiness \[37\].

*Vertiport* regulations establish specific operational guidelines that vertiport facilities must adhere to. Existing work \[22\] References only legacy helipad regulations.

Lastly, *Noise* regulations focus on minimizing the environmental impact of AAM operations, particularly during the take-off and landing phases, which are the noisiest. It is important to note that permitted noise levels vary depending on the land use types of surrounding areas \[24\], necessitating careful consideration to ensure compliance and community acceptance.

**Analyzing Economic Viability:** In this task, the economical viability of the selected vertiport locations is inspected.

*Capital Expense (CAPEX)* involves the initial investments required to establish vertiport infrastructure and acquire necessary assets. Key components of CAPEX include New Infrastructure and Infrastructure Reuse. Investments in New Infrastructure depends on Land Cost \[22\], which includes the expenses related to acquiring land for vertiport construction. Additionally, the required Vertiport Capacity \[34\] defines the necessary land size and facilities needed to accommodate projected AAM demand. Finally, Aircraft Cost \[22\] represents the investment in acquiring AAM vehicles. On the other hand, it is possible to reduce CAPEX through Infrastructure Reuse \[23\], \[24\], \[29\]. This involves repurposing existing helipads, rooftop parking and other transportation facilities. Infrastructure reuse not only lowers CAPEX but also accelerates the deployment of vertiport services by utilizing pre-existing structures.

*Operational Expenses (OPEX)* include the ongoing costs associated with the daily functioning of AAM facilities. The first key component of OPEX is Operational Cost per Flight \[32\], which encompasses expenses related to fuel, maintenance, and staffing for each individual flight. Additionally, Vertiport Utilization \[31\] and Aircraft Utilization \[22\] are critical factors that influence OPEX. Efficient utilization of AAM fleet and vertiport infrastructure minimizes idle times and reduces operational costs. Finally, charges for each landing at the vertiport (so-called Landing Fees \[34\]) are another significant operational cost. Note that depending on the business model, these fees can also be seen as revenue generators rather than OPEX.

*Revenue* generation is a vital aspect of economic viability. Multiple papers \[29\], \[30\], \[32\] predict revenue based on Combined Passenger Fares collected from users for their AAM journeys.

#### 2) Phase 2-Corridor Formulation

Early papers considered the shortest path between the vertiports as the simplest approach to represent corridors with obvious limited applicability. Next, it was suggested to analyze historical data of helicopter flights to define de-facto existing corridors \[63\]. However, the expected scale of AAM operations called for a more holistic approach to defining potential corridors.

Fig. 6 illustrates a comprehensive taxonomy of design factors for formulating effective corridors in AAM systems. Given the vastness of airspace, the corridor formulation process employs a systematic approach to narrow down viable options by gradually removing unsuitable segments. This process is divided into three tasks:

1. **Feasibility** check aims at eliminating infeasible flight trajectories.
2. **Safety** check focuses on removing areas where flying is unsafe.
3. **Sustainability** assessment seeks to indicate corridor candidates that satisfy a broad range of sustainability requirements.

[![FIGURE 6. - Taxonomy of design factors for air corridor formulation.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog6-3686509-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog6-3686509-large.gif)

**FIGURE 6.**

Taxonomy of design factors for air corridor formulation.

Each task encompasses specific factors that collectively ensure the selection of optimal corridors capable of supporting safe, efficient, and environmentally responsible AAM operations.

**Feasibility:** The first task focuses on identifying and eliminating flight paths that are impractical or impossible for AAM operations.

Multiple contributions \[38\], \[39\], \[40\] indicate *Obstacles* as the primary factor to identify infeasible trajectories. Furthermore, obstacles can be categorized into static and dynamic obstacles. The static obstacles \[41\] include permanent physical barriers such as city and terrain that can be obtained from a Geographic Information System (GIS) \[42\] or reconstructed with on-board sensory equipment such as LiDAR \[43\]. On the other hand, dynamic obstacles \[40\], \[44\] refer to temporary or moving objects that can affect flight paths, necessitating (i) a strategic avoidance of these areas or (ii) real-time adjustments and continuous monitoring to maintain operational integrity.

*Aircraft Flight Capability* evaluates the technical performance of AAM aircraft to ensure they can operate effectively within the designated corridors. This can be done based on assessing the Flight Envelope \[24\], \[45\], \[46\], which describes the operational limits of the aircraft in terms of altitude, speed, and maneuverability. Alternatively, a more thorough approach can include the performance assessment for the aircraft sub-systems: propulsion \[40\], \[47\], control systems \[40\], \[44\], dynamics \[27\], \[38\], \[41\], \[42\], \[43\], \[44\], \[47\], \[48\], \[49\], and power systems \[40\], \[50\]. These sub-systems are vital for ensuring that AAM aircraft can reliably operate within the established flight corridors, maintaining performance standards and operational readiness.

**Safety:** The second task emphasizes the importance of safety by removing segments of airspace that pose risks to (i) other aircraft, (ii) ground, and (iii) passengers on board. This step is aligned with the *Safety* category and encompasses *Separation*, *Impact on the Ground*, and *Contingency* factors, respectively.

*Separation* ensures that AAM traffic maintains adequate distances from legacy aviation traffic, other AAM flights, and adds an extra safety margin to the static structures ensuring that the corridors are not only feasible but also pose no risk of collision. Separation from legacy traffic, such as commercial or general aviation, is a popular topic among researchers \[39\], \[49\], \[51\], \[52\], \[53\]. Sometimes it takes a form of adhering to established *No-fly Zones (NFZ)* \[50\], \[53\]. Separation from AAM Traffic involves establishing safety volumes around aircraft \[46\], \[54\] and managing corridor occupancy \[53\] that can be done via establishing no-fly zones \[46\], \[49\], \[54\], \[55\]. As it is expected to have a higher density of operating AAM aircraft around vertiports, several papers suggest provisioning of holding areas \[38\], \[56\] to prevent mid-air collisions and ensure safe operational distances.

*Impact on the Ground* addresses the potential risks associated with AAM operations affecting populated areas \[42\]. Early contributions \[24\], \[57\] favored flying over water (e.g., rivers) to minimize flying overhead people and, consequently, lower the ground risk. A more elaborate approach includes an assessment of casualty risk \[58\] that is defined by factors such as fall risk \[58\] and population density \[41\], \[58\]. Additionally, the casualty risk assessment can consider environmental factors such as sheltering provided by ground structures \[58\].

*Contingency* planning involves preparing for unforeseen events to ensure operational resilience. This includes assessing Communication and Navigation System (CNS) performance: Global Navigation Satellite System (GNSS) accuracy and availability \[42\], cellular communication coverage \[55\], \[59\], and the ability to deal with electromagnetic (EM) interference \[60\]. Following the EASA requirement, several papers consider the assignment of alternate landing sites \[40\], \[42\], \[45\]. Moreover, it is important to ensure maintaining a safe battery charge buffer \[40\] allowing for reaching the alternate landing site in case of emergency. Finally, weather must be considered. This can be done via introducing weather-induced no-fly zones \[27\], \[49\] or via considering effects of wind \[42\], \[45\], \[47\] and rain \[58\] on the AAM aircraft.

**Sustainability:** This task focuses on evaluating the long-term viability and environmental impact of the proposed AAM corridors. It deals with *Noise*, *Energy Efficiency*, and *Fairness* factors.

*Noise* management and the acoustic footprint of AAM operations is a well-studied topic. Early contributions \[24\], \[57\] favored flying over water (e.g., rivers) as this minimizes the number of people affected by noise. A more detailed approach considers noise-sensitive areas \[38\] (mostly defined by the area land use category) and precise acoustic propagation modeling taking into account Doppler shifts \[48\], effects introduced by urban environments \[61\] (multipath propagation, attenuation, diffraction etc.), and dependency on the rotor speed \[62\].

*Energy Efficiency* \[40\], \[45\] addresses the need for sustainable energy use in AAM operations, focusing on optimizing the aircraft energy consumption.

*Fairness* ensures equitable access to airspace among different operators \[43\]. This involves implementing policies that prevent monopolistic practices and ensure that all stakeholders have fair opportunities to utilize the corridors. On the other hand, different operations or corridors may have different priorities and requirements \[63\]. For example, the general public tends to better tolerate noise created by an AAM ambulance than by commercial or tourist flights \[64\].

#### 3) Phase 3-AAM Operations

Following the establishment of a vertiport network and the design of air corridors, the final phase focuses on ensuring the seamless and sustainable operation of AAM services. This phase is critical for maintaining the reliability and efficiency of AAM operations within the established infrastructure. Fig. 7 presents a taxonomy of factors essential for operational management in AAM systems. The operational phase is systematically divided into three primary tasks: **Flight Demand** assessment, **Capacity** estimation, and **Operations Management**. Each task depends on specific factors that collectively facilitate the efficient, reliable, and sustainable functioning of AAM operations. The first two tasks can also rely on the outputs of the previous design phases. For instance, the demand analysis should be performed in phase 1 while the projected capacity of vertiports and corridors can re-use results from phases 1 and 2, respectively.

[![FIGURE 7. - Taxonomy of design factors for AAM operations.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog7-3686509-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog7-3686509-large.gif)

**FIGURE 7.**

Taxonomy of design factors for AAM operations.

**Flight Demand:** This task involves assessing and forecasting the demand for AAM services to align operational capabilities with passenger needs and ensure optimal resource allocation. This assessment can be done based on *Commute demand*. Several papers \[25\], \[31\] calculate the AAM service demand as a percentage of the total transportation demand. The demand can also be predicted based on the proximity of potential users to vertiport locations and their behavioral patterns regarding AAM services \[65\]. Alternatively, *stochastic modeling* can be used toaccount for uncertainty in flight demand. By employing different distribution models such as uniform and Poisson \[56\], \[66\], and considering peak hours \[66\], \[67\], operators can better anticipate demand fluctuations. While this approach is less realistic, it gives more freedom for testing the AAM system behavior in unseen circumstances.

**Capacity:** The second critical task is capacity estimation, focusing on understanding the limits of the vertiports and corridor abilities.

*Vertiport capacity* encompasses both infrastructure and operational aspects. The infrastructure component involves evaluating the number of pads \[53\], \[66\], \[67\], \[68\], parking stalls \[31\], \[66\], \[69\], and charging facilities \[31\] to determine the vertiport’s ability to handle incoming and outgoing traffic. On the operational side, capacity can be influenced by the pad usage approach \[53\], \[66\], \[70\] in which a given pad can be exclusively used for landing or take-off (a safe choice) or the use can be allocated dynamically. Temporal factors such as time spent for taxiing, boarding, charging, and time spent on the pad \[31\], \[53\], \[69\], \[72\] also define the vertiport capacity. Another operational constraint is represented by Temporal separation between pad uses \[53\], \[56\], \[66\], \[70\], \[71\], \[72\]. Additionally, it is necessary to assess the probability of weather-induced vertiport closures \[69\].

*Corridor capacity* is defined by its configuration (geometry): distances for final approach fix points \[70\], \[71\] and number and locations of holding points \[68\], \[70\] will have an effect on capacity. Another factor limiting airspace capacity is dynamic no-fly zones \[45\], \[49\] implemented to avoid, for example, areas with adverse weather conditions. Moreover, the airspace capacity is highly dependent on the used reservation method. When a corridor is reserved for the whole duration of the flight \[66\], it will result in a lower capacity than in the case of a partial reservation \[25\] that can be implemented with a segment-based moving keep-out zone. Alternatively, reserving the corridor can be avoided by relying on time/space separation \[56\], \[70\], \[71\].

**Operations Management** Due to the dynamic nature of the AAM demand and capacity, the next task focuses on harmonizing them to ensure efficient and smooth AAM operations. Fig. 7 depicts the management task consisting of *Corridor Management* and *Vertiport Management*. The primary corridor management goal is to identify (assign) the corridor suitable for the requested flight. As discussed earlier, it may be done for the complete corridor or at the segment level \[25\]. This assignment task can be done based on the traffic density and complexity \[74\], \[76\]. Other corridor management actions include rerouting \[25\], \[45\], \[73\] (changing the corridor configuration) and repositioning \[31\], \[73\] (changing the target vertiport) flights \[25\], \[45\] in response to appearance of the dynamic no-fly zones and vertiport closures (due to weather or full occupancy), respectively.

The vertiport management includes arrival and departure management. Effective arrival scheduling must take into account the required time of arrival \[70\], \[71\], \[72\] and current vertiport occupancy \[31\]; prioritize flights with low battery levels \[70\], \[71\], \[76\]; and ensure safety via controlling the number of arrivals per time slot to maintain a safe and steady flow of incoming traffic \[66\], \[67\], \[68\].

Similarly, departure management focuses on flight authorization and mitigating departure delays \[67\], \[68\], \[76\], ensuring that departures are orderly and timely, thereby maintaining the overall efficiency of AAM operations.

### B. RQ2: Separation Definition Factors

Proper AAM separation standards are essential to ensure safety, prevent collisions, and optimize the use of airspace. It is widely accepted that the initial AAM operations will be performed by pilots following well-established Visual Flight Rules (VFR) or Instrument Flight Rules (IFR). In these cases, AAM will use the separation distances defined for Piloted Aircraft (PA) separations provided in Table 3 adapted from \[77\].2 However, matured AAM systems will require development of a new set of flight rules referred as Autonomous or Digital Flight Rules (AFR/DFR) relying on different separation standards that are still to be defined (highlighted in the table). Note that in order to minimize the effects on the conventional flights, VFR and IFR traffic is given right of way in every encounter with AFR flights.3

While Table 3 defines minimums for distinct vehicle pairings (e.g., AFR vs. Piloted Aircraft), comprehensive studies on the mixed-mode operational phase (where legacy piloted helicopters, semi-automated eVTOLs, and fully autonomous vehicles simultaneously share the same corridor) are absent from the reviewed literature. We discuss the implications of this critical gap in Section IV. In this section, we focus on factors potentially influencing this separation distances.

Fig. 8 presents a detailed taxonomy of factors important for defining safe separation distances in mature AAM systems. This taxonomy consists of three main categories: **Vehicle Characteristics**, **Total System Error (TSE)**, and **Environmental Factors**. Each category includes specific elements that must be considered for establishing effective separation distances promoting safe and efficient AAM operations. From a quantitative perspective, the reviewed literature is relatively evenly distributed among these categories. Environmental factors received the most attention (addressed in 7 papers), closely followed by Vehicle Characteristics (5 papers) and TSE (5 papers).

[![FIGURE 8. - Taxonomy of factors for definition of safe separation distance.](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog8-3686509-small.gif)](https://ieeexplore.ieee.org/mediastore/IEEE/content/media/8784355/11300375/11493558/vinog8-3686509-large.gif)

**FIGURE 8.**

Taxonomy of factors for definition of safe separation distance.

**Vehicle Characteristics** focus on the properties and capabilities of AAM aircraft that influence separation requirements. This category includes *Detect and Avoid (DAA)* systems and *Flight Dynamics*. *Detect and Avoid (DAA)* systems are crucial for identifying potential threats and avoiding collisions. Key components of DAA include Detection Range \[78\], which determines how far an aircraft can detect other objects, and Tracking capabilities \[77\], which allow continuous monitoring of nearby aircraft. Effective DAA systems enable AAM vehicles to make timely adjustments to maintain safe distances. *Flight Dynamics* involves accounting for the Aircraft Velocity \[78\], \[80\] and Relative Velocity \[77\], \[81\] between AAM vehicles. These factors are important for predicting future positions and ensuring that separation maneuvers can be executed smoothly.

**Total System Error (TSE)** addresses the inaccuracies and uncertainties present in the overall AAM system. This category is divided into *Navigation System Error (NSE)* and *Flight Technical Error (FTE)*. *Navigation System Error (NSE)* \[78\] includes errors from Global Navigation Satellite Systems (GNSS) \[78\] and Inertial Navigation Systems (INS) \[78\], which can affect the accuracy of an aircraft’s position. Accurate navigation is essential for maintaining precise separation distances. *Flight Technical Error (FTE)* encompasses errors related to Communication systems \[78\], Control systems \[79\], Weather conditions \[36\], and Pilotage. Reliable communication ensures that positional and intent information is accurately shared between aircraft, while effective control systems enable precise maneuvers to maintain separation. Additionally, external factors like weather and pilot performance can introduce variability, making robust error management strategies necessary.

**Environmental Factors** include external conditions that impact the effectiveness of separation measures. This category covers Wind, Wake Vortices, Noise, and Obstacles. *Wind* \[79\], \[81\] can influence aircraft stability and maneuverability, requiring adjustments to separation distances based on wind speed and direction. Wake Vortices \[36\], \[52\], \[78\], \[81\] generated by one aircraft can pose risks to the following aircraft, especially during takeoff and landing. Managing wake vortices involves maintaining adequate separation and implementing staggered flight schedules. Noise \[61\] considerations are important for minimizing the impact of AAM operations on surrounding communities, influencing how far an aircraft can operate from buildings in noise-sensitive areas. Lastly, Obstacles \[84\], both permanent and temporary, must be accounted for to ensure that AAM vehicles maintain safe distances from physical barriers within the airspace.

Together, these three categories **Vehicle Characteristics**, **Total System Error (TSE)**, and **Environmental Factors** provide a comprehensive framework for defining safe separation distances in AAM operations. By considering the factors depicted in the taxonomy presented in Fig. 8, researchers aim to ensure that separation distances are effective, adaptable, and capable of maintaining high safety standards.

### C. RQ3: Separation Definition Methodology

This section focuses on the adopted methodologies for determining safe separation distances for eVTOL vehicles. Fig. 9 presents the taxonomy of different methodologies for generation of AAM safe separation distance. According to the literature review, we categorized the existing methodologies into two primary groups: **model-based** and **empirical**. Numerous research works utilize model-based methodologies because of their simplicity and ability to represent complex aircraft behavior through simplified abstraction. Within model-based group, *stochastic models* utilize probabilistic estimates to assess collision risks or to delineate the protective geofence surrounding eVTOL in various flight phases of AAM mission. The authors in \[84\] evaluated a collision risk model of AAM aircraft with obstacles providing means to determine appropriate separation standards to be set for aircraft. The geofence is a virtual airspace boundary that prohibits (keep-out) and restricts (keep-in) access to some or all aircraft to a specific volume of airspace \[49\]. The keep-in geofence assumes a safe volume (safety bubble) around the aircraft that encapsulates uncertainties in the flight state. The authors in \[81\] considered ellipsoidal avoidance volumes around the aircraft accounting different atmospheric phenomena such as wake and wind turbulence. The authors in \[49\] presents a dynamic keep-out geofencing framework in metroplex environment to ensure safety and performance of AAM traffic. Besides stochastic models, the *computational models* (fluid dynamics, gas laws) form another category of model-based methodologies. The authors in \[80\] developed macroscopic air-traffic flow models that correlate the vehicle density and relative separation in the airspace to the frequency of conflict occurrence using gas-kinetic analogy (gas-law conflict prediction). The authors in \[79\] used a Computational Fluid Dynamics (CFD) model to derive safety geofence buffer sizing considering the vehicle dynamics, Guidance, Navigation and Control (GNC) uncertainties and wind effects.

**FIGURE 9.**

Taxonomy of methodologies for safe separation distance.

The second major category of methodologies is **empirical**, supported by experimental observations and flight data. The safe separation distances established through comprehensive *simulation* results constitute the initial category of empirical group, corroborated by synthetic or actual flight data. The authors in \[86\] ran fast-time simulations on 20 real-world flight scenarios to estimate the flight collision risks. The minimum horizontal, vertical and lateral separation distances were input to the simulation as per VFR/IFR conditions. The results provide useful insights on identifying, classifying and analyzing the loss of minimum separation. The authors in \[83\] performed comprehensive Monte-Carlo simulations to estimate collision risks of a layered airspace in which Uncrewed Aerial System (UAS) operates in the lower part of the layered airspace and AAM aircraft flies on the higher altitudes. The safe distance buffer among this two layers is concluded to be at least 10 meters through the simulation results.

Another aspect of empirical methodology is attributed to the extensive history of flight operations and *rotorcraft flight data* that inform real-world separation criteria. The early adoption of AAM operations will fundamentally depend on established flight rules (VFR, IFR) and ATC directives \[36\]. Hence, the safe separation studies performed already by federal civil aviation agencies (e.g., FAA, EASA and others) on rotorcraft vehicles will be instrumental for initial roll out of AAM operations. The authors in \[82\] determined the safety-assured minimum separation boundary for AAM operations by conducting safety risk assessment and analysis through simulations over the data gathered from GNSS/INS integrated navigation system. However, growth of AAM operations may easily overwhelm the ability of ATC to manage all of them efficiently. To ease the ATC load in managing increasing AAM eVTOLs, NASA proposes self-separation using AFR to deal with a high number of AAM flights in mixed airspace environment \[77\], \[87\].

The previous section outlined a structured taxonomy of AAM design factors and helped to identify critical gaps in current methodologies. To address these gaps, this section expands the analysis with additional insights and factors, as indicated in the forest charts in Figs. 10 \- 12.

**FIGURE 10.**

Completed taxonomy of design factors for selecting a candidate vertiport location.

**FIGURE 11.**

Completed taxonomy of design factors for air corridor formulation.

**FIGURE 12.**

Completed taxonomy of design factors for AAM operations.

To explicitly differentiate the maturity of these factors, we applied a visual coding scheme. Factors that are empirically supported by the current AAM literature are presented in standard black font. Conversely, factors that are currently hypothetical, projected, or represent critical gaps are emphasized in **red font**. These hypothetical factors are not entirely speculative; rather, they are derived from future research directions identified in the primary literature, expert assessment, and established practices in adjacent disciplines (e.g., small UAVs, intelligent transportation systems, and conventional aviation), which are cited in Figs. 10 - 12 and throughout this section.

Moreover, since this systematic review is focused on corridor design, we excluded papers focusing on smaller-scale tasks (e.g., AAM demand estimation \[4\]) from the text presented above. In this section, we enrich the taxonomy with these works.

### A. Identified Gaps: RQ1-Corridor Design Factors

#### 1) Phase 1-Vertiport Network Design

Though this phase has received significant attention from the research community, there are still several factors and data sources that were not considered \[88\]. Let us briefly describe them for each task.

**AAM Demand:** First of all, we would like to mention several works focusing exclusively on the demand analysis and market potential assessment \[4\], \[5\]. Even though the presented approaches do not significantly differ from the ones presented in our paper, these works contain an in-depth analysis of the demand.

The skewed nature of *Origin-Destination* data from surveys may not accurately capture real-world dynamics. This bias can be also observed in other datasets based on self-reported location information \[89\]. More reliable alternatives, such as ITS or transportation authority datasets, should be prioritized. When the transportation data is not available, one may reasonably assume that transportation demand reflects population dynamics. In this case, cellular network data presents a viable option for tracking real-time population density and estimating transportation demand \[90\], \[91\].

*Comparison with Other Transportation Modes* currently highlights AAM’s potential as a premium service, leveraging advantages in comfort, safety, and efficiency. With shorter travel times, fewer transfers, and strict aviation safety standards, AAM offers a superior passenger experience compared to taxis or private cars, enhancing public trust and adoption. However, unsatisfied transportation demand does not always require an AAM solution. In some cases, adding a new road or improving public transport may be more efficient and sustainable. AAM should be deployed strategically, focusing on areas where it provides the greatest value, such as underserved regions or congested urban centers. Aligning AAM demand assessments with broader urban mobility goals can foster equitable and sustainable growth.

**Feasibility:** Feasibility assessments for vertiports often overlook critical factors. *Climatic* conditions, such as seasonal winds or rains, can make vertiports inoperable for months and must be accounted for to ensure operational resilience. *Infrastructure* availability, including power grid capacity \[92\] and ground transportation access, is equally essential for seamless operations.

**Regulations:** First of all, the extended list of regulations requires refined categories. Hence, we distinguish two types of regulations by their main focus: *Safety* - and *Sustainability* -related regulatory documents.

The *Safety* -related regulations are well-covered in the literature. We provide an overview of relevant regulatory documents in Table 5. However, a comprehensive vertiport Safeguarding strategy is still overlooked in academic literature. Safeguarding should address key operational risks, including ensuring that lighting installations are not obscured or confused with non-aeronautical lighting, mitigating wildlife strike risks such as bird strikes near waste disposal sites, and preventing construction-related interference like dust, smoke, or disruptions to navigational aids. Moreover, forward-looking safeguarding strategies consider urban development plans to ensure that no obstacles or other hazardous objects will appear in the future. For more details on safeguarding as well as required vertiport layouts, we refer to the vertiport regulations provided in Table 5.

**TABLE 5** AAM safety-related regulations.

In the reviewed literature, *Sustainability* in vertiport location definition is often limited to noise-related issues. A more holistic approach is needed to ensure the harmonious development of AAM and the environment surrounding it. First, vertiport placement should align with urban development plans to account for future transportation needs. Additionally, insights from ground public transportation norms can improve route optimization and passenger flow management, enhancing operational efficiency. Second, economic growth potential must be considered, as well-placed vertiports can boost local business activity and connectivity, particularly in underserved areas. Environmental concerns, such as emissions and pollution, remain significant when aircraft are not fully electric. However, AAM has a non-zero greenhouse footprint even for fully-electric vehicles \[93\] due to the grid emissions. Finally, location selection must minimize wildlife impact, avoiding creating disturbances to sensitive ecosystems.

**Economic Viability:** Similar to the task of AAM demand assessment, some works are focused exclusively on economic viability \[94\] providing a greater level of details spanning from the factors we mentioned in Fig. 5 to accounting for maintenance, overhaul, and depreciation.

**Takeaway:** By expanding the scope of demand assessments, feasibility analyses, regulatory considerations, and sustainability criteria, the proposed taxonomy offers a more comprehensive framework for vertiport location definition. Integrating reliable data sources, considering long-term climatic and urban development factors, incorporating lessons from existing transportation modes, and evaluating economic viability more thoroughly will help ensure that AAM infrastructure is both efficient and resilient, ultimately contributing to a balanced and sustainable urban mobility ecosystem.

#### 2) Phase 2-Corridor Design

Fig. 11 presents a modified taxonomy of factors to be considered during the corridor design phase. While the **Feasibility** branch remains unchanged due to its foundational nature,4 the key improvements focus on refining the **Safety** branch with Specific Operations Risk Assessment (SORA), incorporating a new **Security** aspect, and significantly expanding the **Sustainability** definition. Below, we elaborate on these enhancements and their implications.

**Safety:** SORA, widely used for assessing complex UAS operations, systematically identifies risks as a combination of occurrence probability and severity. Safety in this context refers to a state where the risk is acceptable. While the current version (2.5) \[96\] does not include passenger missions, its core principles remain applicable to AAM. Considering AAM-adapted SORA will become particularly important when we face the need of reevaluating the current airspace configurations to increase the *airspace capacity* by identifying new airspace segments that has not yet been thoroughly investigated or utilized but are vital for overall operational efficiency of AAM.

Future AAM-specific SORA frameworks could integrate additional factors identified in this review. For instance, *Air risks* can be enhanced by considering ground structure influences, such as wind patterns \[97\] and temperature gradients caused by urban environments, as well as ground lighting effects on pilots. Similarly, *ground risks* can be assessed by advanced Machine Learnig techniques prior or during the flight based on the data collected by the aircraft \[98\]. *Risk mitigation* measures should extend beyond on-board systems such as impact reduction (e.g., parachute) and DAA solutions: the corridor definition additionally should consider coverage and performance of supporting infrastructure providing weather data and traffic surveillance. Examples of the former include the Integrated Terminal Weather System (ITWS) and the Digital Automatic Terminal Traffic surveillance systems should include both cooperative sources (e.g., ADS-B, Mode S transponders, or Remote ID \[99\], \[100\], \[101\]) and non-cooperative sources (e.g., primary radar systems). Additionally, as it is pointed out in Section III-A2, ground communication network performance should be considered. However, the performance does not have to be static as the network can be reconfigured to serve AAM traffic \[102\], \[103\], \[104\]. Alternatively, multiple independent networks can be used to boost reliability \[105\]. Moreover, future generations of cellular networks can be used for environmental sensing including cooperative/non-cooperative traffic surveillance as well as weather monitoring \[106\].

**Security:** While aircraft-related security issues are addressed by traditional aviation cybersecurity frameworks (such as the technically identical standards jointly published by RTCA and EUROCAE, e.g., DO-326A/ED-202A, DO-356A/ED-203A, and DO-355/ED-204 \[107\], \[108\], \[109\]) and explored in \[15\], secure corridor design is an essential yet underexplored area. Threats include cyberattacks targeting navigation and communication systems \[100\], as well as physical risks to infrastructure. Mitigation strategies should include:

- *Cybersecurity*: Encrypted communications, intrusion detection systems, and network hardening for traffic and weather data exchange.
- *Physical Security*: Robust protections for vertiport and corridor infrastructure to prevent unauthorized access or sabotage.

Addressing these gaps will enhance the resilience and integrity of AAM operations, ensuring secure operations in complex urban environments. Consequently, the presence of secure communication and navigation infrastructure will become a corridor design factor. Because legacy aircraft-centric standards are insufficient for multi-agent network architectures, compliance with emerging Uncrewed Aircraft System Traffic Management (UTM) security standards (e.g., ASTM F3548-21 \[110\]), regional frameworks like EASA U-space \[111\], and global directives like the ICAO Aviation Cybersecurity Strategy \[112\] is critical to protect AAM networks. Additionally, AAM requires new security regulations and protocols aligned with piloted aviation standards, tailored to the unique challenges of AAM corridors.

**Sustainability:** Sustainability in corridor design must extend beyond noise emissions to include other environmental and social impacts \[113\]. All types of *Pollution* such as visual \[114\] (e.g., the daytime aesthetic impact of physical infrastructure and low-flying aircraft), light (e.g., the nighttime impact of mandatory aviation lighting and beacons), electromagnetic, and greenhouse gas emissions \[115\] must be minimized through optimized corridor design.

*Equity* is another crucial factor, going beyond “Fairness” in Section II. Communities negatively affected by AAM operations, such as those exposed to noise, should also receive tangible benefits from the service. It was demonstrated that a wider set of social and societal factors can be embedded into corridor design \[116\]. Moreover, wildlife protection must be a priority, ensuring that corridors avoid disrupting ecosystems and align with the UN’s *Life on Land* goal.

**Takeaway:** The Safety aspect of corridor design will benefit from incorporating AAM-specific risks, including urban environmental factors and enhanced infrastructure-enabled mitigation measures using data from weather services, traffic surveillance, and cellular networks. The Security aspect will address cyber and physical threats, emphasizing encryption, intrusion detection, and alignment with aviation security standards. The broadened Sustainability branch will integrate pollution management, equity considerations, and wildlife protection, ensuring AAM aligns with environmental and social goals. These improvements provide an actionable framework for safe, secure, and sustainable deployment of AAM corridors.

#### 3) Phase 3-AAM Operations

Fig. 12 presents an enhanced taxonomy for AAM operations, focusing on critical aspects of demand, capacity, and their dynamic balancing with management of operations. Below, we provide further insights into these components.

**Flight Demand:** Accurately assessing and forecasting demand for AAM services remains a challenge due to the lack of real-world operational data. Current models serve as proxies, but once *real AAM data* becomes available, it must be integrated to refine demand estimation and forecasting.

**Capacity:** Vertiport capacity assessment can be significantly enhanced by accounting for passenger-centered infrastructure, such as car parking, lobby and waiting areas, and self-service kiosks. These elements are critical for efficient passenger flow and overall service quality. Additionally, corridor capacity is subject to temporary closures caused by hazards such as severe weather events or large gatherings, motivating the need for adaptive planning to maintain operational efficiency.

**Operations Management:** Managing operations in AAM systems is a dynamic challenge that extends beyond traditional infrastructure management, as robustness against operational uncertainties depends on a complex interplay between pre-departure strategic decisions and the effects of tactical manoeuvring \[117\]. Moreover, the list of factors should be expanded: alongside corridor and vertiport management actions proposed in the literature, we suggest adding *Demand Management* strategies to the taxonomy. Dynamic pricing \[118\] is a promising approach, allowing for price adjustments based on demand levels. For instance, higher fares during peak hours can lower demand (causing overflow to other transportation modes), while discounts during off-peak periods can encourage usage and improve utilization rates.

Another innovative strategy is enhancing the passenger Quality of Experience. Offering value-added options, such as scenic routes or premium services during low-demand periods, can attract passengers while optimizing operational efficiency. These strategies not only improve resource allocation but also contribute to passenger satisfaction and system profitability.

**Takeaway:** The availability of real-world AAM data will mark a turning point for the industry, enabling more accurate models for dynamic demand and capacity estimation. These models will inform infrastructure planning and operational strategies. Real operations will also allow for the evaluation of proposed strategies, such as dynamic pricing and quality-enhancing measures, providing insights into their efficiency and scalability. By implementing these advancements, AAM systems can achieve the adaptability and resilience needed to meet the demands of modern urban mobility.

### B. Identified Gaps: RQ2-Separation Distance Definition

While the current taxonomy (Fig. 8) provides a robust foundation for defining safe separation distances in AAM systems, several critical factors remain unexplored. Addressing these gaps is essential for enhancing safety, scalability, and adaptability in AAM operations. Below, we present these factors organized within existing and newly proposed groups.

**Vehicular Characteristics:** The energy state of eVTOLs significantly affects their ability to maintain safe separation distances. Low battery levels may limit maneuverability, such as performing evasive actions or sustaining prolonged hover modes. Hence, separation protocols must account for energy state and battery dynamics related operational constraints to ensure safety during extended or emergency operations.

**Total System Error:** Current TSE subdivision on NSE and FTE does not address vulnerabilities introduced by cyberattacks. Threats like GPS spoofing or communication jamming can disrupt navigation accuracy and coordination. Incorporating the resilience to cyber threats and redundancy measures will be critical for maintaining separation in contested environments.

In cooperative airspace systems, navigation or communication errors in one vehicle can propagate, impacting neighboring aircraft and the broader system. Separation protocols should account for such cascading effects of error propagation in cooperative systems, incorporating strategies like error isolation, real-time error correction, and multi-source validation.

**Environmental Factors:** Current separation protocols do not consider the long-term effects of climate change, such as increased frequency of extreme winds or turbulence. Considering the climate change impacts through climate projections and dynamic weather adaptation into safe separation strategies will enhance the resilience of AAM operations to evolving environmental conditions.

**System-Level and Technological Factors:***Mixed-Mode Operations*: As highlighted in Section III-B, the transitional phase where piloted, automated, and fully autonomous aircraft share airspace is a major gap in the current literature. This phase is highly debated among regulators and practitioners, with consensus far from being reached. Separation definition becomes highly complex due to discrepancies in trajectory predictability, reaction times, and communication methods (voice vs. digital). Future corridor design during this transitional phase will likely require dynamic separation buffers that default to the most conservative standard of the least equipped aircraft, or physical segregation within the corridor (e.g., dedicated altitude strata for autonomous vs. piloted flight) to maintain safety without severely degrading throughput.

As AAM operations scale, ensuring safe separation in dense corridors requires multi-agent coordination mechanism i.e., seamless coordination among multiple vehicles. Collaborative flight planning, decentralized decision-making, and shared situational awareness are vital for scalable and efficient AAM.

The variability in the performance of communication network, particularly coverage and latency, directly impacts real-time separation adjustments. Addressing these variabilities, especially in urban environments, will be essential to ensure reliable and adaptive operations.

Separation protocols currently lack validation through Digital Twin (DT) simulations. These virtual replicas can simulate real-world scenarios, such as high-density traffic or extreme weather, providing a safe and cost-effective way to test and refine separation strategies.

**Takeaway:** The inclusion of these new factors warrants expanding the current taxonomy to introduce a new group, System-Level and Technological Factors, alongside the existing categories of Vehicular Characteristics, Total System Error, and Environmental Factors. This updated taxonomy would provide a more comprehensive framework for defining safe separation distances, addressing both operational challenges and emerging technological opportunities.

By integrating these overlooked factors, AAM systems can adopt safer, more adaptive separation protocols that reflect the complexities of urban airspace, evolving environmental conditions, and advanced technologies.

### C. Identified Gaps: RQ3-Separation Distance Methodology

The methodologies described in the current taxonomy (Fig. 9) are exhaustively examined in literature and are recognized as established methodologies in the legacy aviation domain. As AI capabilities and data-driven decision-making continue to develop, we envision the future research on AAM separation distances will incorporate (1) AI/ML models to complement traditional stochastic and computational approaches, and (2) data-driven techniques at the forefront of innovation that will be accumulated from various AAM experimental campaigns.

**Model-based:** Alongside computational and stochastic models, AI/ML models will persist in being extensively utilized to evaluate various separation requirements prior to their incorporation into regulation. The current application of such models is still in its infancy and requires further research efforts.

**Empirical:** The lack of operational AAM flights has resulted in insufficient data regarding flight behavior, separation distances, and associated hazards, thereby hindering subsequent data-driven research on AAM safety. Data-driven simulations, combined with the integration of AI/ML models, will be essential for developing safe separation methodologies in the future. This will involve comparing and contrasting various separation standards based on eVTOL capabilities, airspace structure, and air traffic density.

**Aircraft reference model:** The reference model for eVTOL vehicles and the avionics equipment significantly affect the design of safe separation minima. Aside from the NASA UAM reference model \[119\], there are no publicly accessible eVTOL models for researchers. This impedes additional research and development by scholars, with such studies predominantly conducted in isolation by eVTOL manufacturers. Introducing the vehicle model to a broader research community will facilitate more comprehensive results and accelerate innovation in this domain.

**Takeaway:** Derivation safe separation distance relies on data assets such as eVTOL vehicle reference models and AAM operation data. With these models as a guide, AI/ML frameworks and smart methodologies may be applied to AAM flights, making them safer and more efficient overall.

### D. Design Choice for Real-World Corridors

Despite the fact that we have provided a comprehensive taxonomy of factors for each phase of AAM corridor design, there is no “one-size-fits-all” formula to determine the optimal factors when the actual AAM corridors are placed in the national airspace. The best-fitting factors are selected on a case-by-case basis, contingent upon the regulatory frameworks and geographical region of a particular country. The “feasibility and safety” factors must be prioritized as a general approach, prior to any consideration of the “sustainability” or “operations management” factors. For instance, the most critical factors in selecting the optimal vertiport location are “demand” and “feasibility,” with “national regulation” following in terms of importance. Economic factors are considered at the end.

To illustrate the practical utility of these taxonomies, we present a step-by-step application for designing a hypothetical AAM corridor connecting a major international airport to a downtown financial district. Instead of an ad-hoc approach, a planner would systematically traverse the proposed taxonomies to transform high-level AAM goals into actionable design constraints:

- **Phase 1 - Vertiport Location (Fig. 10):** The process begins by evaluating *Demand for AAM* (using *Commute Survey* data and projected *Trip time* savings) to justify the origin and destination. *Feasibility* dictates the exact physical placement; planners must find sites with adequate *Land availability* that integrate with existing *Access infrastructure* (e.g., railway or subway networks) while ensuring *No Obstacles* block approach paths. *Regulations* (such as local *Land use* constraints) are then applied to filter out non-compliant sites before *Economic viability* is assessed.
- **Phase 2 - Air Corridor Formulation (Fig. 11):** With the vertiports fixed, the air route is formulated by prioritizing *Feasibility* and *Safety*. Planners minimize *Ground risk* (specifically *population density*) by routing the corridor over rivers or the sea. To manage *Air risk* at the airport node, planners must safely integrate with high-volume *Legacy Traffic*, establishing strict separation standards to deconflict commercial jets from AAM approach sectors. *Sustainability* factors, specifically *Noise*, further constrain the route away from residential zones, while *Weather* conditions (such as local *Wind* patterns over the water or in urban canyons) dictate the physical width and altitude limits of the corridor.
- **Phase 3 - AAM Operations (Fig. 12):** Finally, operational rules are established to manage traffic safely within the newly formulated corridor. Planners utilize *Operations Management* tools, selecting a specific *Reservation method* to balance peak *Flight demand* and ensure the structural *Corridor Capacity* is never exceeded. Operational rules are defined to establish the flight *Priority* (e.g., expediting emergency or low-battery flights) and smoothly integrate the corridor with the surrounding managed airspace.

This structured approach demonstrates how the taxonomies serve as a sequential decision-making framework for urban airspace integration.

### E. Future Trends

Looking ahead, corridor design and separation protocols in AAM are expected to evolve toward more dynamic/adaptive, data-centric, and interconnected frameworks. Below, we summarize several key directions that are likely to shape the next generation of research and practice in this domain:

#### 1) Data Management and Standardization

As corridor operations become increasingly dense and dynamic, a unified data taxonomy covering flight states, weather updates, and communication health will be essential. Ongoing efforts by industry consortia and regulators seek to establish common data standards and best practices regarding data collection, storage, and ownership.

#### 2) Sensing and Communication Technologies

Ongoing research points toward dynamic corridor reconfiguration requiring real-time data on weather, aerial traffic, and local ground conditions. Some of these data is unavailable (e.g., weather for the AAM altitudes over urban environments) and we need efficient ways to collect this information. Additionally, we will need to merge information from cooperative sources (e.g., ADS-B, Remote ID, Mode S transponders) with non-cooperative sensing (e.g., radar, LiDAR, cellular-based detection). Exchanging and processing these data requires reliable, low-latency communication links (e.g., 5G/6G cellular, satellite) and robust sensor fusion algorithms that rapidly process data from multiple sources. Potentially, 5G/6G networks can also provide Integrated Communications, Navigations, and Survellance (ICNS) services \[120\].

#### 3) Digital Twins for Simulation, Testing, and Exploitation

High-fidelity digital twins can serve as continuously updated mirrors of real-world corridors, injecting live telemetry (e.g., weather, traffic density, aircraft states) into virtual replicas. By stress-testing new layouts, separation rules, and emergency scenarios in a risk-free setting, planners can refine operational strategies and identify vulnerabilities before implementing changes in actual airspace. Moreover, infrastructure DTs (i.e., aircraft, vertiport DTs) will enable predictive maintenance and efficient resource utilization \[121\].

#### 4) Coordinated ATM–AAM Traffic Management

Growing AAM volumes in low-altitude airspace intensify the need to unify AAM-specific procedures with conventional Air Traffic Management (ATM). Standardized interfaces for exchanging flight plans, route clearances, and no-fly advisories will help controllers—or automated decision systems—treat AAM flights alongside regular air traffic. This integration becomes particularly urgent when corridor segments intersect with conventional approach paths or controlled airspace, underscoring the importance of a consistent, real-time information flow. Since human controllers will need to interact with highly automated AAM systems, the danger of overloading the controllers must be overcome with careful design of AAM Human-Machine Interfaces (HMI).

#### 5) Autonomous Flight Rules and Onboard Autonomy

Though the AFR concept was suggested almost a decade ago, it is not yet mature. Future concepts envision autonomous or semi-autonomous eVTOLs that handle collision avoidance and minor route adjustments in flight, drawing on local sensor fusion and short-range inter-aircraft communication, although comprehensive fallback procedures and certification frameworks will be essential for practical deployment.

#### 6) Large Language Models and Agent-Based Autonomy

As autonomous systems increasingly transition from rigid, rule-based algorithms to reasoning-driven, multimodal intelligence, the integration of Large Language Models (LLMs) and AI agents presents a transformative direction for AAM \[122\]. Future AAM corridor management could leverage LLM-powered agents to process complex, unstructured data streams (legacy voice ATC instructions, text-based NOTAMs, and dynamic weather reports) and fuse them with spatial sensor data to make real-time separation and routing decisions. Furthermore, generative AI agents can serve as an intelligent bridge in HMI, alleviating controller workload by summarizing complex traffic scenarios and explaining automated conflict-resolution decisions in natural language. However, adapting these foundational models for safety-critical AAM operations will require rigorous research into their security and reliability, specifically focusing on mitigating AI hallucinations, and defending against adversarial inputs (e.g., prompt injection). Perhaps the most challenging issue will be to establish verification methods suitable for aviation certification frameworks of AI solutions.

#### 7) Integration Into Broader Intelligent Transportation Systems (Its)

As AAM becomes part of the urban mobility landscape, interoperability with established ground networks will be vital. Shared data platforms that unify AAM flight schedules with bus, rail, or micro-mobility services allow passengers to plan door-to-door trips seamlessly. Furthermore, integrating AAM routes into citywide congestion-monitoring systems can help alleviate roadway overload, advancing both reliability and sustainability in metropolitan transport ecosystems.

In addition to these corridor- and separation-focused directions, future AAM research will increasingly address broader challenges such as AAM regulatory frameworks, alternative propulsion methods (e.g., hydrogen), new business models for on-demand AAM services, enhanced security protocols for preventing cyber intrusions, and novel approaches for infrastructure design. Efforts to streamline operational certifications, develop rigorous pilot or pilotless (autonomous) training modules, and foster public acceptance through transparent noise and safety assessments will further round out the AAM landscape. By tackling these cross-cutting issues, the AAM ecosystem stands to achieve higher levels of scalability, environmental responsibility, and societal benefit.

This work presents a systematic literature review of the AAM corridor design and the definition of safe separation. The review applies established PRISMA guidelines to reduce bias and ensure the reproducibility of results. The systematic review was structured around three research questions that integrate vertiport network design, corridor design, operational management, and the definition of safe separation. A total of 1949 unique papers were identified during the screening process, from which 175 papers were selected for full-text review. Utilizing inclusion/exclusion criteria, we identified 62 articles that addressed at least one of the research questions. A comprehensive taxonomy of corridor design factors is synthesized, and we have expanded it with additional factors that have been overlooked in existing studies. According to the results of our systematic review, we delineate the effective AAM corridor design approach (RQ1) into three separate phases.

Phase 1 aims to identify suitable vertiport locations that meet commuting demand, are feasible, comply with national regulations, and are economically viable. The vertiports must be strategically positioned in geographical areas characterized by high AAM service demand that can be estimated based on population density and income levels. The vertiport construction must be feasible considering land availability, absence of obstructions, availability of public access and power infrastructure, and aircraft capabilities. The chosen vertiport sites must adhere to national regulations concerning airspace, aircraft, vertiport standards, and noise limitations. Moreover, the enduring economic viability of the chosen sites relies on evaluating both operational and capital expenditures.

In phase 2, AAM corridors are established to connect vertiport locations, guaranteeing that the flight path is feasible, safe, and environmentally sustainable. The feasibility component emphasizes the strategic avoidance of flight paths with static and dynamic obstacles, as well as evaluating the aircraft’s ability to maneuver through designated flight corridors. The safety of the AAM corridor depends on air and ground risks (e.g., probability of colliding with another aircraft or damaging people/infrastructure). Furthermore, these risks can be reduced by contingency measures accounting for unplanned or emergency situations caused by aircraft sub-system malfunctioning or meteorological conditions. The sustainability aspect aims to link AAM corridors with long-term viability, societal and environmental impact concerning many aspects including noise footprint, energy efficiency, and equitable access to airspace.

Phase 3 ensures the effective and efficient operation of AAM services across vertiports and corridors established in previous phases. This phase begins with the assessment and projection of flight demand for AAM services. It is followed by an analysis of the capacity constraints of vertiports and corridors. Prior analysis of demand and capacity is then used by dynamic operation management ensuring that vertiports are adequately prepared for efficient and timely arrival and departure management. Additionally, this approach allows the AAM corridors to effectively manage varying air traffic density, flow management, and time-critical rerouting.

In addition to corridor design, our work provides a comprehensive examination of the definition of safe separation (RQ2), which is essential for preventing collisions and optimizing airspace utilization. The first implementation of AAM will depend on current VFR and IFR, in conjunction with ATC, utilizing a rule-based separation approach; nevertheless, a novel framework of performance-based Digital and Autonomous Flight Rules (DFR/AFR) must be developed to progress towards a complex AAM ecosystem during the next decade. The aircraft performance, particularly regarding DAA capabilities and flight dynamics, are primary factors influencing the safe distance between aircraft. Given that the onboard avionics may experience performance uncertainties and inaccuracies, it is essential to implement robust error management strategies to estimate the total system error related to the aircraft. The total system error consists of the navigation system error resulting from GNSS/INS sensors and the flight technical error stemming from communication, control subsystems of the aircraft. Furthermore, external environmental conditions such as wind, wake vortices are critical factors that must be considered to uphold the highest safety standards. Numerous model-based separation approaches utilize stochastic models to assess collision risks, macroscopic air traffic flow models, gas-law-based conflict prediction models, computational fluid dynamics models, and geometric models to derive safe separation distance of AAM aircraft (RQ3). Many existing works have also illustrated the simulation-based methodology utilizing real or synthetic flight data to get insights regarding the safe separation distances.

We believe that this work on AAM corridor design and safe separation distance definition will serve as a valuable resource for researchers and practitioners in this field.

Conceptualization: Evgenii Vinogradov, Debashisha Mishra, Mariam Ali Askar Alobeidli, Jamal Khaled Al Ali, Ahmed Saleh Alshehhi, Jennifer Simonjan, and Enrico Natalizio; methodology: Evgenii Vinogradov; data collection, paper screening, quality assessment, data extraction, and the writing of the manuscript: Evgenii Vinogradov and Debashisha Mishra; and review and editing: Mariam Ali Askar Alobeidli, Jamal Khaled Al Ali, Ahmed Saleh Alshehhi, Jennifer Simonjan, and Enrico Natalizio.

See Table 4.

See Figs. 10 -- 12 and Table 5.