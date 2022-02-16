from fpdf import FPDF

title = 'Lockdown: Um Método Eficiente no combate ao Covid-19'


class PDF(FPDF):

    def header(self):
        pdf.set_font('Times', '', 18)
        pdf.cell(-200,0, txt='Gabriel Lucas Colangelo Mendes')
        self.ln(10)
        self.image('kick.png',185,4, 26)
        self.set_font('Times', 'B', 18)
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)
        self.cell(title_w, 10, title,align='C')
        self.ln(20)
  

    def text_body(self, name):
        with open(name, 'rb') as fh:
         txt = fh.read().decode('utf-8')
        self.set_font('times', '', 14)
        self.multi_cell(0, 5, txt)
        self.ln()


    def footer(self):
        self.set_y(-15)
        self.set_font('Times', 'B',12)
        self.cell(0, 20, f'Gabriel Lucas Colangelo Mendes, 2022', align='C')


pdf = PDF('P', 'mm', 'Letter')

pdf.alias_nb_pages()

pdf.set_auto_page_break(auto = True, margin = 15)

pdf.add_page()
pdf.image(name="graficos.png", w=230, h=150, y=120, x=-5)

pdf.text_body('chp1.txt')

pdf.output('Relatório.pdf')
