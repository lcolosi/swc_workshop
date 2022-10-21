#!/usr/bin/env python
# coding: utf-8

# # Programming with Python: A General Python Workshop Tutorial for New Python Users 

# ### Table of Contents

# 1) Getting started with Python (Downloading software and botting up python on the terminal)
# 
# 2) Introduction to Jupyter Notebooks environment and libraries 
# 
# 3) Variable types
# 
# 4) Common Mathematical Operations
# 
# 4) Analyzing Data 
# 
#     a) Slicing arrays  
# 
#     b) Statistical operations on arrays
# 
#     c) for loops 
# 
#     d) Working with lists/ List comprehension
# 
#     e) Conditional statements: Making Choices
# 
#     f) Creating Functions 
# 
#     g) Calling data in .nc and .txt formats
#     
#     h) Visualize data: Plotting 
# 
#     i) Errors and Exceptions 
# 
#     j) Defensive Programming 
# 
#     k) Debugging 
# 
# 5) Resources 

# ### Getting started with Python 

# The Python program can be ran via three main platforms: 
# 
# **1) Anaconda or Miniconda**: These two platforms can be installed onto your computer via the app store for Anaconda and via the terminal for miniconda. Anaconda comes with most packages included in the downloading process. Miniconda however does not, but this allows you to customize your packages to fit your needs. The packages are easily installable via the terminal command-line. Both platforms utilize a browser window in order to run python through Jupyter Notebooks. Install Anaconda (https://www.anaconda.com/distribution/) and Miniconda (https://docs.conda.io/en/latest/miniconda.html) from online references. To boot up the anaconda, type "jupyter notebooks" into the command line in the terminal. The Jupyter Notebook kernal will be launched and have the root starting in the directory you were currently in. Note that Jupyter Notebooks **REQUIRES INTERNET**. 
# 
# **2) IPython**: IPython is a command-line python kernal that allows you to code directly into the terminal. IPython can be installed through miniconda and should be automatically installed with Anaconda. To boot up, type ipython into the command -line in the terminal
# 
# We will focus in the Jupyter Notebook Enviroment from hereon. 

# ### Introduction to Jupyter Notebook's Environment 

# Once a kernal is initiated, under the file tab you will see a list of directories and files under the directory which you booted jupyter notebooks in. From here, will be able to go through the file system to find and launch your .ipynb files. If this is the first time running jupyter notebooks, you can create a new directory (outside the jupyter notebook environment) and create a new notebook within this directory by location the new directory and clicking new in the top right corner. Under the running tab in the top left side of the kernal directory page, you can see currently running notebooks and studown or continue them. In the center of the page you can see the current directory and the path to that directory in the blue text. 
# 
# Now that a new Kernal has been created, complete the following: 
# 
# 1) Rename the Notebook at the top center of the page from Untitled to something descriptive. Make sure to not include spaces, wildcards or quotes in the name. 
# 
# 2) Give a title to your notebook with a longer less abreviated description of the purpose of the notebook using a mark down cell (esc + m) and increase fontsize and bold title with esc + 1 or 2 
# 
# Use mark down cell throughout the notebook to describe what the code is doing at each step in order for readers to easy follow. 
# 
# Play around with the drop down menus and the toolbar to fimilarize yourself with the enivorment. The most critical things to note are the short cuts to the toolbar above. Here are a few of the important ones: 
# 
# 1) esc + m = convert a code cell to a markdown cell
# 
# 2) esc + y = convert a markdown cell to a code cell 
# 
# 3) shift + enter = run current cell 
# 
# 4) esc + a = Insert a cell above the current cell 
# 
# 5) esc + b = Insert a cell below the current cell
# 
# 6) esc + x = Cut the current cell
# 
# By pressing esc, you place the notebook in command mode. By pressing enter or clicking the cell, you place the notebook in edit mode. To get a full list of short cuts =, press esc + h.

# ### Variable Types 

# **1) Integers/long numbers, floats, and complex**: Integers are exactly what you would expect (Whole numbers ranging from -inf to inf) while floats are any numbers with a decimal. Long numbers are integer numbers that have scientific notation or significantely large. Complex numbers are any numbers with an imaginary part. 
# 
# **2) Strings**: a collection of letters contained by two quotation marks '' or "".  
# 
# **3) Boolean**: a true or false binary variable 
# 
# **4) Tuples**: a immutable sequences of any tpye  of object elements from strings, floats, and integers (or booleans). Tuples parentheses and separate each element with a comma. 
# 
# **5) Lists**: a mutable sequence of any type of object including strings, floats, integers, and booleans.
# 
# **6) Arrays**: a mutable sequence
# 
# **7) Dictionaries**: an unordered collection of data values, used to store data values. Unlike other Data Types that hold only single value as an element, Dictionary holds key:value pair.
# 
#     e.g. monthly_data = {}
#          monthly_data = {'time': [], 'mean': [], 'median': [],'std': [],'N': [] }
# 

# ### Common Mathematical Operations 

# 1. a + b= elementwise addition 
# 
# 2. np.sum(a) = sum entire numpy array 
# 
# 3. a - b= elementwise subtraction
# 
# 4. a @ b or np.dot(a,b) = matrix multiplication 
# 
# 5. a * b = elementwise multiplication 
# 
# 6. a/b = elementwise division
# 
# 7. a//b = floor division 
# 
# 8. a**b = elementwise exponentiation 
# 
# 9. a.T = transpose of a
# 
# 10. a.conj().T = conjugate transpose of a

# ### Analyzing Data 

# Plot figures within jupyter notebook within following command: 

# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')


# Import Libraries (libraries contain commands for processing data)

# In[6]:


import numpy as np #library for working with arrays 
import matplotlib.pyplot as plt #library for plotting
from netCDF4 import Dataset, num2date #library commands used for reading in netCDF files 
import glob # use to create a list of filenames 


# Setting variables and printing value and attributes 

# In[7]:


swh = np.random.randint(0,6,size=(5,8))
print('Values of swh')
print(swh) 
print('Shape of swh where (rows,columns) = array.shape is:', swh.shape)
print('Type of variable is:', type(swh))
print('Type of number (integer, float, long number, or complex)is:', swh[0,0].dtype)


# **Slicing arrays**
# 
# Basics: 
# 
# 1) Array indices start at 0, not 1
# 
# 2) *Array[x,y]* selects a single element from the 2D array where x = row and y = column
# 
# 3) General syntax for an array: *array[start:stop:step]*
# 
# 4) Use *low:high* to specify a slice of the array along a dimension of the array including indices from *low* to *high-1*
# 
# 5) All indexing and slicing that works on arrays also works on strings 
# 
# 

# In[9]:


print(swh[2,3])
print(swh[0:3,4:8])
print(swh[4:])
print(swh[:3])
print(swh[-3:])
print(swh[0:5:2])
print(swh[::2])
print(swh[4:,5:])
print(swh[::-3])


# **Statistical operations on arrays** 

# In[10]:


#operation on the entire array
swh_mean = np.mean(swh)
swh_std = np.std(swh)
swh_max = np.max(swh)
swh_min = np.min(swh)
print(swh_mean, swh_std, swh_max, swh_min)
#operations along an axis 
swh_mean_column = np.mean(swh, axis=0) #calculate mean across row axis (down each column)
swh_mean_row = np.mean(swh, axis=1) #calculate mean across column axis (across each row)
print('')
print(swh_mean_row)
print('')
print(swh_mean_column)


# In[13]:


mean_test = (2 + 2 + 0 + 2 + 4 + 0 + 3 + 2)/8
print(mean_test)


# **for loops**
# 
# Syntax: 
# 
#     for variable in sequence:
# 
#         print(variable)
#         
# Purpose: Use for loops to process the elements of a squence one at a time

# In[36]:


#initalize list 
swh_list = []

for ilen in range(0,10,1):
    swh_list.append(ilen)
    
#look what swh_list looks like
print(swh_list)
print(len(swh_list))
print(np.size(swh_list))


# **Working with lists**
# 
# Basics:
# 
# 1) Lists are mutable (can be manipulated such that elements can be swapped, deleted, etc.) 
# 
# 2) Lists can contain multple types of variables
# 
# 3) Lists are indexed and sliced with square brackets (e.g., list[0] and list[2:9]), in the same way as strings and arrays.

# In[42]:


#create an empty list
wsp = []
#Create a populated list
wsp = [1.2, 3.5, 'air', 3.2, 3.1, [6.9, 3.8, 4.9]]
#Slicing List
print(wsp[2:4])
print(wsp[-1][1])


# **List Comprehension**: a powerful way of manipulating lists

# In[36]:


#Example of list comprehension
days = [str(i).zfill(2) for i in range(1,31)]
print(days)


# **Conditional statements**: Making Choices 
# 
# Syntax: 
# 
#     if condition: 
# 
#         print(swh)
#         
#     elif condition:
#     
#         print(wsp)
#         
#     else: 
#         
#         print(swh,wsp)
#         
# Other conditional statements: 
# 
#     a==b : test for equivalence
#     
#     Logical Operators: Used in conditional statements for determining whether two boolean arguments are true or false statements based on the following: 
# 
#     a and b:  returns TRUE if both the operands (right side and left side) are true
# 
#     a or b: returns TRUE if either of the operand (right side or left side) is true
#     
#     not a: returns TRUE if operand is false 
#     
#     Note that logicaal operators can only be used to comepare two boolean conditional statements and cannot be used in series. Use multiple conditional statements to save boolean results in variables that can be used later. 
#     
#     Bitwise operators: Bitwise operators compare corresponding digits in two binary numbers and return a result in binary form accordingly. 
#     
#     a & b: Bitwise ‘and’ (&) returns a binary number with 1 at digits where both of the corresponding digits of the operands are 1
# 
#     a | b: Bitwise ‘or’ (|) returns a binary number with 1 at digits where at least one of the digits of the operands was 1
#     
#     >=, <=, != : greater than or equal to, less than or equal to, not equal to 
#     
#     +=, - = , *=, /= : shortcut operators for addition, subtraction, multiplcation, and division which bypasses that step of redefining a variable after preforming one of the four operations on its self with another number  
#     
# Zero, empty strings, and empty lists are considered **False** 
# All other numbers, strings and lists are considered **True**
# True and False represents truth values

# In[10]:


#Logical operator example 
#Initialize variables 
swh_norcal = np.random.randint(0,8,size=(5,8))
swh_socal = np.random.randint(1,10, size=(5,8))

#Set conditional statement
if np.max(swh_norcal) > np.max(swh_socal) and np.min(swh_norcal) < np.min(swh_socal):
    print('Northern California has a larger spread of values than southern California')
elif np.max(swh_norcal) == np.max(swh_socal) or np.min(swh_socal) == np.min(swh_norcal:
    print('Northern California maybe has the same spread of values as southern California')
else: 
    print('Southern California has a larger spread of values than Northern California')


# In[13]:


#Bitwise operator examples 
print(0&1) # prints 0 (0000) since 0000 'and' 0001 => 0000
print(0|1) # prints 1 (0001), since 0000 'and' 0001 => 0001


# **Creating Functions**
# 
# **Syntax**: 
# 
#     def function_name(parameters): 
#         '''
#         Documentation
#         '''
#         #Code for function
#         
#         return variable_1, variable_2 #Output variables from function
# 
# **Basics**: 
#  
# 1) Variables defined within a function can only be seen and used within the body of the function.
# 
# 2) Specify default values for parameters when defining a function using name=value in the parameter list
# 
# 3) Parameters can be passed by matching based on name, by position, or by omitting them (in which case the default value is used)
# 
# **Purpose** of Functions are to automize and streamline your code in order to your code more efficient, easier to debug, and easier to write. Functions can be expanded upon to compelete a wide variety of tasks by adding conditional statements. 
# 
# **Importing functions** from .py files with the following code: 
# 
# import sys # import sys library 
# sys.path.append('/zdata/home/lcolosi/python_functions/') #using sys, give the notebook that path inorder to find the functions .py file 
# 
# #import functions 
# from unweighted_least_square_fit import least_square_fit 
# from char_LSF_curve import character_LSF
# from monthly_mean import monthly_average

# In[20]:


def wind_stress_mag(C_d, rho, U_10):
    
    '''
    Documentation Section: 
    
    wind_stress_mag(C_d, rho, U_10)
        
        Function for computing scalar wind stress magnitude 
        
        Parameter
        ---------
        C_d : wind drag coefficient 
        rho : air density (kg/m^3)
        U_10 : wind speed 10 meters above the suface of the water (m/s)
        
        Libraries necessary
        -------------------
        import numpy as np
    '''
    
    #import libraries
    import numpy as np
    
    #compute wind stress magnitude
    wsm = C_d*rho*U_10**2
    
    return wsm


# In[21]:


wsm = wind_stress_mag(0.001, 1.2, 10)
print(wsm)


# In[25]:


#Obtain documentation on function: 
get_ipython().run_line_magic('pinfo', 'wind_stress_mag')


# **Calling data in .nc and .txt formats**
# 
# **Basic steps for importing data into Jupyter notebooks**:
# 
# 1) Import libraries for calling netCDF or text files 
# 
#     a) netCDF files: from netCDF4 import Dataset, num2date
#     
#     b) Text files: import numpy as np
# 
# 2) Set the path to the data located locally on your computer. There are ways to obtain data located remotely, however that is not covered here. Paths are usually strings. 
# 
#     ex: filenames = '/zdata/downloads/colosi_data_bk/binned_data/ifremer_p1_daily_data/my_daily_binned_ifremer_data/ifremer_swh_daily_binned_data_93_16_bia.nc'
#     
#     If you need to import several files, use the glob library to compile a list of filenames that have a common filename structure or patter. Use wildcards (* or ?) in order to grab multiple files with the same beginning or endings. Use * in a pattern to match zero or more characters, and ? to match any single character.
#     
#     ex: filenames = sorted(glob.glob('/zdata/downloads/colosi_data_bk/binned_data/ccmpv2_wind_data/daily_binned_ccmp_v2_data/ccmp_v2_wsp_daily_binned_data_*_high_res.nc'))
#     
#     where the sorted function (built in function to python) returns a new list containing all items from the iterable in ascending order
# 
# 
# 3) From here, we take two separate paths for netCDF and text files 
# 
#     a) netCDF files: 
#     
#         #set nc variable in order to read attributes and obtained data: 
#         nc = Dataset(filenames[0], 'r')
#         
#         #print key variables:
#         print(nc.variables.keys())
#         
#         #call data 
#         swh = nc.variables['swh'][:]
#     
#     b) Text files: 
#     
#         #Call data 
#         chlorophyll = np.loadtxt(fname='/Users/lukecolosi/Downloads/chlorophyll-01.csv', delimiter=',')
#         
#    For netCDF files and text files, both will leave you with variables linked to data arrays 
# 

# In[39]:


#documentation on loading text files via numpy command
get_ipython().run_line_magic('pinfo', 'np.loadtxt')


# **Visualizing Data: Plotting**
# 
# **Basic types of plotting functions in matplotlib.pyplot library**:
# 
#     1) plt.plot() : line plots 
#     
#     2) plt.contour() : contour plots 
#     
#     3) plt.contourf() : contour filled plots (a discrete pcolor plot with countours)
#     
#     4) plt.pcolor() : colormap with continous or discrete colorbars
#     
#     5) plt.scatter() : scatter plot 
#     
#     6) plt.imshow() : image plot 
#        
#     7) plt.fill_between() : line plots with shadded regions 
#     
# **Single Figure Plotting**: 
# 
# **Plotting Subplots**: 
# 

# In[63]:


#Single Figure Plotting Example: 

#import extra libraries for plotting 
from matplotlib import cm

#import chlorophyll data 
chlorophyll = np.loadtxt(fname='/zdata/downloads/colosi_data_bk/txt_data/chlorophyll-01.csv',delimiter=',')
print(chlorophyll.shape[0])
print(chlorophyll)

#set variables 
profiles = np.arange(1,chlorophyll.shape[0]+1)
depth = -1*np.arange(1,chlorophyll.shape[1]+1)

#Method 1:
#fig = plt.imshow(chlorophyll)
#plt.colorbar()

#Method 2: 
#fig = plt.pcolor(profiles, depth, chlorophyll)
#plt.xlabel('Depth [m]')
#plt.ylabel('Number of profiles')
#plt.title('Chl concentration [mg/m^3]')
#plt.colorbar()

#Method 3: 
#levels = np.arange(0, 1.8, 0.1)
#fig = plt.contourf(profiles, depth, chlorophyll, levels=levels, cmap=cm.YlOrRd,
#                  extend='neither')
#plt.colorbar()

#Method 4: 
#chlorophyll_mean = np.mean(chlorophyll, axis=0)
#fig = plt.plot(chlorophyll_mean,depth)
#plt.xlabel('chl [mg/m^3]')
#plt.ylabel('Depth [m]')
#plt.title('Average Chl concentration')

#method 5: 


#Method 6: 
fig = plt.hist(chlorophyll.flatten(), bins = np.arange(0,1.8, 0.15))

#save figure
#plt.savefig(fname = '/zdata/downloads/colosi_data_bk/surfacewaves_python_figs/swa_frac_ocean/hist_partitioned_ocean', bbox_inches = 'tight', dpi=300)


# In[53]:


#Subplot Example: 

#import swh phase constant data from a .npz file 
ifremer_swh = np.load('/zdata/downloads/colosi_data_bk/binned_data/ifremer_p1_daily_data/my_daily_binned_ifremer_data/char_lsf_5par_npz/ifremer_swhcor_char.npz')

#set variables 
swh_amp1_m = ifremer_swh['swh_annual_amp']
swh_phase1_m = ifremer_swh['swh_annual_phase']

#initialize subplot axes: 
fig, axes = plt.subplots(1, 2, figsize=(6,4))

ax1, ax2 = axes.flatten()


# **Errors and Exceptions**
# 
# Tracebacks (error output) can look intimidating, but they give us a lot of useful information about what went wrong in our program, including where the error occurred and what type of error it was.
# 
# An error having to do with the ‘grammar’ or syntax of the program is called a SyntaxError. If the issue has to do with how the code is indented, then it will be called an IndentationError.
# 
# A NameError will occur if you use a variable that has not been defined, either because you meant to use quotes around a string, you forgot to define the variable, or you just made a typo.
# 
# Containers like lists and strings will generate errors if you try to access items in them that do not exist. This type of error is called an IndexError.
# 
# Trying to read a file that does not exist will give you an FileNotFoundError. Trying to read a file that is open for writing, or writing to a file that is open for reading, will give you an IOError.

# **Defensive Programming**
# 
# Program defensively, i.e., assume that errors are going to arise, and write code to detect them when they do.
# 
# Put assertions in programs to check their state as they run, and to help readers understand how those programs are supposed to work.
# 
# Use preconditions to check that the inputs to a function are safe to use.
# 
# Use postconditions to check that the output from a function is safe to use.
# 
# Test your program or function in order to make sure it is correctly preforming the way you want it to. Give your function or program an input with a know output and make sure this output is outputted. 
# 
# Write documentation before writing code in order to help determine exactly what that code is supposed to do and to assist future reader.

# **Debugging**
# 
# - Know what code is supposed to do before trying to debug it.
# 
# - Make it fail fast.
# 
# - Change one thing at a time, and for a reason.
# 
# - Keep track of what you’ve done.
# 
# - Be humble.

# ### Resources

# To obtain documentation on commands or functions built in to python, from imported libraries, or from your own self-programmed libraries, type help(function) or function?

# NumPy for Matlab Users: Gives python equivalent syntax for common matlab commands (https://docs.scipy.org/doc/numpy/user/numpy-for-matlab-users.html)

# ### Acknowledgements 

# Thank you to Software Carpentry for supply information and structure for this tutorial. Visit the Software Carpentry Website for further discussion: https://swcarpentry.github.io/python-novice-inflammation/reference/
