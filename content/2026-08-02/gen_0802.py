import os, subprocess, tempfile
from PIL import Image

OUT = "/home/user/MrMinor1/content/2026-08-02/slides-bosstaxpro"
CHROMIUM = "/opt/pw-browsers/chromium"

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1200px;background:#050607;color:#fff;
 font-family:'DejaVu Sans',sans-serif;position:relative;overflow:hidden}
/* warm corner light, like the brand banner */
.glow{position:absolute;inset:0;background:
  radial-gradient(1100px 620px at 88% -8%, rgba(217,153,32,.30), rgba(217,153,32,0) 62%),
  radial-gradient(760px 520px at -12% 108%, rgba(217,153,32,.13), rgba(217,153,32,0) 60%);}
.grain{position:absolute;inset:0;opacity:.5;background-image:
  repeating-linear-gradient(0deg, rgba(255,255,255,.020) 0 1px, rgba(0,0,0,0) 1px 3px),
  repeating-linear-gradient(90deg, rgba(255,255,255,.014) 0 1px, rgba(0,0,0,0) 1px 3px);}
.topbar{position:absolute;top:0;left:0;right:0;height:9px;
 background:linear-gradient(90deg,#8A6612,#F5C542 42%,#D99920 62%,#8A6612)}
.pad{position:absolute;inset:0;padding:78px 88px 250px 88px;display:flex;flex-direction:column}
.kicker{font-size:26px;font-weight:800;letter-spacing:8px;text-transform:uppercase;
 background:linear-gradient(180deg,#F7D064,#C68718);-webkit-background-clip:text;
 -webkit-text-fill-color:transparent}
.gold{background:linear-gradient(180deg,#FBE28C 4%,#E6B33A 34%,#D99920 58%,#A8761A 100%);
 -webkit-background-clip:text;-webkit-text-fill-color:transparent}
.chrome{background:linear-gradient(180deg,#FFFFFF 6%,#DCE6EF 34%,#9DAEBE 62%,#F2F6FA 100%);
 -webkit-background-clip:text;-webkit-text-fill-color:transparent}
.h1{font-size:84px;font-weight:800;line-height:1.05;letter-spacing:-1.5px}
.h2{font-size:64px;font-weight:800;line-height:1.1;letter-spacing:-1px}
.sub{font-size:37px;line-height:1.42;color:rgba(233,238,244,.80)}
.rule{height:2px;background:linear-gradient(90deg,#D99920,rgba(217,153,32,.06));margin:26px 0}
.pill{display:inline-block;font-weight:800;font-size:34px;letter-spacing:3px;color:#0A0A0A;
 padding:21px 44px;border-radius:999px;
 background:linear-gradient(180deg,#FBE28C,#E0AC2C 52%,#B98717)}
.card{background:linear-gradient(180deg,rgba(255,255,255,.055),rgba(255,255,255,.018));
 border:2px solid rgba(217,153,32,.55);border-radius:24px;padding:34px 34px}
.card .lbl{font-size:24px;font-weight:800;letter-spacing:5px;text-transform:uppercase}
.card .val{font-size:46px;font-weight:800;margin-top:12px;line-height:1.08}
.card .note{font-size:28px;color:rgba(233,238,244,.78);margin-top:14px;line-height:1.38}
.row{display:flex;gap:26px}.row>*{flex:1}
.badge{width:104px;height:104px;border-radius:50%;color:#0A0A0A;font-size:44px;font-weight:800;
 display:flex;align-items:center;justify-content:center;
 background:linear-gradient(180deg,#FBE28C,#DFA92A 55%,#B07F16)}
.tl{position:relative;height:8px;background:rgba(255,255,255,.16);border-radius:4px;margin-top:64px}
.tl .fill{position:absolute;left:0;top:0;bottom:0;width:16%;border-radius:4px;
 background:linear-gradient(90deg,#B98717,#F5C542)}
.dot{position:absolute;top:-18px;width:44px;height:44px;border-radius:50%;
 background:linear-gradient(180deg,#FBE28C,#D99920);border:7px solid #050607}
.dotO{position:absolute;top:-18px;width:44px;height:44px;border-radius:50%;
 background:#050607;border:6px solid rgba(233,238,244,.42)}
.tlab{position:absolute;top:54px;font-size:27px;font-weight:800;transform:translateX(-50%);
 text-align:center;width:250px;line-height:1.25}
.vs{display:flex;border:2px solid rgba(217,153,32,.5);border-radius:24px;overflow:hidden}
.vs>div{flex:1;padding:38px 32px}
.vs .a{background:linear-gradient(180deg,rgba(217,153,32,.20),rgba(217,153,32,.05))}
.vs .b{background:rgba(255,255,255,.03)}
.vs .t{font-size:31px;font-weight:800;letter-spacing:4px;text-transform:uppercase}
.vs .n{font-size:90px;font-weight:800;line-height:1;margin:12px 0 6px}
.vs .d{font-size:27px;color:rgba(233,238,244,.80);line-height:1.35}
.foot{position:absolute;left:88px;right:88px;bottom:172px;font-size:27px;
 display:flex;justify-content:space-between;align-items:center;color:rgba(233,238,244,.66)}
.foot .fr{position:absolute;left:0;right:0;top:-30px;height:2px;
 background:linear-gradient(90deg,rgba(217,153,32,.75),rgba(217,153,32,.06))}
.wm{font-weight:800;letter-spacing:3px}
.cnt{position:absolute;top:70px;right:88px;font-size:25px;font-weight:800;letter-spacing:3px;
 color:rgba(233,238,244,.42)}
/* inverted gold slide */
body.inv{background:linear-gradient(150deg,#F3CB63 0%,#D99920 42%,#A87718 100%);color:#0A0A0A}
body.inv .glow,body.inv .grain{display:none}
body.inv .sub{color:rgba(10,10,10,.80)}
body.inv .topbar{background:#0A0A0A}
body.inv .foot{color:rgba(10,10,10,.72)}
body.inv .foot .fr{background:linear-gradient(90deg,rgba(10,10,10,.55),rgba(10,10,10,.05))}
body.inv .cnt{color:rgba(10,10,10,.5)}
"""

def page(inner, n, inv=False):
    b = "inv" if inv else ""
    layers = "" if inv else '<div class="glow"></div><div class="grain"></div>'
    foot = ('<div class="foot"><div class="fr"></div>'
            '<span class="wm">BOSS TAX PRO</span><span>helpmybizz.com</span></div>')
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head>"
            f"<body class='{b}'>{layers}<div class='topbar'></div>"
            f"<div class='cnt'>{n}/7</div><div class='pad'>{inner}</div>{foot}</body></html>")

S={}

S["01-cover"]=page("""
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
  <span class="kicker">Rank The Damage</span>
  <div class="h1 chrome" style="margin-top:26px">Four mistakes.<br>Same business.</div>
  <div class="h1 gold" style="margin-top:12px">Which costs<br>the most?</div>
  <div class="rule"></div>
  <div class="sub" style="max-width:860px">Guess your order before you swipe. Most people get the top two backwards.</div>
  <div style="margin-top:40px"><span class="pill">RANK THEM &rarr;</span></div>
</div>""",1)

S["02-setup"]=page("""
<span class="kicker">The same business, four ways to lose</span>
<div class="h2" style="margin-top:22px">One owner. <span class="gold">$12,000 owed.</span></div>
<div class="sub" style="margin-top:34px;font-size:36px">
<b class="gold">1.</b> Pays three months late<br><br>
<b class="gold">2.</b> Files three months late<br><br>
<b class="gold">3.</b> Never tracked 8,000 business miles<br><br>
<b class="gold">4.</b> Buys $10,000 of gear in December &ldquo;for the write-off&rdquo;</div>
<div class="sub" style="margin-top:28px;font-size:29px;opacity:.75">Put them in order, most expensive first. Then swipe.</div>""",2)

S["03-fourth"]=page("""
<span class="kicker">Cheapest &middot; 4th place</span>
<div style="display:flex;align-items:center;gap:30px;margin-top:26px">
  <div class="badge" style="font-size:34px">$180</div>
  <div class="h2" style="flex:1">Paying three<br><span class="gold">months late.</span></div>
</div>
<div class="card" style="margin-top:36px">
  <div class="note" style="font-size:32px;margin-top:0">The failure-to-pay penalty is <b class="gold">0.5% per month</b>. Three months on $12,000 is $180, plus interest.</div>
</div>
<div class="sub" style="margin-top:28px;font-size:32px">Unpleasant. Not catastrophic.</div>""",3)

S["04-third"]=page("""
<span class="kicker">3rd place &middot; ten times worse</span>
<div style="display:flex;align-items:center;gap:30px;margin-top:26px">
  <div class="badge" style="font-size:30px">$1,800</div>
  <div class="h2" style="flex:1">Filing three<br><span class="gold">months late.</span></div>
</div>
<div class="card" style="margin-top:36px">
  <div class="note" style="font-size:32px;margin-top:0">Failure-to-file is <b class="gold">5% per month</b>, capped at 25%. Same three months, same $12,000 &mdash; ten times the penalty.</div>
</div>
<div class="sub" style="margin-top:28px;font-size:32px">This is the one people get backwards. <b class="gold">File even if you can&rsquo;t pay.</b></div>""",4)

S["05-topTwo"]=page("""
<span class="kicker">The expensive two</span>
<div class="h2" style="margin-top:22px">Neither feels<br>like a <span class="gold">mistake.</span></div>
<div class="vs" style="margin-top:36px">
  <div class="b"><div class="t" style="color:rgba(233,238,244,.6)">2nd &middot; Untracked miles</div>
    <div class="n chrome" style="font-size:70px">~$2,150</div>
    <div class="d">8,000 miles &times; 72.5&cent; = $5,800 of deduction never claimed</div></div>
  <div class="a"><div class="t gold">1st &middot; December gear</div>
    <div class="n gold" style="font-size:70px">$6,300</div>
    <div class="d">$10,000 spent to save roughly $3,700 in tax</div></div>
</div>
<div class="sub" style="margin-top:30px;font-size:29px;opacity:.78">Tax figures are estimates at a 22% bracket plus self-employment tax.</div>""",5)

S["06-quote"]=page("""
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
  <div style="font-size:150px;line-height:.55;font-weight:800">&ldquo;</div>
  <div class="h1" style="font-size:72px;margin-top:20px">The penalties are<br>the cheap part.</div>
  <div class="h1" style="font-size:72px;margin-top:14px;opacity:.55">The habits are<br>what cost you.</div>
  <div style="margin-top:44px;font-size:28px;font-weight:800;letter-spacing:6px">&mdash; BOSS TAX PRO</div>
</div>""",6,inv=True)

S["07-cta"]=page("""
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
  <span class="kicker">Free 30-Minute Review</span>
  <div class="h1 gold" style="margin-top:24px">Which one is<br>costing you?</div>
  <div class="rule"></div>
  <div class="sub">Drop your ranking in the comments. Or we&rsquo;ll run the actual numbers on your business &mdash; mileage, timing, entity, all of it.</div>
  <div style="margin-top:38px"><span class="pill">HELPMYBIZZ.COM</span></div>
</div>""",7)

os.makedirs(OUT, exist_ok=True)
for name, html in S.items():
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html); src=f.name
    dest=os.path.join(OUT,name+".png")
    subprocess.run([CHROMIUM,"--headless=new","--no-sandbox","--disable-gpu",
        "--force-device-scale-factor=1","--hide-scrollbars",
        "--window-size=1080,1200",f"--screenshot={dest}",f"file://{src}"],
        check=True,capture_output=True)
    im=Image.open(dest); im.crop((0,0,1080,1080)).save(dest)
    print("wrote",name)
