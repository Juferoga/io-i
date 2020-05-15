% PorFin 

x = -1 : 1 : 7; % intervalo  para  generar  las  rectas
z = (21 - 5. * x )/4;  % funcíon   a  maximizar

% restricciones
R1 = (24 - 6. * x )/4;
R2 = (6 - x )/2;
R3 = 1+x ;

for r = 1: length ( x )  % constantes
R4(r) = 2;
R5(r) = 0;
R6(r) = 0;
end

%grafica de las funciones considerando igualdades
figure(1) ;
plot(x ,z ,'-k' ) ;
hold  on ;
plot(x,R1,'-b',x ,R2,'-b ',x,R3,'-m',x ,R4,'-m') ;
plot(R5,x,'-r ',x,R6,'-r ') ;
grid on