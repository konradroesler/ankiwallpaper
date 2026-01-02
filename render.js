import puppeteer from "puppeteer";
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
        
          path: "./images/6f6c422f753076402f2d.png",
        
          clip: { x: 0, y: 0, width: WIDTH, height: HEIGHT }
        });

        await browser.close();
        