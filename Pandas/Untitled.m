% fid = fopen('Node7.bin');
% m5 = fread(fid, [600000, 2], '*float32');
% fclose(fid);

tic
a = importdata('Node7.out');
toc