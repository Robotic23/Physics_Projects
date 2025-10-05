Title: Determination of Acceleration due to Gravity (g) using a Simple Pendulum

Objective:-
To determine the value of the acceleration due to gravity  𝑔  by measuring the time period of a simple pendulum of different lengths and plotting  𝑇^2 versus L.

Apparatus / Tools:-
1. Python program (Pendulum simulation)
2. Computer with Python and Matplotlib installed
3. Input data: pendulum lengths and measured periods
In a real lab, this would include:
1. String / thread
2. Bob (metal sphere)
3. Stopwatch
4. Meter scale

Procedure:
1. Input the lengths of the pendulum (L) in meters for multiple observations.
2. For each length, input the time period (T) in seconds.
3. The program calculates T² for each observation.
4. The program computes the slope of the T² vs L graph.
5. Using the formula:
T=2π*sqrt(l/g)​ ​⟹ g= 4π^2/slope of graph 
the acceleration due to gravity 𝑔  is calculated.
6. The program also plots T² vs L with a straight line to visualize the relationship.

Observations:
Observation	| Length L (m)	| Time Period T (s) | T² (s²)
1           	0.25	          1	                    1
2	            0.36	          1.2	                  1.44
3	            0.64	          1.6	                  2.56
4	            0.81	          1.8	                  3.24
5	            1	              2                    	4

Slope of T² vs L graph ≈ 0.404 s²/m
Calculated g ≈ 9.87 m/s²

Graph shows a straight line through origin, confirming T^2∝L.

Conclusion

1. The simulation confirms that the time period squared (T²) is directly proportional to the pendulum length (L).
2. Using the slope of the T² vs L graph, the acceleration due to gravity was determined as g ≈ 9.87 m/s², which is close to the standard value 9.8 m/s².
3. This Python-based simulation effectively replicates a real lab experiment and helps visualize the linear relationship between T^2 and L.

