from flask import Flask, request, jsonify
from playwright.async_api import async_playwright
import asyncio

app = Flask(**name**)

async def extract_video(url):
async with async_playwright() as p:
browser = await p.chromium.launch(
headless=True,
args=["--no-sandbox", "--disable-gpu"]
)
page = await browser.new_page()
await page.goto(url, wait_until="networkidle")

 
    videos = page.locator("video")
    count = await videos.count()

    for i in range(count):
        src = await videos.nth(i).get_attribute("src")
        if src and not src.startswith("blob:"):
            return src

    return None

@app.route("/")
def home():
return "Video extractor running. Use /extract?url=..."

@app.route("/extract")
def extract():
url = request.args.get("url")
if not url:
return jsonify({"error": "missing url"})

 
try:
    result = asyncio.run(extract_video(url))
    return jsonify({"video": result})
except Exception as e:
    return jsonify({"error": str(e)})
 

if **name** == "**main**":
app.run(host="0.0.0.0", port=8080)
