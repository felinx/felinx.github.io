Title: 解决Kindle上PDF不能正常显示的问题
Date: 2017-11-14 12:00
Category: Python
Tags: PDF, pdf2imgpdf, img2pdf, Kindle, 乱码
Slug: 2017/11/pdf2imgpdf-pdf2img-img2pdf
Authors: 飞龙
Status: published

我平时用Kindle看书较多，遇到了一些PDF文件在Kindle上不能正常显示的问题，这类问题通常是因为PDF源文件里用了一些特殊字体或是一些扫描版的PDF，常见的现象是乱码或页面一片漆黑。

在Mac上有一个很讨巧的方法解决这个问题，用Mac自带的Preview的Export as PDF功能，将PDF源文件导出为一个新的PDF文件，Preview大致的原理就是将打开的Word、PPT、Excel、JPG、PNG、PDF等格式文件都视为或转为一页页的图片，然后以图片作为新的PDF的每一页的内容，因为是标准的图片所以到哪都能正确显示。但是，很不幸的是Preview在转换一些PDF文件的时候会无响应，搜索Preview export hang up或crash，发现吐槽这个问题的不止我一个，于是想用Python是否能解决下这个问题，参考了网上的一些实现，考察了多个库的实现方案后，找到了解决办法:


### 首先，将PDF转成一张张的图片

主要参考了[Convert specified pages from a PDF to png](https://gist.github.com/jrsmith3/9947838)，系统需要装imagemagick、ghostscript，Python需要[wand](https://github.com/dahlia/wand)、[PyPDF2](https://github.com/mstamy2/PyPDF2)两个库：

```python

    def pdf2img(src_pdf, pagenum=0, filename="filename", resolution=600):
        dst_pdf = PdfFileWriter()
        dst_pdf.addPage(src_pdf.getPage(pagenum))

        pdf_bytes = io.BytesIO()
        dst_pdf.write(pdf_bytes)
        pdf_bytes.seek(0)

        with Image(file=pdf_bytes, resolution=resolution) as img:
            img.convert("png")
            img.save(filename=filename)

```

其原理是用PyPDF2取出PDF的某一页，作为一个新的只有一页的PDF，写到一个BytesIO流中，再由wand库去读这个单页PDF中的内容生成一个图片文件，导出的图片和源PDF页面的内容一致，其中resolution的大小直接决定了导出的图片的画质，建议在300以上。

这里很有意思的是，我在转页数比较多的PDF的时候，发现Python占用的内存疯长，用[memory_profiler](https://pypi.python.org/pypi/memory_profiler)看了下，每转一个文件大概涨50M内存，问题出在`img.save`这一步，进一步发现是imagemagick的内存泄露，搜索imagemagick memory leak的问题也很多，这里就不再展开。

### 然后，图片再转回PDF

我先试了[FPDF](https://github.com/Setasign/FPDF)这个库，FPDF可以实现，但：

1. FPDF输入的图片大小必须和PDF的页面大小一致，如A4大小的PDF，图片宽高为(595.28, 841.89)，需要对图片做一次resize，画质非常受影响。
2. 不管前一步生成的是PNG还是JPEG格式的图片，用FPDF合成的PDF文件都特别很大，以我试的文件为例，从原PDF转完生成新的PDF大约大了10倍。
3. 合成速度比较慢

对FPDF画质不满意，后来我又试了下[img2pdf](https://pypi.python.org/pypi/img2pdf/0.2.4)，关键的就`img2pdf.convert(imgs, layout_fun=layout_fun)`这么一句，layout_fun是为了设置A4大小的PDF格式。

简单的转一个PDF文件的代码如下：

```python

    def convert(src, dest):
        # specify paper size (A4)
        src = escape.to_unicode(src)
        dest = escape.to_unicode(dest)

        a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
        layout_fun = img2pdf.get_layout_fun(a4inpt)

        src_pdf = PdfFileReader(src)
        num_pages = src_pdf.getNumPages()

        imgs = []
        with open(dest, "w") as des_pdf:
            for i in xrange(num_pages):
                filename = "/tmp/page-%s-%s.png" % (i + 1, uuid.uuid4().hex)
                imgs.append(filename)

                pdf2img(src_pdf, i, filename)

            des_pdf.write(img2pdf.convert(imgs, layout_fun=layout_fun))

            for filename in imgs:
                os.remove(filename)

        logging.info("%s converted to %s !" % (src, dest))

```

相比FPDF，img2pdf更优：

1. img2pdf不受图片尺寸限制，可以使用较高的resolution获得清晰的画质，生成的PDF清晰。
2. 图片若采用PNG格式，img2pdf转后的PDF文件很小，以我试的PDF文件为例，resolution设为600时，用PNG格式时大约是源PDF的两倍，而用JPG格式的话，大约是20倍，不可接受。
3. img2pdf的速度也很快，赞！

我一直在读《资治通鉴》，最近找到一版极好的影印版PDF，但在Kindle上PDF全黑看不了，困扰了我几天，终于一言不合就写代码，问题得到完美解决。

代码已开源出来，或许你也能用上 [pdf2imgpdf](https://github.com/felinx/pdf2imgpdf)

