/* Objective function */
min: a_b + a_c + 8b_d + b_e + c_d + d_e ;

/* Variable bounds */ 

a_b + a_c = 1
- a_b + b_d + b_e = 0
- a_c + c_d = 0
- b_d - c_d + d_e = 0
- b_e - d_e = -1













bin: a_b, a_c, a_d, a_e, b_c, b_d, b_e, c_d, c_e, d_e;
