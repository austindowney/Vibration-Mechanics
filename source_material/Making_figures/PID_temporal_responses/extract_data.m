clear;
close all;
clc;

%%

fig=openfig('PID_1.fig');
dataObjsY = findobj(fig,'-property','YData');
y1 = dataObjsY(1).YData;
y2 = dataObjsY(2).YData;
dataObjsX = findobj(fig,'-property','XData');
x1 = dataObjsX(1).XData;
x2 = dataObjsX(2).XData;


% A=[];
% A(:,1)=x1;
% A(:,2)=y1;
% A(:,3)=x2;
% A(:,4)=y2;

data = [x1;y1;y2]';

writematrix(data,'PID_data.csv') 


