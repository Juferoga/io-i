%% Funcion a minimizar %%
%% Z = 150X + 300Y %%
%% S.A.%%
%% 16X + 4Y <= 32 %%
%%  2X + 2Y <= 10 %%
%%  4X + 14Y <= 40 %%

title({'Taller Método Gráfico';'Ejercicio 1 - Minimización'})

xlabel('Mayorista A') 
ylabel('Mayorista B')

x1 = [2 0];
y = [0 8];

z = [5 0];
w = [0 5];

a = [10 0];
b = [0 (40/14)];

plot(x1,y);
hold on;

plot(z,w);
hold on;

plot(a,b);
hold on;

X=[0.16 0.5 0.7 1.11 1.22 1.30 1.38 1.80] 
Y=[2.79 0 2.6 0 2.51 0 2.46 0]

legend({'Res. 3','Res. 1','Res. 2'},'Location','northeast')

plot(X,Y);
hold on;