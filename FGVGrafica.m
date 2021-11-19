function [] = FGVGrafica(plot_x, plot_fondo, plot_y, plot_yc, plot_yn)
    figure; hold on; grid on;
    plot(plot_x, plot_fondo, 'Color', '#804000');
    plot(plot_x, plot_y, 'Color', '#4472C4');    
    plot(plot_x, plot_yc, 'Color', '#FF000');
    plot(plot_x, plot_yn, 'Color', '#70AD47');
    legend('Fondo', 'Altura', 'yc', 'yn');
    xlabel('x');
    ylabel('Altura');
    title('Perfil de flujo (m)');
    savefig('./GraficaFGV.fig'); 
    
end

