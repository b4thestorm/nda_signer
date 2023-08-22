from pathlib import Path
import fitz
import pdb


#can get fields from pdf templates
#can pull in specific pdf templates
#can pull from s3
#can reach out to S3

class NDA(Object):
    '''
        This Module is responsible for writing signatures to PDF's and uploading to a Document Object Store
        PyMuPDF Docs:  https://pymupdf.readthedocs.io/en/latest/index.html
        
        example: 
        file = NDA("./assets/nda_basic.pdf")
        file.select_template("")
    '''

    FIELD_TYPE = {
        0: "PDF_WIDGET_TYPE_UNKNOWN",
        6: "PDF_WIDGET_TYPE_SIGNATURE",
        7: "PDF_WIDGET_TYPE_TEXT",
    }

    def __init__(self):
        self.file = None
      
    def find_pdf_template(self, relative_file_path):
        '''
            Finds file and stores file in memory
            returns:  void
        '''
        try:
            self.file = fitz.open(relative_file_path)
        except:
            print(f"No PDF file exists at {relative_file_path}")
    
    def _parse_fields_on_page(self, document, page_number):
        '''
            Given page number returns form fields
            returns:  list[field_types]
        '''
        if page_number > document.pages() || page_number < 0:
            raise ValueError("Page does not exist.")
        
        page = document.load_page(page_number)
        fields = [field for field in page.widgets()]
        return fields

    def detect_field_type(self, field)
        return FIELD_TYPE[field.field_type]

    def fill_out_field(self, field, input):
        if FIELD_TYPE[field.field_type] == "PDF_WIDGET_TYPE_TEXT":
            #inputs are dangerous, but this is a first take
            field.field_value = input
            field.update()

        file = self.file
        page = file.reload_page(page)
        file.need_appearances(value=True)
        file.save("./assets/nda_basic_copy.pdf")


if __name__ == '__main__':
    relative_file_path = Path('./assets/basic_nda.pdf')
    print(f"invoking canvas __to_s  and display to console {pdf}")
    
