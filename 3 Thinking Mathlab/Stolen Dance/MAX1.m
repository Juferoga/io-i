gasol = optimproblem('ObjectiveSense','max');
x = optimvar('x',2,1,'LowerBound',0);
gasol.Objective = 86*x(1) + 76*x(2);
cons1 = 8*x(1) + 7*x(2) <= 1000;
cons2 = 10*x(1) + 6*x(2) <= 1500;
cons3 = 11*x(1) + 10*x(2) >= 900;
cons4 = 7*x(1) + 6*x(2) >= 500;
gasol.Constraints.cons1 = cons1;
gasol.Constraints.cons2 = cons2;
gasol.Constraints.cons3 = cons3;
gasol.Constraints.cons4 = cons4;
show(gasol);
sol = solve(gasol);
sol.x