# pitchFORK-chia-forks-ports-check
- The tool:
  - checks for port conflicts in chia & chia forks configuration files
  - offers the user the option to fix the conflicts automatically

- The tool needs:
  - no special requirements, it uses basic search and replace methods

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

# Feedback/ Contribution
- Please post any issues you encountered or any feature requests in the issues tab.
- Do not forget to join the Discord server dedicated for this tool: https://discord.gg/ycZtMbWPax
- Also, feel free to contribute to the tool's development with a PR.

# Output example

Here is an output example from print_raw_parsed_data()

![alt text](https://raw.githubusercontent.com/ageorge95/pitchFORK-chia-forks-ports-check/main/ReadMe_res/print_raw_data_snapshot.JPG?raw=true)

Here is an output example from print_port_conflicts()

![alt text](https://raw.githubusercontent.com/ageorge95/pitchFORK-chia-forks-ports-check/main/ReadMe_res/print_port_conflicts_snapshot.JPG?raw=true)

Here is an output example from attempt_auto_fix()

![alt text](https://raw.githubusercontent.com/ageorge95/pitchFORK-chia-forks-ports-check/main/ReadMe_res/attempt_auto_fix_ex.JPG?raw=true)

# How to use
The tool was designed mainly for Windows, but should work on every OS where python is supported.

## WINDOWS usage - instructions
### NOTE: No other prerequisites are needed. It works out of the box. ###
1. [OPTIONAL] Add your forks config.yaml file-paths in "input.json"   
   - **By default, "input.json" will be auto-generated with a default list of forks, if the file is missing from the execution's root dir.**   
   - When a new path needs to be added there, it is simply done by adding the path within "", while respecting the json writing paradigm (\\\\ instead of \\)
    
        ![alt text](https://raw.githubusercontent.com/ageorge95/pitchFORK-chia-forks-ports-check/main/ReadMe_res/edited_json.jpg?raw=true)
    
    - For editing the json I recommend using PyCharm, it will automatically format the pasted paths to the json required format
    - If you messed something up in the json, just delete it, and the tool will recreate it for you.
2. Execute the compiled .exe
3. See the scanned data and possible conflicts on your screen and in "runtime_log.log"
4. Allow or not the auto-fix attempt to be executed

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
8. Execute attempt_auto_fix() to automatically fix the port conflicts

# Support
Found this project useful? Send your ❤ in any form you can 🙂. Please contact me if you donated and want to be added to the contributors list !

- apple APPLE---apple1tdscevmlwa03rt464mr03tf6qs6y2xm3ay4z9lzn9pshad6jkp2s4crqd9
- goldcoin OZT---ozt1u8klct3kcluvmu9hha8w6vte70d2z37zy7zydz55gygper0658rqkjqwts
- salvia XSLV---xslv19j3zexpgels2k8fkp30phxpxxz6syfzq52t2tuy8ac50nfmnennse9vjcw
- chia XCH---xch1glz7ufrfw9xfp5rnlxxh9mt9vk9yc8yjseet5c6u0mmykq8cpseqna6494
- cryptodoge XCD---xcd1ds6jljkla5gwfjgty8w4q442uznmw9erwmwnvfspulqke3ya9nxqy9fe8t
- flax XFX---xfx13uwa4zqp0ah5740mknk0z8g3ejdl06sqq8ldvvk90tw058yy447saqjg3u
- cannabis CANS---cans16ur4nqvvtdr8yduum5pljr3a73q33uuage6ktnsdr579xeerkc5q604j5v
- wheat WHEAT---wheat1z4cz3434w48qumwt2f2dqtmgq4lfyv5aswmda7yfmamhml2afrzsa80mr2
- melati XMX---xmx1am6cjj5hrvwhjt8nvuytf2llnjhklpuzcjr4ywg7fe0n7a7n3tns3dj3jf
- taco XTX---xtx1crayqhdtx2rs5680q65c0c2ndaltje6vem0u0nnxtks4ucy058uqc0ak8m
- greendoge GDOG---gdog1ry524dunyuxkrjmzrdrgf5y6hzcdl0fghmncfcxxl83jknn82kmstzjjxk
- tad TAD---tad19s5nxa04znxsl7j6hud8p0uqtmnwd770d5a3nz40dtgwnuufjz0sgfcpnx
- avocado AVO---avo1x9z98u6jkynkwutwd49cd58enqh3qfwlc3l7mamx2r6hgxdgqphs88t3yn
- spare SPARE---spare12e68ghay27pcdyuqcaz5qvtwst5mxzht33nxsxmygcd8nnxzhj6qjzytex
- cactus CAC---cac189er7g8gfsr6yl40t6gq8qygcrsjxkzhp50sk2xa6wh0f2nxzrhsm6rkfe
- flora XFL---xfl149k04h5p9crzsl0xz50efzka9clt56xtg5h33l35m8ld9h2knhqqvs7u76
- kale XKA---xka1m7hskvcd8xqx0a2e5nxc3ldn8gcz83pwvlkgd5x8vflaaq3uetmqj0ztk5
- maize XMZ---xmz1ycj7x6tsajgyannvr92udj23dsj6l4syqx38pmpzf6e7kkeeuvysscdvyw
- hddcoin HDD---hdd1qfs8hdtdrmsw9ya04cjex0d6dzkn7lfv7vp9g2dgup3p87ye9gqs6zvam2
- dogechia XDG---xdg17g6zx3u2a2zslwxrm0spv2297ygnuzhyme89x8kd5mrjz7mns39q6ge64c
- nchain ext9 NCH---nch1ae8hujcantv7naes30etvvcssm6uak9xzd5edwhtyq05adt60hkqlgyfmz
- chives XCC---xcc1amn5txlltvlcnlt6auw24ys6xku7t3npqt2szllassymswnehepszhnjar
- BTCGreen xBTC---xbtc1njnsnayxuj4nn0fnzf2nsjnladh79spljx5vvs8v6vqhk9kp6rksgvyszh
- Pipscoin PIPS---pips13qcawq6y5dkxqtwnup04m2zmee9lpzsec0zyczt0pd0ra6cuut3qgvhj0k
- mint XKM---xkm1k0nkq575wm3nmtkkxwrfmxg7qpt0hxe5m2fvw0dgvw3q0ynmzn3qqu5ntf
- stor STOR---stor1vahvcz80arp2jl6v4np8grjxncrypzfelmm4uk0gvds5rpuf523qn9w482
- tranzact  TRZ---trz1mct7p22g2m9gn9m0xtuac4mnrwjkev0pqsxgx7tr6cjk2thnxmkq8q45ep
- Staicoin STAI---stai1m0axlhek947j5mz2wpvy0m9sky49h3jfqwqesy8rmzxfv9j9k5kq9zl6ft
- Venidium XVM---xvm1h35hgaqxyvrgjmmr2qgr48ft0cxltyhnge6zkwkfsl9x93d4uq2qq9la0k
- Skynet XNT---xnt1cq8xdu8svwhruefr5khzpqxturemtqrf6gk7uqjyjrhdl2dyapmsh9desg
- Shibgreen XSHIB---xshib1pkelrz8uml46m6hdw06ttezhaqasexe0527jce4cc03uj4fc8rcsaaatwy
- Silicoin SIT---sit1df3l4xpzc65xyzvdlleww6stwt70kd9a4ra0836hf6ahpcwd7yrqj0s60a
- bpx BPX---bpx10d25g8jechcs2rfstkzpj2rzt68skw4etvqm2j7f8545uzd6kyrqgr2ea8
- Gold GL---gl1df3l4xpzc65xyzvdlleww6stwt70kd9a4ra0836hf6ahpcwd7yrqqwx0ye
- joker---xjk1may9ee07y0yf0a5k3hvhq54wem07ny5k7grzksgm4rnhl3yzwnqss8lsge
- profit---profit1df3l4xpzc65xyzvdlleww6stwt70kd9a4ra0836hf6ahpcwd7yrqfhghvg
- littlelambocoin LLC---llc1wfhhxn4dtr7luedc4lzld2y2q32r66ruvqyppj7vr6g5u75xn92s3pz9gw
- ecostake ECO---eco1df3l4xpzc65xyzvdlleww6stwt70kd9a4ra0836hf6ahpcwd7yrq5l9vpy
- chinilla HCX---hcx16ce9d6pj80nw6j2j9hgax30k6ww43na3ve86pm87tecsdhgc03sq7cvnmt
- petroleum XPT---xpt1df3l4xpzc65xyzvdlleww6stwt70kd9a4ra0836hf6ahpcwd7yrqq2qcs2
- Scam SCM---scm1m3sh0pxvjcen2hyzmjgayac0x55ljhlwrptqu90thp6mtpfngx6qgkjwht
- seno XSE---xse1jx8mvumy9243t8qcu0e476r0azvckyaeyhnmu6jswxcr57q09zyqla5w2a
- lucky SIX---six1r09eundsl9ntdw5vgq9xk9qedcvxdg7tg3urndcewppc3cn55p2syhu2d4
- moon---moc1k49pfczryvea0h3hf6ls2fm6gykhaa9jymfhuy27790f470rt8js770rdv
- lotus LCH---lch1yxmdv2jykwsvmwemka3uc2g3zg7dqfaevd8n2z2jht9nstsammtsyla2ex
- Coffee XCF---xcf1df3l4xpzc65xyzvdlleww6stwt70kd9a4ra0836hf6ahpcwd7yrqcq54t6
- ethgreen XETH---xeth1e24uzser8h78gun2jppnqsgx7vsrktzkgdeuknat63ppcfw7htuq2pu73a
- goji XGJ---xgj1x0xyfmkz0xylyaaq6360un9hydjc543lrtuwu9pk5d008acq939qrlgdut
- greenbtc GBTC---gbtc1df3l4xpzc65xyzvdlleww6stwt70kd9a4ra0836hf6ahpcwd7yrqw0awqh
