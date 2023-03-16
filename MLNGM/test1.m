% Get all text files in the current folder
files = dir('C:\Mina\LMISA-master\data\*.png');
% Loop through each file 
for id = 1:length(files)
    % Get the file name 
    [~, f,ext] = fileparts(files(id).name);
    rename = strcat(f,'_img',ext) ; 
    movefile ([files(id).folder '/' files(id).name] , [files(id).folder '/' rename]); 
end
    