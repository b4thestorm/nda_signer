from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch


class NDA():
    '''
        This class is responsible for overlaying signatures on selected generated NDA PDF's

        nda_object = NDA("arnolds_agreement")
        nda_object.select_template("nda_agreement")
        nda_object.sign("arnolds_signature.jpg")
    '''
    
    def __init__(self, filename):
        '''
            Reportlab Canvas Constructor - https://www.reportlab.com/docs/reportlab-userguide.pdf
            ( filename, pagesize=(595.27,841.89), bottomup = 1, pageCompression=0, encoding=rl_config.defaultEncoding, verbosity=0, encrypt=None):
        '''
        self.canvas = Canvas(filename, pagesize=(8.5 * inch, 11 * inch), bottomup=0)

    def select_template(self, filename):
        pass

    def sign(self, signature):
        pass


if __name__ == '__main__':
    pdf = NDA('example.pdf')
    print(f"invoking canvas __to_s  and display to console {pdf}")

