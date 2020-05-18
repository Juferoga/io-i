A = [[8 7];   % 8x + 7y <= 1000
     [10 6];   %  10x +  6y <= 1500
     [-11 -10];   % 11x + 10y >= 900
     [-7 -6];   %  7x +  6y >= 500
     [-1 0];  % non-negativity constraint x>=0
     [0 -1];  % non-negativity constraint y>=0
    ];
b = [1000;
     1500;
     -900;
     -500;
     0;
     0;
    ];
lower_b = [0; 0];
upper_b = [150; 150];
c = [86; 76];


figure(1)
[sorted_vertices, ...
 h_fes, h_bnd, h_fill, h_vert, h_int, h_max, g_labels] = ...
    plot_feasible(A, b, c, lower_b, upper_b, ...
		  'linecolor', 'b', ...
		  'linestyle', '-', ...
		  'filllinestyle', '--', ...
		  'backgroundcolor', [0.6 1 1], ...
		  'linesep', 0.5, ...
		  'plot_vertices', 'ko', ...
		  'label_vertices', 3, ...
		  'label_vertices_size', 14, ...
		  'label_vertices_prec', 0, ...
		  'label_vertices_color', 'b', ...
		  'plot_max', 'r*');
set(h_max, 'markersize', 18)
d = 1.6;
%text(d, 4.9, 'maximize', 'fontsize', 18);
%text(d, 4.5, '  f = 2x + 3y', 'fontsize', 18, 'FontName', 'Courier');
%text(d, 4.1, 'subject to ', 'fontsize', 18);
%text(d, 3.7, '  2x + 4y \leq 12', 'fontsize', 18, 'FontName', 'Courier');
%text(d, 3.3, '   x +  y \leq 4', 'fontsize', 18, 'FontName', 'Courier');
%text(d, 2.9, '        x \geq 0', 'fontsize', 18, 'FontName', 'Courier');
axis square
set(gcf, 'PaperPosition', [0 0 4 4]);
print('-dpng', 'plot_feasible.png');