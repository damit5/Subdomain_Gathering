## Subdomain_Gathering

一款通过**百度**搜索结果提取子域名的**多线程**Python脚本

通过百度 `site:domain ` ，找到对应的域名后提取出域名，并进行存活性检测

## 需求
- python 3
- requests

## 特点
- 体积小
- 速度快

## 下载
```
git clone https://github.com/damit5/Subdomain_Gathering.git
cd Subdomain_Gathering
pip install -r requirement.txt
```

## 使用

`python subdomain_gathering.py domain`

##### example:

```
python subdomain_gathering.py tsinghua.edu.cn

www.tsinghua.edu.cn
sem.tsinghua.edu.cn
info.tsinghua.edu.cn
pbcsf.tsinghua.edu.cn
mail.tsinghua.edu.cn
lib.tsinghua.edu.cn
news.tsinghua.edu.cn
life.tsinghua.edu.cn
guofang.tsinghua.edu.cn
ioe.tsinghua.edu.cn
is.tsinghua.edu.cn
sklhse.tsinghua.edu.cn
phys.tsinghua.edu.cn
student.tsinghua.edu.cn
hq.tsinghua.edu.cn
iiis.tsinghua.edu.cn
tv.tsinghua.edu.cn
sklt.tsinghua.edu.cn
yz.tsinghua.edu.cn
riit.tsinghua.edu.cn
cess.tsinghua.edu.cn
career.tsinghua.edu.cn
hep.tsinghua.edu.cn
its.tsinghua.edu.cn
rd.tsinghua.edu.cn
yqgx.tsinghua.edu.cn
yqhosp.tsinghua.edu.cn
astro.tsinghua.edu.cn
biomed.tsinghua.edu.cn
chem.tsinghua.edu.cn
me.tsinghua.edu.cn
dae.tsinghua.edu.cn
cqi.tsinghua.edu.cn
learn.tsinghua.edu.cn
xsg.tsinghua.edu.cn
id.tsinghua.edu.cn
mass.tsinghua.edu.cn
50.tsinghua.edu.cn
hy.tsinghua.edu.cn
iptu.tsinghua.edu.cn
ott.tsinghua.edu.cn
thtm.tsinghua.edu.cn
gclx.tsinghua.edu.cn
math.tsinghua.edu.cn
cadtc.tsinghua.edu.cn
iccm.tsinghua.edu.cn
itc.tsinghua.edu.cn
goglobal.tsinghua.edu.cn
summer.tsinghua.edu.cn
qiyuan.tsinghua.edu.cn
pt.tsinghua.edu.cn
pm.tsinghua.edu.cn
meng.tsinghua.edu.cn
aqjy.tsinghua.edu.cn
gix.tsinghua.edu.cn
search.tsinghua.edu.cn
csai.tsinghua.edu.cn
bkjxpg.tsinghua.edu.cn
qhfx.tsinghua.edu.cn
speech.tsinghua.edu.cn
tyzx.tsinghua.edu.cn
zhifu.tsinghua.edu.cn
dest.tsinghua.edu.cn
smarx.tsinghua.edu.cn
mailoa.tsinghua.edu.cn
xlzx.tsinghua.edu.cn
cmtest.tsinghua.edu.cn
thss.tsinghua.edu.cn
arts.tsinghua.edu.cn
arch.tsinghua.edu.cn
rwxy.tsinghua.edu.cn
castu.tsinghua.edu.cn
narl.tsinghua.edu.cn
nmgroup.tsinghua.edu.cn
m.tsinghua.edu.cn
93001.tsinghua.edu.cn
olugi.tsinghua.edu.cn
dfll.tsinghua.edu.cn
coach.tsinghua.edu.cn
cppark.tsinghua.edu.cn
mta0.tsinghua.edu.cn
heat.tsinghua.edu.cn
```

> PS : 结果会自动保存在当前目录的 `sub_domain.txt`
