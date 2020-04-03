p="\033[39;1m";a="\033[30;1m";m="\033[31;1m";h="\033[32;1m";k="\033[33;1m";b="\033[34;1m";z="";c="\033[35;1m";pu="\033[36;1m";n="\033[0m"
s="sleep 1"
lol="mjuli"
v3()
{
clear
printf "${p} ╔═════════════════════════════════════╗
${p} ║ ${b}Silahkan Bagi Yang Baru Menggunakan ${p}║
${p} ║ ${b}Tools Ini Di Sarankan Untuk Install ${p}║
${p} ║ ${b}Bahan2 Nya Dulu Yang Ada Di Bawah   ${p}║
${p} ║ ${b}Supaya Tidak Error Saat Menjalankan ${p}║
${p} ║ ${b}Tools Nya Caranya masuk ke Tool rus ${p}║
${p} ╠═════════════════════════════════════╝
${p} ║${m}      <═══════════════════════>
${p} ╠═════════════════════════════════════╗
${p} ║ ${h}Gunakan Tools Ini sebaik baiknya    ${p}║
${p} ║ ${h}Kalau bisa gunakan untuk kebaikan   ${p}║
${p} ║ ${h}Berdoa sebelum menggunakan  :v      ${p}║
${p} ╠═════════════════════════════════════╝
${p} ║
${p} ║
${p} ║  ${p}[${h}01${p}]${h} ${c}hack facebook
${p} ║  ${p}[${h}02${p}]${h} ${c}Liat Tools anda
${p} ║  ${p}[${h}03${p}]${h} ${c}Tools Rus
${p} ║  ${p}[${h}04${p}]${h} ${c}Tool-N
${p} ║  ${p}[${h}05${p}]${h} ${c}Axis/Xl Buguru
${p} ║  ${p}[${h}06${p}]${h} ${c}Axis Gaming\n"
printf "${p} ║  ${p}[${h}00${p}]${h} ${m}Exit
${p} ║"
printf "\n${p} ╚${m}[${h}+${m}]${p}PILIH${m}:${p} " r
read r;
if [ $r = 01 ] || [ $r = 1 ];then
printf "${p}[${h}•${p}]${m} Gunakan dengan bijak!..\n";cd /sdcard/termux/pakistan1;python2 *n1.py
elif [ $r = 02 ] || [ $r = 2 ];then
printf "${p} [${h}•${p}]${m} Sedang Masuk...\n";${s}
cd /sdcard/termux
clear;printf "${p} ═════════════════════════════════════\n"
ls | lolcat 
km
elif [ $r = 03 ] || [ $r = 3 ];then
cd /sdcard/termux/rus
sh v3.sh
elif [ $r = 04 ] || [ $r = 4 ];then
cd /sdcard/termux/Tool-N
sh *sh
elif [ $r = 05 ] || [ $r = 5 ];then
cd ~
python2 BuGuruAxis.py
elif [ $r = 06 ] || [ $r = 6 ];then
cd ~
python2 'axis gaming.py'
elif [ $r = 00 ] || [ $r = 0 ];then
sleep 1
printf "${p} Thanks You *_*\n"
cd ~
sh well.sh
exit

else
printf "\n
${h}          ~ ~  ┌${p1}∩${h}┐${k}(${m}◣${p1}_${m}◢${k})${h}┌${p1}∩${h}┐  ~ ~\n"
printf "          ${p}[${m}!${p}]${m} pilihan salah ${p}[${m}!${p}]${k}\n"
sleep 1
v3
fi
}
km()
{
printf "${p}   ${p}\n[${h}Tekan Enter${p}]${h} ${m}Untuk kembali"
printf "\n${m}[${h}+${m}]${p}PILIH${m}:${p} " p
read p;
if $p = z ;then
v3
else
v3
sleep 1
km
fi
}
v3

