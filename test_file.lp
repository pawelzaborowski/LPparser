/* Objective function */
min: a_a + a_b + a_c + b_a + b_b + b_c + c_a + c_b + c_c ;

/* Variable bounds */ 

- a_a + a_b + a_c - b_a - c_a = 1;
- a_b + b_a - b_b + b_c - c_b = 0;
- a_c - b_c + c_a + c_b - c_c = -1;

int b_a, a_b, c_a, a_c, c_b, b_c;
