ó
L}^c           @   s!   d  d l  Z  e  j d  d Ud S(   iÿÿÿÿNs[  c           @   s  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z e j   Z e  j	 e  j
 d k r{ d n d  d   Z d   Z d   Z d d	 d
  Z d d d  Z d e f d     YZ d e j f d     YZ d   Z e d k r	e   n  d S(   iÿÿÿÿNt   ntt   clst   clearc         C   s    t  j j t  j j t   |  S(   N(   t   ost   patht   dirnamet   abspatht   __file__(   t	   file_name(    (    s   <s>t	   real_path   s    c         C   sn   xN t  t |    D]: } |  | j   |  | <|  | j d  r d |  | <q q Wg  |  D] } | rX | ^ qX S(   Nt   #t    (   t   ranget   lent   stript
   startswith(   t   arrayt   it   x(    (    s   <s>t   filter_array   s
    c         C   sd   i d d 6d d 6d d 6d d 6d	 d
 6d d 6} x- | D]% } |  j  d j |  | |  }  q7 W|  S(   Ns   [31;1mt   R1s   [31;2mt   R2s   [32;1mt   G1s   [33;1mt   Y1s   [34;1mt   P1s   [0mt   CCs   [{}](   t   replacet   format(   t   valuet   patternst   code(    (    s   <s>t   colors   s    #R   s   [R2]c      
   C   sR   t  d j d t j j   j d  d |  d | d |   }  t 
 |  GHWd  QXd  S(   Ns9   {color}[{time}][P1]{color}{status}[CC] {color}{value}[CC]t   times   %H:%M:%SR   t   colort   status(   R   R   t   datetimet   nowt   strftimet   lock(   R   R"   R!   (    (    s   <s>t   log"   s     t   Axiss   [R1]c         C   sI   t  d j | | |    }  t " t j j |   t j j   Wd  QXd  S(   Ns   {}{} ({})        [CC](   R   R   R&   t   syst   stdoutt   writet   flush(   R   R"   R!   (    (    s   <s>t   log_replace+   s    t   injectc           B   s&   e  Z d    Z d d  Z d   Z RS(   c         C   s5   t  t |   j   t |  |  _ t |  |  _ d  S(   N(   t   superR.   t   __init__t   strt   inject_hostt   intt   inject_port(   t   selfR2   R4   (    (    s   <s>R0   2   s    s   [R1]c         C   s   t  | d | d  S(   NR!   (   R'   (   R5   R   R!   (    (    s   <s>R'   8   s    c         C   s,  yí t  j  t  j t  j  } | j |  j |  j f  | j d  t t d   j	   } t
 |  } t |  d k r |  j d d d d  S|  j d j |  j |  j   x< t rë | j   \ } } | j d  t | |  j   q° WWn8 t k
 r'} |  j d	 j |  j |  j  d d n Xd  S(
   Ni   s   /frontend-domains.txti    s   frontend-domains.txtR!   s   [R1]sG   ð¥³ð¥³ => : Inject Ready!! .
[CC]Local Host/Port : [CC]127.0.0.1/8080i   s6   ð­Terjadi ERROR, Silahkan Hapus Data & Mulai Ulang!!(   t   sockett   AF_INETt   SOCK_STREAMt   bindR2   R4   t   listent   openR	   t	   readlinesR   R   R'   R   t   Truet   acceptt   recvt   domain_frontingt   startt	   Exception(   R5   t   socket_servert   frontend_domainst   socket_clientt   _t	   exception(    (    s   <s>RA   ;   s     	(   t   __name__t
   __module__R0   R'   RA   (    (    (    s   <s>R.   1   s   	R@   c           B   ss   e  Z d    Z d d d  Z d   Z d   Z e d j d d d	 d
 d d d d d d d d d d d g   GHRS(   c         C   sV   t  t |   j   | |  _ t j t j t j  |  _ | |  _ d |  _	 t
 |  _ d  S(   Ni   (   R/   R@   R0   RD   R6   R7   R8   t   socket_tunnelRE   t   buffer_sizeR=   t   daemon(   R5   RE   RD   (    (    s   <s>R0   N   s    			R   s   [CC]c         C   s   t  | d | d | d  S(   NR"   R!   (   R'   (   R5   R   R"   R!   (    (    s   <s>R'   W   s    c         C   sè   | | g } d } xÏ t  rã | d 7} t j | g  | d  \ } } } | rP Pn  | rÐ xw | D]l }	 y[ |	 j |  }
 |
 s Pn8 |	 | k r | j |
  n |	 | k r· | j |
  n  d } Wq] Pq] Xq] Wn  | d k r Pq q Wd  S(   Ni    i   i   i<   (   R=   t   selectR?   t   sendall(   R5   RJ   RE   RK   t   socketst   timeoutt	   socket_ioRF   t   errorst   sockt   data(    (    s   <s>t   handlerZ   s,    	
!  
  c         C   sd  y
t  j |  j  j d  |  _ |  j d |  _ t |  j  d k r` |  j d r` |  j d n d |  _ |  j d  |  j	 j
 t |  j  t |  j  f  |  j j d  |  j |  j	 |  j |  j  |  j j   |  j	 j   |  j d j |  j |  j  d	 d
 WnS t k
 r0|  j d d	 d
 n0 t k
 r_|  j d j |  j  d	 d
 n Xd  S(   Nt   :i    i   i   t   433s   :: Connecting.. :: => Gagals   HTTP/1.1 200 OK

s   :: Connecting.. :: => ConnectR!   s   [R1]s   Terjadi Errors   {} not responding(   t   randomt   choiceRD   t   splitt   proxy_host_portt
   proxy_hostR   t
   proxy_portR'   RJ   t   connectR1   R3   RE   RN   RU   RK   t   closeR   t   OSErrort   TimeoutError(   R5   (    (    s   <s>t   runo   s    8()s   
s   [R1]       â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬[CC][R1]â¬â¬[CC][G1]à®Û©ÛÛ©à®[CC][R1]â¬â¬[CC][R1]â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬s¨   [CC][Y1]   Ø§ÙØ³ÙÙÙØ§ÙÙÙ Ø¹ÙÙÙÙÙÙÙÙÙ ÙÙØ±ÙØ­ÙÙÙØ©Ù Ø§ÙÙÙÙ ÙÙØ¨ÙØ±ÙÙÙØ§ØªÙÙÙ[CC][Y1]                         GRETONGERS INDONESIA[CC]s)   [Y1]         Script BuGuru XL/ Axis Cikgus(   [CC][Y1]              Created by Pikachus(   [CC][Y1]               #DirumahLebihBaiks   [CC][R1]       â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬[CC][R1]â¬â¬[CC][G1]à®Û©ÛÛ©à®[CC][R1]â¬â¬[CC][R1]â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬â¬s	   [CC][G1] s,   [CC][R1][[CC][G1] +[CC][R1] ][CC][G1] Alamats4   [CC][R1][[CC][P1] +[CC][R1] ][CC][G1] Host 127.0.0.1s/   [CC][R1][[CC][Y1] +[CC][R1] ][CC][G1] Port 8080s	   [CC][Y1] s!   [CC][Y1]  Whatsapp : 082259285886s   [CC][Y1]  Facebook : Andiis&   [CC][Y1]  From : Palu, Sulawesi Tengah(   RH   RI   R0   R'   RU   Rb   R   t   join(    (    (    s   <s>R@   M   s$   					c          C   sP   d }  d } t  d  } | | k r4 t j d  n  d GHt d d  j   d  S(   Ns    Enter your password !t   ndiis      -Password > ndii : s)     WRONG INPUTâÐâ(â£_â¢)âÐâ!!
s      -Start Psiphon Bosku!!
s	   127.0.0.1t   8080(   t	   raw_inputR)   t   exitR.   RA   (   t   Gt   liket
   user_input(    (    s   <s>t   main   s    t   __main__(   R   R)   RX   R6   RM   t	   threadingR#   t   RLockR&   t   systemt   nameR	   R   R   R'   R-   t   objectR.   t   ThreadR@   Rk   RH   (    (    (    s   <s>t   <module>   s$    "				C		(   t   marshalt   loads(    (    (    s   /sdcard/ApaLoNjink.pyt   <module>   s   