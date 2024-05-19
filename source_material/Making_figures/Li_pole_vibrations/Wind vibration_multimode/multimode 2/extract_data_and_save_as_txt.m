clear;
close all;
clc;

%%

fig=openfig('PSD_multimode_logscale.fig');
dataObjsY = findobj(fig,'-property','YData');
y1 = dataObjsY(1).YData;
y2 = dataObjsY(2).YData;
dataObjsX = findobj(fig,'-property','XData');
x1 = dataObjsX(1).XData;
x2 = dataObjsX(2).XData;


A=[];
A(:,1)=x1;
A(:,2)=y1;
A(:,3)=x2;
A(:,4)=y2;
dlmwrite('xxxxx.txt',A,',');


data = [x1;y1;y2]';

writematrix(data,'vibration_data.csv') 

%%

clear;
close all;
clc;



fig=openfig('Windvibratoin_timehisoty.fig');
dataObjsY = findobj(fig,'-property','YData');
y1 = dataObjsY(1).YData;
y2 = dataObjsY(2).YData;
dataObjsX = findobj(fig,'-property','XData');
x1 = dataObjsX(1).XData;
x2 = dataObjsX(2).XData;


A=[];
A(:,1)=x1;
A(:,2)=y1;
A(:,3)=x2;
A(:,4)=y2;
dlmwrite('xxxxx.txt',A,',');


data = [x1;y1;y2]';

writematrix(data,'time_data.csv') 






