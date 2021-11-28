# Useful info
* All data is stored in the data directory.
* All relevant scripts for data collection is in the root directory
* All supporting scripts from Cambridge Moodle and testing script from TianYao Ding is in the scripts directory


# Cubic Equation Solver

taken from https://github.com/shril/CubicEquationSolver


* Used as a subsitute of np.roots() function which utilizes Eigen Value Matrix Method for finding roots of the polynomial.

  

* ~6x faster than np.roots but exclusive to cubic polynomials.

  

* Manages the issue of inherent in the power basis representation of the polynomial in floating point numbers.

  

* Time Complexity of snippet is O(1).

  

[Algorithm Link](http://www.1728.org/cubic2.htm)

  

### Sample Code
```python
import CubicEquationSolver

CubicEquationSolver.solve(1, 0, 1, 0)
```
```
Output: [ 0.+0.j  0.+1.j -0.-1.j]
```

  

# theoretical

* **theoretical_analysis(lambda_number=1, plot=True)** will calculate the theoretical data for each mass variation. Corresponding lambda_numbers are:
	* 1 = Varying mass in top floor
	* 2 = Varying mass second floor
	* 3 = Varying mass in first floor
	* 4 = Varying mass in every floor

* The return output is the mass list and list of frequency lists corresponding to the the natural frequencies in ascending order i.e. frequencies = [f1_list, f2_list, f3_list]

* If plot is true then will plot data

### Sample Code

```python

from theoretical import theoretical_analysis

m_theo, frequencies_theo = theoretical_analysis(lambda_number=1, plot=False)
print(m_theo[0], frequencies_theo[0][0])

```

```

Output: 1.83 3.1964911958061184

```

# Data Collection
* **data_plot(load_type, on_one_graph=True)** will plot the data according to the load type (refer to theoretical section for the load type definitions). Graph will be frequency against mass.
	* To run the script, navigate to the bottom part of data_plotter.py and change the parameter.
	* To get all the data on a different graph for each mode in each load type, set on_one_graph to False.


* **compare_load_type(mode_type, plot_type=["theoretical"], range_load_type=[1,2,3,4])** will plot all the load types according to the mode of the natural frequencies specify.

	* mode_type refers to the mode of the natural frequency where mode_type=1 is mode 1, mode_type=2 is mode 2 etc.

	* plot_type will specify what data will be plotted eg. plot_type=["theoretical", "simulation", "experimental"] will plot out all the data while plot_type=["simulation"] will plot only the simulation.

	* range_load_type will specify the load types you want to plot eg range_load_type=[1,3,4] will plot load type 1,3 and 4 (cant go over 4 for obvious reasons).