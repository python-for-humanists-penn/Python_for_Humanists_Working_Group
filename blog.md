# A Spring Update: Pytesseract Success!

At the same time that libraries are digitizing more rare materials than ever, many of these scans are unsearchable images that remain largely inaccessible and cumbersome for large-scale analysis. For the past four weeks, the Working Group has begun a small project with the aim to create searchable text (.txt) files from rare books scans.   In defining the parameters of our project, we wanted to use Python's Pytesseract, an optical character recognition (OCR) tool, to make our own files searchable and analysis-ready.

To begin, we started with digitized image files available on Hathi Trust:

![Original Scan](https://github.com/python-for-humanists-penn/Python_for_Humanists_Working_Group/blob/master/blumenstrausse-1912-4.png?raw=true)

Then came the fun part! Over the course of three sessions, we were able to use Pytesseract in the code that we wrote to successfully create a .txt file from the image (.png) files: essentially, by using OCR we were able to extract the text from the scanned image. After running the file through our code, the following text resulted:

![Original OCR](https://github.com/python-for-humanists-penn/Python_for_Humanists_Working_Group/blob/master/blumenstrausse-1912-4-ocr.png?raw=true)

Our results were encouraging, but they weren't quite perfect, so we used ScanTailor software to clean up our original scan:

![Scantailor Scan](https://github.com/python-for-humanists-penn/Python_for_Humanists_Working_Group/blob/master/blumenstrausse_1912_4_scantailor.png?raw=true)

Then we ran the code again with the improved image and were able to improve the ability of Pytesseract to create a much more accurate representation of the text in the original image!

![Scantailor OCR](https://github.com/python-for-humanists-penn/Python_for_Humanists_Working_Group/blob/master/blumenstrausse_1912_4_scantailor_ocr.png?raw=true)
