%https://docplayer.es/22413366-Programacion-lineal-con-matlab.html
clc;
x = 0 : 10 ;%rango para la grafica

y1 = max(8/2);% 2x + 0y<= 8
y2 = max(6-3*x);% x + 3y<=6
y3 = max((9-2*x)/2);% 2x + 2y<=9
%y4 = max(2 ,0)*ones(1 ,9);% y<=2
%y4 = max(2 ,0)*ones(1 ,9);% y>=0
%y5 = max(2 ,0)*ones(1 ,9);% y>=0

%ytop=min([y1;y2;y3;y4]); %vector de minimos
ytop=min([y1;y2;y3]);
%ytop=min([y1;y2;y3;y4;y5]);

area(x,ytop);%se rellena la area

hold on;
[u v]= meshgrid(0:8,0:8);%rango de la grafica

contour(u,v,600*u+700*v);%evaluar z en el rango defindo

%% Draw the line

x1 = [4.5 0];
y = [0 4.5];

z = [0 7];
w = [4 4];

a = [0 2];
b = [6 0];

plot(x1,y);
hold on;
plot(z,w);
hold on;
plot(a,b);
hold on;

hold off;
