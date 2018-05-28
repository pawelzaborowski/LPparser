/* Objective function */
min: 5a_b + 3a_c + b_a + b_c + 4b_d + 2b_e + 5c_b + d_e + d_f + 3e_f + 0.0f_a ;

/* Variable bounds */ 

a_b + a_c - b_a - c_a = 1;
- a_b + b_a + b_c + b_d + b_e - c_b - d_b - e_b = 0;
- a_c - b_c + c_a + c_b = 0;
- b_d + d_b + d_e + d_f - e_d - f_d = 0;
- b_e - d_e + e_b + e_d + e_f - f_e = 0;
- d_f - e_f + f_d + f_e = -1;

int b_a, a_b, c_a, a_c, d_b, b_d, e_b, b_e, f_b, b_f, d_c, c_d, e_d, d_e, f_e, e_f;
