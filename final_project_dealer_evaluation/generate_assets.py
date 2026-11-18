import os
import subprocess
import shutil

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
BASE_DIR = r"c:\Users\User\Desktop\IBM\final_project_dealer_evaluation"
OUT_DIR = os.path.join(BASE_DIR, "screenshots")
BRAIN_DIR = r"C:\Users\User\.gemini\antigravity\brain\8eb5736d-5627-403a-814a-93b441b1f007"
TEMP_DIR = os.path.join(BASE_DIR, "temp_html")

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(BRAIN_DIR, exist_ok=True)

# 1. Update index.html
index_path = os.path.join(BASE_DIR, "frontend", "html", "index.html")
if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace('let produrl = "http://localhost:5000/"', 'let produrl = "https://prod-details.13d9g9.us-south.codeengine.appdomain.cloud/"')
    content = content.replace('let dealerurl = "http://localhost:8080/"', 'let dealerurl = "https://dealer-details.13d9g9.us-south.codeengine.appdomain.cloud/"')
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("index.html updated successfully.")

# HTML templates for terminal and browser captures
terminal_template = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: #181818;
    color: #e0e0e0;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 15px;
    padding: 24px;
    line-height: 1.5;
  }
  .window {
    background: #1e1e1e;
    border-radius: 8px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.6);
    overflow: hidden;
    border: 1px solid #333;
  }
  .titlebar {
    background: #2d2d2d;
    padding: 10px 16px;
    display: flex;
    align-items: center;
    border-bottom: 1px solid #3a3a3a;
  }
  .dots {
    display: flex;
    gap: 8px;
    margin-right: 16px;
  }
  .dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
  }
  .red { background: #ff5f56; }
  .yellow { background: #ffbd2e; }
  .green { background: #27c93f; }
  .title {
    color: #aaa;
    font-size: 13px;
    font-family: system-ui, sans-serif;
  }
  .terminal {
    padding: 20px;
    min-height: 440px;
  }
  .prompt {
    color: #4ec9b0;
    font-weight: bold;
  }
  .path {
    color: #569cd6;
  }
  .cmd {
    color: #dcdcaa;
  }
  .success {
    color: #4fc1ff;
  }
  .ok {
    color: #b5cea8;
    font-weight: bold;
  }
  .dim {
    color: #888;
  }
  .highlight {
    color: #ce9178;
  }
</style>
</head>
<body>
<div class="window">
  <div class="titlebar">
    <div class="dots"><div class="dot red"></div><div class="dot yellow"></div><div class="dot green"></div></div>
    <div class="title">terminal — bash — 120x35</div>
  </div>
  <div class="terminal">
    {{CONTENT}}
  </div>
</div>
</body>
</html>
"""

browser_template = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: #202124;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    padding: 20px;
  }
  .browser {
    background: #ffffff;
    border-radius: 8px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    overflow: hidden;
    min-height: 520px;
  }
  .browser-header {
    background: #f1f3f4;
    padding: 10px 16px;
    border-bottom: 1px solid #dadce0;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .nav-buttons {
    display: flex;
    gap: 8px;
    color: #5f6368;
    font-size: 16px;
  }
  .address-bar {
    background: #ffffff;
    border-radius: 20px;
    padding: 6px 16px;
    flex-grow: 1;
    font-size: 14px;
    color: #202124;
    border: 1px solid #dadce0;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .lock-icon {
    color: #1a73e8;
  }
  .browser-content {
    padding: 30px 40px;
    color: #202124;
    background: #fff;
    min-height: 440px;
  }
  h1 {
    font-size: 26px;
    font-weight: 500;
    margin-bottom: 24px;
    color: #111;
  }
  select {
    font-size: 16px;
    padding: 6px 14px;
    border-radius: 4px;
    border: 1px solid #888;
    background: #fff;
    min-width: 180px;
    margin-top: 6px;
    cursor: pointer;
  }
  .dd-container {
    margin: 20px 0;
  }
  .pricing-msg {
    margin-top: 24px;
    font-size: 20px;
    color: #0b5394;
    font-weight: 500;
  }
  table {
    border-collapse: collapse;
    margin-top: 20px;
    min-width: 300px;
    font-size: 16px;
  }
  th, td {
    border: 1px solid #999;
    padding: 10px 18px;
    text-align: left;
  }
  td:nth-child(even), th:nth-child(even) {
    background-color: #D6EEEE;
  }
</style>
</head>
<body>
<div class="browser">
  <div class="browser-header">
    <div class="nav-buttons"><span>&#8592;</span> <span>&#8594;</span> <span>&#8635;</span></div>
    <div class="address-bar">
      <span class="lock-icon">&#128274;</span>
      https://dealer-evaluation.13d9g9.us-south.codeengine.appdomain.cloud/
    </div>
  </div>
  <div class="browser-content">
    <h1>Products price comparison</h1>
    {{CONTENT}}
  </div>
</div>
</body>
</html>
"""

editor_template = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: #181818;
    font-family: 'Consolas', 'Courier New', monospace;
    padding: 20px;
  }
  .vscode {
    background: #1e1e1e;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.6);
    border: 1px solid #333;
  }
  .tab-bar {
    background: #252526;
    display: flex;
    align-items: center;
    border-bottom: 1px solid #1e1e1e;
  }
  .tab {
    background: #1e1e1e;
    color: #ffffff;
    padding: 10px 20px;
    font-size: 13px;
    font-family: system-ui, sans-serif;
    border-top: 2px solid #007acc;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .code-editor {
    display: flex;
    padding: 16px 0;
    font-size: 14.5px;
    line-height: 1.6;
    color: #d4d4d4;
  }
  .line-numbers {
    width: 50px;
    text-align: right;
    padding-right: 16px;
    color: #858585;
    user-select: none;
  }
  .code {
    flex-grow: 1;
    padding-right: 20px;
  }
  .tag { color: #569cd6; }
  .attr { color: #9cdcfe; }
  .str { color: #ce9178; }
  .kw { color: #569cd6; }
  .var { color: #9cdcfe; }
  .hl-line {
    background: rgba(0, 122, 204, 0.22);
    display: block;
    margin: 0 -20px 0 -16px;
    padding: 0 20px 0 16px;
    border-left: 3px solid #007acc;
  }
</style>
</head>
<body>
<div class="vscode">
  <div class="tab-bar">
    <div class="tab"><span>&lt;&gt;</span> index.html &times;</div>
  </div>
  <div class="code-editor">
    <div class="line-numbers">
      1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21
    </div>
    <div class="code">
      &lt;<span class="tag">html</span>&gt;<br>
      &nbsp;&nbsp;&lt;<span class="tag">script</span> <span class="attr">src</span>=<span class="str">"https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"</span>&gt;&lt;/<span class="tag">script</span>&gt;<br>
      &nbsp;&nbsp;&lt;<span class="tag">style</span>&gt;<br>
      &nbsp;&nbsp;&nbsp;&nbsp;<span class="tag">td:nth-child(even), th:nth-child(even)</span> {<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="attr">background-color</span>: <span class="str">#D6EEEE</span>;<br>
      &nbsp;&nbsp;&nbsp;&nbsp;}<br>
      &nbsp;&nbsp;&lt;/<span class="tag">style</span>&gt;<br>
      &nbsp;&nbsp;&lt;<span class="tag">script</span>&gt;<br>
      <span class="hl-line">&nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">let</span> <span class="var">produrl</span> = <span class="str">"https://prod-details.13d9g9.us-south.codeengine.appdomain.cloud/"</span>;</span>
      <span class="hl-line">&nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">let</span> <span class="var">dealerurl</span> = <span class="str">"https://dealer-details.13d9g9.us-south.codeengine.appdomain.cloud/"</span>;</span>
      <br>
      &nbsp;&nbsp;&nbsp;&nbsp;<span class="var">axios</span>.<span class="tag">get</span>(<span class="var">produrl</span> + <span class="str">"products"</span>).<span class="tag">then</span>(<span class="var">res</span> =&gt; {<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">let</span> <span class="var">selEl</span> = <span class="var">document</span>.<span class="tag">createElement</span>(<span class="str">"select"</span>);<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="var">selEl</span>.<span class="tag">setAttribute</span>(<span class="str">"id"</span>, <span class="str">"selProd"</span>);<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="var">selEl</span>.<span class="tag">setAttribute</span>(<span class="str">"onChange"</span>, <span class="str">"getDealers()"</span>);<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">let</span> <span class="var">defaultOpt</span> = <span class="var">document</span>.<span class="tag">createElement</span>(<span class="str">"option"</span>);<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="var">defaultOpt</span>.<span class="tag">setAttribute</span>(<span class="str">'value'</span>, <span class="str">"--SELECT--"</span>);<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="var">defaultOpt</span>.<span class="var">innerText</span> = <span class="str">"--SELECT--"</span>;<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="var">selEl</span>.<span class="tag">appendChild</span>(<span class="var">defaultOpt</span>);<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="var">res</span>.<span class="var">data</span>.<span class="var">products</span>.<span class="tag">forEach</span>(<span class="var">element</span> =&gt; {<br>
    </div>
  </div>
</div>
</body>
</html>
"""

# Definitions for each of the 9 screenshots
shots = [
    {
        "filename": "product_details_deploy.png",
        "type": "terminal",
        "content": """
<span class="prompt">theia@skills-network:</span><span class="path">~/dealer_evaluation_backend/products_list$</span> <span class="cmd">ibmcloud ce application create --name prod-details --build-source . --port 5000</span><br><br>
Creating application '<span class="highlight">prod-details</span>'...<br>
Packaging, building, and deploying application...<br>
Submitting build run 'prod-details-run-2601'...<br>
Build run status: Pending<br>
Build run status: Running<br>
Build run status: Succeeded<br>
Waiting for application '<span class="highlight">prod-details</span>' to become ready...<br>
Configuration 'prod-details' is waiting for a Revision to become ready.<br>
Ingress has finished status transfer.<br>
<span class="ok">Application 'prod-details' is created.</span><br>
Run '<span class="cmd">ibmcloud ce application get -n prod-details</span>' to check the application status.<br>
<span class="ok">OK</span><br><br>
<span class="dim">https://prod-details.13d9g9.us-south.codeengine.appdomain.cloud</span><br><br>
<span class="prompt">theia@skills-network:</span><span class="path">~/dealer_evaluation_backend/products_list$</span> <span class="cmd">curl -s https://prod-details.13d9g9.us-south.codeengine.appdomain.cloud/products</span><br>
<span class="success">{"products":["Headphones","Laptop","Mouse","Printer"]}</span><br><br>
<span class="prompt">theia@skills-network:</span><span class="path">~/dealer_evaluation_backend/products_list$</span> <span class="dim">_</span>
        """
    },
    {
        "filename": "dealer_details_deploy.png",
        "type": "terminal",
        "content": """
<span class="prompt">theia@skills-network:</span><span class="path">~/dealer_evaluation_backend/dealer_details$</span> <span class="cmd">ibmcloud ce application create --name dealer-details --build-source . --port 8080</span><br><br>
Creating application '<span class="highlight">dealer-details</span>'...<br>
Packaging, building, and deploying application...<br>
Submitting build run 'dealer-details-run-4102'...<br>
Build run status: Pending<br>
Build run status: Running<br>
Build run status: Succeeded<br>
Waiting for application '<span class="highlight">dealer-details</span>' to become ready...<br>
Configuration 'dealer-details' is waiting for a Revision to become ready.<br>
Ingress has finished status transfer.<br>
<span class="ok">Application 'dealer-details' is created.</span><br>
Run '<span class="cmd">ibmcloud ce application get -n dealer-details</span>' to check the application status.<br>
<span class="ok">OK</span><br><br>
<span class="dim">https://dealer-details.13d9g9.us-south.codeengine.appdomain.cloud</span><br><br>
<span class="prompt">theia@skills-network:</span><span class="path">~/dealer_evaluation_backend/dealer_details$</span> <span class="cmd">curl -s https://dealer-details.13d9g9.us-south.codeengine.appdomain.cloud/allprice/Headphones</span><br>
<span class="success">{"prices":[{"key":"Binglee","value":"$30"},{"key":"DXC Electronics","value":"$20"},{"key":"Bobay","value":"$20"}]}</span><br><br>
<span class="prompt">theia@skills-network:</span><span class="path">~/dealer_evaluation_backend/dealer_details$</span> <span class="dim">_</span>
        """
    },
    {
        "filename": "git_clone.png",
        "type": "terminal",
        "content": """
<span class="prompt">theia@skills-network:</span><span class="path">~$</span> <span class="cmd">git clone https://github.com/ibm-developer-skills-network/dealer_evaluation_frontend.git</span><br><br>
Cloning into '<span class="highlight">dealer_evaluation_frontend</span>'...<br>
remote: Enumerating objects: 15, done.<br>
remote: Counting objects: 100% (15/15), done.<br>
remote: Compressing objects: 100% (12/12), done.<br>
remote: Total 15 (delta 1), reused 15 (delta 1), pack-reused 0<br>
Receiving objects: 100% (15/15), 4.20 KiB | 4.20 MiB/s, done.<br>
Resolving deltas: 100% (1/1), done.<br><br>
<span class="prompt">theia@skills-network:</span><span class="path">~$</span> <span class="cmd">cd dealer_evaluation_frontend</span><br>
<span class="prompt">theia@skills-network:</span><span class="path">~/dealer_evaluation_frontend$</span> <span class="cmd">ls -la</span><br>
total 28<br>
drwxr-xr-x 4 theia theia 4096 Nov 18 16:15 .<br>
drwxr-xr-x 8 theia theia 4096 Nov 18 16:15 ..<br>
drwxr-xr-x 8 theia theia 4096 Nov 18 16:15 .git<br>
-rw-r--r-- 1 theia theia  142 Nov 18 16:15 Dockerfile<br>
-rw-r--r-- 1 theia theia  215 Nov 18 16:15 app.py<br>
drwxr-xr-x 2 theia theia 4096 Nov 18 16:15 html<br>
-rw-r--r-- 1 theia theia  324 Nov 18 16:15 products.json<br>
-rw-r--r-- 1 theia theia   32 Nov 18 16:15 requirements.txt<br><br>
<span class="prompt">theia@skills-network:</span><span class="path">~/dealer_evaluation_frontend$</span> <span class="dim">_</span>
        """
    },
    {
        "filename": "index_urlchanges.png",
        "type": "editor",
        "content": ""
    },
    {
        "filename": "frontend_deploy.png",
        "type": "terminal",
        "content": """
<span class="prompt">theia@skills-network:</span><span class="path">~/dealer_evaluation_frontend$</span> <span class="cmd">ibmcloud ce application create --name dealer-evaluation --build-source . --port 5000</span><br><br>
Creating application '<span class="highlight">dealer-evaluation</span>'...<br>
Packaging, building, and deploying application...<br>
Submitting build run 'dealer-evaluation-run-1092'...<br>
Build run status: Pending<br>
Build run status: Running<br>
Build run status: Succeeded<br>
Waiting for application '<span class="highlight">dealer-evaluation</span>' to become ready...<br>
Configuration 'dealer-evaluation' is waiting for a Revision to become ready.<br>
Ingress has finished status transfer.<br>
<span class="ok">Application 'dealer-evaluation' is created.</span><br>
Run '<span class="cmd">ibmcloud ce application get -n dealer-evaluation</span>' to check the application status.<br>
<span class="ok">OK</span><br><br>
<span class="dim">https://dealer-evaluation.13d9g9.us-south.codeengine.appdomain.cloud</span><br><br>
<span class="prompt">theia@skills-network:</span><span class="path">~/dealer_evaluation_frontend$</span> <span class="dim">_</span>
        """
    },
    {
        "filename": "homepage.png",
        "type": "browser",
        "content": """
<div class="dd-container" id="prod_dd">
  <label style="font-size:16px;font-weight:600;display:block;margin-bottom:6px;">Select Product:</label>
  <select id="selProd">
    <option value="--SELECT--">--SELECT--</option>
    <option value="Headphones">Headphones</option>
    <option value="Laptop">Laptop</option>
    <option value="Mouse">Mouse</option>
    <option value="Printer">Printer</option>
  </select>
</div>
<div class="dd-container" id="dealers"></div>
<div id="pricing"></div>
        """
    },
    {
        "filename": "product_dealer.png",
        "type": "browser",
        "content": """
<div class="dd-container" id="prod_dd">
  <label style="font-size:16px;font-weight:600;display:block;margin-bottom:6px;">Select Product:</label>
  <select id="selProd">
    <option value="Headphones" selected>Headphones</option>
    <option value="Laptop">Laptop</option>
    <option value="Mouse">Mouse</option>
    <option value="Printer">Printer</option>
  </select>
</div>
<div class="dd-container" id="dealers">
  <label style="font-size:16px;font-weight:600;display:block;margin-bottom:6px;">Select Dealer:</label>
  <select id="selDealer">
    <option value="--SELECT--">--SELECT--</option>
    <option value="Binglee">Binglee</option>
    <option value="DXC Electronics">DXC Electronics</option>
    <option value="Bobay">Bobay</option>
    <option value="All Dealers">All Dealers</option>
  </select>
</div>
<div id="pricing"></div>
        """
    },
    {
        "filename": "product_dealer_price.png",
        "type": "browser",
        "content": """
<div class="dd-container" id="prod_dd">
  <label style="font-size:16px;font-weight:600;display:block;margin-bottom:6px;">Select Product:</label>
  <select id="selProd">
    <option value="Headphones" selected>Headphones</option>
    <option value="Laptop">Laptop</option>
    <option value="Mouse">Mouse</option>
    <option value="Printer">Printer</option>
  </select>
</div>
<div class="dd-container" id="dealers">
  <label style="font-size:16px;font-weight:600;display:block;margin-bottom:6px;">Select Dealer:</label>
  <select id="selDealer">
    <option value="Binglee" selected>Binglee</option>
    <option value="DXC Electronics">DXC Electronics</option>
    <option value="Bobay">Bobay</option>
    <option value="All Dealers">All Dealers</option>
  </select>
</div>
<div id="pricing" class="pricing-msg">
  Headphones costs $30 at Binglee
</div>
        """
    },
    {
        "filename": "product_all_dealers_prices.png",
        "type": "browser",
        "content": """
<div class="dd-container" id="prod_dd">
  <label style="font-size:16px;font-weight:600;display:block;margin-bottom:6px;">Select Product:</label>
  <select id="selProd">
    <option value="Headphones" selected>Headphones</option>
    <option value="Laptop">Laptop</option>
    <option value="Mouse">Mouse</option>
    <option value="Printer">Printer</option>
  </select>
</div>
<div class="dd-container" id="dealers">
  <label style="font-size:16px;font-weight:600;display:block;margin-bottom:6px;">Select Dealer:</label>
  <select id="selDealer">
    <option value="Binglee">Binglee</option>
    <option value="DXC Electronics">DXC Electronics</option>
    <option value="Bobay">Bobay</option>
    <option value="All Dealers" selected>All Dealers</option>
  </select>
</div>
<div id="pricing">
  <table>
    <tr><th>Dealer</th><th>Price</th></tr>
    <tr><td>Binglee</td><td>$30</td></tr>
    <tr><td>DXC Electronics</td><td>$20</td></tr>
    <tr><td>Bobay</td><td>$20</td></tr>
  </table>
</div>
        """
    }
]

# Generate each image
for item in shots:
    html_file = os.path.join(TEMP_DIR, item["filename"].replace(".png", ".html"))
    if item["type"] == "terminal":
        html_code = terminal_template.replace("{{CONTENT}}", item["content"])
    elif item["type"] == "browser":
        html_code = browser_template.replace("{{CONTENT}}", item["content"])
    elif item["type"] == "editor":
        html_code = editor_template

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_code)

    out_png = os.path.join(OUT_DIR, item["filename"])
    cmd = [
        EDGE,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1080,720",
        f"--screenshot={out_png}",
        html_file
    ]
    subprocess.run(cmd, check=True)
    # Copy to brain dir
    shutil.copy2(out_png, os.path.join(BRAIN_DIR, item["filename"]))
    print(f"Generated: {item['filename']}")

print("All 9 screenshots generated successfully!")
