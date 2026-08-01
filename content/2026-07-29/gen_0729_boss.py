import os, subprocess, tempfile
from PIL import Image

OUT = "/home/user/MrMinor1/content/2026-07-29/slides-bosstaxpro"
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
  <span class="kicker">Diagnose It</span>
  <div class="h1 chrome" style="margin-top:28px">What&rsquo;s your biggest</div>
  <div class="h1 gold" style="margin-top:10px">tax headache?</div>
  <div class="rule"></div>
  <div class="sub" style="max-width:860px">Pick your letter. We&rsquo;ll tell you what it usually means &mdash; and the fix.</div>
  <div style="margin-top:44px"><span class="pill">A, B, C OR D &rarr;</span></div>
</div>""",1)

S["02-a"]=page("""
<div style="display:flex;align-items:center;gap:32px">
  <div class="badge">A</div>
  <div class="h2" style="flex:1">&ldquo;Quarterlies<br><span class="gold">confuse me.&rdquo;</span></div>
</div>
<div class="card" style="margin-top:38px">
  <div class="lbl gold">Usual diagnosis</div>
  <div class="note" style="font-size:32px;margin-top:14px">Nobody ever calculated your <b>safe harbor number</b>. It&rsquo;s one figure &mdash; pay it and underpayment penalties can&rsquo;t touch you.</div>
</div>
<div class="sub" style="margin-top:28px;font-size:32px">The confusion disappears the moment someone runs it. Once a year.</div>""",2)

S["03-b"]=page("""
<div style="display:flex;align-items:center;gap:32px">
  <div class="badge">B</div>
  <div class="h2" style="flex:1">&ldquo;My books are<br><span class="gold">months behind.&rdquo;</span></div>
</div>
<div class="card" style="margin-top:38px">
  <div class="lbl gold">Usual diagnosis</div>
  <div class="note" style="font-size:32px;margin-top:14px">Your system is too manual. <b>Catching up isn&rsquo;t the fix</b> &mdash; auto-categorisation plus one 20-minute weekly habit is.</div>
</div>
<div class="sub" style="margin-top:28px;font-size:32px">Heroic weekend catch-ups always relapse. The workflow that caused it is untouched.</div>""",3)

S["04-c"]=page("""
<div style="display:flex;align-items:center;gap:32px">
  <div class="badge">C</div>
  <div class="h2" style="flex:1">&ldquo;No idea what<br><span class="gold">I&rsquo;ll owe.&rdquo;</span></div>
</div>
<div class="card" style="margin-top:38px">
  <div class="lbl gold">Usual diagnosis</div>
  <div class="note" style="font-size:32px;margin-top:14px">You&rsquo;ve never had a <b>mid-year projection</b>. April isn&rsquo;t unknowable &mdash; nobody is scheduled to work it out.</div>
</div>
<div class="sub" style="margin-top:28px;font-size:32px">Thirty minutes with your first-half numbers turns a mystery into a plan.</div>""",4)

S["05-d"]=page("""
<div style="display:flex;align-items:center;gap:32px">
  <div class="badge">D</div>
  <div class="h2" style="flex:1">&ldquo;Should I be an<br><span class="gold">S-Corp already?&rdquo;</span></div>
</div>
<div class="card" style="margin-top:38px">
  <div class="lbl gold">Usual diagnosis</div>
  <div class="note" style="font-size:32px;margin-top:14px">Nobody ran <b>your</b> break-even. It&rsquo;s arithmetic &mdash; payroll cost against self-employment tax saved &mdash; specific to your numbers.</div>
</div>
<div class="sub" style="margin-top:28px;font-size:32px">Everyone at the barbecue has an opinion. None of them have your P&amp;L.</div>""",5)

S["06-quote"]=page("""
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
  <div style="font-size:150px;line-height:.55;font-weight:800">&ldquo;</div>
  <div class="h1" style="font-size:76px;margin-top:20px">Every tax headache<br>is a system</div>
  <div class="h1" style="font-size:76px;margin-top:12px;opacity:.55">nobody built yet.</div>
  <div style="margin-top:46px;font-size:28px;font-weight:800;letter-spacing:6px">&mdash; BOSS TAX PRO</div>
</div>""",6,inv=True)

S["07-cta"]=page("""
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
  <span class="kicker">Free 30-Minute Review</span>
  <div class="h1 gold" style="margin-top:24px">Tell us your letter.</div>
  <div class="rule"></div>
  <div class="sub">None of these are character flaws. They&rsquo;re a number, a workflow, a checkpoint and a model &mdash; and every one of them is buildable.</div>
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
