import os, subprocess, tempfile
from PIL import Image

OUT = "/home/user/MrMinor1/content/2026-07-31/slides-bosstaxpro"
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
  <span class="kicker">Section 280A(g)</span>
  <div class="h1 chrome" style="margin-top:28px">Your business can<br>rent your home.</div>
  <div class="h1 gold" style="margin-top:12px">You report $0<br>of that income.</div>
  <div class="rule"></div>
  <div class="sub" style="max-width:860px">It sounds like a loophole. It&rsquo;s four lines of the tax code &mdash; with conditions most people skip.</div>
  <div style="margin-top:42px"><span class="pill">THE REAL RULES &rarr;</span></div>
</div>""",1)

S["02-code"]=page("""
<span class="kicker">What the code actually says</span>
<div class="h2" style="margin-top:24px">Fewer than <span class="gold">15 days.</span></div>
<div class="card" style="margin-top:38px">
  <div class="lbl gold">IRC &sect;280A(g) &middot; IRS Topic 415</div>
  <div class="note" style="font-size:32px;margin-top:16px">If you use a dwelling as a residence and rent it for <b>fewer than 15 days</b> in the year, you <b class="gold">don&rsquo;t report the rental income</b> &mdash; and you don&rsquo;t deduct rental expenses.</div>
</div>
<div class="sub" style="margin-top:32px;font-size:34px">Fewer than 15 means <b class="gold">14 days or less</b>. Day 15 makes the whole thing taxable.</div>""",2)

S["03-sides"]=page("""
<span class="kicker">Why owners care</span>
<div class="h2" style="margin-top:24px">It works <span class="gold">both ways.</span></div>
<div class="row" style="margin-top:40px">
  <div class="card"><div class="lbl gold">Your side</div>
    <div class="val chrome">Tax-free</div>
    <div class="note">The rent your business pays you isn&rsquo;t reported as income.</div></div>
  <div class="card"><div class="lbl gold">Business side</div>
    <div class="val chrome">Deductible</div>
    <div class="note">A legitimate, reasonable rent is an ordinary business expense.</div></div>
</div>
<div class="sub" style="margin-top:34px;font-size:33px">Same dollars. Deducted once, taxed never &mdash; <b>if</b> it&rsquo;s done properly.</div>""",3)

S["04-rules"]=page("""
<span class="kicker">The homework nobody mentions</span>
<div class="h2" style="margin-top:22px">Four conditions.</div>
<div class="sub" style="margin-top:30px;font-size:35px">
<b class="gold">1.</b> A real business purpose &mdash; an actual meeting, not a paper one.<br><br>
<b class="gold">2.</b> A fair market rate, supported by written quotes from comparable venues.<br><br>
<b class="gold">3.</b> Documentation &mdash; a rental agreement, an agenda, minutes, the payment.<br><br>
<b class="gold">4.</b> Fourteen days a year. Count them.</div>""",4)

S["05-not"]=page("""
<span class="kicker">Who this does NOT work for</span>
<div class="h2" style="margin-top:22px">Sole props and<br><span class="gold">single-member LLCs.</span></div>
<div class="card" style="margin-top:36px">
  <div class="note" style="font-size:32px;margin-top:0">With no separate entity, you&rsquo;d be paying rent to yourself. The deduction and the income are the same pocket &mdash; there is nothing to exclude.</div>
</div>
<div class="sub" style="margin-top:32px;font-size:33px">This needs a real payer: an <b class="gold">S-Corp, C-Corp or partnership</b> that&rsquo;s separate from you.</div>""",5)

S["06-quote"]=page("""
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
  <div style="font-size:150px;line-height:.55;font-weight:800">&ldquo;</div>
  <div class="h1" style="font-size:76px;margin-top:22px">It isn&rsquo;t a loophole.</div>
  <div class="h1" style="font-size:76px;margin-top:14px;opacity:.55">It&rsquo;s a rule with<br>homework attached.</div>
  <div style="margin-top:46px;font-size:28px;font-weight:800;letter-spacing:6px">&mdash; BOSS TAX PRO</div>
</div>""",6,inv=True)

S["07-cta"]=page("""
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
  <span class="kicker">Free 30-Minute Review</span>
  <div class="h1 gold" style="margin-top:24px">Does this one<br>apply to you?</div>
  <div class="rule"></div>
  <div class="sub">We&rsquo;ll check your entity, your meeting calendar and what a defensible rate looks like &mdash; then tell you straight if it isn&rsquo;t worth it.</div>
  <div style="margin-top:40px"><span class="pill">HELPMYBIZZ.COM</span></div>
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
