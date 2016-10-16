zip movie.zip movie.flv 
tar -cvf movie.tar movie.flv 
tar cvfz movie.tar.gz movie.flv 
tar cvfj movie.tar.bz2 movie.flv
-rw-rw-r-- 1 harish harish 629M Oct 16 12:42 movienew.tar.bz2
-rw-rw-r-- 1 harish harish 633M Oct 16 12:29 movie.tar
-rw-rw-r-- 1 harish harish 629M Oct 16 12:45 movie.tar.bz2
-rw-rw-r-- 1 harish harish 629M Oct 16 12:36 movie.tar.gz
-rw-rw-r-- 1 harish harish 629M Oct 16 12:28 movie.zip

# Instalation ffmpeg : sudo apt-get install ffmpeg 
compression command : ffmpeg  -i movie.flv -qscale 4 -strict -2 outputffpeg.mp4
-rw-rw-r-- 1 harish harish 467M Oct 16 13:51 outputffpeg.mp4   # Compression result
