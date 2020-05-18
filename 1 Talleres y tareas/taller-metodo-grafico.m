%% Funcion a maximizar %%
%% Z = 700T + 600t %%
%% S.A.%%
%% 2T + 0t <= 8 %%
%%  T + 3t <= 6 %%
%% 2T + 2t <= 9 %%

title({'Taller Método Gráfico';'Ejercicio 1 - Maximización'})

xlabel('Telefonos') 
ylabel('Tabletas') 

hold on;

% evaluando en 0's %
##T1 = 0;
##R1 = 8/(2*T1);
##R2 = 6/((T1) * (3*t1));
##R3 = 9/((2*T1) * (2*t1));
##
##% evaluando en 0's %
##t2 = 0;
##Re1 = 8/(2*T2);
##Re2 = 6/((T2) * (3*t2));
##Re3 = 9/((2*T2) * (2*t2));
##
##Z = 700*T+600*t;

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

X=[0 0.1 0.2 0.3 0.4 0.5 0.6 0.75 1 1.05 1.5 1.6 1.9]
Y=[0 4 0 4 0 4 0 3.75 0 2.82 0 1.15 0]

legend({'Res. 3','Res. 1','Res. 2'},'Location','southwest')

plot(X,Y);
hold on;

