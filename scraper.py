from collections import namedtuple

CaseData = namedtuple('CaseData', ['parties', 'filing_date', 'next_hearing', 'pdf_url'])

def fetch_case_data(case_type, case_number, filing_year):
    # Simulated response
    data = CaseData(
        parties="Deepak Vishwakarma vs State",
        filing_date="12-Jan-2023",
        next_hearing="20-Aug-2025",
        pdf_url="https://districts.ecourts.gov.in/sites/default/files/sample.pdf"
    )
    raw_html = "<html><body>Simulated HTML from site</body></html>"
    return data, raw_html