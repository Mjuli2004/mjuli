
blue='\e[1;34m' 
green='\e[1;32m' 
purple='\e[1;35m' 
cyan='\e[1;36m' 
red='\e[1;31m' 
white='\e[1;37m' 
yellow='\e[1;33m' 
NOW=`date "+%d.%m.%Y"`
TIME=`date "+%H:%M"` 
echo -e $green
cd ~
sh lgn.sh
hi()
{
sh .time.sh
echo
cd /sdcard/termux
echo -e $green
cowsay -f eyes.cow 'WELCOME'

echo "______________________________________________________________________"
echo " Hostname : " "@M.Juli_2004"
echo " Username : " $USERNAME "M.juli"
echo " Date : " $NOW 
echo " Time : " $TIME 
echo -e $white
printf " message : Keep Always Your Smile^^ ${red}	▇▇▇▇▇▇▇▇▇▇▇▇ INDONESIA\n"
printf " ${white}selamat datang di termux 	     ▇▇▇▇▇▇▇▇▇▇▇▇ IS MY LIFE\n"
echo ' ______________________________________________________________________' 
echo
echo -e $green '______________NO_SYSTEM_IS_SAFE__________________'
echo -e $red 
echo ' ______________________________________________________________________'
echo -e $yellow '................Your_Tools................'
ls | lolcat
echo -e $yellow '...............Use_for_kind...............'
echo -e $red '______________________________________________________________________'
}
cd /sdcard/termux
PS1=$red'╔═════════════════════════════════╗\n'''$green' \w '$white'		  ''\n╚═════════════════════════════════╝\n :> '$green


# Enables autocompletion of options for bashfuscator
eval "$(/data/data/com.termux/files/usr/bin/register-python-argcomplete bashfuscator)"
