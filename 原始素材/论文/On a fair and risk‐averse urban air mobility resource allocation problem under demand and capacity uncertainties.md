---
title: "On a fair and risk‐averse urban air mobility resource allocation problem under demand and capacity uncertainties"
source: "https://onlinelibrary.wiley.com/doi/epdf/10.1002/nav.22217?getft_integrator=clarivate&src=getftr&utm_source=clarivate"
author:
published:
created: 2026-07-01
description:
tags:
  - "clippings"
---
Received: 21 February 2023 Revised: 23 May 2024 Accepted: 6 July 2024  
DOI: 10.1002/nav.22217  
R E S E A R C H A R T I C L E  
On a fair and risk-averse urban air mobility resource allocation  
problem under demand and capacity uncertainties  
Luying Sun 1 Haoyun Deng 2 Peng Wei 3 Weijun Xie2  
1 Department of Industrial & Systems Engineering,  
Virginia Tech, Blacksburg, Virginia, USA  
2 H. Milton Stewart School of Industrial and  
Systems Engineering, Georgia Institute of  
Technology, Atlanta, Georgia, USA  
3 Department of Mechanical & Aerospace  
Engineering, George Washington University,  
Washington, District of Columbia, USA  
Correspondence  
Weijun Xie, H. Milton Stewart School of Industrial  
and Systems Engineering, Georgia Institute of  
Technology, Atlanta, GA 30332, USA.  
Email: wxie@gatech.edu  
Funding information  
National Science Foundation, Grant/Award  
Numbers: 2246414, 2246417, 2047390  
Abstract  
Urban air mobility (UAM) is an emerging air transportation mode to alleviate the  
ground traffic burden and achieve zero direct aviation emissions. Due to the potential  
economic scaling effects, the UAM traffic flow is expected to increase dramatically  
once implemented, and its market can be substantially large. To be prepared for the  
era of UAM, we study the fair and risk-averse urban air mobility resource alloca-  
tion model (FairUAM) under passenger demand and airspace capacity uncertainties  
for fair, safe, and efficient aircraft operations. FairUAM is a two-stage model, where  
the first stage is the aircraft resource allocation, and the second stage is to fairly and  
efficiently assign the ground and airspace delays to each aircraft provided the realiza-  
tion of random airspace capacities and passenger demand. We show that FairUAM  
is NP-hard even when there is no delay assignment decision or no aircraft alloca-  
tion decision. Thus, we recast FairUAM as a mixed-integer linear program (MILP)  
and explore model properties and strengthen the model formulation by developing  
multiple families of valid inequalities. The stronger formulation allows us to develop  
a customized exact decomposition algorithm with both benders and L-shaped cuts,  
which significantly outperforms the off-the-shelf solvers. Finally, we numerically  
demonstrate the effectiveness of the proposed method and draw managerial insights  
when applying FairUAM to a real-world network.  
KEYWORDS  
fairness, mixed-integer linear programming, resource allocation, risk-averse, urban  
air mobility  
1 INTRODUCTION  
The urban population in the U.S. is expected to increase  
from 83% in 2020 to 89% in 2050 (United Nations, 2018).  
Albeit benefiting people with better opportunities, urban-  
ization leads to more severe traffic congestion problems  
with higher traffic volume, larger travel delays, and more  
energy consumption and air pollution (Schrank et al., 2021).  
This calls for efficient alternative transportation modes  
(Speranza, 2018). One promising way is the on-demand  
point-to-point urban air mobility (UAM) service, which relies  
on automated electric vertical take-off and landing vehicles  
(eVTOLs) to transport passengers at lower altitudes in and  
around metropolitan areas. It has been recognized recently  
that the UAM has the potential to improve personal mobility  
by reducing travel time and cost, reduce energy consumption  
and air pollution by using eVTOL with zero direct emission,  
as well as enhance economic vitality (Price et al., 2020). In  
the meantime, thanks to the emerging aircraft technologies  
in increasing reliability, aviation companies, including Joby,  
Archer, Eve, and so forth, can launch their products and pro-  
totypes to make UAM possible in the near future. Due to the  
potential economic scaling effects, the UAM traffic flow is  
expected to increase dramatically once implemented, and its  
This is an open access article under the terms of the Creative Commons Attribution-NonCommercial-NoDerivs License, which permits use and distribution in any medium, provided  
the original work is properly cited, the use is non-commercial and no modifications or adaptations are made.  
© 2024 The Author(s). Naval Research Logistics published by Wiley Periodicals LLC.  
Naval Res Logistics 2025;72:111–132 wileyonlinelibrary.com/journal/nav 111SUN ET AL . 123  
TABLE 1 Random instance setting and results of different formulations and Algorithm 1.  
MILP MILP.VI Algorithm 1  
Instance Num. of  
scenarios Airspace  
capacity Passenger  
demand Time (s) Gap (%) Obj. val Time (s) Gap (%) Obj. val Time (s) Gap (%) Obj. val  
S-1 5 Low Low 23 0 133.8 12 0 133.8 6 0.0 133.8  
S-2 Medium 67 0 285.8 33 0 285.8 12 0.0 285.8  
S-3 High Medium 37 0 184.3 20 0 184.3 9 0.0 184.3  
S-4 High 85 0 252.3 49 0 252.3 15 0.0 252.3  
S-5 10 Low Low 869 0 145.3 150 0 145.3 67 0.0 145.3  
S-6 Medium 3600 0.5 306.3 535 0 304.7 181 0.0 304.7  
S-7 High Medium 3600 2.4 232.3 364 0 226.7 115 0.0 226.7  
S-8 High 3600 2.7 352.7 1801 0 343.3 337 0.0 343.3  
S-9 20 Low Low 3600 2.2 189.8 2736 0 185.6 869 0.0 185.6  
S-10 Medium 3600 5.4 379.3 3600 0.3 359.8 2497 0.0 358.8  
S-11 High Medium 3600 5.3 285.2 3600 0.8 272.3 1684 0.0 270.0  
S-12 High 3600 6.8 430.0 3600 1.0 406.7 3600 0.2 403.5  
L-13 10 Low Low 3600 13.4 292.2 3600 3.9 264.6 666 0.0 254.3  
L-14 Medium 3600 17.3 340.1 3600 5.4 299.1 1631 0.0 282.9  
L-15 High Medium 3600 15.6 353.3 3600 5.2 313.3 1055 0.0 296.7  
L-16 High 3600 25.1 714.5 3600 8.6 603.4 3600 0.4 549.9  
L-17 20 Low Low 3600 38.9 441.9 3600 11.3 324.4 3600 1.3 294.9  
L-18 Medium 3600 46.1 717.4 3600 14.9 489.1 3600 4.4 435.4  
L-19 High Medium 3600 46.9 609.6 3600 15.3 396.6 3600 7.3 362.2  
L-20 High 3600 57.3 904.7 3600 21.4 681.0 3600 10.2 596.0  
The airspace capacities of each bottleneck point per time unit  
are randomly generated with equal probability from two sets  
of different levels of airspace capacity: {1, 2} for low level,  
{2, 3} for high level. The passenger demand of each OD pair  
during the whole time horizon is generated from three differ-  
ent discrete uniform distributions to represent different levels  
of passenger demand:  (2, 6) for low level,  (6, 10) for  
medium level,  (10, 20) for high level. In the small network,  
the numbers of aircraft for service providers are set to 3 for the  
low-level passenger demand instances, 5 for the medium-level  
passenger demand instances and 10 for the high-level pas-  
senger demand instances. In the larger network, the numbers  
of aircraft for service providers are 6 for the low-level pas-  
senger demand instances, 10 for the medium-level passenger  
demand instances, 15 for the high-level passenger demand  
instances. We let the risk parameter 𝜀 \= 0.1 in CVaR to  
minimize the worst case outcomes. The number of scenar-  
ios is chosen to be 5, 10, and 20 for the following reasons:  
(i) the capacity uncertainty is due to inaccurate weather  
forecasting. However, there is a limited number of weather  
conditions. Hence, the scenarios that we consider are rep-  
resentative and can be of small size; (ii) As mentioned in  
the previous section, the CVaR has distributional robustness  
interpretation, which is known to achieve better out-of-sample  
performance guarantees. We also illustrate the stability of  
the CVaR in Figure 4; and (iii) Our FairUAM model is  
extremely difficult to solve. As shown in Table 1, using  
ten scenarios already takes a much longer time to solve to  
optimality.  
5.1.2 Numerical results  
We summarize the instances and report the results in Table 1  
where a-b in the “Instance” column means the size net-  
work a and random instance b; “MILP” represents FairUAM  
(1a–d) and “MILP.VI” represents FairUAM (1a–d) with valid  
inequalities (5a,b)–(12). We see that the computational time  
increases as the instance size (e.g., network size, number  
of aircraft, etc.) increases. When the number of scenar-  
ios increases, both objective value and computational time  
increases. MILP is only able to solve the first five instances  
to optimality. MILP.VI improves MILP’s performance and  
can solve 80% more instances (i.e., the first nine instances)  
to optimality. However, no instance in the larger network can  
be solved to optimality by either MILP or MILP.VI. On the  
contrary, Algorithm 1 can improve MILP.VI and solve 14  
instances to optimality, which is 56% more instances solv-  
able compared to MILP.VI and 180% more instances solvable  
compared to MILP. This is probably because using decom-  
position and exploring formulation structures take advantage  
of solving smaller and easier subproblems. Besides, we have  
found that the most effective cuts in Algorithm 1 are L-shape  
and feasibility cuts. We also notice that, with the same passen-  
ger demand and the same number of aircraft, smaller airspace  
capacity instances are often more difficult to solve since the  
more restrictions in the airspace are, the harder aircraft assign-  
ment can be. When the airspace capacity increases, the objec-  
tive value decreases since larger airspace capacity allows  
more aircraft to stay in the same airspace at the same time,  
which leads to short delays and smaller unsatisfied passenger124 SUN ET AL .  
FIGURE 3 Comparison of lower bound and optimality gap with and without the valid inequalities.  
demand. With the same airspace capacity, higher passenger  
demand results in longer computational time, since either  
more aircraft should be assigned to OD pairs or some UAM  
service providers may have unsatisfied passenger demand.  
Higher passenger demand also leads to a higher objective  
value, which is intuitive since the total operation cost of UAM  
service providers increases.  
To better demonstrate the effectiveness of valid inequal-  
ities, besides comparing computational time and optimality  
gap of MILP and MILP.VI in Table 1, we solved instance  
S-4 using Algorithm 1 with and without valid inequalities  
(5a,b)–(12) respectively, which are illustrated in Figure 3.  
Note that, the results for other instances are similar and  
Figure 3 is for demonstration. The computational time of  
instance S-4 significantly decreases from 438 to 15 s if we  
apply valid inequalities. The improvement mainly comes from  
the symmetry-breaking ones that prevent exploring unneces-  
sary equivalent solutions.  
To demonstrate the robustness of the solutions from our  
model, we consider an additional risk-neutral FairUAM  
(1a–d) where 𝜀 \= 1 and 𝜌(Z) \= EP\[Z\] to compare with  
our risk-averse one. We first obtained the solutions by solv-  
ing two formulations with instance S-8. Then, we generated  
10 new scenarios following the same procedure mentioned  
before for evaluation. We assumed that weather conditions  
or passenger demand are changing rapidly over time. Thus,  
we applied a truncated Gaussian noise to generate airspace  
capacity and passenger demand per scenario to make sure that  
they are nonnegative. More specifically, we let the random  
perturbation of airspace capacity follow a Gaussian distri-  
bution  (0, 0.1) truncated to be non-positive and rounded  
to the nearest nonnegative integer. For the random perturba-  
tion applied to passenger demand, we let it follow a Gaussian  
distribution  (0, 0.2) truncated to a nonnegative number  
and rounded to the nearest integer. We repeated the process  
15 times to generate asymptotic 95% confidence intervals.  
The results are illustrated in Figure 4. It shows that, when  
the demand increases or the airspace capacity decreases, the  
objective value increases and the risk-averse one is more  
robust. It is worth mentioning that, when the airspace capacity  
is small (e.g., a part of bottleneck points having 0 capacity),  
no aircraft can depart; otherwise, it will violate the airspace  
capacity. In this case, both risk-neutral and risk-averse models  
end up with a trivial solution.  
We conducted a sensitivity analysis of weighted scalar 𝜆 on  
instance S-8 to demonstrate the trade-off between efficiency  
and fairness. We let 𝜆 ∈ {0, 0.25, 0.5, 0.75, 1}. For better  
comparison, we illustrate the change in percentage for total  
cost and unfairness, where for the total cost change, we let  
the base case be the lowest possible cost, and for the unfair-  
ness change, we let the base case be the smallest value of the  
largest average company cost. We evaluate unfairness as the  
absolute difference between the highest and lowest average  
company operation costs. The result is illustrated in Figure 5.  
We see that, when the weighted scalar 𝜆 \= 1, the total oper-  
ation cost is the smallest; however, the solution is extremely  
unfair among different UAM service providers. Some service  
providers suffer much higher average aircraft operation cost  
due to delays. As the weighted scalar increases, we can reduce  
the unfairness dramatically with a small increase in the total  
operation cost. When the weighted scalar 𝜆 \= 0, we make  
the fairest assignment for each service provider; however, as  
expected, the total operation cost is the highest. In summary,  
we recommend using an appropriate parameter 𝜆 which can  
help achieve a good balance between fairness and efficiency.  
To illustrate that a small number of scenarios are sufficient  
to generate effective decisions, we conducted a numerical  
study on four small networks with a time horizon | | \= 20 to  
evaluate the out-of-sample performance of solutions obtained  
from 20 and 100 scenarios. In this numerical study, each net-  
work consists of || \= 3 service providers and || \= 3 OD  
pairs, and each service provider operates three routes. Net-  
works 1 and 2 have || \= 3 bottleneck points, with each  
OD pair having three candidate routes. The airspace capac-  
ity follows a discrete uniform distribution of  (1, 2), and  
the passenger demand follows a discrete uniform distribu-  
tion of  (2, 6). Networks 3 and 4 have || \= 5 bottleneck  
points, with each OD pair having five candidate routes. The

SUN ET AL . 127  
FIGURE 8 Map of 13 airports within 50 miles from KSEA.  
respectively. To model the uncertain parameters, we shifted  
the timeline by five units for each scenario and applied a trun-  
cated Gaussian distribution  (0, 0.5) rounded to the nearest  
integer to generate the airspace capacity of each bottleneck  
point.  
The passenger demand was generated based on population  
and airport operations data. We first collected the total popu-  
lation data in the corresponding area having the same zipcode  
for each vertiport then multiplied them by 0.02%, assuming  
that 0.02% of the population plan to travel during the planning  
horizon. We also collected the average transient general avi-  
ation operation data for each vertiport, and multiplied them  
by 0.02 to represent the travel needs of people not living in  
the corresponding area. We let the sum of these two numbers  
for each vertiport to represent the total passenger demand of  
all the OD pairs that depart from the same vertiports. For a  
given origin vertiport, its destination vertiports are the near-  
est two vertiports at least 30 miles away and within 50 miles.  
(An origin vertiport may have only one destination vertiport,  
i.e., KTIW has only one destination.) We then assigned the  
total passenger demand to OD pairs evenly and rounded them  
up to the nearest integers. For example, KSEA has two desti-  
nation vertiports, KPAE (31.6 miles) and KSHN (41.9 miles).  
Each OD pair has a passenger demand of 13 since the total  
passenger demand at KSEA is 25. To model the future uncer-  
tainty, we applied a truncated Gaussian distribution  (0, 2)  
rounded to the nearest nonnegative integer to the passenger  
demand of each OD pair. In our numerical study, we generated  
10 scenarios for this problem.  
5.2.3 Numerical results  
We ran Algorithm 1 to solve all the cases in this subsection  
and display the results in Table 4, where “Max” denotes the  
largest average company cost, “Ave.G” denotes the average  
company ground delay among different scenarios, “Ave.A”  
denotes the average company airborne delay, and “Ave.S”  
denotes the average unsatisfied passenger demand. “Num.  
of Aircraft” denotes the number of aircraft of each service  
provider, which corresponds to the planning horizon. The  
computational time of all the cases is less than an hour. It  
is seen that increasing the number of aircraft can decrease  
the unsatisfied passenger demand and optimal value. And all  
three models yield the same unsatisfied passenger demand.  
This is probably because satisfying the passenger demand is  
prioritized in all models. Although the ratio of the cost of  
airborne delay and ground delay is not large, airborne delay  
tends to be close to zero and ground delay is always larger128 SUN ET AL .  
TABLE 4 Results of case study on a real-world network.  
Fair and risk averse Without fairness Risk neutral  
Company cost Company cost Company cost  
Case Num. of  
aircraft Total Max Ave.G Ave.A Ave.S Total Max Ave.G Ave.A Ave.S Total Max Ave.G Ave.A Ave.S  
1 (10, 10, 10) 40.4 14.6 (16, 4, 5) (0, 0, 0) (5, 6, 4) 39.7 15.8 (4, 18, 2) (0, 0, 0) (5, 6, 4) 38.3 14.2 (13, 4, 4) (0,0,0) (5, 6, 4)  
2 (15, 15, 15) 17.1 6.7 (15, 25, 17) (0, 0, 0) (4, 0, 0) 16.7 7.3 (27, 13, 15) (0, 0, 0) (4, 0, 0) 16.5 6.4 (15, 22, 16) (0, 0, 0) (4, 0, 0)  
3 (18, 15, 12) 12.5 4.2 (24, 23, 8) (0, 0, 0) (0, 0, 2) 12.2 4.9 (10, 25, 17) (0, 0, 0) (0, 0, 2) 11.9 4.1 (21, 20, 8) (0, 0, 0) (0, 0, 2)  
FIGURE 9 Evaluation of total operation cost when passenger demand increases.  
than zero. This is not surprising, since when the delay can-  
not be avoided, it is better to hold aircraft on the ground  
instead of letting them wait in the air. Compared to the model  
without fairness, the model with fairness can decrease the  
highest company operation cost by about 10% with a 2%  
increase in the optimal value. Notice that, in the fair and  
risk-averse model, due to fairness enforcement among dif-  
ferent UAM service providers, those service providers with  
nonzero unsatisfied passenger demand are assigned to have  
a smaller ground delay. However, in the model without fair-  
ness, due to lack of the fairness term, a service provider with  
nonzero unsatisfied passenger demand may be assigned to a  
large ground delay, which leads to a larger company opera-  
tion cost. Furthermore, the largest ground delay in the fair and  
risk-averse model is always higher than that from the model  
without fairness. Compared to the result from the risk-neutral  
model, the risk-averse one yield a small increase of 5% in  
the total operation cost and the largest company operation  
cost since it is optimizing the worst scenario performance  
instead of average performance over all the scenarios. To fur-  
ther demonstrate the robustness of solutions from the two  
models, following the same procedure in Section 5.1, we gen-  
erated five new scenarios and applied a truncated Gaussian  
noise to passenger demand. The result is shown in Figure 9,  
which shows that, the total operation cost increases and the  
risk-averse one tends to be more robust when the passenger  
demand increases.  
5.2.4 Managerial insight  
FairUAM can provide the UAM traffic manager with an  
optimal UAM aircraft resource allocation plan and delay  
assignment without perfect information, achieving both  
company-level fairness and system-level efficiency. The  
framework accounts for the existence of uncertainties in  
weather information and demand fluctuation. Besides gen-  
erating an optimal operation plan, our framework can also  
provide extra support for the UAM traffic manager to iden-  
tify the busy bottleneck points, which are usually regarded  
as the system hotspots. With such information, UAM ser-  
vice providers are capable of better designing their routes  
in the aircraft path-planning stage before filing the flight  
plan to the UAM traffic manager in the future. UAM ser-  
vice providers can consider more candidate routes or even  
take detours to avoid busy bottleneck points and possible  
future congestion. In addition, identification of the current  
system hotspots can also be valuable when the UAM net-  
work is still in the blueprint or can improve the existing UAM  
network. Instead of improving the capability of all the bottle-  
neck points, which is quite expensive, focusing on the busiest  
bottleneck points is more effective in a mature UAM operat-  
ing environment with high-density aircraft. In this case, we  
would like to evaluate the utilization rate of bottleneck points.  
The higher the utilization rate is, the busier the corresponding  
bottleneck point should be.  
Suppose in time horizon  , the time point that the last  
aircraft landing at its destination vertiport is  
t0 \= arg min  
t′  
{  
t′ ∶ ∑  
t\>t′,t∈  
tB k  
it(𝝃) = 0, ∀k ∈   
}  
.  
We consider the utilization rate of the bottleneck point k ∈  
 between time 0 and t0 as the ratio of the actual number  
of aircraft passing the bottleneck point divided by the total  
number of aircraft it can handle during this period, which can  
be represented as  
UR k \=  
∑  
t∈0  
∑  
𝓁∈  
∑  
i∈𝓁  
B k  
it(𝝃)  
∑  
t∈0  
C k  
tSUN ET AL . 129  
TABLE 5 Airspace utilization rate.  
Case KSEA KRNT KBFI 2S1 S50 S36 KTIW KPWT KPLU 8W5 KPAE KSHN KOLM  
1 0.33 0.14 0.25 0.31 0.17 0.08 0.25 0.11 0.19 0.17 0.11 0.31 0.17  
2 0.50 0.20 0.40 0.40 0.25 0.10 0.50 0.15 0.30 0.30 0.15 0.35 0.25  
3 0.55 0.25 0.50 0.60 0.30 0.15 0.45 0.15 0.35 0.30 0.20 0.20 0.25  
FIGURE 10 Impact on total operation cost and fairness while increasing total capacity of busy bottleneck points (KSEA, KBFI, 2S1, KTIW) or taking  
detours to avoid them.  
where 0 \= {0, … , t0}. The results are displayed in Table 5.  
We see that KSEA, KBFI, 2S1, KTIW are the busiest bot-  
tleneck points with the highest utilization rate. This may be  
because these bottleneck points are located around the cen-  
ter of the network, and many routes pass those bottleneck  
points more often compared to others. When we numeri-  
cally increase the total airspace capacity ∑t∈0 C k  
t of those  
bottleneck points by 10% in Case 1, we find that the opti-  
mal value can be reduced by 5%. Note that the results of  
Cases 2 and 3 are similar. This implies that if the traffic  
manager would like to further reduce total congestion or  
operation cost, it is a good idea to focus on these four bottle-  
neck points. Enlarging the capability of these four bottleneck  
points can benefit the whole network. Note that the capac-  
ity of the system hotspots can be increased by introducing  
promising advanced aircraft separation assurance technolo-  
gies and aircraft onboard automation (see, e.g., Kochenderfer  
et al., 2012; Brittain et al., 2020). We further illustrated  
how the total operation cost and the fairness change while  
increasing the total capacity of these four bottleneck points,  
as shown in Figure 10. The fairness score is defined as the  
ratio of the smallest average company cost to the largest  
average company cost such that 1 is completely fair and  
0 is completely unfair. It is shown that the total opera-  
tion cost decreases when the total capacity increases since  
the congestion level can be reduced. However, when the  
total capacity of these four bottleneck points is increased  
by over 15%, the objective value tends to stay at a similar  
value since the system hotspots transfer to other bottleneck  
points.  
On the other hand, changing the number of bottleneck  
points on a route when designing the routes, that is, taking  
a detour to avoid visiting busy airspace, can also decrease  
the delay. We demonstrate the impact on the total operation  
cost and the largest company average operation cost when  
some routes are redesigned to avoid busy bottleneck points  
(KSEA, KBFI, 2S1, KTIW) using Case 1, which is shown  
in Figure 10. We can see that the total operation cost can  
be reduced, while the fairness almost stays the same. This  
suggests that to achieve the best efficiency, it may not have  
to sacrifice fairness between UAM service providers. The  
overall efficiency can also be improved with better network  
and route design to obtain a win-win situation.  
In our FairUAM framework, a better input (e.g., more accu-  
rate weather prediction) leads to a better operation plan and  
less computational effort. Following the same procedure in  
applying the random Gaussian perturbation to airspace capac-  
ity, we demonstrate the impact of the accuracy of airspace  
capacity on the total operation cost and the largest average  
company operation cost using Case 1 as shown in Figure 11.  
We notice that by increasing the fluctuation in airspace capac-  
ity, the total operation cost increases. This raises the require-  
ment for a better weather forecast or even an online weather  
report for each bottleneck point. For the passenger aspect,  
changes in passenger demand result in an extra computational  
effort or sometimes unsatisfied demand. Therefore, instead  
of only focusing on launching the service or developing the  
technology, it is also important for the service providers to  
understand their passengers and incentivize the passengers for  
higher service satisfaction.130 SUN ET AL .  
FIGURE 11 Evaluation of total operation cost and largest average company cost when airspace capacity changes.  
6 CONCLUSION  
In this paper, we study the FairUAM, which is proven to  
be NP-hard in a deterministic setting and NP-hard with a  
given route and OD pair assignment. To simplify FairUAM,  
we derive monotonicity properties and relax the integrality of  
some decision variables. To further improve the MILP formu-  
lation, we propose valid inequalities by exploring the model  
structures. We develop a decomposition-based algorithm to  
solve FairUAM. Finally, we generate random instances to  
demonstrate the effectiveness of the proposed method to  
apply it to a real-world network in Seattle. Compared to  
the risk-neutral model and the model without fairness con-  
sideration, FairUAM is more robust when the passenger  
demand or weather forecasting is subject to error and can  
fairly assign the aircraft and delay at the company-level.  
Aircraft-level fairness can also be included in FairUAM  
with a simple modification to the fairness term. For the  
managerial aspect, FairUAM not only generates the optimal  
operation plan but also detects the system hotspots by find-  
ing the busy bottleneck points. This information provides  
UAM service providers extra support for better route plan-  
ning. It also provides some guidance in future UAM network  
design. This is consistent with the UAM concept of opera-  
tions provided by the Federal Aviation Administration (FAA)  
and National Aeronautics and Space Administration (NASA)  
(Fontaine, 2023) as  
“ … The ‘buffer’ necessary to account for  
uncertainty as the operational tempo increases  
leads to the eventual need for tactical decon-  
fliction and DCB (demand capacity balancing)  
capabilities to optimize efficiency … ”  
For our future work, we would like to include network  
design and rerouting (see, e.g., Yu, Shen, & Wang, 2021; Toth  
& Vigo, 2002) into consideration and theorectically improve  
the model using stronger formulations. The FairUAM frame-  
work can also be generalized to other resource allocation  
problems under demand and capacity uncertainties. For  
example, we can extend our framework to robot task alloca-  
tion with demand and capacity uncertainties in the warehouse.  
We can also generalize the framework to fair vehicle alloca-  
tion in disaster evacuation to minimize travel time.  
ACKNOWLEDGMENTS  
The first and second authors were supported in part by the  
National Science Foundation grants 2246414 and 2246417.  
The third author was supported by the National Science Foun-  
dation grant 2047390. The first author was also supported  
by the Virginia Space Grant Consortium New Investigator  
Program.  
DATA AVAILABILITY STATEMENT  
The data that support the findings of this study are available  
from the corresponding author upon reasonable request.  
REFERENCES  
Ahmed, S. (2013). A scenario decomposition algorithm for 0–1 stochas-  
tic programs. Operations Research Letters, 41(6), 565–569.  
Benders, J. F. (1962). Partitioning procedures for solving  
mixed-variables programming problems. Numerische Mathematik,  
4(1), 238–252.  
Bennaceur, M., Delmas, R., & Hamadi, Y. (2022). Passenger-centric  
urban air mobility: Fairness trade-offs and operational efficiency.  
Transportation Research Part C: Emerging Technologies, 136,  
103519.  
Bertsimas, D., Lulli, G., & Odoni, A. (2011). An integer optimiza-  
tion approach to large-scale air traffic flow management. Operations  
Research, 59(1), 211–227.  
Bharadwaj, S., Carr, S., Neogi, N., Poonawala, H., Chueca, A. B., &  
Topcu, U. (2019). Traffic management for urban air mobility. In  
NASA formal methods symposium (pp. 71–87). Springer.  
Bharadwaj, S., Wongpiromsarn, T., Neogi, N., Muffoletto, J., &  
Topcu, U. (2021). Minimum-violation traffic management for urban  
air mobility. In NASA formal methods symposium (pp. 37–52).  
Springer.SUN ET AL . 131  
Brittain, M., Yang, X., & Wei, P. (2020). A deep multi-agent reinforce-  
ment learning approach to autonomous separation assurance. arXiv  
preprint arXiv:2003.08353.  
Chen, J., Chen, L., & Sun, D. (2017). Air traffic flow management under  
uncertainty using chance-constrained optimization. Transportation  
Research Part B: Methodological, 102, 124–141.  
Chin, C., Gopalakrishnan, K., Egorov, M., Evans, A., & Balakrishnan,  
H. (2021). Efficiency and fairness in unmanned air traffic flow man-  
agement. IEEE Transactions on Intelligent Transportation Systems,  
22(9), 5939–5951.  
Codato, G., & Fischetti, M. (2006). Combinatorial benders’ cuts for  
mixed-integer linear programming. Operations Research, 54(4),  
756–766.  
Connors, M. M. (2020). Understanding risk in urban air mobility:  
Moving towards safe operating standards.  
Daskilewicz, M., German, B., Warren, M., Garrow, L. A., Boddupalli,  
S.-S., & Douthat, T. H. (2018). Progress in vertiport placement and  
estimating aircraft range requirements for evtol daily commuting.  
2018 aviation technology, integration, and operations conference.  
2884.  
Du, J., Zhao, L., Feng, J., & Chu, X. (2017). Computation offload-  
ing and resource allocation in mixed fog/cloud computing systems  
with min-max fairness guarantee. IEEE Transactions on Communi-  
cations, 66(4), 1594–1608.  
Faghih-Roohi, S., Ong, Y.-S., Asian, S., & Zhang, A. N. (2016).  
Dynamic conditional value-at-risk model for routing and scheduling  
of hazardous material transportation networks. Annals of Operations  
Research, 247, 715–734.  
Fontaine, P. (2023). Urban air mobility (uam) concept of operations v2.0.  
https://www.faa.gov/sites/faa.gov/files/Urban  
Ganji, M., Lovell, D. J., Ball, M. O., & Nguyen, A. (2009). Resource allo-  
cation in flow-constrained areas with stochastic termination times.  
Transportation Research Record, 2106(1), 90–99.  
Garrow, L. A., German, B. J., & Leonard, C. E. (2021). Urban air  
mobility: A comprehensive review and comparative analysis with  
autonomous and electric ground transportation for informing future  
research. Transportation Research Part C: Emerging Technologies,  
132, 103377.  
Gupta, S., & Bertsimas, D. J. (2011). Multistage air traffic flow manage-  
ment under capacity uncertainty: a robust and adaptive optimization  
approach.  
Hamdan, S., Cheaitou, A., Jouini, O., Granberg, T. A., Jemai,  
Z., Alsyouf, I., Bettayeb, M., & Josefsson, B. (2022). Central  
authority–controlled air traffic flow management: An optimization  
approach. Transportation Science, 56(2), 299–321.  
Hamdan, S., Cheaitou, A., Jouini, O., Jemai, Z., Alsyouf, I., & Bettayeb,  
M. (2018). On fairness in the network air traffic flow management  
with rerouting. 2018 9th international conference on mechanical and  
aerospace engineering (ICMAE). IEEE, 100-105.  
Hou, W., Fang, T., Pei, Z., & He, Q.-C. (2021). Integrated design  
of unmanned aerial mobility network: A data-driven risk-averse  
approach. International Journal of Production Economics, 236,  
108131.  
Jiang, N., & Xie, W. (2024). Distributionally favorable optimization: A  
framework for data-driven decision-making with endogenous out-  
liers. SIAM Journal on Optimization, 34(1), 419–458.  
Kleinbekman, I. C., Mitici, M. A., & Wei, P. (2018). Evtol arrival  
sequencing and scheduling for on-demand urban air mobility. 2018  
IEEE/AIAA 37th digital avionics systems conference (DASC).  
IEEE, 1-7.  
Kochenderfer, M. J., Holland, J. E., & Chryssanthacopoulos, J. P. (2012).  
Next-generation airborne collision avoidance system. Tech. rep.  
Massachusetts Institute of Technology-Lincoln Laboratory Lexing-  
ton.  
Kong, N., Schaefer, A. J., & Ahmed, S. (2013). Totally unimod-  
ular stochastic programs. Mathematical Programming, 138(1-2),  
1–13.  
Laporte, G., & Louveaux, F. V. (1993). The integer l-shaped method  
for stochastic integer programs with complete recourse. Operations  
Research Letters, 13(3), 133–142.  
Lei, X., Shen, S., & Song, Y. (2018). Stochastic maximum flow inter-  
diction problems under heterogeneous risk preferences. Computers  
& Operations Research, 90, 97–109.  
Lineberger, R., Hussain, A., & Rutgers, V. (2018). Change is in the  
air: The elevated future of mobility: What’s next on the horizon?  
https://www2.deloitte.com/content/dam/Deloitte/us/Documents  
/energy-resources/di-the-elevated-future-of-mobility.pdf  
Lulli, G., & Odoni, A. (2007). The European air traffic flow management  
problem. Transportation Science, 41(4), 431–443.  
Moug, K., Jia, H., & Shen, S. (2023). A shared-mobility-based frame-  
work for evacuation planning and operations under forecast uncer-  
tainty. IISE Transactions, 55(10), 971–984.  
Mueller, E. R., Kopardekar, P. H., & Goodrich, K. H. (2017). Enabling  
airspace integration for high-density on-demand mobility opera-  
tions. 17th AIAA aviation technology, integration, and operations  
conference. 3086.  
Mukherjee, A., & Hansen, M. (2009). A dynamic rerouting model  
for air traffic flow management. Transportation Research Part B:  
Methodological, 43(1), 159–171.  
Pelegrín, M., d’Ambrosio, C., Delmas, R., & Hamadi, Y. (2021). Urban  
air mobility: From complex tactical conflict resolution to network  
design and fairness insights.  
Powell, W. B., & Topaloglu, H. (2003). Stochastic programming in  
transportation and logistics. Handbooks in Operations Research and  
Management Science, 10, 555–635.  
Price, G., Helton, D., Jenkins, K., Kvicala, M., Parker, S., & Wolfe,  
R. (2020). Urban air mobility operational concept (opscon)  
passenger-carrying operations. https://ntrs.nasa.gov/citations  
/20205001587  
Radunovic, B., & Le Boudec, J.-Y. (2007). A unified framework for  
max-min and min-max fairness with applications. IEEE/ACM Trans-  
actions on Networking, 15(5), 1073–1083.  
Rahmaniani, R., Crainic, T. G., Gendreau, M., & Rei, W. (2017). The  
benders decomposition algorithm: A literature review. European  
Journal of Operational Research, 259(3), 801–817.  
Rajendran, S., & Srinivas, S. (2020). Air taxi service for urban mobil-  
ity: A critical review of recent developments, future challenges,  
and opportunities. Transportation Research Part E: Logistics and  
Transportation Review, 143, 102090.  
Rajendran, S., & Zack, J. (2019). Insights on strategic air taxi net-  
work infrastructure locations using an iterative constrained clus-  
tering approach. Transportation Research Part E: Logistics and  
Transportation Review, 128, 470–505.  
Rath, S., & Chow, J. Y. J. (2022). Air taxi skyport location problem  
with single-allocation choice-constrained elastic demand for airport  
access. Journal of Air Transport Management, 105, 102294.  
Rockafellar, R. T., & Uryasev, S. (2000). Optimization of conditional  
value-at-risk. Journal of Risk, 2, 21–42.  
Rodionova, O., Arneson, H., Sridhar, B., & Evans, A. (2017). Efficient  
trajectory options allocation for the collaborative trajectory options  
program. 2017 IEEE/AIAA 36th digital avionics systems conference  
(DASC). IEEE, 1-10.  
Schrank, D., Albert, L., Eisele, B., & Lomax, T. (2021). Urban mobility  
report 2021.132 SUN ET AL .  
Shapiro, A., & Ahmed, S. (2004). On a class of minimax stochastic  
programs. SIAM Journal on Optimization, 14(4), 1237–1249.  
Shapiro, A., Dentcheva, D., & Ruszczynski, A. (2021). Lectures on  
stochastic programming: Modeling and theory. SIAM.  
Shehadeh, K. S. (2023). Distributionally robust optimization approaches  
for a stochastic mobile facility fleet sizing, routing, and scheduling  
problem. Transportation Science, 57(1), 197–229.  
Speranza, M. G. (2018). Trends in transportation and logistics. European  
Journal of Operational Research, 264(3), 830–836.  
Sun, L., Xie, W., & Witten, T. (2022). Distributionally robust fair transit  
resource allocation during a pandemic. Transportation Science.  
Thipphavong, D. P., Apaza, R., Barmore, B., Battiste, V., Burian, B.,  
Dao, Q., Feary, M., Go, S., Goodrich, K. H., & Homola, J. (2018).  
Urban air mobility airspace integration concepts and considerations.  
2018 aviation technology, integration, and operations conference.  
3676.  
Toth, P., & Vigo, D. (2002). The vehicle routing problem. SIAM.  
Toumazis, I., & Kwon, C. (2013). Routing hazardous materials on  
time-dependent networks using conditional value-at-risk. Trans-  
portation Research Part C: Emerging Technologies, 37, 73–92.  
United Nations. (2018). World Urbanization Prospects 2018.  
https://population.un.org/wup/Download/  
Vascik, P. D., & Hansman, R. J. (2017). Evaluation of key opera-  
tional constraints affecting on-demand mobility for aviation in the  
Los Angeles basin: Ground infrastructure, air traffic control and  
noise. 17th AIAA aviation technology, integration, and operations  
conference. 3084.  
Wang, K., & Jacquillat, A. (2020). A stochastic integer program-  
ming approach to air traffic scheduling and operations. Operations  
Research, 68(5), 1375–1402.  
Wang, Z., Delahaye, D., Farges, J.-L., & Alam, S. (2022). Complex-  
ity optimal air traffic assignment in multi-layer transport network  
for urban air mobility operations. Transportation Research Part C:  
Emerging Technologies, 142, 103776.  
Wu, P., Xie, J., Liu, Y., & Chen, J. (2022). Risk-bounded and  
fairness-aware path planning for urban air mobility operations  
under uncertainty. Aerospace Science and Technology,  
127, 107738.  
Wu, Z., & Zhang, Y. (2021). Integrated network design and demand fore-  
cast for on-demand urban air mobility. Engineering, 7(4), 473–487.  
Yu, X., Shen, S., & Ahmed, S. (2021). On the value of multi-  
stage stochastic facility location with risk aversion. arXiv preprint  
arXiv:2105.11005.  
Yu, X., Shen, S., & Wang, H. (2021). Integrated vehicle routing and  
service scheduling under time and cancellation uncertainties with  
application in nonemergency medical transportation. Service Sci-  
ence, 13(3), 172–191.  
Zhu, G., Wei, P., Hoffman, R., & Hackney, B. (2018a). Centralized  
disaggregate stochastic allocation models for collaborative trajec-  
tory options program (ctop). 2018 IEEE/AIAA 37th digital avionics  
systems conference (DASC). IEEE, 1-10.  
Zhu, G., Wei, P., Hoffman, R., & Hackney, B. (2018b). Saturation  
technique for optimizing planned acceptance rates in traffic man-  
agement initiatives. 2018 21st international conference on intelligent  
transportation systems (ITSC). IEEE, 3536-3543.  
SUPPORTING INFORMATION  
Additional supporting information can be found online in the  
Supporting Information section at the end of this article.  
How to cite this article: Sun, L., Deng, H., Wei, P.,  
& Xie, W. (2025). On a fair and risk-averse urban air  
mobility resource allocation problem under demand  
and capacity uncertainties. Naval Research Logistics  
(NRL), 72(1), 111–