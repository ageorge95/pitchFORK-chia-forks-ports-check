# pitchFORK-chia-forks-ports-check
Tool used to check multiple chia and chia forks cfg files for port conflicts.

Sponsored by https://hddcoin.org/ - Check them out 🙂

![alt text](https://hddcoin.org/wp-content/uploads/2021/09/hdd_coin_logo_website_75.png?raw=true)

- Website: https://hddcoin.org/
- GitHub: https://github.com/HDDcoin-Network/hddcoin-blockchain
- Discord: https://discord.gg/AZdGSFnqAR
- Twitter: https://twitter.com/hddcoin
- Coin: HDD
- Explorer: https://alltheblocks.net/hddcoin
- Calculator: https://chiaforkscalculator.com/hddcoin
- HDD DB: https://hddcoin.org/downloads/blockchain_v1_mainnet.sqlite
- Launched: July 2021
- Unique Genesis: YES
- Pre-Farm: 3,500,000 HDD
- Supply:
- Block Reward: 2 HDD
- Blocks Per Day: 4,608, halved every 3 years.
- GUI: YES, https://github.com/HDDcoin-Network/hddcoin-blockchain/releases

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

## Usage scenario 1
DIRECT USAGE - Useful for a quick overview.
1. Add your fork config.yaml filepaths in "input.json"
2. Execute RUN_ME.py
3. See the scanned data and possible conflicts on your screen and in "runtime_log.log"

## Usage scenario 1
INTERFACE WITH OTHER PYTHON SCRIPTS - usefull as a sub-module in your python scripts.
1. Prepare a list containing the config filepaths.
2. Directly import the pitchfork() class from _pitchfork.py
3. Call the "parse_all_cfgs()" methods with the list created at #1
4. Execute as needed "print_raw_parsed_data()" OR "print_port_conflicts()"
5. See the scanned data and possible conflicts on your screen and in "runtime_log.log"

# Support
Found this project useful? Send your love in any form you can 🙂. Please contact me if you donated and want to be added to the contributors list !

- apple APPLE --- apple1tdscevmlwa03rt464mr03tf6qs6y2xm3ay4z9lzn9pshad6jkp2s4crqd9
- beet XBT --- xbt1kqflshzfhmushajg5hmsrus8rnf2qvh2cstl8wq7tlq2nrdk20msgc4c2g
- goldcoin OZT --- ozt1u8klct3kcluvmu9hha8w6vte70d2z37zy7zydz55gygper0658rqkjqwts
- salvia XSLV --- xslv19j3zexpgels2k8fkp30phxpxxz6syfzq52t2tuy8ac50nfmnennse9vjcw
- chia XCH --- xch1glz7ufrfw9xfp5rnlxxh9mt9vk9yc8yjseet5c6u0mmykq8cpseqna6494
- chia-rose XCR --- xcr1pdf0xetkr0k4pppqwv0hslvldr2qlrem09c00ks9y097zufn8drq5hlprx
- cryptodoge XCD --- xcd1ds6jljkla5gwfjgty8w4q442uznmw9erwmwnvfspulqke3ya9nxqy9fe8t
- flax XFX --- xfx13uwa4zqp0ah5740mknk0z8g3ejdl06sqq8ldvvk90tw058yy447saqjg3u
- fork XFK --- xfk1cxkals86jtug06l5wc2m8nyz3ghxx5alqhj6tl3wjqhc7nagar9sus06un
- chaingreen CGN --- cgn1llw5jp9ytz80pjhs96anxrcu7537mr45dg764xj2y3u8swmdf03ql63v0g
- cannabis CANS --- cans16ur4nqvvtdr8yduum5pljr3a73q33uuage6ktnsdr579xeerkc5q604j5v
- socks SOCK --- sock1cwu9697vldmkk9mn2rs0ww45dx3aspvjqyygjaw4ucv6unaf8txqsajcvx
- equality XEQ --- xeq1scldqgmj7u6gpjevn4hyux7wdnq8len3p23se25p4lxl7c8h2ztqfk0qpg
- wheat WHEAT --- wheat1z4cz3434w48qumwt2f2dqtmgq4lfyv5aswmda7yfmamhml2afrzsa80mr2
- melati XMX --- xmx1am6cjj5hrvwhjt8nvuytf2llnjhklpuzcjr4ywg7fe0n7a7n3tns3dj3jf
- taco XTX --- xtx1crayqhdtx2rs5680q65c0c2ndaltje6vem0u0nnxtks4ucy058uqc0ak8m
- goji XGJ --- xgj1x0xyfmkz0xylyaaq6360un9hydjc543lrtuwu9pk5d008acq939qrlgdut
- greendoge GDOG --- gdog1ry524dunyuxkrjmzrdrgf5y6hzcdl0fghmncfcxxl83jknn82kmstzjjxk
- tad TAD --- tad19s5nxa04znxsl7j6hud8p0uqtmnwd770d5a3nz40dtgwnuufjz0sgfcpnx
- covid COV --- cov1ghxfysxsjknf7atnw7d4zqr9sfe9k4y9xc3lpwk5vv249wenlphssulqgp
- avocado AVO --- avo1x9z98u6jkynkwutwd49cd58enqh3qfwlc3l7mamx2r6hgxdgqphs88t3yn
- spare SPARE --- spare12e68ghay27pcdyuqcaz5qvtwst5mxzht33nxsxmygcd8nnxzhj6qjzytex
- seno XSE --- xse1jx8mvumy9243t8qcu0e476r0azvckyaeyhnmu6jswxcr57q09zyqla5w2a
- sector XSC --- xsc1lxkp9k64r77eh2rkhf6gxlukchnq26nvy6v5l9d6vyfs8jxqgvrs5vsrus
- cactus CAC --- cac189er7g8gfsr6yl40t6gq8qygcrsjxkzhp50sk2xa6wh0f2nxzrhsm6rkfe
- flora XFL --- xfl149k04h5p9crzsl0xz50efzka9clt56xtg5h33l35m8ld9h2knhqqvs7u76
- kale XKA --- xka1m7hskvcd8xqx0a2e5nxc3ldn8gcz83pwvlkgd5x8vflaaq3uetmqj0ztk5
- maize XMZ --- xmz1ycj7x6tsajgyannvr92udj23dsj6l4syqx38pmpzf6e7kkeeuvysscdvyw
- hddcoin HDD --- hdd1h0lgsxraly8yv7p774rel0l7ajflta6fs4u525c69m3wcahm5y4sx0r0w3
- dogechia XDG --- xdg17g6zx3u2a2zslwxrm0spv2297ygnuzhyme89x8kd5mrjz7mns39q6ge64c
- nchain ext9 NCH --- nch1ae8hujcantv7naes30etvvcssm6uak9xzd5edwhtyq05adt60hkqlgyfmz
- chives XCC --- xcc1amn5txlltvlcnlt6auw24ys6xku7t3npqt2szllassymswnehepszhnjar
- lucky SIX --- six1r09eundsl9ntdw5vgq9xk9qedcvxdg7tg3urndcewppc3cn55p2syhu2d4
- BTCGreen xBTC --- xbtc1njnsnayxuj4nn0fnzf2nsjnladh79spljx5vvs8v6vqhk9kp6rksgvyszh
- Olive XOL --- xol15l6n5lj8splqasw7cr83c6cpdth93gu29vkf0dx0thkpnd2g36cqnearjs
- Beer XBR --- xbr1gradjuw6sp78936ecumvjh4gx9kdu7g6gjdh4xdx9er9yk4zv9uqfxfxwm
- Pipscoin PIPS --- pips13qcawq6y5dkxqtwnup04m2zmee9lpzsec0zyczt0pd0ra6cuut3qgvhj0k
- Scam SCM --- scm1m3sh0pxvjcen2hyzmjgayac0x55ljhlwrptqu90thp6mtpfngx6qgkjwht
- peas PEA --- pea1u2pn800fn36cg0lhwrcnpf82a2vsdjuhahdekawffew3u7u3c0xs25yqts
- mint XKM --- xkm1k0nkq575wm3nmtkkxwrfmxg7qpt0hxe5m2fvw0dgvw3q0ynmzn3qqu5ntf
- Kiwi XKW --- xkw1g9g80rq7exm9mqmzhwrug2qpkgh30dlgpcxkq7ca4x3d5deapm0swmgquy
- Silicoin tSIT --- tsit1jjesydjg0xkfut22x2mawlvrs74qe40kkfhju2p2wnpev5r4ugfs35ydxf
- xcha XCA --- xca1zeh3hlyuqau9a6h3xl3nq4efadam3xg5w672v3gvq7gwdyvaq6vs39rksp
- stor STOR --- stor1vahvcz80arp2jl6v4np8grjxncrypzfelmm4uk0gvds5rpuf523qn9w482
- mogua MGA --- mga1a9zhv34v75w8eazly5uuycx0tcskwmeyv8uu0kwc749k9wj866lq0val8m
- tranzact TRZ --- trz1mct7p22g2m9gn9m0xtuac4mnrwjkev0pqsxgx7tr6cjk2thnxmkq8q45ep