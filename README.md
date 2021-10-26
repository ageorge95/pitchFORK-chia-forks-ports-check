# pitchFORK-chia-forks-ports-check
Tool used to check multiple chia and chia forks cfg files for port conflicts.

Sponsored by HDDcoin, an eco-friendly decentralization blockchain based on the Proof of Space and Time (PoST) consensus - https://hddcoin.org/ - Check them out 🙂

![alt text](https://raw.githubusercontent.com/ageorge95/pitchFORK-chia-forks-ports-check/main/ReadMe_res/hdd_coin_spinning_logo.png?raw=true)

### BLOCKCHAIN RESOURCES:
- Website: https://hddcoin.org/
- Explorer: https://alltheblocks.net/hddcoin
- Calculator: https://hddcoinforkscalculator.com/hddcoin
- HDDcoin DB: https://hddcoin.org/downloads/blockchain_v1_mainnet.sqlite

### COMMUNITIES AND SOCIAL CHANNELS:
- Discord: https://discord.gg/AZdGSFnqAR
- Twitter: https://twitter.com/hddcoin
- YouTube: https://www.youtube.com/channel/UChJY3YEOTDBvFJ0vLFEc1Sw
- Facebook: https://www.facebook.com/HDDcoinNetwork
- Telegram: https://t.me/HDDcoin_Network
- Reddit: https://www.reddit.com/r/HDDcoinNetwork

## Other Contributors

![alt text](https://c.tenor.com/FDwYMy302gMAAAAM/tumbleweed-silence.gif?raw=true)

# High level overview
The tool will parse the configured yaml config files and then scan the data for possible port conflicts.

# Feedback/ Contribution
- Please post any issues you encountered or any feature requests in the issues tab.
- Also, feel free to contribute to the tool's development with a PR.

# Output example

Here is an output example from print_raw_parsed_data()

![alt text](https://raw.githubusercontent.com/ageorge95/pitchFORK-chia-forks-ports-check/main/ReadMe_res/print_raw_data_snapshot.JPG?raw=true)

Here is an output example from print_port_conflicts()

![alt text](https://raw.githubusercontent.com/ageorge95/pitchFORK-chia-forks-ports-check/main/ReadMe_res/print_port_conflicts_snapshot.JPG?raw=true)

# How to use
The tool was tested just in Windows, but should work on every OS where python is supported.

If you want fast support (faster than with github issues that is), join our Discord server: https://discord.gg/ycZtMbWPax

## WINDOWS usage - instructions
### NOTE: No other prerequisites are needed. It works out of the box. ###
1. Add your forks config.yaml file-paths in "input.json"   
   - By default, "input.json" will come with no paths in it, it is up to the end-user to add new paths.    
    
        ![alt text](https://raw.githubusercontent.com/ageorge95/pitchFORK-chia-forks-ports-check/main/ReadMe_res/input_json_default.JPG?raw=true)
   
    - When a new path needs to be added there, it is simply done by adding the path within "", while respecting the json writing paradigm (\\\\ instead of \\)
    
        ![alt text](https://raw.githubusercontent.com/ageorge95/pitchFORK-chia-forks-ports-check/main/ReadMe_res/edited_json.jpg?raw=true)
    
    - For editing the json I recommend using PyCharm, it will automatically format the pasted paths to the json required format

    **1.1. IMPORTANT: in the new Releases, if input.json is missing from cwd (current working directory, same folder with the scripts), it will be created containing a preselected list of cfg paths**
    
    **1.2. If you messed something up in the json, just delete it, and the tool will recreate it for you.**
2. Execute the compiled .exe
3. See the scanned data and possible conflicts on your screen and in "runtime_log.log"

## UBUNTU usage - instructions
### NOTE: Python 3.x is required ###
- Clone the repository
  
   ```
   git clone https://github.com/ageorge95/pitchFORK-chia-forks-ports-check  
   cd pitchFORK-chia-forks-ports-check

- Install the required libraries (NOTE: the libs from requirements.txt may be named different for Ubuntu)
  
   ```
   sudo apt-get install python3-yaml  
   pip install tabulate

- Add paths th the config.yaml files using `nano input.json`

   - Note: use the following format     
   ```
   "/home/user/.forkname/mainnet/config/config.yaml",
   "/home/user/.forkname/mainnet/config/config.yaml",
   "/home/user/.forkname/mainnet/config/config.yaml",
   "/home/user/.forkname/mainnet/config/config.yaml" 

- Run the program: `python3 RUN_ME.py`

- Enjoy 🙂

## SUB-MODULE usage - instructions
### NOTE: Python 3.x is required ###
1. Prepare a list containing the config.yaml file-paths.
2. Add pitchfork as a sub-module in your project, or simply copy all files to a new folder in your project
3. Add the path of the folder from #2 into the system's path (you can use sys.path.append(<folder_name>))
4. Directly import the pitchfork() class from _pitchfork.py, from #2
5. Initialize pitchfork() with the list created at #1
6. Execute as needed "print_raw_parsed_data()" OR "print_port_conflicts()"
7. See the scanned data and possible conflicts on your screen and in "runtime_log.log"

# Support
Found this project useful? Send your ❤ in any form you can 🙂. Please contact me if you donated and want to be added to the contributors list !

- apple APPLE---apple1tdscevmlwa03rt464mr03tf6qs6y2xm3ay4z9lzn9pshad6jkp2s4crqd9
- beet XBT---xbt1kqflshzfhmushajg5hmsrus8rnf2qvh2cstl8wq7tlq2nrdk20msgc4c2g
- goldcoin OZT---ozt1u8klct3kcluvmu9hha8w6vte70d2z37zy7zydz55gygper0658rqkjqwts
- salvia XSLV---xslv19j3zexpgels2k8fkp30phxpxxz6syfzq52t2tuy8ac50nfmnennse9vjcw
- chia XCH---xch1glz7ufrfw9xfp5rnlxxh9mt9vk9yc8yjseet5c6u0mmykq8cpseqna6494
- chia-rose XCR---xcr1pdf0xetkr0k4pppqwv0hslvldr2qlrem09c00ks9y097zufn8drq5hlprx
- cryptodoge XCD---xcd1ds6jljkla5gwfjgty8w4q442uznmw9erwmwnvfspulqke3ya9nxqy9fe8t
- flax XFX---xfx13uwa4zqp0ah5740mknk0z8g3ejdl06sqq8ldvvk90tw058yy447saqjg3u
- fork XFK---xfk1cxkals86jtug06l5wc2m8nyz3ghxx5alqhj6tl3wjqhc7nagar9sus06un
- cannabis CANS---cans16ur4nqvvtdr8yduum5pljr3a73q33uuage6ktnsdr579xeerkc5q604j5v
- socks SOCK---sock1cwu9697vldmkk9mn2rs0ww45dx3aspvjqyygjaw4ucv6unaf8txqsajcvx
- wheat WHEAT---wheat1z4cz3434w48qumwt2f2dqtmgq4lfyv5aswmda7yfmamhml2afrzsa80mr2
- melati XMX---xmx1am6cjj5hrvwhjt8nvuytf2llnjhklpuzcjr4ywg7fe0n7a7n3tns3dj3jf
- taco XTX---xtx1crayqhdtx2rs5680q65c0c2ndaltje6vem0u0nnxtks4ucy058uqc0ak8m
- greendoge GDOG---gdog1ry524dunyuxkrjmzrdrgf5y6hzcdl0fghmncfcxxl83jknn82kmstzjjxk
- tad TAD---tad19s5nxa04znxsl7j6hud8p0uqtmnwd770d5a3nz40dtgwnuufjz0sgfcpnx
- covid COV---cov1ghxfysxsjknf7atnw7d4zqr9sfe9k4y9xc3lpwk5vv249wenlphssulqgp
- avocado AVO---avo1x9z98u6jkynkwutwd49cd58enqh3qfwlc3l7mamx2r6hgxdgqphs88t3yn
- spare SPARE---spare12e68ghay27pcdyuqcaz5qvtwst5mxzht33nxsxmygcd8nnxzhj6qjzytex
- sector XSC---xsc1lxkp9k64r77eh2rkhf6gxlukchnq26nvy6v5l9d6vyfs8jxqgvrs5vsrus
- cactus CAC---cac189er7g8gfsr6yl40t6gq8qygcrsjxkzhp50sk2xa6wh0f2nxzrhsm6rkfe
- flora XFL---xfl149k04h5p9crzsl0xz50efzka9clt56xtg5h33l35m8ld9h2knhqqvs7u76
- kale XKA---xka1m7hskvcd8xqx0a2e5nxc3ldn8gcz83pwvlkgd5x8vflaaq3uetmqj0ztk5
- maize XMZ---xmz1ycj7x6tsajgyannvr92udj23dsj6l4syqx38pmpzf6e7kkeeuvysscdvyw
- hddcoin HDD---hdd1h0lgsxraly8yv7p774rel0l7ajflta6fs4u525c69m3wcahm5y4sx0r0w3
- dogechia XDG---xdg17g6zx3u2a2zslwxrm0spv2297ygnuzhyme89x8kd5mrjz7mns39q6ge64c
- nchain ext9 NCH---nch1ae8hujcantv7naes30etvvcssm6uak9xzd5edwhtyq05adt60hkqlgyfmz
- chives XCC---xcc1amn5txlltvlcnlt6auw24ys6xku7t3npqt2szllassymswnehepszhnjar
- lucky SIX---six1r09eundsl9ntdw5vgq9xk9qedcvxdg7tg3urndcewppc3cn55p2syhu2d4
- BTCGreen xBTC---xbtc1njnsnayxuj4nn0fnzf2nsjnladh79spljx5vvs8v6vqhk9kp6rksgvyszh
- Olive XOL---xol15l6n5lj8splqasw7cr83c6cpdth93gu29vkf0dx0thkpnd2g36cqnearjs
- Beer XBR---xbr1gradjuw6sp78936ecumvjh4gx9kdu7g6gjdh4xdx9er9yk4zv9uqfxfxwm
- Pipscoin PIPS---pips13qcawq6y5dkxqtwnup04m2zmee9lpzsec0zyczt0pd0ra6cuut3qgvhj0k
- Scam SCM---scm1m3sh0pxvjcen2hyzmjgayac0x55ljhlwrptqu90thp6mtpfngx6qgkjwht
- peas PEA---pea1u2pn800fn36cg0lhwrcnpf82a2vsdjuhahdekawffew3u7u3c0xs25yqts
- mint XKM---xkm1k0nkq575wm3nmtkkxwrfmxg7qpt0hxe5m2fvw0dgvw3q0ynmzn3qqu5ntf
- Kiwi XKW---xkw1g9g80rq7exm9mqmzhwrug2qpkgh30dlgpcxkq7ca4x3d5deapm0swmgquy
- xcha XCA---xca1zeh3hlyuqau9a6h3xl3nq4efadam3xg5w672v3gvq7gwdyvaq6vs39rksp
- stor STOR---stor1vahvcz80arp2jl6v4np8grjxncrypzfelmm4uk0gvds5rpuf523qn9w482
- mogua MGA---mga1a9zhv34v75w8eazly5uuycx0tcskwmeyv8uu0kwc749k9wj866lq0val8m
- tranzact  TRZ---trz1mct7p22g2m9gn9m0xtuac4mnrwjkev0pqsxgx7tr6cjk2thnxmkq8q45ep
- Staicoin STAI---stai1m0axlhek947j5mz2wpvy0m9sky49h3jfqwqesy8rmzxfv9j9k5kq9zl6ft
- chaingreen CGN---cgn1llw5jp9ytz80pjhs96anxrcu7537mr45dg764xj2y3u8swmdf03ql63v0g
- lotus LCH---lch1yxmdv2jykwsvmwemka3uc2g3zg7dqfaevd8n2z2jht9nstsammtsyla2ex
- melon MELON---melon1uhrg7a43r0hv5n7k2tq9tsgq5adwc4fvjy7xfdjwqwz58vq2f24szftdfc
- kujenga XKJ---xkj14yyasecl9cygeu25ptx5562ulqj47pzkwsxrcdt20kdwhqkm0rjqvfedah
- aedge AEC---aec16r8mda3kxj58y0zsx8yv4vz3prtdzqadm93w56077thhhcqapdsqcgz67n
- Venidium XVM---xvm1h35hgaqxyvrgjmmr2qgr48ft0cxltyhnge6zkwkfsl9x93d4uq2qq9la0k
- Silicoin SIT---sit1lms7kfdzgetw0tnk04hqh0jwy2g3geju5xypkw53fgafw8aumqzqchs05n