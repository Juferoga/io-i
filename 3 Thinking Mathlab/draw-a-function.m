
y1= 0;
t1= 4,5;

x1= 0;
T1= 4,5;

coefficients = polyfit([x1, t1], [y1, T1], 1);
a = coefficients (1);
b = coefficients (2);

plot(a,b);
hold on;

y1= 0;
t2= 2;

x1= 0;
T2= 6;

coefficients2 = polyfit([x1, t2], [y1, T2], 1);
c = coefficients2 (1);
d = coefficient2s (2);

plot(c,d);
hold on;

T3= 4;

line ([0 1], [T3 T3], "linestyle", "-", "color", "b");

title (" Minimizar z = 700T + 600t ");
legend ('"-"', '"--"', '":"', '"-."', 'location', 'eastoutside');

