import PyPDF2

# use https://pythonhosted.org/PyPDF2/ to read documentations


def pdf_opener(location):
    """
    location --> file location of PDF


    opens a PDF file from a location. Decompiles pdf to readable information.
    returns a list of information
    item1 --> pages in the pdf
    item2 --> separate page objects
    item3 --> separate texts of pages
    """

    ret = [[], [], []]
    pdfFileObj = open(location, 'rb')
    pdf = PyPDF2.PdfFileReader(pdfFileObj)
    number_pages = pdf.numPages
    for page in range(0, number_pages):
        pg_obj = pdf.getPage(page)
        ret[0].append(page)
        ret[1].append(pg_obj)
        ret[2].append(pg_obj.extractText())
    return ret


def pdf_explorer(loc, single = False):
    """
    from a folder location,
    list all PDFs,
    return a list of extracted PDFs


    loc --> path to folder containing pdfs
    single --> single PDF or not
    returns --> list of lists of extracted PDFs
    """
    if single == True:
        return pdf_opener(folcer_loc)
    else:
        paths = [os.path.join(loc, pdf) for pdf in os.listdir(loc)]
        ret = []
        for pdf in paths:
            if ".pdf" in pdf:
                ret.append(pdf_opener(pdf))
        return ret
