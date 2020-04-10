"""
#####################################################################
Intro:
The Global Detective Agency (GDA) discovered a secret website 
yesterday that has a single text field and a button. The website 
reveals classified information to anyone who types in the right key:

There are 75 keys, but only found "mars" and "alien". Enter those and
the website will give you secret news on a new line. Listed in
sorted order.

Task: Find all the 75 keys and print each
correspoding piece of secret news on a new lin

Input:

Output:

"""


""" Use json path in source to fetch?
mars : A top-secret space-ship landed on mars yesterday.
alien : Scientists discovered aliens in Jupiter today.

"""
import urllib.request
import urllib.parse
import re
import linkGrabber
import string
# #
# data = {}
# urls = ["https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/secret_json/"]
# ext = {"v060r": "", "fxcne": "", "4ijzo": "", "7o40h": "", "vjkf0": "", "96xmi": "", "7hmxu": "", "lefjd": "", "alien": "", "vejhb": "", "mz9a6": "", "tgihv": "", "utohw": "", "rp3g1": "", "fnsdm": "", "gstfd": "", "o020f": "", "i8z4b": "", "e9uak": "", "k9qxx": "", "9jh01": "", "89rcx": "", "yrxnh": "", "2y1b3": "", "xw5np": "", "276xh": "", "x2s57": "", "2b6f7": "", "t76dy": "", "il0d5": "", "ff8vi": "", "m7c30": "", "a5b38": "", "s94o9": "", "w17qs": "", "44bd3": "", "wnpxm": "", "mars": "", "epmqk": "", "ki0ag": "", "rs500": "", "etdbc": "", "nu5q2": "", "223j4": "", "ue9sp": "", "8bue1": "", "me6mc": "", "n0sh4": "", "3hqk3": "", "w8xh4": "", "i5cxs": "", "0rmqe": "", "kpisp": "", "jck0j": "", "k3dip": "", "oywsu": "", "eej3o": "", "wixg4": "", "62al1": "", "tjgzq": "", "jhpfy": "", "o4zx6": "", "wup33": "", "m88dt": "", "tvygb": "", "24hcw": "", "pjfb8": "", "3dfng": "", "wzeai": "", "0z6uz": "", "zaden": "", "pcxjo": "", "z732w": "", "jdjws": "", "byzms": ""}
#
# for k in ext.keys():
#     ext[k] = urls[0] + k + ".json"
#     # print(ext[k])
#
# for url in ext.values():
#     with urllib.request.urlopen(url) as response:
#         html = response.read()
#     print(html)


d = [{"news_title": "qqqkqqy uwtvpjg swodvmm bntkjra nyrkrpf fxgbvnj nteqsvh pgoeuwi", "key": "v060r"}
,{"news_title": "vxabvbh dcaqtrv rkqzqgb ypjponb jkfwlrs tstgzdx", "key": "fxcne"}
,{"news_title": "fopynpd khsgfjm ipewsnb irqvxim", "key": "4ijzo"}
,{"news_title": "agmyjcs rdrkkyv zskjdbn epfnxmy hdslrpl jfzflxv zqhwbyl rxnvvnx gesvkal fbepjuf", "key": "7o40h"}
,{"news_title": "rrorrcu nvcbqhz hliofyh xzivxaz jiueaza", "key": "vjkf0"}
,{"news_title": "yyepnlu yssrqng udqkoqm zgayihk pzsinln kekkfvj dovuqti dgjhmdd gfunflw", "key": "96xmi"}
,{"news_title": "prijkno wklvzgs gtbnosx uomaoot epbsvlr rhctjel vyozema", "key": "7hmxu"}
,{"news_title": "sorffow kaahpcf rzipnai dgurbcs cihbadk yqgrhni yjuqvpw", "key": "lefjd"}
,{"news_title": "Scientists discovered aliens in Jupiter today.", "key": "alien"}
,{"news_title": "izsfyaz agoatcv anfhmjk qferhyl maacqry lsibksu yvoonmr owlmvrn oupgipb lxglsys", "key": "vejhb"}
,{"news_title": "vescizr ulmmusf looyvdj cabetru hezvyak qtxnkau", "key": "mz9a6"}
,{"news_title": "gjhaauz bblhgwf fxqrraz afmvyad adxcofa hgownnh emkxfab ifkwspv wbrdkkh bfsyxao", "key": "tgihv"}
,{"news_title": "ubtjrpd obgjhrz jvfsjnc", "key": "utohw"}
,{"news_title": "qvlwjjx zufyjwi fgrzncr", "key": "rp3g1"}
,{"news_title": "bvqihji tnndxii bzmxyzv yxudnoz ustjyqk mznedro xeksbco", "key": "fnsdm"}
,{"news_title": "bvxauvb pmevovy zrwbimn jvpwlyj zojqcrp ubkpbtx", "key": "gstfd"}
,{"news_title": "ghgadru cymubcv carbkvc vxzpveo wwevknu riwyvba occwbhh yyuldzf", "key": "o020f"}
,{"news_title": "qiltueq ezlxspg nddsjtg sshckmc ebpxfas vzpivds ckmjegv mpfsipx zbuwijp xkwtdxa", "key": "i8z4b"}
,{"news_title": "birdspg vbftpfk webmfrg epyozzt ojcneol oooyodw tjlokrz bxzwmrm jefmhfp", "key": "e9uak"}
,{"news_title": "khiiwxh ioppgag bobbqhu mwenucy euzvicn xhxdxai xuxvtre lesrgbz voowlki gaqkobj", "key": "k9qxx"}
,{"news_title": "mkwupbw lehradh xtzooon ovykqih npozeqz tojkyxr xywjmuj", "key": "9jh01"}
,{"news_title": "fuhgcqt shhbegf bkanajc esburqn sfkaakq zvbxkke clowrep vghgzdq", "key": "89rcx"}
,{"news_title": "hpwvnzm vktzheq njaklkw", "key": "yrxnh"}
,{"news_title": "rqltwza xuptjkb yunpveo spzgruk ykdekzx xrnqpyk", "key": "2y1b3"}
,{"news_title": "vwxpcbu xnxytjl jkmadeo wsdlqdc", "key": "xw5np"}
,{"news_title": "oahugqh diihixo mghuidk ryvmexb pzinhkc", "key": "276xh"}
,{"news_title": "sclrhjt fxdfpfv jdrlqcb hnffvgj wzudtcu", "key": "x2s57"}
,{"news_title": "xycjpir wfiwict hpbovlj unmerva iqdwdgl dxnkpto qrlhdrj yhulekq rjfeprx", "key": "2b6f7"}
,{"news_title": "klypenn fjwzubx lvedxhb", "key": "t76dy"}
,{"news_title": "pbbraqi hywhkhd yqslfqg xyzfhwm osfmcaz sqfhxzq", "key": "il0d5"}
,{"news_title": "flwccbd jihamlt hpiteml lnnivyo qsipmmk nfgfpgu xtiyijp rkuwhfk srekxyp", "key": "ff8vi"}
,{"news_title": "lvnnnez thjswoh joxsfar gwezuga", "key": "m7c30"}
,{"news_title": "ewzsnjj frlfcrh miwxafi zuifrvy iwrmzgs cexftpv jihwpyx", "key": "a5b38"}
,{"news_title": "vqkxmyo xmlpidp whwuukz uocoaxi joqpmqw lnvaeif xdcinvz wpabqvg zooqbey", "key": "s94o9"}
,{"news_title": "rhptvde rssmjyg hacqrft ejqulvm rvooyaa ainqraw gzivsan kzgkean qevfyrz lvpsknh", "key": "w17qs"}
,{"news_title": "jzbnldk swancuc ajtiduu whlgoii uypcqlz svsnxvh", "key": "44bd3"}
,{"news_title": "atthaip uwfcdzq drypgzs etnojhk nlwbfyp qqgkfdz twashmr ajownip phohaic", "key": "wnpxm"}
,{"news_title": "A top-secret space-ship landed on mars yesterday.", "key": "mars"}
,{"news_title": "zafwmuc zaugsut yfwqefc xijduof unusljx ecwrypz", "key": "epmqk"}
,{"news_title": "aqpvfho hpgruvz omwtojh cudtozt zdnoinj nallhku", "key": "ki0ag"}
,{"news_title": "gjfcnnd xzbabtw baniaaf fhoggfx golikae qtfexcu wdvdbhi plurdft dyvfhgk gagfjlw", "key": "rs500"}
,{"news_title": "uvipujo fcgxoyl huvarcc xbgzkde gtcxjzx hgmcqba zhplibx zzcfqzo rrgohgc", "key": "etdbc"}
,{"news_title": "kykpbma sabcdnj hzxruvg vgojeux iwjrzub ljhvlsq nbrxeqm", "key": "nu5q2"}
,{"news_title": "caatgcq ibenehs limakke cxnfpva adsesro fzunfqk oiqbhzw hwiytkg", "key": "223j4"}
,{"news_title": "swnesej gnqoegf nzrwcao", "key": "ue9sp"}
,{"news_title": "mvgaukc rxcpjbb bhinqww eqwgpzq sizviha mwudgeg feoxwqi xfbfusi fqnulcb gnsoayl", "key": "8bue1"}
,{"news_title": "nxsfxas bveuvuc kcsznqr djjtkjo fbgarlq obvvalu", "key": "me6mc"}
,{"news_title": "afeieqp kgqjtws yhwkwqh hwmdpdb gufwbia rpuvxlj pmflkxc", "key": "n0sh4"}
,{"news_title": "ptgbviv yqcwqgf ndxsvjy dsgadft jmpgqrx nwztkhc vdolbfv", "key": "3hqk3"}
,{"news_title": "wdvedgn rnbyvja kzyefzi", "key": "w8xh4"}
,{"news_title": "zdgziex qiolloe qypuhea zdjrtql vlvbsck lelwafz lkxuepe uoubyfw lxcbmym neolxtm", "key": "i5cxs"}
,{"news_title": "kaegwph zgntrlu msmzscd zfagmyk svcpzon", "key": "0rmqe"}
,{"news_title": "adusydy xjyzvow eddsyfd xwdahha dvblssi", "key": "kpisp"}
,{"news_title": "hmthwzv biywdlj taitxbp rwlzfcd", "key": "jck0j"}
,{"news_title": "vmbfsih fatigcn tyyammo lyplzna", "key": "k3dip"}
,{"news_title": "kxqobne floghnm kcjroov srairex dwfvwix ewjldph rupayxq", "key": "oywsu"}
,{"news_title": "pgannql rtgmmfk oxxhqbb nwetwis wjstpwx yoegfot", "key": "eej3o"}
,{"news_title": "loxxvrb enzsejz nwwuqri dyahpzf gwikjby", "key": "wixg4"}
,{"news_title": "zxurjat lwdwqxs lncgoej qpxlokt qyddhqq fhpgvcu dsuyxar xulthuk", "key": "62al1"}
,{"news_title": "enrtrkr pmqhbdz xvgvuoh czzwlsx odznuqb magyroc rpqrylp", "key": "tjgzq"}
,{"news_title": "ruehvit odfyxpa ayusgxb rrjvezy iiuipry thjbuvf mihapye tunwlqb dpvmymk", "key": "jhpfy"}
,{"news_title": "pblrnpj vgqldad hmabuzl mpcoryq okxnmtl bpwjccx crcnxgh pookbph qlgzizm", "key": "o4zx6"}
,{"news_title": "qwkdoaj mfpvmoe amgqcln", "key": "wup33"}
,{"news_title": "rdghmuw urckrhn xdwckxf nkxzhmx oftimaz ryzgolt", "key": "m88dt"}
,{"news_title": "bohuedw cjrogdp gwgyaph", "key": "tvygb"}
,{"news_title": "shlvckd ntztdlo qszyfez ezdpddi usidjeg mmxcnod", "key": "24hcw"}
,{"news_title": "bpzozds vcfygqx suhwdkm sabjexl plwyxcp uxomeaa hskohzx gjckgsi rasqhuw xslptiw", "key": "pjfb8"}
,{"news_title": "orubbmt fpcxwyk cvljlss", "key": "3dfng"}
,{"news_title": "lsnaale vtuqfuh ebkyrrj lxzipmf ncukrug", "key": "wzeai"}
,{"news_title": "wbpcfrj rfcjnvw jyoenrt", "key": "0z6uz"}
,{"news_title": "dfinxox olwpmnj lbftdfe jbjprwc qfiovrz aimabjo dbitozp xomkbbr waeiivg hmyhqbl", "key": "zaden"}
,{"news_title": "inpbxjt jdifhrr esqepbr gpysoog mbmzntx", "key": "pcxjo"}
,{"news_title": "gxfduzt qcneokd ousdyyj zekvcka fjvqcut hetyfii zbaemza unxzsgx azkhwmk", "key": "z732w"}
,{"news_title": "bwqewaj wshxpwx lroyusv", "key": "jdjws"}
,{"news_title": "sbzvqgx yduvrsl yzjulei dxydpkd", "key": "byzms"}]

q = []
for el in d:
    q.append(el["news_title"])

# print(q)
# map(str, q)
# sorted(q, key=(string.ascii_uppercase + string.ascii_lowercase).index)
q.sort()
# print(q)
for el in q:
    print(el)
