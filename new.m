global time;
global s;
clear all; close all; clc;

time=zeros(1,15);
%fclose(instrfind);
s= serial('/dev/cu.usbserial-14110','BaudRate',115200.0);
s.BytesAvailableFcnMode = 'terminator';
s.BytesAvailableFcn={@callbackSerial};

fopen(s);
