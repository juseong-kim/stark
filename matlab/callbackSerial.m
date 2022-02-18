function callbackSerial(ser,~)
global time;
fprintf(ser,"VAL?");
val = fscanf(ser,'%s',14);
fix = extractBetween(val,":","m")
numval = str2double(fix);
time(16) = numval;
time(1)=[];
disp(time);
plot(time);
end