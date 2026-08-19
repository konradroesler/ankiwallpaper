import subprocess
from main import get_cards, get_svg_file_names, fname_for_latex

if __name__ == "__main__":
  # iterate through dirs in notes
  svg_file_names = get_svg_file_names()
  cards = get_cards()
  for i in range(len(cards)):
    front_svg_name = fname_for_latex(cards[i][0])
    back_svg_name = fname_for_latex(cards[i][1])
    render = (
      """import puppeteer from "puppeteer";
      import path from "path";
      import { fileURLToPath } from "url";

      const __filename = fileURLToPath(import.meta.url);
      const __dirname = path.dirname(__filename);

      const WIDTH = 1920;
      const HEIGHT = 1080;

      const browser = await puppeteer.launch();
      const page = await browser.newPage();

      await page.setViewport({
        width: WIDTH,
        height: HEIGHT,
        deviceScaleFactor: 2 // retina quality
      });

      await page.goto(`file://${__dirname}/template.html`, {
        waitUntil: "networkidle0"
      });

      await page.screenshot({
      """
              + f"""
        path: "./images/{i}.png",
      """
              + """
        clip: { x: 0, y: 0, width: WIDTH, height: HEIGHT }
      });

      await browser.close();
      """
      )
    template = (
              """<!DOCTYPE html>
      <html>
      <head>
        <meta charset="UTF-8" />
        <style>
          html, body {
            margin: 0;
            width: 100%;
            height: 100%;
          }

          body {
            background: #1e1e1e; /* OR background image below */
            /* background: url("background.png") center / cover no-repeat; */
            display: flex;
            justify-content: center;
            align-items: center;
          }

          .canvas {
            width: 1920px;
            height: 1080px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 24px;
          }

          img {
            max-width: 100%;
            height: auto;
          }

              svg text {
                  fill: white;
              }
        </style>
      </head>
      <body>
        <div class="canvas">
        """
              + f"""
          <img src="./svgs/{front_svg_name}" />
          <img src="./svgs/{back_svg_name}" />
          """
              + """
        </div>
      </body>
      </html>"""
        )
    with open("render.js", "w") as file:
        file.writelines(render)
    with open("template.html", "w") as file:
        file.writelines(template)
    subprocess.run(["node", "render.js"])