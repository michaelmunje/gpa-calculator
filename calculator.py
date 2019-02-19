#!/usr/bin/env python
# coding: utf-8

# In[29]:


class Grade():
    # (Units of class, Grade)
    A_plus = 4.0/4.0
    A = 4.0/4.0
    A_minus = 3.7/4.0
    B_plus = 3.3/4.0
    B = 3.0/4.0
    B_minus = 2.7/4.0
    C_plus = 2.3/4.0
    C = 2.0/4.0
    C_minus = 1.7/4.0
    D_plus = 1.3/4.0
    D = 1.0/4.0
    D_minus = 0.7/4.0
    F = 0.0/4.0
    
transcript = (
    # Replace with your own transcript
    (4.0, Grade.A),
    (4.0, Grade.A),
    (3.0, Grade.B_minus),
    (3.0, Grade.C_minus),
    (5.0, Grade.A_minus),
    (5.0, Grade.A),
    (3.0, Grade.A_minus),
)

grade_units = (total_units * gpa_percentage for total_units, gpa_percentage in transcript)
total_units = (total_units for total_units, gpa_percentage in transcript)

print('%.2f' % (sum(grade_units) / sum(total_units) * 4.0))

