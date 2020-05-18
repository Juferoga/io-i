%problema  de  las  pinturas

x = 0 : 8 ;%rango para la grafica

y1 = max((24-6*x)/4,0);% 6x + 4y<= 24
y2 = max((6-x)/2 ,0);% x + 2y<=6
y3 = max(1+x,0);%−x + y<=1
y4 = max(2 ,0)*ones(1 ,9);% y<=2

ytop=min([y1;y2;y3;y4]); %vector de minimos

area(x,ytop);%se rellena la area
hold on;

[u v]= meshgrid(0:8,0:8);%rango de la grafica
contour(u,v,5*u+4*v);%evaluar z en el rango defindo
hold off;