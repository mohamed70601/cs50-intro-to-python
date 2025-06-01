from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font("Helvetica", "", 42)
        self.set_y(30)
        self.cell(0, 10, "CS50 Shirtificate", border=0, align="C")


def main():
    name = input("Name: ")

    pdf = PDF()
    pdf.add_page(
        orientation="portrait",
        format="a4",
    )
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(130)
    pdf.cell(0, 10, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
