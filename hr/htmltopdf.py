import pdfkit


def html2pdf(url, userid):
	config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
	pdf = pdfkit.from_url(
		'http://%s/resume/?vid=%s' % (url, userid),
		False,
		configuration=config)
	return pdf
