
p="\033[39;1m";a="\033[30;1m";m="\033[31;1m";h="\033[32;1m";k="\033[33;1m";b="\033[34;1m";z="";c="\033[35;1m";pu="\033[36;1m";n="\033[0m";
x="mjuli"
ab="run"
1=sleep 1
2=sleep 2
3=sleep 3
clear
lgn()
{
printf "          	Massukan Username pengguna\n${b}Username${m}: ${p}" rus;
read rus
if [ $rus = $x ];then
clear
printf "${h}		Massukan Username pengguna\n${b}Username${m}: ${p}mjuli "
sleep 1
printf " ${h} ✓   Acces Granted"
sleep 3
clear
printf "Loading ..."
python2 loading.py
clear
printf "${h}         	 Selamat datang di Termux Milik M.Juli_2004 \n\n"
sh pil.sh
cd /sdcard/termux
sleep 2
elif [ $rus = $ab ];then
cd ~
sh well.sh
else
printf "\n               ${k} ┌${p2}∩${k}┐(${m}◣${p2}_${m}◢${k})┌${p2}∩${k}┐\n"
printf "                ${m}WRONG INPUT !!!!\n"
sleep 1
clear
lgn
fi
}
lgn
