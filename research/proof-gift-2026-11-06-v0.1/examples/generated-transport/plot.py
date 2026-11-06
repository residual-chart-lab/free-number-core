"""Presentation of exact outputs and the nonuniqueness certificate."""
from pathlib import Path
from fractions import Fraction
import argparse,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

parser=argparse.ArgumentParser();parser.add_argument('--run',type=Path,required=True);args=parser.parse_args()
for candidate in ['C:/Windows/Fonts/meiryo.ttc','C:/Windows/Fonts/YuGothM.ttc']:
    if Path(candidate).exists():
        prop=font_manager.FontProperties(fname=candidate);font_manager.fontManager.addfont(candidate);plt.rcParams['font.family']=prop.get_name();break
plt.rcParams['axes.unicode_minus']=False
c=json.loads((args.run/'EXACT_CERTIFICATE.json').read_bytes())
values=[float(Fraction(c['cases'][n]['response'])) for n in ['constant_axis','forward_triangle','reverse_triangle']]
amb=[float(Fraction(c['nonuniqueness'][n])) for n in ['minimum_cargo_response','compatible_twisted_cargo_response']]
fig,axes=plt.subplots(1,2,figsize=(11,5.3));fig.subplots_adjust(top=.76,bottom=.17,left=.08,right=.98,wspace=.32)
fig.suptitle('自由数の応答から、運搬を構成する\n条件：共通の比較枠 ＋ 余分なひねりを加えない',fontsize=12,y=.965)
axes[0].bar(range(3),values,color=['#999999','#3274a1','#e1812c'])
axes[0].set_xticks(range(3),['向きは一定','順回り','逆回り'],fontsize=10)
axes[0].set_title('入力の残差から運搬を計算',fontsize=11)
axes[0].set_ylabel('運ばれた残差の応答')
axes[1].bar(range(2),amb,color=['#999999','#55a868'],width=.55)
axes[1].set_xticks(range(2),['最小の運び方','別の適合するひねり'],fontsize=9)
axes[1].set_title('同じ入力だけでは一意に決まらない',fontsize=11)
axes[1].set_ylabel('共通の測り方への応答')
for ax in axes:
    ax.axhline(0,color='#444',lw=.8);ax.grid(axis='y',alpha=.2);ax.set_ylim(-2.3,2.3)
fig.savefig(args.run/'generated-transport.png',dpi=160)
fig.savefig(args.run/'generated-transport.svg')
