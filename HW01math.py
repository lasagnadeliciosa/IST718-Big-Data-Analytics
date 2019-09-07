#!/usr/bin/env python
# coding: utf-8

# # IST 718: Big Data Analytics
# 
# - Professor: Willard Williamson <wewillia@syr.edu>
# - Faculty Assistant: Palaniappan Muthukkaruppan
# ## General instructions:
# 
# - You are welcome to discuss the problems with your classmates but __you are not allowed to copy any part of your answers from your classmates.  Short code snippets are allowed from the internet.  Any code is allowed from the class text books or class provided code.__
# - Please do not change the file names. The FAs and the professor use these names to grade your homework.
# - Remove or comment out code that contains `raise NotImplementedError`. This is mainly to make the `assert` statement fail if nothing is submitted.
# - The tests shown in some cells (i.e., `assert` and `np.testing.` statements) are used to grade your answers. **However, the professor and FAs will use __additional__ test for your answer. Think about cases where your code should run even if it passess all the tests you see.**
# - Before submitting your work through Blackboard, remember to save and press `Validate` (or go to 
# `Kernel`$\rightarrow$`Restart and Run All`).

# ## Math (50 pts)

# ## Probability (40 pts)

# The cell below creates a string named pi out to one million decimal places.  Note that this cell may take a few minutes to run to completion.

# In[73]:


import numpy as np
num_pi_digits = 1000000

try:
    # import version included with old SymPy
    from sympy.mpmath import mp
except ImportError:
    # import newer version
    from mpmath import mp
mp.dps = num_pi_digits  # set number of digits

# convert pi to a string
pi = mp.nstr(mp.pi, num_pi_digits)

# print to 100 decimal places
print(pi[:100])

# remove the decimal point
pi = pi.replace(".", "")


# **Question 3.1 (5 pts)** Compute and print the marginal probabilites $P(X_i)$ where X = 0, 1, 2, 3, ..., 9 across all numbers (before and after the decimal point).  Your answer should print 10 marginal probabilities.

# In[72]:


# Your answer here
counts = [0] * 10 #create an empty list to store the counts
for num in pi:
    counts[int(num)] += 1

probs = []  
for count in counts:
    probs.append(str(count/len(pi)))
    
print(' '.join(probs))


# **Question 3.2 (5 pts)** What kind of distribution do the probabilities in 3.1 suggest?

# In[15]:


# your answer here
#The distribution of the numbers are pretty even, with each digits appearing around 10% of the time.


# **Question 3.3 (10 pts)** Compute the joint probability $P(x_i = 1, x_i-1 = 3)$.  Based on the result, what can you say about the independence relationship?

# In[63]:


# your answer here
#joint probability is AND

jointCount = 0

for i in range(1, len(pi)):
    if pi[i] == '1' and (pi[i-1]) == '3':
        jointCount +=1
        
print(jointCount/(len(pi)-1))

#based on the result, the independent relationship is very rare, occuring around 1% of the time.


# **Question 3.4 (10 pts)** Compute the conditional probability $P(x_i = 3 | x_i-1 = 1)$. 

# In[65]:


# your answer here
denominator = 0
numerator = 0

for i in range(1, len(pi)):
    if pi[i-1] == '1':
        denominator += 1
        if pi[i] == '3':
            numerator +=1

print(numerator/denominator)counts = [0] * 10
for num in pi:
    counts[int(num)] += 1

probs = []  
for count in counts:
    probs.append(str(count/len(pi)))
    
print(' '.join(probs))


# **Question 3.5 (10 pts)**
# Assuming that the decimal point is removed from pi, let A be the pi values at indices 1-1000, let B be the pi values at indices 2-1001, let C be the pi values at indices 3-1002.  Compute the sample covariance matrix for A, B, C against each other. without using the built-in command (i.e. code it yourself). The result should be a 3x3 matrix.

# In[92]:


# Your answer here
#Cov(X, Y) = Σ ( Xi - X ) ( Yi - Y ) / N = Σ xiyi / N
# without using build in command such as NumPy
def covariance(x,y):
    u = sum(x)/len(x)
    v = sum(y)/len(y)
    E = 0
    for i in range(len(x)):
        E += (x[i] - u) * (y[i] - v)
    return E/(len(x)-1)

#create the three arrays
A = [int(i) for i in pi[1:1001]]
B = [int(i) for i in pi[2:1002]]
C = [int(i) for i in pi[3:1003]]

#3x1000 matrix
stack = [A, B, C]
#create empty matrix
samp_cov_matrix = []

for X in stack:
    row_cov = []
    for Y in stack:
        row_cov.append(covariance(X,Y))
    samp_cov_matrix.append(row_cov)

print(samp_cov_matrix)


# In[91]:


# with NumPy, much easier
arrayA = np.array(A)
arrayB = np.array(B)
arrayC = np.array(C)

x = np.vstack([arrayA,arrayB,arrayC])
samp_cov_matrix = np.cov(x)

print("samp_cov_matrix:\n")
print(samp_cov_matrix)


# ## Linear Algebra (10 pts)

# **Question 3.5 (5 pts)** Compute the following matrix multiplications
# $$
# \quad
# \begin{bmatrix} 
# 1 \\
# 2 \\
# 3
# \end{bmatrix}
# \quad
# *
# \quad
# \begin{bmatrix} 
# 4 & 5 & 6
# \end{bmatrix}
# \quad
# $$

# In[70]:


# your answer here
# 3x1 matrix
X = np.array([[1],[2],[3]])
# 1x3 matrix
Y = np.array([[4,5,6]])

print(X.dot(Y))


# **Question 3.6 (5 pts)** Compute the following matrix multiplications
# 
# $$
# \quad
# \begin{bmatrix} 
# 1 & 2 \\
# 3 & 4 \\
# 6 & 0 \\
# \end{bmatrix}
# \quad
# *
# \quad
# \begin{bmatrix} 
# 2 & 5 & 3\\
# 2 & 5 & 1
# \end{bmatrix}
# \quad
# *
# \quad
# \begin{bmatrix} 
# 1\\
# 2\\
# 1
# \end{bmatrix}
# \quad
# $$

# In[71]:


# your answer here
#3x2 matrix
X = np.array(
    [[1,2],
     [3,4],
     [6,0]])
# 2x3 matrix
Y = np.array(
    [[2,5,3],
     [2,5,1]])
# 3x1 matrix
Z = np.array(
    [[1],
     [2],
     [3]])

print(X.dot(Y).dot(Z))

#[51]
#[123]
#[126]


# **Extra Credit (5 pts)**  This question is optional.  If you choose to answer this question, you will earn 5 extra credit points.  If you choose not to answer this question, no points will be deducted from your score.  Solve the following equation for $c$ symbolically using the python sympy package.  Convert the solved symbolic solution to a latex format (this can be done with a pyton call), then populate the solution cell with the resulting latex code so that your solution shows up symbolically similar the equation below.
# 
# $$c g - c h + e \left(a + 1\right)^{b} - \frac{d \left(\left(a + 1\right)^{b} - 1\right)}{a} + \frac{f \left(\left(a + 1\right)^{b} - 1\right)}{a} = 0$$

# In[ ]:


# your code here


# Your solved equation in latex here:
# 
